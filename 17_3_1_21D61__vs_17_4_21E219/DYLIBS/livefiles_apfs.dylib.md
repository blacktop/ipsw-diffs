## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0xabff4
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__const: 0x7ff0
-  __TEXT.__oslogstring: 0x134dd
-  __TEXT.__cstring: 0x4cc1
-  __TEXT.__unwind_info: 0xf38
+2236.102.1.0.0
+  __TEXT.__text: 0xacabc
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__const: 0x8020
+  __TEXT.__oslogstring: 0x1395e
+  __TEXT.__cstring: 0x4d85
+  __TEXT.__unwind_info: 0xf5c
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x2d0
   __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH.__data: 0x238
   __DATA.__data: 0x98
   __DATA.__bss: 0x81

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2570
-  Symbols:   5261
-  CStrings:  1969
+  Functions: 2579
+  Symbols:   5280
+  CStrings:  1989
 
Symbols:
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_80
+ _apfs_udirop_rmdir_internal.cold.5
+ _apfs_ufileop_rename.cold.15
+ _calloc
+ _dir_stats_kill
+ _dir_stats_op_ext
+ _dir_stats_op_ext.cold.1
+ _dir_stats_op_ext.cold.2
+ _dir_stats_op_ext.cold.3
+ _dir_stats_op_ext.cold.4
+ _dir_stats_required_op_from_flags
+ _fext_tree_lookup_ext
+ _fext_tree_lookup_last
+ _firebloom_ccpbkdf2_hmac
+ _fs_is_phys_range_writable
+ _ino_phys_size_ext
+ _ino_phys_size_ext.cold.1
+ _jobj_xfield_merge_64
+ _move_inode_to_purgatory_ext
+ _move_inode_to_purgatory_ext.cold.1
+ _remove_selected_and_stale_dir_iterators
+ _sanitize_op_flags
+ _sanitize_op_flags.cold.1
+ _sanitize_op_flags.cold.2
+ _sanitize_op_flags.cold.3
+ _sanitize_op_flags.cold.4
+ _sanitize_op_flags.cold.5
+ _sanitize_op_flags.cold.6
+ _sanitize_op_flags.cold.7
+ _sanitize_op_flags.cold.8
+ _sanitize_op_flags.cold.9
+ _set_dir_stats_handle_origin
+ _set_dir_stats_handle_origin.cold.1
+ _set_dir_stats_handle_origin.cold.2
+ _set_dir_stats_handle_origin.cold.3
+ _set_dir_stats_handle_origin.cold.4
+ _set_dir_stats_handle_origin.cold.5
+ _set_dir_stats_handle_origin.cold.6
+ _spaceman_scan_free_blocks.cold.4
+ _trim_time_tracking_check
+ _trim_time_tracking_end
+ _trim_time_tracking_start
+ _update_dir_stats_move_state
+ _userfs_internal_remove.cold.7
- _OUTLINED_FUNCTION_54
- _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_63
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_79
- _OUTLINED_FUNCTION_95
- __setup_dir_stats_cb.cold.4
- __setup_dir_stats_cb.cold.5
- __setup_dir_stats_cb.cold.6
- __setup_dir_stats_cb.cold.7
- __setup_dir_stats_cb.cold.8
- __setup_dir_stats_cb.cold.9
- _dir_stats_get_all_ancestors_attributes.cold.2
- _dir_stats_get_flags.cold.2
- _dir_stats_set_purgeable_state.cold.2
- _fs_obj_create_name_checked.cold.3
- _get_dir_stats.cold.2
- _get_dir_stats_by_key.cold.3
- _ino_phys_size.cold.1
- _jobj_merge_maybe_clamp_64
- _jobj_refcnt_merge.cold.10
- _jobj_refcnt_merge.cold.11
- _jobj_refcnt_merge.cold.9
- _move_inode_to_purgatory.cold.1
- _sanitize_set_flags
- _set_dir_stats.cold.10
- _set_dir_stats_from_flags
- _set_maintain_dir_stats_ext
- _set_maintain_dir_stats_ext.cold.1
- _set_maintain_dir_stats_ext.cold.2
- _set_maintain_dir_stats_ext.cold.3
- _set_maintain_dir_stats_ext.cold.4
- _set_maintain_dir_stats_ext.cold.5
- _size_tracking_ino_moved.cold.4
- _size_tracking_ino_moved.cold.5
- _update_dir_stats.cold.2
- _update_dir_stats_by_key_ext.cold.2
- _update_dir_stats_chained_key
- _update_size_tracking_purgeable_size.cold.2
CStrings:
+ "%s"
+ "%s:%d: %s %lld blocks free in %lld extents, avg %lld.%02lld\n"
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can only be used with SAF flags\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can't be specified alone\n"
+ "%s:%d: %s DS_OP_ONLY_SPACE_ATTRIBUTION can't be used externally\n"
+ "%s:%d: %s DS_OP_SET_BY_SPACE_ATTRIBUTION cannot be passed along with DS_OP_UNSET_BY_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_SET_BY_SPACE_ATTRIBUTION cannot be passed without DS_OP_SET_FOR_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_SET_FOR_SPACE_ATTRIBUTION cannot be passed along with DS_OP_UNSET_FOR_SPACE_ATTRIBUTION\n"
+ "%s:%d: %s DS_OP_[UN]SET_BY_SPACE_ATTRIBUTION can't be used internally\n"
+ "%s:%d: %s error finishing move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s error starting move for dir-stats %llu of ino %llu: %s (%d); size tracking may go out of sync\n"
+ "%s:%d: %s failed to kill shadow dir-stats %llu for dir-stats %llu (ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to remove kill dir-stats %llu for dir-stats %llu (ino %llu): %s (%d)\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: %s invalid dir-stats SET flags: 0x%llx\n"
+ "%s:%d: %s invalid op_flags for setting dir-stats: 0x%llx\n"
+ "%s:%d: %s no special dir-stats op flags are allowed on non-expanded volumes\n"
+ "%s:%d: %s trims dropped: %lld blocks %lld extents, avg %lld.%02lld \n"
+ "%s:%d: %s xid %llu tx stats: # %llu owait %llu %lluus finish %llu bar2 %lld f %lld enter %llu fq %llu %llu %lluus close %lluus prep %lluus flush %lluus\n"
+ "%s:%d: Failed to move ino %lld to purgatory from dir %lld : %d\n"
+ "2236.102.1"
+ "com.apple.system.fs.speculative_telemetry"
+ "dir_stats_op_ext"
+ "fs_is_phys_range_writable"
+ "hcp_get_class_ek_uncached"
+ "hcp_is_cpclass(apfs, c)"
+ "ino_phys_size_ext"
+ "invalid offset (%llu) for last fext lookup\n"
+ "move_inode_to_purgatory_ext"
+ "remove_selected_and_stale_dir_iterators"
+ "runtime_supports_hcp()"
+ "sanitize_op_flags"
+ "set_dir_stats_handle_origin"
- "%s:%d: %s %lld blocks free in %lld extents\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s allocate_phys_range failed, err = %d\n"
- "%s:%d: %s failed to remove shadow dir-stats %llu for dir-stats %llu (ino %llu): %s (%d)\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: %s invalid set_flags for setting dir-stats: 0x%llx\n"
- "%s:%d: %s xid %llu tx stats: # %llu finish %llu enter %llu wait %llu %lluus close %lluus flush %lluus\n"
- "2235.80.4.0.1"
- "ino_phys_size"
- "mcp_get_class_ek_uncached"
- "mcp_is_cpclass(apfs, c)"
- "move_inode_to_purgatory"
- "runtime_supports_mcp()"
- "set_maintain_dir_stats_ext"

```
