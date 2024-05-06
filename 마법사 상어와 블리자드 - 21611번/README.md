문제 URL : https://www.acmicpc.net/problem/21611

<ul>
  <li>벽 및 칸의 번호를 구현하기 위해 get_line_up 함수를 통해 각 번호별로 어느 행, 어느 열인지 알아냄 </li>
  <li>di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. -> destroy 함수</li>
  <li>구슬이 파괴된 후 빈 칸이 생겨 구슬이 이동 -> move_ball 함수</li>
  <li>구슬 폭발 조건 확인 -> search_bang</li>
  <li>폭발 구현 및 점수 계산 -> bang 함수</li>
  <li>더 이상 폭발한 구슬이 없을 때, 구슬이 변화하는 단계 -> change_board, get_ball_list 함수 </li>
</ul>
