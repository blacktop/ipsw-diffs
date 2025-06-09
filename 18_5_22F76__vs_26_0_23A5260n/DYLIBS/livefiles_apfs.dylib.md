## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0xb3bf0
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__const: 0x8200
-  __TEXT.__oslogstring: 0x145e1
-  __TEXT.__cstring: 0x4eb2
-  __TEXT.__unwind_info: 0xf20
+2632.0.15.0.1
+  __TEXT.__text: 0xbdd70
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__const: 0x85c0
+  __TEXT.__oslogstring: 0x15ab7
+  __TEXT.__cstring: 0x54c5
+  __TEXT.__unwind_info: 0xfd8
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__const: 0x410
+  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__const: 0x470
   __AUTH_CONST.__cfstring: 0x120
   __AUTH.__data: 0x258
   __DATA.__data: 0x98
-  __DATA.__bss: 0x81
   __DATA.__common: 0x438
+  __DATA.__bss: 0x81
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E2C601E4-338F-333C-AD3E-9164F7ACAB2F
-  Functions: 2312
-  Symbols:   5281
-  CStrings:  2060
+  UUID: FCDA2402-91EC-32A8-9E50-447040B94D78
+  Functions: 2425
+  Symbols:   5454
+  CStrings:  2189
 
Symbols:
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ __apfs_calloc_typed
+ __apfs_malloc_typed
+ __apfs_realloc_typed
+ __fv_hw_crypt_no_ephdm
+ _apfs_clonegroup_delete_inode
+ _apfs_clonegroup_find_and_demote_last_full_clone
+ _apfs_clonegroup_find_and_demote_last_full_clone.cold.1
+ _apfs_clonegroup_find_and_demote_last_full_clone.cold.2
+ _apfs_clonegroup_get_physical_size_if_full_clone
+ _apfs_clonegroup_id_from_ino
+ _apfs_clonegroup_inode_became_full_clone
+ _apfs_clonegroup_inode_became_partial_clone
+ _apfs_clonegroup_insert_inode
+ _apfs_clonegroup_key_cmp
+ _apfs_clonegroup_lock
+ _apfs_clonegroup_lookup
+ _apfs_clonegroup_lookup_locked
+ _apfs_clonegroup_lookup_locked.cold.1
+ _apfs_clonegroup_next_id
+ _apfs_clonegroup_remove_dir_stats_key
+ _apfs_clonegroup_remove_locked
+ _apfs_clonegroup_remove_locked.cold.1
+ _apfs_clonegroup_unlock
+ _apfs_clonegroup_update_dir_stats_key
+ _apfs_clonegroup_update_locked
+ _apfs_clonegroup_update_locked.cold.1
+ _apfs_clonegroup_update_locked.cold.2
+ _apfs_clonegroup_update_purgeable_urgency
+ _apfs_get_clonegroup_tree_ext
+ _apfs_has_clonegroup
+ _apfs_invalid_fixups
+ _apfs_ufileop_clonefile
+ _apfs_ufileop_link.cold.5
+ _apfs_ufileop_link.cold.6
+ _apfs_ufileop_link.cold.7
+ _apfs_uvfsop_check.cold.10
+ _apfs_uvfsop_check.cold.11
+ _apfs_uvfsop_check.cold.12
+ _authapfs_hash_comparison_size
+ _clean_stream_xattr
+ _clean_stream_xattr.cold.1
+ _clear_invalid_fixups
+ _clear_invalid_fixups.cold.1
+ _clone_children_cb
+ _clone_children_cb.cold.1
+ _clone_children_cb.cold.2
+ _clone_inode
+ _clone_inode.cold.1
+ _clone_inode.cold.2
+ _clone_item
+ _clone_item.cold.1
+ _clone_item.cold.2
+ _clone_item.cold.3
+ _clone_item.cold.4
+ _clone_item.cold.5
+ _clone_item.cold.6
+ _clone_item.cold.7
+ _clone_item.cold.8
+ _clone_item.cold.9
+ _clone_large_ea_extents
+ _clone_rsrcfork
+ _clone_rsrcfork.cold.1
+ _clone_rsrcfork.cold.2
+ _clone_rsrcfork.cold.3
+ _clone_rsrcfork_fexts_helper
+ _clone_rsrcfork_fexts_helper.cold.1
+ _clone_rsrcfork_fexts_helper.cold.2
+ _clone_rsrcfork_fexts_helper.cold.3
+ _clone_symlink
+ _clone_xattrs
+ _compressed_ino_phys_size
+ _cp_clone_dstream_crypto
+ _cp_new_rsrcfork_crypto_id
+ _cp_new_rsrcfork_crypto_id.cold.1
+ _dir_stats_mark_needs_reconciliation
+ _dir_stats_mark_needs_reconciliation.cold.1
+ _dir_stats_move_prepare
+ _dir_stats_moved
+ _dir_stats_moved.cold.1
+ _dir_stats_moved.cold.2
+ _dir_stats_moved.cold.3
+ _fd_write
+ _fext_cleaner
+ _fext_cleaner.cold.1
+ _fext_cleaner.cold.2
+ _fext_cleaner.cold.3
+ _fext_cloner
+ _fext_cloner.cold.1
+ _fext_cloner.cold.2
+ _fext_cloner.cold.3
+ _fs_obj_clone_name_checked
+ _fs_obj_clone_name_checked.cold.1
+ _fs_obj_clone_name_checked.cold.10
+ _fs_obj_clone_name_checked.cold.2
+ _fs_obj_clone_name_checked.cold.3
+ _fs_obj_clone_name_checked.cold.4
+ _fs_obj_clone_name_checked.cold.5
+ _fs_obj_clone_name_checked.cold.6
+ _fs_obj_clone_name_checked.cold.7
+ _fs_obj_clone_name_checked.cold.8
+ _fs_obj_clone_name_checked.cold.9
+ _fv_hw_crypt_ex
+ _get_ino_purgeable_size
+ _get_rsrcfork
+ _ino_get_rsrc_ekwk
+ _ino_put_rsrc_ekwk
+ _ino_set_purgeable_flags
+ _lookup_purgeable_flags
+ _lookup_purgeable_info
+ _nx_checkpoint_find_valid_checkpoint.cold.2
+ _nx_mount.cold.30
+ _nx_reaper_add_ext
+ _nx_reaper_add_ext.cold.1
+ _nx_reaper_add_ext.cold.2
+ _nx_reaper_add_ext.cold.3
+ _nx_reaper_add_ext.cold.4
+ _nx_reaper_add_ext.cold.5
+ _pipe
+ _pthread_rwlock_trywrlock
+ _purgeable_dir_size_is_stale
+ _purgeable_dir_size_is_stale.cold.1
+ _remove_dir_stats_key_on_ino_and_clone_mapping
+ _set_dir_stats_for_clone
+ _spaceman_free_handle_entitled_reserve
+ _spaceman_unreserve.cold.3
+ _spaceman_unreserve.cold.4
+ _spaceman_unreserve.cold.5
+ _spaceman_unreserve.cold.6
+ _trim_file_tail_if_needed
+ _trim_file_tail_if_needed_ext
+ _trim_file_tail_if_needed_ext.cold.1
+ _update_clone_mapping_if_present
+ _update_clone_mapping_if_present.cold.1
+ _update_ino_purgeable_fsize
+ _update_ino_purgeable_fsize.cold.1
+ _update_size_tracking_no_gencount_bump
+ _update_size_tracking_no_gencount_bump.cold.1
+ _update_size_tracking_no_ino_no_gencount_bump
+ _userfs_clone_internal
+ _userfs_clone_internal.cold.1
+ _userfs_decmpfs_file_is_dataless
+ _userfs_decmpfs_file_is_type5
+ _write
+ _xattr_cloner
+ _xattr_cloner.cold.1
+ _xattr_fext_counter
+ _xattr_is_kind
+ _xattr_nrec_counter
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_69
- _OUTLINED_FUNCTION_75
- __apfs_malloc
- __apfs_realloc
- _apfs_check_for_spillover
- _apfs_check_ino_for_spillover
- _authapfs_hash_size
- _dev_set_tier2_device
- _fusion_mt_key_cmp
- _fv_hw_crypt
- _fv_set_protection.cold.7
- _get_spacemanalloc_flags_for_inode
- _nx_check_omap.cold.1
- _nx_check_omap.cold.2
- _nx_dev_init.cold.10
- _nx_dev_init.cold.11
- _nx_dev_init.cold.12
- _nx_dev_init.cold.7
- _nx_dev_init.cold.8
- _nx_dev_init.cold.9
- _nx_fusion_superblock_write
- _nx_obj_cache_reset
- _nx_reaper_add.cold.1
- _nx_reaper_add.cold.2
- _nx_reaper_add.cold.3
- _nx_reaper_add.cold.4
- _nx_reaper_add.cold.5
- _obj_cache_stats_init
- _omap_set.cold.1
- _omap_set.cold.2
- _readdir_pack_dot_dirents
- _size_tracking_ino_moved.cold.1
- _size_tracking_ino_moved.cold.2
- _size_tracking_ino_moved.cold.3
- _spaceman_fs_bounds_clear.cold.1
- _spaceman_fs_bounds_clear.cold.2
- _spaceman_size_info
- _tx_flush.cold.6
- _tx_unmount.cold.5
CStrings:
+ "!xattr_is_rsrc(xattr)"
+ "%s0x%llx"
+ "%s:%d: !! failed cloning ino %lld into dir %lld/%s (err %d)!!\n"
+ "%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld, below zero!?!\n"
+ "%s:%d: %s *** failed to insert clone inode %lld (dir %lld/%s, ret %d)\n"
+ "%s:%d: %s *** failed to set dest dstream on ino %lld (from %lld, ret = %d)\n"
+ "%s:%d: %s *** failed to update source %lld\n"
+ "%s:%d: %s Already partial! (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu)\n"
+ "%s:%d: %s BUG BUG BUG: ino %lld unbacked-alloced-size %lld.  capping it to %lld\n"
+ "%s:%d: %s Bad val size: %u (group:%llu inum:%llu priv_id:%llu)\n"
+ "%s:%d: %s Coludn't remove dir stats key from (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Coludn't update dir stats key on (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't find lock for (group:%llu inum:%llu priv_id:%llu)\n"
+ "%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu) : %s\n"
+ "%s:%d: %s Couldn't lookup (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't update (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't update other (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu new_priv_id:%llu): %s\n"
+ "%s:%d: %s Error finding/demoting last full clone (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Failed to insert new dir_rec for %s (fid %lld) in parent-dir 0x%.16llx (ret %d)\n"
+ "%s:%d: %s Failed to lookup purgeable record (inode %llu): %d (%s)\n"
+ "%s:%d: %s Failed to remove (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Found no other mapping. (group:%llu inum:%llu priv_id:%llu) count=%u found_inum=%u\n"
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s Inode has no clonegroup id! (inum:%llu priv_id:%llu new_priv_id:%llu)\n"
+ "%s:%d: %s Unable to calculate inode new fsize for %llu - it is not a regular file\n"
+ "%s:%d: %s Unexpected error searching (group:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Value too small:%u (group:%llu inum:%llu priv_id:%llu)\n"
+ "%s:%d: %s cannot clone file extents %llu, %d\n"
+ "%s:%d: %s could not fetch new clone %lld\n"
+ "%s:%d: %s could not remove obj-id %lld: %s (%d)\n"
+ "%s:%d: %s could not remove xattrs for obj-id %lld: %s (%d)\n"
+ "%s:%d: %s could not set dir-stats as part of recursive cloning: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n"
+ "%s:%d: %s couldn't get clonegroup tree err:%s\n"
+ "%s:%d: %s couldn't get clonegroup tree: %s\n"
+ "%s:%d: %s couldn't insert record err:%s\n"
+ "%s:%d: %s couldn't remove (group:%llu inum:%llu priv_id:%llu) err:%s\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s failed insert (group:%llu inum:%llu priv_id:%llu) err:%s\n"
+ "%s:%d: %s failed to alloc dir rec in error path, err=%d ret=%d\n"
+ "%s:%d: %s failed to alloc temp clone drec (name %s, err %d)\n"
+ "%s:%d: %s failed to cleanup fext %lld, for dstream id %lld, %s (%d)\n"
+ "%s:%d: %s failed to cleanup orphan fext %lld, for dstream id %lld, %s (%d)\n"
+ "%s:%d: %s failed to clone %s to %s (err %d)\n"
+ "%s:%d: %s failed to decrement the crypto state refcount for crypto_id %lld, %s (%d)\n"
+ "%s:%d: %s failed to decrement the crypto state refcount for default crypto_id %lld, %s (%d)\n"
+ "%s:%d: %s failed to decrement the refcount for pext %lld, %s (%d)\n"
+ "%s:%d: %s failed to get the new parent ino %lld (for cloning from %lld)\n"
+ "%s:%d: %s failed to increment refcnt on dstream id %llu, err: %d\n"
+ "%s:%d: %s failed to increment the crypto state refcount for crypto_id %lld, %s (%d)\n"
+ "%s:%d: %s failed to increment the crypto state refcount for default crypto_id %lld, %s (%d)\n"
+ "%s:%d: %s failed to increment the refcount for pext %lld, %s (%d)\n"
+ "%s:%d: %s failed to insert dead record in purgatory for failed clone w/ino # %lld (ret %d)\n"
+ "%s:%d: %s failed to insert dest_drec %lld:%s err %d\n"
+ "%s:%d: %s failed to remove temp clone name %s in private dir (err %d)\n"
+ "%s:%d: %s failed to set new name %s on clone\n"
+ "%s:%d: %s failed to set sparse byte count on inode %lld\n"
+ "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
+ "%s:%d: %s fs_tx_enter failed: %s (%d)\n"
+ "%s:%d: %s full clone scan failed (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s ino %lld alloced size is %lld but size is only %lld\n"
+ "%s:%d: %s ino %llu has different group_id (existing: %llu new: %llu)\n"
+ "%s:%d: %s ino %llu:%llu (orig size %llu:%llu) trimmed %llu extents, %llu blocks (ret %d)\n"
+ "%s:%d: %s insert of purgeable record (ino %llu, fsize %llu, size_delta %lld) failed: %d (%s)\n"
+ "%s:%d: %s lookup / remove of directory purgeable record (ino %llu, fsize %llu, size_delta %lld) failed: %d (%s)\n"
+ "%s:%d: %s name <%s> is TOO LONG! (%d / max %d)"
+ "%s:%d: %s set apfs_fixup_flags to %#llx\n"
+ "%s:%d: %s source inode(%lld) marked sparse, but missing extended field\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s there should have been an entry for the name %s ret %d\n"
+ "%s:%d: %s tree_iterator_next failed: %s\n"
+ "%s:%d: %s tried to increment refcount of a dead dstream id %llu\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: cannot clone %llu dstream crypto, %d\n"
+ "%s:%d: cannot clone %llu resource fork, %d\n"
+ "%s:%d: cannot clone rsrcfork fexts %llu, %d\n"
+ "%s:%d: cannot deref staged ek %llu, error %d\n"
+ "%s:%d: cannot insert rsrcfork %llu, %d\n"
+ "%s:%d: cannot remove resource fork %d\n"
+ "%s:%d: close on the read end of the pipe returned error: %d\n"
+ "%s:%d: close on the write end of the pipe returned error: %d\n"
+ "%s:%d: failed to clone xattr %lld:%s (source %lld) err %d\n"
+ "%s:%d: failed to close the write end of the buffer %d\n"
+ "%s:%d: failed to get ino %lld in dir %lld\n"
+ "%s:%d: failed to insert hardlink drec %lld:%s for file-id %lld (err %d)\n"
+ "%s:%d: key %u generation failed %d\n"
+ "%s:%d: locking id %llu, which is already locked by this thread\n"
+ "%s:%d: obj-id %lld is not a dir-rec and should be (type=%d)\n"
+ "%s:%d: spaceman_info failed: error %d\n"
+ "%s:%d: update_jobj() failed trying to increment ino %lld's link count, err %d\n"
+ "%s:%d: userfs_internal_lookup for inum %llu failed: %d\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s %s unlock %s (%d)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null KEK, file radar%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null VEK, file radar%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode blob%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode kek%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode vek%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s icloud recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s institutional recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek and unmanaged vek device protection mismatch vek:%x, kek:%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 2%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s personal recovery key%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep managed vek cannot have flag_no_ephdm%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unknown blob type %i%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys disable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys enable%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s user uuid unexpectedly match new kek uuid%s\n"
+ "(((owner->mode) & 0170000) == 0100000)"
+ "(((src->mode) & 0170000) == 0100000)"
+ "-r"
+ "2632.0.15.0.1"
+ "_O_vol_attributes_attr"
+ "apfs-clonegroup-lock-mutex"
+ "apfs_clonegroup_delete_inode"
+ "apfs_clonegroup_find_and_demote_last_full_clone"
+ "apfs_clonegroup_full_clone_scan"
+ "apfs_clonegroup_inode_became_full_clone"
+ "apfs_clonegroup_inode_became_partial_clone"
+ "apfs_clonegroup_insert_inode"
+ "apfs_clonegroup_lock"
+ "apfs_clonegroup_lookup_locked"
+ "apfs_clonegroup_remove_dir_stats_key"
+ "apfs_clonegroup_remove_locked"
+ "apfs_clonegroup_unlock"
+ "apfs_clonegroup_update_dir_stats_key"
+ "apfs_clonegroup_update_locked"
+ "apfs_clonegroup_update_purgeable_urgency"
+ "clean_stream_xattr"
+ "clear_invalid_fixups"
+ "clone_children_cb"
+ "clone_ea_ctx.err != (-1)"
+ "clone_inode"
+ "clone_item"
+ "clone_rsrcfork2"
+ "clone_stream_xattr"
+ "clonesplit_rsrc_snk_free"
+ "cp_new_crypto"
+ "fext_cleaner"
+ "fext_cloner"
+ "fs_obj_clone_name_checked"
+ "id"
+ "id == id_mut"
+ "ino->ekwk != ekwk"
+ "ino->rsrc_ekwk == ekwk"
+ "kind == XATTR_KIND_RSRCFORK || kind == XATTR_KIND_DECMPFS"
+ "new_rsrc_clonesplit_src"
+ "nx_reaper_add_ext"
+ "purgeable_dir_size_is_stale"
+ "remove_dir_stats_key_on_ino_and_clone_mapping"
+ "sanitize_rsrcfork(rsrcfork)"
+ "snk.ekwk"
+ "trim_file_tail_if_needed_ext"
+ "update_clone_mapping_if_present"
+ "update_ino_purgeable_fsize"
+ "update_size_tracking_no_gencount_bump"
+ "userfs_clone_internal"
+ "xattr_cloner"
- "%s%s:%s%s%s%s%u:%s%u:%s %s %s unlock %s (%d)%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sresult: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Internal Error: Null KEK, file radar%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Internal Error: Null VEK, file radar%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s error %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed to decode blob%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed to decode kek%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed to decode vek%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s icloud recovery key%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s institutional recovery key%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s kek and unmanaged vek device protection mismatch%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s kek constraint violation 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s kek constraint violation 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s personal recovery key%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s unknown blob type %i%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s unsupported vek type for sys disable%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s unsupported vek type for sys enable%s\n"
- "%s:%d: %s %s():%d: dir_nlink = %d for inum %lld, removing %lld?!\n"
- "%s:%d: %s container block size too small for tier2 device block size (%d < %d)\n"
- "%s:%d: %s couldn't read tier2 device superblock of size %d\n"
- "%s:%d: %s failed to set tier2 device: %d\n"
- "%s:%d: %s failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
- "%s:%d: %s superblock container size %lld greater than device size(s) %lld\n"
- "%s:%d: %s tier2 device superblock doesn't agree with main superblock\n"
- "%s:%d: %s xid %lld failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid, tier2=%d\n"
- "%s:%d: spaceman_size_info failed: error %d\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "2332.120.31.0.2"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
