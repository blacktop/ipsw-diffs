## libETLDLFDynamic.dylib

> `/usr/lib/libETLDLFDynamic.dylib`

```diff

-1391.0.0.0.0
-  __TEXT.__text: 0x224
-  __TEXT.__auth_stubs: 0x20
+1397.0.0.0.0
+  __TEXT.__text: 0x298
+  __TEXT.__auth_stubs: 0x30
+  __TEXT.__cstring: 0x52
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x18
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: EDEFD433-E1C4-36FD-BDBF-3EE104A1BAE9
+  UUID: A91691EE-4FEB-3524-BCB1-0A6F8CFA9348
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
