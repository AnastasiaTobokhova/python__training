# Sam's Surf Shop
# Welcome to Sam’s Surf Shop! This project will exercise your knowledge of errors and unit testing practices in Python.
# It will also give you a small taste of testing a full application.
# You’ve been hired to create a handful of tests for the shopping cart software at the surf shop.
# Once that is done, you’ll implement some improvements for these tests using more advanced unit testing features
# (skipping, parameterization, and expected failures). Finally, you’ll have the opportunity to fix bugs that were exposed
# by your tests.
# The shopping cart software for Sam’s Surf Shop lives inside of the file called surfshop.py.
# Look over the files and familiarize yourself with their contents. Most of our work will take place in tests.py.

import unittest
import surfshop

class TestSurfShop(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_one_surfboard(self):
        result = self.cart.add_surfboards(1)
        self.assertEqual(result, 'Successfully added 1 surfboard to cart!')

    def test_add_multiple_surfboards(self):
        for num_boards in [2, 3, 4]:
            with self.subTest(num_boards=num_boards):
                result = self.cart.add_surfboards(num_boards)
                self.assertEqual(result, f'Successfully added {num_boards} surfboards to cart!')

    @unittest.skip("Skipping test as the 4 surfboards limit is not enforced during off season.")
    def test_too_many_boards_error(self):
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards(5)
    @unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()














