import matplotlib.pyplot as plt
size = 50
O_N_2 = [x**2 for x in range(size)]
O_N_3 = [x**3 for x in range(size)]
O_N_4 = [x**4 for x in range(size)]

plt.plot(O_N_2, label=r"O(N^2)")
plt.plot(O_N_3, label=r"O(N^3)")
plt.plot(O_N_4, label=r"O(N^4)")
plt.legend()
plt.ylabel("Steps Involved")
plt.xlabel("Size of Input to the Algorithm")
plt.grid()
plt.title("Big O Performance")
plt.show()