from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional


# test
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BunchOfKeysForm(FlaskForm):
    text_input = StringField("Your text", validators=[DataRequired()], render_kw={
        "placeholder": "your text",
        "class": "input-text",
        "autocomplete": "off",
        "onkeyup": "countLetters();",
        "maxlength": "16",
        "type": "text"
    })

    key_input = StringField("Your key", validators=[Optional()], render_kw={
        "placeholder": "your key",
        "class": "input-key input-text",
        "autocomplete": "off",
        "onkeyup": "countDigits();",
        "maxlength": "6",
        "type": "text"
    })

    generate_btn = SubmitField("Build")


__all__ = ["NameForm", "BunchOfKeysForm"]
