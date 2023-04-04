/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc= new Scanner(System.in);
	    int T=sc.nextInt();
		for(int i=0;i<T;i++){
		   int j=sc.nextInt();
		   int rem,count=0;
		   while(j>0){
		       rem=j%10;
		       if(rem==4)
		         count+=1;
		       j=j/10;
		   }
		   System.out.println(count);
		}
		
	}
}
