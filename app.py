from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This route serves the homepage and returns index.html
    return render_template('index.html')

@app.route('/about')
def about():
    # This route serves the about page and returns about.html
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
