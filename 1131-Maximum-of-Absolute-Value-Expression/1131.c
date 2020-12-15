#include<stdio.h>
#include<limits.h>

int get_max(int a, int b){
    if(a>=b){
        return a;
    }
    else return b;
}

int get_min(int a, int b){
    if(a<b){
        return a;
    }
    else return b;
}

int get_max_of_4(int a, int b, int c, int d){
    int maximum;
    maximum = a>=b ? (a>=c? a : c) : (b>=c? b : c);
    maximum = maximum >= d ? maximum: d;
    return maximum;
}


int max_abs_value(int arr1[], int arr2[], int n){
    int max1, max2, max3, max4;
    //maxima are initialized to INT_MIN, so that they can be upgraded for next maximum value after comparisions
    max1 = max2 = max3 = max4 = INT_MIN;
    
    int min1, min2, min3, min4;
    //minima are initialized to INT_MAX, so that they can be upgraded for next minimum value after comaprisions
    min1 = min2 = min3 = min4 = INT_MAX;

    int temp = 0;

    for(int i=0; i<n; i++){
        temp = arr1[i] + arr2[i] + i;
        max1 = get_max(max1, temp);
        min1 = get_min(min1, temp);

        temp = arr1[i] + arr2[i] - i;
        max2 = get_max(max2, temp);
        min2 = get_min(min2, temp);

        temp = arr1[i] - arr2[i] + i;
        max3 = get_max(max3, temp);
        min3 = get_min(min3, temp);

        temp = arr1[i] - arr2[i] - i;
        max4 = get_max(max4, temp);
        min4 = get_min(min4, temp);

    }

    int final_answer = get_max_of_4(max1-min1, max2-min2, max3-min3, max4-min4);
    return final_answer;
}

int main(){
    int n;
    printf("Enter the size of the arrays: "); //size of both the arrays is same
    scanf("%d",&n);

    int arr1[n], arr2[n];
    //Enter the first array
    printf("Enter the first array of %d elements: ",n);
    for(int i=0; i<n; i++) scanf("%d",&arr1[i]);

    //Enter the second array
    printf("Enter the second array of %d elements: ",n);
    for(int i=0; i<n; i++) scanf("%d",&arr2[i]);

    printf("The maximum of absolute value expression is: %d\n",max_abs_value(arr1, arr2, n));
    return 0;
}