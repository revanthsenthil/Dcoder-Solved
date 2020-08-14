"""
Problem Description:
A town in Death Valley has a water tank that contains 10,000 gallons of water. If there is no rain, calculate the number of weeks the water will last for an input weekly water usage.

Input:
Input contains positive integer n , which indicates weekly water usage

Output:
Output will be number of weeks the water last for.

Constraints:
0<n<10000
Do not include the last week if the water remaining for that week is less than the weekly usage amount.

Sample Input:
1000

Sample Output:
10
"""

import java.util.Scanner;

//Compiler version JDK 11.0.2

class Dcoder
{  
  public static void main(String args[])
  {  
    Scanner scan = new Scanner(System.in);
    int x = scan.nextInt();
    System.out.println(10000 / x);
  }
}
