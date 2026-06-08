## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0xdf44c
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x83c
-  __TEXT.__const: 0x8ad0
-  __TEXT.__cstring: 0x3a0a8
-  __TEXT.__objc_methname: 0x1da3
-  __TEXT.__oslogstring: 0x1ca4
-  __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methtype: 0x305f
-  __TEXT.__gcc_except_tab: 0x484
-  __TEXT.__unwind_info: 0x1b28
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1160
+3277.0.0.0.1
+  __TEXT.__text: 0xe3c6c
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__objc_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x84c
+  __TEXT.__const: 0x8ba0
+  __TEXT.__cstring: 0x3b2ce
+  __TEXT.__objc_methname: 0x1ee5
+  __TEXT.__oslogstring: 0x1d98
+  __TEXT.__objc_classname: 0x124
+  __TEXT.__objc_methtype: 0x2b94
+  __TEXT.__gcc_except_tab: 0x464
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x7a
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_reflstr: 0x19
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x1b68
+  __DATA_CONST.__const: 0x1240
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0xa88
-  __DATA.__objc_selrefs: 0x6d8
-  __DATA.__objc_ivar: 0x38
+  __DATA_CONST.__auth_got: 0x838
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA.__objc_const: 0xae8
+  __DATA.__objc_selrefs: 0x6f0
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1300
-  __DATA.__common: 0xb00
-  __DATA.__bss: 0x1e239
+  __DATA.__data: 0x1360
+  __DATA.__common: 0x9d8
+  __DATA.__bss: 0x1e391
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 89425845-506F-3A87-9FAF-1210678C59DE
-  Functions: 3168
-  Symbols:   1515
-  CStrings:  5283
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 4761FC63-67B0-3742-8397-88B43D61FA5E
+  Functions: 3279
+  Symbols:   1563
+  CStrings:  5400
 
