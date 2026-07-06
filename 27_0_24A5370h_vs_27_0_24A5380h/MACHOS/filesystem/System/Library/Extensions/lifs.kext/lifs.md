## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

   __TEXT.__os_log: 0x1eba
   __TEXT.__cstring: 0x29e6
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20214
+  __TEXT_EXEC.__text: 0x20244
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
Functions:
~ _lifs_vnop_readdir : 1740 -> 1764
~ _lifs_vnop_getattrlistbulk : 1292 -> 1300
~ _lifs_cache_dirattr : 788 -> 792
~ _lifs_readdir_cached : 740 -> 752

```
