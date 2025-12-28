def entity_filter(event):
    required = ["location", "timestamp"]
    return all(k in event for k in required)
