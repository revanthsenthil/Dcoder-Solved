/*

Problem Statement
Print the word Dco...oder

Input
A positive integer n

Output
Print the word: Dco..oder(letter o must be repeted n times)

Constraints
0<n<50

Sample Input
5

Sample Output

Dcoooooder

*/

import java.util.Scanner;

//Compiler version JDK 11.0.2

class Dcoder
{  
  public static void main(String args[])
  {
    Scanner scan = new Scanner(System.in);
    int x = scan.nextInt();
    System.out.print("Dc");
    String rep = "o";
    String no = rep.repeat(x);
    System.out.print(no);
    System.out.println("der");
  }
}
