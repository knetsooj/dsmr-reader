MQTT
====

.. warning::

    Only follow these step if you have enabled MQTT.

.. contents::
    :depth: 2


Recent versions (v3.0.0 or higher)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Execute ``sudo supervisorctl status`` and check whether it includes ``dsmr_mqtt`` with status ``RUNNING``. If not, continue with the steps below.

* Copy the MQTT process config::

    sudo cp /home/dsmr/dsmr-reader/dsmrreader/provisioning/supervisor/dsmr_mqtt.conf /etc/supervisor/conf.d/

* Apply changes::

    sudo supervisorctl reread
    sudo supervisorctl update

* Executing ``sudo supervisorctl status`` should now include ``dsmr_mqtt`` with status ``RUNNING``.


Older versions (< v3.0.0)
~~~~~~~~~~~~~~~~~~~~~~~~~

* Execute ``sudo supervisorctl status`` and check whether it includes ``dsmr_mqtt`` with status ``RUNNING``. If not, continue with the steps below.

* Open ``/etc/supervisor/conf.d/dsmr-reader.conf`` (sudo required) and find::

    [program:dsmr_mqtt]
    environment=PYTHONUNBUFFERED=1
    command=/home/dsmr/.virtualenvs/dsmrreader/bin/python3 -u /home/dsmr/dsmr-reader/manage.py dsmr_mqtt
    directory=/home/dsmr/dsmr-reader/
    user=dsmr
    group=dsmr
    ### To enable: set 'autostart=true' below.
    ### Then execute: "sudo supervisorctl reread" and "sudo supervisorctl update"
    autostart=false
    autorestart=true

* Change::

    autostart=false

* To::

    autostart=true

* Save the file.

* Apply changes::

    sudo supervisorctl reread
    sudo supervisorctl update

* Executing ``sudo supervisorctl status`` should now include ``dsmr_mqtt`` with status ``RUNNING``.



MQTT caching
~~~~~~~~~~~~

Since DSMR-reader ``v2.6`` MQTT messages are:

* Sent with the ``retain`` flag, asking the broker to cache the latest value sent to each topic.
* Cached for an hour, to reduce the number of duplicate messages sent.
* Discarded when there is already another unsent message queued with the exact same topic and contents.

This prevents duplicate messages and removes a significant overhead.