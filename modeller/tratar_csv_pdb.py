import pandas as pd
# gera o dataframe separado por " "
dados = pd.read_csv("C:/Users/Acer/Documents/Progamacao/bot_pyautogui/build_profile.csv", sep='\s+')
# renomeia o dataframe
dados.columns = ("indice","id",'3', '4', "amino_1", '5', 'amino_2', '7', '8', '9', 'identidade', "evalue", "sequencia")
# organiza por evaule = 0.0
evalue0 = dados.query('evalue==0.0')
# organiza por identidade > 40.0 (faz sumir com referencia)
identidade40 = evalue0.query('identidade>40.0')
print (identidade40)
# reset de indice. Ultimo passo para organizar o dataframe
identidade40 = identidade40.reset_index()
#print (identidade40)

# seleciona id_pbd a partir da coluna id em ordem do indice
#print(identidade40['id'][4])

# restringe a linha em que tem aquele valor (no caso o id_pbd)
# linhaInterese = identidade40.loc[identidade40['id']=='4j2kA']
#print(linhaInterese)

print(len(identidade40))

#  gerar arquivo do tratamento de dados
#identidade40.to_csv(r'C:/Users/Acer/Documents/Progamacao\bot_pyautogui/identidade402.csv', index = False)
