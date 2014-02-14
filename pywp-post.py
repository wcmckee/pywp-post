from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
import random

wp = Client('http://blog.brobeur.com/xmlrpc.php', 'jess', 'qwerty123')

def post(titl, content):
     post = WordPressPost()
     post.title = (titl)
     post.post_status = ('publish')
     wp.call(NewPost(post))
