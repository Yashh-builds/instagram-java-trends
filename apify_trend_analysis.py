import json

with open("dataset.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

keywords = [
    "spring boot",
    "spring",
    "microservices",
    "backend",
    "java jobs",
    "javadeveloper",
    "interview",
    "api"
]

trends = {}

for post in posts:
    caption = (post.get("caption") or "").lower()
    for key in keywords:
        if key in caption:
            trends[key] = trends.get(key, 0) + 1

print("\nJava Developer Trends:")
for k, v in trends.items():
    print(f"{k} → {v}")
