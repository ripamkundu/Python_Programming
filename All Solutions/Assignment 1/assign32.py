# Safely Create a Nested Directory

import os
try:
    os.makedirs("python/assign/pyploting/directory")
except FileExistsError:
    print("File already exists")