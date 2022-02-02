# API BLOG

** Under construction**

Starting point of a restful api where my database will store articles, stories, images and pictures, flight logs and tracks about my journey as a paragliding pilot.

Connected to react_blog app.

## STACK AND REQUIREMENTS

django + djangorestframework 

django cors headers

coverage for unit test

## MY LOGS

#### 16/01/2022
Initialize venv and install django. Start project and apps.

core is the project containing both app blog and blog_api.

blog_api is holding API functionnality while blog will hold a simple front end on the webserver.

to connect both app, core's urls.py is set up to include both app url conf.

creation of urls.py files in both apps.

in blog app are templates :
generic views : https://docs.djangoproject.com/fr/4.0/topics/class-based-views/

in blog_api are API endpoints.

Don't forgot to add apps to core/settings.py INSTALLED_APPS

creation of blog/index.html
creation of a template folder and core/settings, TEMPLATES add DIRS BASE_DIR/'templates'

try running server

creation of model in blog : category + post
build of custom manager on Post model
more info about models managers https://docs.djangoproject.com/fr/2.2/topics/db/managers/

makemigrations / migrate

Install djangorestframework (dont forgot to add it to app in core/settings.py)

Building api views and serializers under blog_api
https://www.django-rest-framework.org/api-guide/generic-views/

first trouble : DRF Postlist and PostDetail views weren't working as expected (with a form to create and POST model)
seems that serializer isnt working.
 -> solution: use of ModelSerializer class
 "The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields"

add a superuser as admin and adding models to django admin

setting permissions policy (DRF in core/settings.py) for now to any
https://www.django-rest-framework.org/api-guide/permissions/

Install coverage to help test app
Run :
coverage run --omit='*/venv/*' manage.py test
coverage html
writting missing tests bot in blog (blog content test) and blog_api (testing endpoints response)

CORS Cross-Origin Resource Sharing
Install django cors headers to allow React front end to be connected.
https://pypi.org/project/django-cors-headers/2.0.0/

more about cors :
https://web.dev/cross-origin-resource-sharing/


#### 20/01/2022
Changing rest framework permissions to IsAuthenticatedOrReadOnly
the admin is the only author able to perform CRUD's on posts
Created two different serializer for detail and list view (NB: different "actions" but same GET request for both of them.)
Refactored views.py with viewsets class from DRF. Defining both get_queryset and get_object.
As DRF provide router to automaticly handle URLS I also refactored urls.py
Added auto slug input on Post model save method.

#### 27/01/2022

Added a new model and new serializer, view and route for flight tracks.

#### 28 au 31/01/2022

Worked on photo models, serializer and views.
Configured setting and media folder.
For now models doesnt have any relationship with each other.

### TO BE MADE

Writting missing tests.