# Kenny McTigue, 18/04/2018
# Project 2018, Iris Dataset Analysis
# https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.amin.html
# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.amax.html




import numpy

data = numpy.genfromtxt("data/iris.csv", delimiter = ",") 


# Four variables, Petal length, Petal width, Sepal length and Sepal width
# To identify the data in each variable
petlen = data[:,0] # first column
petwid = data[:,1] # second column
seplen = data[:,2] # third column
sepwid = data[:,3] # fourth column

# to calculate the maximum of each variable
petlenmax = numpy.amax(data[:,0])
petwidmax = numpy.amax(data[:,1])
seplenmax = numpy.amax(data[:,2])
sepwidmax = numpy.amax(data[:,3])

# to calculate the minimum of each variable
petlenmin = numpy.amin(data[:,0])
petwidmin = numpy.amin(data[:,1])
seplenmin = numpy.amin(data[:,2])
sepwidmin = numpy.amin(data[:,3])

# To calculate the mean of each variable
petlenmean = numpy.mean(data[:,0])
petwidmean = numpy.mean(data[:,1])
seplenmean = numpy.mean(data[:,2])
sepwidmean = numpy.mean(data[:,3])

# To identify the data of just the Setosa class of Iris
setpetlen = data[1:50,0]
setpetwid = data[1:50,1]
setseplen = data[1:50,2]
setsepwid = data[1:50,3] 

# To calculate the maximum of each variable in the Setosa class of Iris
setpetlenmax = numpy.amax(data[1:50,0])
setpetwidmax = numpy.amax(data[1:50,1])
setseplenmax = numpy.amax(data[1:50,2])
setsepwidmax = numpy.amax(data[1:50,3])

# To calculate the minimum of each variable in the Setosa class of Iris
setpetlenmin = numpy.amin(data[1:50,0])
setpetwidmin = numpy.amin(data[1:50,1])
setseplenmin = numpy.amin(data[1:50,2])
setsepwidmin = numpy.amin(data[1:50,3])

# To calculate the mean of each variable for the Setosa class of Iris
setpetlenmean = numpy.mean(data[1:50,0])
setpetwidmean = numpy.mean(data[1:50,1])
setseplenmean = numpy.mean(data[1:50,2])
setsepwidmean = numpy.mean(data[1:50,3])

# To identify the data of just the Versicolor class of Iris 
verpetlen = data[51:100,0]
verpetwid = data[51:100,1]
verseplen = data[51:100,2]
versepwid = data[51:100,3]

# To calculate the maximum of each variable in the Versicolor class of Iris
verpetlenmax = numpy.amax(data[51:100,0])
verpetwidmax = numpy.amax(data[51:100,1])
verseplenmax = numpy.amax(data[51:100,2])
versepwidmax = numpy.amax(data[51:100,3])

# To calculate the minimum of each variable in the Versicolor class of Iris
verpetlenmin = numpy.amin(data[51:100,0])
verpetwidmin = numpy.amin(data[51:100,1])
verseplenmin = numpy.amin(data[51:100,2])
versepwidmin = numpy.amin(data[51:100,3])

# To calculate the mean of each variable for the Versicolor class of Iris
verpetlenmean = numpy.mean(data[51:100,0])
verpetwidmean = numpy.mean(data[51:100,1])
verseplenmean = numpy.mean(data[51:100,2])
versepwidmean = numpy.mean(data[51:100,3])

# To identify the data of just the Virginica class of Iris
virpetlen = data[101:150,0]
virpetwid = data[101:150,0]
virseplen = data[101:150,2]
virsepwid = data[101:150,3]

# To calculate the maximum of each variable in the Virginica class of Iris
virpetlenmax = numpy.amax(data[101:150,0])
virpetwidmax = numpy.amax(data[101:150,1])
virseplenmax = numpy.amax(data[101:150,2])
virsepwidmax = numpy.amax(data[101:150,3])

# To calculate the minimum of each variable in the Virginica class of Iris
virpetlenmin = numpy.amin(data[101:150,0])
virpetwidmin = numpy.amin(data[101:150,1])
virseplenmin = numpy.amin(data[101:150,2])
virsepwidmin = numpy.amin(data[101:150,3])

# To calculate the mean of each variable for the Virginica class of Iris
virpetlenmean = numpy.mean(data[101:150,0])
virpetwidmean = numpy.mean(data[101:150,1])
virseplenmean = numpy.mean(data[101:150,2])
virsepwidmean = numpy.mean(data[101:150,3])



virpetlenstd =numpy.std(data[101:150,0])

print (virpetlenstd)# Kenny McTigue, 18/04/2018
