from flask import Flask, request, Markup
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rot">Rotate by:</label>
        <input name="rot" type="text" value="0">
        <textarea name="text" type="text">{0}</textarea>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format("")

@app.route('/', methods=['POST'])
def encrypt():
    form_rot = request.form['rot']
    form_rot = int(form_rot)
    form_text = request.form['text']

    result = rotate_string(form_text, form_rot)
    return form.format(result)

app.run()
