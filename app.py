from flask import Flask, render_template, request, flash
from sql_queries import BlogDB
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jdkkfgnbdnbjkd' 
db = BlogDB("Shop.db")
PATH = os.path.dirname(__file__) + os.sep

@app.route("/")
def index():
    categories = db.get_all_categories()
    posts = db.get_all_posts()
    print(posts)
    return render_template("index.html",
                            title = "Сайт про види ноутбуків",
                            posts = posts,
                            categories = categories)

@app.route("/category/<category_id>")
def posts_by_category(category_id):
    categories = db.get_all_categories()
    posts = db.get_posts_by_category(int(category_id))
    return render_template("category.html", categories = categories, posts = posts)


@app.route("/post/<post_id>")
def post(post_id):
    categories = db.get_all_categories()
    post = db.get_posts(int(post_id))
    return render_template("post.html", categories = categories, post = post)


@app.route("/newpost", methods = ["POST", "GET"])
def newpost():
    categories = db.get_all_categories()
    if request.method == "POST":
        try:
            image = request.files['image']
            image.save(PATH + 'static/img/' + image.filename)
            db.create_post(request.form['title'], request.form['text'], request.form['category'], image.filename)
            flash("Пост додано.", "alert alert-success")
        except:
            flash("Помилка додавання поста. Спробуйте ще раз.", "alert alert-danger")
    return render_template("add_post.html", categories = categories)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)