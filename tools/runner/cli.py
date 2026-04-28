# runner/cli.py

import sys
from runner.orchestrator import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python runner/cli.py /qa.enrich.jira QA-123")
        sys.exit(1)

    command_input = " ".join(sys.argv[1:])

    run(command_input)