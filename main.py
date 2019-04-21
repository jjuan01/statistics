import sys
import math
import modules.data as data
# import modules.mctdo as mctdo
# import modules.deviation as deviation
import modules.print_data as pd
import modules.menu as menu

if __name__ == '__main__':

  finish = False

# LOOP FOR FINISHING PROGRAM
  while(finish == False):
    request = menu.main_menu()
  #Check exit
    menu.check_exit(request)
  #Record data
    if (request == 'r' or request == 'R'):
    # Request for type of variable
      request_variables = menu.type_of_varible_menu()
    # Calculations for entered values
      data.initialize(request_variables)
      new_entry = False
    #Collect data sample
      data.get_data() 
    # LOOP FOR KEEP WORKING WITH SAME SAMPLE 
      while(new_entry == False):
      # Request for measure to show
        request = menu.measures_menu()
      #Check exit
        menu.check_exit(request)
        if(request == 'n' or request == 'N'):
          new_entry = True
          pd.cls()
      # Calls measure requested
        menu.switch(request)
  #Error output
    else:
      print("Wrong entry")