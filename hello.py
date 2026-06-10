#!/usr/bin/python

import datetime
utc_now = datetime.datetime.now(datetime.timezone.utc)
datetime_str = utc_now.strftime("%y.%m.%d %H:%M:%S")
print(f'Started: {datetime_str}')

print("Hello!")
