import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError
import config

db = SQLAlchemy()

app = Flask(__name__)


try:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}/{config.DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
except Exception as e:
    print(f"could not configure database {e}")

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
    try:
        major_name = request.form['major_name']
        sql = text("INSERT INTO Majors (major_name) VALUES (:major_name)")
        with db.session.begin():
            db.session.execute(sql, {"major_name": major_name})
        return show_feedback(f"Success! Added major: {major_name}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_book")
def add_book():
    try:
        sql = text("SELECT B.id, B.address_ FROM IRC I JOIN Building B ON I.building_id = B.id ORDER BY B.address_")
        irc_buildings = db.session.execute(sql).all()
        return render_template("add_book.html", all_ircs=irc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
   
@app.route("/handle_add_book", methods=["POST"])
def handle_add_book():
    try:
        irc_building_id = request.form['irc_building_id']
        title = request.form['title']
        book_availability = request.form['book_availability']
        book_type = request.form['book_type']
        
        sql = text("""
            INSERT INTO Books (irc_building_id, title, book_availability, book_type) 
            VALUES (:irc_id, :title, :avail, :type)
        """)
        params = {"irc_id": irc_building_id, "title": title, "avail": book_availability, "type": book_type}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added book: {title}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_club")
def add_club():
    try:
        sql = text("SELECT B.id, B.address_ FROM SCC S JOIN Building B ON S.building_id = B.id ORDER BY B.address_")
        scc_buildings = db.session.execute(sql).all()
        return render_template("add_club.html", all_sccs=scc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_club", methods=["POST"])
def handle_add_club():
    try:
        scc_building_id = request.form['scc_building_id']
        club_name = request.form['club_name']
        schedule_days = request.form['schedule_days']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        sql = text("""
            INSERT INTO Clubs (scc_building_id, club_name, schedule_days, start_time, end_time) 
            VALUES (:scc_id, :name, :days, :start, :end)
        """)
        params = {"scc_id": scc_building_id, "name": club_name, "days": schedule_days, "start": start_time, "end": end_time}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added club: {club_name}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_equipment")
def add_gym_equipment():
    try:
        sql = text("SELECT B.id, B.address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY B.address_")
        gyms = db.session.execute(sql).all()
        return render_template("add_gym_equipment.html", all_gyms=gyms)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_equipment", methods=["POST"])
def handle_add_gym_equipment():
    try:
        gym_building_id = request.form['gym_building_id']
        equip_name = request.form['equipment_name']
        
        sql = text("INSERT INTO GymEquipment (gym_building_id, equipment_name) VALUES (:gym_id, :name)")
        params = {"gym_id": gym_building_id, "name": equip_name}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added equipment: {equip_name}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_tournament")
def add_tournament():
    try:
        sql = text("SELECT id, name FROM Venue ORDER BY name")
        all_venues = db.session.execute(sql).all()
        
        return render_template("add_tournament.html", all_events=all_venues)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_tournament", methods=["POST"])
def handle_add_tournament():
    try:
        tourn_name = request.form['Tournament_name']
        teams = request.form['Number_of_registered_teams']
        sport = request.form['Sport']
        venue_id = request.form['venue_id']
        event_date = request.form['event_date']

        sql_event = text("INSERT INTO Event (Venue_ID, Date_) VALUES (:venue_id, :date)")
        result = db.session.execute(sql_event, {"venue_id": venue_id, "date": event_date})
        
        new_event_id = result.lastrowid
        
        sql_tourn = text("""
            INSERT INTO Tournament (Event_ID, Tournament_name, Number_of_registered_teams, Sport) 
            VALUES (:event_id, :name, :teams, :sport)
        """)
        params = {"event_id": new_event_id, "name": tourn_name, "teams": teams, "sport": sport}
        db.session.execute(sql_tourn, params)
        
        db.session.commit()
        return show_feedback(f"Success! Added tournament: {tourn_name}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        db.session.rollback()
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_venue")
def add_venue():
    try:
        sql = text("SELECT id, address_ FROM Building ORDER BY address_")
        buildings = db.session.execute(sql).all()
        return render_template("add_venue.html", all_buildings=buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_venue", methods=["POST"])
def handle_add_venue():
    try:
        venue_name = request.form['name']
        start_time = request.form['start_time']
        finish_time = request.form['finish_time']
        building_id = request.form['building_id']

        sql = text("""
            INSERT INTO Venue (name, start_time, finish_time, building_id) 
            VALUES (:name, :start, :finish, :b_id)
        """)
        params = {"name": venue_name, "start": start_time, "finish": finish_time, "b_id": building_id}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added venue: {venue_name}", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/link_hall_to_major")
def link_hall_to_major():
    try:
        halls_sql = text("SELECT building_id, address_ FROM Research_hall R JOIN Building B ON R.building_id = B.id ORDER BY address_")
        majors_sql = text("SELECT id, major_name FROM Majors ORDER BY major_name")

        halls = db.session.execute(halls_sql).all()
        majors = db.session.execute(majors_sql).all()
        
        return render_template("link_hall_to_major.html", all_halls=halls, all_majors=majors)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_link_hall_major", methods=["POST"])
def handle_link_hall_major():
    try:
        hall_id = request.form['research_hall_id']
        major_id = request.form['major_id']
        
        sql = text("INSERT INTO ResearchHallMajors (research_hall_building_id, major_id) VALUES (:hall_id, :major_id)")
        with db.session.begin():
            db.session.execute(sql, {"hall_id": hall_id, "major_id": major_id})
        return show_feedback(f"Success! Linked Hall {hall_id} to Major {major_id}.", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)

@app.route("/add_gym_schedule")
def add_gym_schedule():
    try:
        gyms_sql = text("SELECT building_id, address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY address_")
        personnel_sql = text("SELECT id, personnel_name FROM GymPersonnel ORDER BY personnel_name")

        gyms = db.session.execute(gyms_sql).all()
        personnel = db.session.execute(personnel_sql).all()

        return render_template("add_gym_schedule.html", all_gyms=gyms, all_personnel=personnel)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_gym_schedule", methods=["POST"])
def handle_add_gym_schedule():
    try:
        gym_id = request.form['gym_building_id']
        personnel_id = request.form['personnel_id']
        days = request.form['working_days']
        start = request.form['start_time']
        end = request.form['end_time']
        
        sql = text("""
            INSERT INTO GymSchedule (gym_building_id, personnel_id, working_days, start_time, end_time) 
            VALUES (:gym_id, :p_id, :days, :start, :end)
        """)
        params = {"gym_id": gym_id, "p_id": personnel_id, "days": days, "start": start, "end": end}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added schedule for personnel {personnel_id}.", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    
@app.route("/add_service_schedule")
def add_service_schedule():
    try:
        rlh_sql = text("SELECT B.id as building_id, B.address_ FROM RLH R JOIN Building B ON R.building_id = B.id ORDER BY B.address_")
        services_sql = text("SELECT id, service_name_ FROM RLHServices ORDER BY service_name_")

        rlh_buildings = db.session.execute(rlh_sql).all()
        services = db.session.execute(services_sql).all()
        
        return render_template("add_service_schedule.html", all_rlhs=rlh_buildings, all_services=services)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)

@app.route("/handle_add_service_schedule", methods=["POST"])
def handle_add_service_schedule():
    try:
        rlh_id = request.form['rlh_building_id']
        service_id = request.form['service_id']
        days = request.form['service_schedule_days']
        start = request.form['start_time']
        end = request.form['end_time']

        sql = text("""
            INSERT INTO RLHServicesSchedule (rlh_building_id, service_id, service_schedule_days, start_time, end_time) 
            VALUES (:rlh_id, :s_id, :days, :start, :end)
        """)
        params = {"rlh_id": rlh_id, "s_id": service_id, "days": days, "start": start, "end": end}
        with db.session.begin():
            db.session.execute(sql, params)
        return show_feedback(f"Success! Added schedule for service {service_id}.", success=True)
    except SQLAlchemyError as e:
        db.session.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
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

        sql_query = text("""
            SELECT 
             GP.id, 
             GP.personnel_name AS name, 
             ROUND(AVG(TIME_TO_SEC(TIMEDIFF(GS.end_time, GS.start_time)) / 60)) AS Avg_Working_Minutes 
            FROM GymPersonnel GP 
            LEFT JOIN GymSchedule GS ON GP.id = GS.personnel_id 
            WHERE GP.personnel_name LIKE :p_name_like
            GROUP BY GP.id, GP.personnel_name;
        """)
        
        results = db.session.execute(sql_query, {"p_name_like": search_param}).all()
        return render_template('results_building.html', results_building=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/event-results', methods=['GET'])
def event_research():
   
    try:
        search_term = request.args.get('sport_name', '')
        search_param = f"%{search_term}%"

        sql_query = text("SELECT * FROM Tournament WHERE Sport LIKE :sport_name_like")
        
        results = db.session.execute(sql_query, {"sport_name_like": search_param}).all()
        
        return render_template('results_tournament.html', tournaments=results, search_term=search_term)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)



@app.route('/lecture-hall-results', methods=['GET'])
def lecture_hall_search():
    try:
        min_capacity = request.args.get('min_capacity', 0)
        
        
        sql_query = text("""
            SELECT 
             v.id, v.name AS name, lh.name_ AS hall_name,
             lh.address_, lh.capacity 
            FROM LECTURE_HALL lh 
            JOIN Venue v ON lh.venue_id = v.id 
            WHERE lh.capacity >= :capacity
            ORDER BY lh.capacity DESC;
        """)
        
        results = db.session.execute(sql_query, {"capacity": min_capacity}).all()
        
        
        return render_template('results_venue.html', results_venue=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/tournament/<int:id>')
def tournament_detail(id):
  
    try:
        sql = text("SELECT * FROM Tournament WHERE Tournament_ID = :id")
        tournament = db.session.execute(sql, {"id": id}).first()
        if tournament:
            return render_template('detail_tournament.html', tournament=tournament)
        else:
            return show_feedback("Tournament not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)


@app.route('/personnel/<string:personnel_name>')
def show_personnel(personnel_name):
  
    try:
        sql = text("SELECT * FROM GymPersonnel WHERE personnel_name = :p_name")
        item = db.session.execute(sql, {"p_name": personnel_name}).first()
        if item:
          
            return render_template('detail_personnel.html', item=item)
        else:
            return show_feedback("Personnel not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)




if __name__ == "__main__":
    app.run(debug=True)
