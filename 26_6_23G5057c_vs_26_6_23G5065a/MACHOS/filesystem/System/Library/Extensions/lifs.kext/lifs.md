## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

   __TEXT.__os_log: 0x1385
   __TEXT.__cstring: 0x21a0
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1acbc
+  __TEXT_EXEC.__text: 0x1ace0
   __TEXT_EXEC.__auth_stubs: 0xf60
   __DATA.__data: 0x528
   __DATA.__common: 0x130
Symbols:
+ add_sillyrename_entry.kalloc_type_view_1967
+ add_sillyrename_entry.kalloc_type_view_1990
+ cleanup_sillyrename_entries.kalloc_type_view_2080
+ move_sillyrename_entries.kalloc_type_view_2054
- add_sillyrename_entry.kalloc_type_view_1955
- add_sillyrename_entry.kalloc_type_view_1978
- cleanup_sillyrename_entries.kalloc_type_view_2068
- move_sillyrename_entries.kalloc_type_view_2042
Functions:
~ _lifs_getfsattr_call : 360 -> 384
~ _lifs_mntfromname : 484 -> 496
```
