import sys
import os
from pytrends.request import TrendReq #import pytrends to make a http get request 
# constants
searchKeyword1 = "blue"
searchKeyword2 = "red"
#Create file in write mode to stream response from pytrends to file1
stream = open("file1.csv", "w")
currentPath = os.path.abspath(os.curdir)
pytrend = TrendReq()
pytrend.build_payload(kw_list=[searchKeyword1, searchKeyword2])
dataFrame = pytrend.interest_over_time()
stream.write(dataFrame.to_string())
file = open(os.path.join(currentPath, "file2.csv"), 'w')
with file as f:
    sys.stdout = f
    print("Sum of blue queries:" + str(dataFrame[searchKeyword1].sum()))
    print("Sum of red queries:" + str(dataFrame[searchKeyword2].sum()))
