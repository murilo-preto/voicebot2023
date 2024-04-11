"""
Alteração no Kernel.py do import aiml: time.clock -> time.time
"""

import aiml
from timeit import default_timer as timer
from datetime import timedelta

ai = aiml.Kernel() # inicialização
ai.learn('voicebot2.xml') # lê o arquivo principal da AIML e faz referências aos outros

start = timer()

nome = "Roberto"

response = ai.respond(f"ROBOTSTART {nome}")
print(timedelta(seconds=timer()-start),"Maria Helena:",response)

said = ""

while said != "Até logo":  
    try:
        said = input("Digite: ")
        print(timedelta(seconds=timer()-start), "Usuário:",said)
        response = ai.respond(said)     
        
    except:
        response = "Desculpe, mas não consegui captar o que o que você disse..."
    
    print(timedelta(seconds=timer()-start)," Maria Helena:",response)