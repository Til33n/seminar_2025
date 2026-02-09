import uvicorn
import random
from fastapi import FastAPI
from fastapi.responses import FileResponse
from database_main import show_all, specific_data_lookup, username_lookup
from database_main import show_all_data,show_user_data,show_all_usernames, show_user_matches, show_all_scores_chart, add_data, add_player_score, update_user, update_user_score,update_user_stats, delete_user, update_user_score
from database_main import set_keys, tmp_key_lookup, username_lookup, reset_user_score, output_users, rows, where_tmp_key, where_key, reset_user_keys
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
#from starlette.middleware.cors import CORSMiddleware
app = FastAPI()
random_number = 0

######  GET  #######
@app.get("/")   # MAIN  index  PAGE     
async def root_1():
    return FileResponse('index_2.html', media_type='text/html')



######  POST  #######           
class Item_0(BaseModel):
    user:       str
    password:   str 
@app.post("/test")
def handle_json_0(item: Item_0):
    item = jsonable_encoder(item)
    user =       item["user"]
    password =   item["password"]
    #key = 30
    #tmp_key = 100
    if(username_lookup("database_2", "users", str(user))):
        key = round(random.random() * 10**8)
        tmp_key = round(random.random() * 10**8)
        if(user == specific_data_lookup("database_2", "users","username",1,user)  and  password == specific_data_lookup("database_2","users","username",2,user)):      
            print(key)
            print(tmp_key)
            set_keys("database_2", user, key, tmp_key)
            return {"user" : user, "key" : key, "tmp_key" : tmp_key}    # LOGIN SUCESS
        else:
            print("False")
            return 0  # LOGIN FAILURE
    else:
        print("False")
        return 0    # LOGIN FAILURE



######  GET  #######        +tmp_key
@app.get("/main/{tmp_key}")   #  MAIN USER PAGE
async def root_2(tmp_key: str = ""):
    if(tmp_key_lookup("database_2", "users", str(tmp_key))):
        return FileResponse('main_2.html', media_type='text/html')
    else:
        return FileResponse('index_2.html', media_type='text/html')


######  GET  #######       +tmp_key
@app.get("/scores/{tmp_key}")   #  PLAYERS SCORES    
async def root_3(tmp_key: str = ""):
    print(tmp_key)
    if(tmp_key_lookup("database_2", "users", str(tmp_key))):
        scores = show_all_scores_chart("database_2", "player_scores")
        return scores
    else:
        return 401



#####  POST  #######           
class Item_1(BaseModel):
    user:  str
    key:   str 
@app.post("/get_stats")
def handle_json_1(item: Item_1):
    item = jsonable_encoder(item)
    user =  item["user"]
    key =   item["key"]
    print(user)
    print(key)
    print(type(user))
    if(30 == specific_data_lookup("database_2", "users","username",6, user)):
    #if(key == specific_data_lookup("database_2", "users","username",6, user)):
        print("its working")
        email = specific_data_lookup("database_2", "users","username",3,user)
        score = specific_data_lookup("database_2", "users","username",4,user)
        admin_privileges = specific_data_lookup("database_2", "users","username",5,user)
        #played_rounds = count_number of username scores
        return {"email" : email, "score" : score, "admin_privileges" : admin_privileges} 





######  PUT  #######                        
class Item_2(BaseModel):  
    key:                str
    selection:          str
    updated_email:      str
    updated_password:   str
    current_password:   str

@app.put("/update/{input}")
def handle_json_3(item: Item_2 , input: str =""):
    item = jsonable_encoder(item)
    username =      input
    key =           item["key"]
    selection  =     item["selection"]
    updated_email =         item["updated_email"]
    updated_password = item["updated_password"]
    current_password =   item["current_password"]
    if(username_lookup("database_2", "users", username) and str(key == specific_data_lookup("database_2", "users","username",6, username))):
        if(current_password == specific_data_lookup("database_2","users","username",2,username)):
            if (int(selection) == 1):
                password = specific_data_lookup("database_2","users","username",2,username)
                update_user_stats("database_2", username, password, updated_email)             # change EMAIL 
                # DELETE SESION AND AUTOMATIC LOG OUT
                print("change EMAIL")
                return 204
            elif(int(selection) == 2):
                email = specific_data_lookup("database_2","users","username",3,username)
                update_user_stats("database_2", username, updated_password, email)             # change PASSWORD
                # DELETE SESION AND AUTOMATIC LOG OUT
                print("change PASSWORD")
                return 204
            else:
                update_user_stats("database_2", username, updated_password, updated_email)      # change BOTH
                # DELETE SESION AND AUTOMATIC LOG OUT
                print("change BOTH")
                return 204 
        else:
            print("INCCORECT PASSWORD")
            return  403     # HAS VALID CREDENTIALS BUT PASSWORD INCCORECT
    else:
        print("UNATHORIZED ACCESS")
        return  401     # UNATHORIZED ACCESSS


