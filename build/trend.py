import sys
import os
from pytrends.request import TrendReq
s=open("file1.csv","w")

curpath = os.path.abspath(os.curdir)
pytrend = TrendReq()
pytrend.build_payload(kw_list=["blue", "red"])
df = pytrend.interest_over_time()
s.write(df.to_string())
#file_name = curpath + "file1.csv"
#df.to_csv("file1.csv", encoding='utf-8', index=False)
file = open(os.path.join(curpath, "file2.csv"), 'w')
with file as f:
    sys.stdout = f
    print("Sum of blue queries:" + str(df['blue'].sum()))
    print("Sum of red queries:" + str(df['red'].sum()))
