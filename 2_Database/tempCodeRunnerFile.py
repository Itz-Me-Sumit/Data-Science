import psycopg2
import json

conn = None

def read_db_config(config_file="db_config.json"):
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
            print(f"Database Config Loaded from file : {config_file}")
        return config

    except Exception as e:
        print(f"Error Occured while reading file : {config_file} , Error: {e}")
        return None


def connect_to_postgres(db_name, user, password, host, port):

    connection = None

    try:
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        print(f"Connection To PostgreSQL DB ({db_name}) successful")
        return connection

    except Exception as e:
        print(f"Error Occured While Creating Connection to DB {db_name}, Error: {e}")
        return None


def execute_query(conn, query, params=None):

    cursor = None

    try:
        cursor = conn.cursor()

        cursor.execute(query, params)

        return cursor.fetchall()

    except Exception as e:
        print(f"Error Occured While Running Query , Error : {e}")
        return None

    finally:
        if cursor:
            cursor.close()


db_config = read_db_config()

print(db_config)

if db_config:

    DB_NAME = db_config.get("db_name")
    USER = db_config.get("user")
    PASSWORD = db_config.get("password")
    HOST = db_config.get("host")
    PORT = db_config.get("port")

    conn = connect_to_postgres(
        DB_NAME,
        USER,
        PASSWORD,
        HOST,
        PORT
    )

    print(conn)

query = "SELECT * FROM Album;"

if conn:

    result = execute_query(conn, query)

    if result is None:
        print("Result set is empty")

    else:

        for album_id, title, artist_id in result:

            print(
                f"Album Id: {album_id}, "
                f"Title: {title}, "
                f"Artist Id: {artist_id}"
            )

    conn.close()
    print("Connection Closed")