from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()



class Category(models.Model):
	title = models.CharField(_("title of Product"), max_length=250)
	description = models.TextField(_("description"))
	parent = models.ForeignKey(
		"self",
		verbose_name="child of which category",
		on_delete=models.PROTECT,
		null=True, blank=True
	)

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(_("title of Product"), max_length=250)

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(_("title of Product"), max_length=250)
	category = models.ForeignKey("product.Category", verbose_name=_("category"), on_delete=models.PROTECT)
	seller = models.ForeignKey(User, verbose_name=_("user that sell this item"), on_delete=models.PROTECT) 
	is_active = models.BooleanField(_("is available item?"), default=True)
	price = models.PositiveIntegerField(_("price of Product")) 
	qty_stock = models.PositiveIntegerField(_("quantity of Product form supplier"))
	tags = models.ManyToManyField("product.Tag", verbose_name=_("tags"))

	def __str__(self):
		return self.title


class Favorite(models.Model):
	user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.PROTECT) 
	product = models.ForeignKey("product.Product", verbose_name=_("product"),on_delete=models.PROTECT)

	class Meta:
		unique_together = [["user", "product"]]

	def __str__(self):
		return "{} {}".format(self.user.username, self.product.title)


