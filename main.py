import requests
from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/projects.html')
def project():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return render_template('projects.html', data_list=data)


# ------------------BLOG-------------------
class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body



posts = requests.get(" https://api.npoint.io/ff4fd23cf354995064f7").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)




@app.route('/index-blog.html')
def get_all_posts():
    return render_template("index-blog.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == '__main__':
    app.run(debug=True)
