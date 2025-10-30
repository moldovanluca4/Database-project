import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

def show_feedback(message, success=True):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Submission Feedback</title>
        <link rel="stylesheet" href="{ url_for('static', filename='css/style.css') }">
    </head>
    <body style="padding: 20px;">
        <h1>Submission Feedback</h1>
        <p style="color: {'green' if success else 'red'};">
            {message}
        </p>
        <a href="{ url_for('maintenance') }">Back to Maintenance Page</a>
    </body>
    </html>
    """

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")

@app.route("/imprint")
def imprint():
    return render_template("imprint.html")

@app.route("/add_major")
def add_major():
    return render_template("add_major.html")

@app.route("/handle_add_major", methods=["POST"])
def handle_add_major():
    try:
        major_name = request.form['major_name']
        return show_feedback(f"Success! Added major: {major_name}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_book")
def add_book():
    try:
        irc_buildings = [] 
        return render_template("add_book.html", all_ircs=irc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_book", methods=["POST"])
def handle_add_book():
    try:
        title = request.form['title']
        return show_feedback(f"Success! Added book: {title}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_club")
def add_club():
    try:
        scc_buildings = [] 
        return render_template("add_club.html", all_sccs=scc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_club", methods=["POST"])
def handle_add_club():
    try:
        club_name = request.form['club_name']
        return show_feedback(f"Success! Added club: {club_name}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_equipment")
def add_gym_equipment():
    try:
        gyms = [] 
        return render_template("add_gym_equipment.html", all_gyms=gyms)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_equipment", methods=["POST"])
def handle_add_gym_equipment():
    try:
        equip_name = request.form['equipment_name']
        return show_feedback(f"Success! Added equipment: {equip_name}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_tournament")
def add_tournament():
    try:
        events = [] 
        return render_template("add_tournament.html", all_events=events)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_tournament", methods=["POST"])
def handle_add_tournament():
    try:
        tourn_name = request.form['Tournament_name']
        return show_feedback(f"Success!Added tournament: {tourn_name}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_venue")
def add_venue():
    try:
        buildings = [] 
        return render_template("add_venue.html", all_buildings=buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_venue", methods=["POST"])
def handle_add_venue():
    try:
        venue_name = request.form['name']
        return show_feedback(f"Success!Added venue: {venue_name}", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/link_hall_to_major")
def link_hall_to_major():
    try:
        halls = [] 
        majors = [] 
        return render_template("link_hall_to_major.html", all_halls=halls, all_majors=majors)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_link_hall_major", methods=["POST"])
def handle_link_hall_major():
    try:
        hall_id = request.form['research_hall_id']
        major_id = request.form['major_id']
        return show_feedback(f"Success!Linked Hall {hall_id} to Major {major_id}.", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_schedule")
def add_gym_schedule():
    try:
        gyms = [] 
        personnel = [] 
        return render_template("add_gym_schedule.html", all_gyms=gyms, all_personnel=personnel)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_schedule", methods=["POST"])
def handle_add_gym_schedule():
    try:
        personnel_id = request.form['personnel_id']
        return show_feedback(f"Success! Added schedule for personnel {personnel_id}.", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_service_schedule")
def add_service_schedule():
    try:
        rlh_buildings = [] 
        services = [] 
        return render_template("add_service_schedule.html", all_rlhs=rlh_buildings, all_services=services)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_service_schedule", methods=["POST"])
def handle_add_service_schedule():
    try:
        service_id = request.form['service_id']
        return show_feedback(f"Success! Added schedule for service {service_id}.", success=True)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/building-results', methods=['GET'])
def personnel_search():
    search_term = request.args.get('personnel_name')
    sql_query = "SELECT GP.personnel_name, ROUND(AVG(TIME_TO_SEC(TIMEDIFF(GS.end_time, GS.start_time)) / 60)) AS Avg_Working_Minutes FROM GymPersonnel GP JOIN GymSchedule GS ON GP.id = GS.personnel_id GROUP BY GP.personnel_name;"
    results = db.execute(sql_query, (search_term,))
    return render_template('results_building.html', results_building = results)

"""
@app.route('/event-results', methods=['GET'])
def event_research():
    search_term = request.args.get('event')
    sql_query = "SELECT * FROM Event WHERE name LIKE %s"
    results = db.execute(sql_query, (search_term,))
    return render_template('results_event.html', results_event=results)



@app.route('/venue-results', method=['GET'])
def lecture_hall_search():
    search_term = request.args.get('lecture')
    sql_query = "SELECT v.name AS venue_name,lh.name_ AS hall_name,lh.address_,lh.capacity FROM LECTURE_HALL lh JOIN Venue v ON lh.venue_id = v.id WHERE lh.capacity > 100;"
    results = db.execute(sql_query, (search_term,))
    return render_template('results_venue.html', results_event = results)
"""


if __name__ == "__main__":
    app.run(debug=True)