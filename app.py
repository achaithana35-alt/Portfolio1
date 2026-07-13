from flask import Flask, render_template, request, redirect, flash, send_from_directory
import mysql.connector
import os


# ==========================================
# Flask Configuration
# ==========================================

app = Flask(__name__)

app.secret_key = "chaithna_portfolio_secret_key"


# ==========================================
# MySQL Database Configuration
# XAMPP Default
# ==========================================

db_config = {

    "host": "localhost",

    "user": "root",

    "password": "",

    "database": "portfolio_db"

}



# ==========================================
# Database Connection
# ==========================================

def get_db_connection():

    try:

        connection = mysql.connector.connect(**db_config)

        return connection


    except mysql.connector.Error as error:

        print("Database Error:", error)

        return None




# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    projects = []


    try:

        conn = get_db_connection()


        if conn:


            cursor = conn.cursor(dictionary=True)


            cursor.execute(
                "SELECT * FROM projects ORDER BY id DESC"
            )


            projects = cursor.fetchall()


            cursor.close()

            conn.close()



    except Exception as e:

        print(e)



    return render_template(
        "index.html",
        projects=projects
    )




# ==========================================
# Contact Form
# ==========================================

@app.route("/contact", methods=["POST"])
def contact():


    name = request.form.get("name")

    email = request.form.get("email")

    subject = request.form.get("subject")

    message = request.form.get("message")



    try:


        conn = get_db_connection()


        if conn:


            cursor = conn.cursor()


            query = """

            INSERT INTO contact_messages

            (name,email,subject,message)

            VALUES(%s,%s,%s,%s)

            """



            cursor.execute(

                query,

                (
                    name,
                    email,
                    subject,
                    message
                )

            )


            conn.commit()


            cursor.close()

            conn.close()



        flash(
            "Message sent successfully!",
            "success"
        )


    except Exception as e:


        print(e)


        flash(
            "Something went wrong!",
            "danger"
        )



    return redirect("/#contact")




# ==========================================
# Resume Download
# ==========================================

@app.route("/resume")
def download_resume():

    return send_from_directory(

        "static/resume",

        "resume.pdf"

    )





# ==========================================
# Error Pages
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "index.html"
    ),404




@app.errorhandler(500)
def server_error(error):

    return """

    <h1>
    Internal Server Error
    </h1>

    """,500





# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )
