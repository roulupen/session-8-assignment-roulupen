import pytest
import os
import inspect
import re
import math
import random
import string
import math
from collections import namedtuple, Counter
import statistics
import time

import session8
from session8 import *

README_CONTENT_CHECK_FOR = [
    'Faker',
    'generate_profiles_using_named_tuples',
    'calculate_statistics_tuples',
    'generate_profiles_using_dictionary',
    'namedtuple',
    'Stock',
    'fake_company_generator',
    'calculate_market_value'
]

sample_profiles_tuples = [
    Profile('Alice', 'O+', (10.0, 20.0), 25),
    Profile('Bob', 'A+', (15.0, 25.0), 30),
    Profile('Charlie', 'B+', (20.0, 30.0), 35),
    Profile('David', 'O+', (25.0, 35.0), 40),
    Profile('Eve', 'A+', (30.0, 40.0), 45)
]

sample_profiles_dict = [
    {'name': 'Alice', 'blood_group': 'O+', 'current_location': (10.0, 20.0), 'age': 25},
    {'name': 'Bob', 'blood_group': 'A+', 'current_location': (15.0, 25.0), 'age': 30},
    {'name': 'Charlie', 'blood_group': 'B+', 'current_location': (20.0, 30.0), 'age': 35},
    {'name': 'David', 'blood_group': 'O+', 'current_location': (25.0, 35.0), 'age': 40},
    {'name': 'Eve', 'blood_group': 'A+', 'current_location': (30.0, 40.0), 'age': 45}
]

def test_session6_readme_exists():
    """ Test if ReadMe file exists for session8 """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session8_readme_500_words():
    """ Test if ReadMe file has atleast 500 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session8_readme_proper_description():
    """ Checks if Readme file has contents mentioned in READMELOOKSGOOD variable or else throw error"""
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session8_readme_file_for_more_than_10_hashes():
    """ Test to check if Readme file has atleast 10 #"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Your ReadMe file needs to have at least 10 #"


def test_session8_indentations():
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session8_function_name_had_cap_letter():
    """Test to check if any function names have any capital letters"""
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_session8_module_doc_string():
    """Test to check if the module has a docstring"""
    docstring = session8.__doc__
    assert docstring is not None, "Module does not have a docstring!"

def test_generate_profiles_using_named_tuples():
    """
    Test the generation of profiles using named tuples.
    """
    profiles = generate_profiles_using_named_tuples(1000)
    assert len(profiles) == 1000, "Number of profiles generated is incorrect."
    assert all(isinstance(profile, Profile) for profile in profiles), "Profiles are not namedtuples."

def test_largest_blood_type_tuples():
    """
    Test the calculation of the largest blood type.
    """
    stats = calculate_statistics_tuples(sample_profiles_tuples)
    assert stats['largest_blood_type'] == 'O+', "Largest blood type calculation is incorrect."

def test_mean_current_location_tuples():
    """
    Test the calculation of the mean current location.
    """
    stats = calculate_statistics_tuples(sample_profiles_tuples)
    expected_location = (
        statistics.mean([10.0, 15.0, 20.0, 25.0, 30.0]),
        statistics.mean([20.0, 25.0, 30.0, 35.0, 40.0])
    )
    assert stats['mean_current_location'] == expected_location, "Mean current location calculation is incorrect."

def test_oldest_person_age_tuples():
    """
    Test the calculation of the oldest person's age.
    """
    stats = calculate_statistics_tuples(sample_profiles_tuples)
    assert stats['oldest_person_age'] == 45, "Oldest person's age calculation is incorrect."

def test_average_age_tuples():
    """
    Test the calculation of the average age.
    """
    stats = calculate_statistics_tuples(sample_profiles_tuples)
    expected_average_age = statistics.mean([25, 30, 35, 40, 45])
    assert stats['average_age'] == expected_average_age, "Average age calculation is incorrect."

def test_functionality_tuples():
    """
    Test the namedtuple-based implementation for correctness.
    """
    stats = calculate_statistics_dict(sample_profiles_dict)
    print(stats)
    assert stats['largest_blood_type'] == 'O+', "Namedtuple: Largest blood type calculation is incorrect."
    assert stats['mean_current_location'] == (20.0, 30.0), "Namedtuple: Mean current location calculation is incorrect."
    assert stats['oldest_person_age'] == 45, "Namedtuple: Oldest person's age calculation is incorrect."
    assert stats['average_age'] == 35, "Namedtuple: Average age calculation is incorrect."

