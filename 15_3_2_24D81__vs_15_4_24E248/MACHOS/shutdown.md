## shutdown

> `/sbin/shutdown`

```diff

-1012.80.2.0.0
-  __TEXT.__text: 0x131c
+1026.100.5.0.0
+  __TEXT.__text: 0x1330
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x509
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__cstring: 0x53f
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x600
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 5744B870-55CF-384F-8D22-8F5723126B57
-  Functions: 10
+  UUID: 30B813FD-06CF-3499-9DB2-097E41528D75
+  Functions: 8
   Symbols:   79
-  CStrings:  60
+  CStrings:  61
 
CStrings:
+ "-hknopqrsu"
+ "usage: shutdown [-] [-h | -r | -s | -k] [-o [-n]] [-q] time [warning-message ...]\n"
+ "warning-message supplied but suppressed with -q"
- "-hknoprsu"
- "usage: shutdown [-] [-h | -r | -s | -k] [-o [-n]] time [warning-message ...]\n"

```
