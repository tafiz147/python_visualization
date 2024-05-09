import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares =[1,4,9,16,25]

plt.plot(input_values,squares,linewidth=5)

#set chart title and label axes
plt.title("Square Numbers",fontsize=14)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#set size of tick labels
plt.tick_params(axis='both',labelsize=10)
plt.show()