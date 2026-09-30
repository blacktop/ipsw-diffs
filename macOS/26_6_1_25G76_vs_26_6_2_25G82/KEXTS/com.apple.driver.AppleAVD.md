## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

 962.0.0.0.0
-  __TEXT.__os_log: 0x175d0
+  __TEXT.__os_log: 0x1765d
   __TEXT.__cstring: 0x65e3
   __TEXT.__const: 0x9df79
-  __TEXT_EXEC.__text: 0x5106c
+  __TEXT_EXEC.__text: 0x510d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12d4
   __DATA.__common: 0x78

   __DATA_CONST.__kalloc_type: 0x2a80
   __DATA_CONST.__kalloc_var: 0xbe0
   Functions: 1681
-  Symbols:   3836
-  CStrings:  1674
+  Symbols:   3838
+  CStrings:  1676
 
Symbols:
+ __ZZN25AppleAVDFrameParamManager15resetFrameQslotEiiE11_os_log_fmt_0
+ __ZZN25AppleAVDFrameParamManager15resetFrameQslotEiiE11_os_log_fmt_1
Functions:
~ __ZN25AppleAVDFrameParamManager15resetFrameQslotEii : 232 -> 332
CStrings:
+ "AppleAVD: ERROR: %s(): invalid bufIdx %d\n"
+ "AppleAVD: WARNING: %s(): bufIdx %d already AVAILABLE, skipping reset to avoid in-flight underflow\n"
```
