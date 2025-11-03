import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)

DATABASE = 'campus.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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
        <a href="{ url_for('maintenance') }">Back to Maintenance Page</a> </b>
        <a href="{ url_for('home')}">Back to Home Page</a>
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
    db = get_db()
    try:
        major_name = request.form['major_name']
        sql = "INSERT INTO Majors (major_name) VALUES (:major_name)"
        db.execute(sql, {"major_name": major_name})
        db.commit()
        return show_feedback(f"Success! Added major: {major_name}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_book")
def add_book():
    try:
        sql = "SELECT B.id, B.address_ FROM IRC I JOIN Building B ON I.building_id = B.id ORDER BY B.address_"
        irc_buildings = get_db().execute(sql).fetchall()
        return render_template("add_book.html", all_ircs=irc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
   
@app.route("/handle_add_book", methods=["POST"])
def handle_add_book():
    db = get_db()
    try:
        irc_building_id = request.form['irc_building_id']
        title = request.form['title']
        book_availability = request.form['book_availability']
        book_type = request.form['book_type']
        
        sql = """
            INSERT INTO Books (irc_building_id, title, book_availability, book_type) 
            VALUES (:irc_id, :title, :avail, :type)
        """
        params = {"irc_id": irc_building_id, "title": title, "avail": book_availability, "type": book_type}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added book: {title}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_club")
def add_club():
    try:
        sql = "SELECT B.id, B.address_ FROM SCC S JOIN Building B ON S.building_id = B.id ORDER BY B.address_"
        scc_buildings = get_db().execute(sql).fetchall()
        return render_template("add_club.html", all_sccs=scc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_club", methods=["POST"])
def handle_add_club():
    db = get_db()
    try:
        scc_building_id = request.form['scc_building_id']
        club_name = request.form['club_name']
        schedule_days = request.form['schedule_days']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        sql = """
            INSERT INTO Clubs (scc_building_id, club_name, schedule_days, start_time, end_time) 
            VALUES (:scc_id, :name, :days, :start, :end)
        """
        params = {"scc_id": scc_building_id, "name": club_name, "days": schedule_days, "start": start_time, "end": end_time}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added club: {club_name}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_equipment")
def add_gym_equipment():
    try:
        sql = "SELECT B.id, B.address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY B.address_"
        gyms = get_db().execute(sql).fetchall()
        return render_template("add_gym_equipment.html", all_gyms=gyms)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_equipment", methods=["POST"])
def handle_add_gym_equipment():
    db = get_db()
    try:
        gym_building_id = request.form['gym_building_id']
        equip_name = request.form['equipment_name']
        
        sql = "INSERT INTO GymEquipment (gym_building_id, equipment_name) VALUES (:gym_id, :name)"
        params = {"gym_id": gym_building_id, "name": equip_name}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added equipment: {equip_name}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_tournament")
def add_tournament():
    try:
        sql = "SELECT id, name FROM Venue ORDER BY name"
        all_venues = get_db().execute(sql).fetchall()
        return render_template("add_tournament.html", all_events=all_venues)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_tournament", methods=["POST"])
def handle_add_tournament():
    db = get_db()
    try:
        tourn_name = request.form['Tournament_name']
        teams = request.form['Number_of_registered_teams']
        sport = request.form['Sport']
        venue_id = request.form['venue_id']
        event_date = request.form['event_date']

        sql_event = "INSERT INTO Event (Venue_ID, Date_) VALUES (:venue_id, :date)"
        cursor = db.execute(sql_event, {"venue_id": venue_id, "date": event_date})
        
        new_event_id = cursor.lastrowid
        
        sql_tourn = """
            INSERT INTO Tournament (Event_ID, Tournament_name, Number_of_registered_teams, Sport) 
            VALUES (:event_id, :name, :teams, :sport)
        """
        params = {"event_id": new_event_id, "name": tourn_name, "teams": teams, "sport": sport}
        db.execute(sql_tourn, params)
        
        db.commit()
        return show_feedback(f"Success! Added tournament: {tourn_name}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_venue")
def add_venue():
    try:
        sql = "SELECT id, address_ FROM Building ORDER BY address_"
        buildings = get_db().execute(sql).fetchall()
        return render_template("add_venue.html", all_buildings=buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_venue", methods=["POST"])
def handle_add_venue():
    db = get_db()
    try:
        venue_name = request.form['name']
        start_time = request.form['start_time']
        finish_time = request.form['finish_time']
        building_id = request.form['building_id']

        sql = """
            INSERT INTO Venue (name, start_time, finish_time, building_id) 
            VALUES (:name, :start, :finish, :b_id)
        """
        params = {"name": venue_name, "start": start_time, "finish": finish_time, "b_id": building_id}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added venue: {venue_name}", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/link_hall_to_major")
def link_hall_to_major():
    try:
        db = get_db()
        halls_sql = "SELECT building_id, address_ FROM Research_hall R JOIN Building B ON R.building_id = B.id ORDER BY address_"
        majors_sql = "SELECT id, major_name FROM Majors ORDER BY major_name"

        halls = db.execute(halls_sql).fetchall()
        majors = db.execute(majors_sql).fetchall()
        
        return render_template("link_hall_to_major.html", all_halls=halls, all_majors=majors)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_link_hall_major", methods=["POST"])
def handle_link_hall_major():
    db = get_db()
    try:
        hall_id = request.form['research_hall_id']
        major_id = request.form['major_id']
        
        sql = "INSERT INTO ResearchHallMajors (research_hall_building_id, major_id) VALUES (:hall_id, :major_id)"
        db.execute(sql, {"hall_id": hall_id, "major_id": major_id})
        db.commit()
        return show_feedback(f"Success! Linked Hall {hall_id} to Major {major_id}.", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_schedule")
def add_gym_schedule():
    try:
        db = get_db()
        gyms_sql = "SELECT building_id, address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY address_"
        personnel_sql = "SELECT id, personnel_name FROM GymPersonnel ORDER BY personnel_name"

        gyms = db.execute(gyms_sql).fetchall()
        personnel = db.execute(personnel_sql).fetchall()

        return render_template("add_gym_schedule.html", all_gyms=gyms, all_personnel=personnel)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_schedule", methods=["POST"])
def handle_add_gym_schedule():
    db = get_db()
    try:
        gym_id = request.form['gym_building_id']
        personnel_id = request.form['personnel_id']
        days = request.form['working_days']
        start = request.form['start_time']
        end = request.form['end_time']
        
        sql = """
            INSERT INTO GymSchedule (gym_building_id, personnel_id, working_days, start_time, end_time) 
            VALUES (:gym_id, :p_id, :days, :start, :end)
        """
        params = {"gym_id": gym_id, "p_id": personnel_id, "days": days, "start": start, "end": end}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added schedule for personnel {personnel_id}.", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)
    
@app.route("/add_service_schedule")
def add_service_schedule():
    try:
        db = get_db()
        rlh_sql = "SELECT B.id as building_id, B.address_ FROM RLH R JOIN Building B ON R.building_id = B.id ORDER BY B.address_"
        services_sql = "SELECT id, service_name_ FROM RLHServices ORDER BY service_name_"

        rlh_buildings = db.execute(rlh_sql).fetchall()
        services = db.execute(services_sql).fetchall()
        
        return render_template("add_service_schedule.html", all_rlhs=rlh_buildings, all_services=services)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_service_schedule", methods=["POST"])
def handle_add_service_schedule():
    db = get_db()
    try:
        rlh_id = request.form['rlh_building_id']
        service_id = request.form['service_id']
        days = request.form['service_schedule_days']
        start = request.form['start_time']
        end = request.form['end_time']

        sql = """
            INSERT INTO RLHServicesSchedule (rlh_building_id, service_id, service_schedule_days, start_time, end_time) 
            VALUES (:rlh_id, :s_id, :days, :start, :end)
        """
        params = {"rlh_id": rlh_id, "s_id": service_id, "days": days, "start": start, "end": end}
        db.execute(sql, params)
        db.commit()
        return show_feedback(f"Success! Added schedule for service {service_id}.", success=True)
    except sqlite3.Error as e:
        db.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route('/search-building')
def show_building_search():
    return render_template('search_building.html')

@app.route('/search-event')
def show_event_search():
    return render_template("search_tournament.html")

@app.route('/search-venue')
def show_venue_search():
    return render_template('search_lecture_hall.html')

@app.route('/building-results', methods=['GET'])
def personnel_search():
    try:
        search_term = request.args.get('personnel_name', '')
        search_param = f"%{search_term}%"
        
        sql_query = """
            SELECT 
             GP.id, 
             GP.personnel_name AS name, 
             ROUND(AVG((strftime('%s', GS.end_time) - strftime('%s', GS.start_time)) / 60)) AS Avg_Working_Minutes 
            FROM GymPersonnel GP 
            LEFT JOIN GymSchedule GS ON GP.id = GS.personnel_id 
            WHERE GP.personnel_name LIKE :p_name_like
            GROUP BY GP.id, GP.personnel_name;
        """
        
        results = get_db().execute(sql_query, {"p_name_like": search_param}).fetchall()
        return render_template('results_building.html', results_building=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/event-results', methods=['GET'])
def event_research():
    try:
        search_term = request.args.get('sport_name', '')
        search_param = f"%{search_term}%"

        sql_query = "SELECT * FROM Tournament WHERE Sport LIKE :sport_name_like"
        
        results = get_db().execute(sql_query, {"sport_name_like": search_param}).fetchall()
        
        return render_template('results_tournament.html', tournaments=results, search_term=search_term)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)



@app.route('/lecture-hall-results', methods=['GET'])
def lecture_hall_search():
    try:
        min_capacity = request.args.get('min_capacity', 0)
        
        sql_query = """
            SELECT 
             v.id, v.name AS name, lh.name_ AS hall_name,
             lh.address_, lh.capacity 
            FROM LECTURE_HALL lh 
            JOIN Venue v ON lh.venue_id = v.id 
            WHERE lh.capacity >= :capacity
            ORDER BY lh.capacity DESC;
        """
        
        results = get_db().execute(sql_query, {"capacity": min_capacity}).fetchall()
        
        return render_template('results_venue.html', results_venue=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route('/tournament/<int:id>')
def tournament_detail(id):
    try:
        sql = "SELECT * FROM Tournament WHERE Tournament_ID = :id"
        tournament = get_db().execute(sql, {"id": id}).fetchone()
        if tournament:
            return render_template('detail_tournament.html', tournament=tournament)
        else:
            return show_feedback("Tournament not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/personnel/<string:personnel_name>')
def show_personnel(personnel_name):
    try:
        sql = "SELECT * FROM GymPersonnel WHERE personnel_name = :p_name"
        item = get_db().execute(sql, {"p_name": personnel_name}).fetchone()
        if item:
            return render_template('detail_personnel.html', item=item)
        else:
            return show_feedback("Personnel not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

if __name__ == "__main__":
    app.run(debug=True)