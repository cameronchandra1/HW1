## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
# Resources:
# flask.pocoo.org => Flask website
# https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#searching => Itunes API documentation
# http://docs.python-requests.org/en/master/api/ => requests documentation
# https://darksky.net/dev/docs => darksky API documentation


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask,request	
import requests 
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_to_you():
    return 'Hello!'

# http://localhost:5000/class returns a page that says "Welcome to SI 364"    
@app.route('/class')
def class_page(): 
	return 'Welcome to SI 364!'

# localhost:5000/movie/<movie_name> returns data regarding the inputted movie
@app.route('/movie/<movie_name>')
def show_movie_info(movie_name):
	r = requests.request("GET","https://itunes.apple.com/search?term={}&entity=movie".format(movie_name))
	return(r.text)

# localhost:5000/question displays a page with a form asking for the user's favorite number
@app.route('/question')
def see_form():
	formstring = """<br>
	    <form action="/result" method='GET'>
		What's your favorite number? : <input type="text" name="phrase"> <br>
		<br><input type="submit" value="Submit">"""
	return formstring

# After submitting a number into the form, users are directed to localhost:5000/result?phrase=<favorite_number> (data is shown in URL because it is a GET request). The users number is doubled and displayed.
@app.route('/result', methods= ['GET'])
def show_number():
	if request.method == 'GET':
		number = request.args.get('phrase','')
		double_number = int(number)*2
		return "Double your favorite number is {}".format(double_number)

# localhost:5000/problem4form displays a page with a form asking for the coordinates and language of the desired forecast
@app.route('/problem4form')
def see_form_2():
	formstring = """ <br>
		<form action= "/problem4formresults" method="GET">
		Enter your location's latitude: <input type='text' name= 'lat'> 
		<br>
		Enter your location's longitude: <input type='text' name= 'long'>
		<br>
		Choose a language (select one):
		<br>
		<input type="checkbox" name="English" value="en"> English<br>
  		<input type="checkbox" name="Spanish" value="es"> Spanish<br>
  		<input type="checkbox" name="French" value="fr"> French
 		<input type="submit" value="Submit">
 		</form>"""
	return formstring

# After completing the form, users are directed to localhost:5000/problem4results?<latitude>&<longitude>&<language> and displays forecast information from DarkSKy API
@app.route('/problem4formresults')
def show_forecast():
	key = '03e583150f31cf38f650dba27e3c3dab'
	latitude = request.args.get('lat','')
	longitude = request.args.get('long','')
	url = 'https://api.darksky.net/forecast/{}/{},{}?exlude=minutely,hourly,daily,alerts,flags'.format(key,latitude,longitude)
	forecast = requests.request('GET',url)
	forecast_info = json.loads(forecast.text)
	forecast_summary = forecast_info['currently']['summary']
	precip_prob = forecast_info['currently']['precipProbability']
	temperature = forecast_info['currently']['temperature']
	return "Forecast of location, coordinates ({},{})<br>Forecast Summary: {}<br> Probaility of Precipitation: {}<br>Temperature: {}".format(latitude,longitude,forecast_summary,precip_prob,temperature)


if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
