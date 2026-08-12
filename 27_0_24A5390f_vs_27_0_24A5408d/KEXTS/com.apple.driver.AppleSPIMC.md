## com.apple.driver.AppleSPIMC

> `com.apple.driver.AppleSPIMC`

```diff

-39.0.0.0.0
+39.0.0.0.1
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1757
-  __TEXT_EXEC.__text: 0x7000
+  __TEXT.__cstring: 0x1777
+  __TEXT_EXEC.__text: 0x7040
   __TEXT_EXEC.__auth_stubs: 0x250
   __DATA.__data: 0xc4
   __DATA.__common: 0x68

   __DATA_CONST.__got: 0x50
   Functions: 131
   Symbols:   0
-  CStrings:  165
+  CStrings:  166
 
Functions:
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand : 3912 -> 3976
CStrings:
+ "%s %s:%d: transaction timeout!\n"
```
