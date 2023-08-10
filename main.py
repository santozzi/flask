from flask import Flask, redirect, request, make_response,render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')

    valores = ["valor1","valor2"]
    return render_template('hello.html', valores=valores)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)