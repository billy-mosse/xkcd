from flask import Flask, flash, redirect, render_template, request, session, abort,send_from_directory,send_file,jsonify
import pandas as pd

import json




#1. Declare application
application= Flask(__name__)



@application.route("/main",methods=["GET","POST"])

#3. Define main code
@application.route("/",methods=["GET","POST"])
def homepage():


    return render_template("index.html")


@application.route("/get-data",methods=["GET","POST"])
def returnProdData():
    f=data.Prod

    return jsonify(f)
# export the final result to a json file

@application.route("/get-loss-data",methods=["GET","POST"])
def returnLossData():
    g=data.Loss

    return jsonify(g)


if __name__ == "__main__":
    application.run(debug=True)



