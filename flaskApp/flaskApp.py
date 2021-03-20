from flask import Flask, render_template , json

app = Flask(__name__, static_folder='./static', template_folder='./templates')


@app.route("/")
def home():
    with open('../all_books.json', 'r', encoding='utf-8') as file:
        data = json.load(file)


    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)