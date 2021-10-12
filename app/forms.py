from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, SelectField
from wtforms.validators import URL, InputRequired, Length, Regexp, NumberRange

class AddRecord(FlaskForm):
    id_field = HiddenField()
    plexurl = StringField('Plex URL', [ InputRequired(), URL(message='This must be a correct URL')])
    token = StringField('Token', [ InputRequired() ])
    filmslibrary = StringField('Films Library', [ InputRequired() ])
    tvlibrary = StringField('TV Library')
    library3d = StringField('3D Library')
    #plexpath = StringField('Plex Path', [ InputRequired() ])
    #mountedpath = StringField('Mounted Path')
    t1 = StringField('4k Posters Schedule (HH:MM)', [Regexp(r"[0-2][0-9]:[0-5][0-9]", message="Must be entered as HH:MM in 24 hour format")])
    t5 = StringField('3D Posters Schedule (HH:MM)', [Regexp(r"[0-2][0-9]:[0-5][0-9]", message="Must be entered as HH:MM in 24 hour format")])
    t2 = StringField('Disney Collection Schedule (HH:MM)', [Regexp(r"[0-2][0-9]:[0-5][0-9]", message="Must be entered as HH:MM in 24 hour format")])
    t3 = StringField('Pixar Collection Schedule (HH:MM)', [Regexp(r"[0-2][0-9]:[0-5][0-9]", message="Must be entered as HH:MM in 24 hour format")])
    t4 = StringField('Hide 4k Schedule (HH:MM)', [Regexp(r"[0-2][0-9]:[0-5][0-9]", message="Must be entered as HH:MM in 24 hour format")])
    backup = SelectField('Enable Poster Backups ', [InputRequired()], choices=[('0', 'False'), ('1', 'True')])
    restore_from_tmdb = SelectField('Enable restoration of posters from TheMoviedb', [InputRequired()], choices=[('0', 'False'), ('1', 'True')])
    tmdb_api = StringField("Your TMDB API key, set to none if you don't wish to use the TMDb restore feature")
    posters4k = SelectField('Enable the global 4K Poster script ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    films4kposters = SelectField('Enable 4K Posters For Films', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    tv4kposters = SelectField('Enable 4K Posters For TV Shows', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    mini4k = SelectField('Select Mini 4k Posters ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    hdr = SelectField('Enable HDR Banners ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    new_hdr = SelectField('Use the new HDR Banners ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    recreate_hdr = SelectField('Recreate HDR banners to use the Dolby Vision and HDR 10 banners', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    posters3d = SelectField('Enable 3D Poster script ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    mini3d = SelectField('Select Mini 3D posters ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    hide4k = SelectField('Enable hide 4k Script ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    transcode = SelectField('Enable the Transcode option for hide 4k films ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    disney = SelectField('Enable Disney Collection ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    pixar = SelectField('Enable Pixar Collection ', [InputRequired()],   choices=[('0', 'False'), ('1', 'True')])
    submit = SubmitField('Save Changes ')