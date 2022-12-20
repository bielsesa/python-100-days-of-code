# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")




































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print): 
    with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer='10', expected_print='This is an even number.\n')

  def test_2(self):
    self.run_test(given_answer='12', expected_print="This is an even number.\n")

  def test_3(self):
    self.run_test(given_answer='90', expected_print='This is an even number.\n')

  def test_4(self):
    self.run_test(given_answer='13', expected_print='This is an odd number.\n')


print("\n\n\n.\n.\n.")
print('Checking what your code prints for several different numbers.\nFor the number 8 it should print this *exactly*:\n')
print('This is an even number.')
print('\nRunning some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 


