from django.shortcuts import render
from django.http import  HttpResponse


def sample(request):
    dataset = {'books': [
        {
            'isbn': '9788499898803',
            'title': 'Cien años de soledad',
            'author': 'Gabriel García Márquez',
            'publish': '1967',
            'recommended': 'True'
        },
        {
            'isbn': '9788420428946',
            'title': '1984',
            'author': 'George Orwell',
            'publish': '1949',
            'recommended': True
        },
        {
            'isbn': '9788498382549',
            'title': 'El código Da Vinci',
            'author': 'Dan Brown',
            'publish': '2003',
            'recommended': False
        }
    ]}


    return render(request, 'sample.html', dataset)

def about_page(request):
    return render(request, 'about.html')

def home_page(request):
    return render(request, 'home.html')
