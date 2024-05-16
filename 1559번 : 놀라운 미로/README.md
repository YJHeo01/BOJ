### 이 파일은 두 코드 중 놀라운 미로 - 1559번.py에 대한 해설입니다.

문제 URL : https://www.acmicpc.net/problem/1559

![놀라운 미로](https://github.com/YJHeo01/BOJ/assets/93248202/cc974aac-3a38-4cfa-91e7-e9122934a6af)

<ul>
  <li>permutations를 이용해서 상자를 방문하는 모든 경우의 수를 알아냄</li>
  <li>get_idx_list 함수는 순열을 활용하기 위해 만든 함수</li>
  <li>이 코드의 핵심은 bfs 함수
    <ul>
      <li>distance는 각 지점별 최단 소요 시간을 나타내고, visited는 최단 시간 + 기다리는 시간</li>
      <li>if (visited[vx][vy] + direction[graph[vx][vy]]) % 4 != i : wait = True; continue는 원하는 방향의 문이 열릴 때를 기다리는 것을 구현</li>
    </ul>
  </li>
</ul>


