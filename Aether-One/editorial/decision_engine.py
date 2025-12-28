def editorial_decision(status):
    if status == "GREEN":
        return "PUBLISH"
    elif status == "YELLOW":
        return "PUBLISH WITH DISCLAIMER"
    else:
        return "HOLD & ESCALATE"
