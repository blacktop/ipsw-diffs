## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0xa88e4
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x1ec
-  __TEXT.__const: 0x88f0
-  __TEXT.__cstring: 0x2e642
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__oslogstring: 0x11b
-  __TEXT.__objc_classname: 0x5b
-  __TEXT.__objc_methname: 0x51d
-  __TEXT.__objc_methtype: 0x21e
-  __TEXT.__unwind_info: 0x1398
-  __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0xc0
+2811.100.177.0.1
+  __TEXT.__text: 0xdf450
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__const: 0x8ad0
+  __TEXT.__cstring: 0x3a0a9
+  __TEXT.__objc_methname: 0x1da3
+  __TEXT.__oslogstring: 0x1ca4
+  __TEXT.__objc_classname: 0x129
+  __TEXT.__objc_methtype: 0x305f
+  __TEXT.__gcc_except_tab: 0x484
+  __TEXT.__unwind_info: 0x1b28
+  __DATA_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0xbe8
-  __DATA_CONST.__cfstring: 0x360
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__const: 0x1160
+  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x248
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1068
-  __DATA.__common: 0xad8
-  __DATA.__bss: 0x1e229
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0xa88
+  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x1300
+  __DATA.__common: 0xb00
+  __DATA.__bss: 0x1e239
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: FEBA6D81-5E80-355E-AB87-00375D6B64B3
-  Functions: 2334
-  Symbols:   1201
-  CStrings:  3980
+  UUID: 7F143ED3-1738-320E-80BF-1CD2BA9C6527
+  Functions: 3168
+  Symbols:   1515
+  CStrings:  5283
 
