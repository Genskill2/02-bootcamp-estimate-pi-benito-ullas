import math
import random
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

def wallis(no):
	pi = 1
	x = range(1, no+1, 1)
	for i in x:
		pi *= (4*i*i)/((4*i*i)-1)
	return (2*pi)

def monte_carlo(no):
	r = 1
	centre = r
	circle = 0
    
	for i in range(no):
		x = (2*random.random()) - centre
		y = (2*random.random()) - centre
		if math.sqrt((x*x)+(y*y)) <= r :
			circle += 1
            
	return (4*circle/no)
            
if __name__ == "__main__":
    unittest.main()
