public class C1 {
    public static void main(String args[]) {
      C1 c_obj=new C1();
      c_obj.M1();
    }
    public static void M1() {
      int x=10;
      int y=25;
      int z=x+y;
      int[] array_x = {30, 70, 130, 340};
      int[] array_y = {120, 170, 190, 5300}; 
      double sum_X=0;
      double sum_Y=0;
      for (int i = 0; i < 4; i++) {
          sum_X = sum_X + array_x[i];
          sum_Y = sum_Y + array_y[i];
      }
      double mean_x = sum_X/4;
      double mean_y = sum_Y/4;
      System.out.println("S");
      System.out.println("The average of List X is " + mean_x);
      System.out.println("The average of List Y is " + mean_y);
      System.out.println("E");
    }
}