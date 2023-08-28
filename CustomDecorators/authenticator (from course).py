# Create an @authenticated decorator that only allows the function to run when user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(data):
    if data['valid']:
        return fn(data)
  return wrapper