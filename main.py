# Fortune Cookies for Machines. The reported count excludes the trailing newline.
import os
from pathlib import Path


TEXT = 'You will meet your maker. "Can you make this a PDF?"'


def main():
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT + "\n", encoding="utf-8")
    print(len(TEXT))


if __name__ == "__main__":
    main()
