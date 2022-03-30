# Fresh Java

## Description

Can you get the flag?
Reverse engineer this [Java program](https://artifacts.picoctf.net/c/207/KeygenMe.class).

Decompiled the Java `class` into source code using:

```bash
java -jar cfr_0_115.jar KeygenMe.class > KeygenMe.java

cat KeygenMe.java
```



```java
/* Decompiler 13ms, total 657ms, lines 83 */
import java.util.Scanner;

public class KeygenMe {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.println("Enter key:");
      String var2 = var1.nextLine();
      if (var2.length() != 34) {
         System.out.println("Invalid key");
      } else if (var2.charAt(33) != '}') {
         System.out.println("Invalid key");
      } else if (var2.charAt(32) != '9') {
         System.out.println("Invalid key");
      } else if (var2.charAt(31) != '8') {
         System.out.println("Invalid key");
      } else if (var2.charAt(30) != 'c') {
         System.out.println("Invalid key");
      } else if (var2.charAt(29) != 'a') {
         System.out.println("Invalid key");
      } else if (var2.charAt(28) != 'c') {
         System.out.println("Invalid key");
      } else if (var2.charAt(27) != '8') {
         System.out.println("Invalid key");
      } else if (var2.charAt(26) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(25) != '7') {
         System.out.println("Invalid key");
      } else if (var2.charAt(24) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(23) != 'd') {
         System.out.println("Invalid key");
      } else if (var2.charAt(22) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(21) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(20) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(19) != 'u') {
         System.out.println("Invalid key");
      } else if (var2.charAt(18) != 'q') {
         System.out.println("Invalid key");
      } else if (var2.charAt(17) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(16) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(15) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(14) != 'g') {
         System.out.println("Invalid key");
      } else if (var2.charAt(13) != 'n') {
         System.out.println("Invalid key");
      } else if (var2.charAt(12) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(11) != 'l') {
         System.out.println("Invalid key");
      } else if (var2.charAt(10) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(9) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(8) != '7') {
         System.out.println("Invalid key");
      } else if (var2.charAt(7) != '{') {
         System.out.println("Invalid key");
      } else if (var2.charAt(6) != 'F') {
         System.out.println("Invalid key");
      } else if (var2.charAt(5) != 'T') {
         System.out.println("Invalid key");
      } else if (var2.charAt(4) != 'C') {
         System.out.println("Invalid key");
      } else if (var2.charAt(3) != 'o') {
         System.out.println("Invalid key");
      } else if (var2.charAt(2) != 'c') {
         System.out.println("Invalid key");
      } else if (var2.charAt(1) != 'i') {
         System.out.println("Invalid key");
      } else if (var2.charAt(0) != 'p') {
         System.out.println("Invalid key");
      } else {
         System.out.println("Valid key");
      }
   }
}
```

```bash
grep "charAt" KeygenMe.java | grep -E "'(.*)'" --only-matching | tr -d "[='=]" | tr -d '\n' | rev
picoCTF{700l1ng_r3qu1r3d_738cac89}
```