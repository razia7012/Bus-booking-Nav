from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from django.db import models

class Route(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    distance = models.FloatField()
    duration = models.TimeField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"


class Bus(models.Model):
    bus_name = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=20,blank=True,null=True)
    capacity = models.PositiveIntegerField()
    type_choices = [('AC', 'AC'), ('Non-AC', 'Non-AC')]
    bus_type = models.CharField(max_length=10, choices=type_choices)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('No seats', 'No seats'),
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)  # Foreign key relationship

    def __str__(self):
        return f"{self.bus_name} - {self.bus_number} - {self.route.origin} to {self.route.destination}"


class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.bus} - {self.route} - {self.departure_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.schedule} - Seat {self.seat_number}"

