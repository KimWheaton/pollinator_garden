from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USPostalCodeField

class Gardener(models.Model):
    PIEDMONT = 'PM'
    MOUNTAINS = 'MT'
    COASTAL_PLAIN = 'CP'

    REGION_CHOICES = [
        ('PIEDMONT', 'Piedmont'),
        ('MOUTAINS', 'Mountains'),
        ('COASTAL_PLAIN', 'Coastal Plain'),
]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moniker = models.CharField(max_length=240)
    region = models.CharField(choices=REGION_CHOICES, max_length=100)
    experience_level = models.IntegerField()
    effort_level = models.IntegerField()

def __str__(self):
    return self.moniker

class Plant(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    WATER_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
]
    TREE = 'T'
    SHRUB = 'S'
    FLOWER = 'F'
    GRASS = 'G'

    TYPE_CHOICES = [
        ('TREE', 'Tree'),
        ('SHRUB', 'Shrub'),
        ('FLOWER', 'Flower'),
        ('GRASS', 'Grass'),
]

    common_name = models.CharField(max_length=240, blank=True, null=True)
    scientific_name = models.CharField(max_length=240, blank=True, null=True)
    # zone = models.ManyToManyField('GrowingZone', related_name="plants")
    plant_type = models.CharField(choices=TYPE_CHOICES, blank=True, null=True, max_length=100)
    moisture_need = models.CharField(choices=WATER_CHOICES, max_length=100)
    color = models.CharField(max_length=240, blank=True, null=True)
    flowering_time = models.CharField(max_length=240, blank=True, null=True)
    NC_native = models.BooleanField(default=True)
    bee_friendly = models.BooleanField(default=True)
    butterfly_friendly = models.BooleanField(default=True)
    hummingbird_friendly = models.BooleanField(default=True)

def __str__(self):
    return self.common_name if self.common_name else self.scientific_name    

class Image(models.Model):
    plant = models.ForeignKey(Plant, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

def __str__(self):
    return self.image

# class GrowingZone(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
