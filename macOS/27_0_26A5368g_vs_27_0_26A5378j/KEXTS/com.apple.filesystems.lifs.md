## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

   __TEXT.__os_log: 0x1e9c
   __TEXT.__cstring: 0x29c4
   __TEXT.__const: 0x328
-  __TEXT_EXEC.__text: 0x1ffa4
+  __TEXT_EXEC.__text: 0x1ffd4
   __TEXT_EXEC.__auth_stubs: 0xfa0
   __DATA.__data: 0x528
   __DATA.__common: 0x130
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ _lifs_vnop_readdir : 1740 -> 1764
~ _lifs_vnop_getattrlistbulk : 1296 -> 1304
~ _lifs_cache_dirattr : 788 -> 792
~ _lifs_readdir_cached : 740 -> 752

```
