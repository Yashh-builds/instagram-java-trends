def analyze_trends(captions):
    keywords = [
        "spring boot", "microservices", "backend",
        "java jobs", "interview", "api"
    ]

    trends = {}

    for caption in captions:
        caption = caption.lower()
        for word in keywords:
            if word in caption:
                trends[word] = trends.get(word, 0) + 1

    return trends
