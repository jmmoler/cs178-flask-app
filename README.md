# [NBA Player Statistics]

**NBA Player Statistics Manager**
**Author:** [Joseph Moler]
**GitHub:** [jmmoler]

---

## Overview

<!-- Describe your project in 2-4 sentences. What does it do? Who is it for? What problem does it solve? -->
This project is my NBA Player statistics website using amazon AWS and other cloud computing services to interact with and update my SQL database is real time. It allows you to vuiew NBA players, add/delete players, and import game statistics for players that can later be reviewed in their history. It is also navigatable using buttons on each website page and solves the problem of not having somewhere to track your favorite NBA teams and your rating on them and following your top players' statistics.

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **AWS DynamoDB** — non-relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py             # Main Flask application — routes and app logic
├── dbCode.py                 # Database helper functions (MySQL connection + queries)
├── creds_sample.py           # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html             # Landing page
│   ├── add_player.html       # Add descriptions for your other templates
│   ├── display_players.html  # 
│   ├── update_stats.html     #
│   ├── delete_player.html    #
│   ├── update_player.html    #
│   ├── player_stats.html     #
│   ├── fan_ratings.html      #
├── .gitignore                # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/jmmoler/NBAplayers.git
   cd NBAplayers
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://ec2-98-93-29-134.compute-1.amazonaws.com:8080/
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

I have tables for Players, teams, and Stats. These tables store relevant information about the NBA players and their teams, as well as player's game statistics from different games.

**Example:**

- `Players` — stores first name, last name, position; primary key is `id`
- `Stats` — stores points, assists, rebounds, steals, blocks, etc; foreign key links to `id`

The JOIN query used in this project joined the Players and Stats tables to display a specific player's game stats and game history.

### DynamoDB

My Dynamo table stored the Team names and the fan ratings of each team. The partition key was the team's name and then the user can input the rating they would like to give each team, or add a new team.

- **Table name:** `NBATeamRatings`
- **Partition key:** `Team`
- **Used for:** Storing fan ratings of each NBA team.

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/add-player` | This allows the user to add players first and last name and position. |
| Read      | `/display-players` | Displays all players and their ID, first name, last name, and position. |
| Update    | `/update/stats/<player_id>` | Allows user to update the game stats of the specific player they select. |
| Delete    | `/delete-player` | Allows user to remove players via player ID. |

---

## Challenges and Insights

The hardest part was getting started and understanding the order in which to tackle this project. I had trouble establishing my RDS database and creating it, but once that was done it was just the matter of coding and troubleshooting. Lastly, was design decisions, where i got to play around with what my website looked like and how i wanted users to interact and view my data, but that was fun for me.

---

## AI Assistance

I used ChatGPT to establish my RDS database and create sample rows to use in testing. I also used chat to help with a bit of the html syntax that i was unfamiliar with and bridging the gap one certain websie functions that I was running into issues with, such as selecting the player I wanted to update the stats for without going into the search bar with their player id. Other than that, I just used Ai to help troubleshoot or explain some of the error messages I ran into.
