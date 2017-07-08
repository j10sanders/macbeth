#Zinc's Assignment


### Running the Program:

From the root directory of the project, run `python mac.py run`.  This project has been tested on Python 2.7 - 3.6.

### Running Tests:

From the root directory of the project (feel free to fire up a virtualenv), run: `pip install -r requirements.txt` in your shell.  This will install: [pytest](http://doc.pytest.org/en/latest/).

Then run `py.test`.  This will display test results in your shell.  You can find the tests in `mac_test.py`

### Decisions and trade-offs:

I thought there was a case to be made for a class based approach, but in an app this simple, I think it's best to keep things simple.  The code I use here is essentially identical to the code I use in the [webapp](https://github.com/j10sanders/macwebapp/blob/master/mac/macbeth.py).

[You can run the single-page webapp here.](https://zinc-shakespear.herokuapp.com/)  It may take a bit to start up, since I'm not paying heroku for hosting.  
I did not focus on styling very much -- I opted to get this up and running in a hurry, since I'll be leaving for a funeral on Monday.  

I also opted to use Python with Flask instead of Ruby with Rails, since I'm currently just a quicker programmer with Python.  But it's similar enough to Ruby that transitioning won't be difficult.

This was a fun little project - I'm looking forward to discussing with you.


