# Higher or Lower Game

## Introduction
The "Higher or Lower" game is an interactive, fun, and engaging project designed to challenge players to guess whether the next value in a sequence is higher or lower. This project is based on the original web game, Higher Or Lower (http://www.higherlowergame.com/).

## Features
- **Dynamic Gameplay**: Players engage in a guessing game based on real-world or simulated data. Each round presents two entities with a value (e.g., monthly searches), and players must decide if the second entity's value is higher or lower than the first.
- **Player Data Management**: The game tracks each player's progress, including high scores and previous scores. This information is stored and can be accessed across sessions.
- **Interactive Menus**: Includes a main menu for managing players, starting a game, or exiting, and a player-specific menu for resuming or playing a new game.
- **Randomized Challenges**: Ensures fresh gameplay by dynamically selecting data points without repetition within a single session.
- **Error Handling**: Provides clear prompts and feedback for invalid inputs, enhancing the user experience.
- **Reusable Code**: Modular design for easy maintenance and extension, with separate components for game logic, player management, and utility functions.

## How It Works
1. **Start the Game**:
   - Displays a welcome screen with the game logo.
   - Shows the main menu where players can:
     - Choose an existing player.
     - Create a new player.
     - Remove a player.
     - Exit the game.

2. **Game Mechanics**:
   - The player is presented with two data points (e.g., entities and their associated values).
   - The player guesses whether the second value is higher or lower than the first.
   - Correct answers increase the player's score, while incorrect answers end the session.
   - If the player's score exceeds the high score, it is updated and saved.

3. **Player Management**:
   - Allows creating, selecting, and removing player profiles.
   - Tracks high scores and previous scores for each player.
   - Saves player data persistently to a `.txt` file.

4. **Data Handling**:
   - Uses a `.csv` file to load game data dynamically.
   - Implements random selection of data rows to ensure unique comparisons during a session.
   - Resets used data points when all rows are exhausted, enabling endless replayability.

## Technologies Used
- **Python**: Core programming language for implementing the game logic.
- **Pandas**: For efficient data loading and manipulation.
- **Object-Oriented Design**: Encapsulation of game logic and player management in modular classes.

## The Data
- The values and comparisons use real-world data from the original Higher or Lower game. The repository (https://github.com/julius2503/higher-lower-game) by Julius automates data collection using a Python bot. I utilized this bot to gather up-to-date data for my project, ensuring an authentic and current gameplay experience.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/paschoal-artur/HigherOrLower.git
   ```

2. Navigate to the project directory:
   ```bash
   cd HigherOrLower
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python main.py
   ```

## File Structure
```
HigherOrLower/
|— data/
|   |— game_data_with_formatting.csv  # Game data file
|   |— player_data.txt                # Player data file
|— src/
|   |— core/                         # Core game logic
|   |   |— game.py
|   |   |— player.py
|   |— utils/                        # Utility functions
|       |— display.py
|       |— file_handler.py
|       |— game_data.py
|— main.py                          # Game entry point
|— README.md                        # Project documentation
|— requirements.txt                # Python dependencies
```

## Contributing
Contributions are welcome! If you'd like to improve the game, please:
1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. See LICENSE for more details.

## Connect
If you enjoyed this project or have suggestions, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/artur-paschoal-18295627b/). Let's connect and collaborate!
