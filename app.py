import subprocess

def add(a, b):
    return a + b

def run(cmd):
    return subprocess.run(cmd, shell=True)
