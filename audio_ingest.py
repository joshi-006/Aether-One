def ingest_audio(text):
    return {
        "type": "audio",
        "text": text,
        "timestamp": time.time()
    }
