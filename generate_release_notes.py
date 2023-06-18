import os
import subprocess
import openai

def retrieve_commit_info(commit_id):
    # Use Git command to retrieve commit information based on commit_id
    commit_info = subprocess.check_output(f"git show {commit_id}", shell=True, text=True)
    return commit_info

def generate_release_notes(commit_id_1, commit_id_2):
    commit_info_1 = retrieve_commit_info(commit_id_1)
    commit_info_2 = retrieve_commit_info(commit_id_2)

    prompt = f"## Changes made in commit {commit_id_1}\n{commit_info_1}\n\n## Changes made in commit {commit_id_2}\n{commit_info_2}\n\n## Release Notes:"
    
    openai.api_key = os.environ["OPENAI_API_KEY"]  # Retrieve API key from environment variable

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
        model="gpt-3.5-turbo"
    )

    release_notes = response.choices[0].text.strip()
    return release_notes

if __name__ == "__main__":
    commit_id_1 = os.environ.get("COMMIT_ID_1")
    commit_id_2 = os.environ.get("COMMIT_ID_2")
    release_notes = generate_release_notes(commit_id_1, commit_id_2)
    print(release_notes)
