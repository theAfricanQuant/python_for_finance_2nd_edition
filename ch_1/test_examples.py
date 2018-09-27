import unittest
from examples import Example
import timeit 


class Test_ch_1(unittest.TestCase):

    def setUp(self):
        self.ex = Example()

    def tearDown(self):
        pass

    def test_monte_carlo_estimator_for_euro_opts(self):
        answer = self.ex.monte_carlo_estimator_for_euro_option(
                100.0, 105.0, 1.0, 0.05, 0.2)
        self.assertGreater(answer, 7.9)
        self.assertGreater(8.1, answer)
    
    def test_analyze_historical_index_levels(self):
        data = self.ex.analyze_historical_index_levels(
            "http://hilpisch.com/tr_eikon_eod_data.csv")
        self.assertEqual(data.columns[0], ".SPX")
        self.assertEqual(data.columns[1], "rets")
        self.assertEqual(data.columns[2], "vola")
    
    def test_time_analysis_on_loops(self):
        first_attempt = timeit.Timer(
                lambda: "self.ex.loop_slow(2500000)").timeit()

        second_attempt =  timeit.timeit(
                lambda: "self.ex.loop_medium(2500000)")  

        third_attempt =  timeit.timeit(
                lambda: "self.ex.loop_fast(2500000)") 
        
        self.assertGreater(first_attempt, second_attempt)
        self.assertGreater(second_attempt, third_attempt)



        print("this is 1st: {}\n2nd: {}\n3rd: {}".format(
            first_attempt, second_attempt, third_attempt))
        



        self.assertEqual(True, False)

if __name__ == "__main__":
     unittest.main()
