from flask import Flask, redirect, render_template, request, url_for


app = Flask('blog')


# @app.route('/')
# def hello_world():
    # return 'Hello My First App in Flask'




@app.route('/')
def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/posts/<id_>')
def post_detail(id_):
    post = get_post_by_id(id_)
    return render_template('post_detail.html', post=post)

@app.route('/add-post', methods=('GET', 'POST'))
def add_post():
    if request.method == 'POST':
        form = request.form
        post = save_post_to_file(form['title'], content=form['content'], author=form['author'])
        return redirect(url_for('post_detail', id_=post.id))
    return render_template('add_post.html')

@app.route('/delete-post/<id_>', methods=('GET', 'POST'))
def delete_post(id_):
    post = get_post_by_id(id_)
    if request.method == 'POST':
        delete_post_by_id(post.id)
        return redirect(url_for('index'))
    return render_template('delete_post.html', post=post)




