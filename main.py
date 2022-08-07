import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfe5e34e0c536b6dea0b9be786c141e8f"
# Your Auth Token from twilio.com/console
auth_token  = "dd2386e19035936139976ee8a4cde6ea"

client = Client(account_sid, auth_token)



lista_meses= ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas= pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta.Vendedor: {vendedor}, Vendas:{vendas}")
        message = client.messages.create(
            to="+393471219896",
            from_="+15077365770",
            body=f"No mês {mes} alguém bateu a meta.Vendedor: {vendedor}, Vendas:{vendas}")
        print(message.sid)


