from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from app.utils import create_map_list

db = SQLAlchemy(app)


# Create database model
class Tournament(db.Model):
    __tablename__ = "tournaments"
    url = db.Column(db.String(120), primary_key=True, unique=True)
    tournament = db.Column(db.String(120))
    team1 = db.Column(db.String(120))
    team2 = db.Column(db.String(120))
    starter = db.Column(db.String(1))
    time = db.Column(db.Interval)
    timestamp = db.Column(db.DateTime)
    unbanned = db.Column(db.PickleType)
    team1bans = db.Column(db.PickleType)
    team2bans = db.Column(db.PickleType)

    def __init__(self, url, tournament, team1, team2, starter, time):
        self.url = url
        self.tournament = tournament
        self.team1 = team1
        self.team2 = team2
        self.starter = starter
        self.time = timedelta(seconds=time)
        self.timestamp = datetime.now()
        self.unbanned = create_map_list()
        self.team1bans = []
        self.team2bans = []

    def __repr__(self):
        return '<URL %r>' % self.url
