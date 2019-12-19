# twine22json
Convert a twine 2 story to a json file

## Howto use it

1. Download and install [Python 3](https://www.python.org/downloads/)

2. Download and install [Twine Version 2](http://twinery.org/)

3. Create your story with Twine and test it.

4. Export your story from Twine ("Als Datei veröffentlichen") and save it as "story.html" in the folder of script.py

5. Run "python3 script.py" to convert story.html to story.json

To test the results:

1. Start Python 3 Webserver
	
		python3 -m http.server
		

2. Point Web-Browser to http://localhost:8000/test.html

3. View script output in developer console
