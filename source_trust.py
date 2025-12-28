source_weight = {}

def update_trust(source, reliable=True, lr=0.1):
    w = source_weight.get(source, 0.5)

    if reliable:
        w += lr * (1 - w)
    else:
        w -= lr * w

    source_weight[source] = max(0, min(1, w))
