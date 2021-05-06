package day03;

public class T01_OopTest {
	public static void main(String[] args) {
		T01_Human hum = new T01_Human();
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
		hum.mantang();
		hum.goHakwon();
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
	}
}
