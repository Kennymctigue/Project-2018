# Kenny McTigue, 18/04/2018
# Project 2018, Iris Dataset Analysis
# https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.amin.html
# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.amax.html
# https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
# https://matplotlib.org/
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

import numpy # http://www.numpy.org/



data = numpy.genfromtxt("data/iris.csv", delimiter = ",") 

import matplotlib.pyplot as pl # https://matplotlib.org/


# Four variables, Petal length, Petal width, Sepal length and Sepal width
# To identify the data in each variable

set = "Setosa"
ver = "Versicolor"
vir = "Virginica"

petlen = data[:,2] # first column petal length
petwid = data[:,3] # second column petal width
seplen = data[:,0] # third column sepal length
sepwid = data[:,1] # fourth Column sepal width


# to calculate the maximum of each variable
petlenmax = numpy.amax(data[:,2])
petwidmax = numpy.amax(data[:,3])
seplenmax = numpy.amax(data[:,0])
sepwidmax = numpy.amax(data[:,1])

# to calculate the minimum of each variable
petlenmin = numpy.amin(data[:,2])
petwidmin = numpy.amin(data[:,3])
seplenmin = numpy.amin(data[:,0])
sepwidmin = numpy.amin(data[:,1])

# To calculate the mean of each variable
petlenmean = round(numpy.mean(data[:,2]),2)
petwidmean = round(numpy.mean(data[:,3]),2)
seplenmean = round(numpy.mean(data[:,0]),2)
sepwidmean = round(numpy.mean(data[:,1]),2)

# To calculate the standard deviation from the mean of each variable
petlenstd = round(numpy.std(data[:,2]),3)
petwidstd = round(numpy.std(data[:,3]),3)
seplenstd = round(numpy.std(data[:,0]),3)
sepwidstd = round(numpy.std(data[:,1]),3)

# To identify the data of just the Setosa class of Iris
setpetlen = data[1:50,2]
setpetwid = data[1:50,3]
setseplen = data[1:50,0]
setsepwid = data[1:50,1] 

# To calculate the maximum of each variable in the Setosa class of Iris
setpetlenmax = numpy.amax(data[1:50,2])
setpetwidmax = numpy.amax(data[1:50,3])
setseplenmax = numpy.amax(data[1:50,0])
setsepwidmax = numpy.amax(data[1:50,1])

# To calculate the minimum of each variable in the Setosa class of Iris
setpetlenmin = numpy.amin(data[1:50,2])
setpetwidmin = numpy.amin(data[1:50,3])
setseplenmin = numpy.amin(data[1:50,0])
setsepwidmin = numpy.amin(data[1:50,1])

# To calculate the mean of each variable for the Setosa class of Iris
setpetlenmean = numpy.mean(data[1:50,2])
setpetwidmean = numpy.mean(data[1:50,3])
setseplenmean = numpy.mean(data[1:50,0])
setsepwidmean = numpy.mean(data[1:50,1])

# To identify the data of just the Versicolor class of Iris 
verpetlen = data[51:100,2]
verpetwid = data[51:100,3]
verseplen = data[51:100,0]
versepwid = data[51:100,1]

# To calculate the maximum of each variable in the Versicolor class of Iris
verpetlenmax = numpy.amax(data[51:100,2])
verpetwidmax = numpy.amax(data[51:100,3])
verseplenmax = numpy.amax(data[51:100,0])
versepwidmax = numpy.amax(data[51:100,1])

# To calculate the minimum of each variable in the Versicolor class of Iris
verpetlenmin = numpy.amin(data[51:100,2])
verpetwidmin = numpy.amin(data[51:100,3])
verseplenmin = numpy.amin(data[51:100,0])
versepwidmin = numpy.amin(data[51:100,1])

# To calculate the mean of each variable for the Versicolor class of Iris
verpetlenmean = numpy.mean(data[51:100,2])
verpetwidmean = numpy.mean(data[51:100,3])
verseplenmean = numpy.mean(data[51:100,0])
versepwidmean = numpy.mean(data[51:100,1])

# To identify the data of just the Virginica class of Iris
virpetlen = data[101:150,2]
virpetwid = data[101:150,3]
virseplen = data[101:150,0]
virsepwid = data[101:150,1]

# To calculate the maximum of each variable in the Virginica class of Iris
virpetlenmax = numpy.amax(data[101:150,2])
virpetwidmax = numpy.amax(data[101:150,3])
virseplenmax = numpy.amax(data[101:150,0])
virsepwidmax = numpy.amax(data[101:150,1])

# To calculate the minimum of each variable in the Virginica class of Iris
virpetlenmin = numpy.amin(data[101:150,2])
virpetwidmin = numpy.amin(data[101:150,3])
virseplenmin = numpy.amin(data[101:150,0])
virsepwidmin = numpy.amin(data[101:150,1])

# To calculate the mean of each variable for the Virginica class of Iris
virpetlenmean = numpy.mean(data[101:150,2])
virpetwidmean = numpy.mean(data[101:150,3])
virseplenmean = numpy.mean(data[101:150,0])
virsepwidmean = numpy.mean(data[101:150,1])

