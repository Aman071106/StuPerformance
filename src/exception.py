import sys

def error_message_format(error,error_detail:sys):
    """
        This function takes error detail from sys module and returns custom app formatted string of that error. 
    """
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error_formatted=f"❌ AppError occured in python script [{file_name}] at Line [{line_no}] with following problem [{error}] "
    
    return error_formatted

class AppException(Exception):
    """
        This class handles my app exception.
    """
    def __init__(self,error,error_detail:sys):
        super.__init__(error)
        self.error_message-error_message_format(error=error,error_detail=error_detail)
    def __str__(self):
        return self.error_message