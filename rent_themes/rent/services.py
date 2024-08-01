from datetime import datetime

class Util():
    def calcular_desconto(date_rent, theme_price, client):
        discount = 0

        date = datetime.strptime(date_rent, '%Y-%m-%d')
        day_of_week = date.weekday()
        
        if day_of_week in [0, 1, 2, 3]:
            discount += 0.40

        if not client.first_purchase:
            discount += 0.10
        
        client.first_purchase = False
        client.save()
        
        value_with_discount = theme_price * (1 - discount)
        
        return value_with_discount