from myplot import MyPlot
import sys

data = [[1,2,3,4,5],[6,7,8,9,10]]
print(data)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

#type_of_graph = int(input("What is the type of graph you want. \n Press 1 for histogram \n Press 2 for bar chart \n Press 3 for scatter plot. \n Press 4 for line plot \n Press 5 for histogram\n Press 6 for pie chart"))
#{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}

type_of_graph = int(sys.argv[1])
myplt = MyPlot(type_of_graph, str(sys.argv[2]), data)
myplt.plot_graph()
#fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#axs[0, 0].hist(data[0])
#axs[1, 0].scatter(data[0], data[1])
#axs[0, 1].plot(data[0], data[1])
#axs[1, 1].hist2d(data[0], data[1])
