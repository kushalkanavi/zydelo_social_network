from django.db import models
from neomodel import StructuredNode, StringProperty, DateTimeFormatProperty, UniqueIdProperty, RelationshipTo

class Post(StructuredNode):
    title = StringProperty(unique_index=True, required=True)
    Description = StringProperty(index=True, default="city")
    Image = StringProperty(index=True, default="sample_1.jpg")
    created_at = DateTimeFormatProperty(default_now=True, format="%Y-%m-%d %H:%M:%S")

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    Passwoed = StringProperty(unique_index=True)

    # Relations :
    user_post = RelationshipTo(Post, 'User_post')
    follows = RelationshipTo('User','Follow')


