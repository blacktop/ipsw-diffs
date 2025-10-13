## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-704.40.4.0.0
-  __TEXT.__text: 0x30440
+704.40.4.0.1
+  __TEXT.__text: 0x3022c
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6ea5
+  __TEXT.__cstring: 0x6e13
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x50

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 45F42520-8C0A-3BD3-912F-A74CA64BEA8B
+  UUID: B5EC59B4-DD60-321C-B627-A7F45A137274
   Functions: 471
   Symbols:   138
-  CStrings:  789
+  CStrings:  787
 
Functions:
~ sub_10000faf8 : 6864 -> 6332
CStrings:
+ "hfs_swap_HFSPlusBTInternalNode: invalid free space offset (%X)\n"
- "hfs_swap_HFSBTInternalNode: invalid record offset (free space record)\n"
- "hfs_swap_HFSBTInternalNode: invalid record offset (record #%d)\n"
- "hfs_swap_HFSPlusBTInternalNode: invalid record offset (free space record)\n"

```
