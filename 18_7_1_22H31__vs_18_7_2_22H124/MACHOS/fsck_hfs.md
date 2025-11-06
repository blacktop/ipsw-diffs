## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-683.120.3.0.0
-  __TEXT.__text: 0x2ff70
+683.120.3.700.2
+  __TEXT.__text: 0x301a8
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6cab
+  __TEXT.__cstring: 0x6e38
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x50

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: EFB911FF-A1C4-37FA-A8B4-E135379D1001
+  UUID: 066DF17D-043D-3B31-8411-DB6A67765AA7
   Functions: 468
   Symbols:   134
-  CStrings:  780
+  CStrings:  786
 
Functions:
~ sub_10000fa20 : 6308 -> 6880
~ sub_100021d44 -> sub_100021f80 : 1120 -> 1124
~ sub_1000221a4 -> sub_1000223e4 : 664 -> 656
CStrings:
+ "hfs_swap_HFSBTInternalNode: invalid record count (0x%04X)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (0x%04X)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (free space record)\n"
+ "hfs_swap_HFSBTInternalNode: invalid record offset (record #%d)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (free space record)\n"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record offset (record #%d)\n"

```
