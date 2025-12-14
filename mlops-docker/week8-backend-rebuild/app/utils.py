import time

def timed_stub_response():
    start = time.perf_counter()

    #stub work
    time.sleep(0.01)
    text = "stub response"
    tokens = 0
    cost = 0.0

    latency_ms = int((time.perf_counter() -  start) * 1000)

    return text, tokens, cost, latency_ms