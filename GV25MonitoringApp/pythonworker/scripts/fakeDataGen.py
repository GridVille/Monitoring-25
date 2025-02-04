import psycopg

with psycopg.connect("postgresql://timescaledb:password@timescaledb:5432") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        t = 1
    # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        while True:
            cur.execute("INSERT INTO conditions (temperature, time, device, location) VALUES (%s, now(), 0,0)",100+t)

            # Query the database and obtain data as Python objects.
            #cur.execute("SELECT * FROM test")

            t += 1
            if t == 200: t = 100
