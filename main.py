from math import e, sqrt, log
from scipy.stats import norm


def calculate_adjusted_strike_price(strike_price, interest_rate, years_to_maturity) -> float:
    # Calculate the current value of the strike price. 
    # Value of money changes over time, so discount strike price to reflect.
    return (strike_price * (e ** (-1 * interest_rate * years_to_maturity)))


def calculate_d_values(current_price, strike_price, interest_rate, years_to_maturity, volatility) -> float:
    d_denominator = volatility * sqrt(years_to_maturity)

    d1_numerator = log(current_price / strike_price) + ((interest_rate + (volatility ** 2) / 2) * years_to_maturity)
    d1 = d1_numerator / d_denominator

    d2_numerator = log(current_price / strike_price) + ((interest_rate - (volatility ** 2) / 2) * years_to_maturity)
    d2 = d2_numerator / d_denominator

    return d1, d2


def calculate_call_price(current_price, strike_price, interest_rate, years_to_maturity, volatility) -> float:
    adjusted_strike_price = calculate_adjusted_strike_price(strike_price, interest_rate, years_to_maturity)
    d1, d2 = calculate_d_values(current_price, strike_price, interest_rate, years_to_maturity, volatility)

    #Call = S * N(d1) - N(d2) * K(e^-rT)
    return (current_price * norm.cdf(d1)) - (norm.cdf(d2) * adjusted_strike_price)


def calculate_put_price(current_price, strike_price, interest_rate, years_to_maturity, volatility) -> float:
    adjusted_strike_price = calculate_adjusted_strike_price(strike_price, interest_rate, years_to_maturity)
    d1, d2 = calculate_d_values(current_price, strike_price, interest_rate, years_to_maturity, volatility)

    #Put = N(-d2) * K(e^-rT) - N(-d1) * S
    return (norm.cdf(-d2) * adjusted_strike_price) - (norm.cdf(-d1) * current_price)


# Current price of the stock.
current_stock_price = 100
# Price at which the option many be purchased for or sold at.
strike_price = 95
# Annual risk free interest rate. 
interest_rate = 0.04
# Years until the option expires.
years_to_maturity = 4
# Calcualted by taken the std. dev. of the log of returns.
volatility = 0.4

call = calculate_call_price(current_stock_price, strike_price, interest_rate, years_to_maturity, volatility)
put = calculate_put_price(current_stock_price, strike_price, interest_rate, years_to_maturity, volatility)

print(f"Call: {call}")
print(f"Put: {put}")