#Found at http://stackoverflow.com/questions/691946/short-and-useful-python-snippets by theodor

class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width

    def __call__(self,x):
         # x in percent
         self.pointer = int(self.width*(x/100.0))
         return "|" + "#"*self.pointer + "-"*(self.width-self.pointer)+\
                "|\n %d percent done" % int(x) 
