from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    type_choices = [('AC', 'AC'), ('Non-AC', 'Non-AC')]
    bus_type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return self.bus_number

class Route(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    distance = models.FloatField()
    duration = models.TimeField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.bus} - {self.route} - {self.departure_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.schedule} - Seat {self.seat_number}"

