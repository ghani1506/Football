import random
from dataclasses import dataclass

DIRECTIONS = ["Left", "Center", "Right"]

@dataclass
class ShotResult:
    shot_direction: str
    keeper_direction: str
    is_goal: bool
    message: str

def keeper_save_chance(difficulty: str) -> float:
    """Return probability that the goalkeeper guesses correctly."""
    difficulty = difficulty.lower()
    if difficulty == "easy":
        return 0.25
    if difficulty == "medium":
        return 0.38
    if difficulty == "hard":
        return 0.52
    return 0.38

def take_penalty(shot_direction: str, difficulty: str = "Medium") -> ShotResult:
    """Simulate one penalty shot."""
    chance = keeper_save_chance(difficulty)

    # Keeper is more likely to guess correctly at higher difficulty.
    if random.random() < chance:
        keeper_direction = shot_direction
    else:
        keeper_direction = random.choice([d for d in DIRECTIONS if d != shot_direction])

    is_goal = keeper_direction != shot_direction

    if is_goal:
        message = "GOAL! The goalkeeper dived the wrong way."
    else:
        message = "SAVED! The goalkeeper guessed your direction."

    return ShotResult(
        shot_direction=shot_direction,
        keeper_direction=keeper_direction,
        is_goal=is_goal,
        message=message
    )

def result_emoji(result: ShotResult) -> str:
    if result.is_goal:
        return "⚽🥅 GOAL!"
    return "🧤 SAVED!"
