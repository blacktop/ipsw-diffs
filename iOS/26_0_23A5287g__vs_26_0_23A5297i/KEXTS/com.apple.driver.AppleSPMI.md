## com.apple.driver.AppleSPMI

> `com.apple.driver.AppleSPMI`

```diff

-113.0.1.0.0
-  __TEXT.__cstring: 0x1be1
-  __TEXT.__os_log: 0xb16
+113.0.2.0.0
+  __TEXT.__cstring: 0x1c13
+  __TEXT.__os_log: 0xb39
   __TEXT.__const: 0xf8
-  __TEXT_EXEC.__text: 0xa2c0
+  __TEXT_EXEC.__text: 0xa390
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x18d8
   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0x230
-  UUID: FAC1B172-99C0-3108-B110-FCC9676532A7
+  UUID: 188CAB83-73EB-38FD-9EC9-05E1F0512248
   Functions: 180
   Symbols:   0
-  CStrings:  303
+  CStrings:  306
 
Functions:
~ __ZN19AppleSPMIController14dumpFaultQueueEPcmb : 448 -> 656
CStrings:
+ "[%s]:%s:%d:[error] fault - 0x%08X\n"
+ "dumpFaultQueue"

```
