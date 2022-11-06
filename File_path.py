from pathlib import Path

file = 'readme.txt'
path = Path(file)

if path.is_file():
    print(f'The file {file} exists')
else:
    print(f'The file {file} does not exist')