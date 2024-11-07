import pytest
import subprocess
import os
import sys
from difflib import Differ

def test_normal(projectsdir, wordlist):
    ''' Tests that the normalized word conforms to the regexp'''
    if sys.platform == "win32":
        khnormal = ['python', '-X', 'utf8', os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')]
    else:
        khnormal = [os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')]

    res = subprocess.check_output(khnormal + ["-n", "-f", f"{projectsdir}/{wordlist}"]).decode("utf-8")
    if len(res):
        print(res)
        if wordlist in ("bad_kh.txt", "cmo_words.txt", "cnd_words.txt"):
            pytest.xfail()
        else:
            pytest.fail()

def test_input(projectsdir, wordlist, updatedata):
    ''' Tests the input sequence to see if it is bad, before normalizing '''
    if sys.platform == "win32":
        khnormal = ['python', '-X', 'utf8', os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')]
    else:
        khnormal = [os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')]
    # khnormal = os.path.join(os.path.dirname(__file__), '..', 'python', 'scripts', 'khnormal')
    res = subprocess.check_output(khnormal + ["-N", "-n", "-f", f"{projectsdir}/{wordlist}"]).decode("utf-8")
    if not len(res):
        return
    lines = [s.strip() for s in res.split("\n") if len(s.strip())]
    failfile = os.path.join(os.path.dirname(__file__), 'failures', wordlist)
    if updatedata:
        with open(failfile, "w", encoding="utf-8") as outf:
            outf.write("\n".join(lines))
        return
    if not os.path.exists(failfile):
        faildat = ""
    else:
        with open(failfile, encoding="utf-8") as inf:
            faillines = [s.strip() for s in inf.readlines()]
    if lines != faillines:
        d = Differ()
        print("\n".join(d.compare(lines, faillines)))
        pytest.fail()

