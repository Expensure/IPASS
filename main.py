from src.game import Engine, Environment
from src.player import NaiveAi


def track():
    track_name = Environment('monaco')
    return track_name


def main():
    game_engine = Engine(
        environment=track(),
        players=[NaiveAi()]
    )

    game_engine.play()


if __name__ == "__main__":
    main()
