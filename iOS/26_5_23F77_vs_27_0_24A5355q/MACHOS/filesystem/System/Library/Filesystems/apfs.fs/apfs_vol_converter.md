## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x59010 sha256:9885e53a7a20e661273246c4c3398d93c5aaff43ae89def2a9b2ac0a86db3324
-  __TEXT.__auth_stubs: 0x9f0 sha256:b389c9ca85047bce21a2c73349b99c5aace4935b44885dcd8c30e23bd40d14e9
-  __TEXT.__init_offsets: 0x4 sha256:3dfcf19c21498207de5db2ed73e90f28942f67736592d23b29be53f6c8223f4f
-  __TEXT.__const: 0xc00 sha256:e5bb149046273072ec5d8319e9413aebddcd72bf79ff75a87b85b097578272e9
-  __TEXT.__cstring: 0x11f43 sha256:e9e442e7dc8d031126121839905786a266d5599c0fb6d10acf05d15856b1bd83
-  __TEXT.__gcc_except_tab: 0x63c sha256:bfab7356bf5007082bf4882bcb246d8d166b9daf15b6a6384791204cc15abd86
-  __TEXT.__unwind_info: 0xbe8 sha256:29981e7b68ca5af4e6328a26ceca082bc4542c7b391a1cc4f1b32cd9affb5a3f
-  __DATA_CONST.__auth_got: 0x500 sha256:10218593b4b98b5b5865e7c050f286958c0842b2f31dc7e88df46b9357622ee4
-  __DATA_CONST.__got: 0x78 sha256:ee4f1811f325e3a3f3ab00fcb9aee09c81143b92c3fdd7fadd371e438804fe6d
-  __DATA_CONST.__auth_ptr: 0x20 sha256:f4469dffdf815b6b84e89ba0d06831dda81758ba07381e9e9e37ba7ebf072d68
-  __DATA_CONST.__const: 0xb20 sha256:a624229888962d361cfdf41d3502b4c0818703881692519e9f04f8cbc0413eff
-  __DATA_CONST.__cfstring: 0xb40 sha256:60ed4631c80b123d4449ab00b28d5958ee068971830a7417da6793d07ad82bb4
-  __DATA.__data: 0x370 sha256:8b7ab1655c1f6339d5edf7b64c13be9894f3fa0f14c81beac0623f4e112a3e41
+3277.0.0.0.1
+  __TEXT.__text: 0x5937c sha256:8649be64c84922706dc0b542f508c01aa74db99eac7f86ca8001999e3613d68b
+  __TEXT.__auth_stubs: 0x9f0 sha256:e479dde7e38838502e609b5e606b245df673e38877a0f33ee93a772ff415fd5c
+  __TEXT.__init_offsets: 0x4 sha256:24234ce5910e081b7258f4287718e099d9bdba1857dbdc5cbe513bc60cafcd54
+  __TEXT.__const: 0x750 sha256:39a113fc3c931a1ba43d60f2b856fd973ea5f56c3149ea288d2b0652e4b01994
+  __TEXT.__cstring: 0x11e39 sha256:97bc445e9ad6227f1a18952eede7912c94cfcd95075d75b01d6ccd20ae3432ea
+  __TEXT.__gcc_except_tab: 0x64c sha256:5c2bd14040d01dc4c07f5e134482485f73ec80a93cf9058561c5a2319d5ccb3b
+  __TEXT.__unwind_info: 0xc40 sha256:d73e63f62f7bcf95a3ab5661c08ee33309c3293ed8a9b85a6e1fccbc58522a25
+  __DATA_CONST.__const: 0xb20 sha256:4b53b4f38a2f4195fcf3c8277a49ee8ec9fa54a02a8234405e53b1314e4deabf
+  __DATA_CONST.__cfstring: 0xb40 sha256:7dae592c9520640ae7290e4fa7b053ee56a50f6db97a00d8809aae8891cf7207
+  __DATA_CONST.__auth_got: 0x500 sha256:816c90aa6596b5b98e42bdbf7709944cbd7815834bca45a20468d6870087b4c9
+  __DATA_CONST.__got: 0x78 sha256:d40d5470c3cd18302118352b2bf9439e0f250816dbeb73239ab498478fd9e03c
+  __DATA_CONST.__auth_ptr: 0x20 sha256:7a88e49dcc56c8fc57c67b594f799f94b17851d1dc809739bdebf4ab770d3cfe
+  __DATA.__data: 0x370 sha256:9ca5f80cf4d0682dd5ac84a59c9bf348be090c027144223149ad1ab8699125b6
   __DATA.__bss: 0x78 sha256:6edd9f6f9cc92cded36e6c4a580933f9c9f1b90562b46903b806f21902a1a54f
   __DATA.__common: 0xf9c sha256:3d66b4681f7f2b9d25a0bd19210429ba28a31484da8ab93b9a58344044251578
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: EAB17E3E-984C-396B-8CC0-CA48FC1C9155
-  Functions: 868
+  UUID: 6FF96DE3-A633-38D3-93C2-330CBBB12C67
+  Functions: 887
   Symbols:   185
