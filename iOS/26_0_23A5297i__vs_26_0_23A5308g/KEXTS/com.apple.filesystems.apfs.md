## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2632.0.68.0.3
+2632.0.77.0.1
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c360
-  __TEXT_EXEC.__text: 0x158750
+  __TEXT.__cstring: 0x4c1fa
+  __TEXT_EXEC.__text: 0x15897c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640
   __DATA.__bss: 0xca8
-  __DATA_CONST.__auth_got: 0x1160
+  __DATA_CONST.__auth_got: 0x1158
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 24EA4EBC-A831-3D42-A663-614067DD56B2
-  Functions: 2316
+  UUID: 299BA795-7094-378C-B0E0-2679E28C9E8E
+  Functions: 2317
   Symbols:   0
-  CStrings:  6576
+  CStrings:  6571
 
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "%s:%d: %s failed to set parent chain noflush for graft dir, %d\n"
+ "%s:%d: %s failed to set parent chain noflush for graft file, %d\n"
+ "112122211111112222222222122222222111112222222111112222211122222222222222222222222222222222212221222122212222122212221222122111222122211121222222"
+ "18:33:35"
+ "2025/07/27"
+ "2632.0.77.0.1"
+ "Jul 27 2025"
+ "apfs-2632.0.77.0.1"
+ "update_purgeable_clone_tracking"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s attempting to reclaim a graft file vnode while it is grafted, ino %llu, usecount %d, vnoflush %d, iflags 0x%llx, name [%s]\n"
- "%s:%d: %s failed to set parent chain noflush for graft dir %llu, %d\n"
- "%s:%d: %s failed to set parent chain noflush for graft file %llu, %d\n"
- "%s:%d: %s graft file ino %llu should have VNOFLUSH set\n"
- "%s:%d: %s graft file vnode has no inode\n"
- "%s:%d: %s graft file vnode should have VNOFLUSH set\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "1121222111111122222222221222222221111122222221111122222111222222222222222222222222222222222122212221222122221222122212221221112221222111212222222"
- "2025/07/14"
- "22:55:23"
- "2632.0.68.0.3"
- "Jul 14 2025"
- "apfs-2632.0.68.0.3"
- "update_clone_mapping_if_present"

```
