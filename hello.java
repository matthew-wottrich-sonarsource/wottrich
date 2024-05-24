/* HelloWorld.java
 */

import javax.validation.constraints.NotNull;

const jwt = require('jsonwebtoken');

jwt.sign(payload, key, { algorithm: 'none' }); // Noncompliant

const jwt = require('jsonwebtoken');

jwt.verify(token, key, {
    expiresIn: 360000,
    algorithms: ['none'] // Noncompliant
}, callbackcheck);

public class HelloWorld
{
	public static void main(String[] args) {
		System.out.println("Hello World!");
		System.out.println("Hello again World!");
	}
}
