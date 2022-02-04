import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date


def user_input():

  repeat = True
  while repeat == True:
    
    try:
        #User input
        user_stock = input('Input Ticker: ')
        print('Please input dates in the following format:\nyyyy-mm-dd')
        user_start = input('Input Start Date: ')
        user_stop = input('Input End Date: ')

        #Converting user input for yfinance
        user_start_formatted = date.fromisoformat(user_start)
        user_stop_formatted = date.fromisoformat(user_stop)

        #Getting Ticker Data From yfinance
        stock_data = yf.download(user_stock, start=user_start_formatted,end=user_stop_formatted)
        repeat = False

    except ValueError:
      print('-'*35,'\nPlease make sure your entering the correct value/format')

  return stock_data

#Indexes open & close from ticker dataframe, converts to list, 
def list_converter(stock_data):

  #Indexing open & close from dataframe, storing in variables
  stock_open = stock_data['Open']
  stock_close = stock_data['Close']

  #Converting variables to list
  stock_open_list = stock_open.tolist()
  stock_close_list = stock_close.tolist()
  return stock_open_list, stock_close_list

#Calculates gain/loss by subtracting last close from first open
def calculate_gain_loss(stock_open_list, stock_close_list):

  #Indexing first position from open and last position from close
  first_open = stock_open_list[0]
  last_close = stock_close_list[-1]
  gain_loss = last_close - first_open

  #Displaying output
  print('-'*35 + '\nFirst open: {:.2f}\nLast close: {:.2f}'.format(first_open,last_close))
  print('Total Gain / Loss: {:.2f}'.format(gain_loss))
  return gain_loss, first_open

#Calculates & Displays change in %
def percentage_calculator(gain_loss, first_open):

  percentage = (gain_loss / first_open)*100
  print('Increase / Decrease as a percentage {:.2f}%'.format(percentage))

#Line of best fit & coefficient of determination
def linear_regression(x,stock_open_list,stock_close_list):
  x_values = []
  y_values = []
  ##Linear Regression
  #variables for calculation
  n = len(stock_close_list)
  sum_x = 0
  sum_y = 0
  sum_x_squared = 0
  sum_xy = 0
  counter = 0

  #Calculating sums of x, y, x squared
  for x,y in zip(range(0, (len(stock_open_list))),stock_close_list):
    x_values.append(x)
    y_values.append(y)
    counter +=1
    sum_x = sum_x + counter
    sum_x_squared +=counter**2
    sum_y +=y

  #Solving for m
  sum_xy = sum_x * sum_y
  n_xy = n * sum_xy
  n_x = n * sum_x_squared
  nominator_m = n_xy - (sum_x * sum_y)
  denominator_m = (n_x-sum_x)**2
  m = nominator_m / denominator_m

  #Solving for b
  m_x = m * sum_x
  nominator_b = sum_y - m_x
  b = nominator_b/n

  #y=mx+b Calculation
  x +=n
  regression_line = m*x+b
  print('Point Prediction: {:.2f}'.format(regression_line))

  ##Coeffecient of Determination 
  y_mean = sum_y/counter
  TSS = 0
  SSR = 0
  x = 0

  y_line_of_best_fit = []

  for y in stock_close_list:
    x += 1 

    #Something going wrong with math here
    print('x value: {}'.format(x))
    print('m value: {}'.format(m))
    print('b value: {}'.format(b))
    print('mx value: {}'.format(m * x))
    linear_estimate = m*x+b
    y_line_of_best_fit.append(linear_estimate)

    TSS_remainder = y-y_mean
    SSR_remainder = linear_estimate-y_mean
    TSS += TSS_remainder**2
    SSR += SSR_remainder**2

  cd_ratio = SSR/TSS
  coefficient_determination = 1 - cd_ratio
  
  print("Coefficient of determination: {}".format(coefficient_determination))

  #Graphing
  plt.plot(x_values, y_values)
  plt.plot(x_values, y_line_of_best_fit)
  plt.xlabel('Days')
  plt.ylabel('Share Price')
  plt.title('Graph of Stock Share Price Over Time')
  plt.show()

  return regression_line

#Runs all functions seen above
def execute():
  try:
    #Downloading Dataframe
    stock_data = user_input()
    x = int(input('How many days ahead would you like your prediction?\n>'))

    #Returning stock open and close
    stock_open_list, stock_close_list = list_converter(stock_data)

    #Calculating & Printing gain loss, percentage change, and point prediction
    gain_loss, first_open = calculate_gain_loss(stock_open_list, stock_close_list)
    percentage_calculator(gain_loss, first_open)
    linear_regression(x,stock_open_list,stock_close_list)
  except IndexError:
    print('Something went wrong, please make sure your start date is before your end.')