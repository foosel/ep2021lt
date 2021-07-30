---
title: "time.monotonic vs time.perf_counter: What's the difference?"
description: A look at the difference between time.monotonic and time.perf_counter across platforms
marp: true
---

<!-- class: invert -->

# `time.monotonic` vs `time.perf_counter`: What's the difference?

Gina Häußge // @foosel

EuroPython 2021

---

# What do the docs say?

> `time.monotonic()` → float
> Return the value (in fractional seconds) of a **monotonic clock**, i.e. a clock that cannot go backwards. The clock is **not affected by system clock updates**. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.

> `time.perf_counter()` → float
> Return the value (in fractional seconds) of a **performance counter**, i.e. a clock with the **highest available resolution** to measure a short duration. It does **include time elapsed during sleep** and is system-wide. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.

https://docs.python.org/3/library/time.html

---

# What does `time.get_clock_info` say?

|                  | Windows | Linux |
| ---------------- | -------- | ----- |
| `time.monotonic`    | 64 Hz 👀 | 1,000,000,000 Hz |
| `time.perf_counter` | 10,000,000 Hz| 1,000,000,000 Hz |

Implementation: `GetTickCount64`/`QueryPerformanceCounter` (Windows) vs `clock_gettime(CLOCK_MONOTONIC)` (Linux)

Monotonic: `true`

---

# Let's have a closer look at the resolution

Test: Loop with 1,000,000,000 cycles, number of changes of returned value.

|                     | Windows       | Linux         |
| ------------------- | ------------- | ------------- |
| `time.monotonic`    | 6811 👀       | 1,000,000,000 |
| `time.perf_counter` | 1,000,000,000 | 1,000,000,000 |

---

# And what about performance?

`timeit`, 5,000,000 loops, best of 5.

|                     | Windows   | Linux     |
| ------------------- | --------- | --------- |
| `time.monotonic`    | 54.2 nsec 👀 | 74 nsec   |
| `time.perf_counter` | 84.1 nsec | 73.3 nsec |

---

# Summary

  1. `time.monotonic` and `time.perf_counter` are both monotonic.
  2. Under Windows, `time.monotonic` has lower resolution and higher performance than `time.perf_counter`. Under Linux they are identical.

# Links

  - Repo: [github.com/foosel/ep2021lt](https://github.com/foosel/ep2021lt)
  - Further reading: [https://www.webucator.com/article/python-clocks-explained/](https://www.webucator.com/article/python-clocks-explained/)
