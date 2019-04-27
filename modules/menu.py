import sys
import modules.print_data as pd
import modules.mctdo as mctdo

def main_menu():
  pd.cls()
  print("╔═════════════╗")
  print("║[R]ecord data║")
  print("║[E]xit       ║")              
  print("╚═════════════╝")
  request = input()
  pd.cls()

  return request

def type_of_varible_menu():

  global request_variables

  print("╔════════════╗")
  print("║[D]iscreet  ║")
  print("║[C]ontinuous║")
  print("╚════════════╝")
  request = input()
  pd.cls()

  request_variables = request

  return request

def measures_menu():
  print("╔════════════════════════════════════════════╗")
  print("║ SHOW                                       ║")
  print("╠════════╦══════════════════╦════════════════╣")
  print("║ [M]ean ║ [G]eometric mean ║ [H]armonic mean║")
  print("╠════════╩═╦══════════╦═════╩══╦═════════════╣")
  print("║ [Me]dian ║ [Me]dian ║ [Mo]de ║             ║")
  print("╠══════════╩══════════╩════════╩═════════════╣")
  print("║ [D]eviations                               ║")
  print("╠════­════════════════════════════════════════╣")
  print("║ [A]ll                                      ║")
  print("╚════­════════════════════════════════════════╝")
  print("╔════════════════════════════════════════════╗")
  print("║ [N]ew entry                                ║")
  print("╚════════════════════════════════════════════╝")
  request = input()
  pd.cls()

  return request

def check_exit(request):
  if(request == 'E' or request == 'e'):
      finish = True
      sys.exit()

  return request

def switch(request):
  # if(request_variables == 'D' or request_variables == 'd'):
  if(request == 'C' or request == 'c'):
    pd.print_const()
  if(request == 'M' or request == 'm'):
    pd.print_m()
  elif(request == 'G' or request == 'g'):
    pd.print_mg()
  elif(request == 'H' or request == 'h'):
    pd.print_mh()
  elif(request == 'Me' or request == 'me'):
    pd.print_me()
  elif(request == 'Mo' or request == 'mo'):
    pd.print_md()
  elif(request == 'D' or request == 'd'):
    pd.print_deviations()
  elif(request == 'A' or request == 'a'):
    pd.printall()
  # elif(request_variables == 'C' or request_variables == 'c'):
  #   print("Continuas")
