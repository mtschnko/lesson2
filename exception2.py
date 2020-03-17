stock = [
    {'name': 'IP320', 'stock': 10, 'price': 3092, 'recomendet':['Носки']},
    {'name': 'POI12', 'stock': 9, 'price': 122, 'discount': 90},
    {'name': 'Roor11', 'stock': 3, 'price': 3332.0},
]

def discounted(price, discount, max_discount=20):
  try:
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
  except ValueError:
      print('Переданы некорректные аргументы')