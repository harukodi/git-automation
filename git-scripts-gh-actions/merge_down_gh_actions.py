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
    git_fetch = subprocess.run(["git", "fetch"])
    checkout_to_main_branch = subprocess.run(["git", "checkout", "main"])
    git_pull = subprocess.run(["git", "pull"])
    merge_release_branch_to_main = subprocess.run(["git", "merge", f"origin/release/{release_version}"])
    push_to_main = subprocess.run(["git", "push"])
    print(git_fetch, checkout_to_main_branch, git_pull, merge_release_branch_to_main, push_to_main)
    

fetch_release_version()
merge_release_branch_to_main()
