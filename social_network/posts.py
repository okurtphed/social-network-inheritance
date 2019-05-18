
from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, user = None, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = user

    def set_user(self, a_user):
        self.user = a_user
    
    


class TextPost(Post):
#     def __init__(self, text, timestamp=None):
#         pass

    def __str__(self):
        #return '@{}: "{}"\n\t{}'.format(self.user, self.text,self.timestamp.strftime("%A, %b %d, %Y"))
    
        return f'@{self.user}: "{self.text}"\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        self.text =text
        self.image_url = image_url
        self.timestamp = timestamp
#         super().__init__(self, text)
#         self.image_url = image_url
        

    def __str__(self):
        return f'@{self.user}: "{self.text}"\n\t{self.image_url}\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def __str__(self):
        return f'@{self.user.first_name} Checked In: "{self.text}"\n\t{self.latitude}, {self.longitude}\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'

    
    
#will refactor the code by using super()