## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/Contents/Resources/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-751.0.0.0.0
-  __TEXT.__text: 0x34640
+753.41.1.0.0
+  __TEXT.__text: 0x34868
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__const: 0x10b4
-  __TEXT.__cstring: 0x6e74
+  __TEXT.__cstring: 0x6f24
   __TEXT.__unwind_info: 0x690
   __DATA_CONST.__const: 0x378
   __DATA_CONST.__cfstring: 0x40

   - /usr/lib/libSystem.B.dylib
   Functions: 487
   Symbols:   139
-  CStrings:  785
+  CStrings:  790
 
Functions:
~ sub_100007d38 : 296 -> 400
~ sub_100007e60 -> sub_100007ec8 : 160 -> 272
~ sub_100009254 -> sub_10000932c : 1908 -> 1916
~ sub_1000099c8 -> sub_100009aa8 : 1096 -> 1120
~ sub_10001175c -> sub_100011854 : 6912 -> 7060
~ sub_1000193d4 -> sub_100019560 : 1136 -> 1292
CStrings:
+ "%s(%d):  index %u >= numRecords %u\n"
+ "DeleteOffset"
+ "DeleteRecord"
+ "hfs_UNswap_BTNode: initial record at bad offset (0x%04X)\n"
+ "hfs_swap_BTNode: initial record at bad offset (0x%04X)\n"
```
