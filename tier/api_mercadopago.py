import mercadopago
import json

CLIENT_ID = '326996961336287'
CLIENT_SECRET = 'Iaw4FjTdpkxt01yP1VxHvifQA8r2gK8y'


def payment(req , **kwargs):
    tier = kwargs['ti']
    preference = {
      "items": [
        {
          "title": 'suscripcion',
          "quantity": 1,
          "currency_id": "ARS",
          "unit_price": tier.price
        }
      ]
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
