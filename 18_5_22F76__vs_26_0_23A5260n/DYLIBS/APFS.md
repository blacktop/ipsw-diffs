## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x4fd90
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__const: 0x8080
-  __TEXT.__cstring: 0xde94
-  __TEXT.__oslogstring: 0xa81
+2632.0.15.0.1
+  __TEXT.__text: 0x4fd54
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__const: 0x8410
+  __TEXT.__cstring: 0xddcd
+  __TEXT.__oslogstring: 0xac7
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x930
+  __TEXT.__unwind_info: 0x918
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x4e0
-  __AUTH_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__const: 0x4e8
+  __AUTH_CONST.__auth_got: 0x5a8
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__cfstring: 0x1160
   __DATA.__data: 0x98
   __DATA.__bss: 0x40
   __DATA.__common: 0x418

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: A1693824-811C-3E56-BAB2-DC73632D7116
-  Functions: 797
-  Symbols:   1746
-  CStrings:  1445
+  UUID: B4A39A41-1334-361F-8923-A0F130F2B172
+  Functions: 807
+  Symbols:   1758
+  CStrings:  1441
 
Symbols:
+ _APFSContainerResizePrepare
+ _APFSContainerResizePrepare.cold.1
+ _APFSContainerWaitForReaper
+ _APFSVolumeCacheKey
+ _APFSVolumeDeleteOtiLockerData
+ _APFSVolumeEvictOtiLocker
+ _APFSVolumeGetOtiLockerData
+ _APFSVolumeListOtiLockerData
+ _APFSVolumePurgeOtiLocker
+ _APFSVolumeSetOtiLockerData
+ _APFSVolumeVerifyKey
+ _CFUUIDGetUUIDBytes
+ _OUTLINED_FUNCTION_9
+ __APFSVolumeCacheVerifyKey
+ __APFSVolumeOtiRequestHelper
+ __apfs_calloc_typed
+ __apfs_malloc_typed
+ _authapfs_hash_comparison_size
+ _kAPFSVolumeUUIDKey
+ _nx_reaper_add_ext
+ _spaceman_free_handle_entitled_reserve
+ _spaceman_info
- __apfs_malloc
- _apfs_check_for_spillover
- _authapfs_hash_size
- _dev_set_tier2_device
- _fusion_mt_key_cmp
- _nx_fusion_superblock_write
- _nx_obj_cache_reset
- _obj_cache_stats_init
- _physical_store_get_tier
- _spaceman_size_info
CStrings:
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: APFS_IOUC_CONTAINER_RESIZE_PREPARE for %s %lld failed with %d\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "2632.0.15.0.1"
+ "61706673-7575-6964-0300-766f6c756d00"
+ "APFSContainerResizePrepare"
+ "apfs-clonegroup-lock-mutex"
+ "authapfs_validate_node"
+ "com.apple.apfs.volume.volume_uuid"
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
- "2332.120.31.0.2"
- "Secondary"
- "TierType"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
