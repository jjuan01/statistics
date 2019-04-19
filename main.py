import math
import modules.data as data
import modules.mctdo as mctdo
import modules.deviation as deviation
import modules.print_data as pd


if __name__ == '__main__':

  data.initialize()

  singleData = 0

  while singleData != 'done':
    print("sample data")
    singleData = input()
    data.get_data(singleData)
  
  data.get_constants()

  pd.printall()

