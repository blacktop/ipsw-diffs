## reboot

> `/sbin/reboot`

```diff

-1012.80.2.0.0
-  __TEXT.__text: 0xa90
+1026.100.5.0.0
+  __TEXT.__text: 0xa60
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x1de
   __TEXT.__oslogstring: 0x3e
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__cfstring: 0x40
   __DATA.__bss: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: F0E21B9E-C094-3872-AB21-7AB1B11AFAD6
-  Functions: 7
+  UUID: 87A82FAC-B698-37A2-BB15-44F1937463E6
+  Functions: 6
   Symbols:   56
   CStrings:  29
 
CStrings:
+ "assertion failure: \"v\" -> %llu"
- "assertion failure: \"v\" -> %lld"

```
