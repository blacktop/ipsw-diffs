## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-753.60.3.0.0
-  __TEXT.__text: 0x3d7b0
-  __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x6062
-  __TEXT.__cstring: 0x2722
-  __TEXT.__unwind_info: 0xa48
+753.60.5.0.0
+  __TEXT.__text: 0x3deb0
+  __TEXT.__const: 0x4e70
+  __TEXT.__oslogstring: 0x618c
+  __TEXT.__cstring: 0x2743
+  __TEXT.__unwind_info: 0xa50
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0

   - /usr/lib/libSystem.B.dylib
   Functions: 678
   Symbols:   646
-  CStrings:  760
+  CStrings:  766
 
Functions:
~ _BTIterateRecord : 1392 -> 1864
~ _BTIterateRecords : 1432 -> 2144
~ _BTReloadData : 196 -> 244
~ _builddesc : 296 -> 304
~ _ExtendBTree : 868 -> 884
~ _hfs_swap_BTNode : 3444 -> 3696
~ _FindExtentRecord : 488 -> 708
~ _InsertKeyRecord : 420 -> 484
CStrings:
+ "%s() found mismatched sibling node on volume %s: found kind=%d, height=%u; expected kind=%d, height=%u\n"
+ "BTIterateRecord"
+ "BTIterateRecords"
+ "FindExtentRecord: invalid extent (startBlock %u, blockCount %u, totalBlocks %u)\n"
+ "hfs_swap_BTNode: header node has %d records, should be 3\n"
+ "hfs_swap_BTNode: map node has %d records, should be 1\n"
```
