#include <stdio.h>

void reverse(int n) {
    int reversed = 0;
    while (n != 0) {
        int remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }
    printf("%d\n", reversed);
}

int main() {
    int i;
    scanf("%d", &i);
    reverse(i);
    return 0;
}