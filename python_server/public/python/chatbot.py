"""
Alteração no Kernel.py do import aiml: time.clock -> time.time
"""

import aiml
from datetime import datetime

def chatbot_maria_helena(nome):
    ai = aiml.Kernel()
    ai.learn('voicebot2.xml')

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

chatbot_maria_helena(nome='Murilo')
