from django.db import models

# Models
class Bus(models.Model):
    bus_id = models.CharField(max_length=5, unique=True)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    no_of_seats = models.IntegerField()
    rem_seats = models.IntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return self.bus_name

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUS = ((BOOKED, 'Booked'),(CANCELLED, 'Cancelled'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_id = models.CharField(max_length=5)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    no_of_seats = models.IntegerField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUS, default=BOOKED, max_length=2)

    class Meta:
        verbose_name_plural = "Booking List"

    def __str__(self):
        return self.email