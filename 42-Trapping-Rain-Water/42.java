import java.util.Scanner;

class solution{

    public static int get_max(int a, int b){
        if(a>=b) return a;
        else return b;
    }

    public static int get_min(int a, int b){
        if(a<=b) return a;
        else return b;
    }

    public static int trapping_rain_water(int[] height, int n){
        if(n<=2) return 0;
        else{
            int[] left_max = new int[n];
            int[] right_max = new int[n];
            int vol_of_water = 0;
            left_max[0] = height[0];
            right_max[n-1] = height[n-1];
            int i;
            
            for(i=1;i<n;i++){
                left_max[i] = get_max(left_max[i-1], height[i]);
            }
            i = n-2;
            while(i>=0){
                right_max[i] = get_max(right_max[i+1], height[i]);
                i--;
            }

            for(i=1; i<n-1; i++){
                vol_of_water += get_min(left_max[i], right_max[i]) - height[i];
            }

            return vol_of_water;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.print("Enter the size of the array: ");
        n = sc.nextInt();
        int[] height = new int[n];
        System.out.println("Enter the array of heights: ");
        for(int i=0; i<n; i++){
            height[i] = sc.nextInt();
        }
        System.out.println("Vol of water that can be trapped = " + trapping_rain_water(height, n));
    }
}