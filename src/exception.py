import sys
## import this logger file otherwise it won't show error in the log file
from src.logger import logging
## error- and error-detail:sys which will be isnisd sys
#: in param: Type denotes a type hint, specifying the expected type of a variable or function parameter
def error_message_detail(error,error_detail:sys):
    ## in first two thing which it telss we aren;t nterested we only want to know about exc_info(),whch will telss us on whcih line exception occured etc
    # it will be stored in this varaiable we cerated exc_tb variable
    _,_,exc_tb=error_detail.exc_info()
    #we are getting file name 
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
## we are replacing these placeholders 0,1,2 
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        ## we are inheriting from exception class sow e used super
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    ##__str__ Method: Defines how the CustomError object will be represented as a string.
    def __str__(self):
        return self.error_message
    