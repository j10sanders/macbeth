#Zinc's Assignment


### Running the Program:

From the root directory of the project (feel free to fire up a virtualenv), run: `pip install -r requirements.txt` in your shell.  This will install: [pytest](http://doc.pytest.org/en/latest/) and [requests](http://docs.python-requests.org/en/master/).

From the root directory of the project, run `python shake.py run`.  This project has been tested on Python 3.5 - 3.6.

### Running Tests:

Simply run `py.test`.  Test results will display test results in your shell.  You can find the tests in `shake_test.py`

### Design Decisions:

The code I use here is essentially identical to the code I use in the webapp, although I do the error handling outside the file, in the app's [views.py](https://github.com/j10sanders/macwebapp/blob/master/mac/views.py).

[You can run the single-page webapp here.](https://zinc-shakespeare.herokuapp.com/)  It may take a bit to start up, since I'm not paying heroku for hosting.  


I opted to use Python with Flask instead of Ruby with Rails, since I'm currently just a quicker programmer with Python.  But it's similar enough to Ruby that transitioning to Zinc's stack shouldn't be difficult.

It was a fun little project - I'm looking forward to discussing with you!


