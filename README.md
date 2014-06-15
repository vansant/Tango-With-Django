Tango-With-Django
=================

# Design Assumptions
1. Python 2.x to follow along 
2. There is a one-to-many relationship between the category and page tables meaning each category can have many pages and each page belongs to one category.

# Setup (Ubuntu 14.04)
1. Install python-dev on Ubuntu - needed to compile and install Pillow

    $ sudo apt-get install python-dev
2. Install virutalenv

    $ sudo apt-get install python-virtualenv
3. Make a virtual environment (named venv here in example)

    $ virtualenv venv --no-site-packages
4. Activate the virtual environment (venv)

    $ source venv/bin/activate

    When you see your virtual environment name in parentheses like this(venv)$ you know you are using the virtual environment    
5. Install requirements

    $ pip install -r requirements.txt    
