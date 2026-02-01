# no-spoilers-sports
A project trying to use AI to make a website that will give me sports information without spoilers


# Setup Venv
python3 -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Setup the DB
python3 bin/setup_db.py

# Update the DB
This can be run manually or be setup in a crontab
python3 bin/update_db.py

# Run the Application