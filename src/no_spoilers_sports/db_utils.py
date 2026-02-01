# Moved to src/no_spoilers_sports/db_utils.py
import sqlite3
from contextlib import closing
from configs.db_config import DB_PATH

def init_db():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS nba_games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_id TEXT,
                    away_team TEXT,
                    home_team TEXT,
                    away_score INTEGER,
                    home_score INTEGER,
                    status TEXT,
                    status_detail TEXT,
                    start_time TEXT,
                    away_logo TEXT,
                    home_logo TEXT,
                    UNIQUE(game_id)
                )
            ''')

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def get_nba_games_from_db(date):
    conn = get_db_connection()
    with conn:
        cur = conn.execute('''
            SELECT game_id, away_team, home_team, away_score, home_score, status, status_detail, start_time, away_logo, home_logo
            FROM nba_games
            WHERE date(datetime(start_time, '-5 hours')) = ?
        ''', (date,))
        games = [
            {
                'game_id': row[0],
                'away_team': row[1],
                'home_team': row[2],
                'away_score': row[3],
                'home_score': row[4],
                'status': row[5],
                'status_detail': row[6],
                'start_time': row[7],
                'away_logo': row[8],
                'home_logo': row[9],
            }
            for row in cur.fetchall()
        ]

        print(f"Retrieved {len(games)} NBA games from DB for date {date}")
    return games