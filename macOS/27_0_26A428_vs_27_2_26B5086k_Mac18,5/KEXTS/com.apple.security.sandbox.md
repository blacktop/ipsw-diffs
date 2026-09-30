## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-3051.0.52.0.0
-  __TEXT.__os_log: 0x2634
-  __TEXT.__const: 0x206e7
-  __TEXT.__cstring: 0x7dd5
-  __TEXT_EXEC.__text: 0x521b8
-  __TEXT_EXEC.__auth_stubs: 0x1540
-  __DATA.__data: 0x410
-  __DATA_CONST.__const: 0x3fa0
-  __DATA_CONST.__kalloc_type: 0x1700
+3051.40.70.0.0
+  __TEXT.__os_log: 0x278d
+  __TEXT.__const: 0x20a17
+  __TEXT.__cstring: 0x7dc7
+  __TEXT_EXEC.__text: 0x5281c
+  __TEXT_EXEC.__auth_stubs: 0x15d0
+  __DATA.__data: 0x3b0
+  __DATA_CONST.__const: 0x4080
+  __DATA_CONST.__kalloc_type: 0x1840
   __DATA_CONST.__kalloc_var: 0x550
-  __DATA_CONST.__auth_got: 0xaa0
+  __DATA_CONST.__auth_got: 0xae8
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 967
-  Symbols:   1938
-  CStrings:  1612
+  Functions: 977
+  Symbols:   1974
+  CStrings:  1625
 
