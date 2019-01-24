# Car Models
# Use Python to build a console app that interacts with two files:
  # car-makes
  # car-models

# Car Makes
# This file should contain just the names of several makes.
  # car-makes
  # Toyota
  # Nissan
  # ...

# Car Models
# This file should contain the names of several models for each make. The format will be as follows.
# {first letter of make}={model name}
  # car-models
  # T=Camry
  # N=Altima
# ...

# Requirements
# Create a single class that implements all functionality.


class CarList:

  """ Methods on Carlist """

  # Create a method for reading the car makes file.
  def read_make(self):
    with open('car_makes.txt', 'r') as makes:
      return makes.readlines()

  # Create a method for reading the car models file.
  def read_model(self):
    with open('car_models.txt', 'r') as models:
      return models.readlines()

  # Create a method that invokes the previous two methods and generates a dictionary.
  def make_dictionary(self):
    car_dict = {}



# mob_names = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]


  # The dictionary keys will be the make names.
  # The value for each key will be a list of model names.
  # {
  #     "Toyota": ["Camry"],
  #     ...
  # }

