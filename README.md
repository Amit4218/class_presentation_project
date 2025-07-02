# Riddle Me

- Live working url - [RiddleMe] https://infiniteamit.pythonanywhere.com/

## Overview

Riddle Me is a python-based-game designed to solve fun little riddles, when you are feeling bored. Riddle Me provides both "command-line interface (cli)" and a "web based GUI" to play the game.

## Features

- **Interactive Gameplay:** Engages users with a command-line or graphical interface.
- **Modular Codebase:** Organized into logical modules for easy maintenance and extension.
- **Score Tracking:** Keeps track of player progress and high scores.
- **Error Handling:** Robust input validation and exception management.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Amit4218/class_presentation_project.git
   cd singtam-class-python/game/api
   ```

2. **Install Dependencies:**
   ```bash
   uv pip install -r pyproject.toml
   ```

## Usage web(GUI)

Run the game with :

```bash
python main.py
```

Follow the on-screen instructions to play.

## Usage cli(GUI)

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Amit4218/class_presentation_project.git

   cd singtam-class-python/game/riddle-cli
   ```

2. **Install Dependencies:**

- for Linux and MacOs

  ```bash
  sudo chmod +x main.py  # giving execute permission

  mv main.py  /usr/local/bin/riddleMe

  cd .. && cd ..

  sudo rm -rf singtam-class-python

  ```

## Project Structure

```
api/
├── templates/        # html for the web version
├── db.py             # handels connection with db
├── main.py           # Entry point of the game
├── riddle-cli
├── main.py           # contains function for the cli tool
└── README.md         # Project documentation
```

## Configuration

- You can edit the `MongoClient("mongodb://localhost:27017/")` in the db.py file with your own Database if you have a collection of riddles yourself.

- Additionally you can also edit the `"https://infiniteamit.pythonanywhere.com//get-random-riddle-cli"` in the riddle-cli/main.py to your own url, if you have your own custom domain that is hosted on the internet, that serves riddles.

## Contributing

- Currently there are no plans of adding more function or feature to the project, but if you have a cool feature or idea feel free to open a pull request.
  </br>

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Support

For questions or support, open an issue on the [GitHub repository](https://github.com/Amit4218/class_presentation_project/issues).
