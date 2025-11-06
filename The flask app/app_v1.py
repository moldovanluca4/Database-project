import os
import mariadb
from flask import Flask, render_template, request, redirect, url_for, flash
import config

app = Flask(__name__)
app.secret_key = 'super-secret-key'


#helper function for establishing the connection
def get_db_connection():
    try:
        conn = mariadb.connect(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
            autocommit=False                #this concept means we are in transaction mode good for security purposes, this means we are not saving anything inside the database until we call conn commit and if something happens we call conn rollback and undo everything
        )

        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        raise e


#custom function that shows a simple html page in case of a success or error
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
        <a href="{ url_for('maintenance') }">Back to Maintenance Page</a> <br>
        <a href="{ url_for('home')}">Back to Home Page</a>
    </body>
    </html>
    """

#static page - home page
@app.route("/")
def home():
    return render_template("index.html")

#static page - maintenance page
@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")

#static page - imprint page
@app.route("/imprint")
def imprint():
    return render_template("imprint.html")


#for adding items we are going to use the two routes method

#First we have a GET route for the /add_something routes 
#theyre job is to prepare and display the html forms, they run the SELECT query(sometimes) to get data needed for the dropdown menus(not implement yet for all but its and idea for the future of this project)
#in the end it passes data into the render template

#Second is the POST route for /handle_add_something 
#this rote only accepts POST data ehich is what html forms send to the db
#it reads the input of the user 
#it opens a db connection and a cursora(its like a pointer that allows us to traverse and process result sets from a SELECT query one row at the time within the stored programs)
#it executes an INSERT operation
#IMPORTANT - we use ? placeholders from security purposes to prevent SQL injection attacks
#we call conn commit to save the new data only after everything went ok - also good for the security
#we use the show feedback to report a succes or a failure
#error handling is a must we catch the errors in time and we call rollback to cancel the transaction and show an error message - we do this so we dont save data with problems 
#finally - ensures cursor and conn are closed which prevents the db from running out of connections

@app.route("/add_major")
def add_major():
    return render_template("add_major.html")

@app.route("/handle_add_major", methods=["POST"])
def handle_add_major():
    conn = None
    cursor = None
    try:
        major_name = request.form['major_name']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO Majors (major_name) VALUES (?)"
        cursor.execute(sql, (major_name,))
        conn.commit()
        
        return show_feedback(f"Success! Added major: {major_name}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_book")
def add_book():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT B.id, B.address_ FROM IRC I JOIN Building B ON I.building_id = B.id ORDER BY B.address_"
        cursor.execute(sql)
        irc_buildings = cursor.fetchall()
        
        return render_template("add_book.html", all_ircs=irc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
   
@app.route("/handle_add_book", methods=["POST"])
def handle_add_book():
    conn = None
    cursor = None
    try:
        irc_building_id = request.form['irc_building_id']
        title = request.form['title']
        book_availability = request.form['book_availability']
        book_type = request.form['book_type']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO Books (irc_building_id, title, book_availability, book_type) 
            VALUES (?, ?, ?, ?)
        """
        params = (irc_building_id, title, book_availability, book_type)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added book: {title}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_club")
