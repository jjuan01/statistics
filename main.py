import sys
import math
import modules.data as data
# import modules.mctdo as mctdo
# import modules.deviation as deviation
import modules.print_data as pd
import modules.menu as menu

if __name__ == '__main__':

  data.initialize()

  finish = False

  while(finish == False):
    request = menu.main_menu()
  #Check exit
    menu.check_exit(request)
  #Record data
    if (request == 'r' or request == 'R'):
    # Calculations for entered values
      request_variables = menu.type_of_varible_menu()
      new_entry = False
      while(new_entry == False):
        data.get_data()      
        request = menu.measures_menu()
      #Check exit
        menu.check_exit(request)
        if(request == 'n' or request == 'N'):
          new_entry = True
          pd.cls()
        menu.switch(request_variables, request)
  #Error output
    else:
      print("Wrong entry")
  # data.get_data()

  # pd.printall()