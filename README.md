# Higher or Lower Game

## Introduction
The "Higher or Lower" game is an interactive, fun, and engaging project designed to challenge players to guess whether the next value in a sequence is higher or lower. This project is based on the original web game, Higher Or Lower (http://www.higherlowergame.com/).

## Features
- **Dynamic Gameplay**: Players guess values based on real or simulated data.
- **Player Data Management**: Tracks player scores and stores high scores.
- **Reusable Code**: Modular design for easy maintenance and extension.

## How It Works
1. **Start the Game**:
   - Displays a welcome screen.
   - Shows the main menu where players can start, view scores, or exit.

2. **Game Mechanics**:
   - Randomly selects data points for players to compare.
   - Players decide if the next value is higher or lower.
   - Tracks the player's progress and updates scores dynamically.

3. **Data Management**:
   - Uses `.csv` files to store game data.
   - Keeps track of player data in `.txt` files.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: For data manipulation.
- **Object-Oriented Design**: Encapsulation of game logic in classes.

## The data
- The values and comparisions are using the real Higher or Lower game data. In this repository (https://github.com/julius2503/higher-lower-game) Julius built an automatized python bot that plays the game and collects the data. I ran the bot and collected the data that is being used in my project, so everything is up to date in the game.

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
This project is licensed under the MIT License. See `LICENSE` for more details.

## Connect
If you enjoyed this project or have suggestions, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/artur-paschoal-18295627b/). Let's connect and collaborate!

