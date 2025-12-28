def verify_cross_modal(video, sensor):
    if "smoke" in video["objects"] and sensor["value"] > 100:
        return True
    return False
