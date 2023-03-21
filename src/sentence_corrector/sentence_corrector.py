import argparse
import os
import sys
from typing import Any

import openai
from dotenv import load_dotenv


def parse_argument() -> argparse.Namespace:
    # Define the command-line argument parser
    parser = argparse.ArgumentParser(
        description="Correct a sentence using GPT-3"
    )
    parser.add_argument(
        "sentence", help="The sentence to correct", nargs="?", default=None
    )
    parser.add_argument(
        "--temperature",
        help="Sampling temperature to use",
        default=0.7,
        type=float,
    )
    parser.add_argument(
        "--model",
        help="ID of model to use",
        default="text-davinci-002",
        type=str,
    )
    parser.add_argument(
        "--verbose",
        "-v",
        help="Print the number of tokens consumed.",
        action="store_true",
    )
    parser.add_argument(
        "--reason",
        "-r",
        help="Print the reason of correction.",
        action="store_true",
    )

    # Parse the command-line arguments
    return parser.parse_args()


def gen_configs(args: argparse.Namespace) -> dict[str, Any]:
    return vars(args)


def init_openai() -> None:
    load_dotenv()

    openai.api_key = os.environ["OPENAI_API_KEY"]
    openai.organization = os.environ["OPENAI_ORG_ID"]


# Define the function to correct a sentence using GPT-3
def correct_sentence(sentence: str, configs: dict[str, Any]) -> str:
    # Define the model ID to use for the correction task
    # For details, refer https://platform.openai.com/docs/models/model-endpoint-compatibility
    # Model for Endpoint /v1/completions is available
    model_engine: str = configs["model"]

    # Format the input for the GPT-3 API
    if configs["reason"] is not True:
        prompt = f"Correct this sentence: \n{sentence}\n"
    else:
        prompt = f"Correct this sentence and explain the reason for the correction. :\n{sentence}\n"

    # Use the GPT-3 API to generate a corrected version of the sentence
    # For details, refer https://platform.openai.com/docs/api-reference/completions/create
    temperature: float = float(configs["temperature"])
    response = openai.Completion.create(  # type: ignore
        engine=model_engine,
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=temperature,
    )

    # Extract the corrected sentence from the API response
    returned_text: str = response.choices[0].text  # type: ignore
    corrected_sentence = returned_text.strip()

    # If verbose is true, print the number of tokens consumed.
    if configs["verbose"] is True:
        usage: dict[str, int] = response.usage
        print(f'Number of prompt tokens consumed: {usage["prompt_tokens"]}')
        print(
            f'Number of completion tokens consumed: {usage["completion_tokens"]}'
        )
        print(f'Number of total tokens consumed: {usage["total_tokens"]}')

    # Return the corrected sentence
    return corrected_sentence


def main() -> None:
    args: argparse.Namespace = parse_argument()
    configs: dict[str, str] = gen_configs(args)

    init_openai()

    if args.sentence is not None:
        print(correct_sentence(args.sentence, configs))
    elif args.sentence is None:
        print(correct_sentence(sys.stdin.read(), configs))
