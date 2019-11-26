dj-ango
=======

    À mort plug.dj !

    -- haltode

Installation
------------

TODO: postgresql database setup

.. code:: bash
    # Cloning
    $ git clone git@github.com:haltode/dj-ango.git
    $ cd dj-ango

    # Python virtualenv and dependencies
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -U pip
    (venv) $ pip install -r requirements.txt

    # Configuration
    (venv) $ cp cisco/settings/{conf.sample.py,dev.py}
    (venv) $ $EDITOR cisco/settings/dev.py

    # Database setup
    (venv) $ python manage.py migrate

    # Running
    (venv) $ python manage.py runserver
