from flask import Flask, render_template
import glob
import os
from datetime import datetime

app = Flask("jacky")

@app.route("/")
def root():
  ds = glob.glob("articles/*")
  result = []
  for d in ds:
    fs = glob.glob(d + "/*.txt")
    t = (d.split("/")[-1], len(fs))
    result.append(t)
  return render_template("index.html", d = result)

@app.route("/category/<c>")
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  result = []
  for f in fs:
    fsplit =  f.split("/")[-1].replace(".txt", "")
    m = os.path.getmtime(f)
    mstr = str(datetime.utcfromtimestamp(m))
    t = (fsplit, mstr)
    result.append(t)
  return render_template("category.html", d = result)

app.run(debug=True, port="3000", host="0.0.0.0")