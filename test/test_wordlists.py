import pytest
import subprocess
import os

def test_normal(projectsdir, wordlist):
    khnormal = os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')
    res = subprocess.check_output([khnormal, "-n", "-f", f"{projectsdir}/{wordlist}"]).decode("utf-8")
    if len(res):
        print(res)
        if wordlist == "cmo_words.txt":
            pytest.xfail()
        else:
            pytest.fail()
