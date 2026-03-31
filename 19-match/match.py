import unicodedata

def remove_accents(input_str):
    """
    Removes accents (diacritics) from a string using Unicode normalization.
    """
    # Normalize the string to NFKD form (separates base character and diacritic)
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    
    # Filter out characters that are classified as non-spacing combining marks ('Mn')
    # These are typically the accents themselves
    without_accents = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    return without_accents

dia = 1
match dia:
    case 1: 
        print ('Lunes')
    case 2: 
        print ('Martes')
    case 3:
        print ('Miércoles')
    case _: 
        print ('Otro')

diaNombre = 'miércoles'
match remove_accents(diaNombre.strip().lower()):
    case 'lunes':
        print("Monday")
    case 'martes':
        print("Tuesday")
    case 'miercoles':
        print("Wednesday")
    case 'jueves':
        print("Thursday")
    case 'viernes':
        print('Friday')
    case 'sabado':
        print('Saturday')
    case 'domingo':
        print('Sunday')
    case _:
        print("No es un dia")