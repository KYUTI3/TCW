from flask_assets import Environment, Bundle
from app import app
import os

assets = Environment(app)
assets.register("css", css)

js = Bundle("src/*.js", output="dist/main.js")
css = Bundle("src/main.css", output="dist/main.css")
css.build()
js.build()

if __name__ == "__main__":
    
    # os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    # app.run(debug="True", ssl_context='adhoc')
    app.run(debug="True",use_reloader=True, ssl_context=('cert.pem', 'key.pem'))