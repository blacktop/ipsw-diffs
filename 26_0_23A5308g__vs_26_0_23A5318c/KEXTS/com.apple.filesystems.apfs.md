## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2632.0.77.0.1
+2632.2.1.0.0
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c1fa
-  __TEXT_EXEC.__text: 0x15897c
+  __TEXT.__cstring: 0x4c596
+  __TEXT_EXEC.__text: 0x159a78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640
   __DATA.__bss: 0xca8
-  __DATA_CONST.__auth_got: 0x1158
+  __DATA_CONST.__auth_got: 0x1150
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 299BA795-7094-378C-B0E0-2679E28C9E8E
-  Functions: 2317
+  UUID: BDEED075-6587-305A-84F5-07E407179EAA
+  Functions: 2319
   Symbols:   0
-  CStrings:  6571
+  CStrings:  6589
 
CStrings:
+ "%s:%d: %s Bad blob in (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Checking for solo group returned error: %s\n"
+ "%s:%d: %s Couldn't enter transaction: %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Couldn't lookup_ge (group:%llu inum:0 priv_id:0): %s\n"
+ "%s:%d: %s Error checking for solo group (group:%llu): %s\n"
+ "%s:%d: %s Error inserting cookie (group:%llu): %s\n"
+ "%s:%d: %s Error processing solo inode (group:%llu inum:%llu): %s\n"
+ "%s:%d: %s Error removing (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Error updating inode (group:%llu inum:%llu priv_id:%llu): %s\n"
+ "%s:%d: %s Expected group:%llu, found (group:%llu, inum:%llu, priv_id:%llu)\n"
+ "%s:%d: %s Removed %llu cookies and %llu mappings\n"
+ "%s:%d: %s bad clonegroup_cookie_key_t, klen:%u vlen:%u group_id:%llu\n"
+ "%s:%d: %s can't find purgeable record for ino %llu: %d\n"
+ "%s:%d: %s can't update purgeable record of ino %llu with new dstream_id %llu, (old %llu): %d\n"
+ "%s:%d: %s couldn't insert cookie err:%s\n"
+ "%s:%d: %s couldn't remove cookie (group_id:%llu): %s\n"
+ "%s:%d: %s iterator init failed: %s\n"
+ "%s:%d: inflight i/o count underflow (%llu)\n"
+ "%s:%d: reached maximum async inflight i/o requests (%llu) [fsindex (%d)]\n"
+ "2025/08/05"
+ "22:05:34"
+ "2632.2.1"
+ "Aug  5 2025"
+ "apfs-2632.2.1"
+ "apfs_clonegroup_check_solo_group"
+ "apfs_clonegroup_cleanup_cookies"
+ "apfs_clonegroup_insert_cookie"
+ "apfs_clonegroup_process_solo_group"
+ "update_ino_purgeable_dstream_id"
- "%s:%d: %s Bad map value size: %u (group:%llu inum:%llu priv_id:%llu)\n"
- "%s:%d: %s Bad val size: %u (group:%llu inum:%llu priv_id:%llu)\n"
- "%s:%d: inflight i/o count underflow (%u)\n"
- "%s:%d: max attempts (%d) reached waiting for async I/O to finish at offset(%llu)\n"
- "%s:%d: reached maximum async inflight i/o requests (%d) [fsindex (%d)]\n"
- "%s:%d: timer expired waiting for async I/O to finish at offset(%llu)\n"
- "18:33:35"
- "2025/07/27"
- "2632.0.77.0.1"
- "Jul 27 2025"
- "apfs-2632.0.77.0.1"
- "asyncCryptoReadWaitAndFinish"

```
