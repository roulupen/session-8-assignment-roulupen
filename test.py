from session8 import *
import pytest

companies = fake_company_generator(10)
print(companies)

assert len(companies) == 10
print(companies)
for stock in companies:
    assert stock.open <= stock.high
    assert stock.close <= stock.high