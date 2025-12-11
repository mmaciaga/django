import random
import requests
from django.shortcuts import render


#W aplikacji myapp dodaj stronę about.html, aby wyświetlana była pod adresem /about/ i /about-me/ poprzez funkcję about_view(). Po dodaniu strony about uaktualnij linki w szablonach html, aby można było przechodzić między stronami.

# Create your views here.
def home_view(request):
    context = {
        'your_number': random.randint(1, 10),
        'bool_item': True,
        'some_list': [
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10),
        ],
        'some_dict': {'A': 1, 'B': 2, 'C': 3}
    }
    return render(request, 'myapp/index.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')

def about_view(request):
    context = {
        'lucky_number': random.randint(1, 10),
        'unlucky_number': random.randint(1, 10),
        'bool_item': True,
        'mytech': [
            {
                'name': 'HTML',
                'url': 'https://www.w3schools.com/html/',
                'level': 'beginner'
            },
            {
                'name': 'CSS',
                'url': 'https://www.w3schools.com/css/',
                'level': 'beginner'
            },
            {
                'name': 'Bootstrap',
                'url': 'https://getbootstrap.com',
                'level': 'beginner'
            },
            {
                'name': 'Python',
                'url': 'https://www.python.org',
                'level': 'intermediate'
            },
            {
                'name': 'Django',
                'url': 'https://www.djangoproject.com',
                'level': 'beginner'
            }
        ],
    }
    return render(request, 'myapp/about.html', context)

def genbank_view(request):
    genbank_url = requests.get('https://ftp.ncbi.nlm.nih.gov/genbank/README.genbank')
    gen_text = genbank_url.text
    version = None
    release_date = None

    for line in gen_text.splitlines():
        if 'GenBank Flat File Release' in line:
            version = line.strip()
        if 'Release Availability Date' in line:
            release_date = line.strip()


    context = {
        'version': version,
        'release_date': release_date,
    }
    return render(request, 'myapp/genbank.html', context)