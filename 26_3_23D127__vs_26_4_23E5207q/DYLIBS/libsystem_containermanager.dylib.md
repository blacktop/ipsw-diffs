## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-725.80.5.0.0
-  __TEXT.__text: 0x2d9a0
+725.100.34.0.0
+  __TEXT.__text: 0x2d800
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x3a62
-  __TEXT.__oslogstring: 0x4f5e
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x3a63
+  __TEXT.__oslogstring: 0x4f32
+  __TEXT.__unwind_info: 0x688
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x1c40
   __AUTH_CONST.__auth_got: 0x5b8

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: DFBE5AEC-5534-35F4-B6A6-D0466A996E71
+  UUID: 243CE960-08A0-3293-87D5-22345DAD95AE
   Functions: 588
   Symbols:   1289
-  CStrings:  893
+  CStrings:  892
 
Symbols:
+ ___block_descriptor_tmp.10.1063
+ ___block_descriptor_tmp.11.1064
+ ___block_descriptor_tmp.12.1065
+ ___block_descriptor_tmp.13.1070
+ ___block_descriptor_tmp.17.1074
+ ___block_descriptor_tmp.26.1083
+ ___block_descriptor_tmp.28.1086
+ ___block_descriptor_tmp.34.1090
+ ___block_descriptor_tmp.36.1092
+ ___block_descriptor_tmp.37.1094
+ ___block_descriptor_tmp.7.1059
+ ___block_descriptor_tmp.8.1062
+ ___block_descriptor_tmp.81.1120
+ ___block_descriptor_tmp.9.1060
+ ___block_literal_global.1124
- ___block_descriptor_tmp.10.1064
- ___block_descriptor_tmp.11.1065
- ___block_descriptor_tmp.12.1066
- ___block_descriptor_tmp.13.1071
- ___block_descriptor_tmp.17.1075
- ___block_descriptor_tmp.26.1084
- ___block_descriptor_tmp.28.1087
- ___block_descriptor_tmp.34.1091
- ___block_descriptor_tmp.36.1093
- ___block_descriptor_tmp.37.1095
- ___block_descriptor_tmp.7.1060
- ___block_descriptor_tmp.8.1063
- ___block_descriptor_tmp.81.1121
- ___block_descriptor_tmp.9.1061
- ___block_literal_global.1125
Functions:
~ _container_xpc_send_message : 424 -> 428
~ __container_query_get_result_at_index : 608 -> 604
~ ___container_create_or_lookup_app_group_path_by_app_group_identifier_block_invoke : 2260 -> 2256
~ _c_array_append : 256 -> 252
~ _container_frozenset_create : 1296 -> 1292
~ _container_query_iterate_results_sync : 636 -> 632
~ _container_string_rom_create : 2900 -> 2740
~ _container_string_rom_string_at_index : 660 -> 632
~ __container_pwd : 424 -> 420
~ _container_frozenset_enumerate_matches : 828 -> 824
~ _container_fs_resolve_dirent_type_at : 140 -> 144
~ _container_client_copy_decoded_from_xpc_object : 1192 -> 1184
~ _container_client_is_alive : 72 -> 56
~ __container_user_prefix_managed_by_containermanager_transient : 272 -> 288
~ ___container_paths_create_uid_home_relative_block_invoke : 740 -> 736
~ _container_serialize_copy_deserialized_reference : 456 -> 460
~ __container_serialize_copy_deserialized_reference_v1 : 968 -> 952
~ ___container_references_set_persona_unique_string_block_invoke : 352 -> 348
~ __container_references_query_execute : 2568 -> 2564
~ __container_init : 1428 -> 1408
~ _container_traverse_directory : 3944 -> 3900
~ __container_traverse_get_continuation_fd : 336 -> 328
~ __container_traverse_parse_attr_buf : 3564 -> 3556
~ _container_traverse_node_get_optional_link_count : 376 -> 372
~ ___container_persona_collect_all_ids_block_invoke : 28 -> 24
~ ____container_log_replication_enable_to_uid_relative_path_block_invoke_2 : 204 -> 208
~ _container_query_iterate_results_with_subquery_sync : 808 -> 804
~ ___container_query_copy_block_invoke : 368 -> 376
~ _container_disposition_for_array : 208 -> 204
~ ___container_copy_path_block_invoke : 420 -> 480
~ _container_create_merged_array : 408 -> 404
~ ___container_notify_start_block_invoke : 1076 -> 1072
~ __container_base64_decode : 484 -> 476
~ _container_string_rom_index_of : 1196 -> 1184
~ _container_pwd_copy_user_home_path : 964 -> 972
~ ___container_bundle_copy_data_container_path_block_invoke : 240 -> 252
~ __common_bundle_lookup : 2044 -> 1924
~ ___container_create_or_lookup_system_group_paths_block_invoke : 436 -> 428
~ ___container_create_or_lookup_app_group_paths_for_platform_block_invoke : 432 -> 424
~ ___container_create_or_lookup_app_group_paths_from_entitlements_4ls_block_invoke : 464 -> 456
CStrings:
+ "@(#)VERSION:Container Manager: Jan 26 2026 08:15:06; MobileContainerManager_system-725.100.34~99/arm64e"
- "@(#)VERSION:Container Manager: Jan 16 2026 14:30:24; MobileContainerManager_system-725.80.5~157/arm64e"
- "Could not allocate return container object."

```
