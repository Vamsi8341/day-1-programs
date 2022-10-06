def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_Happy_num(19))
print(is_Happy_num(2))
print(is_Happy_num(1))
print(is_Happy_num(0))
print(is_Happy_num(5))
