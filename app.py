from flask import Flask, render_template,jsonify, Response
from time import sleep


app = Flask(__name__,static_url_path='/static')
app.debug = True
@app.route('/')
def index():
    return render_template('index.html')

from flask import Response

@app.route('/progress')
def progress():
    def generate_progress():
        status = 0
        while status <= 100:
            status += 1
            yield 'data: {"progress": ' + str(status) + '}\n\n'
            sleep(.1)

    return Response(generate_progress(), mimetype='text/event-stream')


if __name__ == '__main__':
  app.run()





