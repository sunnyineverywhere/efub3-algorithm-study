alpha = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(word)):
    alpha = alpha.replace(word[i], "*")

print(len(alpha))