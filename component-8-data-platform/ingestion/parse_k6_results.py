import json
import uuid
from datetime import datetime
from db_client import get_connection

def parse_k6(file_path):
    with open(file_path) as f:
        data = json.load(f)

    test_id = str(uuid.uuid4())

    metrics = data["metrics"]

    avg = metrics["http_req_duration"]["avg"]
    p95 = metrics["http_req_duration"]["p(95)"]
    error_rate = metrics["http_req_failed"]["rate"]
    throughput = metrics["http_reqs"]["rate"]

    return {
        "id": test_id,
        "timestamp": datetime.now(),
        "avg": avg,
        "p95": p95,
        "error_rate": error_rate,
        "throughput": throughput
    }

def insert(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO load_tests (id, timestamp)
        VALUES (%s, %s)
    """, (data["id"], data["timestamp"]))

    cur.execute("""
        INSERT INTO metrics (test_id, avg_response_time, p95, error_rate, throughput)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["id"],
        data["avg"],
        data["p95"],
        data["error_rate"],
        data["throughput"]
    ))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    data = parse_k6("../component-7-load-testing/results/load-test.json")
    insert(data)