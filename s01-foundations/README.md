 DFCS Day 1 Assignment: Foundations
Name: Muhammad Ahmad  
Student ID: TRN-2026-000446  
Course: PSEB Digital Forensics & Cyber Security  
Submission Date: 8 november  2026

ask A: Malware Types and Analysis

Malware Reference Table

| Type | Definition | Named Example and Year | How It Spread | Primary Impact |
| --- | --- | --- | --- | --- |
| Virus | Code attached to a normal file that runs when opened. | ILOVEYOU (2000) | Opened an infected email attachment. | Deleted user files and auto-emailed itself to contacts. |
| Worm | Malware that spreads across a network automatically without user action. | WannaCry (2017) | Exploited a network flaw in Windows SMB. | Locked entire hard drives and demanded bitcoin ransom. |
| Trojan | Fake program disguised as safe software to trick you into downloading it. | Zeus (2007) | Shady download sites and phishing links. | Stole online banking logins and passwords. |
| Ransomware | Locks all your files and demands money for the unlock key. | Colonial Pipeline (2021) | Stolen VPN login details without two-factor authentication[cite: 2]. | Forced a major fuel pipeline to completely shut down[cite: 2]. |
| Spyware | Secret software that tracks what you do and steals personal data. | Pegasus (2016) | Zero-click security flaws in messaging apps. | Secretly recorded calls, read texts, and tracked location. |
| Adware | Displays annoying pop-up ads and hijacks your browser settings. | Fireball (2017) | Came bundled inside free software installers. | Redirected search results to ad sites and tracked web activity. |
| Rootkit | Gives an attacker admin access while hiding itself from antivirus software. | Stuxnet (2010) | Infected USB drives plugged into computers. | Changed industrial machine controls while displaying fake safe readings[cite: 2]. |
| Keylogger | Records every single key you press on your keyboard. | Snake Keylogger (2020) | Malicious file attachments in fake emails. | Stole saved passwords, credit card numbers, and typed notes. |
| Botnet Agent | Turns your computer into a zombie node controlled by a hacker. | Mirai (2016) | Guessed default passwords on smart devices using Telnet. | Used infected devices to crash websites with traffic floods[cite: 3]. |
| Fileless / LotL | Hides in system RAM and uses built-in OS tools to execute attacks. | Astaroth (2019) | Web links that ran built-in commands like WMIC quietly. | Avoided antivirus detection because no malicious files were saved to disk. |
| Logic Bomb | Secret code set to trigger an attack on a specific date or event. | Siemens Insider Bomb (2016) | Sneakily added into custom code by a company employee. | Broke software spreadsheets every few months to force paid support calls. |
| Bootkit | Advanced malware that infects the boot system before the OS even loads. | Rovnix (2011) | Infected document attachments and web downloads. | Took control of the system before any antivirus tools could start up. |

Threat Analysis for Pakistani SMEs

Ransomware is the most dangerous threat to Pakistani SMEs because most small businesses do not keep offline or external backups of their critical files. Many local companies operate with small IT budgets, leaving remote desktop connections exposed to the internet with weak passwords or unpatched software.
 If ransomware encrypts their accounting records or client data, operations stop completely, and many businesses cannot recover from the financial loss.

Task B2: Linux Permissions Demonstration

Command Execution Log

kali@kali:~/dfcs-bootcamp/s01-foundations$ echo "Top Secret Data" > sample.txt
kali@kali:~/dfcs-bootcamp/s01-foundations$ ls -l sample.txt
-rw-rw-r-- 1 kali kali 16 Nov 2 13:18 sample.txt

kali@kali:~/dfcs-bootcamp/s01-foundations$ chmod u+x,o-r sample.txt
kali@kali:~/dfcs-bootcamp/s01-foundations$ ls -l sample.txt
-rwxrw---- 1 kali kali 16 Nov 2 13:19 sample.txt

kali@kali:~/dfcs-bootcamp/s01-foundations$ chmod 755 sample.txt
kali@kali:~/dfcs-bootcamp/s01-foundations$ ls -l sample.txt
-rwxr-xr-x 1 kali kali 16 Nov 2 13:20 sample.txt

kali@kali:~/dfcs-bootcamp/s01-foundations$ chmod 600 sample.txt
kali@kali:~/dfcs-bootcamp/s01-foundations$ ls -l sample.txt
-rw------- 1 kali kali 16 Nov 2 13:21 sample.txt

Explanation of Permission Changes

1. chmod u+x,o-r sample.txt (Symbolic Mode)
Added execute access (+x) for the file owner (u), and removed read access
 (-r) for all other users (o)[cite: 6].

2. chmod 755 sample.txt (Octal Mode)
Gives full read, write, and execute permissions (7) to the owner, 
while giving read and execute permissions (5) to the group and other users[cite: 6].

3. chmod 600 sample.txt (Octal Mode)
Gives read and write permissions (6) exclusively to the owner,
 while blocking all access (0) for everyone else[cite: 6]. 
This is the safest setting for private files like SSH keys[cite: 6].


Task B3: Caesar Cipher Decoder

Python Script Execution Output

Ciphertext: KDFNHU
========================================
Shift -01: JCEMGT
Shift -02: IBDLFS
Shift -03: HACKER
Shift -04: GZBJDQ
Shift -05: FYAICP
Shift -06: EXZHBO
Shift -07: DWYGAN
Shift -08: CVXFZM
Shift -09: BUWEYL
Shift -10: ATVDXK
Shift -11: ZSUCWJ
Shift -12: YRTBVI
Shift -13: XQSAUH
Shift -14: WPRZTG
Shift -15: VOQYSF
Shift -16: UNPXRE
Shift -17: TMOWQD
Shift -18: SLNVPC
Shift -19: RKMUOB
Shift -20: QJLTNA
Shift -21: PIKSMZ
Shift -22: OHJRLY
Shift -23: NGIQKX
Shift -24: MFHPJW
Shift -25: LEGOIV
