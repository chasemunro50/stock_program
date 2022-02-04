from program import execute 
from automated_test import run_tests


while True:
  try:
    selection = int(input('1. Program \n2. Automated Test\n>'))

    if selection == 1:
      execute()
      break

    elif selection == 2:
      run_tests()
      break  

    else:
      print('Please input either 1 or 2.')

  except ValueError:
    print('Please input either 1 or 2.')