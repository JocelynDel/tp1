from flask import Flask, render_template, request
import mysql.connector # import du client mysql
import json, os



#connection au serveur mysql
db = mysql.connector.connect(
  host="mariadb",
  port=3306,
  user="root",
  password="root",
  database="tp1"
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        quote = details['quote']
        author = details['author']
        cur = db.cursor()
        cur.execute("INSERT INTO quotes(quote, author) VALUES (%s, %s)", (quote, author))
        db.commit()
        cur.close()
        return 'success'
    return render_template('core.html')

app.run(host="0.0.0.0", port=8081)

 