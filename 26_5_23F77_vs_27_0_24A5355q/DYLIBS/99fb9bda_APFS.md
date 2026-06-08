## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x532a0 sha256:5613bd8d823e94c57dd6dd42f08a1ddf5a0bd8bd43d97131fa1d309f0dbe6634
-  __TEXT.__auth_stubs: 0xc40 sha256:ecd2b8f1bee09fe0b39b8ecd2afc0629b1d0f3f4ed379f3b957a5de0fc392af8
-  __TEXT.__const: 0x8540 sha256:4149d54f421a5696d4f55ab0f4afe7315776340f596a733d9cd764b1ecb1e37b
-  __TEXT.__cstring: 0xe5a3 sha256:39bd1a2698220dbee8a79e42c5099c629033c1d4530a3a1d0ad8c94ec1fd42ea
+3277.0.0.0.1
+  __TEXT.__text: 0x5384c sha256:4ac7184835592cdf46f12e4535a14df4f297bf177979c81085652bbc730c89ac
+  __TEXT.__const: 0x8540 sha256:e8485a044e0a72ff93a44035ddce7ee53d3a4a120c184e08fbc7407c4b3eaad2
+  __TEXT.__cstring: 0xe625 sha256:248aebd884a255aa74555e2890b0328a97873a84d0c45a5ea37b313a63ee8e7b
   __TEXT.__oslogstring: 0x11b8 sha256:1356b2f848c9baef012eed6a81244dfb5df941cb005673d0d8d4092fff38bdb0
-  __TEXT.__gcc_except_tab: 0x1c sha256:23c836f218c246c5c119e5bbe21f7f0ee08aee7f8c6cde4c40621ef9d0d37a9e
-  __TEXT.__unwind_info: 0x958 sha256:57b888ddf30e93af4f8c87721a319aef091b68e485ba368f228285b0cda6d0e2
-  __DATA_CONST.__got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_CONST.__const: 0x550 sha256:5469bd1077c6c0e8207b777881090e3d1522419b36ac88cdca45604db5a9e47c
-  __AUTH_CONST.__auth_got: 0x628 sha256:acf4c603e8365a5e4ec37beba4fd0de282d1717e3bb29471435100b5e3c71284
-  __AUTH_CONST.__const: 0x380 sha256:8dbaf9669b90b0218fb9755903b77dbeeb1c86227af9fc0f1f77cd9e2a004fb4
-  __AUTH_CONST.__cfstring: 0x1280 sha256:6a6c03c0c89c35c8c41602b95ed3c3a21c9172460b1f2c2eb657109904159433
-  __DATA.__data: 0x9c sha256:c5ff823c21cb583b9589938ff8ebf7408f9ec9610503e6f9dbc8466a02ae1b85
+  __TEXT.__gcc_except_tab: 0x1c sha256:0b561ac68d32676139537d83fc37176be98d039c61e56b0e2cd91e73deff1b13
+  __TEXT.__unwind_info: 0x9e0 sha256:bcffce0a9567858bb5b52a84438def6d0265091683c27170c130f780a8b0694c
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x558 sha256:9d2a15d58641a169595acdf087417c0b573f6023e645dc613dbd1e6811d972b4
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x380 sha256:72bbd78000a547214dcc9e3ea94e2a43d12daa239528ea08a683a0a6385c2ade
+  __AUTH_CONST.__cfstring: 0x1340 sha256:557a342ea378775a5d2e893986f8d318d85874a8da6c4aa1befa7c140c751a55
+  __AUTH_CONST.__weak_auth_got: 0x8 sha256:efc0ffa6f797007169da3d5f4f1075928924239cbc909fa980c86064266931b5
+  __AUTH_CONST.__auth_got: 0x638 sha256:86a618c687c518ca93f7151a26391ef0e19101986d30f7eeefa420b0574fc5ec
+  __DATA.__data: 0x9c sha256:bb9ea0126d71195dfa519b5b836bcf712ce9cf69d32ac6ad43abdb9f562b4201
   __DATA.__bss: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
   __DATA.__common: 0x418 sha256:de2ca1d3d1c0862b06e5e5e33aefe44a2d0290e4ef6228128a1e797e35d3457c
