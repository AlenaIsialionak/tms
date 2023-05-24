my_list = list(range(1, 101))
sp = [i if i % 10 == 0
      else i * 10 if i % 4 != 0 else i * 2
      for i in my_list]
print(sp)
