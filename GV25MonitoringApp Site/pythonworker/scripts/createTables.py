import psycopg

try: 
    with psycopg.connect("postgresql://timescaledb:password@timescaledb:5432") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute(
                    """CREATE TABLE conditions (
            time        TIMESTAMPTZ       NOT NULL,
            location    TEXT              NOT NULL,
            device      TEXT              NOT NULL,
            temperature DOUBLE PRECISION  NULL,
            humidity    DOUBLE PRECISION  NULL
            );"""
            )
            cur.execute("SELECT create_hypertable('conditions', 'time', if_not_exists => TRUE);")


except:
    pass