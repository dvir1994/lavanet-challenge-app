from app import app
from flask import render_template
import requests

isbndb_base_url_prefix='https://openlibrary.org/api/books?bibkeys=ISBN:'
isbndb_base_url_suffix='&jscmd=data&format=json'

@app.route('/')
def home():
    return render_template('home.html', identifier=app.config["BACKEND_IDENTIFIER"])

@app.route('/book/<isbn>')
def isbn_query(isbn):
    try:
        response = requests.get(isbndb_base_url_prefix+isbn+isbndb_base_url_suffix)
        if len(response.json()):
            return response.json()
        else:
            return 'ISBN not found.'
    except Exception as e:
        return str(e)

@app.route('/cover_image/<isbn>')
def cover_image(isbn):
    try:
        response = requests.get(isbndb_base_url_prefix+isbn+isbndb_base_url_suffix)
        if len(response.json()):
            cover_image = response.json()['ISBN:'+isbn]['cover']['medium']
            return render_template('cover_image.html', cover=cover_image, json=response.json())
        else:
            return 'ISBN not found.'
    except Exception as e:
        return str(e)
