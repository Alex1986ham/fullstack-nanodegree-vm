from app import app

@app.route('/')
@app.route('/catalog')
def catalog():
    return "hello world"