-  CStrings:  1700
+  CStrings:  1694
 
CStrings:
+ "%s:%d: %s %s tree: PATH TOO LONG: %d\n"
+ "%s:%d: %s Error %d, reinitializing\n"
+ "%s:%d: %s Error reinitializing free extent cache: %d\n"
+ "%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n"
+ "%s:%d: %s Failed to delete covered node from length tree: %d\n"
+ "%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n"
+ "%s:%d: %s Failed to find next smallest extent in length tree: %d\n"
+ "%s:%d: %s Failed to find smallest extent %d in length tree: %d\n"
+ "%s:%d: %s Failed to find smallest extent in paddr tree: %d\n"
+ "%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n"
+ "%s:%d: %s Failed to find successor node in length tree: %d\n"
+ "%s:%d: %s Failed to get next extent: %d\n"
+ "%s:%d: %s Failed to update partially-covered node in length tree: %d\n"
+ "%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n"
+ "%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n"
+ "%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n"
+ "%s:%d: %s block range %lld:%lld out of bounds %lld\n"
+ "%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n"
+ "%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n"
+ "%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n"
+ "%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n"
+ "%s:%d: %s chunk %lld recent zone count overflow\n"
+ "%s:%d: %s chunk %lld recent zone count underflow\n"
+ "%s:%d: %s chunk %lld recent zone count zero but still marked as current\n"
+ "%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n"
+ "%s:%d: %s failed to attach graft to object cache: %d\n"
+ "%s:%d: %s failed to initialize free extent cache, error %d\n"
+ "%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
+ "%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
+ "%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n"
+ "%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n"
+ "%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n"
+ "%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n"
+ "%s:%d: %s unable to allocate chunk zone info cache\n"
+ "%s:%d: %s unable to create chunk zone info cache lock: %d\n"
+ "%s:%d: %s unable to create chunk zone info cache scan lock: %d\n"
+ "%s:%d: Why are we comparing a chunk to itself?\n"
+ "%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n"
+ "%s:%d: checkpoint<->container superblock mismatch on uuid\n"
+ "%s:%d: graft with invalid fs block size: %u\n"
+ "3277.0.0.0.1"
+ "Attempting to reuse a non-candidate chunk zone info\n"
+ "Reserved space < reserved metadata: %llu < %llu\n"
+ "SYSTEM_GRAFT_4K_OBJS"
+ "nx_superblock_agrees_with_container_superblock"
+ "obj_cache_graft_attach"
+ "obj_cache_remove_graft_persistent_ephemeral"
+ "object-cache-reset-lock"
+ "recent zone chunk should have only ONE reference when being moved to the recent list!\n"
+ "spaceman-czic-lock"
+ "spaceman-czic-scan-lock"
+ "spaceman-dev-lock"
+ "spaceman_chunk_zone_info_add"
+ "spaceman_chunk_zone_info_cache_init"
+ "spaceman_chunk_zone_info_compare"
+ "spaceman_chunk_zone_info_list_remove"
+ "spaceman_chunk_zone_info_load_recent_chunks"
+ "spaceman_chunk_zone_info_recent_decrement"
+ "spaceman_chunk_zone_info_recent_increment"
+ "spaceman_sanitize_datazones"
+ "spaceman_trim_free_blocks"
- "%s container load\n"
- "%s, Reserved space < reserved metadata: %llu < %llu\n"
- "%s:%d: %s allocation zone on dev %d for allocations of %llu blocks starting at paddr %llu\n"
- "%s:%d: %s block range %lld:%lld out of %s bounds %lld\n"
- "%s:%d: %s checkpoint descriptor block %d doesn't agree with main superblock\n"
- "%s:%d: %s dev %d %s tree: PATH TOO LONG: %d\n"
- "%s:%d: %s dev %d Error %d, reinitializing\n"
- "%s:%d: %s dev %d Error reinitializing %s free extent cache: %d\n"
- "%s:%d: %s dev %d Error searching %s free extent cache: %d; Reinitializing.\n"
- "%s:%d: %s dev %d Failed to delete covered node from length tree: %d\n"
- "%s:%d: %s dev %d Failed to find length tree predecessor for node that wasn't the smallest\n"
- "%s:%d: %s dev %d Failed to find next smallest extent in length tree: %d\n"
- "%s:%d: %s dev %d Failed to find smallest extent %d in length tree: %d\n"
- "%s:%d: %s dev %d Failed to find smallest extent in paddr tree: %d\n"
- "%s:%d: %s dev %d Failed to find successor node from length tree while updating smallest: %d\n"
- "%s:%d: %s dev %d Failed to find successor node in length tree: %d\n"
- "%s:%d: %s dev %d Failed to get next extent: %d\n"
- "%s:%d: %s dev %d Failed to update partially-covered node in length tree: %d\n"
- "%s:%d: %s dev %d Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n"
- "%s:%d: %s dev %d Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n"
- "%s:%d: %s dev %d free extent %lld:%lld appears to span container metadata and should not be free: %d\n"
- "%s:%d: %s dev %d length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
- "%s:%d: %s dev %d scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n"
- "%s:%d: %s dev %d smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n"
- "%s:%d: %s error getting cab %d: %d\n"
- "%s:%d: %s error getting cib %d: %d\n"
- "%s:%d: %s error unreserving tier2 space, %lld blocks: %d\n"
- "%s:%d: %s failed to assign chunk %llu to allocation zone %llu\n"
- "%s:%d: %s failed to evaluate chunk %llu (average free ext len %u) for disabled allocation zones, error %d\n"
- "%s:%d: %s failed to evaluate free chunk %llu for disabled allocation zone, error %d\n"
- "%s:%d: %s failed to initialize allocation zone for allocations of %llu blocks from disk: error %d\n"
- "%s:%d: %s failed to initialize data zone for allocations of size %llu, error %d\n"
- "%s:%d: %s failed to initialize free extent cache for device %d, error %d\n"
- "%s:%d: %s failed to move roving pointer for dev %d error %d\n"
- "%s:%d: %s failed to search bitmap hints: %d\n"
- "%s:%d: %s failed to update allocation zone boundaries: error %d\n"
- "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
- "%s:%d: %s main free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s nx_resize detected while processing dev=%d cib=%u out of %u cibs\n"
- "%s:%d: %s scan took %lld.%06lld s (no trims)\n"
- "%s:%d: %s spaceman tier2 cab count is bad: %d\n"
- "%s:%d: %s spaceman tier2 chunk count is bad: %lld\n"
- "%s:%d: %s spaceman tier2 cib count is bad: %d\n"
- "%s:%d: %s spaceman tier2 free count is too large: %lld > %lld\n"
- "%s:%d: %s tier2 free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s<->superblock mismatch on block count: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on block size: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid\n"
- "%s:%d: %s<->superblock mismatch on uuid\n"
- "%s:%d: the %s superblock has a lower XID %lld than the main superblock %lld\n"
- "%s:%u Err: APFS_IOUC_LOCK_UNLOCK_CONTAINER_LOAD failed with status: %x, %u\n"
- "%s:%u Warn: apfs_container_iouc (%s) failed with status: 0x%x, %u, load locking would not be available\n"
- "2811.120.14.0.1"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Locking"
- "Main"
- "T2"
- "Unlocking"
- "lock_unlock_container_load"
- "nx_superblock_agrees_with_main_superblock"
- "spaceman-dev-lock-main"
- "spaceman-dev-lock-tier2"
- "spaceman_datazone_init"
- "spaceman_evaluate_chunk_for_disabled_allocation_zones"
- "spaceman_initialize_allocation_zone_from_disk"
- "spaceman_iterate_process_bitmap_block"
- "spaceman_sanitize_datazone"
- "spaceman_scan_free_blocks"
- "tier2"

```
