from src.game import Engine, Environment
from src.player import NaiveAi, HumanPlayer


def track():
    track_name = Environment('hockenheim')
    return track_name


def main():
    game_engine = Engine(
        environment=track(),
        players=[NaiveAi(), HumanPlayer()]
    )

    game_engine.play()


if __name__ == "__main__":
    main()
