import time

LOOPS=1_000_000_000

tests = {
        "monotonic": time.monotonic,
        "perf_counter": time.perf_counter
}

def duration(test):
    start = tests[test]()
    for _ in range(LOOPS):
            pass
    print(f"{test}: {tests[test]() - start}")

def changes(test):
    last = changes = 0
    for _ in range(LOOPS):
        current = tests[test]()
        if current != last:
            changes += 1
        last = current
    print(f"{test}: {changes}")

print("Duration:")
duration("monotonic")
duration("perf_counter")

print("Changes:")
changes("monotonic")
changes("perf_counter")

