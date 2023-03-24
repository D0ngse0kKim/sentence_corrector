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
    * Default settings is `gpt-3.5-turbo`.
    * Model in `/v1/chat/completions` in [Model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility) is available.
* `--verbose, -v` : Print the number of tokens consumed.
* `--reason, -r` : Print the reason of the correction.

## Usage example

### Simple Correction - 1

#### Command

```bash
python -m sentence_corrector "It is possible to implement only a part of the method required by protocols."
```

#### Response

```bash
The sentence is grammatically correct as it is. However, if you want to make it more clear, you can rephrase it as "It is possible to partially implement the method required by protocols."
```

### Simple Correction - 2

Print corrected sentences with reasons of correction.

#### Example of command

```bash
python -m sentence_corrector "new `Vector` class uses [`array.array()`](https://docs.python.org/3/library/array.html) to store values of its component" -r
```

#### Example of response

```bash
"New `Vector` class uses [`array.array()`](https://docs.python.org/3/library/array.html) to store values of its components."

The correction is changing "component" to "components" to match the plural form of "values" and make the sentence grammatically correct.
```

### Complex Correction

It is possible to correct sentences including vocabulary in multiple languages.

#### Example of command

```bash
python -m sentence_corrector "Class is プロトコールで定めるタイプのように働く by implementing methods required by protocol." -r
```

#### Example of response

```bash
The corrected sentence is: "The class works like a protocol-defined type by implementing the required methods."

The original sentence appears to be a direct translation from Japanese, which leads to a wordy and awkward sentence structure. The corrected sentence simplifies the phrasing while still conveying the same meaning.
```
