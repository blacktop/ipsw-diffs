## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x515f8 sha256:de2eefbce5e74939a0b8f2dfb3d96c33dadccfda020fcff1a9a41a7d6c858efc
-  __TEXT.__auth_stubs: 0x8d0 sha256:5c64936872eeac10511eed3468eb1b6162b8f7e3c87ec0b289002b6f1cb1e3a3
-  __TEXT.__cstring: 0xfab0 sha256:c0e535e6c039e0b980cefcfad3145c386a2ab18a41b05dbbde6fd6f7334697ae
-  __TEXT.__const: 0x8470 sha256:bcb5102657323e62b72bb97673b5a6143828126d90c4b40431e409db7cbe8d04
-  __TEXT.__unwind_info: 0x848 sha256:5d08188d7a30369e522416db4f6d9ac2e77fe600457cf4d1b3752dda21608adb
-  __DATA_CONST.__auth_got: 0x468 sha256:a9b4913f90f17cd24e6912d06a2f835f53d40bc43c4cd53eb08ea85eb1bf4f7c
-  __DATA_CONST.__got: 0x58 sha256:6ca25d6a5afa6515977a59aa74d551f8bf2167f66ae5567fb04f4f7be4c5398a
-  __DATA_CONST.__auth_ptr: 0x28 sha256:1e0d44d9d8ab3a4cec2bcdc0084bf59bff02484a76d31addea5cba43d7b4f6c4
-  __DATA_CONST.__const: 0x570 sha256:782e634455a24b521c911963c01197816abb4b96589ba4ef490f1c23e25946c8
-  __DATA_CONST.__cfstring: 0x140 sha256:eb3ea24802c161f69f93471aa522936054f420bcdbdf6835600a5df24944ae45
-  __DATA.__data: 0x148 sha256:d16ab14a13e6c1b93dc2f1f98c56eb4adfea1d70d42eb5fe40bb62c1a6270893
+3277.0.0.0.1
+  __TEXT.__text: 0x510bc sha256:5c3a592f75266bd53bc307ae80811f7fb46c3113d87cc2b335edaafaf72a2838
+  __TEXT.__auth_stubs: 0x8d0 sha256:6fa33dcfdccfa39fdba8caa89e592c816598d377a6ac9e09638df8f45233bf3b
+  __TEXT.__cstring: 0xf7e1 sha256:630629a18e9b7718cb4272d8222ca8aa3534c6f4c32dfa08524714ae28264e67
+  __TEXT.__const: 0x8480 sha256:5d61e14513b8fcf669e1b1a9b58e7db9117b6e2945438e3af66272705d7576bd
+  __TEXT.__unwind_info: 0x848 sha256:65e146f6879976eacd558d5b6657a86cfa5cefa8a2fe14fba7d7cbef9a762063
+  __DATA_CONST.__const: 0x570 sha256:c3f26707e1d40f00487599eecaa553cb440a0e989357e58c970ed73b9a7ca57e
+  __DATA_CONST.__cfstring: 0x140 sha256:482cedb3476ee0b83887a6724bafffacf20e0303d39087c8aa3376884489472e
+  __DATA_CONST.__auth_got: 0x468 sha256:d75d455f23188f8d681918a81b3abe7a04d58e5e6641a11313e61927d245d4cf
+  __DATA_CONST.__got: 0x58 sha256:0fcccbbd4f78e9b3229f141ac0d3c79b0eae303cb55bcdd020e30496ac813166
+  __DATA_CONST.__auth_ptr: 0x28 sha256:e8318717b4ef55ba73ff2e5c36fe1fd0c4b3db9db95af1254e8b6afbbb11e690
+  __DATA.__data: 0x148 sha256:94dc9fb002e21e11392bd049a3331b464dd4e6757dd231772beeac3ec661f722
   __DATA.__common: 0x418 sha256:de2ca1d3d1c0862b06e5e5e33aefe44a2d0290e4ef6228128a1e797e35d3457c
   __DATA.__bss: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 8B9CB204-023A-360B-9FC0-E950A5C26AAA
