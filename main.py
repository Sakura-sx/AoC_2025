import importlib.util
import time
import pathlib

times = []

for i in range(1, 7+1):
    for j in range(1, 2+1):

        # Build filename like "1.py"
        path = pathlib.Path(f"{i}.py")

        # Load the module dynamically
        spec = importlib.util.spec_from_file_location(f"mod{i}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Get the function like solve1_1, solve2_1, …
        func_name = f"solve{i}_{j}"
        func = getattr(module, func_name)

        print(f"starting {func_name}")
        start = time.perf_counter_ns()
        func()
        end = time.perf_counter_ns()
        print(f"{func_name} took {(end - start) / 1e6}ms")
        times.append((func_name, f"{(end - start) / 1e6}ms"))

print(times)