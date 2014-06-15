Tango-With-Django
=================

# Design Assumptions
1. Using Python 3.4 instead of Python 2.7 
2. There is a one-to-many relationship between the category and page tables meaning each category can have many pages and each page belongs to one category.

# Setup (Ubuntu 14.04)
1. Install python3

    $ sudo apt-get install python3
2. Install virutalenv

    $ sudo apt-get install python-virtualenv
3. Make a virtual environment for Python3 (named venv for this example)

    $ virtualenv venv --no-site-packages -p /usr/bin/python3

    --no-site-packages: do not include system packages

    -p: point to python3
4. Activate the virtual environment (venv)

    $ source venv/bin/activate

    When you see your virtual environment name in parentheses like this(venv)$ you know you are using the virtual environment    
5. Install requirements

    $ pip install -r requirements.txt    

6. Set SECRET_KEY environment variable
   

    $ nano ~/.bash_profile

    Add this export statement and include your own secret key between the double quotes

    export SECRET_KEY=""

    $ source ~/.bash_profile
