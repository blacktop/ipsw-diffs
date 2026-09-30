## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

 962.0.0.0.0
-  __TEXT.__os_log: 0x197a6
+  __TEXT.__os_log: 0x19833
   __TEXT.__cstring: 0x7b30
   __TEXT.__const: 0xbdf09
-  __TEXT_EXEC.__text: 0x599e0
+  __TEXT_EXEC.__text: 0x59a44
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12d4
   __DATA.__common: 0x78

   __DATA_CONST.__kalloc_var: 0xd20
   Functions: 2022
   Symbols:   0
-  CStrings:  1711
+  CStrings:  1713
 
Functions:
~ __ZN25AppleAVDFrameParamManager15resetFrameQslotEii : 232 -> 332
CStrings:
+ "AppleAVD: ERROR: %s(): invalid bufIdx %d\n"
+ "AppleAVD: WARNING: %s(): bufIdx %d already AVAILABLE, skipping reset to avoid in-flight underflow\n"
```
