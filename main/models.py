from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banner_images/')
    bio = models.CharField(max_length=25)
    contact_logo = models.ImageField(upload_to='logos/')
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)


    def __str__(self):
        return self.full_name


class Service_Section_Info(models.Model):
    text = models.CharField(max_length=255)


class Service(models.Model):
    logo = models.ImageField(upload_to='service_logos/')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class About_Us(models.Model):
    logo = models.ImageField(upload_to='service_logos/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class About_Us_Info(models.Model):
    video = models.URLField()
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Our_result(models.Model):
    logo = models.ImageField(upload_to='service_logos/')
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    comment = models.CharField(max_length=255)
    client_photo = models.ImageField(upload_to='cliets/')
    client_name = models.CharField(max_length=255)
    client_job = models.CharField(max_length=25)


class Partner_Brand(models.Model):
    logo = models.ImageField(upload_to='brands_logo/')



class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    instagram = models.CharField(max_length=25)
    facebook = models.CharField(max_length=25)
    twitter = models.CharField(max_length=25)






