# Results

## `time.get_clock_info`

### CPython 3.9.1, Windows 10 64bit

```
$ python src/clockprops.py
monotonic
        monotonic:      True
        implementation: GetTickCount64()
        resolution:     0.015625
        ticks:          64.0
perf_counter
        monotonic:      True
        implementation: QueryPerformanceCounter()
        resolution:     1e-07
        ticks:          10000000.0
```

### CPython 3.8.2, Ubuntu 20.04

```
$ python src/clockprops.py
monotonic
        monotonic:      True
        implementation: clock_gettime(CLOCK_MONOTONIC)
        resolution:     1e-09
        ticks:          999999999.9999999
perf_counter
        monotonic:      True
        implementation: clock_gettime(CLOCK_MONOTONIC)
        resolution:     1e-09
        ticks:          999999999.9999999
```

### MacOS (kindly provided by Mike)

```
$ python src/clockprops.py
monotonic
        monotonic:      True
        implementation: mach_absolute_time()
        resolution:     1e-09
        ticks:          999999999.9999999
perf_counter
        monotonic:      True
        implementation: mach_absolute_time()
        resolution:     1e-09
        ticks:          999999999.9999999
```

## Resolution

Loop with 1,000,000,000 cycles, number of changes of returned value.

### CPython 3.9.1, Windows 10 64bit

```
$ python src/timetest.py
[...]
Changes:
monotonic: 6811
perf_counter: 1000000000
```

### CPython 3.8.2, Ubuntu 20.04

```
$ python src/timetest.py
[...]
Changes:
monotonic: 1000000000
perf_counter: 1000000000
```

### MacOS (kindly provided by Mike)

```
$ python src/timetest.py
[...]
Changes:
monotonic: 1000000000
perf_counter: 1000000000
```

## Execution speed

### CPython 3.9.1, Windows 10 64bit

```
$ python -m timeit -s "import time" "time.monotonic()"
5000000 loops, best of 5: 54.2 nsec per loop
$ python -m timeit -s "import time" "time.perf_counter()"
5000000 loops, best of 5: 84.1 nsec per loop
```

### CPython 3.8.2, Ubuntu 20.04

```
$ python -m timeit -s "import time" "time.monotonic()"
5000000 loops, best of 5: 74 nsec per loop
$ python -m timeit -s "import time" "time.perf_counter()"
5000000 loops, best of 5: 73.3 nsec per loop
```

## Further reading

  * [https://www.webucator.com/article/python-clocks-explained/](https://www.webucator.com/article/python-clocks-explained/)