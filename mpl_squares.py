import matplotlib.pyplot as plt
plt.style.available


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.syyle.use('seaborn')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth= 3)

# set chart title and label axes.
ax.set_title("squares number ", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("square of value", fontsize = 14)


# set size of tick labels 
ax.tick_params(axis='both', labelsize = 14)

plt.show()
