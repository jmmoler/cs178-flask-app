# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # This is required for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-player', methods=['GET', 'POST'])
def add_player_by_pos():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        position = request.form['position']

        # 🚨 check duplicate
        if player_exists(first_name, last_name):
            flash('Player already exists!', 'danger')
            return redirect(url_for('add_player'))

        add_player(first_name, last_name, position)

        flash('Player added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_player.html')

@app.route('/delete-player', methods=['GET', 'POST'])
def delete_player_by_id():
    if request.method == 'POST':
        player_id = request.form['player_id']

        # 🚨 check exists
        if not player_id_exists(player_id):
            flash('Player ID does not exist!', 'danger')
            return redirect(url_for('delete_player_by_id'))

        delete_player(player_id)

        flash('Player deleted successfully!', 'warning')
        return redirect(url_for('home'))

    return render_template('delete_player.html')

@app.route('/display-players')
def display_players():
    # Fetch all players from the database
    players = get_all_players()
    return render_template('display_players.html', players=players)


@app.route('/update-player', methods=['GET', 'POST'])
def go_to_update():
    if request.method == 'POST':
        player_id = request.form['player_id']
        return redirect(url_for('update_stats', player_id=player_id))
    return render_template('update_player.html')


@app.route('/update-stats/<int:player_id>', methods=['GET', 'POST'])
def update_stats(player_id):

    if not player_id_exists(player_id):
        flash("Player ID does not exist!", "danger")
        return redirect(url_for('home'))

    player = get_player_by_id(player_id)

    if request.method == 'POST':
        points = request.form['points']
        assists = request.form['assists']
        rebounds = request.form['rebounds']
        steals = request.form['steals']
        blocks = request.form['blocks']
        game_date = request.form['game_date']

        update_player_stats(player_id, points, assists, rebounds, steals, blocks, game_date)

        flash('Player stats updated successfully!', 'success')
        return redirect(url_for('display_players'))

    return render_template('update_stats.html', player=player)

# These two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)