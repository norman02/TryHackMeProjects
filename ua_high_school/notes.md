# U.A. Highschool CTF

## Recon
1. nmap -sS -oN nmap_initial.txt gives us open ssh and http ports. Lets get detail on the http port 
2. nmap -A -p80 -oN nmap_http.txt school.thm we have an apache web server running lets go ahead and look at the website
3. The webiste has a few forms but non seem functional there doesn't seem to be anything interesting in the sorce code.
4. gobuster dir -u http://school.thm -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 50 reveals only /assets and /server-status
5. Wild goose chase with Japanese word lists
6. the hint says be suspicous of any unused files lets look for files; we find an index.php

