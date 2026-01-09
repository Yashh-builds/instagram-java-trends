from apify_client import ApifyClient
import json

# Initialize client with API token
client = ApifyClient("your api_token")

# Actor input (NO UI interaction)
run_input = {
    "directUrls": [
        "https://www.instagram.com/explore/tags/javadeveloper/",
        "https://www.instagram.com/explore/tags/springboot/",
        "https://www.instagram.com/explore/tags/backenddeveloper/"
    ],
    "resultsType": "posts",
    "resultsLimit": 30
}

# Run actor via API
run = client.actor("apify/instagram-scraper").call(run_input=run_input)

# Fetch dataset items
items = client.dataset(run["defaultDatasetId"]).list_items().items

# Save raw data to JSON
with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=4)

print("Instagram data fetched using Python API and saved to dataset.json")
