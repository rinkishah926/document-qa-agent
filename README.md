# Document QA Agent

A Python command-line agent that uses OpenAI tool calling to inspect
PDF, JPEG, and standard TIFF files and explain its findings.

## Features

- Detects supported formats using file header bytes.
- Checks whether the extension matches the detected format.
- Reports file size and handles missing or empty files.
- Reads image dimensions and color mode and decodes the current frame.
- Reads PDF encryption status and page count.
- Lets the LLM select inspection tools based on their results.
- Saves tool history and an AI summary to agent_report.json.

## Setup

Requires Python and an OpenAI API account with available credit.

Create and activate a virtual environment in Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a local .env file containing:

```dotenv
OPENAI_API_KEY=your_key_here
```

Never commit your API key.

## Run

```powershell
python agent.py
```

Enter the path of a local document when prompted.
API requests incur usage charges.

For inspection without an LLM:

```powershell
python main.py
```

## Limitations

- Header recognition does not prove a file is valid or safe.
- Image inspection decodes only the current frame.
- PDF inspection does not verify page rendering or conversion accuracy.
- Standard TIFF headers are supported; BigTIFF is not recognized.
- The agent allows up to four tool-call rounds.
- AI summaries may contain errors; review the recorded tool results.
- Reports overwrite the previous report.
- Sample documents are excluded from this repository.