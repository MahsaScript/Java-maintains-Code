public class C {
    public static void main(String args[]) {
      C c_obj=new C();
      c_obj.M();
    }
    public static void M() {
      int x=10;
      int y=25;
      int z=x+y;
      int[] array_x = {10457, 234520, 34505, 45480};
      int[] array_y = {24570, 4570, 9543550, 334500}; 
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
