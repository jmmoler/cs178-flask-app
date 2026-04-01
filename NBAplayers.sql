-- Create Players Table
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(20)
);

-- Create Teams Table
CREATE TABLE Teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

-- Create Stats Table
CREATE TABLE Stats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    points INT NOT NULL,
    assists INT NOT NULL,
    rebounds INT NOT NULL,
    steals INT,
    blocks INT,
    game_date DATE NOT NULL
);

-- Create Player_Team Join Table
CREATE TABLE Player_Team (
    player_id INT,
    team_id INT,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (player_id, team_id),
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE
);

-- Create Player_Stats Join Table
CREATE TABLE Player_Stats (
    player_id INT,
    stat_id INT,
    PRIMARY KEY (player_id, stat_id),
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (stat_id) REFERENCES Stats(stat_id) ON DELETE CASCADE
);

INSERT INTO Players (first_name, last_name, position)
VALUES 
('Stephen', 'Curry', 'Point Guard'),
('LeBron', 'James', 'Small Forward'),
('Giannis', 'Antetokounmpo', 'Power Forward'),
('Kevin', 'Durant', 'Small Forward'),
('Joel', 'Embiid', 'Center');

INSERT INTO Teams (team_name, city)
VALUES 
('Golden State Warriors', 'San Francisco'),
('Los Angeles Lakers', 'Los Angeles'),
('Milwaukee Bucks', 'Milwaukee'),
('Phoenix Suns', 'Phoenix'),
('Philadelphia 76ers', 'Philadelphia');

INSERT INTO Stats (points, assists, rebounds, steals, blocks, game_date)
VALUES
(30, 5, 7, 1, 1, '2026-03-28'),
(25, 8, 9, 2, 1, '2026-03-29'),
(40, 6, 13, 3, 2, '2026-03-30'),
(28, 4, 10, 1, 2, '2026-03-30'),
(35, 5, 12, 1, 2, '2026-03-31');

INSERT INTO Player_Team (player_id, team_id, start_date, end_date)
VALUES
(1, 1, '2019-10-01', NULL), -- Stephen Curry - Golden State Warriors
(2, 2, '2018-10-01', NULL), -- LeBron James - Los Angeles Lakers
(3, 3, '2017-10-01', NULL), -- Giannis Antetokounmpo - Milwaukee Bucks
(4, 4, '2021-10-01', NULL), -- Kevin Durant - Phoenix Suns
(5, 5, '2016-10-01', NULL); -- Joel Embiid - Philadelphia 76ers

INSERT INTO Player_Stats (player_id, stat_id)
VALUES
(1, 1), -- Stephen Curry - Stats 1
(2, 2), -- LeBron James - Stats 2
(3, 3), -- Giannis Antetokounmpo - Stats 3
(4, 4), -- Kevin Durant - Stats 4
(5, 5); -- Joel Embiid - Stats 5