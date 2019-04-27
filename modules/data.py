import math

def initialize(type_of_variable_request):
  global data
  global n
  global m
  global nj
  global type_of_variable

  data = []
  n = 0
  m = 0

  if(type_of_variable_request == 'D' or type_of_variable_request == 'd'):
    global classes

    type_of_variable = 'd'

    classes = []
    nj = []

  elif(type_of_variable_request == 'C' or type_of_variable_request == 'c'):
    global medium_point
    global yprime

    type_of_variable = 'c'

    medium_point = []
    nj = []
    yprime = []

def get_constants():
  global n
  global m
  global c
  global nj

  n = len(data)
  # print(n)
  m = int(round((math.log10(n) * 3.3 + 1), 0))
  # print(m)
  c = round((max(data) - min(data))/m, 2)
  # print(c)

  # Discreet variable constant calculations
  if(type_of_variable == 'd'):
    global classes
    for i in data:
      newClass = True
      for j in classes:
        if(i == j):
          newClass = False
      if(newClass):
        classes.append(i)
        
    for i in classes:
      nj.append(0)
    for i in (data):
      for j in range(len(classes)):
        if(i == classes[j]):
          nj[j] += 1

  # Continuous variable constant calculations
  elif(type_of_variable == 'c'):
    global yprime
    global medium_point
    for i in range((int(round(m, 0)) + 1)):
      yprime.append(int(round(min(data) + (c * i), 0)))
    for i in range(len(yprime) - 1):
      medium_point.append(((yprime[i+1] - yprime[i]) / 2) + yprime[i])
    for i in medium_point:
      nj.append(0)
    for i in (data):
      for j in range(len(medium_point)):
        if(i >= yprime[j] and i <= yprime[j + 1]):
          nj[j] += 1

def get_data():
  global data
  singleData = 0

  # while singleData != 'done':
  #   print("sample data")
  #   singleData = input()
  #   if singleData != 'done':
  #     data.append(int(singleData))
  
  # data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5]

  data = [30, 20, 90, 90, 40, 60, 20, 30, 10, 120, 40, 90, 60, 120, 20, 15, 60, 15, 60, 30, 15, 15, 40, 20, 40]
  get_constants()