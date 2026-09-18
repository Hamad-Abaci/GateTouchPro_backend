from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class LaneGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Lane(models.Model):
    name = models.CharField(max_length=100)
    lane_group = models.ForeignKey("LaneGroup",null=True,default=None,on_delete=models.CASCADE,related_name="lanegroup")
    turnstyles= models.ManyToManyField("TurnStyle",related_name="lanes")
    width= models.IntegerField(default=60)
    created_by = models.CharField(max_length=100, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.CharField(max_length=100,blank=True,null=True)
    deleted_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name



    
class TurnStyle(models.Model):

    TYPE_CHOICES = [
        ("center", "Center"),
        ("side", "Side"),
        ("differently_abled", "Differently Abled"),
    ]
    make = models.CharField(max_length=100,blank= True,null= True)
    model = models.CharField(max_length=100,default="UNKNOWN")
    type = models.CharField(max_length=30,choices=TYPE_CHOICES)
    is_left = models.BooleanField(default=False)
    entry_pin = models.IntegerField()
    exit_pin = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.CharField(max_length=100,blank=True,null=True)
    deleted_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        side = "Left" if self.is_left else "Right"
        return f"{self.type} - {side}"




class SystemConfig(models.Model):

    wifi_ssid = models.CharField(max_length=100)
    wifi_password = models.CharField(max_length=255)

    def __str__(self):
        return self.wifi_ssid


 
class AccessLog(models.Model):

    lane = models.ForeignKey(Lane,on_delete=models.CASCADE,related_name="logs")
    user = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(blank=True, null=True)
    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lane} - {self.user} - {self.triggered_at}"