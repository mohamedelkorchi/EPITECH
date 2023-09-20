# TASK 2
# Display the points (0; 12), (1; 32), (2; 42) and (3; 52) in a chart similar to this one:

from matplotlib import pyplot as plt

plt.grid(True)

# plt.plot(0,12, "or")
# plt.plot(1,32, marker="o", color="red")
# plt.plot(2,42, marker="o", color="red")
# plt.plot(3,52, marker="o", color="red")

plt.plot([0,1,2,3], [12,32,42,52],"or")   # raccourci
plt.show()
