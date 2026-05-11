# Interactive Football Game – Streamlit + Python

A simple interactive football penalty shootout game built with Python as the backend and Streamlit as the deployment platform.

## Game Features
- Choose your shooting direction
- Goalkeeper reacts automatically
- Score tracking
- 5-shot penalty round
- Difficulty levels
- Replay/reset button
- Deployable on Streamlit Community Cloud
- GitHub-ready project structure

## Folder Structure
```text
streamlit_football_game/
├── app.py
├── game_engine.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository.
2. Upload all files from this folder.
3. Go to https://streamlit.io/cloud
4. Click **New app**.
5. Select your GitHub repository.
6. Set the main file path to:

```text
app.py
```

7. Click **Deploy**.

## Suggested Repository Name

```text
interactive-football-game-streamlit
```
