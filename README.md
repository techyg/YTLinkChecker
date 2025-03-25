# YTLinkChecker
This is a simple Python script that allows you to check links on any given Youtube channel. It uses the "scrapetube" python library to do so, and also BeautifulSoup.

Be sure to install the latest libraries before running:

pip install scrapetube
pip install BeautifulSoup


# USAGE
At the bottom of the script, you will find a few variables you will need to set to successfully run the script.


# IMPORTANT - CHANNEL VARIABLE MUST BE SET. 
1. Set the channel variable to your Youtube Channel ID. Get this by going to studio.youtube.com/channel - the text that follows it ("ABCDakjhasdlfjkhaskjdhJJ39234Qb") is what you use. Or, you can find this by going to the "About" and clicking "Share Channel" and then "Copy Channel ID". 
2. Set the name of the file you want for the output. 
3. Specify a whitelist of domains that you want to filter out. For example, amzn.to will filter out affiliate links. Put domains you wish to filter out on a separate line.
4. Run the script "python YTLinkChecker.py".
5. Open up the CSV file to view links.

# Config/variables you need to set- found at bottom of script:

channel = "UC6askdjfbadbnasdfkj" (this is fake- replace with a valid channel ID)
output_csv = "youtube_videos.csv"
whitelist_path = "/Users/greg/src/YTLinkChecker/whitelist.txt"
scrape_youtube_channel(channel, output_csv, whitelist_path)
