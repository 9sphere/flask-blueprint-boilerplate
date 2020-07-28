#### A simple boiler plate code for starting a REST API service using python and Flask

##### First steps

Run the flask service inside a virtual environment. Create one using the below command.

```
# install virualenv
pip install virtualenv

# create a virtual env inside the project directory
python3 -m venv venv

# activate the virtual env
source venv/bin/activate
```

Reference: https://pypi.org/project/virtualenv/

##### Install projects dependencies in requirements.txt file
```
pip install -r requirements.txt 
```

##### To start the service run the start_server.sh 
```
sh start_server.sh
```
The above command will start the server in development mode. 
This should be used only for development. For production use `gunicorn`

---
Load the postman_collection.json file in Postman app to test the APIs.

---
Folder structure.
```
    blueprints <-- keep your APIs here
    venv <-- virtual environment you created
    services.py 
    ..
    ..
    ..
```







