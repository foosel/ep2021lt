---
title: time.monotonic vs time.perf_counter
description: A look at the difference between time.monotonic and time.perf_counter across platforms
marp: true
---

<!-- class: invert -->

# time.monotonic vs time.perf_counter: What's the difference?

Gina Häußge // @foosel

EuroPython 2021

---

# What does `time.get_clock_info` say?

|                  | Windows | WSL2 | Linux |
| ---------------- | -------- | ---- | ----- |
| `time.monotonic`    | 64 Hz 👀 | 1,000,000,000 Hz | 1,000,000,000 Hz |
| `time.perf_counter` | 10,000,000 Hz | 1,000,000,000 Hz | 1,000,000,000 Hz |

Implementation: `GetTickCount64`/`QueryPerformanceCounter` (Windows) vs `get_clock("CLOCK_MONOTONIC")` (Linux)

---

# Let's have a closer look at the resolution

Test: Loop with 1,000,000,000 cycles, number of changes of returned value.

|                     | Windows       | WSL2          | Linux         |
| ------------------- | ------------- | ------------- | ------------- |
| `time.monotonic`    | 6811 👀         | 1,000,000,000 | 1,000,000,000 |
| `time.perf_counter` | 1,000,000,000 | 1,000,000,000 | 1,000,000,000 |

---

# And what about performance?

`timeit`, 5,000,000 loops, best of 5.

|                     | Windows   | WSL2      | Linux     |
| ------------------- | --------- | ----------| --------- |
| `time.monotonic`    | 54.2 nsec 👀 | 87.2 nsec | 74 nsec   |
| `time.perf_counter` | 84.1 nsec | 90.3 nsec | 73.3 nsec |

---

# Summary

`time.monotonic` and `time.perf_counter` only differ under Windows, in resolution and performance.

# Links

  - Repo: [github.com/foosel/ep2021lt](https://github.com/foosel/ep2021lt)
  - Further reading: [https://www.webucator.com/article/python-clocks-explained/](https://www.webucator.com/article/python-clocks-explained/)