-  Functions: 710
+  UUID: 4C69AD27-C046-3991-A9B2-8546A1309700
+  Functions: 714
   Symbols:   156
-  CStrings:  1338
+  CStrings:  1318
 
CStrings:
+ "%s:%d: %s %s tree: PATH TOO LONG: %d\n"
+ "%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n"
+ "%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n"
+ "%s:%d: %s %s: could not remove inode obj-id %lld (name: %s)\n"
+ "%s:%d: %s %s: could not update parent obj-id %lld on create of obj-id %lld (name: %s)\n"
+ "%s:%d: %s Error %d, reinitializing\n"
+ "%s:%d: %s Error reinitializing free extent cache: %d\n"
+ "%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n"
+ "%s:%d: %s FS will NOT have extended vek protection classes\n"
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
+ "%s:%d: %s fext_tree_update returned %d\n"
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
+ "Trying to update a namedstream inode %llx on volume %s\n"
+ "__apfs_dec_parent_nlink"
+ "modification"
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
+ "update_jobj"
- "!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))"
- "!(ino->iflags & (JI_RAW_ENCRYPTED))"
- "!apfs->apfs_readonly"
- "%s, Reserved space < reserved metadata: %llu < %llu\n"
- "%s:%d: %s %s: could not create dstream for obj-id %lld (name: %s)\n"
- "%s:%d: %s *** failed to fetch the dstream pointer for %lld (ret %d)\n"
- "%s:%d: %s *** failed to set dstream as an extended field of ino %lld (ret %d)\n"
- "%s:%d: %s allocation zone on dev %d for allocations of %llu blocks starting at paddr %llu\n"
- "%s:%d: %s block range %lld:%lld out of %s bounds %lld\n"
- "%s:%d: %s cannot insert new ep %llu because the policy cache is full\n"
- "%s:%d: %s checkpoint descriptor block %d doesn't agree with main superblock\n"
- "%s:%d: %s crypto_obj_insert of new crypto_id %lld should not have failed (ret %d)\n"
- "%s:%d: %s danger - crypto id %lld had refcnt %d\n"
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
- "%s:%d: %s failed to insert new dstream_id %llu (ret %d)"
- "%s:%d: %s failed to move roving pointer for dev %d error %d\n"
- "%s:%d: %s failed to search bitmap hints: %d\n"
- "%s:%d: %s failed to update allocation zone boundaries: error %d\n"
- "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
- "%s:%d: %s failed to update parent ino %lld nchildren field on create of %s (err %d)\n"
- "%s:%d: %s invalid crypto object type %u\n"
- "%s:%d: %s main free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s nx_resize detected while processing dev=%d cib=%u out of %u cibs\n"
- "%s:%d: %s scan took %lld.%06lld s (no trims)\n"
- "%s:%d: %s spaceman tier2 cab count is bad: %d\n"
- "%s:%d: %s spaceman tier2 chunk count is bad: %lld\n"
- "%s:%d: %s spaceman tier2 cib count is bad: %d\n"
- "%s:%d: %s spaceman tier2 free count is too large: %lld > %lld\n"
- "%s:%d: %s tier2 free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s was NOT able to update/decrement crypto state %lld, err = %d\n"
- "%s:%d: %s<->superblock mismatch on block count: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on block size: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid\n"
- "%s:%d: %s<->superblock mismatch on uuid\n"
- "%s:%d: the %s superblock has a lower XID %lld than the main superblock %lld\n"
- "((&crypto_cache->free_list)->tqh_first == ((void*)0))"
- "2811.120.14.0.1"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Main"
- "T2"
- "checkpoint"
- "crypto object retain count %d is not valid (crypto-id %lld, type %u apfs %p)\n"
- "crypto_hash_insert"
- "crypto_obj_free"
- "fs_create_dstream"
- "fs_is_content_protected(apfs)"
- "get_vol_crypto(apfs) == VOL_CPROTECTED"
- "get_vol_crypto(apfs) == VOL_PFKEY"
- "icp_dec_ref"
- "icp_new_crypto"
- "ino"
- "ino_has_vnode(ino)"
- "ino_poison_vnode(apfs, inode)"
- "invalid crypto id"
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
- "xid"

```
