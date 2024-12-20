# Higher or Lower Game 🎮

Welcome to the **Higher or Lower** game! This interactive game challenges players to guess whether one item's search volume is higher or lower than another. A perfect game for fun and learning!

## 📖 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How to Contribute](#how-to-contribute)
- [License](#license)

---

## 🌟 Features
- **Player Profiles**: Create, manage, and save individual player profiles.
- **Score Tracking**: Tracks high scores and last game scores for each player.
- **Real-time Updates**: Player data is saved and updated in real time.
- **No Repetition**: Ensures that previously shown items do not repeat during a session.
- **Interactive CLI**: User-friendly command-line interface.
- **Data-Driven**: Loads game items and player data from external files (CSV and TXT).

---

## 🛠 Installation

### Prerequisites
- Python 3.8+
- A terminal or command prompt to run the game.

### Clone the Repository
```bash
git clone https://github.com/your-username/HigherOrLower.git
cd HigherOrLower
```

### Install Dependencies
This project uses **pytest** for testing. Install it using:
```bash
pip install pytest
```

---

## 🚀 Usage

### Run the Game
To start the game, navigate to the `src` folder and run:
```bash
python main.py
```

### Play the Game
1. Choose a player or create a new one.
2. Start the game, and guess if the second item has higher or lower searches.
3. Your score and progress will be saved automatically.

### Run Tests
To ensure everything is working properly, run:
```bash
pytest tests/
```

---

## 📂 Project Structure
```
HigherOrLower/
├── data/
│   ├── game_data_with_formatting.csv   # Game items with search data
│   └── player_data.txt                 # Player profiles and scores
├── src/
│   ├── core/                           # Core game logic
│   │   ├── game.py                     # Main game logic
│   │   └── player.py                   # Player management
│   ├── utils/                          # Utility functions
│   │   ├── file_handler.py             # File operations
│   │   ├── game_data.py                # Game data operations
│   │   └── display.py                  # Display utilities
│   └── main.py                         # Entry point for the game
├── tests/                              # Unit tests
│   ├── core/                           # Tests for core logic
│   └── utils/                          # Tests for utility functions
└── README.md                           # Documentation
```

---

## 🤝 How to Contribute

We welcome contributions! Follow these steps:
1. **Fork the repository**: Click on the fork button at the top right of this page.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/HigherOrLower.git
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/new-feature
   ```
4. **Commit your changes**:
   ```bash
   git commit -m "Add a new feature"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/new-feature
   ```
6. **Create a pull request**: Go to the original repository and click on "New Pull Request".

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 🛡️ Disclaimer
This game is a fun project and uses fictitious data for demonstration purposes. It is not responsible for real-world accuracy of search volumes.

---

## 💡 Acknowledgments
- Inspired by the "Higher or Lower" concept.
- Built with love using Python. 💻❤️

