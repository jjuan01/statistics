import math

def initialize():
  global data
  global n
  global m
  global classes
  global nj

  data = []
  n = 0
  m = 0
  classes = []
  nj = []

def get_constants():
  global n
  global m
  global c
  global classes
  global nj

  n = len(data)
  # print(n)
  m = math.log10(n) * 3.3 + 1
  # print(m)
  c = (max(data) - min(data))/m
  # print(c)

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

def get_data():
  global data
  singleData = 0

  # while singleData != 'done':
  #   print("sample data")
  #   singleData = input()
  #   if singleData != 'done':
  #     data.append(int(singleData))
  data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5]
  
  get_constants()