## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2332.140.12.0.0
+2332.140.13.0.0
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49f16
-  __TEXT_EXEC.__text: 0x140320
+  __TEXT.__cstring: 0x49f96
+  __TEXT_EXEC.__text: 0x140810
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x698
   __DATA.__bss: 0xca8
-  __DATA_CONST.__auth_got: 0x1120
+  __DATA_CONST.__auth_got: 0x1128
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x4e00
   __DATA_CONST.__kalloc_var: 0x2b20
   __DATA_CONST.__assert: 0x14
-  UUID: 5F334502-32EB-38F5-BDD9-CB8962BE2AF6
-  Functions: 2268
+  UUID: A720F92E-41A6-3387-9AD7-1B2BFEF85D5C
+  Functions: 2269
   Symbols:   0
-  CStrings:  6427
+  CStrings:  6430
 
Functions:
~ _prepare_write_and_lock : 7032 -> 7156
~ _ino_shrink : 4184 -> 4316
~ _apfs_truncate_locked : 3528 -> 4200
+ sub_fffffff00a9d1754
CStrings:
+ "%s:%d: %s cannot zero out prealloc'ed region [%lld, %lld) of ino %llu; old_eof=%lld, error=%d\n"
+ "2025/07/15"
+ "21:18:59"
+ "21:19:00"
+ "2332.140.13"
+ "Jul 15 2025"
+ "apfs-2332.140.13"
+ "block_is_unwritten"
+ "need_zerofill"
- "02:02:21"
- "02:02:22"
- "2025/07/03"
- "2332.140.12"
- "Jul  3 2025"
- "apfs-2332.140.12"

```
