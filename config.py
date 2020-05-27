from pathlib import Path

current_directory = str(Path.cwd())
password_folder = 'passwords'
password_file = 'passwords.txt'

PATH = str(Path(current_directory, password_folder, password_file))
