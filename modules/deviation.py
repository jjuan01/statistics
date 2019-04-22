import statistics
import math
import modules.mctdo as mctdo
import modules.data as data

def variance():
  sumatory = 0

  if(data.type_of_variable == 'd'):
    for i in data.data:
      sumatory += (i - mctdo.m()) * (i - mctdo.m())
    return (sumatory / data.n)

  elif(data.type_of_variable == 'c'):
    for i in data.medium_point:
      sumatory += (i - mctdo.m()) * (i - mctdo.m())
    return (sumatory / data.n)

def std_deviation():
  return math.sqrt(variance())

def modal_deviation():
  sumatory = 0

  for i in range(len(data.classes)):
    sumatory += abs(data.classes[i] - mctdo.md()) * data.nj[i]

  return (sumatory / data.n)

def median_deviation():
  sumatory = 0

  for i in range(len(data.classes)):
    sumatory += abs(data.classes[i] - mctdo.me()) * data.nj[i]

  return (sumatory / data.n)