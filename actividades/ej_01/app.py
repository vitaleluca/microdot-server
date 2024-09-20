# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

from microdot import send_file

@app.get('/')
async def index(request):
    return send_file('/index.html')

app.run(port = 80)