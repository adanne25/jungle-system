class fol   //function overloading example
{
  void add(int a, int b, int c)
  {
   int sum = a + b + c;
  System.out.println("sum of numbers"+ sum);
}
 
  void add(double a, int b)
{
  double sum = a + b;
  System.out.println("sum of numbers"+ sum);
}
}
  class execute
{
  public static void main(String[]  kjl)
{
  fol obj = new fol();
  obj.add(11,78);
  obj.add(78.4,67);
}
}
