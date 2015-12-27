from django.http import HttpResponse


# multiple urls
def hello(request):
    return HttpResponse("Hello World")


def deardear(request):
    return HttpResponse("Dear World")


def doudou(request):
    return HttpResponse("Dou World")



##########################  template  ###################################
# html test: hard coded into function
def long_html(request):
    a=1
    b=2
    html = "<html><head>Template</head>  <br>  <body>This is body, <br> 2 numbers: %s, %s </body></html>" % (a, b)
    return HttpResponse(html)

# hard coded template
from django.template import Template, Context
def template_test(request):
    t = Template("<html><body>This is template <br> 1 number : {{ number }} <br> {{ string }}</body></html>")
    html = t.render(Context({'number': 1, 'string': 'hard coded'}))   # wrong: {'number': 1} {'number1': 2}
    return HttpResponse(html)

# real template
# don't forget to set templates dir TEMPLATES DIRS in setting.py
#from django.template import Template, Context
from django.template.loader import get_template
def template_test_1(request):
    t = get_template('template.html')
    html = t.render(Context({'number': 1, 'string':'real template'}))
    return HttpResponse(html)


# template: a more brief version, use this one
from django.shortcuts import render_to_response
def template_test_2(request):
    return render_to_response('template.html', {'number' : 2, 'string':'use this one'})

##########################  template  END ###################################




