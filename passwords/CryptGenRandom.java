package security;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Random;

public class CryptGenRandom {

	public static void main(String[] args) {

		String[] symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"};
		int length = 10;
		Random random = null;

		try {
			random = SecureRandom.getInstanceStrong();
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}    // as of JDK 8, this should return the strongest algorithm available to the JVM

		StringBuilder sb = new StringBuilder(length);
		for (int i = 0; i < length; i++) {
		    int indexRandom = random.nextInt(symbols.length);
		    sb.append(symbols[indexRandom]);
		}
		String password = sb.toString();
		System.out.println(password);

	}

}
