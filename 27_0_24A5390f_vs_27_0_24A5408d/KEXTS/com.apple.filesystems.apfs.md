## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-3283.0.13.0.0
+3288.2.1.0.0
   __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x4fdbb
-  __TEXT_EXEC.__text: 0x1512ec
-  __TEXT_EXEC.__auth_stubs: 0x2330
+  __TEXT.__cstring: 0x4ff2d
+  __TEXT_EXEC.__text: 0x1515a4
+  __TEXT_EXEC.__auth_stubs: 0x2360
   __DATA.__data: 0x75c
   __DATA.__bss: 0xd80
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x5440
   __DATA_CONST.__kalloc_var: 0x2bc0
   __DATA_CONST.__assert: 0x14
-  __DATA_CONST.__auth_got: 0x1198
+  __DATA_CONST.__auth_got: 0x11b0
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2400
+  Functions: 2396
   Symbols:   0
-  CStrings:  6952
+  CStrings:  6954
 
CStrings:
+ "%s:%d: %s (dstream_id %lld, flags %x) made %u evictions retries number of blocks to evict %llu, number of evicted blocks till now %llu\n"
+ "%s:%d: %s (dstream_id %lld, flags %x) throttled-pause fired %u times,number of blocks to evict %llu, number of evicted blocks till now %llu\n"
+ "%s:%d: %s _OP_GET_FILE_DSTREAMS requires the get-dstreams entitlement\n"
+ "%s:%d: %s _OP_GET_FILE_EXTS requires the get-file-exts entitlement\n"
+ "%s:%d: %s done processing snap xid %llu (err %d)\n"
+ "%s:%d: %s failed to find attribution tag record with s_hash <%llu> for already-tagged ino!\n"
+ "%s:%d: %s head RMW failed (%d) for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s ino %llu, failed to update cluster range, %llu+%llu, fsize %llu, error %d\n"
+ "%s:%d: %s ino %llu, failed to zero-fill range, %llu+%llu, fsize %llu, error %d\n"
+ "%s:%d: %s invalid zero-fill range for ino %llu, start %llu, length %llu, fsize %llu\n"
+ "%s:%d: %s partial unwritten coverage for ino %llu, page [%lld, %lld), range [%llu, %llu)\n"
+ "%s:%d: %s tail RMW failed (%d) for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s ubc_create_upl failed for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s zero-fill bitmap alloc failed for ino %llu, pages %u\n"
+ "2026/08/05"
+ "21:46:35"
+ "21:46:36"
+ "3288.2.1"
+ "Aug  5 2026"
+ "apfs-3288.2.1"
+ "apfs_zerofill_chunk_cb"
+ "apfs_zerofill_unwritten_range"
+ "com.apple.private.apfs.get-dstreams"
+ "com.apple.private.apfs.get-file-exts"
+ "decrement_dstream_id_for_deletion_ex"
- " or UNWRITTEN fexts"
- "%s:%d: %s Did not find snap meta in the jhash\n"
- "%s:%d: %s Failed to locate apfs of fsindex %llu, error %d\n"
- "%s:%d: %s Invalid fsoid, for fsindex %llu\n"
- "%s:%d: %s Looking for snapmeta in jhash, fsindex %llu, snapshot_xid %llu\n"
- "%s:%d: %s Snap meta found in jhash\n"
- "%s:%d: %s cluster_push() after msync failed with %d on ino(%llu)\n"
- "%s:%d: %s done processing snap xid %llu\n"
- "%s:%d: %s failed to update existing file info attribution tag record for s_hash <%llu> with <%s> <%d>\n"
- "%s:%d: %s ino %llu, prealloced region %llu+%llu is not covered by a file range%s, covered %llu+%llu, offset %llu\n"
- "%s:%d: %s nx_panic_on_corruption restored to %d\n"
- "%s:%d: %s nx_panic_on_corruption set to false\n"
- "%s:%d: %s nx_panic_on_cp_corruption restored to %d\n"
- "%s:%d: %s nx_panic_on_cp_corruption set to false\n"
- "%s:%d: %s preallocated range %llu+%zu is not covered by UNWRITTEN fexts, error %d\n"
- "2026/07/14"
- "21:11:49"
- "3283.0.13"
- "Jul 14 2026"
- "apfs-3283.0.13"
- "check_snap_meta_devt"
- "decrement_dstream_id_for_deletion"
- "ttl"
```
