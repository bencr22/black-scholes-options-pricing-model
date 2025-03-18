from math import e, sqrt, log
from scipy.stats import norm

class BlackScholesModel:
    
    def __init__(self, asset_price, strike_price, interest_rate, years_to_maturity, volatility):
        self.asset_price = asset_price
        self.strike_price = strike_price
        self.interest_rate = interest_rate
        self.years_to_maturity = years_to_maturity
        self.volatility = volatility
        self.d_values = self.calculate_d_values()
        self.adjusted_strike_price = self.calculate_adjusted_strike_price()


    def calculate_adjusted_strike_price(self) -> float:
        # Calculate the current value of the strike price. 
        # Value of money changes over time, so discount strike price to reflect.
        return (self.asset_price * (e ** (-1 * self.interest_rate * self.years_to_maturity)))
    

    def calculate_d_values(self) -> tuple:
        # Calculate values used multiple times in function.
        calc = log(self.asset_price / self.strike_price)
        d_denominator = self.volatility * sqrt(self.years_to_maturity)

        d1 = (calc + ((self.interest_rate + (self.volatility ** 2) / 2) * self.years_to_maturity)) / d_denominator
        d2 = (calc + ((self.interest_rate - (self.volatility ** 2) / 2) * self.years_to_maturity)) / d_denominator

        return d1, d2
    

    # Calculate the call value for the given inputs.
    def calculate_call_value(self) -> float:
        d1, d2 = self.d_values

        # Call = S * N(d1) - N(d2) * K(e^-rT)
        return (self.asset_price * norm.cdf(d1)) - (norm.cdf(d2) * self.adjusted_strike_price)
    

    # Calculate the put value for the given inputs.
    def calculate_put_value(self) -> float:
        d1, d2 = self.d_values

        # Put = N(-d2) * K(e^-rT) - N(-d1) * S
        return (norm.cdf(-d2) * self.adjusted_strike_price) - (norm.cdf(-d1) * self.asset_price)