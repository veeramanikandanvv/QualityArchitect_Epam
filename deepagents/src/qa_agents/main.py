import argparse
import os
from dotenv import load_dotenv

from .supervisor import run_assessment


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Run the DeepAgents QA assessment workflow")
    parser.add_argument("--input", required=True, help="Assessment brief or documentation path")
    parser.add_argument("--output", default="./generated", help="Artifact output directory")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    args = parser.parse_args()
    result = run_assessment(args.input, args.output, args.model)
    print(result)


if __name__ == "__main__":
    main()
