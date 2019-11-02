from flask import Flask, render_template

import datetime
 
app = Flask(__name__)

# FIXME: Somente para modo desenvolvedor
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def page_data(title, styles=None, scripts=None, **kwargs):
  # Styling handle
  default_styles = ['css/main.css']
  if isinstance(styles, str):
    styles = [f'css/{styles}.css']
  elif isinstance(styles, list):
    styles = [f'css/{style}.css' for style in styles]
  else:
    styles = []
  
  # Scripts handle
  default_scripts = ['js/main.js']
  if isinstance(scripts, str):
    scripts = [f'js/{scripts}.js']
  elif isinstance(scripts, list):
    scripts = [f'js/{script}.js' for script in scripts]
  else:
    scripts = []
  
  data = {
    'title': title,
    'styles': default_styles + styles,
    'scripts': default_scripts + scripts,
    'footer_year': datetime.datetime.now().year
  }
  data.update(kwargs)
  return data

 
@app.route('/')
def home():
  data = page_data(
    title='Entrar', styles='credentials', scripts='credentials'
  )
  return render_template('login.html', **data)

@app.route('/signup')
def signup():
  data = page_data(
    title='Cadastro', styles='credentials', scripts='credentials',
    today_date=datetime.datetime.now().strftime('%Y-%m-%d')
  )
  return render_template('signup.html', **data)

@app.route('/dashboard/profile')
def profile():
  data = page_data(
    title='Início',
  )
  return render_template('profile.html', **data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8081, debug=True)