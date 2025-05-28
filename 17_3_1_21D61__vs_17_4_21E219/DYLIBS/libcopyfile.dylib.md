## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-196.0.0.0.0
-  __TEXT.__text: 0x67b0
+196.100.4.0.0
+  __TEXT.__text: 0x6910
   __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x16d8
+  __TEXT.__cstring: 0x1751
   __TEXT.__unwind_info: 0xcc
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0

   - /usr/lib/system/libxpc.dylib
   Functions: 35
   Symbols:   180
-  CStrings:  172
+  CStrings:  175
 
CStrings:
+ "file type (%u) does not match expected %u on %s\n: %m"
+ "missing FTS entry during recursive copy\n: %m"
+ "repeat stat on %s\n: %m"

```
