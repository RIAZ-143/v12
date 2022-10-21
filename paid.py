import os, platform

 

try:

 

    import requests

 

except:

 

    os.system('pip install requests')

 

import requests

 

bit = platform.architecture()[0]

 

if bit == '64bit':

 

    from v12 import riaz

 

    riaz()

 

elif bit == '32bit':

 

    from v11 import riaz

 

    riaz()
