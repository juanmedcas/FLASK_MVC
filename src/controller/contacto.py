from src import app

@app.route('/contacto')
def contacto():
    return 'Esto es contacto'