/* HelloWorld.java
 */

import javax.validation.constraints.NotNull;

const jwt = require('jsonwebtoken');

jwt.sign(payload, key, { algorithm: 'none' }); // Noncompliant

public class HelloWorld
{
	public static void main(String[] args) {
		System.out.println("Hello World!");
		System.out.println("Hello again World!");
	}
}
