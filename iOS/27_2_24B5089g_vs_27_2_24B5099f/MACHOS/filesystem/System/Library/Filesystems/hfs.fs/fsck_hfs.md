## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-753.40.3.0.0
-  __TEXT.__text: 0x34a70
+753.40.4.0.0
+  __TEXT.__text: 0x34c08
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x10b4
-  __TEXT.__cstring: 0x6e74
+  __TEXT.__cstring: 0x6f24
   __TEXT.__unwind_info: 0x688
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x40

   - /usr/lib/libSystem.B.dylib
   Functions: 485
   Symbols:   138
-  CStrings:  785
+  CStrings:  790
 
Functions:
~ sub_100007e38 : 296 -> 400
~ sub_100007f60 -> sub_100007fc8 : 160 -> 276
~ sub_10000934c -> sub_100009428 : 1908 -> 1916
~ sub_100009ac0 -> sub_100009ba4 : 1088 -> 1120
~ sub_1000119b8 -> sub_100011abc : 6912 -> 7060
CStrings:
+ "%s(%d):  index %u >= numRecords %u\n"
+ "DeleteOffset"
+ "DeleteRecord"
+ "hfs_UNswap_BTNode: initial record at bad offset (0x%04X)\n"
+ "hfs_swap_BTNode: initial record at bad offset (0x%04X)\n"
```
