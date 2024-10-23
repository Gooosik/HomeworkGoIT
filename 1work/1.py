from datetime import datetime

def get_days_from_today(date):

    try:

        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        date_now = datetime.today().date()
        result = (date_now - input_date).days

        return result
    
    except ValueError:
        
        return "Неправильний формат дати"

print(get_days_from_today('2006-06-03'))
