## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-683.100.9.0.0
-  __TEXT.__text: 0x2feb4
+683.120.3.0.0
+  __TEXT.__text: 0x2ff70
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6c5c
+  __TEXT.__cstring: 0x6cab
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x50

   - /usr/lib/libSystem.B.dylib
   Functions: 468
   Symbols:   134
-  CStrings:  776
+  CStrings:  778
 
CStrings:
+ "\tInvalid block size block_list_header\n"
+ "%s: jnl: %s: open: bad jhdr size (%d) \n"

```
