import statistics
import math
import modules.data as data

# import modules.menu
# from data.data import data.data, n, m, classes, nj

def m():
  if(data.type_of_variable == 'd'):
    sumatory = 0
    for i in range(len(data.data)):
      sumatory += data.data[i]
    return round(sumatory / data.n, 2)

  elif(data.type_of_variable == 'c'):
    sumatory = 0
    for i in range(len(data.medium_point)):
      sumatory += data.medium_point[i] * data.nj[i]
    return round(sumatory / data.n, 2)

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

    return round(geometric_mean, 2)

  elif(data.type_of_variable == 'c'):
    geometric_mean = 0
    sumatory = 0 
    for i in range(len(data.medium_point)):
      sumatory += math.log10(data.medium_point[i]) * data.nj[i]
    # print(sumatory)
    # print(sumatory / data.n)
    # print(math.log10(sumatory / data.n))
    geometric_mean = 10 ** (sumatory / data.n)

    return round(geometric_mean, 2)


def mh():
  return round(statistics.harmonic_mean(data.data), 2)

def me():
  return round(statistics.median(data.data), 2)

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
      
      return round((average / 2), 2)
    else:
      for i in range(len(data.nj)): 
        if(max(data.nj) == data.nj[i]):
          return round(data.classes[i], 2)

  elif(data.type_of_variable == 'c'):
    nk = max(data.nj)
    k = 0
    for i in range(len(data.nj)):
      if(data.nj[i] == nk):
        k = i

  # yprime k - 1
    ypkm = 0
  # yprime k + 1
    ypkp = 0
  # n k + 1
    nkp = 0
  # n k - 1
    nkm = 0

    if((k + 1) > (len(data.nj) + 1)):
      ypkp = 0
      nkp = 0
    else:
      ypkp = data.yprime[k + 2]
      nkp = data.nj[k + 1]

    ypkm = data.yprime[k]
    if((k - 1) < 0):
      nkm = 0
    else:
      nkm = data.nj[k - 1]

    return round(ypkm + ((data.c * (data.nj[k] - nkm))/(2 * data.nj[k] - nkm + nkp)), 2)