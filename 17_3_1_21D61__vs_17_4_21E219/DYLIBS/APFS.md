## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x4d1a8
+2236.102.1.0.0
+  __TEXT.__text: 0x4d980
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__const: 0x7f30
-  __TEXT.__cstring: 0xdab6
+  __TEXT.__const: 0x7f50
+  __TEXT.__cstring: 0xdb68
   __TEXT.__oslogstring: 0x911
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__unwind_info: 0x920
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x3e8
-  __AUTH_CONST.__cfstring: 0x1160
+  __DATA_CONST.__const: 0x3f0
+  __AUTH_CONST.__cfstring: 0x1180
   __AUTH_CONST.__auth_got: 0x560
   __DATA.__data: 0x98
   __DATA.__bss: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 792
-  Symbols:   1676
-  CStrings:  1275
+  Functions: 796
+  Symbols:   1685
+  CStrings:  1277
 
Symbols:
+ _io_next_child
+ _kAPFSVolumeNoExplicitContentProtectedKey
+ _physical_store_to_container
+ _trim_time_tracking_check
+ _trim_time_tracking_end
+ _trim_time_tracking_start
- _exchange_with_first_child_of_class
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "2236.102.1"
+ "com.apple.apfs.volume.no_explicit_cprotect"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"
- "2235.80.4.0.1"

```
