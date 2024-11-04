import pytest
import subprocess
import os
from difflib import Differ

def test_normal(projectsdir, wordlist):
    khnormal = os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')
    res = subprocess.check_output([khnormal, "-n", "-f", f"{projectsdir}/{wordlist}"]).decode("utf-8")
    if len(res):
        print(res)
        if wordlist == "cmo_words.txt":
            pytest.xfail()
        else:
            pytest.fail()

def test_input(projectsdir, wordlist):
    khnormal = os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')
    res = subprocess.check_output([khnormal, "-N", "-n", "-f", f"{projectsdir}/{wordlist}"]).decode("utf-8")
    if len(res):
        failfile = os.path.join(os.path.dirname(__file__), 'failures', wordlist)
        if not os.path.exists(failfile):
            faildat = ""
        else:
            with open(failfile, encoding="utf-8") as inf:
                faildat = inf.read()
        if res != faildat:
            d = Differ()
            print("".join(d.compare(res, faildat)))
            pytest.fail()

