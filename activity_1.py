import psutil
import timeit
import os
import time


def cpu_benchmark():
    """Benchmark a CPU-bound task."""

    def cpu_intensive_task():
        [x ** 2 for x in range(1_000_000)]

    cpu_time = timeit.timeit(cpu_intensive_task, number=10)

    print(f"CPU benchmark: {cpu_time:.5f} seconds for 10 runs")

    return cpu_time


def memory_benchmark():
    """Measure memory usage before, during, and after allocation."""

    before = psutil.virtual_memory()

    print(f"Memory before: {before.percent:.2f}% "
          f"({before.used / (1024 ** 3):.2f} GB)")

    large_list = list(range(10_000_000))

    time.sleep(1)

    during = psutil.virtual_memory()

    print(f"Memory during: {during.percent:.2f}% "
          f"({during.used / (1024 ** 3):.2f} GB)")

    del large_list

    time.sleep(1)

    after = psutil.virtual_memory()

    print(f"Memory after: {after.percent:.2f}% "
          f"({after.used / (1024 ** 3):.2f} GB)")

    return before, during, after


def storage_benchmark(file_size_mb=100):
    """Benchmark 100 MB file write and read speeds."""

    file_name = "benchmark_test_file.bin"

    print("\nCreating 100 MB test file...")

    data = os.urandom(file_size_mb * 1024 * 1024)

    # WRITE TEST
    start = time.time()

    with open(file_name, "wb") as f:
        f.write(data)

    write_time = time.time() - start

    # READ TEST
    start = time.time()

    with open(file_name, "rb") as f:
        f.read()

    read_time = time.time() - start

    # Delete test file
    os.remove(file_name)

    write_speed = file_size_mb / write_time
    read_speed = file_size_mb / read_time

    print(f"Storage write speed: {write_speed:.2f} MB/s")
    print(f"Storage read speed: {read_speed:.2f} MB/s")

    return write_speed, read_speed


if __name__ == "__main__":

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 1.1")
    print("=" * 50)

    print("\n--- CPU BENCHMARK ---")
    cpu_benchmark()

    print("\n--- MEMORY BENCHMARK ---")
    memory_benchmark()

    print("\n--- STORAGE BENCHMARK ---")
    storage_benchmark()

    print("\nBenchmark complete!")