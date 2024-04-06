from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# class Book(models.Model):
#     name=models.CharField(max_length=100)
#     price=models.PositiveBigIntegerField(help_text='in cents')
#     weight=models.PositiveBigIntegerField(help_text='in grams')

#     def __str__(self) -> str:
#         return super().__str__()
# we want to sell ebook as well with physical book instead of creating two different model we will create single model

# class Book(models.Model):
#     TYPE_PHYSICAL = 'physical'
#     TYPE_VIRTUAL = 'virtual'
#     TYPE_CHOICES = (
#         (TYPE_PHYSICAL, 'Physical'),
#         (TYPE_VIRTUAL, 'Virtual'),
#     )
#     type = models.CharField(
#         max_length=20,
#         choices=TYPE_CHOICES,
#         default=TYPE_PHYSICAL,
#     )

#     # common attribute
#     name=models.CharField(max_length=100)
#     price=models.PositiveBigIntegerField(help_text='in cents')

#     # specifi attribute
#     weight=models.PositiveBigIntegerField(help_text='in grams')

#     # specific attribute
#     download_link=models.URLField(null=True,blank=True)

#     # validation 
#     #  clean() is only called automatically by Django forms
#     def clean(self) -> None:
#         if self.type == Book.TYPE_VIRTUAL:
#             if self.weight != 0:
#                 raise ValidationError(
#                     'A virtual product weight cannot exceed zero.'
#                 )

#             if self.download_link is None:
#                 raise ValidationError(
#                     'A virtual product must have a download link.'
#                 )

#         elif self.type == Book.TYPE_PHYSICAL:
#             if self.weight == 0:
#                 raise ValidationError(
#                     'A physical product weight must exceed zero.'
#                 )

#             if self.download_link is not None:
#                 raise ValidationError(
#                     'A physical product cannot have a download link.'
#                 )

#         else:
#             assert False, f'Unknown product type "{self.type}"'

#     def __str__(self) -> str:
#         return super().__str__()

# abstract base class 
# class Product(models.Model):
#     class Meta:
#         abstract = True

#     name = models.CharField(
#         max_length=100,
#     )
#     price = models.PositiveIntegerField(
#         help_text='in cents',
#     )

#     def __str__(self) -> str:
#         return self.name


# class Book(Product):
#     weight = models.PositiveIntegerField(
#         help_text='in grams',
#     )


# class EBook(Product):
#     download_link = models.URLField()
    
# class Cart(models.Model):
#     user = models.OneToOneField(
#         get_user_model(),
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#     # prodcut table is abstract so its table will not be created so relation will not work.
#     # books = models.ManyToManyField(Product)

#     # to solve above problem we can do this.
#     book = models.ManyToManyField(Book)
#     ebook = models.ManyToManyField(EBook)

# in above model in Cart we have give reference of each type of book becuase Prodcut table is not created to solve 
# this issue we can remvoe abstract base class 

class Product(models.Model):

    name = models.CharField(
        max_length=100,
    )

    price = models.PositiveIntegerField(
        help_text='in cents',
    )

    def __str__(self) -> str:
        return self.name


class Book(Product):
    f_name =models.CharField(
        max_length=100,
    )
    weight = models.PositiveIntegerField(
        help_text='in grams',
    )


class EBook(Product):

    m_name=models.CharField(
        max_length=100,
    )
    download_link = models.URLField()

class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
    )
    # prodcut table is abstract so its table will not be created so relation will not work.
    # books = models.ManyToManyField(Product)

    # to solve above problem we can do this.
    items = models.ManyToManyField(Product)

print("****************************Generic Foriegen key********************************************************************")
#in above model When a derived model is created, Django adds a bases attribute to the migration:

#   migrations.CreateModel(
#       name='Book',
#       fields=[...],
#       bases=('concrete_base_model.product',),
#   ),
# If in the future you remove or change the base class, Django might not be able to perform the migration automatically. You might get this error:

# TypeError: metaclass conflict: the metaclass of a derived class must 
# be a (non-strict) subclass of the metaclasses of all its bases
# This is a known issue in Django (#23818, #23521, #26488). To work around it, you must edit the original migration manually and adjust the bases attribute.

