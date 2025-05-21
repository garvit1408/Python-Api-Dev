from flask import Flask, jsonify, render_template, request
import ipl

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/teams")
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


@app.route("/api/teamVteam")
def teamVteamAPI():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    response = ipl.teamVteamAPI(team1, team2)
    return response


app.run(debug=True)
