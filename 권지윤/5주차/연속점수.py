# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#슬라이딩 ? -> 연속된 수 중 가장 큰 연속 수
total = int(input())
score= list(map(int, input().split()))
first_max = max(score)
second_max = 0
tmp = [score[0]]
for i in range(1, total):
	if len(tmp) == len(score):
		break
	if score[i] - score[i-1] == 1:
		tmp.append(score[i])
	else:
		tmp.clear()
		tmp.append(score[i])
	second_max = max(second_max, sum(tmp))

print(max(first_max, second_max))

