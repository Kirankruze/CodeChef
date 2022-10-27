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
		char ch=sc.next().charAt(0);
		if(ch=='b'||ch=='B')
		   System.out.println("BattleShip");
		if(ch=='c'||ch=='C')
		   System.out.println("Cruiser");
		if(ch=='d'||ch=='D')
		   System.out.println("Destroyer");
		if(ch=='f'||ch=='F')
		   System.out.println("Frigate");
		}
		
	}
}
