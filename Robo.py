import pyautogui
import time
dimencaodata = 680, 528
dimencaodia = 781, 940   
contador = 0  
dimencaonome = 560, 753  
dimencaoexcel = 1027, 1041
dimencaoprimeiralinhaexcel = 126, 548
nome = "MILTON"
email = "MILTON.CABRAL@MERCADOLIVRE.COM"
svc = "smg1"
origem = "BRXPR1"
transportadora = "SEQUOIA"
motorista = "RGERIO AFORNSO"  
placa = "EVL8M64"
lacre = '3120'
dimencaovolta = 598, 348    
contador = 0
link = "https://drive.google.com/drive/folders/1_H8INGOCtwfM2SnN9mnBvN3wHtzMmU3f?usp=sharing"
pyautogui.PAUSE = 0.40                   
pyautogui.alert('ja vai começar')
pyautogui.press('winleft')
time.sleep(0.8)
pyautogui.write("chrome" )
time.sleep(0.8)
pyautogui.press('enter')
time.sleep(0.8)
pyautogui.write("https://docs.google.com/forms/d/e/1FAIpQLSed7e5ks525vW_wyaezlgqnMY2gY5hoBhQPo8AGRvwSYw3wew/viewform")
time.sleep(0.8)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(dimencaodata)
time.sleep(0.8)
pyautogui.click()
time.sleep(0.8)
pyautogui.moveTo(dimencaodia)  
time.sleep(0.8)
pyautogui.click()
time.sleep(0.8)
# nome
pyautogui.moveTo(dimencaonome)
time.sleep(0.8)
pyautogui.click()
pyautogui.write(nome)
time.sleep(0.8)
pyautogui.press('tab')

# email
pyautogui.write(email)
time.sleep(0.8)
pyautogui.press('tab')
time.sleep(0.8)
# shipment
pyautogui.moveTo(dimencaoexcel)
pyautogui.click()
time.sleep(0.8)
pyautogui.moveTo(dimencaoprimeiralinhaexcel)
pyautogui.click()
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 'v')

# motivo da devolução
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('down')
time.sleep(0.2)
pyautogui.press('tab')
time.sleep(0.4)
pyautogui.write(svc)
pyautogui.press('tab')
time.sleep(0.4)
pyautogui.write(origem)
pyautogui.press('tab')
time.sleep(0.6) 
## transportadora
pyautogui.write(transportadora)
time.sleep(0.4)
# placa do veiculo
pyautogui.press('tab')
time.sleep(0.6)
pyautogui.write(placa)
# nome motorista
pyautogui.press('tab')
time.sleep(0.4)
pyautogui.write(motorista)
time.sleep(0.4)
# lacre
pyautogui.press('tab')
time.sleep(0.4)
pyautogui.write(lacre)
pyautogui.press('tab')
time.sleep(0.4)
pyautogui.write('0')
pyautogui.press('tab')
pyautogui.write(link)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(0.4)
#voltar
time.sleep(4)
pyautogui.moveTo(dimencaovolta)
pyautogui.click()
#novo
pyautogui.hotkey('alt', 'tab')
time.sleep(0.4)
pyautogui.press('down')
time.sleep(0.4)

pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(dimencaodata)
time.sleep(0.8)
pyautogui.click()
time.sleep(0.8)
pyautogui.moveTo(dimencaodia)  
time.sleep(0.8)
pyautogui.click()
time.sleep(0.8)
pyautogui.moveTo(dimencaonome)
time.sleep(0.8)
pyautogui.click()
pyautogui.write(nome)

# email

while contador < 66:
    pyautogui.press('tab')
    pyautogui.write(email)
    time.sleep(0.8)
    pyautogui.press('tab')
    time.sleep(0.8)
    # shipment
    pyautogui.moveTo(dimencaoexcel)
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'v')

    # motivo da devolução
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.4)
    pyautogui.write(svc)
    pyautogui.press('tab')
    time.sleep(0.4)
    pyautogui.write(origem)
    pyautogui.press('tab')
    time.sleep(0.6) 
    ## transportadora
    pyautogui.write(transportadora)
    time.sleep(0.4)
    # placa do veiculo
    pyautogui.press('tab')
    time.sleep(0.6)
    pyautogui.write(placa)
    # nome motorista
    pyautogui.press('tab')
    time.sleep(0.4)
    pyautogui.write(motorista)
    time.sleep(0.4)
    # lacre
    pyautogui.press('tab')
    time.sleep(0.4)
    pyautogui.write(lacre)
    pyautogui.press('tab')
    time.sleep(0.4)
    pyautogui.write('0')
    pyautogui.press('tab')
    pyautogui.write(link)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.4)
    #voltar
    time.sleep(4)
    pyautogui.moveTo(dimencaovolta)
    pyautogui.click()
    #novo
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.4)
    pyautogui.press('down')
    time.sleep(0.4)

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.moveTo(dimencaodata)
    time.sleep(0.8)
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.moveTo(dimencaodia)  
    time.sleep(0.8)
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.moveTo(dimencaonome)
    time.sleep(0.8)
    pyautogui.click()
    pyautogui.write(nome)
    contador = contador + 1
    if contador == 66 :
        break
    time.sleep(1)
pyautogui.alert("finalizou")






