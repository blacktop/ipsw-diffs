## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-260.0.3.0.0
-  __TEXT.__text: 0x7f20
+260.40.4.0.0
+  __TEXT.__text: 0x7f48
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x1c51
+  __TEXT.__cstring: 0x1c7e
   __TEXT.__unwind_info: 0x100
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3b0

   - /usr/lib/system/libxpc.dylib
   Functions: 43
   Symbols:   169
-  CStrings:  203
+  CStrings:  204
 
Functions:
~ _copyfile_internal : 7968 -> 7908
~ _copyfile_pack : 4580 -> 4680
CStrings:
+ "skipping attr \"%s\" due to fetch error %d: %m"
```
