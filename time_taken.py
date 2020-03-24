from time import perf_counter
print("Enter your name: ", end="")
start_time = perf_counter()
name = input()
elapsed = perf_counter() - start_time
print(name, "it took you", elapsed, "seconds to respond")