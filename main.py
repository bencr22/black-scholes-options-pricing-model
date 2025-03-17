from math import e, sqrt, log
from scipy.stats import norm

"""
Call = S * N(d1) - N(d2) * K(e^-rT)
Put = N(-d2) * K(e^-rT) - N(-d1) * S
"""

current_stock_price = 100
strike_price = 95
interest_rate = 0.035
years_to_maturity = 4
volatility = 0.4

# Calculate the current value of the strike price. 
# Money changes value over time, so discount the strike price to reflect that.
strike_price_current_value = strike_price * (e ** (-1 * interest_rate * years_to_maturity))

"""
Call = stock_price * N(d1) - N(d2) * strike_price_current_value
Put = N(-d2) * strike_price_current_value - N(-d1) * stock_price

where, N(x) = integral( (e^((-x^2)/2)) / sqrt(2 * pi) ) between -inf and x.
"""

d_denominator = volatility * sqrt(years_to_maturity)

d1_numerator = log(current_stock_price / strike_price) + ((interest_rate + (volatility ** 2) / 2) * years_to_maturity)
d1 = d1_numerator / d_denominator

d2_numerator = log(current_stock_price / strike_price) + ((interest_rate - (volatility ** 2) / 2) * years_to_maturity)
d2 = d2_numerator / d_denominator

call = (current_stock_price * norm.cdf(d1)) - (norm.cdf(d2) * strike_price_current_value)
put = (norm.cdf(-d2) * strike_price_current_value) - (norm.cdf(-d1) * current_stock_price)

print(f"Call: {call}")
print(f"Put: {put}")