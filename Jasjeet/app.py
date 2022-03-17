# 1. import dependencies
import numpy as np
import pandas as pd

from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
#Created connection with local database SQL
rds_connection_string = "postgres:password@localhost:5432/Happiness_Ranking"
engine = create_engine(f'postgresql://{rds_connection_string}')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/Happiness_dataset")
def Happiness_dataset():
    data = pd.read_sql_query('select * from merged', con=engine)
    return jsonify(data.to_json())
    
# 4. Define main behavior 
if __name__ == "__main__":
    app.run(debug=True)