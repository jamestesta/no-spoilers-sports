from flask import Flask, render_template, jsonify
from src.no_spoilers_sports.db_utils import init_db, get_nba_games_from_db
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nba_games')
def nba_games():
    today = datetime.now().strftime('%Y-%m-%d')
    games = get_nba_games_from_db(today)
    return jsonify(games)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
