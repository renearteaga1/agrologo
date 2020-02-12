from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_img_path(instance, filename):
    new_filename = random.randint(1, 3920540249)
    print(f'{instance.user.id} es el codigo de user')
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "profile_img/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=upload_img_path)

    def __str__(self):
        return f'{self.user.first_name} Profile'
