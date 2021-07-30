import time

for x in ("monotonic", "perf_counter"):
    info = time.get_clock_info(x)
    print(x)
    print(f"\tmonotonic:      {info.monotonic}")
    print(f"\timplementation: {info.implementation}")
    print(f"\tresolution:     {info.resolution}")
    print(f"\tticks:          {1 / info.resolution}")

