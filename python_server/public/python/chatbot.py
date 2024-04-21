"""
Alteração no Kernel.py do import aiml: time.clock -> time.time
"""

import aiml
from datetime import datetime

path_xml = r'C:\Users\user\Documents\GitHub\voicebot2023\python_server\public\python\voicebot2.xml'

def chatbot_maria_helena(nome):
    ai = aiml.Kernel()
    ai.learn(path_xml)

    start_time = datetime.now()

    entrada = f"ROBOTSTART {str(nome)}"
    response = ai.respond(entrada)
    print("Tempo decorrido:", datetime.now() - start_time)
    print("Maria Helena:", response)

    while entrada != "Até logo" and not response.startswith("SYSTEM"):
        try:
            entrada = input("Digite: ")
            print("Usuário:", entrada)

            response = ai.respond(entrada)

            print("Tempo decorrido:", datetime.now() - start_time)
            print("Maria Helena:", response)

        except Exception as e:
            print("Desculpe, ocorreu um erro:", str(e))

chatbots = {}
def initialize_chatbot(token):
    ai = aiml.Kernel()
    ai.learn(path_xml)
    chatbots[token] = ai

def chatbot(token, username, input_text):
    ai = chatbots.get(token)
    response = None
    if ai is None:
        print(f'Iniciando voicebot para {username}:{token}')
        initialize_chatbot(token)
        ai = chatbots[token]

        entrada = f"ROBOTSTART {str(username)}"
        response = ai.respond(entrada)
    else:
        print(f'Continuando voicebot para {username}:{token}')
        ai = chatbots[token]
        try:
            response = ai.respond(input_text)
        except Exception as e:
            print(e)
            return "Desculpe, ocorreu um erro"

    return response
