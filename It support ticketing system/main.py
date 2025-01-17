import psycopg2

# Connect to the database
try:
    conn = psycopg2.connect(
        dbname="ticket_system",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    print("Connected to the database 'ticket_system' successfully.")
except psycopg2.OperationalError as e:
    print(f"Database connection failed: {e}")
    exit()

cursor = conn.cursor()

# Table creation queries
create_low_urgency_table = """
CREATE TABLE IF NOT EXISTS low_urgency (
    ticket_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    issue_description TEXT NOT NULL,
    department VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_medium_urgency_table = """
CREATE TABLE IF NOT EXISTS medium_urgency (
    ticket_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    issue_description TEXT NOT NULL,
    department VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_high_urgency_table = """
CREATE TABLE IF NOT EXISTS high_urgency (
    ticket_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    issue_description TEXT NOT NULL,
    department VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Alter table queries to add missing columns
alter_low_urgency_table = """
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'low_urgency' AND column_name = 'department'
    ) THEN
        ALTER TABLE low_urgency ADD COLUMN department VARCHAR(50) NOT NULL;
    END IF;
END $$;
"""

alter_medium_urgency_table = """
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'medium_urgency' AND column_name = 'department'
    ) THEN
        ALTER TABLE medium_urgency ADD COLUMN department VARCHAR(50) NOT NULL;
    END IF;
END $$;
"""

alter_high_urgency_table = """
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'high_urgency' AND column_name = 'department'
    ) THEN
        ALTER TABLE high_urgency ADD COLUMN department VARCHAR(50) NOT NULL;
    END IF;
END $$;
"""

# Execute queries to ensure tables exist and have correct schema
try:
    cursor.execute(create_low_urgency_table)
    cursor.execute(create_medium_urgency_table)
    cursor.execute(create_high_urgency_table)

    cursor.execute(alter_low_urgency_table)
    cursor.execute(alter_medium_urgency_table)
    cursor.execute(alter_high_urgency_table)

    conn.commit()
    print("Tables created or updated successfully.")
except psycopg2.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    try:
        cursor.close()
        conn.close()
        print("Database connection closed.")
    except psycopg2.Error as e:
        print(f"Error closing the connection: {e}")
