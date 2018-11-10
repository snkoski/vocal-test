import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is working'

# if __name__ == '__main__':
#     app.debug = True
#     host = os.environ.get('IP', '0.0.0.0')
#     port = int(os.environ.get('PORT', 8080))
#     app.run(host=host, port=port)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
