import matplotlib.pyplot as plt

input_nums = [1,2,3,4,5]

cubes = [num**3 for num in input_nums]

plt.scatter(input_nums, cubes, c=cubes, cmap=plt.cm.Blues, \
				edgecolor='none',s=100)

plt.title("Numbers Cubed", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic Value", fontsize=14)

plt.show()

#input_nums = list(range(1,5001))

#cubes = [num**3 for num in input_nums]

#plt.scatter(input_nums, cubes, c=cubes, cmap=plt.cm.Blues, \
#				edgecolor='none', s=40)

#plt.title("Numbers Cubed", fontsize=24)
#plt.xlabel("Value", fontsize=14)
#plt.ylabel("Cubic Value", fontsize=14)

#plt.axis([0, 5100, 0, 1110000000])

#plt.show()