def add_club():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT B.id, B.address_ FROM SCC S JOIN Building B ON S.building_id = B.id ORDER BY B.address_"
        cursor.execute(sql)
        scc_buildings = cursor.fetchall()
        
        return render_template("add_club.html", all_sccs=scc_buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_club", methods=["POST"])
def handle_add_club():
    conn = None
    cursor = None
    try:
        scc_building_id = request.form['scc_building_id']
        club_name = request.form['club_name']
        schedule_days = request.form['schedule_days']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO Clubs (scc_building_id, club_name, schedule_days, start_time, end_time) 
            VALUES (?, ?, ?, ?, ?)
        """
        params = (scc_building_id, club_name, schedule_days, start_time, end_time)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added club: {club_name}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_gym_equipment")
def add_gym_equipment():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT B.id, B.address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY B.address_"
        cursor.execute(sql)
        gyms = cursor.fetchall()
        
        return render_template("add_gym_equipment.html", all_gyms=gyms)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_gym_equipment", methods=["POST"])
def handle_add_gym_equipment():
    conn = None
    cursor = None
    try:
        gym_building_id = request.form['gym_building_id']
        equip_name = request.form['equipment_name']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO GymEquipment (gym_building_id, equipment_name) VALUES (?, ?)"
        params = (gym_building_id, equip_name)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added equipment: {equip_name}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_tournament")
def add_tournament():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT id, name FROM Venue ORDER BY name"
        cursor.execute(sql)
        all_venues = cursor.fetchall()
        
        return render_template("add_tournament.html", all_events=all_venues)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_tournament", methods=["POST"])
def handle_add_tournament():
    conn = None
    cursor = None
    try:
        tourn_name = request.form['Tournament_name']
        teams = request.form['Number_of_registered_teams']
        sport = request.form['Sport']
        venue_id = request.form['venue_id']
        event_date = request.form['event_date']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql_event = "INSERT INTO Event (Venue_ID, Date_) VALUES (?, ?)"
        cursor.execute(sql_event, (venue_id, event_date))
        
        new_event_id = cursor.lastrowid
        
        sql_tourn = """
            INSERT INTO Tournament (Event_ID, Tournament_name, Number_of_registered_teams, Sport) 
            VALUES (?, ?, ?, ?)
        """
        params = (new_event_id, tourn_name, teams, sport)
        cursor.execute(sql_tourn, params)
        
        conn.commit()
        return show_feedback(f"Success! Added tournament: {tourn_name}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_venue")
def add_venue():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT id, address_ FROM Building ORDER BY address_"
        cursor.execute(sql)
        buildings = cursor.fetchall()
        
        return render_template("add_venue.html", all_buildings=buildings)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_venue", methods=["POST"])
def handle_add_venue():
    conn = None
    cursor = None
    try:
        venue_name = request.form['name']
        start_time = request.form['start_time']
        finish_time = request.form['finish_time']
        building_id = request.form['building_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO Venue (name, start_time, finish_time, building_id) 
            VALUES (?, ?, ?, ?)
        """
        params = (venue_name, start_time, finish_time, building_id)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added venue: {venue_name}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/link_hall_to_major")
def link_hall_to_major():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        halls_sql = "SELECT building_id, address_ FROM Research_hall R JOIN Building B ON R.building_id = B.id ORDER BY address_"
        cursor.execute(halls_sql)
        halls = cursor.fetchall()
        
        majors_sql = "SELECT id, major_name FROM Majors ORDER BY major_name"
        cursor.execute(majors_sql)
        majors = cursor.fetchall()
        
        return render_template("link_hall_to_major.html", all_halls=halls, all_majors=majors)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_link_hall_major", methods=["POST"])
def handle_link_hall_major():
    conn = None
    cursor = None
    try:
        hall_id = request.form['research_hall_id']
        major_id = request.form['major_id']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO ResearchHallMajors (research_hall_building_id, major_id) VALUES (?, ?)"
        cursor.execute(sql, (hall_id, major_id))
        conn.commit()
        
        return show_feedback(f"Success! Linked Hall {hall_id} to Major {major_id}.", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/add_gym_schedule")
def add_gym_schedule():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        gyms_sql = "SELECT building_id, address_ FROM Gym G JOIN Building B ON G.building_id = B.id ORDER BY address_"
        cursor.execute(gyms_sql)
        gyms = cursor.fetchall()
        
        personnel_sql = "SELECT id, personnel_name FROM GymPersonnel ORDER BY personnel_name"
        cursor.execute(personnel_sql)
        personnel = cursor.fetchall()

        return render_template("add_gym_schedule.html", all_gyms=gyms, all_personnel=personnel)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_gym_schedule", methods=["POST"])
def handle_add_gym_schedule():
    conn = None
    cursor = None
    try:
        gym_id = request.form['gym_building_id']
        personnel_id = request.form['personnel_id']
        days = request.form['working_days']
        start = request.form['start_time']
        end = request.form['end_time']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO GymSchedule (gym_building_id, personnel_id, working_days, start_time, end_time) 
            VALUES (?, ?, ?, ?, ?)
        """
        params = (gym_id, personnel_id, days, start, end)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added schedule for personnel {personnel_id}.", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
    
@app.route("/add_service_schedule")
def add_service_schedule():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        rlh_sql = "SELECT B.id as building_id, B.address_ FROM RLH R JOIN Building B ON R.building_id = B.id ORDER BY B.address_"
        cursor.execute(rlh_sql)
        rlh_buildings = cursor.fetchall()
        
        services_sql = "SELECT id, service_name_ FROM RLHServices ORDER BY service_name_"
        cursor.execute(services_sql)
        services = cursor.fetchall()
        
        return render_template("add_service_schedule.html", all_rlhs=rlh_buildings, all_services=services)
    except Exception as e:
        return show_feedback(f"Error loading page: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route("/handle_add_service_schedule", methods=["POST"])
def handle_add_service_schedule():
    conn = None
    cursor = None
    try:
        rlh_id = request.form['rlh_building_id']
        service_id = request.form['service_id']
        days = request.form['service_schedule_days']
        start = request.form['start_time']
        end = request.form['end_time']

        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO RLHServicesSchedule (rlh_building_id, service_id, service_schedule_days, start_time, end_time) 
            VALUES (?, ?, ?, ?, ?)
        """
        params = (rlh_id, service_id, days, start, end)
        cursor.execute(sql, params)
        conn.commit()
        
        return show_feedback(f"Success! Added schedule for service {service_id}.", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database Error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


@app.route('/add_register')
def register():
    return render_template("register.html")


@app.route('/handle_add_register', methods = ['POST'])
def handle_register():
    conn = None
    cursor = None

    try:
        username = request.form['user_name']
        password = request.form['user_password']

        if not username or password:
            flash('Username and password are required here')
            return redirect(url_for('add_register'))
        

        conn = get_db_connection()
        cursor = conn.cursor()

        sql_check = "SELECT user_name FROM users WHERE user_name = ?"
        cursor.execute(sql_check, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username taken - choose another")
            return redirect(url_for('add_register'))
        

        sql_insert_user = "INSERT INTO users (username, password) VALUES (?,?)"
        cursor.execute(sql_insert_user)
        conn.sommit()

        return show_feedback(f"Succes registration has succeded, welcome {username}", success=True)
    except mariadb.Error as e:
        if conn: conn.rollback()
        return show_feedback(f"Database error: {e}", success=False)
    except Exception as e:
        if conn: conn.rollback()
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()



#The Search pattern also uses a two routes approach
#its a same two route approach like before but the difference between the search pattern and add pattern is that the search uses GET for the both routes

#First we have the search forms in the routes of form /search-something
#the first part is simple just renders the html template with the search box

#Second we show the search results in the routes of form /something-results
#it reads the item to be searched from the URL 
#it uses request args get to get it
#it builds a query using the important placeholders - again for security
#it fetches all the results and passes them to a result template or a result html page


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
    conn = None
    cursor = None
    try:
        search_term = request.args.get('personnel_name', '')
        search_param = f"%{search_term}%"

        sql_query = """
            SELECT 
             GP.id, 
             GP.personnel_name AS name, 
             ROUND(AVG(TIME_TO_SEC(TIMEDIFF(GS.end_time, GS.start_time)) / 60)) AS Avg_Working_Minutes 
            FROM GymPersonnel GP 
            LEFT JOIN GymSchedule GS ON GP.id = GS.personnel_id 
            WHERE GP.personnel_name LIKE ?
            GROUP BY GP.id, GP.personnel_name;
        """
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute(sql_query, (search_param,))
        results = cursor.fetchall()
        
        return render_template('results_building.html', results_building=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


@app.route('/event-results', methods=['GET'])
def event_research():
    conn = None
    cursor = None
    try:
        search_term = request.args.get('sport_name', '')
        search_param = f"%{search_term}%"

        sql_query = "SELECT * FROM Tournament WHERE Sport LIKE ?"
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute(sql_query, (search_param,))
        results = cursor.fetchall()
        
        return render_template('results_tournament.html', tournaments=results, search_term=search_term)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


@app.route('/lecture-hall-results', methods=['GET'])
def lecture_hall_search():
    conn = None
    cursor = None
    try:
        min_capacity = request.args.get('min_capacity', 0)
        
        sql_query = """
            SELECT 
             v.id, v.name AS name, lh.name_ AS hall_name,
             lh.address_, lh.capacity 
            FROM LECTURE_HALL lh 
            JOIN Venue v ON lh.venue_id = v.id 
            WHERE lh.capacity >= ?
            ORDER BY lh.capacity DESC;
        """
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute(sql_query, (min_capacity,))
        results = cursor.fetchall()
        
        return render_template('results_venue.html', results_venue=results)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


#The Detail Page approach

#this approach uses a dynamic URL to show information about one specific item in this case a specific tournament taking place or a specific gym worker
#int id captures a number from the URL and passes it as an id argument to the function
#the function runs a query for that specific id
#and renders a detailed html page about that single item data
#this part will be improved


@app.route('/tournament/<int:id>')
def tournament_detail(id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT * FROM Tournament WHERE Tournament_ID = ?"
        cursor.execute(sql, (id,))
        tournament = cursor.fetchone()
        
        if tournament:
            return render_template('detail_tournament.html', tournament=tournament)
        else:
            return show_feedback("Tournament not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


@app.route('/personnel/<string:personnel_name>')
def show_personnel(personnel_name):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT * FROM GymPersonnel WHERE personnel_name = ?"
        cursor.execute(sql, (personnel_name,))
        item = cursor.fetchone()
        
        if item:
            return render_template('detail_personnel.html', item=item)
        else:
            return show_feedback("Personnel not found", success=False)
    except Exception as e:
        return show_feedback(f"Error: {e}", success=False)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

if __name__ == "__main__":
    app.run(debug=True)