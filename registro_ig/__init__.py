#aquí es dónde vamos a crear la app
from flask import Flask

app = Flask(__name__) 

from registro_ig.routes import *