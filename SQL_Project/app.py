from flask import Flask,request,redirect,render_template
import sqlalchemy
from sqlalchemy import create_engine,text
import pandas as pd
app = Flask(__name__)

db_string= ""
db_engine = None
db_conn = None

@app.route("/", methods=["GET","POST"])
def index():
    global db_string
    if request.method == "POST":
        db_ip = request.form["ip"]
        username = request.form["user"]
        passphrase = request.form["passphrase"]
        db = request.form["dbname"]
        db_string = f'mssql+pymssql://{username}:{passphrase}@{db_ip}:1433/{db}'
        return redirect("/query")
    else:
        return render_template("index.html")

@app.route("/query",methods=["GET","POST"])
def query():
    global db_engine
    global db_conn
    print("DB String: ",db_string)
    db_engine = create_engine(db_string)
    db_conn = db_engine.connect()
    if request.method == "POST":
        sql = text(request.form["statement"])
        df = pd.read_sql_query(sql,db_conn)
        print(df)
        return "You did it"
    return render_template("query.html")

if __name__ == "__main__":
    app.run(debug=True)
