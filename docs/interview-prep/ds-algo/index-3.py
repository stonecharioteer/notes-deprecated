import matplotlib.pyplot as plt
size = 100
O_1 = [1 for _ in range(size)]
O_N = list(range(size))
O_N_2 = [x**2 for x in range(size)]
O_N_3 = [x**3 for x in range(size)]
O_N_4 = [x**4 for x in range(size)]

plt.plot(O_1, label=r"O(1)")
plt.plot(O_N, label=r"O(N)")
plt.plot(O_N_2, label=r"O(N^2)")
plt.plot(O_N_3, label=r"O(N^3)")
plt.plot(O_N_4, label=r"O(N^4)")
plt.legend()
plt.ylabel("Steps Involved")
plt.xlabel("Size of Input to the Algorithm")
plt.grid()
plt.yscale("log")
plt.title("Big O Performance")
plt.show()