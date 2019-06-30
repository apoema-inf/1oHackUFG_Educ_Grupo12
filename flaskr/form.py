from wtforms import Form, StringField, SelectField

class NameSearchForm(Form):
	choices = [('Titulo', 'Titulo'),
			    ('Unidade', 'Unidade'),
				('Codigo', 'Codigo'),
				('Integrantes', 'Integrantes'),
				('Area de Conhecimento', 'Area de Conhecimento')]
	select = SelectField('Procurar projeto', choices=choices)
	search = StringField('')
