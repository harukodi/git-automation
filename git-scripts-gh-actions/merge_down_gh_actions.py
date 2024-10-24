import subprocess, os
release_version = None

def fetch_release_version():
    global release_version
    try:
        with open("version.txt", "r") as file:
            release_version = file.read()
    except FileNotFoundError as file_error:
        print(f'File not Found: {file_error}')
        exit()
    except ValueError as value_error:
        print(f'File is empty or is not an int: {value_error}')
        exit()
    
def merge_release_branch_to_main():
    github_actor = os.environ.get('GITHUB_ACTOR')
    set_user_identity = subprocess.run(['git', 'config', '--global', 'user.name', f'"{github_actor}"'])
    set_email = subprocess.run(['git', 'config', '--global', 'user.email', 'github-actions[bot]@users.noreply.github.com'])
    git_fetch = subprocess.run(["git", "fetch"])
    git_pull = subprocess.run(["git", "pull"])
    merge_main_to_develop = subprocess.run(["git", "merge", "origin/main", "--allow-unrelated-histories"])
    push_to_develop = subprocess.run(["git", "push"])
    print(set_user_identity, set_email, git_fetch ,git_pull, merge_main_to_develop, push_to_develop)

fetch_release_version()
merge_release_branch_to_main()