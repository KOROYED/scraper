import httpx
from selectolax.parser import HTMLParser
import schedule
import time
import datetime
from collections import defaultdict
import os


url = "https://quotes.toscrape.com"
selected_popularity_tag = 1
folder_path = "./scrapes/"
execute_time = "00:00"


def scraper(url=url):
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0"}
    html_response = httpx.get(url) #, headers=headers)
    return HTMLParser(html_response.text)

def parser(parsed_html):
    tags = parsed_html.css("span.tag-item")
    selected_tag = tags[selected_popularity_tag].css_first("a.tag").text()              

    quotes = parsed_html.css("div.quote")
    
    return (selected_tag, quotes)

def processer(quotes):
    author_quote_count = defaultdict(int)                                       
    author_tags = defaultdict(list)                                             
    author_sum_of_symbols = defaultdict(int)                                    

    for quote in quotes:
        author = quote.css_first("small.author").text()
        post = quote.css_first("span.text").text()
        author_quote_count[author] += 1
        author_sum_of_symbols[author] += len(post)
        for tag in quote.css("a.tag"):
            if tag.text() in author_tags[author]:
                continue
            author_tags[author].append(tag.text())

    return (author_quote_count, author_tags, author_sum_of_symbols)

def formater(processed_params, selected_tag):
    data = []
    author_quote_count, author_tags, author_sum_of_symbols = processed_params
    for author, tags in author_tags.items():
        if selected_tag in tags:
            string_to_write = (f"Author: {author}\n"
                            f"Tags: {', '.join(tags)}\n"
                            f"Post Count: {author_quote_count[author]}\n"
                            f"Character Count: {author_sum_of_symbols[author]}\n")
            
            data.append(string_to_write)

    return data

def stats_writer(data):
    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as error:
        print(f"Error creating folder {folder_path}: {error}")

    filepath = folder_path + datetime.datetime.now().strftime("%d-%m-%Y") + ".txt"

    try:
        with open(filepath, "w") as file:
            for info in data:
                file.write(info + "\n")
            print("Data written")
    except FileExistsError:
        print("That file already exists!")

def main():
    parsed_html = scraper()

    selected_tag, quotes = parser(parsed_html)

    processed_params = processer(quotes)

    formated_data = formater(processed_params, selected_tag)

    stats_writer(formated_data)

if __name__ == "__main__":
    schedule.every().day.at(execute_time).do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)

