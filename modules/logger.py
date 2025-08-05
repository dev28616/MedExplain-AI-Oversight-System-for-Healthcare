# modules/logger.py

import sqlite3
import os
import datetime

def initialize_logger():
    conn = sqlite3.connect("log.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_event(module_name, item):
    timestamp = datetime.datetime.now().isoformat()
    conn = sqlite3.connect("log.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (event, timestamp) VALUES (?, ?)
    ''', (f"{module_name} - {item}", timestamp))
    conn.commit()
    conn.close()
