### Algorithm : 데이크스트라

문제 URL : https://www.acmicpc.net/problem/13907

<ul>
  <li>최적화가 중요한 문제이다. 최적화를 위해 사용한 방법은 다음과 같다.</li>
  <li>distance 배열을 2차원으로 선언하여 지나간 도로 개수 별로 최단 금액이 어느정도인지 나타낸다.</li>
  <li>dijkstra 함수 내 best_path_road_cnt를 활용하여 최단 경로보다 더 많은 도로를 지나가는 경로는 무시하도록 했다.</li>
  <li>tax 함수에서 k번째 함수를 부과했을 때, length = answer_idx + 1을 통 가장 적은 금액이 나온 경로보다 더 많은 도로를 지나가는 경우는 생략하도록 했다. </li>
  <li>위 요소를 제외하면 전형적인 데이크스트라 문제라고 볼 수 있다.</li>
</ul>
