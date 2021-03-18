from src import app

@app.route('/productos')
def productos():
    return 'Esto es productos'