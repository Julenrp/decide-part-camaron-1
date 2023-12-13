import json

from random import choice

from locust import (
    HttpUser,
    SequentialTaskSet,
    TaskSet,
    task,
    between
)


HOST = "http://localhost:8000"
VOTING = 1


class DefVisualizer(TaskSet):

    @task
    def index(self):
        self.client.get("/visualizer/{0}/".format(VOTING))


class DefVoters(SequentialTaskSet):

    def on_start(self):
        with open('voters.json') as f:
            self.voters = json.loads(f.read())
        self.voter = choice(list(self.voters.items()))

    @task
    def login(self):
        username, pwd = self.voter
        self.token = self.client.post("/authentication/login/", {
            "username": username,
            "password": pwd,
        }).json()

    @task
    def getuser(self):
        self.usr= self.client.post("/authentication/getuser/", self.token).json()
        print( str(self.user))

    @task
    def voting(self):
        headers = {
            'Authorization': 'Token ' + self.token.get('token'),
            'content-type': 'application/json'
        }
        self.client.post("/store/", json.dumps({
            "token": self.token.get('token'),
            "vote": {
                "a": "12",
                "b": "64"
            },
            "voter": self.usr.get('id'),
            "voting": VOTING
        }), headers=headers)


    def on_quit(self):
        self.voter = None
        
class DefAutenticar(SequentialTaskSet):

    def carga(self):
        with open('autenticar.json') as json_file:
            self.data = json.load(json_file)
        self.datos = self.data

    @task
    def autenticar(self):
        for i in range(1,19):
            data = {'username': 'plr{i}', 'email': 'plr{i}@gmail.com', 'password': 'holamundo{i}'}
            response = self.client.post("/authentication/", data)
        try:
            self.token = response.json()
        except ValueError as e:
            print(f"Error decodificando JSON: {e}")
            print(f"Respuesta del servidor: {response.text}")

    def on_quit(self):
        self.datos = None

        

    

class Visualizer(HttpUser):
    host = HOST
    tasks = [DefVisualizer]
    wait_time = between(3,5)

class Autenticar(HttpUser):
    host = HOST
    tasks = [DefAutenticar]
    wait_time = between(3,5)

class Voters(HttpUser):
    host = HOST
    tasks = [DefVoters]
    wait_time= between(3,5)

    
