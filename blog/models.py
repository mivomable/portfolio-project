from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+"..."

    def shorttime(self):
        return self.pub_date.strftime("%b %e %Y")
# Create a blog model
#       title, pub date, body, image

# add the blog app to the settings
# create a migration
# do a migrate
# add to the admin