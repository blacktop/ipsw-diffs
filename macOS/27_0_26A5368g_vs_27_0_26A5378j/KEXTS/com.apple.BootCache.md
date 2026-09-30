## com.apple.BootCache

> `com.apple.BootCache`

```diff

   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x17a6
-  __TEXT_EXEC.__text: 0xb484
+  __TEXT_EXEC.__text: 0xb490
   __TEXT_EXEC.__auth_stubs: 0x880
   __DATA.__data: 0x118
   __DATA.__common: 0x38
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ _BC_sysctl : 7480 -> 7436
~ _BC_close : 1192 -> 1148
~ _BC_handle_discards : 968 -> 924
~ _fill_in_bc_cache_mounts : 2280 -> 2388
~ _check_for_new_mount_itr : 1720 -> 1756

```
