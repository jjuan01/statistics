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