import physics



def zjisti_cas_svetla(distance):
    fall_time = physics.light(distance)
    print(f'Čas potřebný pro světlo k uražení {distance} km je {fall_time:.2f} s.')

def zjisti_cas_zvuku(distance):
    fall_time = physics.sound(distance)
    print(f'Čas potřebný pro zvuk k uražení {distance} km je {fall_time:.2f} s.')

def zjisti_cas_padu(distance):
    fall_time = physics.time_to_fall_earth(distance)
    print(f'Čas potřebný pro objekt na zemi ve výšce {distance} m je {fall_time:.2f} s.')

zjisti_cas_svetla(int(input('Napiš vzdálenost v km pro rychlost světla:')))
zjisti_cas_zvuku(int(input('Napiš vzdálenost v km pro rychlost zvuku:')))
zjisti_cas_padu(int(input('Napiš výšku v metrech, ze které bude těleso padat na zemi: ')))
