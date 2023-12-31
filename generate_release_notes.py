import os
import subprocess
import openai

def retrieve_commit_info(commit_id):
    # Use Git command to retrieve commit information based on commit_id
    commit_info = subprocess.check_output(f"git show --stat {commit_id}", shell=True, text=True)
    return commit_info

def generate_release_notes(commit_id_1, commit_id_2):
    commit_range = get_commit_range(commit_id_1, commit_id_2)

    release_notes = ""
    for commit_id in commit_range:
        commit_info = retrieve_commit_info(commit_id)
        release_notes += f"- **Changes made in commit {commit_id}**:\n{commit_info}\n\n"

    prompt = f"## Release Notes:\n{release_notes}"
    
    openai.api_key = os.environ["OPENAI_API_KEY"]  # Retrieve API key from environment variable

    # Split the prompt into chunks to fit within the model's maximum context length
    prompt_chunks = split_prompt(prompt, max_tokens=4096)
    response_chunks = []

    for chunk in prompt_chunks:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "/start"},
                {"role": "user", "content": chunk}
            ]
        )
        response_chunks.append(response.choices[0].message.content)

    release_notes = " ".join(response_chunks).strip()
    return release_notes

def get_commit_range(commit_id_1, commit_id_2):
    cmd = f"git rev-list --reverse {commit_id_1}..{commit_id_2}"
    commit_range = subprocess.check_output(cmd, shell=True, text=True).splitlines()
    return commit_range

def split_prompt(prompt, max_tokens):
    prompt_tokens = prompt.split()
    chunks = []
    current_chunk = ""

    for token in prompt_tokens:
        if len(current_chunk) + len(token) < max_tokens:
            current_chunk += token + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = token + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

if __name__ == "__main__":
    commit_id_1 = os.environ.get("COMMIT_ID_1")
    commit_id_2 = os.environ.get("COMMIT_ID_2")
    release_notes = generate_release_notes(commit_id_1, commit_id_2)
    print(release_notes)