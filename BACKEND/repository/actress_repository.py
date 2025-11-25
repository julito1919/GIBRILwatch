from database import connection

def get_actress():
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM actress")
            return cur.fetchall()

