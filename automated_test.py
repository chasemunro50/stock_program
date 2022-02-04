import yfinance as yf
from program import  calculate_gain_loss, percentage_calculator, list_converter, linear_regression
import sys
sys.path.insert(1, '/home/runner/finalTermProject/logging/')
from logger import tests_passed, test_failed

#Automated test function
def run_tests():

  #Preset Input to Pass on
  stock = 'msft'
  start = '2010-01-01'
  stop = '2020-01-01'
  x = 10
  stock_data = yf.download(stock, start = start, end = stop)
  
  #Returning stock open and close
  stock_open_list, stock_close_list = list_converter(stock_data)

  #Printing / assigning variables for comparison
  gain_loss, first_open = calculate_gain_loss(stock_open_list, stock_close_list)
  last_close = stock_close_list[-1]
  percentage_calculator(gain_loss, first_open)
  regression_line = linear_regression(x,stock_open_list,stock_close_list)

  #Comparison print out for user to see exact amounts
  print('-'*35,'\nCOMPARISON\nExpected Vs Actual')
  print('First Open:\n30.62  |  {:0,.2f}'.format(first_open))
  print('Last Close:\n157.70 |  {:0,.2f}'.format(last_close))
  print('Gain / Loss:\n127.08 |  {:0,.2f}'.format(gain_loss))
  print('Regression Line:\n56.32  |  {:,.2f}'.format(regression_line))
  print('-'*35)
  print('TESTS')
  
  #lists of each set of numbers for comparison
  expected_outputs = [30.6200008392334, 157.6999969482422, 127.07999610900879, 56.32216621046947]
  actual_outputs = [first_open, last_close, gain_loss, regression_line]
  test_names = ['First open','Last close', 'Gain loss','Regression line']
  failed_tests = 0
  
  #Comparing outputs
  for expected,actual,name in zip(expected_outputs, actual_outputs, test_names):

    if expected == actual:
      print('{} passed'.format(name))

    else: 
      print('{} failed'.format(name))
      failed_tests += 1
      test_failed(name)
      
  if failed_tests == 0:
    tests_passed()