import pg8000

def get_connection():
    return pg8000.connect(
        host="localhost",
        port=5432,
        database="qa_lab",
        user="qa_user",
        password="qa_pass"
    )