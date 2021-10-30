
#---------------------------------------------------------getting html of website 


import pycurl
from io import BytesIO 

b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, 'https://www.atrsara.com/products/atrsara?filter%5B%5D=54')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()
print(get_body)