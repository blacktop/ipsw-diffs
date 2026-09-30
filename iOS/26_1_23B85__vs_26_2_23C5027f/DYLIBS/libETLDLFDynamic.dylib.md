## libETLDLFDynamic.dylib

> `/usr/lib/libETLDLFDynamic.dylib`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x224
-  __TEXT.__auth_stubs: 0x20
+1399.2.0.0.0
+  __TEXT.__text: 0x298
+  __TEXT.__auth_stubs: 0x30
+  __TEXT.__cstring: 0x52
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x18
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: DAD9DD2B-26A4-39C4-80C3-A84FD8A88FD8
+  UUID: A0F8CA87-D207-3CE1-ADFB-9F530A202E86
   Functions: 2
-  Symbols:   7
-  CStrings:  0
+  Symbols:   8
+  CStrings:  3
 
Symbols:
+ __ETLDebugPrint
Functions:
~ _ETLDLFParse : 160 -> 276
CStrings:
+ "ETLDLFParse"
+ "Length %u not enough, need %zu\n"
+ "Length %u not whole payload, need %u\n"

```
