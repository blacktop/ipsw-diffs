## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-753.42.1.0.0
-  __TEXT.__text: 0x34c08
+753.60.3.0.0
+  __TEXT.__text: 0x34c94
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x10b4
-  __TEXT.__cstring: 0x6f24
+  __TEXT.__cstring: 0x6fcb
   __TEXT.__unwind_info: 0x688
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x40

   - /usr/lib/libSystem.B.dylib
   Functions: 485
   Symbols:   138
-  CStrings:  790
+  CStrings:  794
 
Functions:
~ sub_100011abc : 7060 -> 7200
CStrings:
+ "has extra space"
+ "hfs_swap_HFSPlusBTInternalNode: catalog file record #%d has extra space\n"
+ "hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d %s\n"
+ "hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d has extra space\n"
+ "too big"
- "hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d too big\n"
```
