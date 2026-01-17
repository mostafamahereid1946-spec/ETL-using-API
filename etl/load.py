import sqlite3


def load_data(df):
    conn = sqlite3.connect("company.db")

    df.to_sql(
        "api_users",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
