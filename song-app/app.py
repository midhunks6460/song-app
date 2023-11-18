from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

songs = []

@app.route('/')
def index():
    return render_template('index.html', songs=songs)

@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.form['song']
    songs.append(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
