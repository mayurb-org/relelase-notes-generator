# Release Notes Generator

This script generates release notes for a software project based on two commit IDs. It retrieves the commit information using Git commands and utilizes the OpenAI GPT-3.5 language model to generate the release notes.

## Usage

1. Make sure you have Python installed on your system.

2. Install the required dependencies by running the following command:

   ```
   pip install openai
   ```

3. Set up the OpenAI API key by either:
   - Exporting your API key as an environment variable named `OPENAI_API_KEY`, or
   - Directly assigning your API key to the `openai.api_key` variable in the script.

4. Modify the `COMMIT_ID_1` and `COMMIT_ID_2` environment variables to the desired commit IDs.

5. Run the script using the following command:

   ```
   python release_notes_generator.py
   ```

6. The generated release notes will be displayed in the console.

## How It Works

1. The script uses the `retrieve_commit_info(commit_id)` function to retrieve the commit information for the given commit IDs. It utilizes Git commands executed through the subprocess module.

2. The commit information from both commit IDs is combined into a prompt string.

3. The script utilizes the OpenAI GPT-3.5 Turbo engine to generate the release notes. It sends the prompt string to the language model using the `openai.Completion.create()` function.

4. The generated release notes are extracted from the response and returned as a string.

## Dependencies

- Python 3.x
- openai Python library

## Limitations

- The script has a default limit of 200 tokens for the generated release notes. If the release notes exceed this limit, they may be truncated. You can adjust the `max_tokens` parameter in the `openai.Completion.create()` function to accommodate longer release notes.

- The script assumes that the Git command is available in the system's PATH variable. Make sure you have Git installed and properly configured.

- The OpenAI GPT-3.5 Turbo engine has usage limits and may incur costs depending on your OpenAI subscription plan. Refer to the OpenAI documentation for more details.

## License

This script is released under the [MIT License](LICENSE). Feel free to modify and distribute it according to your needs.
