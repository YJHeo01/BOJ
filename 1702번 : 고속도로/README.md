문제 URL : https://www.acmicpc.net/problem/1702

![image](https://github.com/YJHeo01/BOJ/assets/93248202/904c6e37-0e7f-4653-8df9-00a5eb0e63ab)

해설
<ul>
  <li>최단 시간 경로와 최단 시간은 아니어도 더 저렴한 가격으로 통과할 수 있는 경로를 찾는 문제</li>
  <li>dijkstra 함수 내 max_time, max_cost, min_cost가 이를 위한 해법이다.</li>
  <li>if nt > max_time[nx] and nc < min_cost[nx]: max_time[nx] = nt; min_cost[nx] = nc</li>
  <li>38번째, 39번째 줄(위 코드)은 현재까지 가장 저렴한 경로보다 더 저렴한 경로를 위한 코드이다.</li>
  <li>if nc > max_cost[nx] and nt < distance[nx][max_cost[nx]]: max_cost[nx] = nc</li>
  <li>40번째, 41번째 줄(위 코드)은 현재까지의 최단 시간 경로보다 더 비싼 경로가 있을 때 더 비싼 경로가 새 최단 시간 경로인지 알아내는 코드이다.</li>
  <li>위 코드들을 통해 max_time, max_cost, min_cost를 갱신하여 q에서 뽑아낸 정보가 유효한 정보인지 검사하는 32번째, 35번째 줄 코드에 사용한다.</li>
  <li>위의 요소를 제외하면 특별한 점은 없는 데이크스트라 문제이다.</li>
</ul>
