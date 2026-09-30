## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2317.60.14.0.2
-  __TEXT.__text: 0x4f544
+2317.60.21.0.1
+  __TEXT.__text: 0x4f534
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x1000d
+  __TEXT.__const: 0x4f8
+  __TEXT.__cstring: 0x1001d
   __TEXT.__unwind_info: 0x8e8
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__const: 0x758
   __DATA_CONST.__cfstring: 0x160
   __DATA.__data: 0x358
   __DATA.__common: 0x414

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 728
+  Functions: 730
   Symbols:   125
-  CStrings:  1291
+  CStrings:  1292
 
CStrings:
+ "SNAP_DELETE_TXN"

```
