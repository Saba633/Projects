import time
import os

print(os.getcwd())
os.mkdir('testing')
time.sleep(5)
os.rename('testing', 'tested')
time.sleep(5)
