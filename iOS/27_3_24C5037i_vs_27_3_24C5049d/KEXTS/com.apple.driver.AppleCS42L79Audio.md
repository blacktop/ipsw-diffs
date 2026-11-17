## com.apple.driver.AppleCS42L79Audio

> `com.apple.driver.AppleCS42L79Audio`

```diff

-1010.2.0.0.0
-  __TEXT.__cstring: 0x1fc5
-  __TEXT.__os_log: 0x2951
+1020.2.0.0.0
+  __TEXT.__cstring: 0x2007
+  __TEXT.__os_log: 0x29c5
   __TEXT.__const: 0x3e0
-  __TEXT_EXEC.__text: 0x11054
+  __TEXT_EXEC.__text: 0x11158
   __TEXT_EXEC.__auth_stubs: 0x310
   __DATA.__data: 0xd0
   __DATA.__common: 0x140

   __DATA_CONST.__got: 0x58
   Functions: 381
   Symbols:   0
-  CStrings:  468
+  CStrings:  473
 
Functions:
~ sub_fffffe0008cc525c -> sub_fffffe0008c2e77c : 960 -> 1072
~ sub_fffffe0008cca0c0 -> sub_fffffe0008c33650 : 1884 -> 2032
CStrings:
+ "Setup mic-settling-ms:%u\n"
+ "enableHPMics settling mask:%x delay:%ums"
+ "mic-settling-ms"
+ "mic-settling-ms:%u exceeds max, clamping to %ums"
+ "mic-settling-ms:%u exceeds max, clamping to %ums\n"
```
