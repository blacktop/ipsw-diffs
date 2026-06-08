## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x4ece4 sha256:04912a22d56876ed56f40c79bd5aab086228b728c0e79d261bb12145a0833670
-  __TEXT.__auth_stubs: 0x760 sha256:6f0ec122c5d478ed27e3ec21ddc73b578eda616923d0f54cb8a173f78d1d00a7
-  __TEXT.__const: 0x4c0 sha256:f01ce619e6d619e92a43100927daacac84491196903cb8b04e9e12eaee719334
-  __TEXT.__cstring: 0xff10 sha256:dfa9dde53ed18e642f77f5e003294ebf13e9db4518f35fe8529b53ec1819c412
-  __TEXT.__unwind_info: 0x8c0 sha256:d3cf8c1fd3c4519d2f89d41d7b013c1ce07d0e495fa34f0beda06ef9ff1078c5
-  __DATA_CONST.__auth_got: 0x3b0 sha256:5b8e3dd793da001a85ee30996324ebd1a0ddb43db71c8c2c08a6c310befb9760
-  __DATA_CONST.__got: 0x50 sha256:e43830b2b87543f97c5bbd9c9d74231044c1bd9fa36c96aef56dbafde93c0889
-  __DATA_CONST.__auth_ptr: 0x28 sha256:e4c4a54beb43181a25348f41618bee35fe0c17da09270000c85153ff46ec8826
-  __DATA_CONST.__const: 0x7b8 sha256:1d65950e2c02fb137c16c9d201437fe9bbe0577e21d6ba806a2381aefb6a8095
-  __DATA_CONST.__cfstring: 0x160 sha256:37c18464d11922f30c7b7a94cf3a487617379e2d5013a843778283b1d15bac65
-  __DATA.__data: 0x360 sha256:a92d9dccc481db1f4f1daa7dff179e3e295b689f6d218a19bd915f76cda4d8c1
+3277.0.0.0.1
+  __TEXT.__text: 0x4f4cc sha256:92160da5b181b40bd0a5e911f80ac7a1b4c0c748e54fa9a4af30af9e1cc65f14
+  __TEXT.__auth_stubs: 0x760 sha256:b68b4df3dd107ab6ba2d031d64a74d5b7dc11e09f5804bf429dac23c5d310ef7
+  __TEXT.__const: 0x4c0 sha256:62ff652cd45d40fd1f8c0a37e8173161ebb9820175342d4db1f9dac442b51b9b
+  __TEXT.__cstring: 0xfefd sha256:6fd0c0e7b5ca370551cf7c653b0c5c997695cfadae70e4d152ea40df9118c9f8
+  __TEXT.__unwind_info: 0x900 sha256:2642a9cf7a81425ba2a2c1ef52da46055422fb1e49a83c4e97ac3d6d0c00e5f3
+  __DATA_CONST.__const: 0x7b8 sha256:8fc5ebf32cb92e37c26bddbf9d490696df8ec4599599e807c0545b16338f7b98
+  __DATA_CONST.__cfstring: 0x160 sha256:eb40eab58498599a62fc070bbce639a554c3dc6cd9cd6e8ba3ab452cde499029
+  __DATA_CONST.__auth_got: 0x3b0 sha256:807dbfefbfa64e3cf4b62d634df1e588d80660588478e0e2224178bf14c07e14
+  __DATA_CONST.__got: 0x50 sha256:a37f443d7d5d32cc3dbe4169f8c5eb367acc740405833860473c11c3b3d27589
+  __DATA_CONST.__auth_ptr: 0x28 sha256:4d18290b7719cc1c8ace5e31e5110a96d59089c1ac003ee4f332b3bfe78a66ea
+  __DATA.__data: 0x360 sha256:80726c3cc093bf6c8d245ccf78fc5b89680b963554eeed821908ab2dc6a3de30
   __DATA.__common: 0x414 sha256:86d911c492b42593042265fd0e6f48a2cee1f9090238e1d849420feae106ccdd
   __DATA.__bss: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 25D96488-51AD-3A56-B381-6D51765906CA
-  Functions: 729
+  UUID: 1E7372FB-017E-3CBE-8A53-1FDD7C4DC70D
+  Functions: 747
   Symbols:   133
   CStrings:  1296
 
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
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Main"
- "T2"
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
