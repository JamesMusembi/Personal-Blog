
from flask import render_template,request,redirect,url_for, flash
from sqlalchemy import delete
from ..requests import get_blogs
from . import main
from .. import db, login_manager
from ..models import Blog, User,Comment
from flask_login import  current_user ,login_required
from ..email import mail_message

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def make_blogs(blogs):

  new_blogs = []
  for blog in blogs:
    user = User.query.filter_by(id=blog.user_id).first()
   
    comments = Comment.query.filter_by(blog_id=blog.id).all()
    addblog.append({
      'id': blog.id,
      'title': blog.title,
      'author': blog.author,
      'content': blog.content,
      
      'user': user,
      'upvotes': blog.upvotes,
      'downvotes': blog.downvotes,
      'comments': len(comments)
    })
  return new_blogs

@main.route('/')
def index():
    quotes = get_blogs()
    
    blogs=Blog.query.order_by(Blog.created_at.desc()).all()
    
    return render_template ("pages/index.html",blogs=blogs,quote1=quotes[0],quote2=quotes[2])

@main.route('/blogs/add', methods=['GET','POST'])
@login_required
def addblog():
  if request.method=='POST':
    title=request.form['title']
    author=request.form['author']
    content=request.form['editor1']
    blog=Blog(title=title,author=author,content=content,user_id=current_user.id)

    db.session.add(blog)
    db.session.commit()
    flash('blog created successfully',"success")
    users=User.query.all()
    for user in users:

      # mail_message("Welcome to blogs app","email/welcome_user",user.email,user=user)
      # print("Email message,..,.,",mail_message)
      return redirect(url_for('main.index'))
  return render_template ('pages/blogs/addblog.html')

@main.route('/blogs/delete/<int:blog_id>')
def delete_blog(blog_id):
  blog_deleted=Blog.query.get(int(blog_id))
  blog_deleted.delete()
  return render_template('pages/index.html',blog_id=blog_id)
  # try:
  #   db.session.delete(blog_deleted)
  #   db.session.commit()
  #   flash('deleted successfully ')
  #   blogs=Blog.query.all()
  #   return render_template('pages/index.html',blogs=blogs)
  # except:
  #   flash('whoops!there was an error')
  #   blogs=Blog.query.all()
  #   return render_template('pages/blogs/view.html',blogs=blogs)

@main.route('/blogs/view/<int:blog_id>', methods=['GET','POST'])
def view_blog(blog_id):
  blog=Blog.query.get(int(blog_id))
  quotes = get_blogs()
  if blog:
    comments = Comment.query.filter_by(blog_id=blog.id).all()
    new_comments = []
    for comment in comments:
      user = User.query.filter_by(id=comment.user_id).first()
      new_comments.append({
        'id': comment.id,
        'content': comment.content,
        'user': user,
        'created_at': comment.created_at
      })
  
  blogs=Blog.query.all()
  return render_template('pages/blogs/view.html',comments=new_comments,blog=blog,quote1=quotes[0],quote2=quotes[2],blogs=blogs,quote3=quotes[3],quote4=quotes[4])


@main.route('/comments/add/<string:blog_id>',methods=['GET','POST'])
def comment_view(blog_id):
  blog = Blog.query.filter_by(id=blog_id).first()
  if request.method == 'POST':
    content = request.form['comment']
    
    if blog:
      comment = Comment(blog_id=blog.id, user_id=current_user.id, content=content)
      db.session.add(comment)
      db.session.commit()
      
      flash('Comment added', 'success')
      return redirect(url_for('main.view_blog', blog_id=blog_id))
    else:
      flash('blog not found', 'warning')
      return redirect(url_for('main.index'))
  
  

