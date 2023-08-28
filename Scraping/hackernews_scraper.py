import pprint

import requests
from bs4 import BeautifulSoup

# Function to scrape a single page and return links and subtexts
def scrape_single_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # Collect links
    links = soup.select(".titleline > a")
    # Collect subtexts (including vote information)
    subtexts = soup.select(".subtext")

    return links, subtexts

# Function to scrape multiple pages and collect links and subtexts
def scrape_multiple_pages(base_url, num_of_pages):
    collected_links = []
    collected_subtexts = []

    # get the url to scrape from
    for i in range(1, num_of_pages + 1):
        url = base_url if i == 1 else f"{base_url}?p={i}"

        links, subtexts = scrape_single_page(url)
        collected_links.append(links)
        collected_subtexts.append(subtexts)

    return collected_links, collected_subtexts

# Function to get articles with votes greater than or equal to a given threshold
def get_articles(num_of_pages, min_vote_point):
    base_url = "https://news.ycombinator.com/"
    collected_links, collected_subtexts = scrape_multiple_pages(base_url, num_of_pages)

    articles = []

    # loop through links
    for page_id in range(len(collected_links)):

        links = collected_links[page_id]
        subtexts = collected_subtexts[page_id]

        for idx in range(len(links)):

            # return the HTML element in a list
            # [< span class ="score" id="score_37279109" > 653 points < /span >]
            vote = subtexts[idx].select(".score")

            # if article has associated vote
            # extract vote points
            if len(vote) != 0:

                vote_point = int(vote[0].getText().split()[0])
                # if article vote is >= min_vote_point
                # add the article
                if vote_point >= min_vote_point:
                    title = links[idx].getText()
                    link = links[idx].get("href", None)
                    articles.append({"title": title, "link": link, "vote": vote_point,"page":page_id+1})

    # Sort articles by vote points in descending order
    articles.sort(key=lambda x: x['vote'], reverse=True)

    return articles


# Entry point of the program
if __name__ == "__main__":
    num_of_pages = int(input("Enter the number of pages to scrape from ""https://news.ycombinator.com/"":" ))
    min_vote_point = int(input("Enter the minimum vote points required (exclusive): "))

    print("---Fetching Articles---")
    result = get_articles(num_of_pages, min_vote_point)

    pprint.pprint(result)