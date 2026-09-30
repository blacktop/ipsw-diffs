## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-3288.2.1.0.0
+3288.40.13.0.0
   __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x4ff24
-  __TEXT_EXEC.__text: 0x150bc4
+  __TEXT.__cstring: 0x4ff4b
+  __TEXT_EXEC.__text: 0x151068
   __TEXT_EXEC.__auth_stubs: 0x2360
-  __DATA.__data: 0x754
+  __DATA.__data: 0x75c
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x6890

   __DATA_CONST.__auth_got: 0x11b0
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2396
+  Functions: 2395
   Symbols:   0
-  CStrings:  6952
+  CStrings:  6954
 
CStrings:
+ "%s:%d: %s failed to remove extents iteratively\n"
+ "%s:%d: %s ino %llu, failed to get region covering %llu+%zu, error %d\n"
+ "%s:%d: %s request flags: 0x%llx type: 0x%llx min_size: %lld: max_age %lld desired_amt: %lld (age-for-urgency: %lld, requesting uid: %d, search_start_time: %llu)\n"
+ "2026/09/04"
+ "3288.40.13"
+ "apfs-3288.40.13"
+ "btree_node_compact"
+ "decrement_dstream_id_for_deletion"
- "%s:%d: %s request flags: 0x%llx type: 0x%llx min_size: %lld: max_age %lld desired_amt: %lld (age-for-urgency: %lld, requesting uid: %d)\n"
- "%s:%d: container is locked to be loadable only by pid <%d>, refusing request to load the container by pid <%d> device = %s\n"
- "2026/08/13"
- "3288.2.1"
- "apfs-3288.2.1"
- "decrement_dstream_id_for_deletion_ex"
```
