## Automated Notification Service in a federated Cloud Setup for de.NBI Cloud

### Starting the Automated Notification Service
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

The terminal should display something similar to this:
<pre>
 * Serving Flask app "newsservice"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
</pre>

The service is now up and running. You can visit the web page at http://localhost:5000.

### Publishing a News at the Automated Notification Service

If you are an Administrator at one of de.NBI Clouds facilities you can publish a News to the Service via an Application like cURL or Postman.

You can publish a News by posting a JSON-Document at the REST-Interface /savenews. 
The JSON-Document containing the News has to be in a particular format:

```javascript
{"news" : [
	"Title",
	"Author",
	"Text of the News",
	"Tag",
	"FacilityID1,FacilityID2,...",
	"PERUN Log In Token",
	]
}
```

An example cURL call could look like this:
<pre> $ curl -X POST -H "Content-Type: application/json" -d  @.../news.json http://localhost:5000/savenews </pre>

An example news.json could look like this:

```javascript
{"news" : [
	"Update Analyze Service",
	"John Doe",
	"The Update v1.4 was deployed.",
	"Update",
	"123,124",
	"edAf6FK8wIGkBn1u8hE_9zVK4_oOTCeMd8axTpA",
	]
}
```

After publishing a News it will be display at your [web page](http://localhost:5000/savenews)

### Requesting news of the Automated Notification Service with filters

In order to get already published News of the Automated Notification Service you can post a JSON-Document containing filters to the REST-Interface /requestnews via an Application like cURL or Postman.
The Automated Notification Service will return a JSON-Document containing News according to the filters you posted

The JSON-Document containing the filters has to be in a particular format:

```javascript
{
    "id": "",
    "tag": "",
    "author": "",
    "title": "",
    "text": "",
    "older": "",
    "newer": "",
    "facilityid":""
}
```


An example cURL call could look like this:
<pre> $ curl -X POST -H "Content-Type: application/json" -d  @.../filter.json http://localhost:5000/requestnews </pre>

An example filter.json could look like this:

```javascript
{
    "id": "",
    "tag": "Update",
    "author": "John Doe",
    "title": "Analyze Service",
    "text": "Update v1.4",
    "older": "2019-07-21 17:00:00",
    "newer": "2019-07-15 17:00:00",
    "facilityid":"123,124"
}
```
empty filters are going to be ignored during the filtering

### Requesting the MOTD of the Automated Notification Service

In order to request the MOTD, that is the last published News to the Automated Notification Service, you simply need to send a GET Request at /latestnews.
The Automated Notification Service returns already formatted String. Not a JSON-Document.

An example cURL call could look like this:
<pre> curl -s 'http://127.0.0.1:5000/latestnews' </pre>


### Implement the Custom Message of the Day at your Ubuntu/Debian Distribution

The Automated Notification Service contains custom de.NBI MOTD shell-scripts. In order to install them you need to copy the [scripts](https://github.com/prichter327/newsservice/tree/master/motdscripts) into the following directory of your Ubuntu/Debian system:
<pre>/etc/update-motd.d</pre>
You need Root-Permission to perfom this action. Via chmod make sure that the scripts are executable!
In order to display you may need to edit the **IP-ADRESS** and **PORT** inside the script *51-denbi-motd* in line 6:
<pre>curl -s 'http://'IP-ADRESS':'PORT'/latestnews'</pre>
In case you want to keep a slim log-in experience it is recommended to remove the scripts *10-help-text* and *50-motd-news* of the directory.

