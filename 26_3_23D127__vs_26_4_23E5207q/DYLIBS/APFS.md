## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0x50694
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__const: 0x8420
-  __TEXT.__cstring: 0xdde8
-  __TEXT.__oslogstring: 0xb0e
+2811.100.177.0.1
+  __TEXT.__text: 0x53350
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__const: 0x8540
+  __TEXT.__cstring: 0xe5d0
+  __TEXT.__oslogstring: 0x11b8
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x918
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x4e8
-  __AUTH_CONST.__auth_got: 0x5b8
+  __TEXT.__unwind_info: 0x950
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x550
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1180
-  __DATA.__data: 0x98
+  __AUTH_CONST.__cfstring: 0x12e0
+  __DATA.__data: 0x9c
   __DATA.__bss: 0x40
   __DATA.__common: 0x418
-  __DATA_DIRTY.__data: 0x168
+  __DATA_DIRTY.__data: 0x148
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 57369921-150B-337D-9DA5-DB9C1FF7F8F4
-  Functions: 809
-  Symbols:   1765
-  CStrings:  1445
+  UUID: 722AB8F2-5228-3D3F-B785-88BCB3591637
+  Functions: 881
+  Symbols:   1933
+  CStrings:  1541
 
Symbols:
+ _APFSPurgeExtentIteratorCopyState
+ _APFSPurgeExtentIteratorCopyState.cold.1
+ _APFSPurgeExtentIteratorCopyState.cold.2
+ _APFSPurgeExtentIteratorCreate
+ _APFSPurgeExtentIteratorCreate.cold.1
+ _APFSPurgeExtentIteratorCreate.cold.10
+ _APFSPurgeExtentIteratorCreate.cold.2
+ _APFSPurgeExtentIteratorCreate.cold.3
+ _APFSPurgeExtentIteratorCreate.cold.4
+ _APFSPurgeExtentIteratorCreate.cold.5
+ _APFSPurgeExtentIteratorCreate.cold.6
+ _APFSPurgeExtentIteratorCreate.cold.7
+ _APFSPurgeExtentIteratorCreate.cold.8
+ _APFSPurgeExtentIteratorCreate.cold.9
+ _APFSPurgeExtentIteratorCreateWithState
+ _APFSPurgeExtentIteratorCreateWithState.cold.1
+ _APFSPurgeExtentIteratorCreateWithState.cold.10
+ _APFSPurgeExtentIteratorCreateWithState.cold.11
+ _APFSPurgeExtentIteratorCreateWithState.cold.12
+ _APFSPurgeExtentIteratorCreateWithState.cold.13
+ _APFSPurgeExtentIteratorCreateWithState.cold.14
+ _APFSPurgeExtentIteratorCreateWithState.cold.15
+ _APFSPurgeExtentIteratorCreateWithState.cold.2
+ _APFSPurgeExtentIteratorCreateWithState.cold.3
+ _APFSPurgeExtentIteratorCreateWithState.cold.4
+ _APFSPurgeExtentIteratorCreateWithState.cold.5
+ _APFSPurgeExtentIteratorCreateWithState.cold.6
+ _APFSPurgeExtentIteratorCreateWithState.cold.7
+ _APFSPurgeExtentIteratorCreateWithState.cold.8
+ _APFSPurgeExtentIteratorCreateWithState.cold.9
+ _APFSPurgeExtentIteratorDestroy
+ _APFSPurgeExtentIteratorIterate
+ _APFSPurgeExtentIteratorIterate.cold.1
+ _APFSPurgeExtentIteratorIterate.cold.2
+ _CFRetain
+ _CFSetAddValue
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ __NSConcreteStackBlock
+ ___APFSPurgeExtentIteratorAssertValid
+ ___APFSPurgeExtentIteratorAssertValid.cold.1
+ ___APFSPurgeExtentIteratorAssertValid.cold.2
+ ___APFSPurgeExtentIteratorAssertValid.cold.3
+ ___APFSPurgeExtentIteratorAssertValid.cold.4
+ ___APFSPurgeExtentIteratorAssertValid.cold.5
+ ___APFSPurgeExtentIteratorCreate
+ ___APFSPurgeExtentIteratorCreate.cold.1
+ ___APFSPurgeExtentIteratorCreate.cold.10
+ ___APFSPurgeExtentIteratorCreate.cold.2
+ ___APFSPurgeExtentIteratorCreate.cold.3
+ ___APFSPurgeExtentIteratorCreate.cold.4
+ ___APFSPurgeExtentIteratorCreate.cold.5
+ ___APFSPurgeExtentIteratorCreate.cold.6
+ ___APFSPurgeExtentIteratorCreate.cold.7
+ ___APFSPurgeExtentIteratorCreate.cold.8
+ ___APFSPurgeExtentIteratorCreate.cold.9
+ ___APFSPurgeExtentIteratorIterate_block_invoke
+ ___assert_rtn
+ ___block_descriptor_tmp
+ ___block_descriptor_tmp.167
+ ___iterate_purge_directory_block_invoke
+ __include_codes_in_dsym
+ __os_assert_log
+ __os_crash
+ __os_log_debug_impl
+ _cf_dict_get_value
+ _cf_unwrap_uint64
+ _fd_is_eapfs.req
+ _ffsctl
+ _fgetattrlist
+ _free_purgeable_extents_iterator
+ _fts_read_fd_
+ _fts_set
+ _get_purgeable_extents_state
+ _get_urgencies.MAP
+ _inloc_cmp
+ _iterate_purge
+ _iterate_purge.cold.1
+ _iterate_purge.cold.2
+ _kAPFSPurgeExtentIteratorBatchSize
+ _kAPFSPurgeExtentIteratorOptions
+ _kAPFSPurgeExtentIteratorUrgency
+ _kCFTypeSetCallBacks
+ _lookup_jobj_ext
+ _make_purgeable_extents_iterator
+ _oc_finish_async_read
+ _set_purgeable_extents_state
+ _spaceman_info_internal
+ _statfs
+ _sysctlbyname
- _apfs_cstrncmp
- _btree_node_copy
- _fd_dev_hint
- _fd_dev_hint_flush
- _lookup_jobj_in_snap
- _obj_exchange_phys
CStrings:
+ "%@addcg_t=%llu "
+ "%@findcg_t=%llu "
+ "%@num_cg=%zu "
+ "%@snap_t=%llu "
+ "%s:%d: cannot create state from a completed iterator\n"
+ "%s:%d: creating a purge extent iterator is currently only supported on the root of an enhanced apfs volume\n"
+ "%s:%d: dir %llu no longer has a desired urgency\n"
+ "%s:%d: done err = %d\n"
+ "%s:%d: expected file %llu but got mode %#o ino %llu\n"
+ "%s:%d: expected inode entry but got extent %#llx:+%#llx\n"
+ "%s:%d: expected inode entry but got nothing\n"
+ "%s:%d: failed to allocate APFSPurgeExtentIterator\n"
+ "%s:%d: failed to allocate memory for extent iterator\n"
+ "%s:%d: failed to create purgeable extent iterator: %s (%d)\n"
+ "%s:%d: failed to create state dictionary\n"
+ "%s:%d: failed to disable rapid-aging vnodes: %s (%d)\n"
+ "%s:%d: failed to enable rapid-aging vnodes: %s (%d)\n"
+ "%s:%d: failed to fts_read(): %s (%d)\n"
+ "%s:%d: failed to get bulk purgeable extents: %s (%d)\n"
+ "%s:%d: failed to get fd for fts: %s (%d)\n"
+ "%s:%d: failed to get path for ino %llu: %s (%d)\n"
+ "%s:%d: failed to get purgeable extents for file %llu: %s (%d)\n"
+ "%s:%d: failed to get purgeable extents: %s (%d)\n"
+ "%s:%d: failed to get purgeable info for ino %llu: %s (%d)\n"
+ "%s:%d: failed to get requested attributes: %s (%d)\n"
+ "%s:%d: failed to iterate purgeable extents of dir %llu: %s (%d)\n"
+ "%s:%d: failed to open fts on ino %llu: %s (%d)\n"
+ "%s:%d: failed to open path: %s (%d)\n"
+ "%s:%d: failed to read fd from fts: %s (%d)\n"
+ "%s:%d: failed to skip fts for ino %llu: %s (%d)\n"
+ "%s:%d: failed to stat: %s (%d)\n"
+ "%s:%d: failed to statfs(%s): %s (%d)\n"
+ "%s:%d: fts_read() returned error: %s (%d)\n"
+ "%s:%d: incorrect version (actual %llu, expected %u)\n"
+ "%s:%d: invalid arguments\n"
+ "%s:%d: invalid arguments (active %#x, optional %#x, required %#x)\n"
+ "%s:%d: invalid combination of options (actual %#llx, expected %#llx)\n"
+ "%s:%d: invalid options dictionary\n"
+ "%s:%d: invalid state dictionary\n"
+ "%s:%d: iterate_purge() returned with ret = %d\n"
+ "%s:%d: kAPFSPurgeExtentIteratorBatchSize was invalid (%llu), must be between %u and %u\n"
+ "%s:%d: kAPFSPurgeExtentIteratorBatchSize was not an integer CFNumber\n"
+ "%s:%d: kAPFSPurgeExtentIteratorCursorAtime was not an integer CFNumber\n"
+ "%s:%d: kAPFSPurgeExtentIteratorCursorUrgency was invalid (%llu)\n"
+ "%s:%d: kAPFSPurgeExtentIteratorCursorUrgency was not an integer CFNumber\n"
+ "%s:%d: kAPFSPurgeExtentIteratorOptions had invalid options specified (%#llx)\n"
+ "%s:%d: kAPFSPurgeExtentIteratorOptions must include at least one option\n"
+ "%s:%d: kAPFSPurgeExtentIteratorOptions was not an integer CFNumber\n"
+ "%s:%d: kAPFSPurgeExtentIteratorPath was not a valid CFString\n"
+ "%s:%d: kAPFSPurgeExtentIteratorUrgency was invalid (%llu)\n"
+ "%s:%d: kAPFSPurgeExtentIteratorUrgency was not an integer CFNumber\n"
+ "%s:%d: kAPFSPurgeExtentIteratorVersion was not an integer CFNumber\n"
+ "%s:%d: no stat info requested\n"
+ "%s:%d: options was not a CFDictionary\n"
+ "%s:%d: ordered iteration must be reset once finished\n"
+ "%s:%d: processing dir %llu\n"
+ "%s:%d: processing file %llu with %u extents\n"
+ "%s:%d: skipping already seen dir %llu\n"
+ "%s:%d: skipping already seen file %llu\n"
+ "%s:%d: skipping already seen ino %llu\n"
+ "%s:%d: state was not a CFDictionary\n"
+ "%s:%d: stop iteration requested\n"
+ "%s:%d: unexpected attributes were returned\n"
+ "%s:%d: unexpected mode %#o for ino %llu\n"
+ "%s:%d: urgency %#06x done\n"
+ "(ent->fts_info == FTS_D) || (ent->fts_info == FTS_F)"
+ "/Library/Caches/com.apple.xbs/992F42F9-8D6E-4F06-8F00-436F9D8F0AD0/TemporaryDirectory.dOpYuv/Sources/apfs_framework/nx/obj.c"
+ "2811.100.177.0.1"
+ "APFSPurgeExtentIteratorCreate"
+ "APFSPurgeExtentIteratorCreateWithState"
+ "APFSPurgeExtentIteratorIterate"
+ "__APFSPurgeExtentIteratorCopyState"
+ "__APFSPurgeExtentIteratorCreate"
+ "com.apple.apfs.iterator.extent.purge.batch_size"
+ "com.apple.apfs.iterator.extent.purge.cursor.atime"
+ "com.apple.apfs.iterator.extent.purge.cursor.urgency"
+ "com.apple.apfs.iterator.extent.purge.options"
+ "com.apple.apfs.iterator.extent.purge.path"
+ "com.apple.apfs.iterator.extent.purge.urgency"
+ "com.apple.apfs.iterator.extent.purge.version"
+ "dir"
+ "fd_is_eapfs"
+ "fd_is_root"
+ "fts_openbyid_"
+ "fts_read_fd_"
+ "i16@?0^{purge_entry=i^{?}IQS}8"
+ "i8@?0"
+ "iterate_purge"
+ "iterate_purge_directory"
+ "kern.rage_vnode"
+ "lookup_jobj_ext"
+ "make_purgeable_extents_iterator"
+ "parse_options_into_args"
+ "parse_state_into_args"
+ "purging_util.c"
- "%s:%d: %s btree_node_insert_internal failed: %d\n"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "/Library/Caches/com.apple.xbs/Sources/apfs_framework/nx/obj.c"
- "2632.80.1.0.1"
- "btree_node_compact"
- "btree_node_copy"
- "fd_dev_hint_flush"
- "lookup_jobj_in_snap"

```
