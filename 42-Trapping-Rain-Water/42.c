#include<stdio.h>

int get_max(int a, int b){
    if(a>=b) return a;
    else return b;
}

int get_min(int a, int b){
    if(a<=b) return a;
    else return b;
}

int trapping_rain_water(int height[], int n){
    if(n<=2){
        return 0;
    }
    else{
        int i;
        int left_max[n], right_max[n], vol_of_water = 0;
        left_max[0] = height[0];
        right_max[n-1] = height[n-1];
        
        for(i=1; i<n; i++){
            left_max[i] = get_max(left_max[i-1], height[i]);
        }

        i = n-2;
        while(i>=0){
            right_max[i] = get_max(right_max[i+1], height[i]);
            i--;
        }

        for(i=1;i<n-1;i++){
            vol_of_water += get_min(left_max[i], right_max[i]) - height[i];
        }

        return vol_of_water;
    }
}

int main(){
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int height[n];
    printf("Enter the array of heights: ");
    for(int i=0; i<n; i++){
        scanf("%d",&height[i]);
    }

    printf("Volume of water that can be trapped = %d\n", trapping_rain_water(height, n));
    return 0;
}