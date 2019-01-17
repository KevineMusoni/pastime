from django.db import models

# Create your models here.
# adding sport details

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location):
        location = cls.objects.get(pk=id)
        location = cls(location=location)
        location.save()

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Categories'

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_category(cls,id,category):
        category = cls.objects.get(pk=id)
        category = cls(category=category)
        category.save()
      
class Sport(models.Model):
    sport_name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to = 'articles/')

    def __str__(self):
        return self.sport_name
    class Meta:
        ordering = ['sport_name']

    def save_sport(self):
        self.save()

    def delete_sport(self):
        self.delete()

    @classmethod
    def update_sport(cls,id,name,description,location,category):
        sport = cls.objects.get(pk=id)
        sport = cls(name=name,description=description,location=location,category=category)
        sport.save()

    @classmethod
    def get_sport_by_id(cls, id):
        sport = cls.objects.get(pk=id)
        return sport

    @classmethod
    def filter_by_location(cls, location):
        sports = cls.objects.filter(location=location)
        return sports
    @classmethod
    def all_sports(cls):
        sports = cls.objects.all()
        return sports
# search sport 
    @classmethod
    def search_by_category(cls,search_term):
        sports = cls.objects.filter(category__category=search_term)
        return sports