######  PUT  #######
class Item_3(BaseModel):  
    tmp_key:        str
    
@app.put("/reset/{input}")
def handle_json_3(item: Item_3 , input: str =""):
    item = jsonable_encoder(item)
    username =      input
    tmp_key =       item["tmp_key"]
    if (tmp_key == str(specific_data_lookup("database_2", "users","username",7, username))):
        reset_user_score("database_2", username, 0)                                # resets score of said user in users
        delete_user("database_2", "player_scores", username)                       # deletes all traces of said user in player_scores
        print("score RESET")
        return 204
    




#####################################################   function_5     
#####  POST  #######           
class Item_4(BaseModel):
    user:  str
    tmp_key: str
@app.post("/delete")
def handle_json_1(item: Item_4):
    item = jsonable_encoder(item)
    user =  item["user"]
    tmp_key =   item["tmp_key"]
    if(username_lookup("database_2", "users", user) and str(tmp_key == specific_data_lookup("database_2", "users","username",7, user))):  
        i = rows("database_2")  
        users_list = output_users("database_2", str(1))
        for x in range(1,i+1,1):
            if (x==1): {}
            else:
                users_list = '"' + users_list + '"' + " , " + '"' +  output_users("database_2", str(x)) + '"' 
        array_users = "[" + users_list + "]"
        print(users_list)
        return array_users

######  DELETE  #######                         function_5_1                    
class Item_5(BaseModel):  
    key:                str
    tmp_key:            str  
@app.delete("/delete/{input}")
def handle_json_3(item: Item_5 , input: str =""):
    user_delete = input
    item = jsonable_encoder(item)                   
    key =                item["key"]
    tmp_key =            item["tmp_key"]
    row_id = (where_tmp_key("database_2","users", tmp_key))[0]
    actual_key = str(where_key("database_2", str(row_id)))
    admin = (where_tmp_key("database_2","users", tmp_key))[5]
    user = (where_tmp_key("database_2","users", tmp_key))[1]
    if(key == actual_key):                                                        # souble security authorization
        if(admin):                                                                # check for admin privileges
            if(user_delete != user):                                              # protectiong from admin deleting himself
                delete_user("database_2", "users", user_delete)                  # delete user turned off for testing
                delete_user("database_2", "player_scores", user_delete)          # deletes all traces of said user in player_scores
                print("deleted user " + user_delete)
                return 202
            else:
                 print("unable to delete yourself")
                 return 403
        else:
            print("")
            return 401
    else:
        print("credentials are invalid")
        return 401

######################################################################




#####################################################    function_6     
#####  DELETE  #######      
      
class Item_6(BaseModel):  
    key:                str
    tmp_key:            str  
@app.delete("/log_out/{input}")
def handle_json_3(item: Item_6 , input: str =""):
    username = input                                                                
    item = jsonable_encoder(item)                   
    key =                item["key"]
    tmp_key =            item["tmp_key"]
    row_id = (where_tmp_key("database_2","users", tmp_key))[0]
    actual_key = str(where_key("database_2", str(row_id)))
    #user = (where_tmp_key("database_2","users", tmp_key))[1]                        # current user that is atempting to log_out
    if(key == actual_key):
        reset_user_keys("database_2", username, None, None)                        # log_out disabled for testing 
        # delete key entry with timer in database_t
        print(username + " ---> log_out")
        return 200
    else:
        return 401


##########################################################################################################################








################################################   register procedure
######  POST  #######                       
class Item_7(BaseModel):
    username:    str
    email:       str
    password:    str
    
@app.post("/register")
def handle_json_0(item: Item_7):
    item = jsonable_encoder(item)
    username =     item["username"]
    email    =     item["email"]
    password =     item["password"]


################################################   passsword reset procedure
######  PUT  #######                       
class Item_8(BaseModel):
    username:    str
    email:       str
    password:    str
    
@app.post("/reset")
def handle_json_0(item: Item_8):
    item = jsonable_encoder(item)
    username =     item["username"]
    email    =     item["email"]
    password =     item["password"]
    
    





origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    
)



if __name__ == "__main__":
    uvicorn.run(app, host="192.168.64.18", port=5000)
    app.run(debug = True)
    
 








#### DATABASE STRUCTURES ####

######## database_2 ########
    #### users ####
        #username TEXT PRIMARY KEY,
        #password TEXT,
        #email TEXT,
        #highest_score INT,
        #admin INT,
        #key INT,
        #tmp_key INT

    #### played_rounds ####
        #match_ID text, 
        #username text,
        #score INT,
        #current_time INT,
        #FOREIGN KEY(username) REFERENCES users(username)

    #### player_scores #####
        #username text,
        #highest_score INT


######## database_2_1 ########
    #### sessions ####
        #key INT,
        #tmp_key INT,
        #timer INT
