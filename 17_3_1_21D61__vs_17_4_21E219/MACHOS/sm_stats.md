## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x40204
+2236.102.1.0.0
+  __TEXT.__text: 0x40990
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__cstring: 0xca87
+  __TEXT.__cstring: 0xcb11
   __TEXT.__const: 0x100
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x6e4
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x4f8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 557
+  Functions: 560
   Symbols:   116
-  CStrings:  1034
+  CStrings:  1035
 
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"

```
