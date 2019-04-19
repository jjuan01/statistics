import modules.data as data
import modules.mctdo as mctdo
import modules.deviation as deviation

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

def print_const():
  print("n = ", data.n)
  print("m = ", data.m)
  print("c = ", data.c)

def printall():
  print_const()
  print_m()
  print_mg()
  print_mh()
  print_me()
  print_md()



