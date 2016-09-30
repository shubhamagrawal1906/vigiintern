from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
import os

# def set_path(instance, filename):
# 	return os.path.join("image","profile",filename)

# Create your models here.

class Domain(models.Model):
	username = models.OneToOneField(User, null=True)
	domain = models.CharField(max_length=1000, blank=False, null=True)

	def __unicode__(self):
		return self.domain

class Profile(models.Model):
	username = models.OneToOneField(User,null=True)
	firstname = models.CharField(max_length=30, blank=True, null=True)
	lastname = models.CharField(max_length=30, blank=True, null=True)
	gender = models.IntegerField(default=1, blank=True, null=True)
	dob = models.DateField(blank=True, verbose_name="DOB", null=True)
	profileimage = models.FileField(blank=True, null=True)

	def __unicode__(self):
		list=[self.firstname,self.lastname]
		str=",".join(list)
		return str

	#def get_absolute_url(self):
	#	return reverse("posts:detail", kwargs={"id": self.id})

# class Database(models.MOdel):
# 	intern_id = models.AutoField(primary=True)
User.profile = property(lambda u: Profile.objects.get_or_create(username=u)[0])
User.domain = property(lambda u: Domain.objects.get_or_create(username=u)[0])
