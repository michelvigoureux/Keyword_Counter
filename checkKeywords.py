import requests
import re
import csv
from tqdm import tqdm

def check_word(word, url):
    response = requests.get(url)
    word_count = len(re.findall(word, response.text))
    return word_count

def main():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    csv_file = open('word_counts.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file, delimiter=',')

    keyword = input("Enter the keyword: ")

    # Creating a progress bar with the total number of URLs to process
    progress_bar = tqdm(total=len(urls))

    for url in urls:
        url = url.strip()
        word_count = check_word(keyword, url)
        csv_writer.writerow([url, keyword, word_count])
        # Updating the progress bar for each processed URL
        progress_bar.update(1)

    # Closing the progress bar
    progress_bar.close()

if __name__ == "__main__":
    main()