from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.
# from django.contrib.auth.models import User
User = get_user_model()



class Address(models.Model):
	user = models.ForeignKey(
		User, 
		verbose_name=_("user"), 
		on_delete=models.PROTECT
	)
	title = models.CharField(_("title of address"), max_length=150)
	country = models.CharField(_("country"), max_length=20)
	city = models.CharField(_("city"), max_length=50)
	zone = models.CharField(_("zone"), max_length=20)
	number = models.PositiveIntegerField(_("number"))
	zip_code = models.PositiveIntegerField(_("zip code of address"))
	is_customer = models.BooleanField(_("is it customer address?s"))

	# class Meta:
	# 	abstract = True


# class CustomerAddress(BaseAddress):

# 	def __str__(self):
# 		return self.title


# class SellerAdress(BaseAddress):
# 	def __str__(self):
# 		return self.title
