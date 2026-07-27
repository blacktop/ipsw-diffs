## mount_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/mount_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0x9df8
+324.160.3.0.0
+  __TEXT.__text: 0x9e10
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__cstring: 0x1064
+  __TEXT.__cstring: 0x1092
   __TEXT.__gcc_except_tab: 0x304
   __TEXT.__const: 0x564
   __TEXT.__unwind_info: 0x3d0

   - /usr/lib/libutil.dylib
   Functions: 247
   Symbols:   78
-  CStrings:  148
+  CStrings:  149
 
Functions:
~ sub_10000124c : 264 -> 288
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
```
