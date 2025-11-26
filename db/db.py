import sqlite3

class DatabaseManager:
    def __init__(self, db_name='Inlay_system.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.inlay_table_name = "deploying_soldiers"
    
    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS deploying_soldiers (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender INTEGER,
        citi TEXT NOT NULL,                    
        distance_from_Base INTEGER,
        assignment_status TEXT,
        residential_building TEXT,
        room INTEGER
     )''')

        self.conn.commit()
        self.conn.close()
    
    

    @staticmethod
    def add_soldiers_to_table(conn, table_name: str, rows: list[dict]):
        if not rows:
            return
        columns = rows[0].keys()
        placeholders = ", ".join(["?"] * len(columns))
        columns_sql = ", ".join([f'"{col}"' for col in columns])

        insert_sql = f'INSERT INTO "{table_name}" ({columns_sql}) VALUES ({placeholders})'

        values = [
        [row.get(col, "") for col in columns]
        for row in rows
        ]
        conn.executemany(insert_sql, values)
        conn.commit()




    def fetch_table_as_dicts(self, query: str) -> list[dict]:
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        col_names = [desc[0] for desc in self.cursor.description]
        result = []
        for row in rows:
            d = {col: (value if value is not None else "") for col, value in zip(col_names, row)}
            result.append(d)
        return result
    
    
    def get_occupancy_by_building(self, building):
        pass
    
    def get_waiting_list(self):
        pass
    
    def get_soldier_by_id(self, id):
        pass




        