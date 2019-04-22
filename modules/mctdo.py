import statistics
import math
import modules.data as data

# import modules.menu
# from data.data import data.data, n, m, classes, nj

def m():
  return statistics.mean(data.data)

def mg():
  # global data.type_of_variable

  if(data.type_of_variable == 'd'):
    geometric_mean = 0
    sumatory = 0 
    for i in data.data:
      sumatory += math.log10(i)
    # print(sumatory)
    # print(sumatory / data.n)
    # print(math.log10(sumatory / data.n))
    geometric_mean = 10 ** (sumatory / data.n)

    return geometric_mean

  elif(data.type_of_variable == 'c'):
    geometric_mean = 0
    sumatory = 0 
    for i in range(len(data.medium_point)):
      sumatory += math.log10(data.medium_point[i]) * data.nj[i]
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
  howManyMax = 0
  if(data.type_of_variable == 'd'):
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

  elif(data.type_of_variable == 'c'):
    statistics.mode(data.data)
    # k_indexes = []
    # for i in range(len(data.nj)):
    #   if(data.nj[i] == max(data.nj)):
    #     k_indexes.append(i)
    #     howManyMax += 1
      
    # if(howManyMax>1):
    #   average = 0


    # #   for i in range(len(data.nj)):
    # #     if(max(data.nj) == data.nj[i]):
    # #       average += data.classes[i]
      
    # # #   return (average / 2)
    # else:
    #   k = k_index[0]
    #   mode = data.yprime[k] + ((data.c) * (nj[k] - ))