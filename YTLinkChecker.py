### This script is intended for Content Creators to keep track of links in descriptions.
### Go to USAGE section at bottom for more information on usage.
### Be sure to install python libraries: 
### pip install scrapetube
### pip install BeautifulSoup

import scrapetube
import csv
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def load_whitelist(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        return set()

def extract_links(description, whitelist):
    url_pattern = re.compile(
        r'(https?:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?)',
        re.IGNORECASE,
    )
    links = set(url_pattern.findall(description))
    
    # Filter out links with domains in the whitelist
    filtered_links = []
    for link in links:
        parsed_url = urlparse(link)
        domain = parsed_url.netloc.lower()
        domain = domain.replace("www.", "")  # Normalize by removing 'www.'
        
        # Ensure only URLs not in whitelist are included
        if not any(domain == whitelisted or domain.endswith("." + whitelisted) for whitelisted in whitelist):
            filtered_links.append(link)
    
    return filtered_links


def scrape_youtube_description(video_url):
    try:
        # Send a GET request to the YouTube video page
        response = requests.get(video_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Use a regular expression to extract the description
        pattern = re.compile(r'"shortDescription":"(.*?)"')
        match = pattern.search(str(soup))

        if match:
            description = match.group(1).replace("\\n", "\n")
            return description
        else:
            return "Description not found."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def scrape_youtube_channel(channel, output_csv, whitelist_path):
    """Scrape video URLs and descriptions from a YouTube channel and extract links."""
    
    try:
        videos = scrapetube.get_channel(channel)
        if not videos:
            print(f"Error: No videos found for channel {channel}.")
            return
    except Exception as e:
        print(f"Error retrieving channel data: {e}")
        return
    
    whitelist = load_whitelist(whitelist_path)
    
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Video ID", "Video URL", "Video Title", "Extracted Hyperlink"])
        
        for video in videos:
            video_id = video["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video['videoId']}"
            title = video["title"]["runs"][0]["text"]
            description = scrape_youtube_description(video_url)
            links = extract_links(description, whitelist)
            
            # Write each unique link in a separate row
            if links:
                for link in links:
                    writer.writerow([video_id, video_url, title, link])
            else:
                writer.writerow([video_id, video_url, title, "No links found"])

# USAGE
### Set the channel variable to your Youtube Channel ID. Get this by going to studio.youtube.com/channel - the text that follows it ("ABCDakjhasdlfjkhaskjdhJJ39234Qb") is what you use.
### Set the name of the file you want for the output. 
### Specify a whitelist of domains that you want to filter out. For example, amzn.to will filter out affiliate links. Put domains you wish to filter out on a separate line.
### Run the script "python YTLinkChecker.py".
### Open up the CSV file to view links.


channel = "<<REPLACE WITH YOUR CHANNEL ID HERE AS NOTED ABOVE- MUST BE VALID OR YOU WILL GET AN ERROR>>"
output_csv = "youtube_videos.csv"
whitelist_path = "/Users/greg/src/YTLinkChecker/whitelist.txt"
scrape_youtube_channel(channel, output_csv, whitelist_path)
