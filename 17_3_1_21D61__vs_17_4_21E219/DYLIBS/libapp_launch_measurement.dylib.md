## libapp_launch_measurement.dylib

> `/usr/lib/libapp_launch_measurement.dylib`

```diff

-17.0.0.0.0
-  __TEXT.__text: 0x1dac
-  __TEXT.__auth_stubs: 0x1b0
+18.1.0.0.0
+  __TEXT.__text: 0x209c
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x121
-  __TEXT.__oslogstring: 0x575
-  __TEXT.__unwind_info: 0xc4
-  __DATA_CONST.__got: 0x18
+  __TEXT.__cstring: 0x14d
+  __TEXT.__oslogstring: 0x5a7
+  __TEXT.__unwind_info: 0xd4
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x128
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0x148
   __DATA.__bss: 0x89
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
-  UUID: 075C2C41-D54B-3F48-84E7-7AE2F856AA0A
-  Functions: 44
-  Symbols:   110
-  CStrings:  41
+  - /usr/lib/libnetwork.dylib
+  UUID: 1570C80B-EF47-3242-AF7C-6D2F66638BEA
+  Functions: 48
+  Symbols:   130
+  CStrings:  44
 
Symbols:
+ ___alm_app_did_present_with_metrics_payload_block_invoke
+ ___alm_app_did_present_with_metrics_payload_block_invoke_2
+ ___alm_app_extended_launch_end_with_details_block_invoke
+ ___alm_app_extended_launch_end_with_details_block_invoke_2
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.28
+ ___block_descriptor_tmp.29
+ ___block_literal_global.19
+ ___block_literal_global.27
+ __os_log_debug_impl
+ __xpc_type_dictionary
+ _alm_app_did_present_with_metrics_payload
+ _alm_app_extended_launch_end_with_details
+ _alm_app_will_launch_with_details_and_metrics_payload
+ _alm_app_will_launch_with_details_and_metrics_payload.cold.1
+ _nw_activity_activate
+ _nw_activity_complete_with_reason
+ _nw_activity_copy_xpc_object
+ _nw_activity_create
+ _nw_activity_create_from_xpc_object
+ _nw_activity_set_global_parent
+ _nw_release
+ _xpc_dictionary_create
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_value
+ _xpc_get_type
+ _xpc_release
+ _xpc_retain
- ___alm_app_did_present_block_invoke
- ___alm_app_did_present_block_invoke_2
- ___alm_app_extended_launch_end_block_invoke
- ___alm_app_extended_launch_end_block_invoke_2
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.27
- ___block_literal_global.17
- ___block_literal_global.25
CStrings:
+ "appLaunchActivity"
+ "extendedAppLaunchActivity"
+ "network activtity data is added to metric payload"

```
