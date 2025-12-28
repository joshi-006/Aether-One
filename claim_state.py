class ClaimState:
    def __init__(self):
        self.status = "UNKNOWN"
        self.evidence = []

    def verify(self, event):
        self.evidence.append(event)

        if len(self.evidence) >= 2:
            self.status = "GREEN"
        else:
            self.status = "YELLOW"

    def rollback(self):
        self.status = "RED"
