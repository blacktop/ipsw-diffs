## libETLDLFDynamic.dylib

> `/usr/lib/libETLDLFDynamic.dylib`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x260
-  __TEXT.__auth_stubs: 0x20
+1218.0.0.0.0
+  __TEXT.__text: 0x2bc
+  __TEXT.__auth_stubs: 0x30
+  __TEXT.__cstring: 0x52
   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x18
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libSystem.B.dylib
   Functions: 3
-  Symbols:   7
-  CStrings:  0
+  Symbols:   8
+  CStrings:  3
 
Symbols:
+ __ETLDebugPrint
CStrings:
+ "ETLDLFParse"
+ "Length %u not enough, need %zu\n"
+ "Length %u not whole payload, need %u\n"

```
