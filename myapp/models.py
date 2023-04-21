from pyexpat import model
from statistics import mode
from uuid import uuid4
from django.db import models
import uuid
import os

#create model for folder
class Folder(models.Model):
    #uuid for primary key unique identification
    uid = models.UUIDField(primary_key= True , editable= False , default=uuid.uuid4)
    #auto_now auto matically set date
    created_at = models.DateField(auto_now= True)
 

def get_upload_path(instance , filename):
    #folder's uuid with the filename for a unique path
    return os.path.join(str(instance.folder.uid) , filename)


class Files(models.Model):
    #foreignkey for connect the specific folder
    folder = models.ForeignKey(Folder , on_delete=models.CASCADE)
    #filefield to upload files to the server
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now= True)