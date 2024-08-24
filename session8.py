from faker import Faker
from collections import namedtuple, Counter
import statistics
import random

# Initialize Faker
fake = Faker()

# Define the namedtuple structure
Profile = namedtuple('Profile', ['name', 'blood_group', 'current_location', 'age'])

# Define the namedtuple structure for the stock data
Stock = namedtuple('Stock', ['name', 'symbol', 'open', 'high', 'close', 'weight'])

def generate_profiles_using_named_tuples(n = 10_000):
    """
    Generate a list of Profile namedtuples.
    :param n: Number of profiles to generate.
    :return: A list of Profile namedtuples.
    """
    profiles = []
    for _ in range(n):
        profile = fake.profile()
        name = profile['name']
        blood_group = profile['blood_group']
        current_location = profile['current_location']
        age = 2024 - profile['birthdate'].year
        profiles.append(Profile(name, blood_group, current_location, age))
    return profiles


def calculate_statistics_tuples(profiles):
    """
    Calculate the largest blood type, mean current location, oldest person age, and average age.

    :param profiles: A list of Profile namedtuples.
    :return: A dictionary containing the calculated statistics.
    """
    # Largest blood type
    blood_groups = [profile.blood_group for profile in profiles]
    largest_blood_group = Counter(blood_groups).most_common(1)[0][0]

    # Mean current location
    latitudes = [profile.current_location[0] for profile in profiles]
    longitudes = [profile.current_location[1] for profile in profiles]
    mean_current_location = (statistics.mean(latitudes), statistics.mean(longitudes))

    # Oldest person age
    oldest_person_age = max(profile.age for profile in profiles)

    # Average age
    average_age = statistics.mean(profile.age for profile in profiles)

    return {
        'largest_blood_type': largest_blood_group,
        'mean_current_location': mean_current_location,
        'oldest_person_age': oldest_person_age,
        'average_age': average_age
    }


def generate_profiles_using_dictionary(n = 10_000):
    """
    Generate a list of Profile dictionaries.
    :param n: Number of profiles to generate.
    :return: A list of Profile dictionaries.
    """
    profiles = []
    for _ in range(n):
        profile = fake.profile()
        profile_dict = {
            'name': profile['name'],
            'blood_group': profile['blood_group'],
            'current_location': profile['current_location'],
            'age': 2024 - profile['birthdate'].year
        }
        profiles.append(profile_dict)
    return profiles


def calculate_statistics_dict(profiles):
    """
    Calculate the largest blood type, mean current location, oldest person age, and average age using dictionaries.

    :param profiles: A list of profile dictionaries.
    :return: A dictionary containing the calculated statistics.
    """
    # Largest blood type
    blood_groups = [profile['blood_group'] for profile in profiles]
    largest_blood_group = Counter(blood_groups).most_common(1)[0][0]

    # Mean current location
    latitudes = [profile['current_location'][0] for profile in profiles]
    longitudes = [profile['current_location'][1] for profile in profiles]
    mean_current_location = (statistics.mean(latitudes), statistics.mean(longitudes))

    # Oldest person age
    oldest_person_age = max(profile['age'] for profile in profiles)

    # Average age
    average_age = statistics.mean(profile['age'] for profile in profiles)

    return {
        'largest_blood_type': largest_blood_group,
        'mean_current_location': mean_current_location,
        'oldest_person_age': oldest_person_age,
        'average_age': average_age
    }


def fake_company_generator(num_companies=100):
    """
    Generate fake stock data for an imaginary stock exchange.
    :param num_companies: Number of companies to generate.
    :return: List of Stock namedtuples containing company stock data.
    """
    stocks = []
    for _ in range(num_companies):
        name = fake.company()
        symbol = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
        open_price = round(random.uniform(100, 500), 2)
        high_price = round(open_price * random.uniform(1.01, 1.2), 2)  # Ensure high is slightly above open
        close_price = round(random.uniform(open_price * 0.95, high_price), 2)  # Close is between open and high
        weight = random.uniform(1, 5)  # Random weight for each stock
        stocks.append(Stock(name, symbol, open_price, high_price, close_price, weight))
    return stocks


# Calculate the market values
def calculate_market_value(stocks, price_type):
    """
    Calculate the market value based on the given price type (open, high, or close).

    :param stocks: List of Stock namedtuples.
    :param price_type: The price type to use for the calculation ('open', 'high', or 'close').
    :return: The calculated market value.
    """
    total_weight = 0
    weighted_sum = 0
    
    for stock in stocks:
        total_weight += stock.weight
        weighted_sum += getattr(stock, price_type) * stock.weight
    
    market_value = weighted_sum / total_weight
    return market_value