def intent_filter(event):
    critical_words = ["fire", "explosion", "accident"]
    text = str(event).lower()
    return any(word in text for word in critical_words)