Symbols:
+ ____bastion_profile_create_block_invoke
+ ___appbundle_register_block_invoke
+ ___appbundle_register_path_block_invoke
+ ___appbundle_unregister_block_invoke
+ ___appbundle_unregister_path_block_invoke
+ ___appcontainer_register_block_invoke
+ ___appcontainer_register_path_block_invoke
+ ___appcontainer_unregister_block_invoke
+ ___appcontainer_unregister_path_block_invoke
+ ___disk_image_backing_store_register_path_block_invoke
+ ___disk_image_backing_store_unregister_block_invoke
+ ___disk_image_backing_store_unregister_path_block_invoke
+ ___syncroot_register_path_block_invoke
+ ___syscall_sandcastle_appcontainer_check_block_invoke_2
+ _appbundle_registration_mtx
+ _appcontainer_registration_mtx
+ _appcontainer_unregister_path
+ _bastion_profile_create_from_data
+ _bastion_profile_free_callback
+ _bastion_profile_smr_domain
+ _bastion_profile_write_lock
+ _builtin_profile_uninit
+ _disk_image_registration_mtx
+ _handle_unexpected_container_vnode_type
+ _hook_vnode_notify_begin_rename_swap
+ _hook_vnode_notify_end_rename_swap
+ _os_pcpu_ref_destroy
+ _os_pcpu_ref_init
+ _os_pcpu_ref_kill
+ _os_pcpu_ref_release
+ _os_pcpu_ref_retain_try
+ _profile_dealloc.kalloc_type_view_170
+ _profile_retain_persistent_and_release_transient
+ _registered_profile_uninit
+ _sandcastle_pattern_buffer_free_callback
+ _sandcastle_pattern_buffer_release
+ _sandcastle_pattern_buffer_retain
+ _sandcastle_pattern_smr_domain
+ _smr_call
+ _smr_domain_create
+ _smr_enter
+ _smr_leave
+ _syncroot_registration_mtx
+ appbundle_register_path._os_log_fmt
+ appbundle_unregister_path._os_log_fmt
+ appcontainer_register_path._os_log_fmt
+ appcontainer_unregister_path._os_log_fmt
+ bastion_init.kalloc_type_view_417
+ bastion_profile_create_from_data._os_log_fmt
+ bastion_profile_create_from_data.kalloc_type_view_209
+ bastion_profile_create_from_data.kalloc_type_view_220
+ bastion_profile_free_callback.kalloc_type_view_66
+ derive_socket_info.kalloc_type_view_1484
+ disk_image_backing_store_register_path._os_log_fmt
+ disk_image_backing_store_unregister_path._os_log_fmt
+ extension_create.kalloc_type_view_1529
+ extension_release.kalloc_type_view_1757
+ extension_set_create_class_locked.kalloc_type_view_969
+ extension_set_create_class_locked.kalloc_type_view_973
+ extension_set_create_storage_class_locked.kalloc_type_view_1001
+ extension_set_new.kalloc_type_view_705
+ extension_set_release.kalloc_type_view_809
+ extension_set_release.kalloc_type_view_827
+ extension_set_release.kalloc_type_view_833
+ handle_unexpected_container_vnode_type._os_log_fmt
+ match_sandcastle_unregistered_appbundle.kalloc_type_view_743
+ match_sandcastle_unregistered_appbundle.kalloc_type_view_751
+ mount_info_alloc.kalloc_type_view_1684
+ mount_info_release.kalloc_type_view_1719
+ pending_approval_entry_create.kalloc_type_view_1677
+ pending_approval_entry_create.kalloc_type_view_1684
+ pending_approval_entry_release.kalloc_type_view_1656
+ pending_swap_begin.kalloc_type_view_2145
+ pending_swap_release.kalloc_type_view_2100
+ pending_update_append.kalloc_type_view_291
+ pending_update_append_pair.kalloc_type_view_319
+ pending_update_append_pair.kalloc_type_view_321
+ pending_update_append_pair.kalloc_type_view_322
+ profile_construct.kalloc_type_view_357
+ profile_construct.kalloc_type_view_365
+ profile_uninit.kalloc_type_view_149
+ profile_uninit.kalloc_type_view_155
+ sandcastle_init.kalloc_type_view_3427
+ sandcastle_pattern_buffer_free_callback.kalloc_type_view_318
+ sandcastle_pattern_buffer_new.kalloc_type_view_301
+ sandcastle_pattern_load_from_disk._os_log_fmt
+ storage_class_for_vnode.kalloc_type_view_3608
+ syncroot_register_path._os_log_fmt
+ syscall_sandcastle_pattern_set._os_log_fmt
- ___disk_image_backing_store_register_block_invoke_2
- ___sandbox_unregister_disk_image_backing_store_by_vnode_block_invoke
- ___sandbox_unregister_disk_image_backing_store_by_vnode_block_invoke_2
- ___syncroot_register_block_invoke_2
- ___syscall_sandcastle_appbundle_register_block_invoke
- ___syscall_sandcastle_appbundle_unregister_block_invoke
- ___syscall_sandcastle_appcontainer_register_block_invoke
- ___syscall_sandcastle_appcontainer_unregister_block_invoke
- __get_bastion_profile
- __set_bastion_profile
- _bastion_profile_lock
- _builtin_destroy
- _disk_image_backing_store_register
- _do_bastion_profile_register._os_log_fmt
- _hook_vnode_check_readlink
- _hook_vnode_notify_will_rename_swap
- _pending_swap_done
- _profile_dealloc.kalloc_type_view_174
- _registered_profile_destroy
- bastion_init.kalloc_type_view_260
- derive_socket_info.kalloc_type_view_1481
- disk_image_backing_store_index_block_invoke_2._os_log_fmt
- extension_create.kalloc_type_view_1515
- extension_release.kalloc_type_view_1743
- extension_set_create_class_locked.kalloc_type_view_955
- extension_set_create_class_locked.kalloc_type_view_959
- extension_set_create_storage_class_locked.kalloc_type_view_987
- extension_set_new.kalloc_type_view_691
- extension_set_release.kalloc_type_view_795
- extension_set_release.kalloc_type_view_813
- extension_set_release.kalloc_type_view_819
- match_sandcastle_unregistered_appbundle.kalloc_type_view_744
- match_sandcastle_unregistered_appbundle.kalloc_type_view_752
- mount_info_alloc.kalloc_type_view_1673
- mount_info_release.kalloc_type_view_1708
- pending_approval_entry_create.kalloc_type_view_1454
- pending_approval_entry_create.kalloc_type_view_1461
- pending_approval_entry_release.kalloc_type_view_1433
- pending_swap_begin.kalloc_type_view_2148
- pending_swap_release.kalloc_type_view_2103
- pending_update_append.kalloc_type_view_257
- pending_update_append_pair.kalloc_type_view_285
- pending_update_append_pair.kalloc_type_view_287
- pending_update_append_pair.kalloc_type_view_288
- profile_construct.kalloc_type_view_361
- profile_construct.kalloc_type_view_369
- profile_uninit.kalloc_type_view_153
- profile_uninit.kalloc_type_view_159
- sandcastle_init.kalloc_type_view_3201
- storage_class_for_vnode.kalloc_type_view_3586
- syncroot_discover_count_block_invoke._os_log_fmt
- syscall_sandcastle_appbundle_register._os_log_fmt
- syscall_sandcastle_appbundle_unregister._os_log_fmt
CStrings:
+ "\"failed to allocate memory for globals\" @%s:%d"
+ "118"
+ "21218"
+ "bastion_profile_smr_domain"
+ "failed to load %s: %d"
+ "failed to register app bundle for %s: %d"
+ "failed to register app container for %s: %d"
+ "failed to register disk image backing store for %s: %d"
+ "failed to register sync root for %s: %d"
+ "failed to set pattern #%llu: %d"
+ "failed to unregister app bundle for %s: %d"
+ "failed to unregister app container for %s"
+ "failed to unregister disk image backing store for %s: %d"
+ "failed to unregister sync root for %s: %d"
+ "path %s should not be in app container index, removing"
+ "registered app bundle for %s"
+ "registered app container for %s"
+ "sandcastle_pattern_smr_domain"
+ "site.typeof(**(&bp))"
+ "site.typeof(**(&pattern))"
+ "site.typeof(*bp)"
+ "site.typeof(*pattern)"
+ "unregistered app bundle for %s"
+ "unregistered app container for %s"
- "\"Invoked %s before initialization of bastion_globals\" @%s:%d"
- "\"expected NULL for `bastion_pointers`\" @%s:%d"
- "\"failed to initialize authenticated pointers for bastion\" @%s:%d"
- "_get_bastion_profile"
- "_set_bastion_profile"
- "failed to register disk image backing store for %s"
- "failed to register sync root for %s"
- "failed to unregister disk image backing store for %s"
- "failed to unregister sync root for %s"
- "registered app bundle for %{public}s"
- "unregistered app bundle for %{public}s"
```
