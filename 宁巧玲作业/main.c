#include<stdio.h>
int main(){
    int m, n, count = 0; 
    scanf("%d %d", &m, &n);
    
    for(int i = m; i <= n; i++){
        if((i % 4 == 0 && i % 100 != 0) || i % 400 == 0){ 
            printf("%d ", i);
            count++; 
        }
        if(count % 10 == 0 && count != 0){ 
            printf("\n");
        }
    }
    
    return 0;
}
