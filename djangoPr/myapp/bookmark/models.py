from django.db import models

# Create your models here.

# title이라는 필드를 만들고 형식은 CharField이며 최대 100까지 허용하며 blank를 허용한다. 현재 필드 두개
# unique는 primary key가 된다. 
class Bookmark(models.Model):
  title=models.CharField(max_length=100,blank=True, null=True)
  url = models.URLField('url', unique=True)


#
def __str__(self):
  return self.title
