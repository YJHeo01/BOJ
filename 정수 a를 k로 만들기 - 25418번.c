/*
  https://www.acmicpc.net/problem/25418
  https://www.acmicpc.net/source/75019676
  백준 온라인저지 25418번 - 정수 a를 k로 만들기
*/

#define MIN(a,b) a > b ? b : a
#define MAX(a,b) a > b ? a : b
#include <stdio.h>
#include <stdlib.h>

int dp[1000001] = { 0, };

int main() {
	int a, k;
	scanf("%d %d", &a, &k);
	int length = MIN(2 * a, k);
	for (int i = a+1; i <= length; i++) {
		dp[i] = dp[i - 1] + 1;
	}
	for (int i = 2 * a; i <= k; i++) {
		if (i % 2 == 0) {
			dp[i] = MIN(dp[i / 2], dp[i - 1]) + 1;
		}
		else {
			dp[i] = dp[i - 1] + 1;
		}
	}
	printf("%d", dp[k]);
}
