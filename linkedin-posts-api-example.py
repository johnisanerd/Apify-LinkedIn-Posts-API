"""
LinkedIn Posts API: A Quick Start Example
See more at: https://apify.com/johnvc/linkedin-posts-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/linkedin-posts-api/input-schema?fpr=9n7kx3

This script shows how to call the LinkedIn Posts API on Apify from Python and
read its structured JSON output. Give it a profile URL and it discovers that
person's recent posts, or pass specific post URLs to fetch directly. You get one
clean row per post (text, reactions, comments, shares, date, author, and more).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Kept small on purpose: one profile URL with maxPostsPerProfile set to 5, so
# your first run stays cheap (you pay per post returned). Raise maxPostsPerProfile,
# add a startDate/endDate window, add more profile URLs, or pass specific posts in
# postUrls to collect more.
run_input = {
    "profileUrls": ["https://www.linkedin.com/in/williamhgates"],
    "maxPostsPerProfile": 5,
    # "startDate": "2025-01-01",   # only posts on or after this date
    # "endDate": "2025-12-31",     # only posts on or before this date
    # "postUrls": ["https://www.linkedin.com/posts/..."],  # fetch specific posts
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/linkedin-posts-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} post(s).\n")

# Show a few key fields from each post.
for item in items:
    print(f"Author:   {item.get('authorName')}")
    print(f"Posted:   {item.get('datePosted')}")
    print(f"Likes:    {item.get('numLikes')}")
    print(f"Comments: {item.get('numComments')}")
    print(f"Shares:   {item.get('numShares')}")
    text = (item.get("text") or "").replace("\n", " ")
    print(f"Text:     {text[:120]}")
    print(f"URL:      {item.get('postUrl')}")
    print(f"Summary:  {item.get('summary')}")
    print("-" * 60)
