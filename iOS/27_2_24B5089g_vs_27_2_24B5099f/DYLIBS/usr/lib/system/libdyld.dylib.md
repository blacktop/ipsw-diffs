## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-27102.0.0.0.0
-  __TEXT.__text: 0x1c47c
+27104.0.0.0.0
+  __TEXT.__text: 0x1cff8
   __TEXT.__const: 0x32c
-  __TEXT.__cstring: 0x4d20
+  __TEXT.__cstring: 0x4dd6
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__unwind_info: 0xda0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__const: 0x17e8
   __AUTH_CONST.__auth_got: 0x1a0
-  __DATA.__data: 0x10
   __DATA.__crash_info: 0x148
+  __DATA.__data: 0x8
   __DATA.__common: 0x11
   __DATA_DIRTY.__common: 0x28
   __TPRO_CONST.__dyld_apis: 0x8

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 853
+  Functions: 854
   Symbols:   1079
-  CStrings:  548
+  CStrings:  552
 
Symbols:
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
- __ZZ16get_xprr_versionvE19cached_xprr_version
Functions:
~ __dyld_objc_class_count : 140 -> 164
~ _dyld_program_sdk_at_least : 144 -> 168
~ _dyld_get_active_platform : 140 -> 164
~ _dyld_image_header_containing_address : 144 -> 168
~ __dyld_for_each_objc_class : 148 -> 172
~ __dyld_get_objc_selector : 144 -> 168
~ __dyld_is_memory_immutable : 148 -> 172
~ __dyld_find_protocol_conformance_on_disk : 156 -> 180
~ __dyld_stack_range : 148 -> 172
~ __dyld_find_unwind_sections : 148 -> 172
~ __dyld_find_protocol_conformance : 152 -> 176
~ __dyld_call_with_writable_tpro_memory : 148 -> 172
~ __dyld_shared_cache_real_path : 144 -> 168
~ _dyld_sdk_at_least : 148 -> 172
~ _dyld_get_program_sdk_version_token : 140 -> 164
~ __dyld_get_image_slide : 144 -> 168
~ _dyld_process_is_restricted : 140 -> 164
~ _dyld_version_token_at_least : 148 -> 172
~ _dyld_shared_cache_some_image_overridden : 140 -> 164
~ __dyld_get_prog_image_header : 140 -> 164
~ __dyld_lookup_section_info : 152 -> 176
~ _dyld_image_path_containing_address : 144 -> 168
~ _dlopen : 140 -> 164
~ _dyld_get_base_platform : 144 -> 168
~ __dyld_shared_cache_contains_path : 144 -> 168
~ __dyld_for_each_objc_protocol : 148 -> 172
~ _dlsym : 140 -> 164
~ __dyld_find_pointer_hash_table_entry : 156 -> 180
~ __dyld_find_foreign_type_protocol_conformance : 152 -> 176
~ __NSGetExecutablePath : 140 -> 164
~ _dyld_has_inserted_or_interposing_libraries : 144 -> 176
~ __dyld_lazy_load_internal : 148 -> 172
~ __dyld_get_lib_msg_send_offsets : 140 -> 164
~ __dyld_objc_register_callbacks : 296 -> 320
~ __dyld_get_shared_cache_range : 144 -> 168
~ __dyld_for_objc_header_opt_ro : 140 -> 164
~ __dyld_for_objc_header_opt_rw : 140 -> 164
~ __dyld_has_preoptimized_swift_protocol_conformances : 144 -> 168
~ _NSVersionOfLinkTimeLibrary : 136 -> 160
~ _dladdr : 140 -> 164
~ __dyld_launch_mode : 140 -> 164
~ __dyld_find_foreign_type_protocol_conformance_on_disk : 156 -> 180
~ _dyld_program_minos_at_least : 144 -> 168
~ __dyld_get_image_uuid : 148 -> 172
~ _dlopen_from : 152 -> 176
~ __dyld_get_swift_prespecialized_data : 140 -> 164
~ __dyld_register_for_bulk_image_loads : 144 -> 168
~ __dyld_get_dlopen_image_header : 144 -> 168
~ _dyld_get_program_sdk_version : 140 -> 164
~ __dyld_images_for_addresses : 152 -> 176
~ __tlv_atexit : 116 -> 140
~ __dyld_swift_optimizations_version : 140 -> 164
~ __dyld_get_shared_cache_uuid : 144 -> 168
~ __dyld_register_func_for_add_image : 136 -> 160
~ __dyld_register_func_for_remove_image : 136 -> 160
~ __dyld_image_count : 132 -> 156
~ __dyld_get_image_header : 136 -> 160
~ __dyld_is_preoptimized_objc_image_loaded : 144 -> 168
~ __dyld_get_image_name : 136 -> 160
~ _dlopen_preflight : 136 -> 160
~ _dlclose : 136 -> 160
~ _NSVersionOfRunTimeLibrary : 136 -> 160
~ _dyld_get_image_versions : 148 -> 172
~ __dyld_get_image_vmaddr_slide : 136 -> 160
~ _dlerror : 132 -> 156
~ __dyld_dlsym_blocked : 140 -> 164
~ __dyld_dlopen_atfork_prepare : 140 -> 164
~ __dyld_atfork_prepare : 140 -> 164
~ __dyld_atfork_parent : 140 -> 164
~ __dyld_dlopen_atfork_parent : 140 -> 164
~ __tlv_exit : 108 -> 132
~ _dyld_shared_cache_iterate_text : 208 -> 232
~ _dyld_shared_cache_file_path : 140 -> 164
~ _dyld_shared_cache_find_iterate_text : 232 -> 256
~ __dyld_register_dlsym_notifier : 144 -> 168
~ __dyld_fork_child : 372 -> 388
~ _dyld_get_sdk_version : 144 -> 168
~ _dyld_get_min_os_version : 144 -> 168
~ _dyld_get_program_min_os_version : 140 -> 164
~ _dyld_dynamic_interpose : 100 -> 124
~ __tlv_bootstrap_error : 116 -> 140
~ __dyld_shared_cache_file_path_containing_address : 152 -> 176
~ __dyld_objc_notify_register : 152 -> 176
~ _dyld_is_simulator_platform : 144 -> 168
~ _dyld_minos_at_least : 148 -> 172
~ __dyld_register_for_image_loads : 144 -> 168
~ _dyld_need_closure : 148 -> 172
~ __dyld_shared_cache_optimized : 140 -> 164
~ __dyld_shared_cache_is_locally_built : 140 -> 164
~ __dyld_register_driverkit_main : 144 -> 168
~ __dyld_is_objc_constant : 148 -> 172
~ __dyld_has_fix_for_radar : 144 -> 168
~ _dlopen_audited : 148 -> 172
~ __dyld_visit_objc_classes : 144 -> 168
~ __dyld_objc_uses_large_shared_cache : 140 -> 164
~ __dyld_dlopen_atfork_child : 140 -> 164
~ __dyld_pseudodylib_register_callbacks : 288 -> 312
~ __dyld_pseudodylib_deregister_callbacks : 144 -> 168
~ __dyld_pseudodylib_register : 156 -> 180
~ __dyld_pseudodylib_deregister : 144 -> 168
~ __dyld_register_dlsym_notifier_with_handle : 144 -> 168
~ __dyld_is_pseudodylib : 144 -> 168
~ _dyld_get_program_minos_version_token : 140 -> 164
~ _dyld_version_token_get_platform : 144 -> 168
~ __dyld_for_each_prewarming_range : 144 -> 168
~ __dyld_get_dyld_header : 140 -> 164
~ __dyld_shared_cache_will_check_for_image_overrides : 140 -> 164
~ ___clang_call_terminate : 20 -> 28
~ __ZNK6mach_o6Header19parse_dylib_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE : 280 -> 352
~ __ZNK6mach_o6Header20parse_string_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE : 220 -> 260
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb1EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2404 -> 2412
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb0EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2368 -> 2376
~ __ZNK6mach_o6Header29stringFromOffsetInLoadCommandERKNS0_15LoadCommandInfoEjPNS_5ErrorE : 284 -> 320
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
~ ____ZNK6mach_o6Header9dylibInfoEv_block_invoke : 124 -> 148
CStrings:
+ "load command #%d %.*s name offset too small"
+ "load command #%d %.*s not a dylib load command"
+ "load command #%d %.*s path offset too small"
+ "load command #%d string start offset too small"
```
