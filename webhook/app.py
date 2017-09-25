from chalice import Chalice
from collections import defaultdict

app = Chalice(app_name='webhook')


@app.route('/')
def index():
    return {'hello': 'world22'}




bloodGroupDict = defaultdict(int)
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = app.current_request
    result = req.json_body.get("result")

    intentName = result.get("metadata").get("intentName")


    bloodGroup=""
    name=""

    if (intentName == "BloodDonationIntent"):
        parameters = result.get("parameters")
        name = parameters.get("name")
        bloodGroup = parameters.get("bloodGroup")

        current = bloodGroupDict[bloodGroup] + 1
        bloodGroupDict[bloodGroup] = current
        print(name, bloodGroup, current)
        return {'speech': 'Thankyou for the donation. Now we have ' + str(current) + ' bottle(s) of blood group ' + bloodGroup}
    elif(intentName=="InquireBlood"):
        parameters = result.get("parameters")
        bloodGroup = parameters.get("bloodGroup")
        print(bloodGroup)
        current = bloodGroupDict[bloodGroup] 
        print(bloodGroup, current)
        return {'speech': 'Thankyou for the Inquiry. We have ' + str(current) + ' bottle(s) of blood group ' + bloodGroup + ' available in stock'}

    return {"speech": "Unable to understand the request"}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
