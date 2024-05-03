from check_vacancies import check_vacancies
import time

cont = 0
while True:
    print(f'Execucao {cont+1}')
    check_vacancies()
    time.sleep(600)
    cont+=1