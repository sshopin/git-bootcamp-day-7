#!/usr/bin/python

import datetime
utc_now = datetime.datetime.now(datetime.timezone.utc)
datetime_str = utc_now.strftime("%y.%m.%d %H:%M:%S")
print(f'Started: {datetime_str}')

try:
    print("Hello!")
except Exception as e:
    print(e)    
    pass
finally:
    # This block is optional but ensures cleanup if needed
    print('Finalization') 


 
