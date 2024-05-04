from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from send_email import email_alert
from selenium.webdriver.chrome.options import Options
import IPython


def check_vacancies():
    
    to_addr = ['andre.romoli@gmail.com',
                'biiagrachet@hotmail.com', 
                'isaacespelho@gmail.com',
                'pedromorande@gmail.com',
                'ricardoutil@gmail.com',
                'verofarma@bol.com.br']

    #to_addr = ['pedromorande@gmail.com']

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://outlook.office365.com/owa/calendar/Vagasacademia@sesisenaisp.onmicrosoft.com/bookings/")

    time.sleep(1.5)
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[4]/div[1]/button').click()
    time.sleep(1.5)

    xpaths = {'Volei': '/html/body/div/div/form/div[4]/div[1]/ul/li[1]/label/div[1]',
            'Natacao Adulto': '/html/body/div/div/form/div[4]/div[1]/ul/li[2]/label/div[1]',
            'Judo': '/html/body/div/div/form/div[4]/div[1]/ul/li[3]/label/div[1]',
            'Beach Training': '/html/body/div/div/form/div[4]/div[1]/ul/li[4]/label/div[1]',
            'Beach Tennis': '/html/body/div/div/form/div[4]/div[1]/ul/li[5]/label/div[1]',
            'Pilates': '/html/body/div/div/form/div[4]/div[1]/ul/li[6]/label/div[1]',
            'Musculacao': '/html/body/div/div/form/div[4]/div[1]/ul/li[7]/label/div[1]',
            'Hidroginastica': '/html/body/div/div/form/div[4]/div[1]/ul/li[8]/label/div[1]',
            }
    
    msg = 'Vagas disponiveis Sesi Araras: \n'

    for xpath in xpaths:
        driver.find_element(By.XPATH, xpaths[xpath]).click()
        time.sleep(1.5)
        try:
            horarios = driver.find_element(By.XPATH, '/html/body/div/div/form/div[5]/div[2]/div/div[2]/ul').text
            msg += f'\n ************** \n {xpath} - VAGA ENCONTRADA!\n'
            cont_hor = 0
            for horario in horarios.split('\n'):
                if cont_hor == 0:
                    msg +=  f'{horario}'
                else:
                    msg +=  f' - {horario}'
                cont_hor += 1    
        except:
            pass

    driver.quit()

    if msg.split('Vagas disponiveis Sesi Araras: \n')[1] != '':
        msg += '\n \n Acesse o link para fazer sua inscricao! \n https://outlook.office365.com/owa/calendar/Vagasacademia@sesisenaisp.onmicrosoft.com/bookings/'
        email_alert(msg, to_addr)