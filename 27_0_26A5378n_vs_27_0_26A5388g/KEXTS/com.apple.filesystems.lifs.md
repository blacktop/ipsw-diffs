## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-974.0.7.0.0
-  __TEXT.__os_log: 0x1e9c
-  __TEXT.__cstring: 0x29c4
+974.0.11.0.0
+  __TEXT.__os_log: 0x1ef8
+  __TEXT.__cstring: 0x29d8
   __TEXT.__const: 0x328
-  __TEXT_EXEC.__text: 0x1ffd4
+  __TEXT_EXEC.__text: 0x20114
   __TEXT_EXEC.__auth_stubs: 0xfa0
   __DATA.__data: 0x528
   __DATA.__common: 0x130

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 459
-  Symbols:   1341
-  CStrings:  512
+  Symbols:   1342
+  CStrings:  514
 
Symbols:
+ add_sillyrename_entry.kalloc_type_view_2093
+ add_sillyrename_entry.kalloc_type_view_2116
+ cleanup_sillyrename_entries.kalloc_type_view_2214
+ lifs_readdir_cached._os_log_fmt
+ lifs_reclaim_done.kalloc_type_view_4955
+ lifs_vnop_reclaim.kalloc_type_view_4999
+ lifs_vnop_reclaim.kalloc_type_view_5053
+ move_sillyrename_entries.kalloc_type_view_2188
- add_sillyrename_entry.kalloc_type_view_2020
- add_sillyrename_entry.kalloc_type_view_2043
- cleanup_sillyrename_entries.kalloc_type_view_2141
- lifs_reclaim_done.kalloc_type_view_4924
- lifs_vnop_reclaim.kalloc_type_view_4968
- lifs_vnop_reclaim.kalloc_type_view_5022
- move_sillyrename_entries.kalloc_type_view_2115
Functions:
~ _lifs_vnop_getattrlistbulk : 1304 -> 1384
~ _lifs_getfsattr_call : 360 -> 384
~ _lifs_cache_dirattr : 792 -> 848
~ _lifs_readdir_cached : 752 -> 912
CStrings:
+ "%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found"
+ "lifs_readdir_cached"
```