# To calculate the standard deviation from the mean for the Virginica class of Iris
virpetlenstd = numpy.std(data[101:150,2])
virpetwidstd = numpy.std(data[101:150,3])
virseplenstd = numpy.std(data[101:150,0])
virsepwidstd = numpy.std(data[101:150,1])


if setpetlenmax > verpetlenmax and setpetlenmax > virpetlenmax:
    print ("The", set, "class has the highest maximum petal length with", setpetlenmax, "cm")
elif verpetlenmax > setpetlenmax and verpetlenmax > virpetlenmax:
    print ("The", ver, "class has the highest maximum petal length with", verpetlenmax, "cm")
else:
    print ("The", vir , "class has the highest maximum petal length with", virpetlenmax, "cm")

if setpetlenmin < verpetlenmin and setpetlenmin < virpetlenmin:
    print ("The", set, "class has the lowest minimum petal length with", setpetlenmin, "cm")
elif verpetlenmin < setpetlenmin and verpetlenmin < virpetlenmin:
    print ("The", ver, "class has the lowest minimum petal length with", verpetlenmin, "cm")
else:
    print ("The", vir , "class has the lowest petal  minimum length with", virpetlenmin, "cm")
print ("The average petal length across all the classes is", petlenmean, "cm with a standard deviation of", petlenstd)

if setpetwidmax > verpetwidmax and setpetwidmax > virpetwidmax:
    print ("The", set, "class has the highest maximum petal width with", setpetwidmax, "cm")
elif verpetwidmax > setpetwidmax and verpetwidmax > virpetwidmax:
    print ("The", ver, "class has the highest maximum petal width with", verpetwidmax, "cm")
else:
    print ("The", vir , "class has the highest maximum petal width with", virpetwidmax, "cm")

if setpetwidmin < verpetwidmin and setpetwidmin < virpetwidmin:
    print ("The", set, "class has the lowest minimum petal width with", setpetwidmin, "cm")
elif verpetwidmin < setpetwidmin and verpetwidmin < virpetwidmin:
    print ("The", ver, "class has the lowest minimum petal width with", verpetwidmin, "cm")
else:
    print ("The", vir , "class has the lowest petal  minimum width with", virpetwidmin, "cm")
print ("The average petal width across all the classes is", petwidmean, "cm with a standard deviation of", petwidstd)

if setseplenmax > verseplenmax and setseplenmax > virseplenmax:
    print ("The", set, "class has the highest maximum sepal length with", setseplenmax, "cm")
elif verseplenmax > setseplenmax and verseplenmax > virseplenmax:
    print ("The", ver, "class has the highest maximum sepal length with", verseplenmax, "cm")
else:
    print ("The", vir , "class has the highest maximum sepal length with", virseplenmax, "cm")

if setseplenmin < verseplenmin and setseplenmin < virseplenmin:
    print ("The", set, "class has the lowest minimum sepal length with", setseplenmin, "cm")
elif verseplenmin < setseplenmin and verseplenmin < virseplenmin:
    print ("The", ver, "class has the lowest minimum sepal length with", verseplenmin, "cm")
else:
    print ("The", vir , "class has the lowest sepal minimum length with", virseplenmin, "cm")
print ("The average sepal length across all the classes is", seplenmean, "cm with a standard deviation of", seplenstd)

if setsepwidmax > versepwidmax and setsepwidmax > virsepwidmax:
    print ("The", set, "class has the highest maximum sepal width with", setsepwidmax, "cm")
elif versepwidmax > setsepwidmax and versepwidmax > virsepwidmax:
    print ("The", ver, "class has the highest maximum sepal width with", versepwidmax, "cm")
else:
    print ("The", vir , "class has the highest maximum sepal width with", virsepwidmax, "cm")

if setsepwidmin < versepwidmin and setsepwidmin < virsepwidmin:
    print ("The", set, "class has the lowest minimum sepal width with", setsepwidmin, "cm")
elif versepwidmin < setsepwidmin and versepwidmin < virsepwidmin:
    print ("The", ver, "class has the lowest minimum sepal width with", versepwidmin, "cm")
else:
    print ("The", vir , "class has the lowest sepal  minimum width with", virsepwidmin, "cm")
print ("The average sepal width across all the classes is", sepwidmean, "cm with a standard deviation of", sepwidstd)


pl.title("Petals")
pl.xlabel("Petal Length cm")
pl.ylabel("Petal Width cm")
pl.scatter(setpetlen, setpetwid)
pl.scatter(verpetlen, verpetwid)
pl.scatter(virpetlen, virpetwid)
pl.scatter(petlenmean, petwidmean)
pl.legend(["Setosa", "Versicolor", "Virginica", "Overall Mean"])
pl.show()   

pl.title("Sepals")
pl.xlabel("Sepal Length cm")
pl.ylabel("Sepal Width cm")
pl.scatter(setseplen, setsepwid)
pl.scatter(verseplen, versepwid)
pl.scatter(virseplen, virsepwid)
pl.scatter(seplenmean,sepwidmean)
pl.legend(["Setosa", "Versicolor", "Virginica", "Overall Mean"])
pl.show()   

