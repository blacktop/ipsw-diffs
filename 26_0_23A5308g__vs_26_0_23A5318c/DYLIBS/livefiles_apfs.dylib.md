## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2632.0.77.0.1
-  __TEXT.__text: 0xbe970
+2632.2.1.0.0
+  __TEXT.__text: 0xbf730
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x85c0
-  __TEXT.__oslogstring: 0x15afa
-  __TEXT.__cstring: 0x54c5
-  __TEXT.__unwind_info: 0xfe0
+  __TEXT.__oslogstring: 0x15d81
+  __TEXT.__cstring: 0x5544
+  __TEXT.__unwind_info: 0xfe8
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8
   __AUTH_CONST.__auth_got: 0x478

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: F91E9278-8D9F-3A39-AD98-44AFA6CB9182
-  Functions: 2433
-  Symbols:   5476
-  CStrings:  2190
+  UUID: 929322CE-54CB-342C-9282-2CEBB32E861E
+  Functions: 2446
+  Symbols:   5504
+  CStrings:  2205
 
Symbols:
+ _apfs_clonegroup_check_solo_group
+ _apfs_clonegroup_check_solo_group.cold.1
+ _apfs_clonegroup_check_solo_group.cold.2
+ _apfs_clonegroup_delete_inode.cold.1
+ _apfs_clonegroup_delete_inode.cold.2
+ _apfs_clonegroup_delete_inode.cold.3
+ _apfs_clonegroup_delete_inode.cold.4
+ _apfs_clonegroup_find_and_demote_last_full_clone.cold.3
+ _apfs_clonegroup_validate_record_size
+ _apfs_clonegroup_validate_record_size.cold.1
+ _update_ino_purgeable_dstream_id
+ _update_ino_purgeable_dstream_id.cold.1
CStrings:
+ "%s:%d: %s Bad blob in (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Checking for solo group returned error: %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:0 priv_id:0): %s\n"
+ "%s:%d: %s Error inserting cookie (group:%llu): %s\n"
+ "%s:%d: %s Found corrupt record: %s\n"
+ "%s:%d: %s bad clonegroup_cookie_key_t, klen:%u vlen:%u group_id:%llu\n"
+ "%s:%d: %s bad clonegroup_key_t, size:%u\n"
+ "%s:%d: %s bad clonegroup_mapping_key_t, klen:%u vlen:%u group_id:%llu\n"
+ "%s:%d: %s can't find purgeable record for ino %llu: %d\n"
+ "%s:%d: %s can't update purgeable record of ino %llu with new dstream_id %llu, (old %llu): %d\n"
+ "%s:%d: %s couldn't insert cookie err:%s\n"
+ "2632.2.1"
+ "apfs_clonegroup_check_solo_group"
+ "apfs_clonegroup_insert_cookie"
+ "apfs_clonegroup_validate_record_size"
+ "update_ino_purgeable_dstream_id"
- "%s:%d: %s Bad val size: %u (group:%llu inum:%llu priv_id:%llu)\n"
- "2632.0.77.0.1"

```
