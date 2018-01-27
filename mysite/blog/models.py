from django.db import models
from django.utils import timezone

# `class` is a special keyword indicated that we're defining an object.
# `Post` is the name of our model. This can be any string, but no special characters or spaces are allowed.
# `models.Model` means that `Post` is a Django model, and helps Django to know that we're saving this in our database
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        # 'ForeignKey' indicates that `Posts` are linked to another model. In this case, it's a `User`.

    title = models.CharField(max_length=200)
        # `CharField` is a text field with a defined character limit.

    text = models.TextField()
        # `TextField` is a text field with no character limit.

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
        # `DateTimeField` is pretty self-explanatory. `timezone.now` tells our database that we want to use the exact current date and time

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Dunder Mifflin
    def __str__(self):
        return self.title
