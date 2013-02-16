gal is a django based image gallery.  Its goal is to provide easy access to
viewing images and rating them.


Installation
------------

1. Add "gal" to your `INSTALLED_APPS` setting like this:

        INSTALLED_APPS = (
            ...
            'gal',
        )

2. Include the gal URLconf in your project `urls.py` like this:

        url(r'^gal/', include('gal.urls')),

3. Run `python manage.py syncdb` to create the gal models.

4. Run `python manage.py migrate gal` to run the gal migrations.

5. Configure `GAL_IMAGES_DIR` and `GAL_IMAGES_CACHE_DIR` and create them.

6. Copy directories, they represent galeries, of images to `gal/images` and run
   `gal/import-images` to import them.

