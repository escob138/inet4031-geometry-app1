# INET 4031 Intro to Systems
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Orig Date: 3/31/2022
# Mod Date: 12/30/2023
# Mod Date: 12/31/2024
#

# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder
import sphere   # <-- now correct
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def mainForm():
    if request.method == "POST":
        sphere_sel = request.form.get("sphere")
        cylinder_sel = request.form.get("cylinder")

        if sphere_sel == "on":
            return redirect(url_for("sphereForm"))
        elif cylinder_sel == "on":
            return redirect(url_for("cylinderForm"))

    return render_template("index.html")

@app.route("/cylinder", methods=["GET","POST"])
def cylinderForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        height = request.form.get("hgt")
        vol = cylinder.volume(int(radius), int(height))
        return f"Radius: {radius}, Height: {height}<p>Volume: {vol}"
    return render_template("cylinder.html")

@app.route("/sphere", methods=["GET","POST"])
def sphereForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        vol = sphere.volume(int(radius))
        return f"Radius: {radius}<p>Volume of sphere: {vol}"
    return render_template("sphere.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
