from datetime import datetime
from .models import Rent

class Util():
    def calcular_desconto(date_rent, theme_price, client):
        discount = 0

        date = datetime.strptime(date_rent, '%Y-%m-%d')
        day_of_week = date.weekday()
        
        if day_of_week in [0, 1, 2, 3]:
            discount += 0.40

        if Rent.objects.filter(client=client).exists():
            discount += 0.10
        
        value_with_discount = theme_price * (1 - discount)
        
        return value_with_discount