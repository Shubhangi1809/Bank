from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image





class Test(models.Model):
    ID = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    Key = models.CharField(max_length=200)
    mac_id= models.CharField(max_length=200, null=True, blank=True)
    Device = models.CharField(max_length=200, null=True, blank=True)
    Username = models.CharField(max_length=200, null=True, blank=True)
    UsageDateAndTime = models.CharField(max_length=200, null=True, blank=True)
    Temperature = models.CharField(max_length=200, null=True, blank=True)
    pHin = models.CharField(max_length=200, null=True, blank=True)
    TDSin = models.CharField(max_length=200, null=True, blank=True)
    pHout = models.CharField(max_length=200, null=True, blank=True)
    TDSout = models.CharField(max_length=200, null=True, blank=True)
    MotorONInSeconds = models.CharField(max_length=200, null=True, blank=True)
    VolumeSampled = models.CharField(max_length=200, null=True, blank=True)
    NoOfHourUsed = models.CharField(max_length=200, null=True, blank=True)
    CartridgeLifeLeft = models.CharField(max_length=200, null=True, blank=True)
    OperationStatus = models.CharField(max_length=200, null=True, blank=True)
    InputTankUp = models.CharField(max_length=200, null=True, blank=True)
    InputTankDown = models.CharField(max_length=200, null=True, blank=True)
    OutputTankUp = models.CharField(max_length=200, null=True, blank=True)
    OutputTankDown = models.CharField(max_length=200, null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)



class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_Pic = models.ImageField(default="default.png", upload_to ="profile_pics")
    FullName = models.CharField(max_length=200)
    PhoneNo = models.CharField(max_length=10)
    Age = models.CharField(max_length=2)
    Country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Project"

    # def save(self):
    #     super().save()
    #     img = Image.open(self.Profile_Pic.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.Profile_Pic.path)







