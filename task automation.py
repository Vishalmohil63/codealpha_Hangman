# Task 3 - Task Automation with Python Scripts (CodeAlpha Internship)
# This program has 3 small automation examples:
# 1. Move JPG files
# 2. Extract emails from text
# 3. Scrape webpage title

import os
import shutil
import re
import requests

# 1. Move all JPG files from one folder to another
def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files_moved = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            files_moved += 1

    print(f"{files_moved} JPG files moved successfully.")


# 2. Extract emails from a text file
def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print("Input file not found.")
        return

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Extracted {len(emails)} emails. Saved to {output_file}.")


# 3. Scrape the title of a webpage
def scrape_title(url, output_file):
    try:
        response = requests.get(url)
        html = response.text
    except Exception as e:
        print("Error while fetching webpage:", e)
        return

    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    if match:
        title = match.group(1)
        with open(output_file, "w") as f:
            f.write(title)
        print(f"Page title saved in {output_file}: {title}")
    else:
        print("No title found.")


# Main menu
def main():
    while True:
        print("\n--- Task 3 Automation Menu ---")
        print("1. Move JPG files")
        print("2. Extract emails from text")
        print("3. Scrape webpage title")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            src = input("Enter source folder path: ")
            dest = input("Enter destination folder path: ")
            move_jpg_files(src, dest)

        elif choice == "2":
            infile = input("Enter input text file path: ")
            outfile = input("Enter output file path: ")
            extract_emails(infile, outfile)

        elif choice == "3":
            url = input("Enter webpage URL: ")
            outfile = input("Enter output file path: ")
            scrape_title(url, outfile)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
