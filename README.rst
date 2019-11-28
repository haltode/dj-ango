dj-ango
=======

    À mort plug.dj !

    -- haltode

Installation
------------

PostgreSQL
~~~~~~~~~~

You first need to install PostgreSQL, and then have a user with database
creation permission:

.. code:: bash

    $ sudo -u postgres createuser --createdb $USER

Website
~~~~~~~

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
    (venv) $ createdb cisco
    (venv) $ python manage.py migrate

    # Running
    (venv) $ python manage.py runserver

Testing
-------

Here is a dump of a test database: https://haltode.fr/upload/cisco-test.pgsql

To import it, use:

.. code:: bash

    $ createdb cisco
    $ psql cisco < cisco-test.pgsql

You can log in with:

- `admin` account (password: `admin`)
- users accounts such as `acu1` or `ing1-1` (password: `dj-ango-test`)
