import subprocess
set_new_version = ""

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
    
def create_release_branch():
    create_release_branch_command = subprocess.run(['git', 'branch', f'release/{set_new_version}'], capture_output=True, text=True)
    push_release_branch_command = subprocess.run(['git', 'push', 'origin', f'release/{set_new_version}'], capture_output=True, text=True)
    print(create_release_branch_command)
    print(push_release_branch_command)

def release_to_main():
    switch_to_main = subprocess.run(['git', 'switch', 'main'], capture_output=True, text=True)
    merge_release_to_main = subprocess.run(['git', 'merge', f'release/{set_new_version}'], capture_output=True, text=True)
    add_file = subprocess.run(['git', 'add', '.'])
    commit_to_main = subprocess.run(['git', 'commit', '-m', f'"{set_new_version}"'])
    push_to_main = subprocess.run(['git', 'push'])
    print(switch_to_main)
    print(merge_release_to_main)
    print(add_file)
    print(commit_to_main)
    print(push_to_main)

set_release_version()
create_release_branch()
release_to_main()