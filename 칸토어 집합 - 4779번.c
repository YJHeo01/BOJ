//https://www.acmicpc.net/problem/4779
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void cantor(int first, int last, char chr) {
	if (first + 1 == last) {
		printf("%c", chr); // 선의 길이가 1일때 출력한다.
		return;
	}
	cantor(first, first + (last - first) / 3, chr);
	cantor(first + (last - first) / 3, first + 2 * (last - first) / 3, ' '); // 가운데 문자열을 공백으로
	cantor(first + 2 * (last - first) / 3, last, chr);
	return;
}
int main() {
	int n;
	while (scanf("%d", &n)!=EOF) {
		cantor(0, (int)pow(3, n), '-');
		printf("\n");
	}
}
