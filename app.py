from flask import Flask, render_template, request, redirect
import re
import urllib.parse
import base64

app = Flask(__name__)

def encode_url(url):
    return base64.urlsafe_b64encode(url.encode()).decode()

def auto_hyperlink(text):
    url_regex = r'(https?://[^\s]+)'
    def repl(match):
        url = match.group(0)
        encoded = encode_url(url)
        return f'<a href="https://yourwebsite.com/redirect?url={encoded}" target="_blank">{url}</a>'
    return re.sub(url_regex, repl, text)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        user_input = request.form['input']
        output = auto_hyperlink(user_input)
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)