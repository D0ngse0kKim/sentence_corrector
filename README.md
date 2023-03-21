# sentence_corrector

A sentence corrector using [GPT-3 API](https://platform.openai.com/overview).

## Prerequisites

[API key](https://platform.openai.com/account/api-keys) and [Organization ID](https://platform.openai.com/account/org-settings) of OpenAI API is needed.

Set your API key into environment variable `OPENAI_API_KEY`, and your organization ID into environment variable `OPENAI_ORG_ID`.

This can be done by using the following commands in linux or macOS.

```bash
export OPENAI_API_KEY=YOUR-API-KEY
export OPENAI_ORG_ID=YOUR-ORGANIZATION-ID
```

`.env` file can be used to set the environment variables. Below is the example of `.env` file.

```
OPENAI_API_KEY=YOUR-API-KEY
OPENAI_ORG_ID=YOUR-ORGANIZATION-ID
```

## Setup

Clone this repository and `python -m pip install .`.
```bash
python -m pip install .
```

## Usage

```
python -m sentence_corrector [-h] [--temperature TEMPERATURE] [--model MODEL] [--verbose] [sentence]
```

## Arguments

### Positional Arguments

* `sentence` : The sentence to correct
* If `sentence` is not specified, sentences from `stdin` will be corrected.

### Options

* `-h`, `--help`  : show help message and exit
* `--temperature TEMPERATURE` : Sampling temperature to use
    * Default settings is 0.7.
    * See [this](https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature) for details.
* `--model MODEL` : ID of model to use
    * Default settings is `text-davinci-002`.
    * Model in `/v1/completions` in [Model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility) is available.
* `--verbose, -v` : Print the number of tokens consumed.
* `--reason, -r` : Print the reason of the correction.
