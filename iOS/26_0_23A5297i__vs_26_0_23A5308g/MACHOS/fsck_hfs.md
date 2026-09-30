## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-704.0.3.0.0
-  __TEXT.__text: 0x301f0
+704.0.3.0.2
+  __TEXT.__text: 0x30440
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6d18
+  __TEXT.__cstring: 0x6ea5
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x50

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: A899F8C2-49BB-3182-B2B3-CA0EFD001788
+  UUID: 6DDE3827-FA27-30E9-BDA7-91F6DA1BE454
   Functions: 471
   Symbols:   138
-  CStrings:  783
+  CStrings:  789
 
Functions:
~ sub_10000faf8 : 6268 -> 6864
~ sub_100021ecc -> sub_100022120 : 1020 -> 1024
~ sub_1000222c8 -> sub_100022520 : 660 -> 652
CStrings:
+ "hfs_swap_HFSBTInternalNode: invalid record count (0x%04X)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (0x%04X)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (free space record)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (record #%d)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (free space record)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"

```
