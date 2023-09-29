from pathlib import Path
import os

def get_root_dir():
    return Path(__file__).parent.parent


if __name__ == "__main__":
    print(get_root_dir())