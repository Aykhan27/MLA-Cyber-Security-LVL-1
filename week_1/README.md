# Welcome to the Assignment Guide

## Overview

This guide outlines the tasks and challenges for the first week. Your assignments are divided into categories based on difficulty and skill set required. Please follow the instructions carefully and submit your solutions as per the guidelines provided.

## Assignments

### 1. Forensics Challenge: "Enhance!"

#### Objective:

Analyze the provided image file to uncover the hidden flag.

#### Instructions:

- Download the image file from the provided link.
- Utilize forensic analysis tools and techniques to extract the flag hidden within the image.

#### File Details:

- **Category:** Forensics
- **File Format:** SVG

#### Solution Approach:

- Examine the SVG file's contents, focusing on elements that may contain encoded or hidden data.
- Utilize text extraction and manipulation commands (`grep`, `cut`, `tr`) to isolate and reveal the flag.

### 2. Forensics Challenge: "File Types"

#### Objective:

Determine the correct file type and extract the flag from the mislabeled file.

#### Instructions:

- Analyze the provided file, which is incorrectly marked as a PDF.
- Identify the correct file format and use appropriate methods to extract its contents.

#### File Details:

- **Category:** Forensics
- **Incorrect Label:** PDF

#### Solution Approach:

- Use the `file` command to identify the true nature of the file.
- Apply file-specific extraction commands (`chmod`, `ar xv`) to access the contents and uncover the flag.

### 3. Custom Challenge: Hidden Web Form

#### Objective:

Locate and submit your name in the hidden form on the specified website.

#### Instructions:

- Visit the provided website link.
- Utilize directory and file enumeration tools (e.g., `gobuster`) to discover hidden paths.

```bash
    gobuster dir -u rs11.mohammadlotfi.com -w /usr/share/wordlists/rockyou.txt -x php,js,html,css,txt -o output
```
- Find the hidden form and submit your name as instructed.

#### Website Details:

- **URL:** [https://rs11.mohammadlotfi.com/](#)

#### Solution Approach:

- Conduct a thorough enumeration of the website's directories and files.
- Identify the path containing the hidden form and complete the submission process.