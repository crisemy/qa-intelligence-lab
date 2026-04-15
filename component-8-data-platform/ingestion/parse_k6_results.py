import json
import uuid
from datetime import datetime
from db_client import get_connection

def parse_k6(file_path):
    test_id = str(uuid.uuid4())

    durations = []
    errors = 0
    total_requests = 0

    with open(file_path) as f:
        for line in f:
            try:
                obj = json.loads(line)

                # Just point events
                if obj.get("type") != "Point":
                    continue

                metric = obj.get("metric")
                data = obj.get("data", {})

                # Request duration
                if metric == "http_req_duration":
                    durations.append(data.get("value", 0))

                # Request count and errors
                if metric == "http_reqs":
                    total_requests += 1
                    status = data.get("tags", {}).get("status")

                    if status and status.startswith("5"):
                        errors += 1

            except Exception:
                continue

    if not durations:
        raise ValueError("No duration data found")

    # Added metrics
    avg = sum(durations) / len(durations)
    sorted_durations = sorted(durations)
    p95 = sorted_durations[int(len(sorted_durations) * 0.95)]

    error_rate = errors / total_requests if total_requests > 0 else 0
    throughput = total_requests  # Simplified

    return {
        "id": test_id,
        "timestamp": datetime.now(),
        "avg": avg,
        "p95": p95,
        "error_rate": error_rate,
        "throughput": throughput,
        "total_requests": total_requests,
        "total_errors": errors
    }


def insert(data, test_type="load", error_probability=0.5, latency_ms=3000):
    conn = get_connection()
    cur = conn.cursor()

    # 1. Insert metadata
    cur.execute("""
        INSERT INTO load_tests (id, timestamp, test_type)
        VALUES (%s, %s, %s)
    """, (data["id"], data["timestamp"], test_type))

    # 2. Insert metrics
    cur.execute("""
        INSERT INTO metrics (
            test_id, avg_response_time, p95, error_rate, throughput, total_requests, total_errors
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data["id"],
        data["avg"],
        data["p95"],
        data["error_rate"],
        data["throughput"],
        data["total_requests"],
        data["total_errors"]
    ))

    # 3. Insert fault config (important for ML)
    cur.execute("""
        INSERT INTO fault_config (test_id, error_probability, latency_ms)
        VALUES (%s, %s, %s)
    """, (
        data["id"],
        error_probability,
        latency_ms
    ))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    file_path = "../../component-7-load-testing/results/load-test.ndjson"

    data = parse_k6(file_path)

    insert(
        data,
        test_type="load",            
        error_probability=0.5, 
        latency_ms=3000
    )

    print("✅ Data inserted successfully")