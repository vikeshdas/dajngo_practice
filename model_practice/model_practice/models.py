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
class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text='in cents',
    )

    def __str__(self) -> str:
        return self.name


class Book(Product):
    weight = models.PositiveIntegerField(
        help_text='in grams',
    )


class EBook(Product):
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
    book = models.ManyToManyField(Book)
    ebook = models.ManyToManyField(EBook)



