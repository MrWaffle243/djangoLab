# Source - https://stackoverflow.com/a
# Posted by Carl Meyer, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-19, License - CC BY-SA 4.0
import sys

def in_venv():
    return sys.prefix != sys.base_prefix

print(in_venv())
