from check_vacancies import check_vacancies
import time

cont = 0
while True:
    print(f'Execucao {cont+1}')
    check_vacancies()
    time.sleep(1800)
    cont+=1