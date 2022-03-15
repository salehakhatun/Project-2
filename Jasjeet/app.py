# 1. import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
#Created connection with local database SQL
rds_connection_string = "postgres:Mithuji007@localhost:5432/Happiness_Ranking"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
merged = Base.classes.merged

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/Project2")
def Project2():
    print("Server received request for 'Home' page...")
    return "Welcome to project 2: Group members: Saleha, Erika, Pim, Jasjeet"
    
# 4. Define main behavior 
if __name__ == "__main__":
    app.run(debug=True)