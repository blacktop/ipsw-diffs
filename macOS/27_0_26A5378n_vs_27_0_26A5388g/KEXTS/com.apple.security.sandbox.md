## com.apple.security.sandbox

> `com.apple.security.sandbox`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-3051.0.30.0.0
-  __TEXT.__os_log: 0x255d
-  __TEXT.__const: 0x204d7
-  __TEXT.__cstring: 0x7d64
-  __TEXT_EXEC.__text: 0x541e4
-  __TEXT_EXEC.__auth_stubs: 0x1510
+3051.0.42.0.2
+  __TEXT.__os_log: 0x2583
+  __TEXT.__const: 0x20717
+  __TEXT.__cstring: 0x7c91
+  __TEXT_EXEC.__text: 0x52bc0
+  __TEXT_EXEC.__auth_stubs: 0x1500
   __DATA.__data: 0x410
-  __DATA.__bss: 0x7f190
-  __DATA_CONST.__const: 0x3f68
+  __DATA.__bss: 0x7f18c
+  __DATA_CONST.__const: 0x3f70
   __DATA_CONST.__kalloc_type: 0x1700
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__auth_got: 0xa80
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 969
-  Symbols:   1931
-  CStrings:  1602
+  Functions: 963
+  Symbols:   1925
+  CStrings:  1591
 
Symbols:
+ __ZL15walk_rootdeviceP7IOMedia
+ __ZL34_walk_AppleAPFSContainerFromVolumeP15IORegistryEntry
+ __ZZL23record_protected_deviceiPKcE19kalloc_type_view_98
+ __ZZL30reset_protected_devices_lockedvE20kalloc_type_view_127
+ _derive_vnode_storage_class_is_cacheable
+ _get_static_storage_class_for_vnode.kalloc_type_view_959
+ _get_static_storage_class_for_vnode.kalloc_type_view_968
+ _prepopulate_storage_class
+ _sandcastle_pattern_persist_to_disk
+ _storage_class_cache_invalidate_all_with_callback
+ _storage_class_cache_invalidate_with_callback
+ derive_socket_info.kalloc_type_view_1481
+ extension_create.kalloc_type_view_1515
+ extension_release.kalloc_type_view_1743
+ extension_set_create_class_locked.kalloc_type_view_955
+ extension_set_create_class_locked.kalloc_type_view_959
+ extension_set_create_storage_class_locked.kalloc_type_view_987
+ extension_set_new.kalloc_type_view_691
+ extension_set_release.kalloc_type_view_795
+ extension_set_release.kalloc_type_view_813
+ extension_set_release.kalloc_type_view_819
+ free_filter_context.kalloc_type_view_135
+ mount_info_alloc.kalloc_type_view_1673
+ mount_info_release.kalloc_type_view_1708
+ pending_approval_entry_create.kalloc_type_view_1454
+ pending_approval_entry_create.kalloc_type_view_1461
+ pending_approval_entry_release.kalloc_type_view_1433
+ pending_swap_begin.kalloc_type_view_2148
+ pending_swap_release.kalloc_type_view_2103
+ profile_syscallmask_populate._os_log_fmt
+ sandcastle_init.kalloc_type_view_3201
+ schedule_microstackshot.kalloc_type_view_1749
+ schedule_microstackshot.kalloc_type_view_1777
+ schedule_microstackshot.kalloc_type_view_1800
+ storage_class_for_vnode.kalloc_type_view_3586
+ storage_class_for_vnode.kalloc_type_view_3597
+ thread_ustackshot_destroy.kalloc_type_view_1715
+ thread_ustackshot_destroy.kalloc_type_view_1718
- __Z16OSUnserializeXMLPKcPP8OSString
- __ZL15walk_rootdeviceP7IOMediab
- __ZL17_copy_root_volumev
- __ZL34_walk_AppleAPFSContainerFromVolumeP15IORegistryEntryb
- __ZZL23record_protected_deviceiPKcE20kalloc_type_view_105
- __ZZL30reset_protected_devices_lockedvE20kalloc_type_view_134
- __storage_class_cache_invalidate_all
- __storage_class_cache_invalidate_all_exclusive
- _get_static_storage_class_for_vnode.kalloc_type_view_949
- _get_static_storage_class_for_vnode.kalloc_type_view_958
- _iokit_check_nvram_set
- _retain_vnode_label_macl_ref
- _rootless_allowed_local_configuration
- _rootless_allowed_netboot_configuration
- _storage_class_cache_insert
- _storage_class_cache_invalidate
- _storage_class_cache_invalidate_exclusive
- _storage_class_cache_lookup
- derive_socket_info.kalloc_type_view_1429
- extension_create.kalloc_type_view_1241
- extension_release.kalloc_type_view_1469
- extension_set_create_class_locked.kalloc_type_view_707
- extension_set_create_class_locked.kalloc_type_view_711
- extension_set_create_storage_class_locked.kalloc_type_view_739
- extension_set_new.kalloc_type_view_443
- extension_set_release.kalloc_type_view_547
- extension_set_release.kalloc_type_view_565
- extension_set_release.kalloc_type_view_571
- free_filter_context.kalloc_type_view_118
- mount_info_alloc.kalloc_type_view_1686
- mount_info_release.kalloc_type_view_1721
- pending_approval_entry_create.kalloc_type_view_1448
- pending_approval_entry_create.kalloc_type_view_1455
- pending_approval_entry_release.kalloc_type_view_1427
- pending_swap_begin.kalloc_type_view_2118
- pending_swap_release.kalloc_type_view_2073
- sandcastle_init.kalloc_type_view_3182
- schedule_microstackshot.kalloc_type_view_1745
- schedule_microstackshot.kalloc_type_view_1773
- schedule_microstackshot.kalloc_type_view_1796
- storage_class_for_vnode.kalloc_type_view_3599
- storage_class_for_vnode.kalloc_type_view_3610
- thread_ustackshot_destroy.kalloc_type_view_1711
- thread_ustackshot_destroy.kalloc_type_view_1714
CStrings:
+ "mask size (%zu) exceeds maximum (%zu)"
+ "perl"
+ "python"
- "\"mask size (%zu) exceeds maximum (%zu)\" @%s:%d"
- "/options"
- "IOAPFSPreBootDevice"
- "IOEFIBootOption"
- "IOEFIDevicePathType"
- "IOMatch"
- "IOPropertyMatch"
- "IOProviderClass"
- "MediaFilePath"
- "Path"
- "RemoteIpAddress"
- "csr-data"
- "netboot-sources"
- "pythonperl"
```
