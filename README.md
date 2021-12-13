# Super Admin

## Install
Create virtualenv for this project and activate it. 

Then clone the repo and install requirements.

```shell
git clone git@github.com:margloG/super_admin.git
cd super_admin
pip install -r requirements.txt
```

### local_settings.py
Create this file beside settings.py file (under super_admin directory)

With the following content:
```python
DEBUG = True
```

That's it.

Now you could start the server and access the site [admin](http://127.0.0.1:8000/admin/) panel.

