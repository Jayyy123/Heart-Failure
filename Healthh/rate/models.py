from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank = False)
    nick_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0, null=False, blank = False)
    sex = models.IntegerField(blank=False, null=False, default=0)
    anaemia = models.IntegerField(blank=False, null=False, default= 0)
    creatinine_phosphokinase = models.IntegerField(blank=False, null=False , default= 0)
    diabetes = models.IntegerField(blank=False, null=False, default= 0)
    ejection_fraction = models.IntegerField(blank=False, null=False, default= 0)
    high_blood_pressure = models.IntegerField(blank=False, null=False, default= 0) 
    platelets = models.IntegerField(blank=False, null=False, default= 0)
    serum_creatinine = models.IntegerField(blank=False, null=False, default= 0)
    serum_sodium = models.IntegerField(blank=False, null=False, default= 0)
    smoking = models.IntegerField(blank=False, null=False, default= 0)
    time = models.IntegerField(blank=False, null=False, default= 0)
    log = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self) -> str:
        return self.first_name
@receiver(post_save, sender = User)
def update(sender, instance, created, **kwargs):
    if created:
        user = instance
        details = Details.objects.create(
            user = user,
            first_name = user.username
        )

    print("Hello")
    print("instance:", instance)
    # print("instance:", instance)
    print("Created:", created)

@receiver(post_delete, sender = Details)
def deletedetails(sender, instance, **kwargs):
    user = instance.user
    user.delete()

class HeartFailure(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    result = models.IntegerField()
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self) -> str:
        return self.first_name


# post_save.connect(update, sender = Details)