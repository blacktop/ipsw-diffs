## libmrc.dylib

> `/usr/lib/libmrc.dylib`

```diff

-2200.80.16.0.0
-  __TEXT.__text: 0x2608
-  __TEXT.__auth_stubs: 0x360
+2200.100.94.0.2
+  __TEXT.__text: 0x340c
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1eb
+  __TEXT.__cstring: 0x326
   __TEXT.__oslogstring: 0x17c
-  __TEXT.__unwind_info: 0xf4
-  __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methname: 0x148
+  __TEXT.__unwind_info: 0x15c
+  __TEXT.__objc_classname: 0xad
+  __TEXT.__objc_methname: 0x15b
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x190
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6b0
+  __DATA_CONST.__objc_const: 0x9c8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__auth_got: 0x200
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_classrefs: 0x8
   __DATA.__objc_superrefs: 0x8
-  __DATA.__data: 0x1e0
+  __DATA.__data: 0x300
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 59
-  Symbols:   241
-  CStrings:  87
+  Functions: 96
+  Symbols:   356
+  CStrings:  108
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFSetApplyFunction
+ _CFSetGetCount
+ _CFSetGetValues
+ _OBJC_CLASS_$_OS_mrc_dns_service_registration
+ _OBJC_CLASS_$_OS_mrc_enabler
+ _OBJC_CLASS_$_OS_mrc_mdns_string_builder
+ _OBJC_METACLASS_$_OS_mrc_dns_service_registration
+ _OBJC_METACLASS_$_OS_mrc_enabler
+ _OBJC_METACLASS_$_OS_mrc_mdns_string_builder
+ __OBJC_$_PROP_LIST_OS_mrc_dns_service_registration
+ __OBJC_$_PROP_LIST_OS_mrc_enabler
+ __OBJC_$_PROP_LIST_OS_mrc_mdns_string_builder
+ __OBJC_$_PROTOCOL_REFS_OS_mrc_dns_service_registration
+ __OBJC_$_PROTOCOL_REFS_OS_mrc_enabler
+ __OBJC_$_PROTOCOL_REFS_OS_mrc_mdns_string_builder
+ __OBJC_CLASS_PROTOCOLS_$_OS_mrc_dns_service_registration
+ __OBJC_CLASS_PROTOCOLS_$_OS_mrc_enabler
+ __OBJC_CLASS_PROTOCOLS_$_OS_mrc_mdns_string_builder
+ __OBJC_CLASS_RO_$_OS_mrc_dns_service_registration
+ __OBJC_CLASS_RO_$_OS_mrc_enabler
+ __OBJC_CLASS_RO_$_OS_mrc_mdns_string_builder
+ __OBJC_LABEL_PROTOCOL_$_OS_mrc_dns_service_registration
+ __OBJC_LABEL_PROTOCOL_$_OS_mrc_enabler
+ __OBJC_LABEL_PROTOCOL_$_OS_mrc_mdns_string_builder
+ __OBJC_METACLASS_RO_$_OS_mrc_dns_service_registration
+ __OBJC_METACLASS_RO_$_OS_mrc_enabler
+ __OBJC_METACLASS_RO_$_OS_mrc_mdns_string_builder
+ __OBJC_PROTOCOL_$_OS_mrc_dns_service_registration
+ __OBJC_PROTOCOL_$_OS_mrc_enabler
+ __OBJC_PROTOCOL_$_OS_mrc_mdns_string_builder
+ ____mrc_client_activate_async_block_invoke
+ ____mrc_client_invalidate_async_block_invoke
+ ____mrc_dns_service_registration_generate_event_with_error_block_invoke
+ ____mrc_enabler_activate_async_block_invoke
+ ____mrc_enabler_invalidate_async_block_invoke
+ ____mrc_enabler_send_start_message_block_invoke
+ ____mrc_enabler_send_stop_message_block_invoke
+ ___block_descriptor_tmp.19.318
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.24.326
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.328
+ ___block_descriptor_tmp.33
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.38
+ ___block_descriptor_tmp.7
+ ___block_literal_global.27
+ ___block_literal_global.324
+ ___block_literal_global.40
+ ___mdns_dns_service_definition_create_xpc_dictionary_block_invoke
+ ___mdns_dns_service_definition_create_xpc_dictionary_block_invoke_2
+ __mdns_cf_applier_function
+ __mdns_string_builder_copy_description
+ __mdns_string_builder_finalize
+ __mdns_string_builder_grow_buffer
+ __mdns_string_builder_kind
+ __mrc_client_activate_async
+ __mrc_client_finalize
+ __mrc_client_invalidate_async
+ __mrc_client_kind
+ __mrc_client_set_queue
+ __mrc_dns_proxy_create_start_message
+ __mrc_dns_proxy_create_stop_message
+ __mrc_dns_proxy_handle_interruption
+ __mrc_dns_proxy_handle_invalidation
+ __mrc_dns_proxy_handle_start_event
+ __mrc_dns_service_registration_copy_description
+ __mrc_dns_service_registration_create_start_message
+ __mrc_dns_service_registration_create_stop_message
+ __mrc_dns_service_registration_finalize
+ __mrc_dns_service_registration_generate_event_with_error
+ __mrc_dns_service_registration_handle_interruption
+ __mrc_dns_service_registration_handle_invalidation
+ __mrc_dns_service_registration_handle_start_event
+ __mrc_dns_service_registration_kind
+ __mrc_enabler_copy_description
+ __mrc_enabler_finalize
+ __mrc_enabler_invalidate_async
+ __mrc_enabler_kind
+ __mrc_enabler_send_start_message
+ _calloc
+ _g_enabler_list
+ _malloc_good_size
+ _mdns_string_builder_append_formatted
+ _mdns_string_builder_copy_string
+ _mdns_string_builder_create
+ _mdns_xpc_dictionary_array_append_string
+ _mrc_dns_service_registration_activate
+ _mrc_dns_service_registration_create
+ _mrc_dns_service_registration_invalidate
+ _mrc_dns_service_registration_set_event_handler
+ _mrc_dns_service_registration_set_queue
+ _xpc_array_create_empty
+ _xpc_array_set_string
+ _xpc_dictionary_create_empty
- ____mrc_dns_proxy_start_block_invoke
- ____mrc_dns_proxy_stop_block_invoke
- ____mrc_dns_proxy_terminate_async_block_invoke
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.8
- ___block_literal_global.11
- ___block_literal_global.21
- ___block_literal_global.31
- ___mrc_dns_proxy_activate_block_invoke
- __mrc_dns_proxy_start
- __mrc_dns_proxy_terminate_async
- _g_dns_proxy_list
CStrings:
+ "B16@?0r^{mdns_address_s=}8"
+ "B16@?0r^{mdns_domain_name_s=}8"
+ "DNS Proxy"
+ "DNS Service Registration"
+ "OS_mrc_dns_service_registration"
+ "OS_mrc_enabler"
+ "OS_mrc_mdns_string_builder"
+ "T@\"NSString\",?,R,C"
+ "[E%llu] %{public}s start reply -- error: %{mdns:err}ld"
+ "[E%llu] %{public}s stop reply -- error: %{mdns:err}ld"
+ "[E%llu] Abnormal %{public}s start reply: %{public}s"
+ "[E%llu] Abnormal %{public}s stop reply: %{public}s"
+ "addresses"
+ "capacity: %zu, string length: %zu"
+ "definition"
+ "dns_service_registration.start"
+ "dns_service_registration.stop"
+ "domains"
+ "entity: %s"
+ "ifindex"
+ "mdns_string_builder"
+ "mrc_client"
+ "mrc_dns_service_registration"
+ "mrc_enabler"
+ "scoped"
- "[DP%llu] Abnormal DNS proxy start reply: %{public}s"
- "[DP%llu] Abnormal DNS proxy stop reply: %{public}s"
- "[DP%llu] DNS proxy start reply -- error: %{mdns:err}ld"
- "[DP%llu] DNS proxy stop reply -- error: %{mdns:err}ld"

```
