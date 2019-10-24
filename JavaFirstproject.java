import java.util.*;
public class HelloWorld {
	public static void main(String[] args) {
		char response;
		do
		{
		System.out.println("欢迎来到购买页面，请进行挑选");
		System.out.println("[1]口香糖");
		System.out.println("[2]巧克力");
		System.out.println("[3]爆米花");
		System.out.println("[4]果汁");
		System.out.println("[5]显示购买总数");
		System.out.println("[6]确认购买");
		System.out.println("[7]退出");
		int i,a=0,b=0,c=0,d=0;
		do 
		{
		Scanner sc=new Scanner(System.in);
		i=sc.nextInt();
		switch(i)
		{
		case 1:System.out.println("您购买了口香糖");
		a++;
		break;
		case 2:System.out.println("您购买了巧克力");
		b++;
		break;
		case 3:System.out.println("您购买了爆米花");
		c++;
		break;
		case 4:System.out.println("您购买了果汁");
		d++;
		break;
		case 5:
		System.out.println("您购买了"+a+"个口香糖");
		System.out.println("您购买了"+b+"个巧克力");
		System.out.println("您购买了"+c+"桶爆米花");
		System.out.println("您购买了"+d+"杯果汁");
		break;
		case 6:System.out.println("您已成功购买");
		break;
		case 7:
		break;
		default:System.out.println("错误输入");
		}
		}while(i !=7);
		System.out.println("成功退出，感谢本次使用");
		System.out.println("是否进入购买页面？（yes/no)");
		Scanner sd=new Scanner(System.in);
		response=sd.next().charAt(0);
		}while (response=='yes');
		
		
		
	}
}