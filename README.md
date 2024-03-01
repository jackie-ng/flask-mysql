## Creating RESTful Web APIs using Flask and Python

Virtual Environment

```cmd
python -m vnev .venv
.venv/Scripts/activate.bat
```

```cmd
pip install Flask
flask run

or

python app.py
```

app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
```

### Variable Rules

You can add variable sections to a URL by using <variable_name>. The function receives the variable as a keyword argument.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

app.run()
```

### Accessing Request Data

To access the request data, use the following

```python
from flask import request
```

You can use the following attributes to fetch the data sent with the request:

```
request.data → Access incoming request data as a string
request.args → Access the parsed URL parameters. Returns ImmutableMultiDict
request.form → Access the form parameters. Return ImmutableMultiDict
request.values → Returns CombinedMultiDict that combines args and form
request.json → Returns parsed JSON data if mimetype is application/json
request.files → Returns MultiDict object which contains all uploaded files. Each key is the name of the file and the value is the FileStorage object.
request.authorization → Returns an object of Authorization class. It represents an Authorization header sent by the client.
```
