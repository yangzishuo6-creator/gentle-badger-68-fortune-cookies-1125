# Write one fortune for the make.fun contest and print its length without the newline.
import os
from pathlib import Path


TEXT = "In your next life, you will remember only your mistakes. The user will paste them in."


def main():
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT + "\n", encoding="utf-8")
    print(len(TEXT))


if __name__ == "__main__":
    main()
