'''
print("Програма успішно запущена")
import logging
logging.basicConfig(level=logging.ERROR)
logging.info("Програма успішно запущена")


age = -5
if age < 0:
    logging.error("Error")

import logging
logging.basicConfig(filename="test.txt", level=logging.INFO)
logging.info("Hi!")
logging.warning("Little problem")
logging.error("Error")


import logging
logging.basicConfig(level=logging.ERROR)
try:
    x = int("abc")
except ValueError:
    logging.error("Can't convert str to int")
else:
    print(x)
'''

import logging
'''
logging.basicConfig(level=logging.ERROR)
try:
    5 / 0
except Exception:
    logging.exception("Division by zero")


result = 10 + 5
assert result == 15


import unittest
def squere(x):
    return x*x

class TestSquere(unittest.TestCase):
    def test_squere(self):
        self.assertEqual(squere(5), 25)

if __name__ == "__main__":
    unittest.main
'''

import unittest
'''
def squere(x):
    return x*x

class TestSquere(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(squere(0), 0)

    def test_negative(self):
        self.assertEqual(squere(-3), 9)

def divide(a,b):
    return a / b

class TestDevide(unittest.TestCase):
    def test_zero_devision(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
'''

def check_age(age):
    if age < 0:
        raise ValueError("Wrong age!")
    return age

import unittest

class TestAge(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(check_age(18), 18)

    def test_raise(self):
        with self.assertRaises(ValueError):
            check_age(-5)