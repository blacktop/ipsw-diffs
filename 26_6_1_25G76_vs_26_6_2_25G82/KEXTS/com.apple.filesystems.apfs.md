## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

 2811.160.7.0.4
   __TEXT.__const: 0xa28
-  __TEXT.__cstring: 0x556f9
-  __TEXT_EXEC.__text: 0x166330
+  __TEXT.__cstring: 0x557d5
+  __TEXT_EXEC.__text: 0x166404
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA.__bss: 0xb60

   __DATA_CONST.__assert: 0x294
   Functions: 2505
   Symbols:   4571
-  CStrings:  7325
+  CStrings:  7328
 
Functions:
~ _sanity_check_alloced_blocks : 1432 -> 1424
~ _encryption_rolling_mount_check : 3456 -> 3676
CStrings:
+ "%s:%d: extent exceeds checksums buf, idx 0x%llx, len 0x%llx, left 0x%llx\n"
+ "%s:%d: extent exceeds rolled buf, idx 0x%llx, extent_size 0x%llx, buf_size 0x%lx\n"
+ "%s:%d: extent exceeds unrolled buf, idx 0x%llx, len 0x%llx, left 0x%llx\n"
+ "2026/08/06"
- "2026/07/11"
```
