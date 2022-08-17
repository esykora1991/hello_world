from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def hello_world(): 
    user_name = request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME')
        
    return f'Hello world: {user_name}. This is the app as of Aug 17.'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
