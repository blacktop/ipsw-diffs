## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-974.0.7.0.0
-  __TEXT.__os_log: 0x1eba
-  __TEXT.__cstring: 0x29e6
+974.0.11.0.0
+  __TEXT.__os_log: 0x1f16
+  __TEXT.__cstring: 0x29fa
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x20244
+  __TEXT_EXEC.__text: 0x20390
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 460
-  Symbols:   1243
-  CStrings:  517
+  Symbols:   1244
+  CStrings:  519
 
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
~ _lifs_vnop_getattrlistbulk : 1300 -> 1380
~ _lifs_getfsattr_call : 360 -> 384
~ _lifs_mntfromname : 484 -> 496
~ _lifs_cache_dirattr : 792 -> 848
~ _lifs_readdir_cached : 752 -> 912
CStrings:
+ "%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found"
+ "lifs_readdir_cached"
```
