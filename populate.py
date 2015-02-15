import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Myapp.settings')

import django
django.setup()

from Myblog.models import Category, Page

def populate():
    python_cat = add_cat('Pythoon')

    add_page(cat= python_cat,
             title = "Official Python Tutorial")
    add_page(cat=python_cat,
             title = "How to Think like a computer Scientist")
    add_page(cat=python_cat,
             title="Learn Python in 10 minutes")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
             title="Official Django Tutorial")


    add_page(cat=django_cat,
             title="Django Rocks")

    add_page(cat=django_cat,
             title="How to Tango with Django")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
             title="Bottle")

    add_page(cat=frame_cat,
             title="Flask")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()