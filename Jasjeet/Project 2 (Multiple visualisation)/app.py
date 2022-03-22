# 1. import dependencies
import numpy as np
import pandas as pd

from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
#Created connection with local database SQL
rds_connection_string = "postgres:Mithuji007@localhost:5432/Happiness_Ranking"
engine = create_engine(f'postgresql://{rds_connection_string}')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
results = engine.execute("SELECT * FROM data").fetchall()

# new = []
# for i in results:
#     a = {"abrr":i[0],"country":i[1],"score":i[2],"gdp":i[3],"social_support":i[4],"life_expectancy":i[5],"freedom":i[6],"generosity":i[7],"corruption":i[8],"healthcare":i[9],"healthcareLow":i[10],"healthcareHigh":i[11],"obesity":i[12],"obesityLow":i[13],"obesityHigh":i[14],"smokes":i[15],"smokesLow":i[16],"smokesHigh":i[17]}
#     new.append(a)

#{abb}

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/linkbuttonk")
def test():
    
    return render_template("test.html")

    




@app.route("/data")
def Happiness_dataset():
    data = pd.read_sql_query('select * from data', con=engine)
    return jsonify(data.to_json(orient="records"))
    
# 4. Define main behavior 
if __name__ == "__main__":
    app.run(debug=True)