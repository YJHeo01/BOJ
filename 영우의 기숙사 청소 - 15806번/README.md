### Algorithm : BFS

문제 URL : https://www.acmicpc.net/problem/15806
<ul>
  <li>그래프 탐색을 통해 곰팡이의 위치를 체크한다.</li>
  <li>특정한 시간 x에 좌표 (a,b)에 곰팡이가 증식했을 경우, 영우의 방 크기가 충분하다는 조건 하에 (2*n)초가 지난 이후 같은 위치 (a,b)에 다시 곰팡이가 증식한다. (단, n은 자연수)</li>
  <li>즉, 짝수 시간에 핀 곰팡이는 이후 짝수 시간대에도 다시 곰팡이가 증식하고, 홀수 시간도 이와 같다. <br>따라서, 그래프 탐색을 할 때 앞선 짝수 시간 혹은 홀수 시간에 방문했을 경우 다시 큐에 넣을 필요가 없다. </li>
  <li>그렇기 때문에 visited 리스트를 2 x (n+1) x (n+1) 사이즈로 선언한다. (n+1) x (n+1)은 영우의 방 사이즈이고, 앞에 2 x 는 짝수 시간 방문, 홀수 시간 방문을 구별하기 위해 이용하는 것이다. </li>
  <li>단, 영우의 방 크기가 충분하지 않을 경우 곰팡이는 증식할 수 없다. 따라서 마지막에 이런 예외를 위한 if문을 추가한다.</li>
</ul>
 



