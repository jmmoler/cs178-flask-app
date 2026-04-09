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
    conn = get_conn()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    try:
        # check player exists
        cur.execute("SELECT player_id FROM Players WHERE player_id = %s", (player_id,))
        player = cur.fetchone()

        if not player:
            raise ValueError(f"Player ID {player_id} does not exist.")

        # insert stats
        cur.execute("""
            INSERT INTO Stats (points, assists, rebounds, steals, blocks, game_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (points, assists, rebounds, steals, blocks, game_date))

        stat_id = cur.lastrowid

        # insert join row
        cur.execute("""
            INSERT INTO Player_Stats (player_id, stat_id)
            VALUES (%s, %s)
        """, (player_id, stat_id))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cur.close()
        conn.close()


def get_player_by_id(player_id):
    query = "SELECT * FROM Players WHERE player_id = %s"
    result = execute_query(query, (player_id,))
    return result[0] if result else None

def player_exists(first_name, last_name):
    query = """
    SELECT * FROM Players 
    WHERE first_name = %s AND last_name = %s
    """
    result = execute_query(query, (first_name, last_name))
    return len(result) > 0

def player_id_exists(player_id):
    query = "SELECT * FROM Players WHERE player_id = %s"
    result = execute_query(query, (player_id,))
    return len(result) > 0

def get_player_stats_history(player_id):
    query = """
        SELECT 
            p.player_id,
            p.first_name,
            p.last_name,
            s.stat_id,
            s.points,
            s.assists,
            s.rebounds,
            s.steals,
            s.blocks,
            s.game_date
        FROM Players p
        JOIN Player_Stats ps ON p.player_id = ps.player_id
        JOIN Stats s ON ps.stat_id = s.stat_id
        WHERE p.player_id = %s
        ORDER BY s.game_date DESC, s.stat_id DESC
    """
    return execute_query(query, (player_id,))