Symbols:
+ _FSDirectoryCookieInitial
+ _FSTaskParameterConstantForceLoad
+ _FSTaskParameterConstantOptionReadOnly
+ _OBJC_CLASS_$_APFSItem
+ _OBJC_CLASS_$_APFSVolume
+ _OBJC_CLASS_$_FSFileName
+ _OBJC_CLASS_$_FSItem
+ _OBJC_CLASS_$_FSItemAttributes
+ _OBJC_CLASS_$_FSItemGetAttributesRequest
+ _OBJC_CLASS_$_FSStatFSResult
+ _OBJC_CLASS_$_FSVolume
+ _OBJC_CLASS_$_FSVolumeIdentifier
+ _OBJC_CLASS_$_FSVolumeSupportedCapabilities
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_APFSItem
+ _OBJC_METACLASS_$_APFSVolume
+ _OBJC_METACLASS_$_FSItem
+ _OBJC_METACLASS_$_FSVolume
+ __NSConcreteGlobalBlock
+ __NSGetExecutablePath
+ ___apfs_dec_parent_nlink
+ ___snprintf_chk
+ ___strlcat_chk
+ __apfs_max_origins_per_ino
+ __dispatch_queue_attr_concurrent
+ __get_inode_with_lookaside
+ __include_codes_in_dsym
+ __release_inode_carefully
+ __release_item_carefully
+ _add_entry_to_dir_stats_dir_stack
+ _add_entry_to_dir_stats_shadow_dir_stack
+ _advance_dir_iterator
+ _alloc_space_for_write
+ _alloc_space_for_write_with_hint_and_spino
+ _allocate_phys_range
+ _apfs_appex_log
+ _apfs_check_name
+ _apfs_clonegroup_delete_inode
+ _apfs_clonegroup_find_and_demote_last_full_clone
+ _apfs_clonegroup_get_physical_size_if_full_clone
+ _apfs_clonegroup_id_from_ino
+ _apfs_clonegroup_inode_became_partial_clone
+ _apfs_clonegroup_lock
+ _apfs_clonegroup_lookup
+ _apfs_clonegroup_remove_dir_stats_key
+ _apfs_clonegroup_unlock
+ _apfs_clonegroup_update_dir_stats_key
+ _apfs_clonegroup_update_locked
+ _apfs_clonegroup_update_purgeable_urgency
+ _apfs_clonegroup_validate_record_size
+ _apfs_create_doc_id_tree_if_needed
+ _apfs_get_block_size
+ _apfs_get_clonegroup_tree_ext
+ _apfs_has_clonegroup
+ _apfs_hashinit
+ _apfs_increment_num_objects
+ _apfs_io_lock_exclusive
+ _apfs_io_lock_shared
+ _apfs_io_unlock_exclusive
+ _apfs_io_unlock_shared
+ _apfs_is_dir_empty
+ _apfs_jhash_get_fsitem
+ _apfs_jhash_init
+ _apfs_jhash_insert_fsitem
+ _apfs_jhash_locks
+ _apfs_jhash_remove_fsitem
+ _apfs_jhash_shutdown
+ _apfs_jhash_swap
+ _apfs_jhash_try_insert
+ _apfs_jhash_try_insert_stream
+ _apfs_jhash_wakeup
+ _apfs_keybag_load_class_keys
+ _apfs_keybag_unlock_record
+ _apfs_lock_dir_stats_id
+ _apfs_lock_inode_pair
+ _apfs_lock_phys_extents
+ _apfs_lock_stream_id
+ _apfs_mark_inconsistent_
+ _apfs_mount
+ _apfs_mount_livefs
+ _apfs_release_objects
+ _apfs_remove_prev_fsize
+ _apfs_set_default_protclass
+ _apfs_set_file_size
+ _apfs_stop_bg_work
+ _apfs_store_ephemeral
+ _apfs_strcmp
+ _apfs_timestamp_to_timespec
+ _apfs_trim_to_prev_fsize
+ _apfs_unlock_dir_stats_id
+ _apfs_unlock_stream_id
+ _apfs_unmount
+ _apfs_update_cow_exempt_file_count
+ _apfs_update_last_modified_by
+ _apfs_update_phys_range
+ _apfs_update_purge_stat
+ _appexQueue
+ _appex_apfs_get_next_vol
+ _appex_apfs_mount
+ _appex_apfs_unmount
+ _appex_check_name
+ _appex_check_parent_chain
+ _appex_cleanup_fskit_format_context
+ _appex_combine_block_and_buf
+ _appex_get_item_with_lookaside
+ _appex_init_fskit_format_context
+ _appex_internal_blockmap
+ _appex_internal_lookup
+ _appex_load_inode
+ _appex_nx_mount
+ _appex_nx_unmount
+ _appex_volume_is_mountable
+ _authapfs_integrity_meta_cache_ref
+ _authapfs_integrity_meta_cache_release
+ _authapfs_seal_break
+ _btree_key_count
+ _calculate_directory_size
+ _calculate_link_size
+ _calculate_num_complete_blocks
+ _check_stale_doc_id_index
+ _cleanup_purgatory_dir
+ _clear_ino_purgeable_state_
+ _clear_invalid_fixups
+ _clear_revert_to_snapshot_ro_mount_state
+ _clone_extents_if_needed
+ _clone_extents_if_needed_with_gst
+ _clone_file_fexts
+ _clone_mapping_add_ino
+ _clone_mapping_add_mapping
+ _clone_mapping_get
+ _clone_mapping_remove
+ _clone_mapping_remove_locked
+ _clone_mapping_update_flags
+ _compressed_ino_phys_size
+ _cp_get_ek2
+ _cp_inc_ref
+ _cpx_copy
+ _create_sibling_link
+ _crypto_id_map_free
+ _crypto_id_map_get
+ _crypto_state_fext_iterator
+ _current_linkid
+ _decrement_dstream_id_for_deletion
+ _decrement_dstream_id_refcnt
+ _dereference_phys_range
+ _dev_get_num_read_errs
+ _device_is_mounted
+ _dir_rec_alloc
+ _dir_stats_mark_purgeable
+ _dir_stats_move_prepare
+ _dir_stats_unmark_purgeable
+ _dispatch_once
+ _dispatch_queue_create
+ _do_iterative_file_extent_removal
+ _doc_id_tree_create
+ _doc_id_tree_destroy
+ _doc_id_tree_invalid_crypto
+ _dump_extents_of_stream
+ _estimate_number_of_extents
+ _ever_cloned_bit_is_ok
+ _fext_collector
+ _fext_collector_cleanup
+ _fext_collector_reset
+ _fext_get_crypto_id
+ _fext_set_crypto_id_for_new_data
+ _fext_tree_lookup
+ _fext_tree_lookup_last
+ _fext_tree_update
+ _file_is_cloned_or_in_snapshot
+ _filter_purgeable_flags_for_vol
+ _find_and_destroy_orphaned_snapshots
+ _find_dir_iterator
+ _fixup_ino_with_sibling
+ _free_all_iterators
+ _free_fext_resources
+ _free_iterator_state_callback
+ _free_linkids
+ _free_tmp_ino_helper
+ _freemntopts
+ _fs_add_xattr
+ _fs_add_xattr_with_flags
+ _fs_delete_inode
+ _fs_delete_inode_with_name
+ _fs_destroy_shadow_fs_root_tree
+ _fs_dstream_get_crypto_id_for_new_data
+ _fs_get_clone_apfs
+ _fs_get_dstream
+ _fs_get_inode
+ _fs_get_inode_with_hint
+ _fs_get_inum_for_name
+ _fs_get_xattr
+ _fs_get_xattr_ext
+ _fs_insert_snapshot_metadata
+ _fs_iterate_dir
+ _fs_lookup_name
+ _fs_lookup_name_and_hash
+ _fs_map_file_offset
+ _fs_map_file_offset_ext
+ _fs_name_exists_with_parent_id
+ _fs_remove_all_xattrs
+ _fs_remove_snapshot_metadata
+ _fs_remove_xattr_with_nstream_inode
+ _fs_rename_snapshot
+ _fs_snapshot_is_reserved_name
+ _fs_tx_enter_recursively
+ _fs_write_stream
+ _gNx
+ _get_cp_class_for_crypto_id
+ _get_dir_stats
+ _get_dir_stats_by_key
+ _get_dstream_id_refcnt
+ _get_fext_crypto_logic
+ _get_ino_dstream_id_refcnt
+ _get_ino_purgeable_size_and_compressed
+ _get_new_crypto_id_if_needed
+ _get_next_apfs_obj_id
+ _get_padding_amount_for_dstream
+ _get_purgeable_dir_size
+ _get_vol_crypto_check
+ _get_wrapped_ek_snap
+ _get_wrapped_ekwk_snap
+ _get_xattr_size_info
+ _getmnt_silent
+ _getmntoptnum
+ _getmntopts
+ _getprogname
+ _increment_dstream_id_refcnt
+ _init_dir_iterator
+ _ino_get_atime
+ _ino_name
+ _ino_phys_size
+ _ino_phys_size_ext
+ _ino_rsrc_fork_phys_size
+ _ino_set_rage
+ _ino_swap_rsrc_ekwk
+ _ino_uncache_ekwk
+ _insert_linkid
+ _insert_new_skey
+ _is_non_iterative_extent_manipulation_faster
+ _iterate_dirents
+ _iterate_ino_crypto_state
+ _iterate_jobjs
+ _iterate_jobjs_with_hint
+ _iterative_fext_cloner
+ _iteratively_remove_extents_of_file
+ _jdev_fext_read_data
+ _jdev_fext_write_data
+ _jnodehash_mask
+ _jnodehash_size
+ _jnodehashtbl
+ _lookup_file_extent
+ _lookup_jobj_ext
+ _lookup_sibling_link
+ _mark_doc_id_index_for_rebuild_if_needed
+ _merge_ino_purgeable_flags
+ _meta_crypto_state_unwrap
+ _move_inode_to_purgatory
+ _move_inode_to_purgatory_ext
+ _move_snapshot_to_purgatory
+ _num_jhash_locks
+ _nx_cancel_block_out
+ _nx_is_panic_on_cp_corruption_enabled
+ _obj_cache_drain_async_reads
+ _obj_cache_flush
+ _obj_cache_flush_if_needed
+ _obj_cache_flush_needed_count
+ _objc_msgSendSuper2
+ _objc_opt_new
+ _objc_release_x1
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _omap_revert_to_snapshot
+ _os_log_create
+ _parse_nx_mount_options
+ _pthread_equal
+ _pthread_self
+ _purgeable_file_has_tracked_size
+ _reference_phys_range
+ _remove_dir_entry
+ _remove_dir_entry_ext
+ _remove_dir_stats_key_on_ino_and_clone_mapping
+ _remove_dstream_id_and_fexts_copy
+ _remove_extent_of_file
+ _remove_purgatory_entry
+ _remove_sibling_link
+ _retain_crypto_id
+ _retain_xdstream_crypto_states
+ _revert_extents_to_snapshot
+ _revert_to_snapshot
+ _rolling_stats_roll_window
+ _save_dir_iterator
+ _set_dir_stats_for_rename
+ _set_dir_stats_for_rename_cleanup
+ _set_ino_purgeable_state
+ _should_embed_xattr
+ _size_tracking_ino_moved
+ _size_tracking_ino_moved_ext
+ _size_tracking_untrack_inode
+ _skey_lookup
+ _spaceman_info
+ _spaceman_info_internal
+ _squash
+ _supplemental_tree_copy
+ _supplemental_tree_node_count
+ _supplemental_tree_revert
+ _tx_is_closing
+ _u32CharToUTF8Bytes
+ _unretain_crypto_states
+ _update_file_extent
+ _update_ino_purgeable_dstream_id
+ _update_jobj
+ _update_size_tracking_no_gencount_bump
+ _update_size_tracking_no_ino_no_gencount_bump
+ _update_size_tracking_purgeable_size
+ _update_sparse_bytes
+ _userfs_crypto_alloc_cst
+ _userfs_meta_crypto_state_unwrap
+ _utf8_normalizeOptCaseFoldToUTF8
+ _utf8_strlen
+ _xattr_collector
+ _xattr_name_to_kind
- ___NSArray0__struct
- _apfs_cstrncmp
- _backtrace
- _backtrace_symbols
- _fskit_std_log
- _lookup_jobj_in_snap
- _obj_exchange_phys
- _objc_claimAutoreleasedReturnValue
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x9
CStrings:
+ " inline"
+ "!\"bad name\""
+ "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_RAGE | BT_CACHED | BT_ASYNC | BT_PREFETCH | BT_PREFETCH_8))"
+ "!(ino->iflags & JI_HAS_EPHEMERAL_POLICY)"
+ "!(ino->iflags & JI_NAMEDSTREAM)"
+ "!(src->flags & FEXT_CRYPTO_ID_IS_TWEAK)"
+ "!INO_IS_DIR_STATS_ORIGIN(ino)"
+ "!dst_poff"
+ "!ino_is_class_v(apfs, ino)"
+ "!refresh"
+ "!tx_entered"
+ "!xid"
+ "%s (id %llu): xf %u/%u: %s: SAF dir-stats key found on non origin ino (%llu)\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield even though the file is marked as purgeable\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on directory without INODE_MARK_CHILD_PURGEABLE flag\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on file without INODE_WANTS_TO_BE_PURGEABLE flag\n"
+ "%s (id %llu): xf %u/%u: %s: invalid SAF dir_stats_key (%llu)\n"
+ "%s cannot be called for namedstream inodes\n"
+ "%s: Both inodes are NULL\n"
+ "%s:%d: ### obj-id %llu/%llu,  error %d, offset %lld, size %zu, mapflags %d, dstream %llu/%llu ###\n"
+ "%s:%d: %@"
+ "%s:%d: %s    %3d: %lld:%lld (crypto-id %lld, hash ref count %x) %lld\n"
+ "%s:%d: %s !!! failed to fixup to_ino %lld (to_drec ino %lld name %s; to_ino parent/name %lld/%s nlink %d; iret %d)\n"
+ "%s:%d: %s ### obj-id %lld/%lld error %d filesize %lld offset %lld resid %zu ###\n"
+ "%s:%d: %s ### obj-id %lld/%lld error %d filesize %llu offset %lld resid %zu ###\n"
+ "%s:%d: %s %s dir-stats for ino %llu (dir-stats key %llu -> %llu), set_flags 0x%llx\n"
+ "%s:%d: %s %s flags 0x%x for clone mapping <%llu, %llu> failed: %s (%d)\n"
+ "%s:%d: %s %s only collected %d crypto states for ino %llu (op %d, err %d)\n"
+ "%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n"
+ "%s:%d: %s %s():%d: xf-nlink count = %llu for inum %lld, removing %lld?!\n"
+ "%s:%d: %s %s."
+ "%s:%d: %s *#*#*#* from_ino %lld has nlink %d but no sibling link on the drec %lld:%s\n"
+ "%s:%d: %s *** DANGER! ino %lld has prev_fsize %lld but size %lld\n"
+ "%s:%d: %s *** failed to remove the from drec for ino %lld to_ino %lld: error %d\n"
+ "%s:%d: %s *** ino %lld resuming truncation to pos %lld (from %lld)\n"
+ "%s:%d: %s *** reset ino %lld size back to %lld (from %lld)\n"
+ "%s:%d: %s *** to ino %lld has nlink %d!\n"
+ "%s:%d: %s Aborting iterative purgeable record removal for id %llu because transaction is closing\n"
+ "%s:%d: %s Already partial! (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu)\n"
+ "%s:%d: %s Attempted to %s range %llu+%llu but it isn't entirely there! (found gap at %llu, next range at %llu+%llu)\n"
+ "%s:%d: %s BUG BUG BUG: ino %lld non-contiguous extents! prev_fext %lld:%lld (%lld) and orig_fext %lld:%lld (%lld)\n"
+ "%s:%d: %s Bad blob in (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s COW exempt file count underflow: %lld (delta %lld).  capping to zero.\n"
+ "%s:%d: %s Can't mount a volume undergoing restore/livefs-create\n"
+ "%s:%d: %s Cannot allocate space for %zu bytes at offset %lld in dstream %lld of inode %lld: %s(%d)\n"
+ "%s:%d: %s Cannot find extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n"
+ "%s:%d: %s Cannot insert purgeable record with zero atime (ino %llu).\n"
+ "%s:%d: %s Cannot load the filesystem root tree: %s(%d)\n"
+ "%s:%d: %s Cannot load the secondary filesystem root tree: %s(%d)\n"
+ "%s:%d: %s Cannot mark space for %zu bytes at offset %lld in dstream %lld of inode %lld as writable: %s(%d)\n"
+ "%s:%d: %s Cannot remove purgeable record with zero atime (ino %llu).\n"
+ "%s:%d: %s Cannot restore unwritten status of extent at offset %lld in dstream %lld of inode %lld: %s(%d)\n"
+ "%s:%d: %s Cannot start transaction with XID %lld: %s(%d)\n"
+ "%s:%d: %s Cannot trim extent at offset %lld in inode %lld from %lld to %lld bytes: %s(%d)\n"
+ "%s:%d: %s Cannot update extent at offset %lld in inode %lld: %s(%d)\n"
+ "%s:%d: %s Cannot write to dead inode (%llu)\n"
+ "%s:%d: %s Checking for solo group returned error: %s\n"
+ "%s:%d: %s Coludn't remove dir stats key from (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Coludn't update dir stats key on (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't acquire lock on %llu-%llu, err=%d\n"
+ "%s:%d: %s Couldn't create extentref tree for demo mode: %d\n"
+ "%s:%d: %s Couldn't enter TX on mount for demo mode: %d\n"
+ "%s:%d: %s Couldn't find lock for (group:%llu inum:%llu priv_id:%llu)\n"
+ "%s:%d: %s Couldn't find name for snap_xid %llu\n"
+ "%s:%d: %s Couldn't get active extentref tree, err=%d\n"
+ "%s:%d: %s Couldn't insert extent, err=%d\n"
+ "%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu) : %s\n"
+ "%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:0 priv_id:0): %s\n"
+ "%s:%d: %s Couldn't move snap xid %llu to purgatory, err %d\n"
+ "%s:%d: %s Couldn't remove extent at pbn %llu, err=%d\n"
+ "%s:%d: %s Couldn't rename snap %llx to %s\n"
+ "%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't update other (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s DONE reverting to snapshot w/xid %lld\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can only be used with SAF flags\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can't be specified alone\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can't be used externally\n"
+ "%s:%d: %s DS_OP_ONLY_SPEC_TELEMETRY can't be specified alone\n"
+ "%s:%d: %s DS_OP_ONLY_SPEC_TELEMETRY can't be used externally\n"
+ "%s:%d: %s DS_OP_SET_BY_SPACE_ATTRIBUTION cannot be passed along with DS_OP_UNSET_BY_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_SET_BY_SPACE_ATTRIBUTION cannot be passed without DS_OP_SET_FOR_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_SET_FOR_SPACE_ATTRIBUTION cannot be passed along with DS_OP_UNSET_FOR_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_SET_SPEC_TELEMETRY cannot be passed along with DS_OP_UNSET_SPEC_TELEMETRY\n"
+ "%s:%d: %s DS_OP_TRACK_PURGEABLE_RSRC_SIZE can only be used with DS_OP_TRACK_RSRC_FORKS and DS_OP_TRACK_PURGEABLE_SIZE\n"
+ "%s:%d: %s DS_OP_[UN]SET_BY_SPACE_ATTRIBUTION can't be used internally\n"
+ "%s:%d: %s Deleted the shadow_fs_root tree %p\n"
+ "%s:%d: %s EALREADY; rooted from snap, apfs %p\n"
+ "%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n"
+ "%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Error inserting cookie (group:%llu): %s\n"
+ "%s:%d: %s Error looking up dstream id %llu: %d (%s)\n"
+ "%s:%d: %s Failed %s purgeability on directory %llu: %d (%s)\n"
+ "%s:%d: %s Failed to allocate read block buffer while attempting to read inode (%llu)!\n"
+ "%s:%d: %s Failed to copy supplemental tree (type %d): %d (%s)\n"
+ "%s:%d: %s Failed to create purgeable record (drec) for lookup (ino %llu): %d (%s)\n"
+ "%s:%d: %s Failed to create purgeable record (drec) for removal: %d (%s)\n"
+ "%s:%d: %s Failed to create purgeable record (drec) for time/flags modification (ino %llu): %d (%s)\n"
+ "%s:%d: %s Failed to create purgeable record (drec): %d (%s)\n"
+ "%s:%d: %s Failed to fetch crypto for crypto_id %lld\n"
+ "%s:%d: %s Failed to find host inode (id %llu) for purgeable drec lookup, falling back to ino %llu\n"
+ "%s:%d: %s Failed to find purgeable record (ino %llu) for flags merging: %d\n"
+ "%s:%d: %s Failed to get file ID from purgeable record key/val: error %d\n"
+ "%s:%d: %s Failed to get files's size (%llu) error %d"
+ "%s:%d: %s Failed to insert drec associated with purgatory_dir and ino %llu, error = %d\n"
+ "%s:%d: %s Failed to insert purgeable record (drec): %d (%s)\n"
+ "%s:%d: %s Failed to insert purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n"
+ "%s:%d: %s Failed to insert purgeable record (record): %d (%s)\n"
+ "%s:%d: %s Failed to iterate directory %lld, error %d\n"
+ "%s:%d: %s Failed to lookup purgeable drec (id %llu): error %d\n"
+ "%s:%d: %s Failed to lookup purgeable record (record) for time/flags modification (ino %llu): %d (%s)\n"
+ "%s:%d: %s Failed to lookup purgeable record for removal (ino %llu): error %d\n"
+ "%s:%d: %s Failed to mark the dir-stats record for ino %llu as purgeable: error %d (%s)\n"
+ "%s:%d: %s Failed to move ino %lld to purgatory from dir %lld : %d\n"
+ "%s:%d: %s Failed to move ino %llu to purgatory from dir %llu : %d\n"
+ "%s:%d: %s Failed to release reference to crypto ID %lld for data stream %lld: %s(%d)\n"
+ "%s:%d: %s Failed to remove (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Failed to remove existing purgeable record (ino %llu): %d\n"
+ "%s:%d: %s Failed to remove purgatory_dir drec from fs_root tree: xid %llu, drec %llu, error = %d\n"
+ "%s:%d: %s Failed to remove purgeable record (drec): %d (%s)\n"
+ "%s:%d: %s Failed to remove purgeable record (ino %llu): error %d\n"
+ "%s:%d: %s Failed to remove purgeable record (record): %d (%s)\n"
+ "%s:%d: %s Failed to remove purgeable record for ino %llu (parent id %llu, internal_flags %#llx) iteratively (err %d).\n"
+ "%s:%d: %s Failed to remove snap_meta record!\n"
+ "%s:%d: %s Failed to remove snap_name record!\n"
+ "%s:%d: %s Failed to set purgeable drec's dir gen-count: error %d\n"
+ "%s:%d: %s Failed to set purgeable rec's dir gen-count: error %d\n"
+ "%s:%d: %s Failed to set purgeable start time for ino %lld: error %d (%s)\n"
+ "%s:%d: %s Failed to unlock volume '%s'\n"
+ "%s:%d: %s Failed to unwrap metadata crypto state: %d\n"
+ "%s:%d: %s Failed to update extended fields when %s APFS_PURGEABLE_MARK_CHILDREN on ino %llu: %d (%s)\n"
+ "%s:%d: %s Failed to update extended fields when %s WANTS_TO_BE_PURGEABLE on ino %llu: %d (%s)\n"
+ "%s:%d: %s Failed to update inode : xid %llu, ino %llu, error = %d\n"
+ "%s:%d: %s Failed to update purgatory_dir: xid %llu, ino %llu, error = %d\n"
+ "%s:%d: %s Failed to update purgeable flags on ino %llu (new flags %u):%d (%s)\n"
+ "%s:%d: %s Failed to update purgeable record (drec) time/flags (ino %llu): %d (%s)\n"
+ "%s:%d: %s Failed to update_jobj(ino %llu) after %s purgeability: %d (%s)\n"
+ "%s:%d: %s Failed to update_jobj(ino %llu) when %s is transitioning from pending-purgeable to purgeable: %d (%s)\n"
+ "%s:%d: %s Failing with error=%d\n"
+ "%s:%d: %s Found corrupt record: %s\n"
+ "%s:%d: %s Found no other mapping. (group:%llu inum:%llu priv_id:%llu) count=%u found_inum=%u\n"
+ "%s:%d: %s Found purgeable record with file ID 0!\n"
+ "%s:%d: %s Init does not have a cpx!\n"
+ "%s:%d: %s Inode %llu not a directory. Aborting.\n"
+ "%s:%d: %s Inode has no clonegroup id! (inum:%llu priv_id:%llu new_priv_id:%llu)\n"
+ "%s:%d: %s Inserting snap_meta failed, %d\n"
+ "%s:%d: %s Inserting snap_name failed, %d\n"
+ "%s:%d: %s Invalid purgeable record type %u found on volume expecting type %u\n"
+ "%s:%d: %s Invalid residency reason %d ino %llu\n"
+ "%s:%d: %s Manually managed omaps don't support snapshots\n"
+ "%s:%d: %s No file extent found during truncate down: %d\n"
+ "%s:%d: %s No file extent found during truncate up: %d\n"
+ "%s:%d: %s No memory for unaligned write buffer (for inode %llu)!\n"
+ "%s:%d: %s Only CRYPTO_ONEKEY_ID supported under UserFS!\n"
+ "%s:%d: %s Purgeable start time (%llu) is unsupported on purgeable drecs.\n"
+ "%s:%d: %s ROSV: Deleting the shadow_fs_root tree 0x%llx\n"
+ "%s:%d: %s ROSV: failed to delete shadow fs_root: %d\n"
+ "%s:%d: %s Read: danger! read on a dead inode (%llu)!\n"
+ "%s:%d: %s Reverting to snapshot w/xid %lld and old sblock oid %lld.\n"
+ "%s:%d: %s Shadow fs_root does not exist\n"
+ "%s:%d: %s The directory hierarchy rooted at ino %llu was modified - please retry.\n"
+ "%s:%d: %s This is a compressed file not supported yet by the appex\n"
+ "%s:%d: %s Trying to delete space for extent %lld %lld which has invalid owning_obj_id %lld\n"
+ "%s:%d: %s Unable to look up any snapshot greater than %lld ?: %d\n"
+ "%s:%d: %s Unaligned read starts at non zero offset %llu for obj-id %lld/%lld\n"
+ "%s:%d: %s Unexpected error searching (group:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Unexpected unwritten extent for offset %lld of data stream %lld in inode %lld\n"
+ "%s:%d: %s Unknown flags being used on purgeable record: %x. Truncating...\n"
+ "%s:%d: %s Unknown purgeable record type (%hhu)\n"
+ "%s:%d: %s Unsupported flags being used on purgeable drec: %llx. Truncating...\n"
+ "%s:%d: %s Unsupported flags being used on purgeable record: %llx. Truncating...\n"
+ "%s:%d: %s Value too small:%u (group:%llu inum:%llu priv_id:%llu)\n"
+ "%s:%d: %s Volume has unsupported purgeable record type: %u\n"
+ "%s:%d: %s Volume inconsistency detected by %s:%u!\n"
+ "%s:%d: %s Volume is incompletely restored and needs to be cleaned up\n"
+ "%s:%d: %s Would have attempted to create an entry with kind == NEW and refcnt == %d! (flags=0x%x, existing val len_and_kind=0x%llx owning_obj_id=%llu refcnt=%d)\n"
+ "%s:%d: %s added initial cow-exempt-count xattr!\n"
+ "%s:%d: %s adjusting cow exempt count from %lld to %lld\n"
+ "%s:%d: %s apfs_free_data_blocks_if_needed(%llu,%llu) failed: %d %s\n"
+ "%s:%d: %s apfs_jhash_remove_fsitem failed with error %d\n"
+ "%s:%d: %s apfs_update_phys_range failed, err = %d\n"
+ "%s:%d: %s apfs_update_phys_range for satisfiable range failed on 0x%llx+%llu, error %d\n"
+ "%s:%d: %s appex_internal_lookup returned %d\n"
+ "%s:%d: %s appex_internal_lookup with name %s in directory %llu returned %d\n"
+ "%s:%d: %s appex_load_inode returned %d\n"
+ "%s:%d: %s bad clonegroup_cookie_key_t, klen:%u vlen:%u group_id:%llu\n"
+ "%s:%d: %s bad clonegroup_key_t, size:%u\n"
+ "%s:%d: %s bad clonegroup_mapping_key_t, klen:%u vlen:%u group_id:%llu\n"
+ "%s:%d: %s bad move stan. extents w/id %lld on ino %lld has a refcnt of %d!\n"
+ "%s:%d: %s can't %s xattr (id %llu, name %s): %d\n"
+ "%s:%d: %s can't UNSET dir-stats for inode (id %llu, internal_flags 0x%llx) that is not origin\n"
+ "%s:%d: %s can't add dir %llu for recursive extent deletion\n"
+ "%s:%d: %s can't enter the cleanup transaction, ret %d\n"
+ "%s:%d: %s can't enter the cleanup transaction... ret %d\n"
+ "%s:%d: %s can't enter transaction for %llu records, %llu blocks, err %d\n"
+ "%s:%d: %s can't enter transaction to delete tmp xattr inode %llu, err %d!\n"
+ "%s:%d: %s can't find purgeable record for ino %llu: %d\n"
+ "%s:%d: %s can't get <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s can't get fsroot tree for inode %llu: %d\n"
+ "%s:%d: %s can't remove drec ino %llu, err %d\n"
+ "%s:%d: %s can't remove dstream id %lld, %d\n"
+ "%s:%d: %s can't remove item (%llu / %u) from the jhash: %d"
+ "%s:%d: %s can't remove tmp inode %llu (%s) from disk, %d\n"
+ "%s:%d: %s can't remove xattr inode %llu from disk, %d\n"
+ "%s:%d: %s can't revert because a revert is still pending to be cleaned up: %d\n"
+ "%s:%d: %s can't update inode (id %llu): %d\n"
+ "%s:%d: %s can't update purgeable record of ino %llu with new dstream_id %llu, (old %llu): %d\n"
+ "%s:%d: %s cannot add new dstream to %llu, err %d\n"
+ "%s:%d: %s cannot deref crypto id %llu, %d\n"
+ "%s:%d: %s cannot deref pexts %llu, %llu:+%llu, %d\n"
+ "%s:%d: %s cannot insert file extent record for extent of %lld bytes at offset %lld of data stream %lld in transaction %lld: %s(%d)\n"
+ "%s:%d: %s cannot persist dstream to %llu, err %d\n"
+ "%s:%d: %s cannot refresh dir-stats %llu (ino %llu) because it has unknown flags (0x%x)\n"
+ "%s:%d: %s cannot set dir-stats (%llu) for ino %llu because its current dir-stats has unknown flags\n"
+ "%s:%d: %s cannot set dstream on %llu, err %d\n"
+ "%s:%d: %s cannot update ino %llu, %d\n"
+ "%s:%d: %s checking the generation count was specified but the generation count of ino %llu is zero.\n"
+ "%s:%d: %s clone_extents_if_needed failed with error %d\n"
+ "%s:%d: %s cloning extents failed with %d (base_xid %lld)\n"
+ "%s:%d: %s cloning_err %d must_join_current_txn %s xid %lld\n"
+ "%s:%d: %s could not alloc %zd bytes @ pos %lld for obj-id %lld (err %d)\n"
+ "%s:%d: %s could not get dir-stats %llu to untrack ino %llu: %s (%d)\n"
+ "%s:%d: %s could not get dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s could not locate old super block w/sblock_oid %lld\n"
+ "%s:%d: %s could not re-set dir-stats on ino %llu after rename failure: %s (%d); space tracking may go out of sync\n"
+ "%s:%d: %s could not set dir-stats on ino %llu before it is moved to dir %llu: %s (%d); space tracking may go out of sync\n"
+ "%s:%d: %s could not start txn to revert to snapshot w/xid %lld : txerr %d\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_cloneinfo_id_epoch, %d\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n"
+ "%s:%d: %s couldn't find drec for ino %llu\n"
+ "%s:%d: %s couldn't find drec for tmp_ino %llu (%s)\n"
+ "%s:%d: %s couldn't find name from tmp ino %d\n"
+ "%s:%d: %s couldn't get clonegroup tree err:%s\n"
+ "%s:%d: %s couldn't get clonegroup tree: %s\n"
+ "%s:%d: %s couldn't insert cookie err:%s\n"
+ "%s:%d: %s couldn't insert record err:%s\n"
+ "%s:%d: %s couldn't remove (group:%llu inum:%llu priv_id:%llu) err:%s\n"
+ "%s:%d: %s couldn't remove the last clone mapping of private_id %llu, error %d\n"
+ "%s:%d: %s cp_corrupt_assert() failed: %s"
+ "%s:%d: %s createLinkToItem: received an invalid name"
+ "%s:%d: %s createSymbolicLinkNamed: received invalid name or contents"
+ "%s:%d: %s createSymbolicLinkNamed: symlink contents cannot be empty"
+ "%s:%d: %s created doc-id tree, oid %llu\n"
+ "%s:%d: %s decrement dstream id returned ENOENT for private-id %lld (ino %lld)\n"
+ "%s:%d: %s deleting extent %lld %lld with invalid owning_obj_id %lld while apfs_num_snapshots is 0, this will cause overallocation\n"
+ "%s:%d: %s did not find purgeable record for ino %lld (parent id %lld) (fsize %lld)\n"
+ "%s:%d: %s didn't find <%llu, %llu> clone mapping which was expected, not failing\n"
+ "%s:%d: %s dir %s got deleted under our feet\n"
+ "%s:%d: %s dir-stats %llu maintains clone size but failed to get the xfield: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s dir-stats %llu maintains purgeable rsrc size but failed to get the xfield: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s dir-stats %llu maintains purgeable size but failed to get the xfield: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s dir-stats can either be set or unset, but not both and not neither\n"
+ "%s:%d: %s dir-stats key %llu is busy even though we hold the inode lock\n"
+ "%s:%d: %s directory has an illegal hardlinked child (dir: %lld ; child ino %lld)\n"
+ "%s:%d: %s directory has an illegal sub-directory (dir: %lld ; sub-dir ino %lld)\n"
+ "%s:%d: %s directory sizing aborted (dir: %lld)\n"
+ "%s:%d: %s dirent hash chain iteration, dir_id %llu, hash 0x%x, count %d\n"
+ "%s:%d: %s doc-id index is stale (apfs_doc_id_index_xid %llu, expected xid %llu), but volume is RO\n"
+ "%s:%d: %s doc-id index needs rebuild, doc_id_index_flags 0x%x, role %u, doc_id_index_xid %llu, expected_xid %llu\n"
+ "%s:%d: %s doc-id tree (oid %llu, flags 0x%llx) is not encrypted but volume is encrypted (fs_flags 0x%llx)\n"
+ "%s:%d: %s doc-id tree creation failed: %d\n"
+ "%s:%d: %s dstream id %llu had refcount == 0\n"
+ "%s:%d: %s encryption type %llx unsupported\n"
+ "%s:%d: %s error %d removing purgatory entry %lld/%s for ino %lld\n"
+ "%s:%d: %s error %d while removing extents on %lld\n"
+ "%s:%d: %s error adding omap 0x%llx type 0x%x to reap list for cleaning: %d\n"
+ "%s:%d: %s error adding snapshot: %d\n"
+ "%s:%d: %s error finishing move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error finishing move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error starting move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error starting move for shadow dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error updating chained key for calculating dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error updating chained key for dir-stats %llu of ino %llu: %s (%d)\n"
+ "%s:%d: %s error updating chained key for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s failed inserting hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n"
+ "%s:%d: %s failed to %s SAF flag for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to %s dir-stats %llu as purgeable: %s (%d)\n"
+ "%s:%d: %s failed to %s shadow dir-stats %llu as purgeable: %s (%d)\n"
+ "%s:%d: %s failed to RE-insert orig from_drec %lld:%s ino %lld error %d\n"
+ "%s:%d: %s failed to add <%llu, %llu> clone mapping in error path, error %d\n"
+ "%s:%d: %s failed to add <%llu, %llu> stale clone mapping in error path, error %d\n"
+ "%s:%d: %s failed to add initial cow-exempt-count xattr! err %d\n"
+ "%s:%d: %s failed to allocate temporary block memory\n"
+ "%s:%d: %s failed to check if doc-id index is stale (error %d)\n"
+ "%s:%d: %s failed to clean up doc-id trees, error %d\n"
+ "%s:%d: %s failed to create doc-id tree, error %d\n"
+ "%s:%d: %s failed to create dstream (ino %llu), error %d\n"
+ "%s:%d: %s failed to create dstream on ino %lld (isreg: %s)\n"
+ "%s:%d: %s failed to create object named %s in dir w/obj-id %llu error %d\n"
+ "%s:%d: %s failed to create sibling link entry for %lld/%s hardlink key %lld error %d\n"
+ "%s:%d: %s failed to create sibling link entry on child of %llu pointing to %llu, error %d\n"
+ "%s:%d: %s failed to create sibling link for ino %llu, error %d\n"
+ "%s:%d: %s failed to create symlink xattr on ino %llu, error %d\n"
+ "%s:%d: %s failed to create temporary inode under %llu with %d\n"
+ "%s:%d: %s failed to decrement crypto state = %llu, err %d\n"
+ "%s:%d: %s failed to decrement crypto state refcnt, ino %llu, crypto_id %llu, error %d\n"
+ "%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld\n"
+ "%s:%d: %s failed to decrement physical range pbn=%llu len=%llu for obj-id %lld (ret %d/%s)\n"
+ "%s:%d: %s failed to decrement refcnt from cloned dstream id %llu, err: %d\n"
+ "%s:%d: %s failed to decrement refcnt on crypto-id %lld on behalf of ino %lld %lld:%lld (ret %d) \n"
+ "%s:%d: %s failed to deep copy tree (type %d, oid %llu) during reversion: %d (%s)\n"
+ "%s:%d: %s failed to delete dir entry %lld:%s (file-id %lld) ret=%d\n"
+ "%s:%d: %s failed to delete doc-id tree, error %d\n"
+ "%s:%d: %s failed to delete ino %lld (%s) iflags 0x%llx err %d\n"
+ "%s:%d: %s failed to delete prev doc-id tree (no tracked files), error %d\n"
+ "%s:%d: %s failed to delete prev doc-id tree, error %d\n"
+ "%s:%d: %s failed to dereference blocks, pbn:%llu len:%llu\n"
+ "%s:%d: %s failed to destroy old live fs tree (type %d, oid %llu) during reversion: %d (%s)\n"
+ "%s:%d: %s failed to enter a delete transaction, err %d\n"
+ "%s:%d: %s failed to enter delete txn for removal of directory, err %d\n"
+ "%s:%d: %s failed to enter tx - %s(%d)\n"
+ "%s:%d: %s failed to enter tx to %s dir-stats %llu as needing reconciliation: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s failed to enter tx to %s dir-stats for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to enter tx to finalize calculation: %s (%d)\n"
+ "%s:%d: %s failed to enter tx to remove dir-stats for unsetting %llu: %s (%d)\n"
+ "%s:%d: %s failed to enter tx to set the SAF flag on dir-stats for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to enter tx to unset dir-stats for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to enter tx while %s dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to enter tx, error %d\n"
+ "%s:%d: %s failed to extend existing extent %lld:%lld of inode %lld: %s(%d)\n"
+ "%s:%d: %s failed to fetch sub-dir ino %lld\n"
+ "%s:%d: %s failed to fetch the extentref tree (error %d)\n"
+ "%s:%d: %s failed to fetch the fext tree (error %d)\n"
+ "%s:%d: %s failed to fetch the integrity object (error %d)\n"
+ "%s:%d: %s failed to fetch the pfkur tree (error %d)\n"
+ "%s:%d: %s failed to finalize calculation for dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to find <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed to find directory entry with name ( %.*s ) inside directory with ino: %llu, inside volume %s. Error %d \n"
+ "%s:%d: %s failed to find host inode (id %llu) for purgeable rec lookup, falling back to ino %llu's atime\n"
+ "%s:%d: %s failed to finish writing to obj-id %lld (pos %lld / new_size %lld)\n"
+ "%s:%d: %s failed to free allocated blocks, ino %llu, 0x%llx+%llu, error %d\n"
+ "%s:%d: %s failed to get a new default crypto-id, ino %lld\n"
+ "%s:%d: %s failed to get doc-id tree (oid %llu, type 0x%x), error %d\n"
+ "%s:%d: %s failed to get doc-id tree key count, error %d\n"
+ "%s:%d: %s failed to get doc-id tree, error %d\n"
+ "%s:%d: %s failed to get fsys oid %lld: %d\n"
+ "%s:%d: %s failed to get ino %lld\n"
+ "%s:%d: %s failed to get ino %lld in dir %lld\n"
+ "%s:%d: %s failed to get new crypto id for clone ino %lld (cret %d; clone prot class %d)\n"
+ "%s:%d: %s failed to get next physical extent, error %s(%d)\n"
+ "%s:%d: %s failed to get shadow dir-stats %llu for calculating dir-stats %llu (ino %llu): %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s failed to get the snapshot blockref tree for delta_tree_oid %lld!\n"
+ "%s:%d: %s failed to get tree (type %d, oid %llu) for reversion: %d (%s)\n"
+ "%s:%d: %s failed to increment crypto state refcnt, ino %llu, crypto_id %llu, error %d\n"
+ "%s:%d: %s failed to increment physical range pbn=%llu len=%llu for obj-id %lld\n"
+ "%s:%d: %s failed to init extended fields for dir-stats object on ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to init extended fields for dir-stats object on ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s failed to init set shadow key for dir-stats object on ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to init xfield %d for dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to initialize item\n"
+ "%s:%d: %s failed to insert dir-stats object on ino %llu\n"
+ "%s:%d: %s failed to insert extent for ino %lld @ logical offset %lld\n"
+ "%s:%d: %s failed to insert hardlink drec %lld:%s for file-id %lld (err %d)\n"
+ "%s:%d: %s failed to insert new dir-stats object on ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to insert updated to_drec %lld:%s ino %lld error %d\n"
+ "%s:%d: %s failed to jhash_insert the inode for %llu! (err %d)\n"
+ "%s:%d: %s failed to kill dir-stats %llu (origin ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to kill shadow dir-stats %llu for dir-stats %llu (ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to leave tx, error %d\n"
+ "%s:%d: %s failed to load inode %lld ret %d on volume: %s\n"
+ "%s:%d: %s failed to load the integrity object - %s(%d)\n"
+ "%s:%d: %s failed to look up dir-stats %llu for origin inode %llu: %s (%d)\n"
+ "%s:%d: %s failed to look up drec for inode %llu, error %d\n"
+ "%s:%d: %s failed to look up shadow dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to lookup pos %lld in obj-id %lld\n"
+ "%s:%d: %s failed to lookup pos %lld in obj-id %lld err %d\n"
+ "%s:%d: %s failed to make dir-stats %llu shadow: %s (%d)\n"
+ "%s:%d: %s failed to mark apfs object for modifications - %s(%d)\n"
+ "%s:%d: %s failed to mark doc-id index for rebuild (error %d)\n"
+ "%s:%d: %s failed to mark doc-id index for rebuild, error %d\n"
+ "%s:%d: %s failed to mark integrity object for modifications - %s(%d)\n"
+ "%s:%d: %s failed to mark sealed volume's seal as broken: %s(%d)\n"
+ "%s:%d: %s failed to re-insert ext %lld:%lld for obj %lld (ret %d)\n"
+ "%s:%d: %s failed to read-modify during write: %d\n"
+ "%s:%d: %s failed to remove <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed to remove dir stats key from <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed to remove dir-stats for unsetting %llu: %s (%d)\n"
+ "%s:%d: %s failed to remove dir-stats object (id %llu): %s (%d)\n"
+ "%s:%d: %s failed to remove drec %lld:%s ino %lld ret %d\n"
+ "%s:%d: %s failed to remove dstream_id %llu (err %d)\n"
+ "%s:%d: %s failed to remove ext %lld:%lld for obj %lld (ret %d)\n"
+ "%s:%d: %s failed to remove extent %lld %lld:%lld (ret %d) \n"
+ "%s:%d: %s failed to remove extent for extent-id %lld @ logical offset %lld:%lld err %d\n"
+ "%s:%d: %s failed to remove extents of dstream %llu (err %d)\n"
+ "%s:%d: %s failed to remove file extents: %d\n"
+ "%s:%d: %s failed to remove first, error %d\n"
+ "%s:%d: %s failed to remove hash file info for id %llu @ logical offset %llu err %u\n"
+ "%s:%d: %s failed to remove head_fext, ino %llu, laddr 0x%llx, error %d\n"
+ "%s:%d: %s failed to remove kill dir-stats %llu for dir-stats %llu (ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to remove prev_fsize after truncation: %d\n"
+ "%s:%d: %s failed to remove prev_fsize: %d\n"
+ "%s:%d: %s failed to remove shadow dir-stats %llu when unsetting dir-stats %llu (ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to remove shadow dir-stats object (id %llu): %s (%d)\n"
+ "%s:%d: %s failed to remove sibling hard link entry for ino %lld under hardlink/sibling key %lld/%lld w/drec %lld:%s (ret %d)\n"
+ "%s:%d: %s failed to remove tail_fext, ino %llu, laddr 0x%llx, error %d\n"
+ "%s:%d: %s failed to remove the FROM sibling hard link (ino %lld, sib-id %lld, nlink %d) and drec %lld/%s (error %d) (to_ino %lld)\n"
+ "%s:%d: %s failed to remove the TO sibling hard link from ino %lld sib-id %lld (nlink %d) for drec %lld/%s error %d\n"
+ "%s:%d: %s failed to remove the remaining extents on ino %lld (rret %d; num_deleted %d)\n"
+ "%s:%d: %s failed to remove the stale clone mapping <%llu , %llu>, error %d\n"
+ "%s:%d: %s failed to removeItem on the inode %llu! (err %d)\n"
+ "%s:%d: %s failed to restore clone attributes for ino %llu (err %d)\n"
+ "%s:%d: %s failed to restore orig_fext, ino %llu, pbn 0x%llx, laddr 0x%llx, len %llu, crypto_id %llu, error %d\n"
+ "%s:%d: %s failed to restore refcnt on cloned dstream id %llu, err: %d\n"
+ "%s:%d: %s failed to restore refcnt on dstream id %llu, err: %d\n"
+ "%s:%d: %s failed to retain crypto-id %llu for ino %llu, %d\n"
+ "%s:%d: %s failed to retrieve existing dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to set dir stats key for <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed to set dir-stats key %llu on ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to set fast-path SAF dir-stats %llu: %s (%d)\n"
+ "%s:%d: %s failed to set file size: %d\n"
+ "%s:%d: %s failed to set shadow dir-stats key new dir-stats: %s (%d)\n"
+ "%s:%d: %s failed to set the dir-gen-count xf field on the purgeable rec for ino %lld : err %d\n"
+ "%s:%d: %s failed to set the drec SIBLING id %lld for ino %lld\n"
+ "%s:%d: %s failed to set the sibling id on ino %llu\n"
+ "%s:%d: %s failed to set up dir-stats for ino %llu: %s (%d);  size tracking may be out of sync\n"
+ "%s:%d: %s failed to setAttributes the inode for %llu! (err %d)\n"
+ "%s:%d: %s failed to tx enter, error %d\n"
+ "%s:%d: %s failed to unset SAF flag for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to unset dir-stats for ino %llu: %s (%d);  size tracking may be out of sync\n"
+ "%s:%d: %s failed to update <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed to update dir-stats key for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to update dir-stats state for ino %llu: %s (%d)\n"
+ "%s:%d: %s failed to update dstream id %lld err %d\n"
+ "%s:%d: %s failed to update ino %lld error %d\n"
+ "%s:%d: %s failed to update ino %llu as dir-stats origin: %s (%d)\n"
+ "%s:%d: %s failed to update ino %llu on-disk: %s (%d)\n"
+ "%s:%d: %s failed to update inode attributes: %d\n"
+ "%s:%d: %s failed to write %llu blocks to disk at pbn %llu, err %d\n"
+ "%s:%d: %s failed to write 1 block to disk at pbn %llu, err %d\n"
+ "%s:%d: %s failed to zero-fill tail during truncate down: %d\n"
+ "%s:%d: %s failed to zero-fill tail during truncate up: %d\n"
+ "%s:%d: %s failed to%s update the <%llu, %llu> clone mapping, error %d\n"
+ "%s:%d: %s failed updating hole %lld:%lld (pos %lld, len %lld alloced_size %lld) err %d\n"
+ "%s:%d: %s failed with err %d while getting the cow-exempt-file-count xattr on the root dir\n"
+ "%s:%d: %s fext_ref_extent_key for fext %llu with crid %llu failed with %d\n"
+ "%s:%d: %s fext_tree_update returned %d\n"
+ "%s:%d: %s find_next_snap(%llu) returned %d\n"
+ "%s:%d: %s free'ing allocated extents for snap_xid %llu\n"
+ "%s:%d: %s free'ing extents in main extentref tree %lld\n"
+ "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
+ "%s:%d: %s fs_delete_inode failed with error %d\n"
+ "%s:%d: %s fs_tx_enter failed: %s (%d)\n"
+ "%s:%d: %s fs_update_snap_metadata() returned %d\n"
+ "%s:%d: %s full clone scan failed (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s get_cp_class_for_crypto_id failed (crypto id %llu, error %d)\n"
+ "%s:%d: %s got an invalid type %ld"
+ "%s:%d: %s got err %d writing at pos %lld in obj-id %lld (blkcount %llu, len %zd)\n"
+ "%s:%d: %s ino %lld (%s) could not get a new crypto-id (ret %d gencount %d xid %lld)!\n"
+ "%s:%d: %s ino %lld did not have a source-purge-id\n"
+ "%s:%d: %s ino %lld failed to remove purgatory entry: iflags 0x%llx internal_flags 0x%llx isdir: %d\n"
+ "%s:%d: %s ino %lld file extent %lld:%lld extends beyond alloced_size %lld (fsize %lld). fixing it.\n"
+ "%s:%d: %s ino %lld no extent covering dstream alloced_size %lld (fsize %lld) pos/len %lld:%lld\n"
+ "%s:%d: %s ino %llu is being moved but we don't know how to account for it (from_dir %llu/%llu, to_dir %llu/%llu); size tracking may go out of sync\n"
+ "%s:%d: %s ino %llu is compressed and this volume does not support compressed purgeable files.\n"
+ "%s:%d: %s ino %llu is flagged as dir-stats origin but has no dir-stats key\n"
+ "%s:%d: %s ino %llu is marked as dir-stats origin (id %llu), but could not get its dir-stats: %s (%d)\n"
+ "%s:%d: %s inode %llu is already in purgatory\n"
+ "%s:%d: %s inode %llu was marked sparse but didn't have a sparse bytes extended field?\n"
+ "%s:%d: %s integrity protection will be disabled (from xid: %llu)\n"
+ "%s:%d: %s invalid dir-stats UNSET flags: 0x%llx\n"
+ "%s:%d: %s invalid dir-stats flags 0x%x\n"
+ "%s:%d: %s invalid op_flags for %s dir-stats: 0x%llx\n"
+ "%s:%d: %s invalid op_flags for setting dir-stats: 0x%llx\n"
+ "%s:%d: %s invalid ref count %d for non NULL zero ref tree\n"
+ "%s:%d: %s invalid zero len, paddr %llu\n"
+ "%s:%d: %s iterated through %llu inodes while %s dir-stats %llu\n"
+ "%s:%d: %s key @ %p key.hdr.obj_id %lld val @ %p val.kind %d refcnt %d owning_obj_id 0x%llx\n"
+ "%s:%d: %s key.hdr.kind != NEW && numsnapshots == 0\n"
+ "%s:%d: %s link count == %d for inum %lld?!\n"
+ "%s:%d: %s link count == %d for inum %llu?!\n"
+ "%s:%d: %s lookup_file_extent failed: %s (%d)\n"
+ "%s:%d: %s mount for ramdisk\n"
+ "%s:%d: %s must mount read-write after revert to unsealed snapshot\n"
+ "%s:%d: %s no special dir-stats op flags are allowed on non-expanded volumes\n"
+ "%s:%d: %s no txn for remove_prev_fsize: %d\n"
+ "%s:%d: %s not enough space to enter transaction\n"
+ "%s:%d: %s overprovisioning volume can only mount r/o\n"
+ "%s:%d: %s parent is %lld name is %s\n"
+ "%s:%d: %s prepare for rebuild, doc_id_index_flags 0x%x, doc_id_tree_oid %llu, prev_doc_id_tree_oid %llu, doc_id_tree_type %u, apfs_next_doc_id %d\n"
+ "%s:%d: %s prev doc-id tree oid is non-zero (%llu), but index is not being built (flags 0x%x), deleting prev tree\n"
+ "%s:%d: %s processed %d extents and free'd %lld blocks\n"
+ "%s:%d: %s proposed crypto id %llu already in use, making a new one\n"
+ "%s:%d: %s rapid-aged %llu inodes\n"
+ "%s:%d: %s readSymbolicLink: item is not a symbolic link"
+ "%s:%d: %s refreshing (nested) dir-stats for ino %llu (dir-stats key %llu -> %llu), set_flags 0x%llx\n"
+ "%s:%d: %s remove_dir_entry failed, err %d\n"
+ "%s:%d: %s remove_jobj(old-snap-name) returned %d\n"
+ "%s:%d: %s remove_purgatory_entry failed on %s for file-id %lld err %d\n"
+ "%s:%d: %s removing xattrs returned ENOENT for private-id %lld (ino %lld)\n"
+ "%s:%d: %s resizing will be cancelled as the user volume is encrypted and is changing mount state to mounted\n"
+ "%s:%d: %s reverted supplemental tree (type %d): %llu -> %llu\n"
+ "%s:%d: %s set apfs_fixup_flags to %#llx\n"
+ "%s:%d: %s set cloneinfo_id_epoch to %llu\n"
+ "%s:%d: %s snap xid %llu is an orphan... moving it to purgatory\n"
+ "%s:%d: %s snap_name='%s' snap_xid %lld extentref oid %lld sblock oid %lld\n"
+ "%s:%d: %s spaceman_alloc() FAILED, err: %d xid: %lld paddr: %lld blocks requested: %lld blocks allocated: %lld\n"
+ "%s:%d: %s stop background work requested, stopping tree destroy, prev %d\n"
+ "%s:%d: %s the source inode for rename has been deleted and does not match the looked up inode, source ino %llu, looked up ino %llu\n"
+ "%s:%d: %s there is no drec for ino %lld\n"
+ "%s:%d: %s tree creation failed: %d\n"
+ "%s:%d: %s tree_iterator_next failed: %s\n"
+ "%s:%d: %s tree_remove(%llu) failed\n"
+ "%s:%d: %s trying to restore refcnt on dstream id %llu\n"
+ "%s:%d: %s unable to create snapshot for reversion: %d\n"
+ "%s:%d: %s unable to create snapshot tree: %d\n"
+ "%s:%d: %s unable to find snapshot %lld: %d\n"
+ "%s:%d: %s unable to modify the apfs object (err %d) to be able to revert the fs.\n"
+ "%s:%d: %s unable to mount livefs as volume is restoring or mounted\n"
+ "%s:%d: %s unknown dir-stats op flags: 0x%llx\n"
+ "%s:%d: %s unknown flags for dir-stats %llu (origin ino %llu): 0x%x (first dir-stats %llu)\n"
+ "%s:%d: %s unsetting dir-stats for ino %llu (dir-stats key %llu -> %llu), unset_flags 0x%llx\n"
+ "%s:%d: %s unsupported apfs_incompatible_features (%llx): unable to mount\n"
+ "%s:%d: %s unsupported apfs_readonly_compatible_features (%llx): mount r/o\n"
+ "%s:%d: %s unsupported tree type, %d\n"
+ "%s:%d: %s update of the purgatory dir failed! err %d xid %lld\n"
+ "%s:%d: %s update_jobj() failed trying to increment ino %lld's link count, err %d\n"
+ "%s:%d: %s using fext tree oid %lld\n"
+ "%s:%d: %s volume marked for doc-id index rebuild but does not support index (role %d, flags 0x%x)\n"
+ "%s:%d: %s volume was marked for revert while mounted RO, skip revert to xid %lld\n"
+ "%s:%d: %s waiting for snapshot deletion to finish (id %lld) failed: %d\n"
+ "%s:%d: %s was asked to revert to snapshot w/xid %llu but got error %d\n"
+ "%s:%d: %s write blockmap failed: %d\n"
+ "%s:%d: %s xattr %lld:%s err %d decrementing crypto state id %lld (xattr dstream id %lld)\n"
+ "%s:%d: %s zero-filling blockmap failed: %d\n"
+ "%s:%d: Couldn't set sparse bytes extended attribute on ino %lld, error %d\n"
+ "%s:%d: DANGER! got the same extent for logical addr %lld twice!\n"
+ "%s:%d: Expected to read %lu bytes, read %lu"
+ "%s:%d: FAILED TO LOAD THE PRIVATE DIR INODE!\n"
+ "%s:%d: FAILED TO LOAD THE ROOT INODE!\n"
+ "%s:%d: Failed to read, error %ld"
+ "%s:%d: Failed to remove sparse bytes attribute from ino %lld, but it was successfully got, errro %d\n"
+ "%s:%d: Free'ing in-use iterator (index %lld ; name %s)\n"
+ "%s:%d: Given device is not a block device"
+ "%s:%d: Mounted volume %s"
+ "%s:%d: Mounting volume %s"
+ "%s:%d: NULL blockmap args.\n"
+ "%s:%d: NULL blockmap arguments.\n"
+ "%s:%d: No entry for private metadata dir!\n"
+ "%s:%d: No entry for root dir!\n"
+ "%s:%d: No message connection object, can't log message"
+ "%s:%d: Parent directory %llu is deleted.\n"
+ "%s:%d: Refusing to mount a volume undergoing encryption rolling.\n"
+ "%s:%d: Sparse bytes removed from inode %lld internal flags: 0x%llx iflags 0x%llx, new_sparse_bytes %lld; name %s parent-id %lld), but it wasn't marked sparse.\n"
+ "%s:%d: Sparse bytes removed from inode %lld that didn't have an extended field.\n"
+ "%s:%d: Successfully reverted to snapshot.\n"
+ "%s:%d: Unexpected unwritten extent for offset %llu in data stream %llu of the inode %llu\n"
+ "%s:%d: Unmounted volume w/oid %llu"
+ "%s:%d: Unmounting volume %s (oid %llu)"
+ "%s:%d: alloc_space_for_write failed with error %d\n"
+ "%s:%d: apfs_jhash_init failed: error %d\n"
+ "%s:%d: apfs_mount failed, err: %d\n"
+ "%s:%d: appex_apfs_load_nodes failed, err: %d\n"
+ "%s:%d: appex_apfs_mount failed: error %d"
+ "%s:%d: appex_nx_mount failed: error %d\n"
+ "%s:%d: blockmap failed: %d\n"
+ "%s:%d: call to load volume class keys does not exist\n"
+ "%s:%d: can't have a namedstream vnode without a valid name\n"
+ "%s:%d: cannot clone split fext %llu -> %llu, %d\n"
+ "%s:%d: cannot deref ino %llu old ekwk %llu, %d\n"
+ "%s:%d: cannot free fext %llu %llu:+%llu, %d\n"
+ "%s:%d: cannot get ino %llu ek %llu, %d\n"
+ "%s:%d: cannot get ino %llu ekwk %d\n"
+ "%s:%d: cannot get on-disk ekwk %llu, %d\n"
+ "%s:%d: cannot get unwrapped ekwk ino %llu, %d\n"
+ "%s:%d: cannot insert reserved, un-busy jhash object"
+ "%s:%d: cannot revert pext references %llu, %llu:+%llu, %d\n"
+ "%s:%d: couldn't allocate memory for link origin\n"
+ "%s:%d: done"
+ "%s:%d: error, %d, when checking tree entry size %u, %u\n"
+ "%s:%d: failed to allocate %d dir stack entries (%zu bytes)\n"
+ "%s:%d: failed to find unlock record to load class keys, error = %d\n"
+ "%s:%d: failed to find volume key to load class keys, error = %d\n"
+ "%s:%d: failed to get fs oid %llu: %d\n"
+ "%s:%d: failed to get next vol: error %d\n"
+ "%s:%d: failed to initialise volume"
+ "%s:%d: failed to initialise volume's UUID"
+ "%s:%d: failed to initialise volume's name"
+ "%s:%d: failed to initialize item\n"
+ "%s:%d: failed to initialize root item\n"
+ "%s:%d: failed to load ekwk for ino %llu, id %llu, class %d, decode error\n"
+ "%s:%d: failed to load volume class keys, error = %x\n"
+ "%s:%d: failed to move ino %lld from dir %lld to purgatory : %d\n"
+ "%s:%d: failed to read block at pbn %llu, err %d\n"
+ "%s:%d: failed to revert snapshot, err: %d\n"
+ "%s:%d: failed to unwrap proposed volume key, err = %d\n"
+ "%s:%d: failed to unwrap volume key, err = %d\n"
+ "%s:%d: failed to unwrap volume key, err = 0x%x (tag = %u)\n"
+ "%s:%d: found a reserved, non-busy jhash object"
+ "%s:%d: how odd... there is nothing at the tail of the dir iterator list for ino %llu yet the count is %d\n"
+ "%s:%d: ino %llu has no ekwk id\n"
+ "%s:%d: inode %llu was marked sparse but has no sparse bytes extended field. Ignoring.\n"
+ "%s:%d: invalid option -S should follow -E\n"
+ "%s:%d: loaded resource with ID (%@)"
+ "%s:%d: locking id %llu, which is already locked by this thread\n"
+ "%s:%d: nx_mount failed: %d\n"
+ "%s:%d: obj %llu @ %p has non-null list %p\n"
+ "%s:%d: obj %llu @ %p has zero devt!\n"
+ "%s:%d: obj is NULL or not apfs object!"
+ "%s:%d: object %llu / %p has bad dev\n"
+ "%s:%d: reserved jhash objects should be busy"
+ "%s:%d: skipped creating system-enabled vek without a kek, encountered unexpected crypto-type.\n"
+ "%s:%d: spaceman_info failed: error %d\n"
+ "%s:%d: stale clone mapping <%llu, %llu> had non-empty extended fields\n"
+ "%s:%d: start"
+ "%s:%d: started to format resource"
+ "%s:%d: successfully loaded volume class keys\n"
+ "%s:%d: unlock succeeded, but failed to fix-up and replace stale-invalid wvek with committed-proposed wvek, err = %d\n"
+ "%s:%d: unlocking id %llu, which is not locked\n"
+ "%s:%d: zero devt: old %llu, %d; new %llu, %d"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh, Unexpected short PDK len%s\n"
+ "%s:%u: cannot unwrap ek %llu, %d\n"
+ "%s:%u: ino %llu invalid class %u\n"
+ "(((ino->mode) & 0170000) == 0100000)"
+ "(add_flags != 0) || (remove_flags != 0)"
+ "(new_parent_id == 0) || (op_flags == 0)"
+ "(required_op == SET_NEEDED) || (required_op == UNSET_NEEDED)"
+ "*xid && (*xid != ((xid_t)~0ULL))"
+ "-[APFSFileSystem scanVolumes:]"
+ "-[APFSFileSystem unloadResource:options:replyHandler:]"
+ "-[APFSItem createItem:type:attributes:content:volumeIndex:outItem:]"
+ "-[APFSItem createLinkToItem:named:]"
+ "-[APFSItem getItemSizes:]"
+ "-[APFSItem readFromFile:offset:length:intoBuffer:actuallyRead:]"
+ "-[APFSItem removeDirectory:DirectoryEntry:]"
+ "-[APFSItem removeFile:DirectoryEntry:]"
+ "-[APFSItem removeItem:name:]"
+ "-[APFSItem renameItem:inDirectory:named:toNewName:overItem:]"
+ "-[APFSItem setAttributes:error:]"
+ "-[APFSItem setItemSizes:]"
+ "-[APFSItem setXattr:toData:policy:]"
+ "-[APFSItem writeContents:atOffset:actuallyWritten:]"
+ "-[APFSItem zeroTailOfBlock:locked:]"
+ "-[APFSVolume activateWithOptions:replyHandler:]"
+ "-[APFSVolume createItemNamed:type:inDirectory:attributes:replyHandler:]"
+ "-[APFSVolume createItemNamed:type:inDirectory:attributes:replyHandler:]_block_invoke"
+ "-[APFSVolume createLinkToItem:named:inDirectory:replyHandler:]"
+ "-[APFSVolume createLinkToItem:named:inDirectory:replyHandler:]_block_invoke"
+ "-[APFSVolume createSymbolicLinkNamed:inDirectory:attributes:linkContents:replyHandler:]"
+ "-[APFSVolume createSymbolicLinkNamed:inDirectory:attributes:linkContents:replyHandler:]_block_invoke"
+ "-[APFSVolume deactivateItem:replyHandler:]"
+ "-[APFSVolume deactivateWithOptions:replyHandler:]"
+ "-[APFSVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:]"
+ "-[APFSVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:]_block_invoke"
+ "-[APFSVolume getAttributes:ofItem:replyHandler:]"
+ "-[APFSVolume getAttributes:ofItem:replyHandler:]_block_invoke_2"
+ "-[APFSVolume getXattrNamed:ofItem:replyHandler:]"
+ "-[APFSVolume getXattrNamed:ofItem:replyHandler:]_block_invoke"
+ "-[APFSVolume listXattrsOfItem:replyHandler:]"
+ "-[APFSVolume listXattrsOfItem:replyHandler:]_block_invoke"
+ "-[APFSVolume lookupItemNamed:inDirectory:replyHandler:]"
+ "-[APFSVolume lookupItemNamed:inDirectory:replyHandler:]_block_invoke"
+ "-[APFSVolume preallocateSpaceForItem:atOffset:length:flags:replyHandler:]"
+ "-[APFSVolume readFromFile:offset:length:intoBuffer:replyHandler:]"
+ "-[APFSVolume readFromFile:offset:length:intoBuffer:replyHandler:]_block_invoke"
+ "-[APFSVolume readSymbolicLink:replyHandler:]"
+ "-[APFSVolume readSymbolicLink:replyHandler:]_block_invoke"
+ "-[APFSVolume reclaimItem:replyHandler:]"
+ "-[APFSVolume reclaimItem:replyHandler:]_block_invoke"
+ "-[APFSVolume removeItem:named:fromDirectory:replyHandler:]"
+ "-[APFSVolume removeItem:named:fromDirectory:replyHandler:]_block_invoke"
+ "-[APFSVolume renameItem:inDirectory:named:toNewName:inDirectory:overItem:replyHandler:]"
+ "-[APFSVolume renameItem:inDirectory:named:toNewName:inDirectory:overItem:replyHandler:]_block_invoke"
+ "-[APFSVolume setAttributes:onItem:replyHandler:]"
+ "-[APFSVolume setAttributes:onItem:replyHandler:]_block_invoke"
+ "-[APFSVolume setVolumeName:replyHandler:]"
+ "-[APFSVolume setXattrNamed:toData:onItem:policy:replyHandler:]"
+ "-[APFSVolume setXattrNamed:toData:onItem:policy:replyHandler:]_block_invoke"
+ "-[APFSVolume volumeStatistics]"
+ "-[APFSVolume writeContents:toFile:atOffset:replyHandler:]"
+ "-[APFSVolume writeContents:toFile:atOffset:replyHandler:]_block_invoke"
+ "."
+ ".."
+ "/..namedfork/rsrc"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/apfs_appex/APFSAppexFunctions.m"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/apfs_appex/APFSAppexJhash.m"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/apfs_appex/APFSAppexVolume.m"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/apfs_appex/APFSItem.m"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/dir_iteration.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/fs_utils.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/purging.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/size_tracking.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/jobj.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/jobj_snap.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/obj.c"
+ "0x%llx-0x%llx:%d"
+ "2811.100.177.0.1"
+ "@\"APFSItem\""
+ "@\"FSStatFSResult\"16@0:8"
+ "@\"FSVolumeSupportedCapabilities\"16@0:8"
+ "@\"NSArray\"24@0:8@\"FSItem\"16"
+ "@24@0:8@16"
+ "@24@0:8^@16"
+ "@32@0:8@16^i24"
+ "@40@0:8^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}16^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}24Q32"
+ "@48@0:8Q16@24@32@40"
+ "APFSAppexFunctions.m"
+ "APFSAppexJhash.m"
+ "APFSItem"
+ "APFSItem has null apfs reference"
+ "APFSItem has null inode"
+ "APFSItem.m"
+ "APFSVolume"
+ "B"
+ "B36@0:8@16^{dir_iterator=QQqQQIIIQ[766c](?={btree_hint=Q^v}){?=^{dir_iterator}^^{dir_iterator}}}24B32"
+ "FSUnaryFileSystemOperations"
+ "FSVolumeItemDeactivation"
+ "FSVolumeOperations"
+ "FSVolumePathConfOperations"
+ "FSVolumePreallocateOperations"
+ "FSVolumeReadWriteOperations"
+ "FSVolumeRenameOperations"
+ "FSVolumeXattrOperations"
+ "INO_EXT_TYPE_SAF_DIR_STATS_KEY"
+ "INO_IS_DIR_STATS_ORIGIN(ino)"
+ "Jhash-appex-lock"
+ "NO"
+ "NONAME"
+ "Q"
+ "SET_FLAG_IS_SET(dir_stats_state->op_flags)"
+ "S_ISREG(ino->mode)"
+ "T@\"APFSItem\",&,V_rootItem"
+ "T@\"FSStatFSResult\",R,N"
+ "T@\"FSVolumeSupportedCapabilities\",R,N"
+ "TB,?"
+ "TB,?,GisPreallocateInhibited"
+ "TB,?,GisVolumeRenameInhibited"
+ "TB,R"
+ "TB,R,VrestrictsOwnershipChanges"
+ "TB,R,VtruncatesLongNames"
+ "TQ,?"
+ "TQ,?,R"
+ "TQ,R,VitemDeactivationPolicy"
+ "TQ,V_volumeIndex"
+ "T^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}},V_apfs"
+ "T^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}},V_ino"
+ "Tq,?,R"
+ "Tq,?,R,VmaximumFileSizeInBits"
+ "Tq,?,R,VmaximumXattrSizeInBits"
+ "Tq,R"
+ "Tq,R,VmaximumLinkCount"
+ "Tq,R,VmaximumNameLength"
+ "Trying to update a namedstream inode %llx on volume %s\n"
+ "UNSET_FLAG_IS_SET(*set_flags)"
+ "UNSET_FLAG_IS_SET(dir_stats_state->op_flags)"
+ "YES"
+ "[%s] reply(%@ %@)"
+ "[%s] reply(%@)"
+ "[%s] reply(%@, %@)"
+ "[%s] reply(%@, %@, %@)"
+ "[%s] reply(%d, %@)"
+ "[%s] reply(%zu, %@)"
+ "^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}"
+ "^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16@0:8"
+ "^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}"
+ "^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}16@0:8"
+ "__apfs_dec_parent_nlink"
+ "_apfs"
+ "_fs_add_xattr"
+ "_ino"
+ "_omap_snapshot_create"
+ "_omap_snapshot_delete"
+ "_release_item_carefully"
+ "_remove_extents_of_file_cb"
+ "_remove_purgeable_record_cb"
+ "_rootItem"
+ "_setup_dir_stats_cb"
+ "_volumeIndex"
+ "accessTime"
+ "activateWithOptions:replyHandler:"
+ "addObject:"
+ "add_entry_to_dir_stack"
+ "alloc_space_for_write_with_hint_and_spino"
+ "alloc_tmp_ino_helper"
+ "apfs->apfs_fs_rr_total_blocks == 0"
+ "apfs->apfs_reverted_sb == NULL"
+ "apfs_clonegroup_check_solo_group"
+ "apfs_clonegroup_delete_inode"
+ "apfs_clonegroup_find_and_demote_last_full_clone"
+ "apfs_clonegroup_full_clone_scan"
+ "apfs_clonegroup_inode_became_partial_clone"
+ "apfs_clonegroup_insert_cookie"
+ "apfs_clonegroup_lock"
+ "apfs_clonegroup_lookup_locked"
+ "apfs_clonegroup_remove_dir_stats_key"
+ "apfs_clonegroup_remove_locked"
+ "apfs_clonegroup_unlock"
+ "apfs_clonegroup_update_dir_stats_key"
+ "apfs_clonegroup_update_locked"
+ "apfs_clonegroup_update_purgeable_urgency"
+ "apfs_clonegroup_validate_record_size"
+ "apfs_create_doc_id_tree_if_needed"
+ "apfs_free_data_blocks_if_needed"
+ "apfs_is_dir_empty"
+ "apfs_jhash_get_fsitem_internal"
+ "apfs_jhash_insert_fsitem"
+ "apfs_jhash_remove_fsitem"
+ "apfs_jhash_swap"
+ "apfs_jhash_try_insert_stream"
+ "apfs_keybag_load_class_keys"
+ "apfs_keybag_unlock_record"
+ "apfs_keybag_unlock_record_tag"
+ "apfs_lock_id"
+ "apfs_lock_inode_pair_internal"
+ "apfs_lock_phys_range"
+ "apfs_mark_inconsistent_"
+ "apfs_mount"
+ "apfs_mount_livefs"
+ "apfs_release_objects"
+ "apfs_set_file_size"
+ "apfs_trim_to_prev_fsize"
+ "apfs_unlock_id"
+ "apfs_unmount"
+ "apfs_update_cow_exempt_file_count"
+ "apfs_update_phys_range"
+ "appex_apfs_get_next_vol"
+ "appex_apfs_load_nodes"
+ "appex_apfs_mount"
+ "appex_combine_block_and_buf"
+ "appex_internal_blockmap"
+ "appex_internal_lookup"
+ "appex_load_inode"
+ "appex_nx_mount"
+ "appex_volume_is_mountable"
+ "atime"
+ "authapfs_seal_break"
+ "auto"
+ "automounted"
+ "birthTime"
+ "bm_poff == 0"
+ "bm_run == fs_bsize"
+ "browse"
+ "buf_size < fs_bsize"
+ "bytes"
+ "can not lock id zero\n"
+ "can't return crypto_id if it's a tweak\n"
+ "check_stale_doc_id_index"
+ "child_remover_cb"
+ "child_size_calculator_cb"
+ "clean_up_doc_id_trees_if_needed"
+ "clear"
+ "clear_invalid_fixups"
+ "clearing"
+ "clone_extents_adjust_dstream_cryptoid_if_needed"
+ "clone_extents_if_needed_with_gst"
+ "clone_fext_resources"
+ "clone_fexts_"
+ "clone_file_fexts"
+ "clone_iteratively"
+ "clone_mapping.c"
+ "clone_mapping_clear_flags"
+ "clone_mapping_remove"
+ "clone_mapping_remove_locked"
+ "clone_mapping_update_flags"
+ "clone_split_fext"
+ "com.apple.BootInfo"
+ "com.apple.apfs.appex"
+ "com.apple.rootless"
+ "combined_data"
+ "commit_ino_clonesplit"
+ "committmpcp"
+ "compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n"
+ "consumedAttributes"
+ "copy"
+ "could not get the current executable path of %s\n"
+ "could not open %s to prevent reclaims: %s\n"
+ "createItem:type:attributes:content:volumeIndex:outItem:"
+ "createItemNamed:type:inDirectory:attributes:replyHandler:"
+ "createLinkToItem:named:"
+ "createLinkToItem:named:inDirectory:replyHandler:"
+ "createSymbolicLinkNamed:inDirectory:attributes:linkContents:replyHandler:"
+ "create_empty_extentref_tree"
+ "create_sibling_link"
+ "createtmpcp"
+ "cur_fext->phys_block_num == 0"
+ "curr_xid && (curr_xid != ((xid_t)~0ULL))"
+ "cursor == OBJ_ID_FROM_KEY(key.hdr)"
+ "dataWithBytes:length:"
+ "deactivateItem:replyHandler:"
+ "deactivateWithOptions:replyHandler:"
+ "dealloc"
+ "decrement-dstream-id-for-deletion"
+ "decrement_dstream_id_for_deletion"
+ "default"
+ "defwrite"
+ "delta_from_dir_stats"
+ "demomode"
+ "dereference"
+ "dev"
+ "device_is_mounted(%s) failed with error: %s\n"
+ "didFinishLoading"
+ "dir_stats.chained_key != dir_stats.hdr.obj_id"
+ "dir_stats_are_expanded(apfs)"
+ "dir_stats_get_all_ancestors_attributes"
+ "dir_stats_get_flags"
+ "dir_stats_move_origin"
+ "dir_stats_move_regular_origin"
+ "dir_stats_moved"
+ "dir_stats_op_ext"
+ "dir_stats_origin_can_be_moved"
+ "dir_stats_required_op_from_flags"
+ "dir_stats_set_purgeable_state"
+ "dir_stats_update_reconciliation"
+ "doc_id_tree_create"
+ "doc_id_tree_destroy"
+ "doc_id_tree_invalid_crypto"
+ "dst_poff == 0"
+ "dst_run <= fs_bsize"
+ "dump_extents_of_stream"
+ "enableOpenUnlinkEmulation"
+ "enumerate:verifier:attributes:packer:"
+ "enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:"
+ "exec"
+ "extent_remover_callback"
+ "fext->phys_block_num"
+ "fext_collector"
+ "fileIsCompressed"
+ "filter_purgeable_flags_for_vol"
+ "first_pbn != 0"
+ "fixup-hardlink-progress"
+ "flags"
+ "follow"
+ "freeFiles"
+ "free_all_iterators"
+ "free_allocated_snapshot_extents"
+ "free_fext_resources"
+ "free_tmp_ino_helper"
+ "fs_delete_inode_internal"
+ "fs_destroy_shadow_fs_root_tree"
+ "fs_get_inode_with_hint"
+ "fs_get_xattr_ext"
+ "fs_insert_fext_record"
+ "fs_insert_snapshot_metadata"
+ "fs_is_phys_range_writable"
+ "fs_make_hole_range_writable"
+ "fs_make_phys_range_writable"
+ "fs_map_file_offset_ext"
+ "fs_remove_snapshot_metadata"
+ "fs_remove_xattr_with_nstream_inode"
+ "fs_rename_snapshot"
+ "fs_update_unwritten_extent_record"
+ "fs_write_stream"
+ "fsize"
+ "fv_create_pdk"
+ "getAttributes:"
+ "getAttributes:completionHandler:"
+ "getAttributes:ofItem:replyHandler:"
+ "getInoType"
+ "getItemSizes:"
+ "getXattr:data:"
+ "getXattrNamed:ofItem:replyHandler:"
+ "get_dir_stats"
+ "get_dir_stats_by_key"
+ "get_dstream_id_refcnt"
+ "get_fext_crypto_logic"
+ "get_ino_purgeable_size_and_compressed"
+ "get_new_crypto_id_if_needed"
+ "get_offset_position"
+ "get_purgeable_record_details"
+ "get_purgeable_record_id_for_lookup"
+ "get_purgeable_sizes_of_dir"
+ "get_unwrapped_ekwk_snap"
+ "get_vol_crypto(apfs) != VOL_PFKEY"
+ "gid"
+ "groupquota"
+ "hasNoneDefaultCreateAttrs:"
+ "hasReadOnlyAttrs:"
+ "hcp_clone_ek"
+ "hcp_get_class_ek"
+ "hcp_get_class_ek_uncached"
+ "hcp_is_cpclass(apfs, c)"
+ "i24@0:8Q16"
+ "i24@0:8^@16"
+ "i28@0:8Q16B24"
+ "i32@0:8@16@24"
+ "i32@0:8@16^@24"
+ "i32@0:8@16^{j_dir_rec={apfs_object=CCSQ}QQ{x_fields=SSSS^{x_field}^v}ISS*}24"
+ "i40@0:8@16@24Q32"
+ "i40@0:8@16q24^Q32"
+ "i48@0:8Q16Q24@32@40"
+ "i56@0:8@16@24@32@40@48"
+ "i56@0:8@16q24Q32@40^Q48"
+ "i64@0:8@16q24@32@40Q48^@56"
+ "icp_clone_ek"
+ "id != default_crypto_id"
+ "id %llu not in crypto cache"
+ "id %llu was expected to be held but it's not!\n"
+ "id %llu was locked but not by the current thread!\n"
+ "id is zero\n"
+ "init"
+ "initWithBytes:length:encoding:"
+ "initWithCString:"
+ "initWithFileSystemTypeName:"
+ "initWithIndex:volumeID:volumeName:resource:"
+ "initWithString:"
+ "initWithVolumeID:volumeName:"
+ "initWithino:apfs:devNumber:"
+ "init_dir_stats_xfields"
+ "ino %lld illogical file extent %lld:%lld != alloced_size %lld (fsize %lld)\n"
+ "ino %lld pos:len %lld:%lld fext %lld:%lld (%lld)\n"
+ "ino %lld you must have an extent covering the alloced size %lld (fsize %lld) orig_pos %lld:%lld err %d\n"
+ "ino->ekwk == cur_ekwk"
+ "ino->ekwk == ekwk"
+ "ino->rsrc_ekwk != ekwk"
+ "ino->rsrc_ekwk == cur_ekwk"
+ "ino_get_ekwk_"
+ "ino_get_ekwk_id"
+ "ino_get_ekwk_uncached"
+ "ino_is_dir_stats_origin_full(apfs, ino)"
+ "ino_name"
+ "ino_phys_size_ext"
+ "ino_set_rage"
+ "inode (id %llu): finder info internal flag is missing\n"
+ "inode (id %llu): finder info internal flag is unexpectedly set\n"
+ "inode (id %llu): security xattr internal flag is unexpectedly set\n"
+ "insert"
+ "insert_linkid"
+ "insert_phys_extent"
+ "insert_purgeable_record"
+ "inum != 0"
+ "invalid crypto id %llu"
+ "invalid offset (%llu) for last fext lookup\n"
+ "isAttributeWanted:"
+ "isEqualToString:"
+ "isPreallocateInhibited"
+ "isValid:"
+ "isVolumeRenameInhibited"
+ "is_non_iterative_extent_manipulation_faster"
+ "itemDeactivationPolicy"
+ "iterate_dirents_case_or_norm_insensitive"
+ "iterate_expanded_purgeable_records"
+ "iterate_ino_crypto_state"
+ "iterate_purgeable_records"
+ "iterative_fext_cloner"
+ "iteratively_clone_extents_of_file"
+ "jdev_fext_read_data"
+ "jdev_fext_write_data"
+ "jobj->type == APFS_EXPANDED_TYPE_CLONE_MAPPING"
+ "jobj_snap.c"
+ "kind == NEW && refcnt = %d\n"
+ "last_clone_cb"
+ "legacy_get_ek"
+ "length > (max_contig_blocks * fs_bsize)"
+ "listXattrs:"
+ "listXattrsOfItem:replyHandler:"
+ "load"
+ "loadtmpcp"
+ "lookupItemNamed:inDirectory:replyHandler:"
+ "lookup_and_remove_purgeable_record"
+ "lookup_expanded_purgeable_record"
+ "lookup_jobj_ext"
+ "lookup_purgeable_drec"
+ "lookup_purgeable_drec_as_record"
+ "make_purgeable_drec_xfs_from_record"
+ "map capacity overflow %lu"
+ "map->capacity <= map->max_capacity"
+ "map->next_index <= map->capacity"
+ "mark"
+ "mark_doc_id_index_for_rebuild_if_needed"
+ "marking"
+ "maximumFileSize"
+ "maximumFileSizeInBits"
+ "maximumLinkCount"
+ "maximumNameLength"
+ "maximumXattrSize"
+ "maximumXattrSizeInBits"
+ "merge_ino_purgeable_flags"
+ "mode"
+ "modification"
+ "modifyTime"
+ "mountWithOptions:replyHandler:"
+ "move_inode_to_purgatory_ext"
+ "move_snapshot_to_purgatory"
+ "n"
+ "name"
+ "nameWithString:"
+ "name_len > 0"
+ "name_len > 0 && name_len <= UINT16_MAX"
+ "neighbors == NULL || !(neighbors->first_is_adjacent && neighbors->last_is_adjacent) || (OBJ_ID_FROM_KEY(neighbors->first_key.hdr) != OBJ_ID_FROM_KEY(neighbors->last_key.hdr))"
+ "new_ino_clonesplit_src"
+ "new_sparse_bytes < 0"
+ "no"
+ "no-name"
+ "obj_subtype(tree) == OBJECT_TYPE_FEXT_TREE || obj_subtype(tree) == OBJECT_TYPE_PFKUR_TREE"
+ "obj_type(tree) == OBJECT_TYPE_BTREE"
+ "object_in_jhash"
+ "object_in_jhash(apfs, old_obj->dev, old_obj->hdr.obj_id, old_obj->hdr.type, NULL, FALSE)"
+ "offset > fext->logical_addr + fext->len"
+ "offsets[midpoint].off != BTOFF_MT_GHOST"
+ "old_id != new_id"
+ "old_obj->dev == new_obj->dev"
+ "old_obj->hdr.obj_id == new_obj->hdr.obj_id"
+ "old_obj->hdr.type == new_obj->hdr.type"
+ "old_obj->jhash_flags & (JH_RESERVED | JH_BUSY)"
+ "omap_revert_to_snapshot"
+ "orig_fext->phys_block_num != 0"
+ "orig_fext->phys_block_num == 0"
+ "orig_fext_crypto_id == CRYPTO_ONEKEY_ID"
+ "orphan_snap_check_iterator"
+ "owners"
+ "packDot:diter:is_parent:"
+ "packEntryWithName:itemType:itemID:nextCookie:attributes:"
+ "perm"
+ "preallocateInhibited"
+ "preallocateSpaceForItem:atOffset:length:flags:replyHandler:"
+ "protect"
+ "purgatory_cleaner_cb"
+ "purging.c"
+ "q"
+ "q16@0:8"
+ "quarantine"
+ "raw_xattr_remover"
+ "rdonly"
+ "readFromFile:offset:length:intoBuffer:actuallyRead:"
+ "readFromFile:offset:length:intoBuffer:replyHandler:"
+ "readSymbolicLink:outContent:"
+ "readSymbolicLink:replyHandler:"
+ "real_crypto != NULL"
+ "rec_size <= UINT16_MAX"
+ "received null APFSItem"
+ "reclaimItem:replyHandler:"
+ "recursively_remove_extents_of_dir"
+ "reference"
+ "refresh"
+ "refreshing"
+ "remove"
+ "removeDirectory:DirectoryEntry:"
+ "removeFile:DirectoryEntry:"
+ "removeItem:name:"
+ "removeItem:named:fromDirectory:replyHandler:"
+ "remove_clone_mapping_if_last"
+ "remove_dir_entry_ext"
+ "remove_dir_stats_key_on_ino_and_clone_mapping"
+ "remove_dstream_id_and_fexts_copy"
+ "remove_extent_of_file"
+ "remove_hash_file_info_record"
+ "remove_purgatory_entry"
+ "remove_purgeable_record"
+ "renameItem:inDirectory:named:toNewName:inDirectory:overItem:replyHandler:"
+ "renameItem:inDirectory:named:toNewName:overItem:"
+ "requestedMountOptions"
+ "res->new_sparse_bytes <= 0"
+ "res->xid %lld but xid is now %lld\n"
+ "restrictsOwnershipChanges"
+ "ret"
+ "retain_xdstream_crypto_states"
+ "revert_extents_iterator"
+ "revert_extents_to_snapshot"
+ "revert_to_snapshot"
+ "ro"
+ "rootItem"
+ "rounded_up_opos != OPOS_AFTER_END"
+ "rounded_up_opos == OPOS_AT_END"
+ "runtime_retains()"
+ "runtime_supports_hcp()"
+ "rw"
+ "sanitize_op_flags"
+ "sanity_check_alloced_blocks"
+ "save_dir_iterator"
+ "scalable_id_is_valid(apfs, id)"
+ "scanVolumes:"
+ "set"
+ "setAccessTime:"
+ "setAllocSize:"
+ "setApfs:"
+ "setAttributes:error:"
+ "setAttributes:onItem:replyHandler:"
+ "setAvailableBlocks:"
+ "setBirthTime:"
+ "setBlockSize:"
+ "setCaseFormat:"
+ "setChangeTime:"
+ "setConsumedAttributes:"
+ "setDoesNotSupportSettingFilePermissions:"
+ "setEnableOpenUnlinkEmulation:"
+ "setFileID:"
+ "setFileSystemSubType:"
+ "setFlags:"
+ "setFreeBlocks:"
+ "setFreeFiles:"
+ "setGid:"
+ "setIno:"
+ "setIoSize:"
+ "setItemSizes:"
+ "setLinkCount:"
+ "setMode:"
+ "setModifyTime:"
+ "setParentID:"
+ "setPreallocateInhibited:"
+ "setRequestedMountOptions:"
+ "setRootItem:"
+ "setSize:"
+ "setSupports2TBFiles:"
+ "setSupports64BitObjectIDs:"
+ "setSupportsDocumentID:"
+ "setSupportsFastStatFS:"
+ "setSupportsHardLinks:"
+ "setSupportsHiddenFiles:"
+ "setSupportsPersistentObjectIDs:"
+ "setSupportsSharedSpace:"
+ "setSupportsSymbolicLinks:"
+ "setSupportsZeroRuns:"
+ "setTotalBlocks:"
+ "setTotalFiles:"
+ "setType:"
+ "setUid:"
+ "setUsedBlocks:"
+ "setVolumeIndex:"
+ "setVolumeName:replyHandler:"
+ "setVolumeRenameInhibited:"
+ "setWantedAttributes:"
+ "setXattr:toData:policy:"
+ "setXattrNamed:toData:onItem:policy:replyHandler:"
+ "setXattrOperationsInhibited:"
+ "set_cloneinfo_id_epoch"
+ "set_dir_stats"
+ "set_dir_stats_for_SAF"
+ "set_dir_stats_handle_origin"
+ "set_ino_purgeable_state"
+ "setting"
+ "setup_demo_mode"
+ "should_embed_xattr"
+ "size"
+ "size_tracking.c"
+ "size_tracking_untrack_inode"
+ "skipsanity"
+ "snk->ekwk"
+ "src->ekwk != snk->ekwk"
+ "src->phys_block_num"
+ "state->src->ekwk && state->snk->ekwk"
+ "string"
+ "suid"
+ "supplemental_tree.c"
+ "supplemental_tree_copy"
+ "supplemental_tree_get"
+ "supplemental_tree_revert"
+ "supportedVolumeCapabilities"
+ "supportedXattrNamesForItem:"
+ "sxid == xid"
+ "sxidprev == (omp->om_pending_revert_min - 1)"
+ "synchronizeWithFlags:replyHandler:"
+ "tinyobjcache"
+ "tmp-ino-"
+ "tmp-ino-xattr-dstream-0x%llx-0x%llx"
+ "tree"
+ "tree->o_fs"
+ "tree_type == fs_root"
+ "truncatesLongNames"
+ "trying to zero the superblock!\n"
+ "tx"
+ "tx_is_closing"
+ "uid"
+ "union"
+ "unmark"
+ "unmountWithReplyHandler:"
+ "unset"
+ "unset_dir_stats"
+ "unset_dir_stats_for_ino"
+ "unset_dir_stats_handle_origin"
+ "unsetting"
+ "update_dir_stats_key_on_ino_and_clone_mapping"
+ "update_file_extent"
+ "update_ino_purgeable_dstream_id"
+ "update_jobj"
+ "update_purgeable_clone_tracking"
+ "update_purgeable_record_time_and_flags"
+ "update_size_tracking_no_gencount_bump"
+ "update_size_tracking_purgeable_size"
+ "update_sparse_bytes"
+ "usableButLimitedProbeResult"
+ "userfs_meta_crypto_state_unwrap"
+ "userquota"
+ "v20@0:8B16"
+ "v20@?0@\"FSItemAttributes\"8i16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8Q16"
+ "v24@0:8^{apfs={obj=^{obj_cache}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16"
+ "v24@0:8^{j_inode={apfs_object=CCSQ}{?=^{j_hashed_obj}^^{j_hashed_obj}}^v^{jhash_mutex}iIC[7C]QQQQQQQ(?=ii)IIIIISS(?=Q{?=(?=ii)i})Q{_opaque_pthread_rwlock_t=q[192c]}(?={btree_hint=Q^v})(?={btree_hint=Q^v})(?={?=*i}{?=QQQQ(?={link_origins=^{link_origin}^^{link_origin}}{?=Q})^{j_inode}}{?={dir_iterators=^{dir_iterator}^^{dir_iterator}}III}){x_fields=SSSS^{x_field}^v}^{ekwk}^{ekwk}{_opaque_pthread_rwlock_t=q[192c]}}16"
+ "v28@?0Q8Q16i24"
+ "v32@0:8@\"FSFileName\"16@?<v@?@\"FSFileName\"@\"NSError\">24"
+ "v32@0:8@\"FSItem\"16@?<v@?@\"FSFileName\"@\"NSError\">24"
+ "v32@0:8@\"FSItem\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"FSItem\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FSTaskOptions\"16@?<v@?@\"FSItem\"@\"NSError\">24"
+ "v32@0:8@\"FSTaskOptions\"16@?<v@?@\"NSError\">24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"FSFileName\"16@\"FSItem\"24@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">32"
+ "v40@0:8@\"FSFileName\"16@\"FSItem\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"FSItemGetAttributesRequest\"16@\"FSItem\"24@?<v@?@\"FSItemAttributes\"@\"NSError\">32"
+ "v40@0:8@\"FSItemSetAttributesRequest\"16@\"FSItem\"24@?<v@?@\"FSItemAttributes\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
+ "v48@0:8@\"FSItem\"16@\"FSFileName\"24@\"FSItem\"32@?<v@?@\"FSFileName\"@\"NSError\">40"
+ "v48@0:8@\"FSItem\"16@\"FSFileName\"24@\"FSItem\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"FSItem\"24q32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSItemSetAttributesRequest\"32@\"FSFileName\"40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
+ "v56@0:8@\"FSFileName\"16@\"NSData\"24@\"FSItem\"32Q40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"FSFileName\"16q24@\"FSItem\"32@\"FSItemSetAttributesRequest\"40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
+ "v56@0:8@\"FSItem\"16q24Q32@\"FSMutableFileDataBuffer\"40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@\"FSItem\"16q24Q32Q40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8@16@24@32Q40@?48"
+ "v56@0:8@16q24@32@40@?48"
+ "v56@0:8@16q24Q32@40@?48"
+ "v56@0:8@16q24Q32Q40@?48"
+ "v64@0:8@\"FSItem\"16Q24Q32@\"FSItemGetAttributesRequest\"40@\"FSDirectoryEntryPacker\"48@?<v@?Q@\"NSError\">56"
+ "v64@0:8@16Q24Q32@40@48@?56"
+ "v72@0:8@\"FSItem\"16@\"FSItem\"24@\"FSFileName\"32@\"FSFileName\"40@\"FSItem\"48@\"FSItem\"56@?<v@?@\"FSFileName\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "voff <= btree_node_val_space_total(btn)"
+ "vol_crypto != VOL_PFKEY"
+ "volumeIndex"
+ "volumeRenameInhibited"
+ "volumeStatistics"
+ "we asked for %lld blocks but got %lld (orig %lld, blks_this_allocation %lld)\n"
+ "we asked for %lld blocks but got zero (paddr %lld) from spaceman_alloc() and no error.\n"
+ "writeContents:atOffset:actuallyWritten:"
+ "writeContents:toFile:atOffset:replyHandler:"
+ "xattr.c"
+ "xattrOperationsInhibited"
+ "xattr_key_size <= UINT16_MAX"
+ "xattr_key_size >= sizeof(j_xattr_key_t)"
+ "xattr_name_to_kind"
+ "xattr_val_size <= UINT16_MAX"
+ "xattr_val_size >= sizeof(j_xattr_val_t)"
+ "xid == ((xid_t)~0ULL)"
+ "yes"
+ "zeroTailOfBlock:locked:"
+ "zero_tail_of_last_block"
+ "\x82"
- "\t%16p %s\n"
- "!(flags & ~(BT_MODIFY | BT_LOCK | BT_IGNORE_CORRUPT | BT_RAGE | BT_CACHED | BT_ASYNC | BT_PREFETCH))"
- "!bind_kek"
- "!cur_wvek.data"
- "%s: Context is null, can't log message"
- "%s: Expected to read %lu bytes, read %lu"
- "%s: Failed to read, error %ld"
- "%s: Given device is not a block device"
- "%s: No message connection object, can't log message"
- "%s: done"
- "%s: loaded resource with ID (%@)"
- "%s: started to format resource"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: failed to generate new sibling vek, err = 0x%x\n"
- "%s:%d: failed to lookup sibling wvek for uuid = %s, err = %d\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
- "%s:start"
- "(space == BTNODE_SPACE_KEY) || (space == BTNODE_SPACE_VAL)"
- "-f"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/nx/obj.c"
- "2632.80.1.0.1"
- "Allocated %s object with OID %lld flags %llx type %x %d from\n"
- "FSFileSystemOperations"
- "addr < dev->dev_block_count"
- "apfs->sibling_apfs->apfs_crypto.cpx"
- "btree_node_free_list_get"
- "count <= (dev->dev_block_count - addr)"
- "cur_wvek.data"
- "dev_is_mounted(%s) failed with error: %s\n"
- "didFinishLaunching"
- "ephemeral"
- "fd_dev_hint"
- "fd_dev_hint_flush"
- "hint"
- "index + findcount <= search_end"
- "invalid option -S should follow -E\n"
- "lookup_jobj_in_snap"
- "skipping purgeable cross checks\n"
- "space == BTNODE_SPACE_KEY || space == BTNODE_SPACE_VAL"
- "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "virtual"
- "voff <= vsize"

```
