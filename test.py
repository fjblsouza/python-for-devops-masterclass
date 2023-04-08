import subprocess

cmd = "df -Th"

# returns output
returned_value = subprocess.call(cmd, shell=True)

print()