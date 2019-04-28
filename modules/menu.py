import sys
import modules.mctdo as mctdo
import modules.utilities as uts

def main_menu():
  uts.cls()
  print("╔═════════════╗")
  print("║[R]ecord data║")
  print("║[E]xit       ║")              
  print("╚═════════════╝")
  request = input()
  uts.cls()

  return request

def type_of_varible_menu():

  global request_variables

  print("╔════════════╗")
  print("║[D]iscreet  ║")
  print("║[C]ontinuous║")
  print("╚════════════╝")
  request = input()
  uts.cls()

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
  print("╠════════════════════════════════════════════╣")
  print("║ [A]ll                                      ║")
  print("╚════════════════════════════════════════════╝")
  print("╔════════════════════════════════════════════╗")
  print("║ [N]ew entry                                ║")
  print("╚════════════════════════════════════════════╝")
  request = input()
  uts.cls()

  return request

def check_exit(request):
  if(request == 'E' or request == 'e'):
      finish = True
      sys.exit()

  return request

def switch(request):
  # if(request_variables == 'D' or request_variables == 'd'):
  if(request == 'C' or request == 'c'):
    uts.print_const()
  if(request == 'M' or request == 'm'):
    uts.print_m()
  elif(request == 'G' or request == 'g'):
    uts.print_mg()
  elif(request == 'H' or request == 'h'):
    uts.print_mh()
  elif(request == 'Me' or request == 'me'):
    uts.print_me()
  elif(request == 'Mo' or request == 'mo'):
    uts.print_md()
  elif(request == 'D' or request == 'd'):
    uts.print_deviations()
  elif(request == 'A' or request == 'a'):
    pd.printall()
  # elif(request_variables == 'C' or request_variables == 'c'):
  #   print("Continuas")
