'''
Link: https://softeer.ai/practice/info.do?idx=1&eid=407&sw_prbl_sbms_sn=266442
'''
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

answer = k

for _ in range(n):
    answer = (answer * p) % 1000000007

print(answer)
