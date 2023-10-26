max_num = 0
people = 0
for _ in range(10):
    bye , hello = map(int, input().split())
    people -= bye
    people += hello

    max_num = max(people, max_num)
print(max_num)
