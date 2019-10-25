import java.util.*;
public class HelloWorld {
	public static void main(String[] args) {
		char response;
		do
		{
		System.out.println("Please input a x coordinate");
		Scanner sc=new Scanner(System.in);
		int x;
		x=sc.nextInt();
		System.out.println("Please input a y coordiante");
		int y;
		y=sc.nextInt();
		if (x==0)
		{
			if(y==0)
			{
				System.out.println("("+x+","+y+") is the origin");
			}
			else
			{
				System.out.println("("+x+","+y+") is on the y-aixs");
			}
		}
		else
		{
			if(x>0)
			{
				if(y==0)
				{
					System.out.println("("+x+","+y+") is on the x-aixs");
				}
				else
				{
					if(y>0)
					{
						System.out.println("("+x+","+y+") is in the first quadrant");
					}
					else
					{
						System.out.println("("+x+","+y+") is in the fourth quadrant");
					}
				}
			}
			else
			{
				if(y==0)
				{
					System.out.println("("+x+","+y+") is on the x-aixs");
				}
				else
				{
					if(y>0)
					{
						System.out.println("("+x+","+y+") is in the second quadrant");
					}
					else 
					{
						System.out.println("("+x+","+y+") is in the third quadrant");
					}
				}
			}
		}
		System.out.println("Try again? (y/n)");
		response=sc.next().charAt(0);
		}while(response=='y');
	}
}