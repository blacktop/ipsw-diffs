## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0x58c30
+2811.100.177.0.1
+  __TEXT.__text: 0x58ff0
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0xc50
-  __TEXT.__cstring: 0x11c5b
-  __TEXT.__gcc_except_tab: 0x628
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__const: 0xc00
+  __TEXT.__cstring: 0x11fb0
+  __TEXT.__gcc_except_tab: 0x62c
+  __TEXT.__unwind_info: 0xbf0
   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__cfstring: 0xb20
-  __DATA.__data: 0x378
-  __DATA.__bss: 0x64
-  __DATA.__common: 0xf8c
+  __DATA_CONST.__cfstring: 0xba0
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x78
+  __DATA.__common: 0xfac
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 84ACC6AB-1523-3BD6-BD9B-DD1A4F9E1A2E
-  Functions: 854
-  Symbols:   184
-  CStrings:  1684
+  UUID: 48891BD1-53C2-31A2-9295-BB23187C0A17
+  Functions: 868
+  Symbols:   185
+  CStrings:  1706
 
Symbols:
+ __include_codes_in_dsym
CStrings:
+ "         Evicted by alloc   : %16llu\t(~%8llu MB)\n"
+ "         Hits               : %16llu\t(~%8llu MB)\n"
+ "         Misses             : %16llu\t(~%8llu MB)\n"
+ "         Size max           : %16llu\t(~%8llu MB)\n"
+ "         oc_dirty_count     : %16llu\t(~%8llu MB)\n"
+ "         oc_free_count      : %16llu\t(~%8llu MB)\n"
+ "         oc_phys_dirty_count: %16llu\t(~%8llu MB)\n"
+ "         oc_phys_free_count : %16llu\t(~%8llu MB)\n"
+ "%@addcg_t=%llu "
+ "%@findcg_t=%llu "
+ "%@num_cg=%zu "
+ "%@snap_t=%llu "
+ "%s container load for %s\n"
+ "%s:%d: %s rapid-aged %llu inodes\n"
+ "%s:%u Err: APFS_IOUC_LOCK_UNLOCK_CONTAINER_LOAD failed with status: %x, %u\n"
+ "%s:%u Err: apfs_container_iouc (%s) failed with status: 0x%x, %u\n"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/fscommon/purging.c"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj.c"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj_snap.c"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/obj.c"
+ "2811.100.177.0.1"
+ "Locking"
+ "Metadata Size (estimated)   : %16llu\t(~%8llu MB)\n"
+ "ObjCache Size current       : %16llu\t(~%8llu MB)\n"
+ "Object Cache usage"
+ "Object Cache usage\n"
+ "Trying to update a namedstream inode %llx on volume %s\n"
+ "Unlocking"
+ "ino_set_rage"
+ "lock_unlock_container_load"
+ "lookup_jobj_ext"
- "%s:%d: %s btree_node_insert_internal failed: %d\n"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "%s:%u Err: apfs_container_iouc (%s) failed with status: %x, %u\n"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/fscommon/purging.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "2632.80.1.0.1"
- "btree_node_compact"
- "btree_node_copy"
- "fd_dev_hint_flush"
- "lookup_jobj_in_snap"

```
