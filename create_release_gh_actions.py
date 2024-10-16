import subprocess, os
set_new_version = None

def set_release_version():
    try:
        global set_new_version
        with open("version.txt", "r") as file:
            version = file.read()
            list_version = version.split(".")
            new_version = int(list_version[0]) + 1
        with open("version.txt", "w") as file:
            file.write(f"{new_version}.0.0")
        set_new_version = f"{new_version}.0.0"
    except FileNotFoundError as file_error:
        print(f'File not Found: {file_error}')
        exit()
    except ValueError as value_error:
        print(f'File is empty or is not an int: {value_error}')
        exit()
    

def update_version_in_dev_branch():
    github_actor = os.environ.get('GITHUB_ACTOR')
    set_user_identity = subprocess.run(['git', 'config', '--global', 'user.name', f'"{github_actor}"'])
    set_email = subprocess.run(['git', 'config', '--global', 'user.email', 'github-actions[bot]@users.noreply.github.com'])
    add_new_version_file_to_dev_branch = subprocess.run(['git', 'add', 'version.txt'], capture_output=True, text=True)
    commit_new_version_to_dev_branch = subprocess.run(['git', 'commit', '-m', f'"bump version to {set_new_version}"'], capture_output=True, text=True)
    push_new_version_to_dev_branch = subprocess.run(['git', 'push'], capture_output=True, text=True)
    print(set_user_identity, set_email)
    print(add_new_version_file_to_dev_branch, commit_new_version_to_dev_branch, push_new_version_to_dev_branch)

def create_release_branch():
    create_release_branch = subprocess.run(['git', 'branch', f'release/{set_new_version}'], capture_output=True, text=True)
    push_release_branch = subprocess.run(['git', 'push', 'origin', f'release/{set_new_version}'], capture_output=True, text=True)
    print(create_release_branch, push_release_branch)

set_release_version()
update_version_in_dev_branch()
create_release_branch()