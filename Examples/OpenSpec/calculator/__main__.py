"""Allow running the calculator as ``python -m calculator``."""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
