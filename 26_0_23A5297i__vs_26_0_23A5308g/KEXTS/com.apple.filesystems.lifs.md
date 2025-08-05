## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-737.0.17.0.2
+737.0.29.0.2
   __TEXT.__os_log: 0x13b7
-  __TEXT.__cstring: 0x2203
+  __TEXT.__cstring: 0x2220
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1b9dc
+  __TEXT_EXEC.__text: 0x1b9e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 2590497A-F411-38F2-879A-E774D5569213
+  UUID: CBF03198-0DAD-30AC-9D58-2612E7928A3B
   Functions: 406
   Symbols:   0
   CStrings:  402
Functions:
~ _lifs_fsync_internal : 1608 -> 1620
CStrings:
+ "%s: client %p pid: %d pidversion: %d supportBlockResource: %d\n"
+ "ALUC:clientDied(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_block_resource %d\n"
+ "ALUC:init(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_block_resource %d\n"
- "%s: client %p pid: %d pidversion: %d supportKOIO: %d\n"
- "ALUC:clientDied(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_koio %d\n"
- "ALUC:init(pid: %d pidversion: %d), fskitd_entitled %d fsmodule_entitled %d support_koio %d\n"

```
