# Uruchamiamy komendą:
# flask run --debug
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return "Hello, world!"


@app.route('/template/')
def hello_template():
    return render_template('hello.html')


@app.route('/hello/<string:name>/')
def hello_name(name):
    # return f"Hello, {name}!"  # podatność xss
    return render_template(
        'hello_name.html',
        name=name,
    )


# Formularz GET
@app.route('/form_get/')
def hello_form_get():

    # dane metody GET siedzą w atrybucie args obiektu request
    data = request.args
    name = data.get('name')

    if name:
        return render_template(
            'hello_name.html',
            name=name
        )

    return render_template(
        'hello_form.html'
    )


# Formularz POST
@app.route('/form_post/', methods=["GET", "POST"])
def hello_form_post():

    if request.method == "GET":
        return render_template(
            'hello_form_post.html'
        )

    elif request.method == 'POST':
        # dane metody POST siedzą w atrbucie form obiektu request
        data = request.form
        name = data.get('name')

        if name:
            return render_template(
                'hello_name.html',
                name=name,
            )
