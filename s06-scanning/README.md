# Session 02: Network Scanning and Vulnerability Assessment

Author: Muhammad Ahmad
Target Host: 192.168.56.102 (Metasploitable 2)
Attacker Host: 192.168.56.103 (Kali Linux - Dual Adapter Setup)

---

## Task A: Compulsory Vulnerability Findings

### Finding 1: Remote Code Execution via vsftpd 2.3.4 Backdoor

Title: FTP Backdoor Command Execution in vsftpd 2.3.4
Severity: 9.8 Critical (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
Affected Asset: 192.168.56.102:21/tcp (vsftpd 2.3.4)
Identifiers: CVE-2011-2523 / CWE-78

- Description: The distributed vsftpd 2.3.4 source code contained a backdoor added between June 30 and July 3, 2011. Supplying a username ending in :) opens a command shell on TCP port 6200.
- Evidence: Scan performed using nmap -p 21 --script ftp-vsftpd-backdoor.nse 192.168.56.102 returned VULNERABLE: vsFTPd version 2.3.4 backdoor.
- Proof of Concept:
  1. Connect via FTP: ftp 192.168.56.102
  2. Username: hacker:)
  3. Connect via Netcat: nc 192.168.56.102 6200
  4. Run command: id
- Impact: Full root command execution.
- Remediation: Upgrade vsftpd to a clean release and verify package signatures.

---

### Finding 2: Information Disclosure via Exposed phpinfo() File

Title: Sensitive Information Exposure via /phpinfo.php
Severity: 5.3 Medium (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)
Affected Asset: 192.168.56.102:80/tcp (Apache httpd 2.2.8)
Identifiers: CWE-200

- Description: The web server hosts /phpinfo.php which exposes PHP compilation flags, system paths, loaded modules, and kernel details.
- Evidence: Scan performed using nmap -p 80 --script http-enum.nse 192.168.56.102 returned /phpinfo.php page present.
- Proof of Concept: Run curl -s http://192.168.56.102/phpinfo.php | head -n 15 to view exposed headers without login.
- Impact: Provides operational details for planning targeted attacks.
- Remediation: Delete phpinfo.php or restrict web access.

---

### Finding 3: Unauthenticated Access via Anonymous FTP

Title: Anonymous FTP Service Configuration
Severity: 5.3 Medium (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)
Affected Asset: 192.168.56.102:21/tcp (vsftpd 2.3.4)
Identifiers: CWE-284 / CWE-306

- Description: The FTP server allows anonymous login using username anonymous with no password.
- Evidence: Scan performed using nmap -p 21 --script ftp-anon.nse 192.168.56.102 returned Anonymous FTP login allowed.
- Proof of Concept: Connect via ftp 192.168.56.102 and enter anonymous to log in.
- Impact: Unauthorized users can list and download public files.
- Remediation: Set anonymous_enable=NO in /etc/vsftpd.conf.

---

## Task B: Optional Tasks

### Option B3: Decoded CVSS Vector Metrics (CVE-2011-2523)

Vector String: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

- Attack Vector (AV:N): Network remote access
- Attack Complexity (AC:L): Low complexity
- Privileges Required (PR:N): No privileges needed
- User Interaction (UI:N): No user interaction needed
- Scope (S:U): Unchanged scope
- Confidentiality (C:H): High impact
- Integrity (I:H): High impact
- Availability (A:H): High impact

---

### Option B6: vsftpd 2.3.4 Supply-Chain Compromise Analysis

Between June 30 and July 3, 2011, an attacker modified vsftpd-2.3.4.tar.gz on the main download server to include a backdoor in str_replace_text.c listening on port 6200. Linux distributions maintaining signed package mirrors were unaffected, showing the necessity of cryptographic signature validation.
