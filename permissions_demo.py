import os
import stat

filename = "demo_file.txt"
with open(filename, "w") as f:
    f.write("This is a demo file.\n")

os.chmod(filename, 0o775)

file_stat = os.stat(filename)
permissions = stat.filemode(file_stat.st_mode)
print(f"File '{filename}' permissions: {permissions}")