/*
Problem Description:
Tom is a scientist. He uses huge machines for complex calculations. There is a problem, the machines takes input as Fahrenheit and Tom has the temperatures in Degree Celsius. As he is busy with his work, he asks your help to convert Degree Celsius to Fahrenheit.

Input:
The first and only line of the input consists of a single integer T denoting temperature in Degree Celsius.

Output:
Print an integer denoting temperature in Fahrenheit.

Constraints:
0<=T<=1000

Sample Input:
100

Sample Output:
212
*/

import java.util.Scanner;

class Dcoder
{  
  public static void main(String args[])
  {  
    Scanner scan = new Scanner(System.in);
      int celsius = scan.nextInt();
      int farenheit = ((celsius * 9) / 5) + 32; 
      System.out.println(farenheit);
  }
}
