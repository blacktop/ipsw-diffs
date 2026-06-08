## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x4bf60 sha256:bbdabae66018c240083faa2283842e8ef1c43254215934ae2be76f65d6a4e4dd
-  __TEXT.__auth_stubs: 0x780 sha256:e0c3017ef92ee7206991541b5741ad58f8b53a18c4e6f76925ad29344fd472bc
-  __TEXT.__cstring: 0xf5c3 sha256:1a20c1ef9481e94cc633613d0d63ed9817052f21f8aef84e434b30fa43281b59
-  __TEXT.__const: 0x210 sha256:ad194721cec668f877a2b5e80c5fa2cbec8c7351f855fe7cb61aa7df0ec3c5c1
-  __TEXT.__unwind_info: 0x7f0 sha256:1f5c216bc4e31f8efd16d175465540fb7bb49e5d90e160094ee5f4ba5186fcf0
-  __DATA_CONST.__auth_got: 0x3c0 sha256:2079edccc5a45c065f68e0d71999b8df08717472b27c8c73317de01fa05e7359
-  __DATA_CONST.__got: 0x48 sha256:84961b82954df5a6b5b11fa0f5784ab4155224b97499acb233376bb6ad4ec808
-  __DATA_CONST.__auth_ptr: 0x20 sha256:6fa8241f7a4cad1a17d8ea196243d34caa25c5efa97caf85e2efc4cdad50a9bb
-  __DATA_CONST.__const: 0x8f8 sha256:c7943477b752c704f260f771d4a5bd3e62b600129f9d5e3ee2904b5a5f9b7207
-  __DATA_CONST.__cfstring: 0x120 sha256:3d3731c9cd93e3e106f906834fa15bbcf170cbf13053c0777dcd71c46d1d9e99
-  __DATA.__data: 0x358 sha256:9a37fe49d20c78c3c526721c4a443d6a7bba319704bdad34106946dd90906838
+3277.0.0.0.1
+  __TEXT.__text: 0x4c68c sha256:a69087cee276ef074fd6dc7824bfd30b7b12732a0348bd1568fc4e301ff83c6f
+  __TEXT.__auth_stubs: 0x780 sha256:2611f7b80751413a210db3d183b0f17e2f1f5f17d7994a181c9af18406a640f7
+  __TEXT.__cstring: 0xf5ad sha256:b0af22048dbd3e18b999acc12514169042414121a84782440d0d83c6d5566e6d
+  __TEXT.__const: 0x220 sha256:e5418a92ad22124f4238dceb7478754811127735ad55f3b819147ce8f284f771
+  __TEXT.__unwind_info: 0x828 sha256:9939cb212f6e295308e55b159864fe42d50d15e4e19ffadae100abbe606838e7
+  __DATA_CONST.__const: 0x8f8 sha256:1c6d2737bab37537b7157c91336e782ba807fa07e82d9251b3586df292b40085
+  __DATA_CONST.__cfstring: 0x120 sha256:7b96af20ab08b69e0107c7939e714099762745e57fdae5d7cf10192b66074955
+  __DATA_CONST.__auth_got: 0x3c0 sha256:08c99add646725411ed56be363f9bfe2a2ee60afa59fec4df44a3481f5268f01
+  __DATA_CONST.__got: 0x48 sha256:d47d4ed4b6d2cbc039cb687d50fcdfff34e992c18ed136ba10b659afaffd6536
+  __DATA_CONST.__auth_ptr: 0x20 sha256:ed5e028de8d4b9db5ec131940da29155a4a5d9d7afb5e8545d85d98fda199f25
+  __DATA.__data: 0x358 sha256:7d3a774495628092b952a2f7dc885a871f7cae69547d08de60e4436fe9dbe014
   __DATA.__common: 0x41c sha256:d6369598c0846422df1f6e1029041784e34d3b6fcc12a3ba0fc1613a0f80530a
   __DATA.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 52935970-44F4-35FE-A360-75E8A0FD7EF0
-  Functions: 663
+  UUID: 7C6691E1-FC0E-3636-8FF0-3D94E9D16B37
+  Functions: 681
   Symbols:   134
   CStrings:  1265
 
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
