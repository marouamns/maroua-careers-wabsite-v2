from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'data analyst',
  'location': 'bengluru, india',
  'salary': 'rs,100000'
}, {
  'id': 2,
  'title': 'data scientist',
  'location': 'delhi, india',
  'salary': 'rs,150000'
}, {
  'id': 2,
  'title': 'backend',
  'location': 'remote',
  'salary': 'rs,120000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