Symbols:
+ OBJC_IVAR_$_APFSVolume.jhash_shutting_down
+ OBJC_IVAR_$_APFSVolume.jhash_sync_cond
+ OBJC_IVAR_$_APFSVolume.jhash_sync_mutex
+ _CacheLock
+ _CacheReinit
+ _CacheUnlock
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ _apfs_jhash_is_item_in_jhash_lockless
+ _clonegroup_register_cookie
+ _construct_drec_key
+ _crypto_make_fexts_sparse_cb
+ _extentref_validate_repair_key_val
+ _fancy_size
+ _fsck_trees
+ _fsroot_validate_repair_key_val
+ _hex_print
+ _inode_repair_remove_xf
+ _inode_repair_update_xf
+ _main
+ _nx_obj_cache_reset
+ _nx_superblock_agrees_with_container_superblock
+ _obj_cache_graft_attach
+ _obj_cache_graft_detach
+ _obj_cache_is_graft_nx
+ _obj_cache_remove_graft_persistent_ephemeral
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _omap_sv_lock
+ _pthread_join
+ _sec_fsroot_validate_repair_key_val
+ _snapmeta_validate_repair_key_val
+ _spaceman_chunk_zone_info_add
+ _spaceman_chunk_zone_info_cache_destroy
+ _spaceman_chunk_zone_info_cache_init
+ _spaceman_chunk_zone_info_cache_update
+ _spaceman_chunk_zone_info_extent_insert
+ _spaceman_chunk_zone_info_init
+ _spaceman_datazone_active
+ _spaceman_datazone_allocatable
+ _spaceman_datazone_load_from_disk
+ _spaceman_datazones_destroy
+ _spaceman_iterate_free_chunk_zone_info
+ _spaceman_iterate_process_bitmap_block_simple
+ _spaceman_sanitize_datazones
+ _spaceman_trim_free_blocks
+ _swift_errorInMain
+ _swift_getOpaqueTypeConformance2
+ _swift_getWitnessTable
+ _update_inode_xfield
+ _volume_supports_precise_purgeable_sizing
+ _xattr_is_class_v
- _CacheUpdateDevBlockSize
- _bitmap_range_find_clear_range
- _cdevname
- _fext_collector_cleanup
- _fext_collector_reset
- _fsroot_jobj_advance
- _inode_repairs_add_xf_deletion
- _jobj_validate_repair_key_val
- _lflag
- _live_fsck
- _nx_superblock_agrees_with_main_superblock
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _print_wrapped_crypto_state
- _set_inode_xfield
- _spaceman_datazone_destroy
- _spaceman_datazone_init
- _spaceman_evaluate_chunk_for_disabled_allocation_zones
- _spaceman_get_number_of_disabled_allocation_zones
- _spaceman_initialize_allocation_zone_from_disk
- _spaceman_sanitize_datazone
- _spaceman_scan_free_blocks
CStrings:
+ "\tactual hash:   %s\n"
+ "\texpected hash: %s\n"
+ " ("
+ " kMGT"
+ "!(o->o_flags & OBJ_SPACE_RESERVED) || fs_atomic_load(&oc->oc_resetting_nx, relaxed)"
+ "!fxc->fxc_nx || ((fxc->fxc_block_count + length) <= fxc->fxc_sm->sm_phys->sm_block_count)"
+ "!fxc->fxc_nx || (length < fxc->fxc_sm->sm_phys->sm_block_count)"
+ "!fxc->fxc_nx || (length <= fxc->fxc_sm->sm_phys->sm_block_count)"
+ "!nx"
+ "!nx || (nx->nx_oc == oc)"
+ "!nx->nx_reaper"
+ "!obj_cache_is_graft_nx(nx->nx_oc, nx)"
+ "!obj_cache_is_graft_nx(oc, nx) || (o->o_flags & OBJ_NONPERSISTENT)"
+ "!obj_cache_is_graft_nx(oc, o->o_nx) || (o->o_flags & OBJ_NONPERSISTENT)"
+ "%03llu"
+ "%s (id %llu): unknown flags: (0x%x / known flags are: 0x%x)\n"
+ "%s (id %llu): xf %u/%u: %s: found on a non class F file\n"
+ "%s xfield of inode object (id %llu) does not match expected value (%llu)\n"
+ "%s%llu %cB%s"
+ "%s%llu%-*.*s %cB%s"
+ "%s%llu.%.*s %cB%s"
+ "%s:%d: %s %s tree: PATH TOO LONG: %d\n"
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
+ "%s:%d: %s Failed to remove item %llu from jhash: %d"
+ "%s:%d: %s Failed to update jobj %llu while removing xattr %s with error: %d\n"
+ "%s:%d: %s Failed to update partially-covered node in length tree: %d\n"
+ "%s:%d: %s Item %llu still in jhash during dealloc - removing it (this shouldn't happen)"
+ "%s:%d: %s Item %llu still in jhash during volume deactivation"
+ "%s:%d: %s Remainders: zero %lld one %lld tiny %lld small %lld good %lld, total %lld blocks %lld avg %lld\n"
+ "%s:%d: %s Searches: %lld success %lld fail %lld partial %lld, bm search yes:%lld (%lld/%lld/%lld) no:%lld/%lld\n"
+ "%s:%d: %s attempt to attach to oc %p nx %p which is already on a list\n"
+ "%s:%d: %s block range %lld:%lld out of bounds %lld\n"
+ "%s:%d: %s cannot clone split fext %llu -> %llu at offset %llu (index %d), error %d\n"
+ "%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n"
+ "%s:%d: %s checkpoint descriptor block %d doesn't agree with container superblock\n"
+ "%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n"
+ "%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n"
+ "%s:%d: %s chunk %lld recent zone count overflow\n"
+ "%s:%d: %s chunk %lld recent zone count underflow\n"
+ "%s:%d: %s chunk %lld recent zone count zero but still marked as current\n"
+ "%s:%d: %s cleanup failed with error %d after original error %d\n"
+ "%s:%d: %s did not find purgeable drec for dir %lld (parent id %lld) (fsize %lld)\n"
+ "%s:%d: %s did not find purgeable drec for file %lld (parent id %lld) (fsize %lld)\n"
+ "%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n"
+ "%s:%d: %s failed to attach graft to object cache: %d\n"
+ "%s:%d: %s failed to initialize free extent cache, error %d\n"
+ "%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
+ "%s:%d: %s graft ephemeral object in non-graft ephemeral list\n"
+ "%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
+ "%s:%d: %s non-ephemeral object in graft ephemeral list\n"
+ "%s:%d: %s non-graft ephemeral object in graft ephemeral list\n"
+ "%s:%d: %s non-persistent ephemeral object in graft ephemeral list\n"
+ "%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n"
+ "%s:%d: %s object on graft ephemeral list has refs, o %p oid 0x%llx flags 0x%llx 0x%x type 0x%x/0x%x refcount %llu nx %p oc %p\n"
+ "%s:%d: %s scan_stats[%d]: foundmax %lld extents %lld blocks %lld long %lld avg %lld %d.%02d%% range %lld:%lld %d.%02d%%\n"
+ "%s:%d: %s smfree %lld/%lld table %d/%d blocks %lld %lld:%lld:%lld %d.%02d%% range %lld:%lld %d.%02d%% scans %lld\n"
+ "%s:%d: %s stopped purgatory dir cleanup after %d loops\n"
+ "%s:%d: %s tx_finish failed with error %d\n"
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
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid implicit stash%s\n"
+ "(adjustment > 0) || (oc->oc_graft_ephemeral_cache_size > 0)"
+ "(fr_key->fr_op == FSCK_REPAIR_OP_DELETION && fr_key->fr_subop == FSCK_REPAIR_SUBOP_NONE) || (fr_key->fr_op == FSCK_REPAIR_OP_UPDATE && fr_key->fr_subop == FSCK_REPAIR_UPDATE_DREC_HASH) || (fr_key->fr_op == FSCK_REPAIR_OP_INSERTION && fr_key->fr_subop == FSCK_REPAIR_SUBOP_NONE)"
+ "(o->o_size_phys % o->o_nx->nx_sb->nx_block_size) == 0"
+ "(q == SFQ_IP) || (sm->sm_fq_inflight == 0)"
+ "(score >= INT32_MIN) && (score <= INT32_MAX)"
+ ")"
+ "-[APFSItem dealloc]"
+ "-[APFSVolume synchronizeWithFlags:replyHandler:]_block_invoke"
+ "3277.0.0.0.1"
+ "@\"APFSVolume\""
+ "@40@0:8^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}16@24Q32"
+ "Attempting to reuse a non-candidate chunk zone info\n"
+ "CI_COUNT(chunk_info->ci_free_count) == CI_COUNT(chunk_info->ci_block_count)"
+ "INO_EXT_TYPE_STRICT_CLASS_F"
+ "OBJ_TYPE_FROM_KEY(*jobj_key) == APFS_TYPE_EXTENT"
+ "OBJ_TYPE_FROM_KEY(fr_snap_jobj_key->fr_j_key) != APFS_TYPE_EXPANDED || fr_key_len >= FSCK_REPAIR_SNAP_J_LARGE_KEY_SIZE"
+ "Requested cache size: %s (%uk blocks * %ukB)\n"
+ "Reserved space < reserved metadata: %llu < %llu\n"
+ "Round %s ov_size (oid 0x%llx) to block size? "
+ "SYSTEM_GRAFT_4K_OBJS"
+ "Set ov_size (oid 0x%llx) to the block size? "
+ "T@\"APFSVolume\",&,V_volume"
+ "TAILQ_EMPTY(&oc->oc_graft_ephemeral_list)"
+ "T^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}},V_apfs"
+ "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}"
+ "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16@0:8"
+ "_cmd_stash_kek"
+ "_volume"
+ "apfs superblock at index %u: APFS_FEATURE_EXTENDED_VEK_CLASSES set on non-HCP volume (apfs_features: 0x%llx)\n"
+ "bm_addr || (flags & SM_ITER_FREE_IN_ORDER) || (CI_COUNT(cib->cib_chunk_info[bm_addrs[processed - 1].index].ci_free_count) == 0) || (CI_COUNT(cib->cib_chunk_info[bm_addrs[processed - 1].index].ci_free_count) >= CI_COUNT(cib->cib_chunk_info[bm_addrs[processed - 1].index].ci_block_count))"
+ "btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid node hash\n"
+ "btree_key_val_validate_repair != NULL"
+ "can't find new dir-stats key for inode (id %llu): error %d\n"
+ "can't repair inode (id %llu) with dir stats (id %llu)\n"
+ "cleanup_ctx->xid && (cleanup_ctx->xid != ((xid_t)~0ULL))"
+ "cleanup_fext_iterative_processor"
+ "cleanup_purgatory_dir"
+ "clone_fext_iterative_processor"
+ "clonegroup-cookie"
+ "extract_snap_jobj_key"
+ "failed to add PFKUR entry for inode (%llu): %s\n"
+ "failed to construct drec key (dir_id %llu, file_name %s)\n"
+ "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) flags: 0x%x repair: %s\n"
+ "failed to look up resource fork for inode (%llu): %s\n"
+ "failed to register the clonegroup trees in the fsck memory storage\n"
+ "failed to remove INODE_PROT_CLASS_UPGRADE_ROLLIP flag for inode (%llu): %s\n"
+ "failed to sparse VEK extents for inode (%llu): %s\n"
+ "failed to sparse VEK extents for resource fork of inode (%llu): %s\n"
+ "fext->phys_block_num == 0"
+ "found invalid object (type %u, id %llu)\n"
+ "found solo clonegroup inode: (group_id %llu, private_id %llu, file_id %llu)\n"
+ "fr_key->fr_op == FSCK_REPAIR_OP_UPDATE || fr_key->fr_op == FSCK_REPAIR_OP_INSERTION || fr_key->fr_op == FSCK_REPAIR_OP_DELETION"
+ "fr_key->fr_subop != FSCK_REPAIR_SUBOP_NONE || fr_key->fr_op != FSCK_REPAIR_OP_UPDATE"
+ "fr_key->fr_subop == FSCK_REPAIR_DELETE_INVALID_JOBJ"
+ "fr_key->fr_subop == FSCK_REPAIR_SUBOP_NONE"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_CRYPTO_REFCOUNT || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INC_CRYPTO_REFCOUNT"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_CHAINED_KEY || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_DESCENDANTS || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_FLAGS || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_ORIGIN_ID || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_PHYS_SIZE || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_REMOVE_XFIELD || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_RESOURCE_FORK_SIZE || fr_key->fr_subop == FSCK_REPAIR_UPDATE_DIR_STATS_UPDATE_XFIELD"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_DREC_HASH"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_DSTREAM_ID_REFCOUNT"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_FEXT_LEN_AND_FLAGS || fr_key->fr_subop == FSCK_REPAIR_UPDATE_FEXT_MAKE_SPARSE"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_FILE_INFO_OBJ_ID || fr_key->fr_subop == FSCK_REPAIR_UPDATE_FILE_INFO_TOTAL_COUNT || fr_key->fr_subop == FSCK_REPAIR_UPDATE_FILE_INFO_PHYS_SIZE || fr_key->fr_subop == FSCK_REPAIR_UPDATE_FILE_INFO_CLONE_SIZE || fr_key->fr_subop == FSCK_REPAIR_UPDATE_FILE_INFO_HASH"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_NCHILDREN || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_ALLOCED_SIZE || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_DEFAULT_CRYPTO_ID || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_REMOVE_XFIELD || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_SPARSE_BYTES || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_FLAGS_SET || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_FLAGS_CLEAR || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_BSD_FLAGS_SET || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_BSD_FLAGS_CLEAR || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INODE_DIR_NLINK"
+ "fr_key->fr_subop == FSCK_REPAIR_UPDATE_XATTR_DEFAULT_CRYPTO_ID"
+ "fr_key->fr_tree == FSCK_REPAIR_TREE_FSROOT || fr_key->fr_tree == FSCK_REPAIR_TREE_SEC_FSROOT"
+ "fr_key->fr_tree == FSCK_REPAIR_TREE_SNAP_META || fr_key->fr_tree == FSCK_REPAIR_TREE_EXTENTREF || fr_key->fr_tree == FSCK_REPAIR_TREE_FSROOT || fr_key->fr_tree == FSCK_REPAIR_TREE_SEC_FSROOT"
+ "fr_key_len >= sizeof(fsck_repair_snap_j_key_t)"
+ "fr_val_len >= sizeof(j_drec_val_t)"
+ "fsck_repairs_apply_invalid"
+ "fsck_trees"
+ "fsck_trees_consume"
+ "hash validation: invalid node hash for node %llu (hash type: %u, hash size: %u, root oid: %llu, seal xid: %llu, broken xid: %llu)\n"
+ "initWithino:volume:devNumber:"
+ "inode (id %llu) has a stale dir_stats (id %llu)\n"
+ "inode (id %llu) needs to untrack from dir-stats\n"
+ "inode (id %llu): found unexpected security xattr\n"
+ "insert missing directory record object (parent_id %llu, file_id %llu)\n"
+ "isSSD"
+ "iterative_ctx->xid && (iterative_ctx->xid != ((xid_t)~0ULL))"
+ "jhash_shutting_down"
+ "jhash_sync_cond"
+ "jhash_sync_mutex"
+ "jobj_key_len == sizeof(j_key_t) && jobj_val_len == ((fr_key->fr_op == FSCK_REPAIR_OP_DELETION || fr_key->fr_subop == FSCK_REPAIR_UPDATE_INC_CRYPTO_REFCOUNT) ? 0 : sizeof(j_crypto_val_t))"
+ "jobj_key_len == sizeof(j_phys_ext_key_t)"
+ "min_inode_id <= MAX_JOBJ_ID"
+ "missing upgrade-rolling entry for inode (%llu), version (%d)\n"
+ "missing_dir_stats_do_repair"
+ "nx || !(flags & OBJ_NONPERSISTENT)"
+ "nx || (obj_type(o) == OBJECT_TYPE_NX_SUPERBLOCK)"
+ "nx || (oid != OID_DEFAULT)"
+ "nx_obj_cache_reset"
+ "nx_reaper_shut_down"
+ "nx_superblock_agrees_with_container_superblock"
+ "o->o_flags & OBJ_EPHEMERAL"
+ "obj_cache_graft_attach"
+ "obj_cache_graft_detach"
+ "obj_cache_is_graft_nx(oc, nx)"
+ "obj_cache_remove_graft_persistent_ephemeral"
+ "obj_create_bootstrap"
+ "obj_dirty"
+ "obj_dirty_locked"
+ "object-cache-reset-lock"
+ "obsolete spaceman tier2 fields should be empty but they aren't\n"
+ "oc"
+ "oc->oc_graft_count == 0"
+ "oc->oc_graft_count > 0"
+ "oc->oc_graft_ephemeral_cache_size == 0"
+ "omap entry (oid 0x%llx): invalid ov_paddr + ov_size (%llu + %u)\n"
+ "passphrase"
+ "prev_async_read_count > 0"
+ "queues[min_item_queue].consumer_node_index < queues[min_item_queue].items_len"
+ "recent zone chunk should have only ONE reference when being moved to the recent list!\n"
+ "setVolume:"
+ "sm->sm_reserved_space <= sm->sm_phys->sm_free_count"
+ "sm->sm_reserved_space <= smp->sm_free_count"
+ "sm: sm_free_count (%llu) is not valid (%llu)\n"
+ "spaceman-czic-lock"
+ "spaceman-czic-scan-lock"
+ "spaceman-dev-lock"
+ "spaceman_chunk_zone_info_add"
+ "spaceman_chunk_zone_info_cache_init"
+ "spaceman_chunk_zone_info_calculate_scores"
+ "spaceman_chunk_zone_info_compare"
+ "spaceman_chunk_zone_info_compare_with_table_index(czic, czi, table_index, 0) > 0"
+ "spaceman_chunk_zone_info_list_remove"
+ "spaceman_chunk_zone_info_load_recent_chunks"
+ "spaceman_chunk_zone_info_recent_decrement"
+ "spaceman_chunk_zone_info_recent_increment"
+ "spaceman_metazone.inited && type < ALLOCATION_TYPE_META_COUNT && spaceman_metazone.division[type].enabled"
+ "spaceman_sanitize_datazones"
+ "spaceman_trim_free_blocks"
+ "spaceman_zones.c"
+ "table_index != CZI_INVALID_INDEX"
+ "too many parent chain lookups during missing dir-stats repairs\n"
+ "trees_count > 1"
+ "uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %.*s\n"
+ "unable to allocate space to walk dir-stats parent chain\n"
+ "unable to init fsroot tree to enqueue dir-stats repairs\n"
+ "v24@0:8^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16"
+ "xattr record too small (%u)\n"
+ "xattr size (%u) does not match expected size (%lu)\n"
+ "xattr value length (%u) does not match record size (%u)\n"
+ "zero type"
+ "zero type/id"
+ "{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}"
+ "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
+ "\xf0r"
- "!(o->o_flags & (OBJ_SPACE_RESERVED_MAIN | OBJ_SPACE_RESERVED_TIER2)) || oc->oc_destroying"
- "!fxc->fxc_nx || ((fxc->fxc_block_count + length) <= fxc->fxc_sm->sm_phys->sm_dev[fxc->fxc_dev].sm_block_count)"
- "!fxc->fxc_nx || (length < fxc->fxc_sm->sm_phys->sm_dev[fxc->fxc_dev].sm_block_count)"
- "!fxc->fxc_nx || (length <= fxc->fxc_sm->sm_phys->sm_dev[fxc->fxc_dev].sm_block_count)"
- "!sm->sm_fxc[ss.dev] || !ss.fxc_need_scan_finish"
- "%s, Reserved space < reserved metadata: %llu < %llu\n"
- "%s:%d: %s %s: could not create dstream for obj-id %lld (name: %s)\n"
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
- "%s:%d: %s failed to update parent ino %lld nchildren field on create of %s (err %d)\n"
- "%s:%d: %s main free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s nx_resize detected while processing dev=%d cib=%u out of %u cibs\n"
- "%s:%d: %s scan took %lld.%06lld s (no trims)\n"
- "%s:%d: %s tier2 free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s<->superblock mismatch on block count: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on block size: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid\n"
- "%s:%d: %s<->superblock mismatch on uuid\n"
- "%s:%d: cannot clone split fext %llu -> %llu, %d\n"
- "%s:%d: the %s superblock has a lower XID %lld than the main superblock %lld\n"
- "(fr_key->fr_op == FSCK_REPAIR_OP_DELETION && fr_key->fr_update_field == FSCK_REPAIR_UPDATE_NONE) || (fr_key->fr_op == FSCK_REPAIR_OP_UPDATE && fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DREC_HASH)"
- "(fr_key->fr_op == FSCK_REPAIR_OP_UPDATE) == (fr_key->fr_update_field != FSCK_REPAIR_UPDATE_NONE)"
- "(fr_key->fr_op == FSCK_REPAIR_OP_UPDATE) || (fr_key->fr_op == FSCK_REPAIR_OP_INSERTION) || (fr_key->fr_op == FSCK_REPAIR_OP_DELETION)"
- "(o->o_size_phys % o->o_oc->oc_nx->nx_sb->nx_block_size) == 0"
- "(q == SFQ_IP) || (sm->sm_fq_inflight[SFQ_TO_SMDEV(q)] == 0)"
- "2811.120.14.0.1"
- "@40@0:8^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}16^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}24Q32"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "NO-NAME"
- "OBJ_TYPE_FROM_KEY(phys_ext_key->hdr) == APFS_TYPE_EXTENT"
- "Requested cache size: %lluMB (%uk blocks * %ukB)\n"
- "T2"
- "T^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}},V_apfs"
- "^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}"
- "^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16@0:8"
- "any"
- "bm_addr || (flags & SM_ITER_FREE_IN_ORDER)"
- "extract_phys_ext_snap_xid"
- "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) repair: %s\n"
- "failed to register the clonegroup tree in the fsck memory storage\n"
- "fext->phys_block_num"
- "flags & (SM_ALLOC_DEV_MAIN | SM_ALLOC_DEV_TIER2)"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_CRYPTO_REFCOUNT || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INC_CRYPTO_REFCOUNT"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_CHAINED_KEY || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_DESCENDANTS || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_FLAGS || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_ORIGIN_ID || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_PHYS_SIZE || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_REMOVE_XFIELD || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_RESOURCE_FORK_SIZE || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DIR_STATS_UPDATE_XFIELD"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DREC_HASH"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_DSTREAM_ID_REFCOUNT"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FEXT_LEN_AND_FLAGS || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FEXT_MAKE_SPARSE"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FILE_INFO_OBJ_ID || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FILE_INFO_TOTAL_COUNT || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FILE_INFO_PHYS_SIZE || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FILE_INFO_CLONE_SIZE || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_FILE_INFO_HASH"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_NCHILDREN || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_ALLOCED_SIZE || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_DEFAULT_CRYPTO_ID || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_REMOVE_XFIELD || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_SPARSE_BYTES || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_FLAGS_SET || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_FLAGS_CLEAR || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_BSD_FLAGS_SET || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_BSD_FLAGS_CLEAR || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INODE_DIR_NLINK"
- "fr_key->fr_update_field == FSCK_REPAIR_UPDATE_XATTR_DEFAULT_CRYPTO_ID"
- "fr_key_len == fr_jobj_key->fr_j_key_len + offsetof(fsck_repair_j_key_t, fr_j_key)"
- "fr_key_len == sizeof(fsck_repair_phys_ext_key_t)"
- "hash validation: invalid node hash for node %llu (root oid: %llu, seal xid: %lld, broken xid: %lld)\n"
- "initWithino:apfs:devNumber:"
- "ino_poison_vnode(apfs, inode)"
- "jobj_key_len == sizeof(j_key_t) && jobj_val_len == ((fr_key->fr_op == FSCK_REPAIR_OP_DELETION || fr_key->fr_update_field == FSCK_REPAIR_UPDATE_INC_CRYPTO_REFCOUNT) ? 0 : sizeof(j_crypto_val_t))"
- "missing upgrade-rolling entry for inode (%llu)\n"
- "nx_superblock_agrees_with_main_superblock"
- "omap entry (oid 0x%llx): invalid ov_paddr (%llu)\n"
- "pass"
- "purgeable inode (id %llu) was unexpectedly registered twice\n"
- "sm->sm_reserved_space[dev] <= sm->sm_phys->sm_dev[dev].sm_free_count"
- "sm->sm_reserved_space[dev] <= smp->sm_dev[dev].sm_free_count"
- "sm: sm_free_count (%llu) is not valid (%llu) (sm_dev %d)\n"
- "spaceman tier2 fields should be empty but they aren't\n"
- "spaceman-dev-lock-main"
- "spaceman-dev-lock-tier2"
- "spaceman_datazone_init"
- "spaceman_evaluate_chunk_for_disabled_allocation_zones"
- "spaceman_initialize_allocation_zone_from_disk"
- "spaceman_metazone[dev].inited && type < ALLOCATION_TYPE_META_COUNT && spaceman_metazone[dev].division[type].enabled"
- "spaceman_sanitize_datazone"
- "spaceman_scan_free_blocks"
- "tier2"
- "uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %s\n"
- "using_datazone"
- "v24@0:8^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16"
- "\x82"

```
