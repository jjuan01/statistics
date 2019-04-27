import modules.data as data
import modules.mctdo as mctdo
import modules.deviation as deviation

def cls():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

def print_m():
  print("M(x) =", mctdo.m())
  
def print_mg():
  print("Mg(x) =", mctdo.mg())

def print_mh():
  print("Mh(x) =", mctdo.mh())

def print_me():
  print("Me(x) =", mctdo.me())

def print_md():
  print("Md(x) =", mctdo.md())

def print_variance():
  print("Variance =", deviation.variance())

def print_std_deviation():
  print("Standard Deviation =", deviation.std_deviation())

def print_modal_deviation():
  print("Modal Deviation =", deviation.modal_deviation())

def print_median_deviation():
  print("Median Deviation =", deviation.median_deviation())
  
def print_const():
  print("n = ", data.n)
  print("m = ", data.m)
  print("c = ", data.c)
def printall():
  print_const()
  print("----------------------")
  print_m()
  print_mg()
  print_mh()
  print_me()
  print_md()
  print("----------------------")
  print_variance()
  print_std_deviation()
  print_modal_deviation()
  print_median_deviation()



