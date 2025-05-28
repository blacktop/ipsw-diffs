## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x4d7d0
+2236.102.1.0.0
+  __TEXT.__text: 0x4de54
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0xf4d3
-  __TEXT.__const: 0x7e40
-  __TEXT.__unwind_info: 0x820
+  __TEXT.__cstring: 0xf58d
+  __TEXT.__const: 0x7e70
+  __TEXT.__unwind_info: 0x824
   __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 694
+  Functions: 696
   Symbols:   143
-  CStrings:  1279
+  CStrings:  1281
 
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "%s:%d: cannot change role of system-unique volume\n"
+ "%s:%d: cannot change role of xART volume\n"
+ "2236.102.1"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"
- "%s:%d: Cannot change role of xART volume\n"
- "2235.80.4.0.1"

```
