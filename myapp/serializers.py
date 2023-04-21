import shutil # Importing shutil module to perform operations related to file and directory handling
from numpy import require 
from rest_framework import serializers # Importing rest_framework serializers to serialize and deserialize Django model instances
from .models import *  # Importing all the models from models.py of the current app


class FileSerializer(serializers.ModelSerializer):
    # Serializer for File model
    class Meta:
        model = Files  # Specifying the model for the serializer
        fields = '__all__' # Specifying all the fields to be serialized

class FileListSerializer(serializers.Serializer):
    # Serializer for list of files
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
          # Specifying the field for list of files where each file should be a FileField and have max_length of 100000 bytes
          # The allow_empty_file attribute is set to False so that an empty file cannot be uploaded
          # use_url attribute is set to False so that the file URL is not returned in the response
    )
    folder = serializers.CharField(required = False)  # Optional field for folder name
    
    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,f'public/static/{folder}' )

    def create(self , validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder = folder , file = file)
            files_objs.append(files_obj)

        
        self.zip_files(folder.uid)


        return {'files' : {} , 'folder' : str(folder.uid)}