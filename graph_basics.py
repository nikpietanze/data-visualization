from matplotlib import pyplot as plt

plt.plot([1,2,3], [1,4,9])
plt.plot([1,2,3], [10,20,30])
plt.legend(['Data Set 1', 'Data Set 2'])
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.title('this is the title')

#* Show the graph
# plt.show()

#* Save the graph
plt.savefig('exported_img')