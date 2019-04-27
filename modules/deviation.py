import statistics
import math
import modules.mctdo as mctdo
import modules.data as data

def variance():
  sumatory = 0

  if(data.type_of_variable == 'd'):
    for i in data.data:
      sumatory += pow((i - mctdo.m()), 2)
    return round((sumatory / data.n), 2)

  elif(data.type_of_variable == 'c'):
    for i in range(len(data.medium_point)):
      sumatory += data.nj[i] * pow((data.medium_point[i] - mctdo.m()), 2)
    return round((sumatory / data.n), 2)

def std_deviation():
  return round(math.sqrt(variance()), 2)

def modal_deviation():
  sumatory = 0
  if(data.type_of_variable == 'd'):
    for i in range(len(data.classes)):
      sumatory += abs(data.classes[i] - mctdo.md()) * data.nj[i]

    return round((sumatory / data.n), 2)

  elif(data.type_of_variable == 'c'):
    for i in range(len(data.medium_point)):
      sumatory += abs(data.medium_point[i] - mctdo.md()) * data.nj[i]

    return round((sumatory / data.n), 2)

def median_deviation():
  sumatory = 0

  if(data.type_of_variable == 'd'):
    for i in range(len(data.classes)):
      sumatory += abs(data.classes[i] - mctdo.me()) * data.nj[i]

    return round((sumatory / data.n), 2)

  elif(data.type_of_variable == 'c'):
    for i in range(len(data.medium_point)):
      sumatory += abs(data.medium_point[i] - mctdo.me()) * data.nj[i]

    return round((sumatory / data.n), 2)