-  __DATA_DIRTY.__data: 0x148 sha256:eed8024a194ab075cccd843698a0d35635234cb2a4dc8cf8e220405fa6dd6fac
+  __DATA_DIRTY.__data: 0x148 sha256:33519f8c6ef18b3d0cc86b4e9e6306a35ba51b76f524658c22b0d56a6b6542a5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: EE22DE63-2B63-3613-AE0D-32C79054645B
-  Functions: 881
-  Symbols:   1934
-  CStrings:  1535
+  UUID: DB6DA676-D756-320A-AC4D-1EE96043DAA2
+  Functions: 901
+  Symbols:   1977
+  CStrings:  1547
 
Symbols:
+ _APFSCaptureSetPreallocSizeForFile
+ _conveyNewFileSizeToASP
+ _conveyNewVCCSizeToASP
+ _ftruncate
+ _growCaptureFile
+ _kAPFSVolumeAllowExtendedVEKClassesKey
+ _mkstemp
+ _nx_superblock_agrees_with_container_superblock
+ _obj_cache_graft_attach
+ _obj_cache_graft_detach
+ _obj_cache_is_graft_nx
+ _obj_cache_remove_graft_persistent_ephemeral
+ _shrinkCaptureFile
+ _spaceman_chunk_zone_info_add
+ _spaceman_chunk_zone_info_cache_destroy
+ _spaceman_chunk_zone_info_cache_init
+ _spaceman_chunk_zone_info_cache_update
+ _spaceman_chunk_zone_info_calculate_scores
+ _spaceman_chunk_zone_info_compare
+ _spaceman_chunk_zone_info_extent_insert
+ _spaceman_chunk_zone_info_for_chunk
+ _spaceman_chunk_zone_info_get_adjacent_extents
+ _spaceman_chunk_zone_info_init
+ _spaceman_chunk_zone_info_list_insert
+ _spaceman_chunk_zone_info_list_remove
+ _spaceman_chunk_zone_info_load_recent_chunks
+ _spaceman_chunk_zone_info_recent_increment
+ _spaceman_chunk_zone_info_sorted_index
+ _spaceman_chunk_zone_info_update
+ _spaceman_datazone_active
+ _spaceman_datazone_allocatable
+ _spaceman_datazone_can_use_chunk
+ _spaceman_datazone_load_from_disk
+ _spaceman_datazones_destroy
+ _spaceman_get_new_chunk_for_allocation_zone_scan_callback
+ _spaceman_iterate_free_chunk_zone_info
+ _spaceman_iterate_process_bitmap_block
+ _spaceman_iterate_process_bitmap_block_simple
+ _spaceman_sanitize_datazones
+ _spaceman_trim_free_blocks
+ _strcpy
+ _stuffUInt64
+ _uint32_cmp
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _bitmap_range_find_clear_range
- _nx_superblock_agrees_with_main_superblock
- _spaceman_alloc_flags_to_devs
- _spaceman_candidate_free_chunk_cmp
- _spaceman_datazone_destroy
- _spaceman_datazone_init
- _spaceman_evaluate_chunk_for_disabled_allocation_zones
- _spaceman_free_extent_cache_table_init
- _spaceman_get_number_of_disabled_allocation_zones
- _spaceman_initialize_allocation_zone_from_disk
- _spaceman_iterate_bitmap_hints
- _spaceman_sanitize_datazone
- _spaceman_scan_free_blocks
- _spaceman_search_bitmap_hints_for_space
- _update_bm_hint
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
+ "AppleEmbeddedNVMeController"
+ "Attempting to reuse a non-candidate chunk zone info\n"
+ "Number of purgeable files"
+ "Reserved space < reserved metadata: %llu < %llu\n"
+ "SYSTEM_GRAFT_4K_OBJS"
+ "Total Size of purgeable files"
+ "VCCInput0"
+ "VCCInput1"
+ "VCParams"
+ "com.apple.apfs.volume.allow_ext_vek_classes"
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
- "2811.120.14.0.1"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Main"
- "T2"
- "main"
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
