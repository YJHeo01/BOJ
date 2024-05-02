### Algorithm : BFS, 구현

https://www.acmicpc.net/problem/21609

문제의 내용을 요약하면 다음과 같다.
<ol>
  <li>크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다. </li>
  <li>1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.</li>
  <li>격자에 중력이 작용한다.</li>
  <li>격자가 90도 반시계 방향으로 회전한다.</li>
  <li>다시 격자에 중력이 작용한다.</li>
  <li>블록 그룹이 존재하는 동안 계속해서 반복되어야 한다</li>
</ol>

이를 해결하기 위해 사용한 함수는 다음과 같다.
<ul>
  <li> 격자판의 초기상태를 입력받음 -> get_board()</li>
  <li> 크기가 가장 큰 블록 그룹을 찾는다 -> get_block_cnt(graph,visited,start)</li>
  <li> 크기가 같은 블록 그룹이 여러 개일 경우 -> main 함수 내 반복문 내 if문 </li>
  <li>1에서 찾은 블록 그룹의 모든 블록을 제거한다. -> remove_block(graph,start)</li>
  <li>격자의 중력 작용 -> gravity(graph) </li>
  <li>격자의 반시계 방향 회전 -> turn_counterclockwise(board)</li>
  <li>블록 그룹이 존재하는 동안 반복 -> finish_game(target_block_cnt) </li>
</ul>
