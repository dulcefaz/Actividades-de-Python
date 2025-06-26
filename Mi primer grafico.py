import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x, y ,color='blue',linestyle='-', marker='x')
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.grid(True)
plt.show()