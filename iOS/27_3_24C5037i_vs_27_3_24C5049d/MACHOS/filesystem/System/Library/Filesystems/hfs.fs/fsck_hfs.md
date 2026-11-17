## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-753.60.3.0.0
-  __TEXT.__text: 0x34c94
+753.60.5.0.0
+  __TEXT.__text: 0x34e64
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x10b4
-  __TEXT.__cstring: 0x6fcb
+  __TEXT.__cstring: 0x703c
   __TEXT.__unwind_info: 0x688
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x40

   - /usr/lib/libSystem.B.dylib
   Functions: 485
   Symbols:   138
-  CStrings:  794
+  CStrings:  796
 
Functions:
~ sub_100005c78 : 1132 -> 1232
~ sub_100006c38 -> sub_100006c9c : 904 -> 928
~ sub_100011abc -> sub_100011b38 : 7200 -> 7404
~ sub_100015f60 -> sub_1000160a8 : 692 -> 828
CStrings:
+ "hfs_swap_BTNode: header node has %d records, should be 3\n"
+ "hfs_swap_BTNode: map node has %d records, should be 1\n"
```
