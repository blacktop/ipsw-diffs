## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0x4f3b8
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__const: 0x510
-  __TEXT.__cstring: 0xff23
+2811.100.177.0.1
+  __TEXT.__text: 0x4ece4
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0xff10
   __TEXT.__unwind_info: 0x8c0
-  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160
-  __DATA.__data: 0x368
+  __DATA.__data: 0x360
   __DATA.__common: 0x414
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 15440B4D-00C9-350E-B7CD-DBE480E69D11
-  Functions: 724
-  Symbols:   131
-  CStrings:  1300
+  UUID: EFC64B42-E9E7-3EE3-8E2C-42F7BC453627
+  Functions: 729
+  Symbols:   133
+  CStrings:  1296
 
Symbols:
+ ___memcpy_chk
+ __include_codes_in_dsym
CStrings:
+ "%s:%d: %s rapid-aged %llu inodes\n"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj.c"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/jobj_snap.c"
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/obj.c"
+ "ino_set_rage"
+ "lookup_jobj_ext"
- "%s:%d: %s btree_node_insert_internal failed: %d\n"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/jobj_snap.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "btree_node_compact"
- "btree_node_copy"
- "fd_dev_hint_flush"
- "lookup_jobj_in_snap"

```
