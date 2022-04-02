from flask import Flask, render_template
from flask import send_file
from mido import MidiFile


app = Flask(__name__)


@app.route('/')
def main():
  return render_template("index.html")


@app.route('/output')
def output():
  return render_template("output.html")


@app.route('/output/file')
def outputFile():
	mid = MidiFile('/Users/jj/Desktop/music_generator/output/n.mid', clip=True)
	return send_file(mid, mimetype="audio\midi")


if __name__ == "__main__":
    app.run(debug=True)

