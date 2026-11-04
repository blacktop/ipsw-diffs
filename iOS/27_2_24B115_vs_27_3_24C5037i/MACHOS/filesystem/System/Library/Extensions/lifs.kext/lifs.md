## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

-974.40.12.0.0
+974.60.5.0.0
   __TEXT.__os_log: 0x1ffc
   __TEXT.__cstring: 0x2a13
   __TEXT.__const: 0x348
-  __TEXT_EXEC.__text: 0x20a04
+  __TEXT_EXEC.__text: 0x20ae0
   __TEXT_EXEC.__auth_stubs: 0xfb0
   __DATA.__data: 0x578
   __DATA.__common: 0x138

   __DATA_CONST.__auth_got: 0x7d8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 463
-  Symbols:   1232
+  Functions: 464
+  Symbols:   1233
   CStrings:  524
 
Symbols:
+ _add_sillyrename_entry.kalloc_type_view_2144
+ _add_sillyrename_entry.kalloc_type_view_2167
+ _cleanup_sillyrename_entries.kalloc_type_view_2265
+ _lifs_mark_setattr_supported
+ _lifs_mirror_mount_domount.kalloc_type_view_1331
+ _move_sillyrename_entries.kalloc_type_view_2239
- _add_sillyrename_entry.kalloc_type_view_2093
- _add_sillyrename_entry.kalloc_type_view_2116
- _cleanup_sillyrename_entries.kalloc_type_view_2214
- _lifs_mirror_mount_domount.kalloc_type_view_1229
- _move_sillyrename_entries.kalloc_type_view_2188
Functions:
~ _lifs_vnop_setattr : 1388 -> 1384
+ _lifs_mark_setattr_supported
```
