from src.game import Engine, Environment
from src.player import NaiveAi, AcceleratingAi


def track():
    track_name = Environment('assen')
    return track_name


def main():
    game_engine = Engine(
        environment=track(),
        players=[NaiveAi(), AcceleratingAi()]
    )

    game_engine.play()


if __name__ == "__main__":
    main()
