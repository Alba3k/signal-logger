import sqlite3
import csv
import os
from datetime import datetime

class SignalLogger:
    def __init__(self, target="signals.db", table="signal_log", mode="sqlite"):
        self.target = target
        self.table = table
        self.mode = mode

        if self.mode == "sqlite":
            self.conn = sqlite3.connect(self.target)
            self._create_table()
        elif self.mode == "csv":
            if not os.path.exists(self.target):
                with open(self.target, "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["timestamp", "symbol", "signal", "strategy", "info"])

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            symbol TEXT,
            signal TEXT,
            strategy TEXT,
            info TEXT
        )""")
        self.conn.commit()

    def log_signal(self, timestamp=None, symbol="", signal="", strategy="", info=""):
        timestamp = timestamp or datetime.now().isoformat()
        row = (timestamp, symbol, signal, strategy, info)

        if self.mode == "sqlite":
            cursor = self.conn.cursor()
            cursor.execute(f"""INSERT INTO {self.table} 
                (timestamp, symbol, signal, strategy, info) VALUES (?, ?, ?, ?, ?)""", row)
            self.conn.commit()

        elif self.mode == "csv":
            with open(self.target, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
