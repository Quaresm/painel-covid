from datetime import datetime, timedelta

class Patients():

    def register_patient(self, patients_quantity):

        patients = []
        
        for p in range(patients_quantity):
            while True:
                name = input(f"Digite o nome do patiente {p + 1}: ")
                if not name.replace(" ", "").isalpha():
                    print("O nome deve conter apenas letras e espaços. Tente novamente.")
                    continue

                start_sick = input(f"Digite a data de início dos sintomas (formato DD/MM/AAAA) do {name}: ").strip()
                
                confirmed_sick_date = input(f"Digite a data de confirmação da COVID-19 (formato DD/MM/AAAA) do {name}: ").strip()

                accuatily_year = datetime.now().year
                accuatily_date = datetime.now()
                
                try:
                    # Convertendo para datetime formato de datas
                    confirmed_sick_date_converted = datetime.strptime(confirmed_sick_date, "%d/%m/%Y")
                    start_sick_converted = datetime.strptime(start_sick, "%d/%m/%Y")

                    # Verifica se os anos são válidos
                    if (
                        confirmed_sick_date_converted.year < 2020 
                        or start_sick_converted.year < 2020 
                        or confirmed_sick_date_converted.year > accuatily_year 
                        or start_sick_converted.year > accuatily_year
                    ):
                        print("O ano deve ser entre 2020 e o ano atual. Tente novamente.")
                        continue
                    else:
                        print("As datas estão válidas!")
                except ValueError:
                    print("Formato de data inválido. Use o formato DD-MM-AAAA.")
                    continue
                
                if start_sick_converted > accuatily_date:
                    print("A data de início não pode ser no futuro, digite novamente")
                    
                # Adicionando 14 dias a start_sick
                threshold_date_to_sick = start_sick_converted + timedelta(days=14)

                if confirmed_sick_date_converted > threshold_date_to_sick:
                    print("""Segundo as fontes da internet, o patiente pode confirmar somente até 14º dia após o início dos sintômas,
                        confira em https://www.cnnbrasil.com.br/saude/covid-quando-fazer-o-teste-para-evitar-falso-negativo/""")
                    continue

                if confirmed_sick_date_converted < start_sick_converted or confirmed_sick_date_converted > accuatily_date:
                    print("A data de confirmação não pode ser menor que a data de início do sintoma, digite novamente")
                    continue
                
                # Se ambas as entradas forem válidas, adiciona o paciente à lista
                patients.append({
                    "name": name,
                    "start_sick": start_sick_converted,
                    "confirmed_sick_date": confirmed_sick_date_converted
                })
                print(f"Paciente {name} registrado com sucesso!")
                break
        return patients

    #Calculo o tempo máximo que pode ter sintomas ou transmitir o COVID, baseado na wiki  https://coronavirus.es.gov.br/
    def calculate_sick_time(self, patients):
        for patient in patients:
            symptoms_and_transmission_end = patient['start_sick'] + timedelta(days=7)
            # Atualiza o próprio dicionário do paciente
            patient["symptoms_and_transmission_end"] = symptoms_and_transmission_end
        return patients