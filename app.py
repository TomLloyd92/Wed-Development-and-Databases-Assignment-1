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
        
        the_title="NumberWang",
    )

    app.run(debug=True)