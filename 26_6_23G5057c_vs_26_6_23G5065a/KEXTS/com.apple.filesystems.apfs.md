## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`

```diff

   __TEXT.__const: 0x9a8
-  __TEXT.__cstring: 0x4d93c
-  __TEXT_EXEC.__text: 0x148bdc
+  __TEXT.__cstring: 0x4da0d
+  __TEXT_EXEC.__text: 0x148e38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA.__bss: 0xd48

   __DATA_CONST.__assert: 0x14
   Functions: 2341
   Symbols:   0
-  CStrings:  6717
+  CStrings:  6720
 
Functions:
~ _fetch_particular_snap_extent : 608 -> 620
~ _graft_blockmap_lut_tree_insert : 848 -> 868
~ _nx_checkpoint_traverse : 3660 -> 4224
~ sub_fffffe000a5c9f94 -> sub_fffffe000a52faa8 : 484 -> 488
~ sub_fffffe000a602714 -> sub_fffffe000a56822c : 624 -> 628
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "2026/07/09"
+ "23:19:03"
+ "2811.160.7.0.4"
+ "Jul  9 2026"
+ "apfs-2811.160.7.0.4"
- "2026/06/28"
- "20:04:07"
- "2811.160.7"
- "Jun 28 2026"
- "apfs-2811.160.7"
```
