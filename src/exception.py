'''
This code is a Python class called CustomException that is designed to be used as an exception. 
This means that when an error occurs in a program, this class can be used to print out a more detailed message about the error. 
The code also imports the sys module from the src.logger package and defines a function called error_message_detail. 
This function takes two parameters, error and error_detail, which is the sys module. 
This function then gets information about the error, such as the name of the file and the line number,
 and puts this information into a string.

The CustomException class is then defined. It takes two parameters, error_message and error_detail. 
It then calls the super class constructor with the error_message. It then calls the error_message_detail function 
and stores the result in self.error_message. Finally, it defines the __str__ method which just returns the self.error_message.


This code is useful because it allows programmers to easily get more detailed information when an error occurs in their program. 
The error_message_detail function is used to get the error information and put it into a string, 
and the CustomException class is used to print out this detailed error message.

Here Exception class is inh in custome exception.
'''

import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message

    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

