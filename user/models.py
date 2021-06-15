from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver




from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    sector = models.CharField(max_length=15, null=True,blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)

    institute1 = models.CharField(max_length=20, null=True, blank=True)
    institute2 = models.CharField(max_length=20, null=True, blank=True)
    institute3 = models.CharField(max_length=20, null=True, blank=True)
    institute4 = models.CharField(max_length=20, null=True, blank=True)

    degree1 = models.CharField(max_length=8, null=True,blank=True)
    degree2 = models.CharField(max_length=8, null=True,blank=True)
    degree3 = models.CharField(max_length=8, null=True,blank=True)
    degree4 = models.CharField(max_length=8, null=True,blank=True)

    year1 = models.CharField(max_length=4, null=True, blank=True)
    year2 = models.CharField(max_length=4, null=True, blank=True)
    year3 = models.CharField(max_length=4, null=True, blank=True)
    year4 = models.CharField(max_length=4, null=True, blank=True)

    grade1 = models.CharField(max_length=8, null=True,blank=True)
    grade2 = models.CharField(max_length=8, null=True,blank=True)
    grade3 = models.CharField(max_length=8, null=True,blank=True)
    grade4 = models.CharField(max_length=8, null=True,blank=True)

    skills = models.CharField(max_length=100, null=True, blank=True)
    certifications = models.CharField(max_length=100, null=True, blank=True)

    companyname1 = models.CharField(max_length=20, null=True, blank=True)
    companyname2 = models.CharField(max_length=20, null=True, blank=True)
    companyname3 = models.CharField(max_length=20, null=True, blank=True)

    position1 = models.CharField(max_length=20, null=True, blank=True)
    position2 = models.CharField(max_length=20, null=True, blank=True)
    position3 = models.CharField(max_length=20, null=True, blank=True)

    duty1 = models.CharField(max_length=20, null=True, blank=True)
    duty2 = models.CharField(max_length=20, null=True, blank=True)
    duty3 = models.CharField(max_length=20, null=True, blank=True)

    timeperiod1 = models.CharField(max_length=20, null=True, blank=True)
    timeperiod2 = models.CharField(max_length=20, null=True, blank=True)
    timeperiod3 = models.CharField(max_length=20, null=True, blank=True)

    project = models.CharField(max_length=150, null=True, blank=True)
    interest = models.CharField(max_length=150, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    








User = get_user_model()
class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)

