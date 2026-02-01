from src.no_spoilers_sports.db_utils import get_db_connection
from src.no_spoilers_sports.espn_score_fetcher import ESPNScoreFetcher

def upsert_nba_game(game):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO nba_games (game_id, away_team, home_team, away_score, home_score, status, status_detail, start_time, away_logo, home_logo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(game_id) DO UPDATE SET
                away_score=excluded.away_score,
                home_score=excluded.home_score,
                status=excluded.status,
                status_detail=excluded.status_detail,
                start_time=excluded.start_time,
                away_logo=excluded.away_logo,
                home_logo=excluded.home_logo
        ''', (
            game['gameId'],
            game['awayTeam']['name'],
            game['homeTeam']['name'],
            game['awayTeam']['score'],
            game['homeTeam']['score'],
            game['status'],
            game['status_detail'],
            game['startDate'],
            game['awayTeam']['logo'],
            game['homeTeam']['logo'],
        ))


if __name__ == "__main__":
    # Get today's date in 'YYYY-MM-DD' format
    from datetime import datetime
    today_str = datetime.now().strftime('%Y-%m-%d')

    # Fetch NBA scores for today
    fetcher = ESPNScoreFetcher()
    games = fetcher.get_nba_scores_by_date(today_str.replace('-', ''))
    for game in games:
        print(game)
        upsert_nba_game(game)