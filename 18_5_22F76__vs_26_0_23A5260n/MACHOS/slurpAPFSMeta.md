## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x371b4
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x9102
+2632.0.15.0.1
+  __TEXT.__text: 0x36e0c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__cstring: 0x9092
   __TEXT.__const: 0x200
-  __TEXT.__unwind_info: 0x688
-  __DATA_CONST.__auth_got: 0x418
+  __TEXT.__unwind_info: 0x678
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x470

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 15C09A02-2176-3F8D-8ABF-ACA8278EE0A0
-  Functions: 520
-  Symbols:   144
-  CStrings:  792
+  UUID: 2C9708A3-13FC-3582-9245-67918DC98D74
+  Functions: 518
+  Symbols:   143
+  CStrings:  790
 
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
- "%s:%d: %s superblock container size %lld greater than device size(s) %lld\n"
- "%s:%d: %s tier2 device superblock doesn't agree with main superblock\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid, tier2=%d\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"

```
