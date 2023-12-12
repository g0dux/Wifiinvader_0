import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
from scapy.all import *

def obter_bssid_alvo():
    redes_wifi = []
    def callback(pacote):
        if pacote.haslayer(Dot11Beacon):
            bssid = pacote[Dot11].addr2
            if bssid not in redes_wifi:
                redes_wifi.append(bssid)

    sniff(iface="wlan0", prn=callback, timeout=10)

    print("Redes Wi-Fi disponíveis:")
    for i, bssid in enumerate(redes_wifi):
        print(f"{i+1}. {bssid}")

    escolha = int(input("Escolha o número da rede Wi-Fi alvo: "))
    bssid_alvo = redes_wifi[escolha-1]
    return bssid_alvo

# Definir as constantes para os tipos de ataque
TIPO_ATAQUE_BEACON = "beacon"
TIPO_ATAQUE_REPLAY = "replay"
TIPO_ATAQUE_DATA = "data"

# Definir a classe WifiInvader
class WifiInvader:
    """
    Uma classe que representa uma ferramenta de invasão Wi-Fi.
    """

    def __init__(self, janela):
        """
        Inicializa a ferramenta com a janela principal.

        Args:
            janela: A janela principal da aplicação.
        """

        self.janela = janela
        self.janela.title("WifiInvader")
        self.janela.geometry("600x400")
        self.janela.resizable(False, False)

        # Criar os widgets da interface
        self.criar_widgets()

    def criar_widgets(self):
        """
        Cria os widgets da interface gráfica.
        """

        # Criar o frame para os widgets de entrada
        self.frame_entrada = ttk.Frame(self.janela)
        self.frame_entrada.pack(fill=tk.BOTH, expand=True)

        # Adicionar um rótulo para o SSID alvo
        self.rotulo_ssid_alvo = ttk.Label(self.frame_entrada, text="SSID alvo:")
        self.rotulo_ssid_alvo.grid(row=0, column=0, sticky=tk.W)

        # Adicionar um campo de entrada para o SSID alvo
        self.entrada_ssid_alvo = ttk.Entry(self.frame_entrada)
        self.entrada_ssid_alvo.grid(row=0, column=1, sticky=tk.W)

        # Adicionar um rótulo para o tipo de ataque
        self.rotulo_tipo_ataque = ttk.Label(self.frame_entrada, text="Tipo de ataque:")
        self.rotulo_tipo_ataque.grid(row=1, column=0, sticky=tk.W)

        # Adicionar um menu suspenso para selecionar o tipo de ataque
        self.combobox_tipo_ataque = ttk.Combobox(self.frame_entrada, values=[TIPO_ATAQUE_BEACON, TIPO_ATAQUE_REPLAY, TIPO_ATAQUE_DATA], state="readonly")
        self.combobox_tipo_ataque.grid(row=1, column=1, sticky=tk.W)

        # Adicionar um botão para iniciar o ataque
        self.botao_iniciar_ataque = ttk.Button(self.frame_entrada, text="Iniciar ataque", command=self.iniciar_ataque)
        self.botao_iniciar_ataque.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

        # Criar o frame para os widgets de saída
        self.frame_saida = ttk.Frame(self.janela)
        self.frame_saida.pack(fill=tk.BOTH, expand=True)

        # Adicionar um rótulo para o status do ataque
        self.rotulo_status = ttk.Label(self.frame_saida, text="Status do ataque:")
        self.rotulo_status.grid(row=0, column=0, sticky=tk.W)

        # Adicionar uma caixa de texto para exibir o status do ataque
        self.texto_status = tk.Text(self.frame_saida, state="disabled")
        self.texto_status.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

        # Configurar a caixa de texto para usar a barra de rolagem

        # Criar a barra de rolagem para a caixa de texto
        self.barra_rolagem_status = ttk.Scrollbar(self.frame_saida, command=self.texto_status.yview)
        self.barra_rolagem_status.grid(row=1, column=2, sticky=tk.E)

    def iniciar_ataque(self):
        """
        Inicia o ataque.
        """

        # Obter o tipo de ataque
        tipo_ataque = self.combobox_tipo_ataque.get()

        # Obter o SSID alvo
        ssid_alvo = self.entrada_ssid_alvo.get()

        # Iniciar o ataque específico
        if tipo_ataque == TIPO_ATAQUE_BEACON:
            # Indicar que o ataque de beacon está desativado
            self.mostrar_status("Ataque de Beacon está desativado.")
        elif tipo_ataque == TIPO_ATAQUE_REPLAY:
            # Indicar que o ataque de replay está desativado
            self.mostrar_status("Ataque de Replay está desativado.")
        elif tipo_ataque == TIPO_ATAQUE_DATA:
            # Indicar que o ataque de data está desativado
            self.mostrar_status("Ataque de Data está desativado.")

    def mostrar_status(self, mensagem):
        """
        Exibe uma mensagem no campo de status.

        Args:
            mensagem: A mensagem a ser exibida.
        """
        self.texto_status.config(state="normal")
        self.texto_status.insert(tk.END, mensagem + "\n")
        self.texto_status.config(state="disabled")
        self.texto_status.yview(tk.END)

    def obter_bssid_alvo(self):
        """
        Obtém o BSSID alvo.
        """
        # Implemente a lógica para obter o BSSID alvo aqui
        pass

# Criar a janela principal
janela = tk.Tk()

# Criar uma instância da classe WifiInvader
wifi_invader = WifiInvader(janela)

# Iniciar o loop principal da aplicação
janela.mainloop()