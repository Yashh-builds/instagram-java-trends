import json
from scraper import fetch_posts
from analyzer import analyze_trends

captions = fetch_posts()
trends = analyze_trends(captions)

with open("java_trends.json", "w") as file:
    json.dump(trends, file, indent=4)

print("Java Developer Instagram trends saved successfully!")

print("\nTrending Java Topics:")
for k, v in trends.items():
    print(f"{k} → {v}")
