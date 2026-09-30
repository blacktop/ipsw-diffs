## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2632.0.36.0.1
+2632.0.54.0.2
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c0a1
-  __TEXT_EXEC.__text: 0x1575ac
+  __TEXT.__cstring: 0x4c12f
+  __TEXT_EXEC.__text: 0x157b0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640
   __DATA.__bss: 0xca8

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x6718
-  __DATA_CONST.__kalloc_type: 0x4e80
+  __DATA_CONST.__const: 0x6730
+  __DATA_CONST.__kalloc_type: 0x4ec0
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 6DF5D1D5-3D11-3B11-8CC7-8E8EA183BF4F
-  Functions: 2308
+  UUID: EF785261-4DA9-3451-8CE8-118E49565A0A
+  Functions: 2312
   Symbols:   0
-  CStrings:  6558
+  CStrings:  6566
 
CStrings:
+ "%s:%d: %s failed to authorize rmdir for ino %llu (parent %llu): %d (%s)\n"
+ "%s:%d: %s failed to authorize unlink for ino %llu (parent %llu): %d (%s)\n"
+ "%s:%d: %s failed to get parent %llu for authorization of ino %llu\n"
+ "%s:%d: %s ino %llu has no name"
+ "%s:%d: %s purging not permitted for ino %llu (parent %llu): requesting user is not the owner\n"
+ "%s:%d: destroyed key for uuid %s and type %u, as it exceeded the TTL of %u seconds\n"
+ "(*ino)->vp"
+ "*ino"
+ "122212"
+ "2025/06/30"
+ "21:43:27"
+ "21:43:28"
+ "2632.0.54.0.2"
+ "Jun 30 2025"
+ "apfs-2632.0.54.0.2"
+ "com.apple.private.apfs.key-cache-eviction"
+ "consider_drec_for_size_tracking"
+ "methodKeyCacheEvict"
+ "parent->vp"
- "%s:%d: %s authorize_purge failed for ino (%llu) as vn_authorize_rmdir returned an error (%d)\n"
- "%s:%d: %s authorize_purge failed for ino (%llu) as vn_authorize_unlink returned an error (%d)\n"
- "%s:%d: %s purging failed for open-unlinked ino (%llu) with ENOENT\n"
- "%s:%d: %s purging not permitted for ino (%llu) as parent vp is null\n"
- "%s:%d: %s purging not permitted for ino (%llu) as the requesting uid is not the owner\n"
- "12221"
- "2025/06/16"
- "23:39:37"
- "2632.0.36.0.1"
- "Jun 16 2025"
- "apfs-2632.0.36.0.1"

```
