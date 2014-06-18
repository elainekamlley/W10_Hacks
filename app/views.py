# -*- coding: utf-8 -*-
#Section 1: Importing tools
from app import app, db
from flask import render_template, redirect
from models import Post, User
from forms import NewPostForm

#Section 2: Views
@app.route('/', methods = ['GET', 'POST'])
def index():
	#form = NewPostForm
	#if form.validate_on_submit():
	#	form.populate_obj(post)
	#	db.session.add(post)
	#	db.session.commit()
	#	return redirect('/')
	users = User.query.all
	#posts = Post.query.all
	return render_template('index.html', users = users)#, posts = posts, form = form)

#Status Update:
	#Have been able to do:
		#Launched the flask app
		#Connect to a database
		#Add users data via a for looping through a csv
	#Stuck:
		#At this point I am just trying to get the users on the index page but I am getting a internal server error. I am able to still print hello, world but at the point of trying to pull from the database it gives me the error. I would like some support in figuring out this bug. 
		#I have yet to do bootstrap or JQuery. I have spent the morning working on the back end first before doing the front end. I feel like I want to get the mechanics down before making it pretty. 