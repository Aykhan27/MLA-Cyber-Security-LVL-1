# Project Overview

This document outlines the projects you need to complete, categorized by difficulty. Each project is designed to test your skills in cybersecurity, with a focus on practical application. Follow the detailed instructions and provide your solutions as instructed.

## Project 1: "Safe Opener 2" Challenge

### Objective:
Retrieve the lost key to unlock a virtual safe by analyzing a Java class file named `SafeOpener.class`.

### Instructions:

1. **Download the File:**
   - Acquire the `SafeOpener.class` file from the provided source.

2. **Decompile the Java Class:**
   - Use a Java decompiler to convert the `.class` file back into readable Java code.
   - Command: `jd-gui SafeOpener.class`
   - Tool Suggestion: JD-GUI is a standalone graphical utility that displays Java source codes of `.class` files.

3. **Analyze the Decompiled Code:**
   - Review the Java code displayed by the decompiler to locate the section where the key (flag) is defined or used.

4. **Retrieve the Key:**
   - Document the process of how you located the key within the decompiled code.

### Deliverable:
Submit a report detailing the decompilation process, including screenshots of the decompiled code where the key is visible, and the retrieved key itself.

## Custom Project 1: Bypassing Access Restrictions

### Objective:
Access a restricted website and retrieve the flag by spoofing an IP address in the request header.

### Instructions:

1. **Understand the Scenario:**
   - A website is inaccessible from outside a certain network, likely due to IP-based access control.

2. **Spoof IP Address:**
   - Use the `curl` command with the `X-Forwarded-For` header to spoof your IP address as if the request is coming from an allowed network.
   - Command: `curl -H "X-Forwarded-For: 127.0.0.1" https://403.mohammadlotfi.com/flag.txt`

3. **Retrieve the Flag:**
   - The correct use of the `curl` command with the spoofed IP should provide access to the restricted content, revealing the flag.

### Deliverable:
Provide a brief report that includes the command used, an explanation of the IP spoofing technique, and the flag retrieved.

## Custom Project 2: Cryptography and Penetration Testing Challenge

### Objective:
Intercept and decrypt secured data using a combination of cryptography and penetration testing skills.

### Part 1: Decrypting with RSA

1. **Analyze the Public Key:**
   - Understand that the provided public key is of the RSA type but has vulnerabilities due to the use of unsafe primes.

2. **Extract Prime Numbers:**
   - Use the provided `calcul_PQ.py` script or an equivalent method to calculate the prime factors (`p` and `q`) of the RSA modulus.

### Part 2: Word-list Utilization

1. **Understand the Clue:**
   - Recognize that the word-list provided as a hexadecimal string (`75706C6F6164732F323032332F3030302F666C61672E747874.txt`) points to a file path.

2. **Convert and Access the File:**
   - Convert the hexadecimal string to ASCII to reveal the file path.
   - Retrieve the file, which may require additional steps or tools based on the context provided.

### Part 3: Penetration Testing

1. **Perform Brute-Force Attack:**
   - With the `username` and `target` obtained from the decrypted data, use the `ftp_BruteForce.py` script or a similar method to brute-force the FTP server and gain access to `flag.txt`.

### Deliverable:
Submit a comprehensive report detailing each step of the process, including the decryption of the public key, the conversion of the word-list, the brute-force attack, and the final flag obtained.