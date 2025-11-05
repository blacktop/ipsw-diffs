## libsystem_asl.dylib

> `/usr/lib/system/libsystem_asl.dylib`

```diff

 402.0.0.0.0
-  __TEXT.__text: 0x15590
+  __TEXT.__text: 0x1534c
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x1011
-  __TEXT.__unwind_info: 0x4d8
-  __DATA_CONST.__got: 0x68
+  __TEXT.__cstring: 0x1002
+  __TEXT.__unwind_info: 0x4c8
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x5c0
   __AUTH_CONST.__auth_got: 0x4e8
   __AUTH_CONST.__const: 0x560

   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 26693E85-AFDC-38E2-B939-D6EC865FA506
-  Functions: 386
-  Symbols:   625
-  CStrings:  327
+  UUID: 9BAEFFB7-48AF-322A-9115-182C60AEBADD
+  Functions: 399
+  Symbols:   661
+  CStrings:  322
 
Symbols:
+ __asl_level_char
+ __asl_level_string
+ _asl_auxiliary.cold.1
+ _asl_evaluate_send.cold.1
+ _asl_open_default.cold.1
+ _asl_send_message.cold.1
+ _asl_send_message.cold.2
+ _asl_send_message_text.cold.1
+ _asl_server_control_query.cold.1
+ asl_add_output_file.cold.1
+ asl_core_get_service_port.cold.1
+ asl_filesystem_path.cold.1
+ asl_get_filter.cold.1
+ asl_get_local_control.cold.1
+ asl_log_from_descriptor.cold.1
+ asl_new.cold.1
+ asl_object_append.cold.1
+ asl_object_count.cold.1
+ asl_object_get_key_val_op_at_index.cold.1
+ asl_object_get_object_at_index.cold.1
+ asl_object_get_val_op_for_key.cold.1
+ asl_object_match.cold.1
+ asl_object_next.cold.1
+ asl_object_prepend.cold.1
+ asl_object_prev.cold.1
+ asl_object_remove_object_at_index.cold.1
+ asl_object_search.cold.1
+ asl_object_set_iteration_index.cold.1
+ asl_object_set_key_val_op.cold.1
+ asl_object_unset_key.cold.1
+ asl_release.cold.1
+ asl_remove_output_file.cold.1
+ asl_set_filter.cold.1
+ asl_set_local_control.cold.1
+ asl_set_output_file_filter.cold.1
+ asl_store_location.cold.1
CStrings:
- "\t "
- "+-"
- "-1"
- "Q"
- "UTC"

```
