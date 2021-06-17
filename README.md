## Install Virtual Environment
```
As Django works with Python Its better to create a Virtual Environment.
- virtualenv <envname> --python=python3
    - type this command to create a virtual environment, where envname can be any name chosen by user.
- To Activate Virtual Environment
    - source envname/bin/activate
- To Deactivate Virtual Environment
    - deactivate
```

## Instal required libraries from requirements.txt
```
Libraries required for working of Django Project, all libraries are stored in requirements.txt 
To Install type this command.
- pip install -r requirements.txt    
```

## For Database to run smoothly
```
    - python manage.py runserver
```


## For running Django Server
```
    - python manage.py install_labels
    - python manage.py migrate
```

## On Browser
```
    - Goto Browser and type : http://localhost:8000/network/login/
```