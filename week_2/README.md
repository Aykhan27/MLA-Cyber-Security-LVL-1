# Course Assignments: Detailed Guide

Welcome to your assignments guide. This document provides a step-by-step walkthrough of each task you're expected to complete, including commands and detailed explanations. Please follow these instructions closely and submit your solutions via GitHub as per the course requirements.

## Assignment 1: "Useless" Script Analysis

### Objective
Investigate a bash script named "useless" found in a user's home directory on a remote server accessible via SSH. The goal is to understand the script's functionality and uncover a hidden flag.

### Environment Access
- **SSH Details:**
  - Hostname: `saturn.picoctf.net`
  - Port: `*****` 
  - Username: `picoplayer`
  - Password: `*******`

### Instructions

1. **SSH into the Server**
   - Open your terminal.
   - Run the command: `ssh picoplayer@saturn.picoctf.net -p *****`
   - Enter the password when prompted.

2. **Locate the Script**
   - List files in the home directory: `ls`
   - You should see a file named `useless`.

3. **Examine the Script**
   - Display the content of the script: `cat useless`

4. **Analyze the Script's Functionality**
   - Note the operations performed by the script (addition, subtraction, etc.).
   - Pay attention to any echoes or comments that might hint at further actions or the location of the flag.

5. **Follow the Clues**
   - If the script suggests reading the manual or other files, use the `man` or `cat` commands respectively. For example, `man useless` or `cat <filename>`.

### Deliverable
Submit a document detailing each step taken, including commands used, any findings from the script analysis, and the discovered flag.

## Assignment 2: CVE Identification

### Objective
Identify the CVE number for the first recorded RCE vulnerability in 2021 related to the Windows Print Spooler Service.

### Instructions

1. **Research the Vulnerability**
   - Use a search engine or CVE databases to find information on the first RCE vulnerability in the Windows Print Spooler Service from 2021.

2. **Find the CVE Number**
   - Look for official security [advisories](https://msrc.microsoft.com/blog/2021/07/clarified-guidance-for-cve-2021-34527-windows-print-spooler-vulnerability/) or credible tech news articles reporting on the vulnerability.

### Deliverable
Provide a brief report that includes:
- The search terms used.
- The CVE number found.
- An explanation of the vulnerability's impact.

## Assignment 3: Cryptography Challenge - "Basic-Mod1"

### Objective
Decrypt a given message using a specific decryption scheme involving modulo operations.

### Instructions

1. **Download the Encrypted Message**
   - Use the provided link to download the message file.

2. **Write the Decryption Script**
   - Use Python or another programming language to write a script that:
     - Reads the encrypted numbers from the file.
     - Applies modulo 37 to each number.
     - Maps the result to the corresponding character as per the given character set.
   - Example Python snippet:
     ```python
     encrypted_numbers = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]  # Load numbers from the file
     character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
     decrypted_message = ''.join([character_set[n % 37] for n in encrypted_numbers])
     print(f"picoCTF{{{decrypted_message}}}")
     ```

3. **Run the Script**
   - Execute the script to decrypt the message.

### Deliverable
Submit the decryption script along with a document explaining the script's logic and the decrypted message.

## Assignment 4: Web Exploitation Challenges

### "Power Cookie" Challenge

#### Objective
Manipulate cookie values on a given website to reveal hidden content or functionalities.

#### Instructions

1. **Access the Website**
   - Use a web browser to visit the provided website URL.

2. **Inspect Cookies**
   - Right-click on the webpage and select "Inspect" or "Inspect Element".
   - Navigate to the "Application" or "Storage" tab to view cookies.
   - Look for a cookie named `isAdmin` and note its value.

3. **Modify the Cookie**
   - Change the value of the `isAdmin` cookie to `1`.
   - Refresh the page to check for changes in content or accessible functionalities.

### "Roboto Sans" Challenge

#### Objective
Discover a hidden flag by exploring unlinked or disallowed paths on a web application.

#### Instructions

1. **Check `/robots.txt`**
   - Access `http://http://saturn.picoctf.net:63195//robots.txt` in your browser.
   - Look for dis

allowed paths or directories that might contain hints.

2. **Decode Potential Clues**
   - If you find base64 encoded strings, decode them using online tools or commands like `echo 'ZmxhZzEudHh0;anMvbXlmaWanMvbXlmaWxlLnR4dA==' | base64 --d`.

3. **Follow the Paths**
   - Navigate to any discovered paths or files in your browser and look for the flag.

### Deliverables
For each web challenge, provide a detailed walkthrough of your exploration process, including any modified values, discovered paths, decoded strings, and the final flags.

## Custom Challenge: 

### SHA3-512 Hash Reversal

### Objective
Attempt to reverse a given SHA3-512 hash or explain why it's not feasible.

### Instructions

We can use `revHash.py` for execution our hased code using password list.

### WordPress Password Attack

#### Objective

The goal is to exploit vulnerabilities in a WordPress website's login system to gain unauthorized access to user accounts.

#### Instructions

1. **Initial Credentials:**
   - Username: think
   - Password: 123

2. **Discovery of Additional Username:**
   - While exploring the website, we notice a comment from the user `admin`. This indicates the presence of a second username, `admin`, which we need to find the password for.

3. **Attack Strategy:**
   - To avoid triggering security measures, we'll adopt a cautious approach:
     - First, we'll log in with the known credentials (`think` and `123`).
     - After successfully accessing the system, we'll attempt to log in as `admin` using a password list.

4. **Using BurpSuite:**
   - Through BurpSuite, we discover potential login credentials:
     - Username: admin
     - Password: #1mama

#### Action Plan

1. Log in with the initial credentials (`think` and `123`).
2. Upon successful login, attempt to log in as `admin` using the discovered password.