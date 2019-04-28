import modules.data as data
import modules.mctdo as mctdo
import modules.deviation as deviation
import modules.utilities as uts

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
  print("S(x) =", deviation.std_deviation())
  print("C.V.(x) =", deviation.coefficient_of_variation(), "%")

def print_modal_deviation():
  print("DMd(x) =", deviation.modal_deviation())
  print("CVMd(x) =", deviation.modal_coefficient_of_variation(), "%")

def print_median_deviation():
  print("Dme(x) =", deviation.median_deviation())
  print("CVMe(x) =", deviation.median_coefficient_of_variation(), "%")

def print_deviations():
  print_variance(), print_std_deviation(), print_modal_deviation(), print_median_deviation()
  
def print_const():
  print("n = ", data.n)
  print("m = ", data.m)
  print("c = ", data.c)

def printall():
  print_const()
  print("------------------------------")
  print("MEASURES OF CENTRAL TENDENCY")
  print("------------------------------")
  print_m(), print_mg(), print_mh(), print_me(), print_md()
  print("------------------------------")
  print("DEVIATIONS")
  print("------------------------------")
  print_variance()
  print("------------------------------")
  print_std_deviation()
  print("------------------------------") 
  print_modal_deviation()
  print("------------------------------")
  print_median_deviation()



