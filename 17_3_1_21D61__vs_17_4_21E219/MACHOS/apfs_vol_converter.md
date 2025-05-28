## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x534e8
-  __TEXT.__auth_stubs: 0x960
+2236.102.1.0.0
+  __TEXT.__text: 0x53c6c
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x113ac
+  __TEXT.__cstring: 0x11437
   __TEXT.__const: 0x168
   __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__unwind_info: 0xb64
+  __TEXT.__unwind_info: 0xb70
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x800

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 828
-  Symbols:   174
-  CStrings:  1550
+  Functions: 833
+  Symbols:   173
+  CStrings:  1551
 
Symbols:
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "2236.102.1"
+ "ino_phys_size_ext"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"
- "2235.80.4.0.1"
- "ino_phys_size"

```
