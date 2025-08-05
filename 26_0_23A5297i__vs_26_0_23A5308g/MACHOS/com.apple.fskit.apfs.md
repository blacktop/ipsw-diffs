## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0xa73c8
+2632.0.77.0.1
+  __TEXT.__text: 0xa8530
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x88f0
-  __TEXT.__cstring: 0x2dfb7
+  __TEXT.__cstring: 0x2e50f
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__oslogstring: 0x11b
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methname: 0x51d
   __TEXT.__objc_methtype: 0x21e
-  __TEXT.__unwind_info: 0x1380
+  __TEXT.__unwind_info: 0x1398
   __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: AEE5554C-6CDD-32F4-BCB3-DE0808D39340
-  Functions: 2325
-  Symbols:   1192
-  CStrings:  3959
+  UUID: 0D8CF634-6C87-3DEA-953C-4421BAACE5AE
+  Functions: 2331
+  Symbols:   1197
+  CStrings:  3975
 
Symbols:
+ _clonegroup_get_file_ids_of_private_id
+ _clonegroup_register_dstream
+ _clonegroup_register_purgeable
+ _get_inode_64bit_xfield
+ _get_inode_phys_size
+ _spaceman_entitled_reserve_active
- _get_inode_xfield
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "2632.0.77.0.1"
+ "can't add attribution tag for clonegroup: %s (%d)\n"
+ "can't add dir stats key for clonegroup: %s (%d)\n"
+ "can't allocate memory to insert a new clonegroup value\n"
+ "can't cross check inode (id %llu) with its corresponding clonegroup record: %d (%s)\n"
+ "clone group mapping record missing for (group_id %llu, private_id %llu, file_id %llu)\n"
+ "clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n"
+ "clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n"
+ "clonegroup records of (private_id %llu) count (%u) != dstream_id refcount (%u)\n"
+ "clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect attribution tag (%llu)\n"
+ "clonegroup_record (group_id %llu, private_id %llu, file_id %llu) has incorrect dir-stats key (%llu)\n"
+ "compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): missing the full clone flag\n"
+ "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) repair: %s\n"
+ "file (id %llu) isn't purgeable but its matching clonegroup record flags (0x%x) suggest it is\n"
+ "file (id %llu) purgeable_flags (0x%x) disagree with its matching clonegroup record flags (0x%x)\n"
+ "file_id %llu (group_id %llu, private_id %llu) has different clonegroup group_id (%llu)\n"
+ "found clone mapping in a volume with initialized clonegroup tree\n"
+ "found multiple clonegroup records for file_id %llu\n"
+ "missing clone group record for file_id %llu (private_id %llu, group_id %llu)\n"
+ "number of files in clonegroup (%u) != dstream reference count (%u)\n"
+ "private_id (%llu) has multiple clonegroup ids (%llu, %llu)\n"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"
- "failed to enqueue clone group mapping (group_id %llu, private_id %llu, file_id %llu) for deletion: %s\n"
- "fr_val == NULL && fr_val_len == 0"
- "missing clone group record for file_id %llu\n"

```
