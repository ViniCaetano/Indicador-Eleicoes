import requests
import json
import pandas  as pd 
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        if t == 0:
            t=60
            data = requests.get( 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
            json_data = json.loads(data.content)

            candidato = []
            partido = []
            votos =[]
            porcentagem =[]
            apuração = []
            for informacoes in json_data['cand']:
                if informacoes['seq'] == '1' or informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4':
                    candidato.append(informacoes['nm'])
                    votos.append(informacoes['vap'])
                    porcentagem.append(informacoes['pvap'])


            df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns = ['Candidato', 'Nº Votos', 'Porcentagem'])

            print(df_eleicao)
            print(json_data['pst'])
t = 1

countdown(t)
