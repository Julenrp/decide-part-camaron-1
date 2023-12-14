import json

from bs4 import BeautifulSoup
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
    
    def on_start(self):
        # Realizar una solicitud GET para obtener el token CSRF y establecer las cookies
        response = self.client.get("/authentication/")
        # Extraer el token CSRF de la respuesta
        self.csrf_token = self.obtener_csrf_token(response)
        # Imprimir el token CSRF para verificar
        print(f"Token CSRF obtenido: {self.csrf_token}")

    def obtener_csrf_token(self, response):
        # Utilizar BeautifulSoup para analizar el contenido HTML de la respuesta
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_input = soup.find("input", {'name': 'csrfmiddlewaretoken'})
        if csrf_input:
            return csrf_input.attrs["value"]
        else:
            print("No se encontró el token CSRF en la respuesta.")
            return None

    @task
    def autenticar(self):
        for i in range(1, 19):
            data = {
                'username': f'plr{i}',
                'email': f'plr{i}@gmail.com',
                'password': f'holamundo{i}',
                "csrfmiddlewaretoken": self.csrf_token,
            }
            response = self.client.post("/authentication/", data)
            try:
                response.raise_for_status()  # Verificar si hay errores HTTP
                self.token = response.json()
            except Exception as e:
                print(f"Error en la solicitud POST: {e}")
                print(f"Respuesta del servidor: {response.text}")

    def on_quit(self):
        self.datos = None

class DefUrlVarias(TaskSet):

    @task
    def index(self):
        self.client.get("/home/")

    @task
    def español(self):
        self.client.get("/esp/")

    @task
    def español(self):
        self.client.get("/census/peticion/")

    

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

class Admin(HttpUser):
    host = HOST
    tasks = [DefUrlVarias]
    wait_time= between(3,5)




    

    
