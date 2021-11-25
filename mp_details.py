from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/endpoint',methods=['GET'])
def endpoint():
    
    pincode = request.args.get('postcode')
    url1 = "https://members-api.parliament.uk/api/Location/Constituency/Search"
    PARAMS = {'searchText': pincode}

    r1 = requests.get(url=url1, params=PARAMS)
    data = r1.json()
    
    result1 = data['items'][0]['value']['currentRepresentation']['member']['links'][3]['href']

    Name = data['items'][0]['value']['currentRepresentation']['member']['value']['nameDisplayAs']
    Constituency = data['items'][0]['value']['name']

    url2 = "https://members-api.parliament.uk/api"
    url3 = url2+result1

    r2 = requests.get(url3)
    data1 = r2.json()

    Email = data1['value'][0]['email']
    

    return ("The MP details for the given Postcode are:\n\nName : %s\nConstituency : %s\nEmail : %s\n"%
          (Name, Constituency, Email))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2476)
