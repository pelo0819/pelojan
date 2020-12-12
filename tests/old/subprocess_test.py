import sys
import subprocess

cp = subprocess.run(['ls', '-la'], stdout = subprocess.PIPE)
print(cp.stdout)
