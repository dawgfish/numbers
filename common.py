ERROR_MSG = "error: input must be a postive integer..."

class NegativeInteger(Exception):
    def __init___(self,dErrorArguments):
        Exception.__init__(self,"negative integer exception was raised with argument {0}".format(dErrArguments))
        self.dErrorArguments = dErrorArguements
        
def pos(val):
   if val < 0 :
       raise NegativeInteger({
                'input' : val 
       })
   else:
       return val
