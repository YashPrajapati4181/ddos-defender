import sqlite3
import threading
from datetime import datetime
from config import Config

class IPBlocker:
    def __init__(self):
        # Use thread-local storage
        self.local = threading.local()
    
    def _get_conn(self):
        if not hasattr(self.local, "conn"):
            self.local.conn = sqlite3.connect(
                'blocked_ips.db',
                check_same_thread=False  # Allow multi-thread access
            )
            self._create_table()
        return self.local.conn
    
    def _create_table(self):
        self._get_conn().execute('''
            CREATE TABLE IF NOT EXISTS blocked_ips (
                ip TEXT PRIMARY KEY,
                blocked_at TIMESTAMP,
                reason TEXT
            )
        ''')
        self._get_conn().commit()

    def block_ip(self, ip: str, reason: str):
        try:
            self._get_conn().execute(
                "INSERT INTO blocked_ips VALUES (?, ?, ?)",
                (ip, datetime.now(), reason)
            )
            self._get_conn().commit()
        except sqlite3.IntegrityError:
            pass

    def is_blocked(self, ip: str) -> bool:
        cursor = self._get_conn().execute(
            "SELECT 1 FROM blocked_ips WHERE ip = ?",
            (ip,)
        )
        return cursor.fetchone() is not None
