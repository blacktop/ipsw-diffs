## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0xbf798
+2811.100.177.0.1
+  __TEXT.__text: 0xb4bec
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__const: 0x85c0
-  __TEXT.__oslogstring: 0x15d81
-  __TEXT.__cstring: 0x5549
-  __TEXT.__unwind_info: 0xfe8
+  __TEXT.__const: 0x8690
+  __TEXT.__oslogstring: 0x15dd3
+  __TEXT.__cstring: 0x59c5
+  __TEXT.__unwind_info: 0x1018
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x470
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH.__data: 0x258
-  __DATA.__data: 0x98
+  __AUTH.__data: 0x248
+  __DATA.__data: 0x9c
   __DATA.__common: 0x438
-  __DATA.__bss: 0x81
+  __DATA.__bss: 0x89
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 577FCAC4-D1B2-344B-A78F-9C5C163909CF
-  Functions: 2447
-  Symbols:   5506
-  CStrings:  2205
+  UUID: E9932E80-6915-3B26-99B5-E2BAEBB5AB00
+  Functions: 2540
+  Symbols:   5802
+  CStrings:  2216
 
Symbols:
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ __fv_pdk_derive_pre_ps
+ __include_codes_in_dsym
+ _apfs_udirop_rmdir_internal.cold.6
+ _apfs_udirop_rmdir_internal.cold.7
+ _btree_check_ext.cold.4
+ _clone_extents_if_needed_with_gst.cold.13
+ _clone_split_fext.cold.2
+ _cp_get_ek2.cold.3
+ _cp_get_ek2.cold.4
+ _cp_get_ek2.cold.5
+ _fs_get_xattr_ext
+ _fv_acm_process
+ _fv_create_pdk
+ _fv_decode_kek_blob_with_secret
+ _get_new_crypto_id_if_needed.cold.2
+ _icp_clone_ek.cold.1
+ _inloc_cmp
+ _ino_get_atime
+ _ino_get_ekwk_id.cold.1
+ _ino_set_rage
+ _ino_set_rage.rage_count
+ _iteratively_remove_purgeable_record
+ _iteratively_remove_purgeable_record.cold.1
+ _lookup_jobj_ext
+ _move_inode_to_purgatory_ext.cold.2
+ _nx_is_panic_on_cp_corruption_enabled
+ _obj_cache_drain_async_reads
+ _oc_finish_async_read
+ _remove_dir_entry_ext
+ _set_ino_purgeable_state.cold.8
+ _size_tracking_ino_moved_ext
+ _spaceman_info_internal
+ _update_size_tracking_no_gencount_bump.cold.2
+ _userfs_internal_remove.cold.8
+ _userfs_internal_remove.cold.9
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_72
- _OUTLINED_FUNCTION_77
- _OUTLINED_FUNCTION_78
- __fv_master_key_derive
- _apfs_cstrncmp
- _apfs_ufileop_rename.cold.15
- _authapfs_hash_comparison_size
- _container_keybag_operation.cold.1
- _container_keybag_operation.cold.2
- _fd_dev_close.cold.2
- _fd_dev_hint
- _fd_dev_hint_flush
- _fd_dev_hint_flush.cold.1
- _fext_tree_iterate_fexts
- _fs_get_xattr_in_snap
- _fv_get_kek_from_blob
- _lookup_jobj_in_snap
- _obj_exchange_phys
- _walk_file_extents
CStrings:
+ "%s:%d: %s Failed to update_jobj(ino %llu) when %s is transitioning from pending-purgeable to purgeable: %d (%s)\n"
+ "%s:%d: %s Invalid residency reason %d ino %llu\n"
+ "%s:%d: %s cp_corrupt_assert() failed: %s"
+ "%s:%d: %s inode %llu is already in purgatory\n"
+ "%s:%d: %s rapid-aged %llu inodes\n"
+ "%s:%d: victim_ino is NULL\n"
+ "%s:%d: victim_ino obj_id %llu does not match looked up inum %llu\n"
+ "%s:%d: victim_node obj_id %llu does not match looked up inum %llu\n"
+ "%s:%d: victim_node->ino is NULL\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh, Unexpected short PDK len%s\n"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/userfs_dirops.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/userfs_fileops.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/userfs_fileutils.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/apfs_userfs/userfs_vfsops.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/dir_iteration.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/fs_utils.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/purging.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/size_tracking.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/fscommon/xattr.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/jobj.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/jobj_snap.c"
+ "/Library/Caches/com.apple.xbs/D19F7E5A-0C89-47ED-A086-7CBFCF6FAD42/TemporaryDirectory.Gecsne/Sources/apfs_userfs/nx/obj.c"
+ "2811.100.177.0.1"
+ "Trying to update a namedstream inode %llx on volume %s\n"
+ "_N_f_subtype"
+ "apfs"
+ "fv_create_pdk"
+ "hcp_clone_ek"
+ "hcp_get_class_ek"
+ "icp_clone_ek"
+ "ino_"
+ "ino_get_ekwk_id"
+ "ino_set_rage"
+ "lookup_jobj_ext"
+ "name_len > 0"
+ "owner"
+ "remove_dir_entry_ext"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: %s obj_exchange_phys timed out!\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: failed to delete target inode (%llu) that was renamed-over: %d\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "%s:%d: malformed %s keybag%s\n"
- "%s:%d: unable to wipe %s keybag (%d)\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
- "%s:%u: cp_corrupt_assert() failed: %s"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/apfs_userfs/userfs_dirops.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/apfs_userfs/userfs_fileops.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/apfs_userfs/userfs_fileutils.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/apfs_userfs/userfs_vfsops.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/fscommon/dir_iteration.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/fscommon/fs_utils.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/fscommon/purging.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/fscommon/size_tracking.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/fscommon/xattr.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/nx/jobj.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/nx/jobj_snap.c"
- "/Library/Caches/com.apple.xbs/Sources/apfs_userfs/nx/obj.c"
- "2632.80.1.0.1"
- "btree_node_compact"
- "fd_dev_hint_flush"
- "keybag_operation"
- "lookup_jobj_in_snap"
- "obj_exchange_phys"
- "remove_dir_entry"

```
