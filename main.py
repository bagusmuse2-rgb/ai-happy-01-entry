"""Entry for make.fun bounty ai-happy-01 - "Make the AI judge happy".

The program writes one image to /output/entry.png: a kitten and a puppy
laughing together at a birthday party. It simply copies the image stored
in this repository (happy.png), so every run writes exactly the same bytes.
No network, no randomness, no inputs.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "happy.png")
OUTPUT = os.path.join("/output", "entry.png")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
