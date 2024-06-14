#janela
#título
#campos para selecionaras moedas de origem e destino
#botão pra converter
#lista de exibição com os nomes das moedas 

#importar a biblioteca que vai fazer a janela
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


janela = customtkinter.CTk()
janela.geometry("400x400")
#criar os botoes,textos edemais elementos 
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])

def converter_moeda() : 
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: dolar americano","EUR: euro", "BRL: real brasileiro", "BTC: bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

#colocar os elementos criados na tela
titulo.pack()
texto_moeda_origem.pack()
campo_moeda_origem.pack()
texto_moeda_destino.pack()
campo_moeda_destino.pack()
botao_converter.pack()
lista_moedas.pack()
#rodar a janela

janela.mainloop()