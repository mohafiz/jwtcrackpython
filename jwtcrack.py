import jwt
import sys
from termcolor import colored

if len(sys.argv) != 3:
      print 'Usage: python {} {} {}'.format(sys.argv[0], 'encoded_jwt', 'dictionary_list')
      sys.exit(1)

encoded = sys.argv[1]
dictionary_list = sys.argv[2]

with open(dictionary_list, 'r') as dic:
   for secret in dic:
      try:
         jwt.decode(encoded, secret, algorithms=['HS256'])
         print colered('secret is ' + secret, 'green')
	 sys.exit(0)
      except:
         print colored('Error in decoding JWT !', 'red')