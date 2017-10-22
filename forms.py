from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
#import flask.ext.wtf.html5.URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()]) #Actual Fields WTForms will use these attributes to generate fields instances
    description = StringField('description')

    def validate (self):
        if not (self.url.data.startswith("http://") or\
                self.url.data.startswith("https://")):
            self.url.data = "http://" + self.url.data

        if not Form.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        return True