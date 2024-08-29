from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)])
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation
