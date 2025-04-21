## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-220.0.0.0.0
-  __TEXT.__text: 0x74e8
+220.0.0.0.1
+  __TEXT.__text: 0x7578
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x19c8
+  __TEXT.__cstring: 0x1a10
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0

   - /usr/lib/system/libxpc.dylib
   Functions: 37
   Symbols:   188
-  CStrings:  189
+  CStrings:  191
 
Symbols:
+ _freadlink
- _readlink
CStrings:
+ "file %s changed behind our feet: %m"
+ "fstat on open fd failed for %s\n: %m"

```