def test_generate_profiles_using_dictionary():
    """
    Test the generation of profiles using dictionaries.
    """
    profiles = generate_profiles_using_dictionary(1000)
    assert len(profiles) == 1000, "Number of profiles generated is incorrect."
    assert all(isinstance(profile, dict) for profile in profiles), "Profiles are not dictionaries."

def test_dict_functionality():
    """
    Test the dictionary-based implementation for correctness.
    """
    stats = calculate_statistics_dict(sample_profiles_dict)
    assert stats['largest_blood_type'] == 'O+', "Dict: Largest blood type calculation is incorrect."
    assert stats['mean_current_location'] == (20.0, 30.0), "Dict: Mean current location calculation is incorrect."
    assert stats['oldest_person_age'] == 45, "Dict: Oldest person's age calculation is incorrect."
    assert stats['average_age'] == 35, "Dict: Average age calculation is incorrect."

def test_performance_comparison():
    """
    Compare the performance of namedtuple vs dictionary implementations.
    """
    profiles = generate_profiles_using_named_tuples(100)
    start_time_namedtuple = time.time()
    more_profiles = profiles * 1000_000
    for profile in more_profiles:
        _ = profile.name
    elapsed_time_namedtuple = time.time() - start_time_namedtuple

    profiles_dict = generate_profiles_using_dictionary(100)
    start_time_dict = time.time()
    profiles_dict = profiles_dict * 1000_000
    for profile in profiles_dict:
        _ = profile['name']
    elapsed_time_dict = time.time() - start_time_dict

    print(f"Namedtuple: {elapsed_time_namedtuple}, Dictionary: {elapsed_time_dict}")

    assert elapsed_time_namedtuple > elapsed_time_dict, "Dictionary is faster than dictionary."


def test_stock_namedtuple_structure():
    """
    Test that the Stock namedtuple has the correct fields.
    """
    stock = Stock(name='Test Company', symbol='TSTC', open=100.0, high=110.0, close=105.0, weight=2.5)
    assert stock.name == 'Test Company'
    assert stock.symbol == 'TSTC'
    assert stock.open == 100.0
    assert stock.high == 110.0
    assert stock.close == 105.0
    assert stock.weight == 2.5

def test_fake_company_generator_output_type():
    """
    Test that fake_company_generator returns a list of Stock namedtuples.
    """
    stocks = fake_company_generator(10)
    assert isinstance(stocks, list)
    assert all(isinstance(stock, Stock) for stock in stocks)

def test_fake_company_generator_length():
    """
    Test that fake_company_generator returns the correct number of companies.
    """
    num_companies = 50
    stocks = fake_company_generator(num_companies)
    assert len(stocks) == num_companies

def test_stock_price_order():
    """
    Test that the open price is less than or equal to the high price,
    and the close price is between open and high.
    """
    stocks = fake_company_generator(10)
    print(stocks)
    for stock in stocks:
        assert stock.open <= stock.high
        assert stock.close <= stock.high

def test_calculate_market_value_open():
    """
    Test the calculation of market value using the 'open' price.
    """
    stocks = fake_company_generator(100)
    market_value = calculate_market_value(stocks, 'open')
    assert isinstance(market_value, float)
    assert market_value > 0

def test_calculate_market_value_high():
    """
    Test the calculation of market value using the 'high' price.
    """
    stocks = fake_company_generator(100)
    market_value = calculate_market_value(stocks, 'high')
    assert isinstance(market_value, float)
    assert market_value > 0

def test_calculate_market_value_close():
    """
    Test the calculation of market value using the 'close' price.
    """
    stocks = fake_company_generator(100)
    market_value = calculate_market_value(stocks, 'close')
    assert isinstance(market_value, float)
    assert market_value > 0

def test_stock_weight_distribution():
    """
    Test that the stock weights are within the expected range.
    """
    stocks = fake_company_generator(100)
    for stock in stocks:
        assert 1 <= stock.weight <= 5

def test_market_value_with_single_stock():
    """
    Test market value calculation with a single stock to ensure correct behavior.
    """
    stock = Stock(name='Single Stock', symbol='SNGL', open=200.0, high=220.0, close=210.0, weight=3.0)
    market_value = calculate_market_value([stock], 'close')
    assert market_value == stock.close

def test_edge_case_zero_weight():
    """
    Test edge case where a stock has zero weight (should be ignored in the calculation).
    """
    stock1 = Stock(name='Stock 1', symbol='STK1', open=200.0, high=220.0, close=210.0, weight=3.0)
    stock2 = Stock(name='Stock 2', symbol='STK2', open=200.0, high=220.0, close=210.0, weight=0.0)
    market_value = calculate_market_value([stock1, stock2], 'close')
    assert market_value == stock1.close