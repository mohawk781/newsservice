# Automated Notification Service in a federated Cloud Setup for de.NBI Cloud

It is recommended to run this service in a virtual environment. You can check out how to set up a virtual environment [here](https://docs.python.org/3/library/venv.html).

Once you activated the virtual environment you can install all necassary libarys and frameworks with:

<pre>$ pip install -r requirements.txt</pre>

Afterwards you need to deactivate and re-activate the virtual environment, so changes take place.

You need to point out to flask, which application you wanna run:

<pre>$ export FLASK_APP=newsservice</pre>

The port is set to 5000 on default.
In order to change the port of the service you can use:

<pre>$ export FLASK_RUN_PORT=****</pre>

Finally to run the service use:

<pre>$ flask run</pre>
