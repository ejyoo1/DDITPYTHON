package day03;

public class T01_Animal {
	int fullness = 0; // 배부른 정도
	
	public void eat() { // 한번 먹을 때
		fullness++;
	}
	
	public void mantang() { // 많이 먹을때
		fullness = 10;
	}
}
