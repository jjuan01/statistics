import statistics
import math
import modules.data as data

# from data.data import data.data, n, m, classes, nj

def m():
  return statistics.mean(data.data)

def mg():
  geometric_mean = 0
  sumatory = 0 
  for i in data.data:
    sumatory += math.log10(i)
  # print(sumatory)
  # print(sumatory / data.n)
  # print(math.log10(sumatory / data.n))
  geometric_mean = 10 ** (sumatory / data.n)
  return geometric_mean

def mh():
  return statistics.harmonic_mean(data.data)

def me():
  return statistics.median(data.data)

def md():
  for i in data.data:
    newClass = True
    for j in data.classes:
      if( i == j):
        newClass = False
    if(newClass):
      data.classes.append(i)
      
  for i in data.classes:
    data.nj.append(0)
  for i in (data.data):
    for j in range(len(data.classes)):
      if(i == data.classes[j]):
        data.nj[j] += 1

  howManyMax = 0

  for i in data.nj:
    if(i == max(data.nj)):
      howManyMax += 1

  if(howManyMax>1):
    average = 0
    for i in range(len(data.nj)):
      if(max(data.nj) == data.nj[i]):
        average += data.classes[i]
    
    return (average / 2)
  else:
    for i in range(len(data.nj)): 
      if(max(data.nj) == data.nj[i]):
        return data.classes[i]