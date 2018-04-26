# Kenny McTigue, 18/04/2018
# Project 2018, Iris Dataset Analysis
# https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91




import numpy

data = numpy.genfromtxt("data/iris.csv", delimiter = ",") 


# Four variables, Petal length, Petal width, Sepal length and Sepal width
# To identify the data in each variable
petlen = data[:,0] # first column
petwid = data[:,1] # second column
seplen = data[:,2] # third column
sepwid = data[:,3] # fourth column

# To calculate the mean of each variable
meanpetlen = numpy.mean(data[:,0])
meanpetwid = numpy.mean(data[:,1])
meanseplen = numpy.mean(data[:,2])
meansepwid = numpy.mean(data[:,3])

# To identify the data of just the Setosa class of Iris
setpetlen = data[1:50,0]
setpetwid = data[1:50,1]
setseplen = data[1:50,2]
setsepwid = data[1:50,3]

# To calculate the mean of each variable for the Setosa class of Iris
setmeanpetlen = numpy.mean(data[1:50,0])
setmeanpetwid = numpy.mean(data[1:50,1])
setmeanseplen = numpy.mean(data[1:50,2])
setmeansepwid = numpy.mean(data[1:50,3])

# To identify the data of just the Versicolor class of Iris 
verpetlen = data[51:100,0]
verpetwid = data[51:100,1]
verseplen = data[51:100,2]
versepwid = data[51:100,3]

# To calculate the mean of each variable for the Versicolor class of Iris
vermeanpetlen = numpy.mean(data[51:100,0])
vermeanpetwid = numpy.mean(data[51:100,1])
vermeanseplen = numpy.mean(data[51:100,2])
vermeansepwid = numpy.mean(data[51:100,3])

# To identify the data of just the Virginica class of Iris
virpetlen = data[101:150,0]
virpetwid = data[101:150,0]
virseplen = data[101:150,2]
virsepwid = data[101:150,3]

# To calculate the mean of each variable for the virginica class of Iris
virmeanpetlen = numpy.mean(data[101:150,0])
virmeanpetwid = numpy.mean(data[101:150,1])
virmeanseplen = numpy.mean(data[101:150,2])
virmeansepwid = numpy.mean(data[101:150,3])


