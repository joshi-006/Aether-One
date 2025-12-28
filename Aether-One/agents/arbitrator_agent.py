def arbitrate(conflict):
    if conflict:
        return "RECHECK"
    return "CONFIRMED"
