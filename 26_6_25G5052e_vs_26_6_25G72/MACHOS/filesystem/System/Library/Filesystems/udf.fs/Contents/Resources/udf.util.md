## udf.util

> `/System/Library/Filesystems/udf.fs/Contents/Resources/udf.util`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0xa07c
+324.160.3.0.0
+  __TEXT.__text: 0xa094
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__cstring: 0xf78
+  __TEXT.__cstring: 0xfa6
   __TEXT.__gcc_except_tab: 0x328
   __TEXT.__const: 0x564
   __TEXT.__unwind_info: 0x3f0

   - /usr/lib/libc++.1.dylib
   Functions: 255
   Symbols:   70
-  CStrings:  135
+  CStrings:  136
 
Functions:
~ sub_100001254 : 264 -> 288
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
```
