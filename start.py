#Objetivo dessa aplicação e criar um visual no terminal de quantos afetados foram pelo covid conforme o cadastro
from patients.register_patient import Patients

patients = Patients()

def init_covid_graph():
    print("Se bem-vindo ao dashboard de pacientes com COVID.")

    while True:
        patients_count = input("Digite em números a quantidade de pacientes infectados: ")
        if patients_count.isdigit():
            patients_count = int(patients_count)
            break
        else:
            print("Por favor, digite somente números inteiros.")

    patients = Patients()
    
    # Chamando a função para registrar pacientes
    registered_patients = patients.register_patient(patients_count)

    # Calculando o tempo de sintomas para os pacientes registrados
    patients_with_sick_time = patients.calculate_sick_time(registered_patients)

    print("\n--- Lista de Pacientes com Informações Completas ---")
    for patient in patients_with_sick_time:
        print(f"Nome: {patient['name']}")
        print(f"Data de Início dos Sintomas: {patient["start_sick"].strftime('%d/%m/%Y')}")
        print(f"Data de Confirmação: {patient["confirmed_sick_date"].strftime('%d/%m/%Y')}")
        print(f"Período de Transmissão: até {patient["symptoms_and_transmission_end"].strftime('%d/%m/%Y')}")
        print("-" * 30)
    
    while True:
        immunity_recipe = input("Você deseja saber como aumentar a sua imunidade? Digite sim ou não: ")
        if immunity_recipe == "NÃO".lower():
            break
        elif immunity_recipe.isalpha():
            print("-" * 30)
            print("""
            Coma alimentos que tenham:
                  
            Ômega-3: sardinha, salmão, arenque, atum, sementes de chia, nozes e linhaça;
            Selênio: castanha-do-pará, trigo, arroz, gema de ovo, sementes de girassol, frango, pão, queijo, repolho e farinha de trigo;
            Zinco: ostras, camarão, carne bovina, frango, peru e peixe, gérmen de trigo, grãos integrais e frutos secos (castanha, amendoim e castanha-do-pará);
            Vitamina C: laranja, tangerina, abacaxi, limão, morango, melão, mamão, manga, kiwi, brócolis, tomate e melancia;
            Vitamina E: sementes de girassol, avelã, amendoim, amêndoas, pistache, manga, azeite de oliva, molho de tomate, óleo de girassol, nozes e mamão;
            Vitamina A: cenoura, babata doce, manga, espinafre, melão, acelga, pimentão vermelho, brócolis, alface e ovo;
        """)    
            print("-" * 30)
            break
        else:
            print("Digite apenas a resposta sim ou não")
            continue
if __name__ == "__main__":
    init_covid_graph()