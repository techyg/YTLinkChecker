# YTLinkChecker
This is a simple Python script that allows you to check links on any given Youtube channel. It will iterate through all the videos for the specified channel and parse the description for any and all hyperlinks / url's. 

# Why did I create this?
Links get out of date, especially for older videos. A few reasons to check:

1. It's just good hygiene. Old broken links suck, and your viewers might even give you a thumbs down. Boo!
2. Affiliate links, or links to url's sometimes change or expire. Also a bummer- you lose out on revenue, and the viewer gets annoyed. 
3. And worst of all.. (this has happened to me!) You may have an older video that goes to a domain and the original owener lets the domain lapse. Someone else purchases the domain and turns it into a spam or generally unsavory site. Youtube can issue a warning, or even strike your channel for violating community guidelines. Too many of those, and your channel can be turned off! Yikes. It literally pays to keep your links updated!

So, hopefully I've convinced you of the importance of checking your links. This utility is free and easy to use. It's generally just a starting point, as it doesn't currently do much beyond pull a list of links down. However, that's still better than navigating to each Youtube video manually, checking descriptions, and clicking links. Ain't nobody got time for that! 

I do plan on adding some more capability, like just checking to see if there is a 404 (not found), 503, etc. or other response. I'm not going to get too sophisticated. But feel free to take what I've built and extend it! That would be awesome. 


# Technical information

It uses the "scrapetube" python library to do so, and also BeautifulSoup.

Be sure to install the latest libraries before running:

pip install scrapetube

pip install BeautifulSoup


# USAGE
At the bottom of the script, you will find a few variables you will need to set to successfully run the script.


# IMPORTANT - CHANNEL VARIABLE MUST BE SET. 
1. Set the channel variable to your Youtube Channel ID. Get this by going to studio.youtube.com/channel - the text that follows it ("UC6askdjfbadbnasdfkj") is what you use. Or, you can find this by going to the "About" and clicking "Share Channel" and then "Copy Channel ID". 
2. Set the name of the file you want for the output. 
3. Specify a whitelist of domains that you want to filter out. For example, amzn.to will filter out affiliate links. Put domains you wish to filter out on a separate line.
4. Run the script "python YTLinkChecker.py".
5. Open up the CSV file to view links.

# Config/variables you need to set- found at bottom of script:

channel = "UC6askdjfbadbnasdfkj"

output_csv = "youtube_videos.csv"

whitelist_path = "/Users/greg/src/YTLinkChecker/whitelist.txt"

# Things to know

I've tested this with my channel, which has about 150 videos. It takes about a minute or two to run. The more videos and links you have, the longer it will take. It will print status information while running. 
