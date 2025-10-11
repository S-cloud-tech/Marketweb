from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    site_name = models.CharField(max_length=10)
    # site_logo = models.ImageField()
    location = models.CharField(max_length=255, default='Port Harcourt, Nigeria')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default='+2348074259720')
    linkedIn_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.site_name
    
    def get_social_links(self):
        return {
            "linkedin_url": self.linkedIn_url,
            "github_url": self.github_url,
            "instagram_url": self.instagram_url,
            "twitter_url": self.twitter_url,
        }


class About(models.Model):
    about_text = models.TextField()

    def __str__(self):
        return self.about_text

class Service(models.Model):
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    star_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    client_image = models.ImageField(upload_to='clients', blank=True, null=True)
    client_name = models.CharField(max_length=50)
    rating_count = models.IntegerField(choices=star_count)
    review = models.TextField()

    def __str__(self):
        return f"{self.client_name} - {self.review}"


