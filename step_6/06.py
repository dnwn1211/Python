char = input()

croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0 

for i in croatian_alphabets:
    count += char.count(i)

print(len(char) - count)
