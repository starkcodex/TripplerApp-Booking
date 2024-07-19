from django.db import models
import uuid
# from django.contrib.auth import get_user_model


# User = get_user_model()


# class Category(models.Model):
#     name = models.CharField()


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media')
    hotel_amount = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    joined = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-joined']
    
    
# class Room(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     is_availbale = models.BooleanField(default=True)
#     room_amount = models.PositiveIntegerField()
    

# class Booking(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     guest_names = models.CharField(max_length=150)
#     guest_email = models.CharField(max_length=150)
#     guest_phone = models.CharField(max_length=20)
#     start_date = models.CharField()
#     end_date = models.CharField()
#     timestamp = models.DateTimeField(auto_now_add=True)
    
    
    