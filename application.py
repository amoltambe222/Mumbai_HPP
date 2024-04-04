from flask import Flask, request, jsonify,render_template
from  hpp_app import functions
import config
application = Flask(__name__)
import locale
# Set the locale to the desired format
locale.setlocale(locale.LC_ALL, 'en_IN')

################ Root API ########################################
@application.route('/')
def index():
   return render_template('home.html')


################# Location Name API ################################
@application.route('/get_location_names')
def get_location_names():
    locations =  functions.get_location_names()  # list of 247 items(loc)
    return jsonify({"locations":locations})


################## Prediction of House Price ######################
@application.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        user_data = request.form  # Dict
        area = user_data['Area']
        bedrooms = int(user_data['No. of Bedrooms'])
        new = 1 if user_data['New/Resale'] == 'New' else 0
        gym = 1 if user_data['Gymnasium']=='Yes' else 0
        lift = 1 if user_data['Lift Available']=='Yes' else 0
        park = 1 if user_data['Car Parking']=='Yes' else 0
        staff = 1 if user_data['Maintenance Staff']=='Yes' else 0
        security = 1 if user_data['24x7 Security']=='Yes' else 0
        play = 1 if user_data["Children's Play Area"]=='Yes' else 0
        club = 1 if user_data['Clubhouse']=='Yes' else 0
        com = 1 if user_data['Intercom']=='Yes' else 0
        garden = 1 if user_data['Landscaped Gardens']=='Yes' else 0
        games = 1 if user_data['Indoor Games']=='Yes' else 0
        gas = 1 if user_data['Gas Connection']=='Yes' else 0
        track = 1 if user_data['Jogging Track']=='Yes' else 0
        pool = 1 if user_data['Swimming Pool']=='Yes' else 0
        loc = user_data['Location']

        prediction = functions.get_predicted_price(loc,area,bedrooms,new,gym,lift,park,staff,security,play,club,com,garden,games,gas,track,pool)
        # Format the house price with commas and currency symbol
        formatted_price = locale.currency(prediction, grouping=True, symbol=True)
        return render_template('result.html', prediction_text = f"The Predicted house price is {formatted_price}")

    return jsonify({"Message":"Method is wrong"})

if __name__ == "__main__":
    print("House Price Prediction ")
    application.run(host='0.0.0.0', port=config.HPP_PORT_NO,debug=True)