문제 URL : https://www.acmicpc.net/problem/21610

문제의 내용을 요약하면 다음과 같다.
<ol>
  <li>모든 구름이 di 방향으로 si칸 이동한다.</li>
  <li>각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.</li>
  <li>구름이 모두 사라진다.</li>
  <li>
  2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
  </li>
      <ul>
        <li>이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.</li>
        <li>예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.</li>
    </ul>
  <li>바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.</li>
</ol>
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
<br>번호 별 함수는 다음과 같다.
<ol>
  <li>move_cloud(cloud_list,command)</li>
  <li>rain(ground,cloud_list)</li>
  <li>erase_cloud_area(cloud_area,cloud_list)</li>
  <li>magic(ground,cloud_list)</li>
  <li>creative_new_cloud(ground,cloud_area)</li>
</ol>
<br> 모든 이동이 끝난 후 바구니에 들어있는 물의 양의 합을 구하는 함수 -> get_answer(ground)
