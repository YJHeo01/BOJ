/*
  https://www.acmicpc.net/problem/10431
  https://www.acmicpc.net/source/73012792
*/

#include <stdio.h>

int student[20] = { 0, };

void change_value(int left, int right) {
	for (int i = right; i > left; i--) {
		int tmp = student[i];
		student[i] = student[i - 1];
		student[i - 1] = tmp;
	}

}
int check_student(int idx) {
	for (int i = 0; i < idx; i++) {
		if (student[i] > student[idx]) {
			change_value(i, idx);
			return idx - i;
		}
	}
	return 0;
}
int main() {
	int p;
	scanf("%d", &p);
	for (int j = 0; j < p; j++) {
		int test_num = 0;
		int answer = 0;
		scanf("%d", &test_num);
		for (int i = 0; i < 20; i++) {
			scanf("%d", &student[i]);
			answer += check_student(i);
		}
		printf("%d %d\n",test_num,answer);
	}
}
