from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id.__str__()

class Store(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name.__str__()

class Mileage(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    registered_date = models.DateTimeField('Registered Date', default=timezone.now())

    def __str__(self):
        store = Store.objects.get(id=self.store)
        user = User.objects.get(id=self.user)
        string = store.__str__() + '/' + user.__str__() + '/' + self.registered_date.__str__()
        return string