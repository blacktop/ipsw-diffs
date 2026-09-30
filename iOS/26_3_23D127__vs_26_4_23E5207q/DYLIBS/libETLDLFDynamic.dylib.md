## libETLDLFDynamic.dylib

> `/usr/lib/libETLDLFDynamic.dylib`

```diff

-1399.9.0.0.0
-  __TEXT.__text: 0x224
-  __TEXT.__auth_stubs: 0x20
+1416.1.0.0.0
+  __TEXT.__text: 0x25c
+  __TEXT.__auth_stubs: 0x30
+  __TEXT.__cstring: 0x52
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x18
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: DDBDF882-33F0-3373-8026-A1948F7078E2
+  UUID: E5105657-3629-3572-A459-BB360D0455E1
   Functions: 2
-  Symbols:   7
-  CStrings:  0
+  Symbols:   8
+  CStrings:  3
 
Symbols:
+ __ETLDebugPrint
Functions:
~ _ETLDLFParse : 160 -> 216
CStrings:
+ "ETLDLFParse"
+ "Length %u not enough, need %zu\n"
+ "Length %u not whole payload, need %u\n"

```
