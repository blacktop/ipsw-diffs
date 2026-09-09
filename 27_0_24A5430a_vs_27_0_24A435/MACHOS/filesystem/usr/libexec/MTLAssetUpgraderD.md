## MTLAssetUpgraderD

> `/usr/libexec/MTLAssetUpgraderD`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 382.5.3.0.0
-  __TEXT.__text: 0x18600
+  __TEXT.__text: 0x18618
   __TEXT.__auth_stubs: 0x8c0
   __TEXT.__objc_stubs: 0x840
   __TEXT.__gcc_except_tab: 0xfe8
Functions:
~ _OUTLINED_FUNCTION_7 : 12 -> 20
~ _OUTLINED_FUNCTION_8 : 20 -> 12
~ _mdb_txn_renew0 : 1012 -> 1016
~ _mdb_txn_end : 584 -> 588
~ _mdb_cursor_init : 176 -> 180
~ _mdb_freelist_save : 1416 -> 1420
~ _mdb_page_flush : 940 -> 944
~ _mdb_env_open : 760 -> 764
```
