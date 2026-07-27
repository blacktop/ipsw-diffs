## fsck_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/fsck_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0x10ec4
+324.160.3.0.0
+  __TEXT.__text: 0x10edc
   __TEXT.__auth_stubs: 0x420
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x34d0
+  __TEXT.__cstring: 0x34fe
   __TEXT.__const: 0x4f5d
   __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__unwind_info: 0x518

   - /usr/lib/libc++.1.dylib
   Functions: 365
   Symbols:   84
-  CStrings:  387
+  CStrings:  388
 
Functions:
~ sub_100001610 : 264 -> 288
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
```
