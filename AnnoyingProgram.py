import os
import sys


while(True):
	os.system("say hi")
	stop = input("Type *stop* if u want this to stop: ")
if stop == 'stop':
	sys.exit()
else:
	os.system("say ha")