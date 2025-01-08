"""
Description: This script collects commit data from all repositories in a parent directory, prints and saves it to a CSV file.
This script is intended to be run in the parent directory containing all cloned repositories.

Requirements:
Python 3.x
"""

import os
import csv
from datetime import datetime

# Define the parent directory containing all cloned repos
user_input = input("Enter the path to the parent directory containing all cloned repos: ")
parent_dir = "/" + user_input


# Gets the current working directory
dir = os.getcwd()
dirname = os.path.dirname(__file__)
parent_dir = dir + "//" +parent_dir

# Get list of all files in the parent directory
list_of_files = os.listdir(parent_dir)

# Output file to store all commit data. This will create a csv file in each repo directory.
# NOT THE INTENDED RESULT####################################
name_output_file = input("Enter the name of the csv output file (e.g., commit_logs): ")
output_file = f"{name_output_file}.csv"
output_file = os.path.join(parent_dir, output_file)

# Write header for the output CSV
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Repo Name", "Commit Hash", "Date", "Message"])


# Loop through each repository
for repo in list_of_files:
    repo_path = os.path.join(parent_dir, repo)
    # print("REPO PATH" + repo_path)
    if os.path.isdir(repo_path):
        os.chdir(repo_path)  # Change to repo directory
        # print(f"Processing {repo}...")
        # Get commit history
        stream = os.popen('git log --pretty=format:"%h,%ad,%s" --date=short')
        commits = stream.read().strip()
        print(f"*******Processing {repo}...*******")
        for commit in commits.split("\n"):
            hash_, date, message = commit.split(",", 2)

            # Print commit data
            print(f" - Date: {date} | Message: {message}")
            
            # Write to output file
            with open(output_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([repo, hash_, date, message])

print(f"Commit data collected and saved to {output_file}")
print(f"Commit data collected for all repositories")
