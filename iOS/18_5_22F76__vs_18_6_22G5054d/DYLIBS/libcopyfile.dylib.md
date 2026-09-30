## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-221.122.1.0.0
-  __TEXT.__text: 0x74e8
+224.0.0.0.0
+  __TEXT.__text: 0x7578
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x19c8
+  __TEXT.__cstring: 0x1a10
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 675716DC-E2FE-3850-9BE6-C8D0B0B7C278
+  UUID: CE07F8D2-8444-3894-867A-FDE2526C21A2
   Functions: 37
   Symbols:   188
-  CStrings:  189
+  CStrings:  191
 
Functions:
~ _copyfile_open : 3636 -> 3780
CStrings:
+ "file %s changed behind our feet: %m"
+ "fstat on open fd failed for %s\n: %m"

```
