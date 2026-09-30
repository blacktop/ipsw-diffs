## com.apple.BootCache

> `com.apple.BootCache`

```diff

 162.0.0.0.0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x17a6
-  __TEXT_EXEC.__text: 0xae3c
+  __TEXT_EXEC.__text: 0xaf10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__kalloc_type: 0xcc0
   __DATA_CONST.__kalloc_var: 0x6e0
-  UUID: AD05C83B-0708-3FE0-9E20-1ADE67DBEB46
+  UUID: 37B13EC0-1714-3510-9B23-4A8C52D2030C
   Functions: 71
   Symbols:   603
   CStrings:  158
Functions:
~ _BC_sysctl : 6636 -> 6756
~ _BC_root_mount_hook : 644 -> 632
~ _BC_load : 252 -> 268
~ _BC_terminate_history : 480 -> 468
~ _BC_terminate_cache : 2020 -> 1952
~ _BC_update_mounts : 128 -> 140
~ _BC_copyout_history_mounts : 80 -> 84
~ _BC_copyout_history_entries : 148 -> 152
~ _BC_reset_cache : 244 -> 256
~ _BC_add_history : 1752 -> 1812
~ _BC_check_handlers : 176 -> 168
~ _BC_cache_contains_block : 244 -> 260
~ _BC_mount_available : 568 -> 580
~ _BC_strategy : 8264 -> 8112
~ _BC_close : 1084 -> 1012
~ _BC_find_cache_mount : 156 -> 152
~ _BC_find_extent : 492 -> 540
~ _extents_status : 112 -> 116
~ _BC_blocks_present : 104 -> 124
~ _BC_discard_bytes : 516 -> 564
~ _BC_handle_discards : 908 -> 988
~ _BC_terminate_cache_async : 108 -> 120
~ _uuid_string : 92 -> 112
~ _BC_setup_mount : 336 -> 344
~ _BC_setup_extent : 172 -> 176
~ _BC_alloc_pagebuffer : 168 -> 152
~ _BC_fill_in_extent : 444 -> 500
~ _fill_in_bc_cache_mounts : 2212 -> 2240
~ _BC_free_pagebuffer : 108 -> 104
~ _BC_teardown_mount_and_extents : 228 -> 252
~ _BC_fill_in_cache_mount : 656 -> 724
~ _BC_fill_in_cache_mount_ex : 1568 -> 1652
~ _BC_reader_thread : 3880 -> 3596
~ _check_for_new_mount_itr : 1792 -> 1688
~ _BC_get_history_mount_device : 304 -> 312
~ _bc_get_volume_info : 2184 -> 2244
~ _bc_get_group_uuid_for_dev : 1536 -> 1596
~ _lookup_dev_name : 828 -> 888

```
