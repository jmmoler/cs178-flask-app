# dbCode.py
# Author: Joseph Moler
# Helper functions for database connection and queries

import pymysql
import creds

def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    conn = get_conn()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def execute_update(query, args=()):
    """Executes an UPDATE/INSERT/DELETE query and commits the changes."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    cur.close()
    conn.close()

# Function to add a new player
def add_player(first_name, last_name, position):
    query = "INSERT INTO Players (first_name, last_name, position) VALUES (%s, %s, %s)"
    execute_update(query, (first_name, last_name, position))

# Function to delete a player
def delete_player(player_id):
    query = "DELETE FROM Players WHERE player_id = %s"
    execute_update(query, (player_id,))

# Function to fetch all players
def get_all_players():
    query = "SELECT * FROM Players"
    return execute_query(query)

# Function to update a player's stats (or other attributes)
def update_player_stats(player_id, points, assists, rebounds, steals, blocks, game_date):
    query = """
    INSERT INTO Stats (points, assists, rebounds, steals, blocks, game_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    execute_update(query, (points, assists, rebounds, steals, blocks, game_date))

    # Get the last inserted stat ID
    query = "SELECT LAST_INSERT_ID()"
    stat_id = execute_query(query)[0]['LAST_INSERT_ID()']

    # Link the player to the stat in the Player_Stats table
    query = "INSERT INTO Player_Stats (player_id, stat_id) VALUES (%s, %s)"
    execute_update(query, (player_id, stat_id))