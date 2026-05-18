import psycopg2

conn = psycopg2.connect(
    host="awsprddbs4836.shared.sydney.edu.au",
    database="y26s1c9120_pkam0421",
    user="y26s1c9120_pkam0421",
    password="f7aHu9KZ"
)

cursor = conn.cursor()