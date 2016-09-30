from django.contrib import admin
from .models import Profile,Domain
# Register your models here.

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["username", "firstname", "lastname", "gender", "dob", "profileimage"]
	class Meta:
		model = Profile

class DomainModelAdmin(admin.ModelAdmin):
	list_display = ["username", "domain"]
	class Meta:
		model = Domain

admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Domain, DomainModelAdmin)