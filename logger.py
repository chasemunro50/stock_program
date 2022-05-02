import logging 

# Settings for logger (file, format, mode)
logging.basicConfig(filename="log/tests.log", 
          format='%(message)s %(asctime)s', 
          filemode='a') 
logger=logging.getLogger() 

# Log Functions with unique print messages 
def tests_passed():
  logger.setLevel(logging.DEBUG) 
  logger.debug("TESTS PASSED:") 

def test_failed(test):
  logger.setLevel(logging.DEBUG) 
  logger.debug("{} FAILED:".format(test)) 