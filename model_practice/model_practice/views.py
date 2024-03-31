from django.http import HttpResponse
from model_practice.models import Book,Cart,EBook
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
def run_script(request):
    print("*******************************************************************************************************")
    # book = Book.objects.create(name='Python Tricks', price=1000, weight=200)
    # print(book.name)

    # haki = User.objects.create_user('vikesh103')
    # print("user",haki)
    
    # cart = Cart.objects.create(user=haki)
    # print("cart",cart.user)

    # cart.book.add(book)
    # print(cart.book.all())

    print("*********************************************************************************************************")
    # WE want to sell e book as well 

    # add physical book
    # physical_book = Book.objects.create(type=Book.TYPE_PHYSICAL,name='Python Tricks',price=1000,weight=200,download_link=None,)
    # print("physical book",physical_book.name)

    # add virtual book
    # virtual_book = Book.objects.create(type=Book.TYPE_VIRTUAL,name='The Old Man and the Sea',price=1500,weight=0,download_link='https://books.com/12345')
    # print(virtual_book.download_link)
    # Your users can now add both books and e-books to the car 
    # cart.book.add(virtual_book,physical_book)#car and book is manyto many relation sheep so one instance of cart can have many instance of book
    # print(cart.book.all())

    print("*********************************************************************************************************")
    # using aboce method what if user add weight in virual_book weight of ebook is not possible,to solve this problem we
    # we can add validation in model for virtual_book don't accept weight from form but this becomes little complex.

    print("**********************************************abstract base class*****************************************")
    book = Book.objects.create(name='Python Tricks', price=1000, weight=200)
    print("book",book)
    ebook=EBook.objects.create(name="ebook python Trick",price=200,download_link='http://books.com/12345')
    print(ebook)

    # create user
    user =User.objects.create_user('vik777eshdas998')
    print(user)
    # user = get_user_model().objects.first()
    cart = Cart.objects.create(user=user)
    cart.book.add(book)
    cart.ebook.add(ebook)
    print("cart",cart)

    print(cart.objects.filter(pk=cart.pk))
    return HttpResponse("Script executed successfully:")