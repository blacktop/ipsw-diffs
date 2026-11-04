## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-753.42.1.0.0
-  __TEXT.__text: 0x3d5d4
+753.60.3.0.0
+  __TEXT.__text: 0x3d7b0
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5fd3
-  __TEXT.__cstring: 0x270a
+  __TEXT.__oslogstring: 0x6062
+  __TEXT.__cstring: 0x2722
   __TEXT.__unwind_info: 0xa48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8

   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  Functions: 677
+  Functions: 678
   Symbols:   646
-  CStrings:  756
+  CStrings:  760
 
Functions:
~ _cat_rename : 1504 -> 1536
~ _hfs_swap_HFSPlusBTInternalNode : 4912 -> 5244
~ _hfs_swap_HFSPlusBTInternalNode.cold.20 : 232 -> 112
~ _hfs_swap_HFSPlusBTInternalNode.cold.21 : 112 -> 232
+ _hfs_swap_HFSPlusBTInternalNode.cold.23
CStrings:
+ "has extra space"
+ "hfs_swap_HFSPlusBTInternalNode: catalog file record #%d has extra space\n"
+ "hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d %s\n"
+ "hfs_swap_HFSPlusBTInternalNode: catalog thread record #%d has extra space\n"
+ "too big"
- "hfs_swap_HFSPlusBTInternalNode: catalog folder record #%d too big\n"
```
