## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-3288.40.17.0.0
+3288.42.1.0.0
   __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x501aa
-  __TEXT_EXEC.__text: 0x1514d4
+  __TEXT.__cstring: 0x50305
+  __TEXT_EXEC.__text: 0x151844
   __TEXT_EXEC.__auth_stubs: 0x2360
   __DATA.__data: 0x75c
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__auth_got: 0x11b0
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2397
+  Functions: 2399
   Symbols:   0
-  CStrings:  6961
+  CStrings:  6966
 
CStrings:
+ "%s:%d: %s apfs_rr: cleanup 0 failed to decrement head split crypto refcount (ret %d) \n"
+ "%s:%d: %s apfs_rr: cleanup first failed to decrement crypto refcount (ret %d) \n"
+ "%s:%d: %s apfs_rr: cleanup last failed to decrement crypto refcount (ret %d) \n"
+ "%s:%d: %s applied dstream workaround inode %llu\n"
+ "%s:%d: %s ino %llu '%s' cp_open() failed with EILSEQ\n"
+ "2026/10/10"
+ "3288.42.1"
+ "apfs-3288.42.1"
- "2026/09/27"
- "3288.40.17"
- "apfs-3288.40.17"
```
