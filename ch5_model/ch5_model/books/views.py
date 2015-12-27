from django.shortcuts import render
from django.http import HttpResponse
from books.models import DatabaseTest



# Create your views here.
def books_hello(request):
    html = "books hello"
    DatabaseTest.objects.all().delete()
    return HttpResponse(html)


# database testing functions
def books_write(request):
    # method 0
    write_data = DatabaseTest(name='a')
    write_data.save()
    write_data = DatabaseTest(name='b')
    write_data.save()
    write_data = DatabaseTest(name='c')
    write_data.save()
    # method 1: prefered
    DatabaseTest.objects.create(name='d')

    html = "books write"
    return HttpResponse(html)

def books_update(request):
#    read_data = DatabaseTest.objects.filter(id = '20').update(name = 'updated') # get a list
    read_data = DatabaseTest.objects.filter(name = 'a').update(name = 'updated') # get a list
    html = "books update"
    return HttpResponse(html)


def books_read(request):
#    read_data = DatabaseTest.objects.get(name='a')  # get one
#    read_data = DatabaseTest.objects.order_by('name') # get a list
    read_data = DatabaseTest.objects.all() # get a list
#    read_data = DatabaseTest.objects.filter(id = 10) # get a list

    number=0
    html=''
    for x in read_data:
        temp = str(number) + ': '+ str(x.id) + 'th in data base, name=' + x.name +'<br>'
        html = html + temp
        number = number+1

#    html = html."books read"
    return HttpResponse(html)


# load image
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def image(request):
    image_path = os.path.join(BASE_DIR, 'static/image/')
    image_data = open(image_path + "image_0.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")  # no more mimetype

# template
from django.shortcuts import render_to_response
def template(request):
    return render_to_response('template.html', {'number' : 2, 'string':'use this one'})

from django.shortcuts import render_to_response
def bootstrap(request):
    return render_to_response('bootstrap.html')






