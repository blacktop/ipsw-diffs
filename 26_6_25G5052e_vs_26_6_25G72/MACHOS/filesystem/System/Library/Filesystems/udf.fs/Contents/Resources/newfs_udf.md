## newfs_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/newfs_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0x1216c
+324.160.3.0.0
+  __TEXT.__text: 0x12184
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x658
   __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__cstring: 0x38c8
+  __TEXT.__cstring: 0x38f6
   __TEXT.__unwind_info: 0x540
   __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0x78

   - /usr/lib/libutil.dylib
   Functions: 344
   Symbols:   115
-  CStrings:  328
+  CStrings:  329
 
Functions:
~ sub_100000c30 : 264 -> 288
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
```
