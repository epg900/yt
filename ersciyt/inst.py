import os

def inst():
    try:
        os.system('''
        sudo apt install -y nginx
        sudo sed -i "s/root \/var\/www\/html/root \/tmp/" /etc/nginx/sites-enabled/default
        sudo sed -i "s/index index.html/index a.mp4 index.html/" /etc/nginx/sites-enabled/default
        sudo service nginx restart
        /usr/local/bin/django-admin  startproject proj
        sed -i "s/ALLOWED_HOSTS = \[/&'*'/" proj/proj/settings.py
        sed -i "s/INSTALLED_APPS = \[/& \n\t\t'ersciyt',/" proj/proj/settings.py
        sed -i "s/STATIC_URL = 'static\/'/& \nERSCIYT_LINK = 'https:\/\/80-$WEB_HOST'/" proj/proj/settings.py
        sed -i "s/from django.urls import path/&,include/" proj/proj/urls.py
        sed -i "s/urlpatterns = \[/&\n\t\tpath('', include('ersciyt.urls')),/"  proj/proj/urls.py
        python proj/manage.py runserver
        ''')
    except:
        print('Error in command')
        
