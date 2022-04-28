import yfinance as yf
from program import  calculate_gain_loss, list_converter, linear_regression
import sys
sys.path.insert(1, '/Users/cmunro50/Desktop/PythonMasterClass/stock_program/logging/')
from logger import tests_passed, test_failed

#Automated test function
def run_tests():

  #Defining Variables
  stock = 'msft'
  start = '2010-01-01'
  stop = '2020-01-01'
  x = 10
  expected_outputs = [30.6200008392334, 157.6999969482422, 127.07999610900879, 56.32216621046947]
  test_names = ['First open','Last close', 'Gain loss','Regression line']
  failed_tests = 0

  #Getting ticker data, returning open & close
  stock_data = yf.download(stock, start = start, end = stop)
  stock_open_list, stock_close_list = list_converter(stock_data)

  #Calling functions to test, storing outputs in list 
  gain_loss, first_open = calculate_gain_loss(stock_open_list, stock_close_list)
  last_close = stock_close_list[-1]
  regression_line = linear_regression(x,stock_open_list,stock_close_list)
  actual_outputs = [first_open, last_close, gain_loss, regression_line]
  
  #Comparing outputs
  for expected,actual,name in zip(expected_outputs, actual_outputs, test_names):

    if expected == actual:
      print('{} passed'.format(name))

    else: 
      print('{} failed'.format(name))
      print('Expected: {:.2f} Actual: {:.2f}'.format(expected, actual))
      failed_tests += 1
      test_failed(name)
      
  if failed_tests == 0:
    tests_passed()