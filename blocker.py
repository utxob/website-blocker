import os
import platform

# Detect the OS
current_os = platform.system()

# Hosts file path for different OS
if current_os == "Windows":
    hosts_file = r'C:\\Windows\\System32\\drivers\\etc\\hosts'  # Windows path
else:
    hosts_file = '/etc/hosts'  # Linux/MacOS path

redirect_ip = '127.0.0.1'

# List to keep track of blocked websites
blocked_websites = []

# Function to read the hosts file and get blocked websites
def read_hosts():
    global blocked_websites
    blocked_websites = []
    
    with open(hosts_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if redirect_ip in line:
                domain = line.split()[1]
                blocked_websites.append(domain)

# Function to add a website to the block list
def add_website(domain):
    with open(hosts_file, 'a') as file:
        file.write(f'{redirect_ip} {domain}\n')
    print(f'{domain} has been added to the block list.')

# Function to delete a website from the block list
def delete_website(domain):
    with open(hosts_file, 'r') as file:
        lines = file.readlines()
    
    with open(hosts_file, 'w') as file:
        for line in lines:
            if domain not in line:
                file.write(line)
    
    print(f'{domain} has been removed from the block list.')

# Function to show all blocked websites
def show_blocked_websites():
    if len(blocked_websites) == 0:
        print("No websites are blocked.")
    else:
        print("Blocked websites:")
        for website in blocked_websites:
            print(f"- {website}")

# Main function to run the tool
def run_tool():
    while True:
        read_hosts()
        print("\n1. Add a website to block")
        print("2. Delete a website from block list")
        print("3. Show blocked websites")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            domain = input("Enter website domain to block (e.g. example.com): ")
            add_website(domain)
        elif choice == '2':
            domain = input("Enter website domain to unblock (e.g. example.com): ")
            delete_website(domain)
        elif choice == '3':
            show_blocked_websites()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the tool
if __name__ == '__main__':
    run_tool()

