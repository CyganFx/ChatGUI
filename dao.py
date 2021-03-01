import psycopg2 as pg

DB_URL = "postgres://postgres:duman070601@127.0.0.1:5432/python"

CREATE_TABLE_USERS = """CREATE TABLE IF NOT EXISTS users(
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(255)
                        );"""
CREATE_TABLE_USER_LOGS = """create table if not exists user_logs(
                        id int,
                        log varchar(255),
                        created timestamp, 
                        foreign key (id) references users(id)
                        );"""


def init_db():
    """Do only once!"""
    conn = pg.connect(DB_URL)
    cursor = conn.cursor()
    try:
        cursor.execute(CREATE_TABLE_USERS)
        cursor.execute("insert into users (username) values ('duman')")
        cursor.execute("insert into users (username) values ('shyngys')")
        cursor.execute("insert into users (username) values ('tleu')")
        cursor.execute(CREATE_TABLE_USER_LOGS)
        conn.commit()
    finally:
        if conn is not None:
            cursor.close()
            conn.close()


def is_authenticated(username):
    conn = pg.connect(DB_URL)
    cursor = conn.cursor()
    stmt = "SELECT id from users where username = %s"
    records = [username]
    cursor.execute(stmt, records)
    id = cursor.fetchone()
    if id is None:
        conn.close()
        return 0
    else:
        res = int(''.join(map(str, id)))
        conn.close()
        return res


def insert_log_info(id, log, created):
    conn = pg.connect(DB_URL)
    cursor = conn.cursor()
    try:
        stmt = """insert into user_logs values(
                                %s, %s, %s
                )"""
        records = (id, log, created)
        cursor.execute(stmt, records)
        conn.commit()

    finally:
        if conn is not None:
            cursor.close()
            conn.close()


def get_log_info_by_id(id) -> list:
    conn = pg.connect(DB_URL)
    cursor = conn.cursor()
    try:
        stmt = """select log, created from user_logs where id = %s"""
        record = [id]
        cursor.execute(stmt, record)
        records = cursor.fetchall()
        formatted_records = []

        for row in records:
            formatted_records.append(row[0])
            time = row[1]
            new_time = time.strftime("%H:%M:%S")
            formatted_records.append(new_time)

        return formatted_records

    finally:
        if conn is not None:
            cursor.close()
            conn.close()
