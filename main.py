import math
import statistics

data = []
n = 0
m = 0
classes = []
nj = []

def get_data(singleData):
  if singleData != 'done':
    data.append(int(singleData))

  # print(data)

def get_constants():
  global n
  global m
  global c
  n = len(data)
  # print(n)
  m = math.log10(n) * 3.3 + 1
  # print(m)
  c = (max(data) - min(data))/m
  # print(c)


def M():
  return statistics.mean(data)

def Mg():
  geometric_mean = 0
  sumatory = 0 
  for i in data:
    sumatory += math.log10(i)

  geometric_mean = 10 ** math.log10(sumatory / n)
  return geometric_mean

def Mh():
  return statistics.harmonic_mean(data)

def Me():
  return statistics.median(data)

def Md():
  global classes
  global nj 

  for i in data:
    newClass = True
    for j in classes:
      if( i == j):
        newClass = False
    if(newClass):
      classes.append(i)
      
  for i in classes:
    nj.append(0)
  for i in (data):
    for j in range(len(classes)):
      if(i == classes[j]):
        nj[j] += 1

  howManyMax = 0

  for i in nj:
    if(i == max(nj)):
      howManyMax += 1

  if(howManyMax>1):
    average = 0
    for i in range(len(nj)):
      if(max(nj) == nj[i]):
        average += classes[i]
    
    return (average / 2)
  else:
    for i in range(len(nj)): 
      if(max(nj) == nj[i]):
        return classes[i]
  

if __name__ == '__main__':

  singleData = 0

  while singleData != 'done':
    print("sample data")
    singleData = input()
    get_data(singleData)
  
  get_constants()


