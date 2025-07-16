import subprocess, sys
result = subprocess.run(["flake8", "."], capture_output=True)
print(result.stdout.decode(), file=sys.stderr)
sys.exit(result.returncode)
