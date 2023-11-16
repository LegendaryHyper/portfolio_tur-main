# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)
@app.route('/', methods=['POST'])
def discord_button():
    button_discord = request.form.get('button_discord')
    return redirect("https://discord.gg/DxWsHRW9")


if __name__ == "__main__":
    app.run(debug=True)
