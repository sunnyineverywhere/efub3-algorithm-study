import sys
r, c, t = map(int, sys.stdin.readline().split()) #행,열, t초후
room  = []
cleaner_top_index = 0
cleaner_bottom_index = 0


# 1. 미세먼지 확산
def diffuse_fine_dust():
  steps = [[-1, 0], [1,0], [0,-1], [0,1]] #상하좌우
  diffusion = [[0] * c for _ in range(r)] # r*c 확산표, 초기값:0
  # 각 좌표를 돌면서 좌표별로 추가될 먼지 계산, 빠질 먼지 반영해서 업데이트
  for i in range(r):
    for j in range(c):
      # 현위치에서 확산되는 양 계산
      if not (room[i][j] == -1 or room[i][j] == 0):
        side = 0
        for dx, dy in steps:
          nx = i + dx
          ny = j + dy  
          if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1 : # 방에 실재하는 위치이고 공기청정기가 있는 위치가 아니면
            side += 1 # 확산 가능
            diffusion[nx][ny] += room[i][j] // 5 #상하좌우 (i,j)에 확산될 양 추가
        room[i][j] = room[i][j] - (room[i][j]//5 * side) # 상하좌우로 확산될 먼지 빼기

  for i in range(r):
    for j in range(c):
      room[i][j] += diffusion[i][j]
  return
        

# 2-1. 공기청정기 위쪽 바람 - 먼지 이동 (동->북->서->남)
def cleaner_top():
  global cleaner_top_index
  x, y =  cleaner_top_index, 0
  pre_value = 0
  while True:
    # 이동할 좌표
    if x == cleaner_top_index and y != c-1:
      y += 1 # 동쪽으로 이동
    elif 0 < x <= cleaner_top_index and y == c-1 :
      x -= 1 # 북쪽으로 이동
    elif x == 0  and y != 0:
      y -= 1
    elif 0<= x < cleaner_top_index and y==0:
      x += 1
    pre_value, room[x][y] = room[x][y], pre_value
    if x == cleaner_top_index and y == 0:
      room[x][y] = -1
      break
      
# 2-2. 공기청정기 아래쪽 바람 - 먼지 이동(동->남->서->북)
def cleaner_bottom():
  global cleaner_bottom_index
  x = cleaner_bottom_index
  y =  0
  pre_value = 0
  while True:
    if x == cleaner_bottom_index and y != c-1:
      y += 1
    elif cleaner_bottom_index <= x < r-1 and y == c-1:
      x += 1
    elif x == r-1 and y != 0:
      y -= 1
    elif cleaner_bottom_index < x <= r-1 and y == 0:
      x -= 1

    pre_value, room[x][y] = room[x][y], pre_value
    if x == cleaner_bottom_index and y == 0:
      room[x][y] = -1
      break


for i in range (r):
  room.append(list(map(int, sys.stdin.readline().split())))
  for j in range(len(room[i])):
    if room[i][j] == -1: # room[i][j] == -1이면 공기청정기 있는 것
      cleaner_top_index = i
      cleaner_bottom_index = i+1
      
total = 0
for _ in range(t):
  diffuse_fine_dust()
  cleaner_top()
  cleaner_bottom()

for i in range(r):
  for j in range(c):
    if room[i][j] > 0:
      total += room[i][j]

print(total)




  

  
  
  





