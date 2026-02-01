import requests
from typing import List, Dict

class ESPNScoreFetcher:
    NFL_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    NHL_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard"
    NBA_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    MLB_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

    def get_nfl_scores_by_date(self, date: str) -> List[Dict]:
        """
        Get NFL game scores for a specific date.
        Args:
            date (str): Date in 'YYYYMMDD' format (e.g., '20260102')
        Returns:
            List[Dict]: List of games with their scores and details.
        """


        params = {"dates": date}
        response = requests.get(self.NFL_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        games = data.get("events", [])
        results = []
        for game in games:
            competition = game.get("competitions", [{}])[0]
            competitors = competition.get("competitors", [])
            teams = []
            home_team = None
            neutral_site = competition.get("neutralSite", False)
            for team in competitors:
                logo_url = ""
                print(team)
                if "logos" in team["team"] and team["team"]["logos"]:
                    logo_url = team["team"]["logos"][0]["href"]
                team_info = {
                    "name": team["team"]["displayName"],
                    "score": team["score"],
                    "winner": team.get("winner", False),
                    "home": team.get("homeAway", "") == "home",
                    "away": team.get("homeAway", "") == "away",
                    "logo": logo_url
                }
                if team_info["home"]:
                    home_team = team_info["name"]
                teams.append(team_info)
            results.append({
                "gameId": game.get("id"),
                "status": competition.get("status", {}).get("type", {}).get("description", ""),
                "startDate": competition.get("date", game.get("date", "")),
                "teams": teams,
                "homeTeam": home_team,
                "neutralSite": neutral_site
            })
        return results

    def get_nhl_scores_by_date(self, date: str) -> List[Dict]:
        """
        Get NHL game scores for a specific date.
        Args:
            date (str): Date in 'YYYYMMDD' format (e.g., '20260102')
        Returns:
            List[Dict]: List of games with their scores and details.
        """
        params = {"dates": date}
        response = requests.get(self.NHL_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        games = data.get("events", [])
        results = []
        for game in games:
            competition = game.get("competitions", [{}])[0]
            competitors = competition.get("competitors", [])
            teams = []
            home_team = None
            neutral_site = competition.get("neutralSite", False)
            for team in competitors:
                team_info = {
                    "name": team["team"]["displayName"],
                    "score": team["score"],
                    "winner": team.get("winner", False),
                    "home": team.get("homeAway", "") == "home",
                    "away": team.get("homeAway", "") == "away"
                }
                if team_info["home"]:
                    home_team = team_info["name"]
                teams.append(team_info)
            results.append({
                "gameId": game.get("id"),
                "status": competition.get("status", {}).get("type", {}).get("description", ""),
                "startDate": competition.get("date", game.get("date", "")),
                "teams": teams,
                "homeTeam": home_team,
                "neutralSite": neutral_site
            })
        return results

    def get_nba_scores_by_date(self, date: str) -> List[Dict]:
        """
        Get NBA game scores for a specific date.
        Args:
            date (str): Date in 'YYYYMMDD' format (e.g., '20260102')
        Returns:
            List[Dict]: List of games with their scores and details.
        """
        params = {"dates": date}
        response = requests.get(self.NBA_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        games = data.get("events", [])
        results = []
        for game in games:
            competition = game.get("competitions", [{}])[0]
            competitors = competition.get("competitors", [])
            home_team = None
            away_team = None
            for team in competitors:
                logo_url = ""
                team_obj = team.get("team", {})
                if "logos" in team_obj and team_obj["logos"]:
                    logo_url = team_obj["logos"][0].get("href", "")
                elif "logo" in team_obj:
                    logo_url = team_obj["logo"]
                team_info = {
                    "name": team_obj.get("displayName", ""),
                    "score": team.get("score", ""),
                    "winner": team.get("winner", False),
                    "home": team.get("homeAway", "") == "home",
                    "away": team.get("homeAway", "") == "away",
                    "logo": logo_url
                }
                if team_info["home"]:
                    home_team = team_info
                else:
                    away_team = team_info
                print(competition.get("status", {}))
            results.append({
                "gameId": game.get("id"),
                "status": competition.get("status", {}).get("type", {}).get("description", ""),
                "status_detail": competition.get("status", {}).get("type", {}).get("detail", ""),
                "startDate": competition.get("date", game.get("date", "")),
                "homeTeam": home_team,
                "awayTeam": away_team,
            })
        return results

    def get_mlb_scores_by_date(self, date: str) -> List[Dict]:
        """
        Get MLB game scores for a specific date.
        Args:
            date (str): Date in 'YYYYMMDD' format (e.g., '20260102')
        Returns:
            List[Dict]: List of games with their scores and details.
        """
        params = {"dates": date}
        response = requests.get(self.MLB_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        games = data.get("events", [])
        results = []
        for game in games:
            competition = game.get("competitions", [{}])[0]
            competitors = competition.get("competitors", [])
            teams = []
            home_team = None
            neutral_site = competition.get("neutralSite", False)
            for team in competitors:
                team_info = {
                    "name": team["team"]["displayName"],
                    "score": team["score"],
                    "winner": team.get("winner", False),
                    "home": team.get("homeAway", "") == "home",
                    "away": team.get("homeAway", "") == "away"
                }
                if team_info["home"]:
                    home_team = team_info["name"]
                teams.append(team_info)
            results.append({
                "gameId": game.get("id"),
                "status": competition.get("status", {}).get("type", {}).get("description", ""),
                "startDate": competition.get("date", game.get("date", "")),
                "teams": teams,
                "homeTeam": home_team,
                "neutralSite": neutral_site
            })
        return results

if __name__ == "__main__":
    # Example usage
    fetcher = ESPNScoreFetcher()
    date_str = "20250928"  # Example date
    try:
        nfl_games = fetcher.get_nfl_scores_by_date(date_str)
        if not nfl_games:
            print("No NFL games found for this date.")
        for game in nfl_games:
            print(game)
        
        nhl_games = fetcher.get_nhl_scores_by_date(date_str)
        if not nhl_games:
            print("No NHL games found for this date.")
        for game in nhl_games:
            print(game)

        nba_games = fetcher.get_nba_scores_by_date(date_str)
        if not nba_games:
            print("No NBA games found for this date.")
        for game in nba_games:
            print(game)

        mlb_games = fetcher.get_mlb_scores_by_date(date_str)
        if not mlb_games:
            print("No MLB games found for this date.")
        for game in mlb_games:
            print(game)
    except Exception as e:
        print(f"Error fetching scores: {e}")