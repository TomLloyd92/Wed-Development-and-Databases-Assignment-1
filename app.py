from flask import Flask, render_template, session, request
import random
import os
import pickle

FNAME = "data/scores.pickle"
app = Flask(__name__)




@app.route("/Introduction")
def intro():

    return render_template(
        "introduction.html",
        
        the_title="Number",
    )

app.secret_key = "bigrb40953452=f___D_ndjf29jf239j50945fgjfj23j-ff "
app.run(debug=True)