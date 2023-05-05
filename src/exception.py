import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()    # This will contain details of file, line number where error is occuring.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)   # we are inheriting the init function, and the exception class. 
        self.error_message = error_message_detail(error_message,error_detail = error_detail )

        # Note - error_detail is tracked by sys. 

    def __str__(self):
        return self.error_message

# To test this file
# if __name__ == "__main__":

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Dividing by zero")
#         raise CustomException(e,sys) 
