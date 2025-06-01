## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x493e4
+2236.102.1.0.0
+  __TEXT.__text: 0x49a88
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xf3b6
+  __TEXT.__cstring: 0xf43d
   __TEXT.__const: 0xf8
-  __TEXT.__unwind_info: 0x81c
+  __TEXT.__unwind_info: 0x820
   __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: A8009DF1-238A-3138-8C49-B062B74BB4FD
-  Functions: 658
+  UUID: 46B159CD-FEE9-3131-91D8-5C86C0DD2CAC
+  Functions: 660
   Symbols:   128
-  CStrings:  1256
+  CStrings:  1257
 
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "2236.102.1"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"
- "2235.80.4.0.1"

```
