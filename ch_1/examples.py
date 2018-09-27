import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Example:
    def __init__(self):
        pass

    def monte_carlo_estimator_for_euro_option(self, S0, K, T, R, sigma):
        I = 10000
        np.random.seed(1000)
        z = np.random.standard_normal(I)
        ST = S0 * np.exp((R - sigma ** 2/2) * T + sigma * math.sqrt(T) *z)
        hT = np.maximum(ST - K, 0)
        C0 = math.exp(-R * T) * np.mean(hT)
        return C0

    def analyze_historical_index_levels(self, location):
        data  = pd.read_csv(location, index_col=0, parse_dates=True)
        data = pd.DataFrame(data['.SPX'])
        # data.info()
        data["rets"] = np.log(data / data.shift(1))
        data["vola"] = data['rets'].rolling(252).std() * np.sqrt(252)
        data[[".SPX", 'vola']].plot(subplots=True, figsize=(10,6))
        plt.savefig('./example_images/spx_colatility.png')
        return data

    def loop_slow(self, loops):
        for x in range(1, loops):
            pointless = 3 * math.log(x) + math.cos(x) ** 2
        return

    def loop_medium(self, loops):
        pass

    def loop_fast(self, loops):
        pass

