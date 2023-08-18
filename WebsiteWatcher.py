import requests
import difflib
import os

def save_html(url, content):
    with open(f'{url.replace("/", "_")}.html', 'w') as html_file:
        html_file.write(content)

def main():
    websites = []

    # Read website URLs from the text file
    with open('websites.txt', 'r') as file:
        websites = file.read().splitlines()

    for url in websites:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text

            # Check if the old HTML exists
            html_file_path = f'{url.replace("/", "_")}.html'
            if os.path.exists(html_file_path):
                with open(html_file_path, 'r') as html_file:
                    old_content = html_file.read()

                if old_content != content:
                    print(f'Website {url} has changed!')

                    # Generate and display the diff using difflib
                    d = difflib.Differ()
                    diff = d.compare(old_content.splitlines(), content.splitlines())
                    print('\n'.join(diff))

                    # Save the updated HTML content
                    save_html(url, content)

            else:
                # Save the new HTML content
                save_html(url, content)

if __name__ == '__main__':
    main()
