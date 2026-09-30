## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-677.80.1.0.0
-  __TEXT.__text: 0x30080
+677.82.4.0.0
+  __TEXT.__text: 0x301bc
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x10dc
-  __TEXT.__cstring: 0x6c1c
+  __TEXT.__cstring: 0x6c5c
   __TEXT.__unwind_info: 0x518
   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x50

   - /usr/lib/libSystem.B.dylib
   Functions: 475
   Symbols:   134
-  CStrings:  775
+  CStrings:  776
 
CStrings:
+ "\r Pure HFS Plus"
+ "hfs_swap_HFSPlusBTInternalNode: invalid record count (0x%04X)\n"
- "\rPure HFS Plus"

```
