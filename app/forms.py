from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES
from wtforms import validators

images = UploadSet('images',IMAGES)

class UploadForm(FlaskForm):
	image = FileField('Image',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])