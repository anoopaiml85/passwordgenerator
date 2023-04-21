#flask-restx - for swagger

from flask import Flask,request,jsonify
from services.passwordGeneratorService import Passwordgenerator
from flask_restx import Api,Resource,fields,reqparse
from db.model.credentials import Credentials
from dotenv import load_dotenv
from db.db_connect import session


load_dotenv()
app = Flask(__name__) #create instance

rest_api = Api(app) #create a instance of the api.
#rest_api.init_app(app)
cred_model = rest_api.model('credmodel',{"user_name": fields.String(required=True,min_length=4,max_length=32),
                                         "password":  fields.String(required=False),
                                         "app_name":  fields.String(required=True,min_length=4,max_length=32),
                                         "web_URL":   fields.String(required=True )})
cred_parser=reqparse.RequestParser()
cred_parser.add_argument('length',type = int,help ='Provide the length of the password:')
cred_parser.add_argument('Pattern',type = str,help='Password pattern \n * Do not repeat the characters \n * 1: Upper_case \n 2: lower_case\n3: numbers\n4: special characters;\n * Example: 2 3 4 \nabove example selects Lowercase, numbers and special charactes:')


"""Credentials Save"""
@rest_api.route('/save_credential/')

class Credential(Resource):
  #  @rest_api.expect(cred_model,validate=True)
    @rest_api.expect(cred_parser,cred_model)
    def post(self):
        req_data = request.get_json()
        user_name = req_data.get("user_name")
        password=req_data.get("password")
        app_name = req_data.get("app_name")
        web_URL = req_data.get("web_URL")
        #print (f'password is {password}')

        if(not password):
            args=cred_parser.parse_args() 
            length = args.get("length")
            print(length)
            pattern = args.get("Pattern")
            pattern=list(set([int(i) for i in pattern.split()]))
            print(pattern)
            pg=  Passwordgenerator(length,pattern) 
            newpassword=pg.generate_password()
            print (newpassword)
            cred=Credentials(user_name=user_name,password=newpassword ,app_name=app_name,web_URL=web_URL)
            session.add(cred)
            session.commit()
            session.close()
        return {"user_name":user_name,"password":password,"app_name":app_name,"web_URL":web_URL}
        
# Pass username,appname,URL and password(optional) from the API.
# Take the values and insert the credentials.db
# length,pattern should come in arguments or request params

# check for password none
# if none from the arguments take length and pattern and generate a password. 
# insert into the database
# else insert the supplied values to the database.
# return success.




if __name__ == '__main__':
    app.run(debug=True)