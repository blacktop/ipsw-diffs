## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x43c38
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xce7e
+2632.0.15.0.1
+  __TEXT.__text: 0x43410
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__cstring: 0xcd6a
   __TEXT.__const: 0x218
-  __TEXT.__unwind_info: 0x700
-  __DATA_CONST.__auth_got: 0x390
+  __TEXT.__unwind_info: 0x6e0
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x6f8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: CF52D853-8AB4-3A97-A26F-05EEFA3C4153
-  Functions: 576
-  Symbols:   128
-  CStrings:  1065
+  UUID: 8C0FF80D-6825-39E9-9312-E62575AF05D0
+  Functions: 573
+  Symbols:   127
+  CStrings:  1060
 
Symbols:
- _uuid_is_null
CStrings:
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "apfs-clonegroup-lock-mutex"
+ "authapfs_validate_node"
+ "nx_reaper_add_ext"
- "%s:%d: %s container block size too small for tier2 device block size (%d < %d)\n"
- "%s:%d: %s couldn't read tier2 device superblock of size %d\n"
- "%s:%d: %s failed to set tier2 device: %d\n"
- "%s:%d: %s failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s superblock container size %lld greater than device size(s) %lld\n"
- "%s:%d: %s tier2 device superblock doesn't agree with main superblock\n"
- "%s:%d: %s xid %lld failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid, tier2=%d\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
