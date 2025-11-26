import sqlite3

class DatabaseManager:
    def __init__(self, db_name='Inlay_system.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
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
    
    def add_soldiers_to_table(self, soldiers:list):
        pass
    
    def get_occupancy_by_building(self, building):
        pass
    
    def get_waiting_list(self):
        pass
    
    def get_soldier_by_id(self, id):
        pass




        