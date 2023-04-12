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
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		for(int i=0;i<T;i++){
		    int N=sc.nextInt();
		    String[] strNums=new String[4];
		    int[] arr= new int[4];
		    for(int j=0;j<strNums.length;j++){
		        strNums[j]=sc.next();
		        arr[j]=Integer.parseInt(strNums[j]);
		    }
		    int max=arr[0];
		    for(int k=1;k<4;k++){
		        if(max<arr[k]){
		            max=arr[k];
		        }
		    }
		    System.out.println(max);
		}
	}
}
