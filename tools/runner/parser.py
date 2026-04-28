# runner/parser.py

def parse_command(input_str: str):
    parts = input_str.strip().split()

    command = parts[0]
    args = parts[1:]

    return {
        "command": command,
        "issue_key": args[0] if args else None,
        "extra": " ".join(args[1:]) if len(args) > 1 else None
    }