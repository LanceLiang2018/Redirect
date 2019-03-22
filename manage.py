import os
from flask import *

app = Flask(__name__)


@app.route('/<string>', methods=["GET", ])
def index(string):
    return string


if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get('PORT', '5000')), debug=False)

