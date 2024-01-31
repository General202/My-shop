from flask import Flask, render_template

from sql_queries import BlogDB

app = Flask(__name__)

db = BlogDB("shop.db")

@app.route("/")
def index():
    categories = db.get_all_categories()
    posts = db.get_all_posts()
    print(posts)
    return render_template("index.html",
                            title = "Сайт про види ноутбуків",
                            posts = posts,
                            categories = categories)

@app.route("/logika")
def hello_logika():
    return render_template("logika.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)