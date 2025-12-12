from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('Main_page.html')

@app.route('/about')
def About():
    return render_template('About.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')

# НОВЫЙ МАРШРУТ для страницы скачивания
@app.route('/download')
def Download():
    return render_template('Download.html')

if __name__ == '__main__':
    app.run(debug=True)