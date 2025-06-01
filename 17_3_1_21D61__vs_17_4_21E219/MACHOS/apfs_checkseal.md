## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x4bf8c
+2236.102.1.0.0
+  __TEXT.__text: 0x4c6c8
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x3c0
-  __TEXT.__cstring: 0xfcc2
-  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__cstring: 0xfd78
+  __TEXT.__unwind_info: 0x8cc
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x10

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 35209B1B-8871-3AA4-B739-DA87C627F777
-  Functions: 715
+  UUID: 272ECE20-CC1E-3650-9E54-F7FE78A94766
+  Functions: 719
   Symbols:   125
-  CStrings:  1284
+  CStrings:  1286
 
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "invalid offset (%llu) for last fext lookup\n"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"

```
