import argparse

from src.media import MediaPlayer

parser = argparse.ArgumentParser()
parser.add_argument("-album", type=str)
args = parser.parse_args()


def main():
    player = MediaPlayer(album=args.album)
    player.play(file_=player.files)


if __name__ == '__main__':
    main()
