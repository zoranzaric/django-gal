gal is a django based image gallery.  Its goal is to provide easy access to
viewing images and rating them.


Installation
------------

    # create a virtualenv
    $ virtualenv .virtualenv

    # activate the virtualenv
    $ source .virtualenv/bin/activate

    # install dependencies
    $ pip install -r requirements.txt

    # create the database and an admin user
    $ python manage.py syncdb

    # run migrations
    $ python manage.py migrate gal

    # create images and cache directory
    $ mkdir images cache

    # copy images to images directory
    $ cp ~/some-image.jpg images

    # import images
    $ ./import-images

