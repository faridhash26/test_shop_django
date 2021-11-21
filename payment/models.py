from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Basket(models.Model):
	user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.PROTECT)
	is_paiad = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.user.username

class BasketItem(models.Model):
	basket = models.ForeignKey("payment.Basket", verbose_name=_("basket"), on_delete=models.PROTECT)
	product = models.ForeignKey("product.Product", verbose_name=_("produce"), on_delete=models.PROTECT)
	qnt = models.PositiveIntegerField(_("quantity"))
	price = models.PositiveIntegerField(_("product price in create time"))

	def __str__(self):
		return "{} {}".format(self.basket.user.username, self.product.title)