## icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

-2013.0.0.0.0
-  __TEXT.__text: 0x5014
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x22c
-  __TEXT.__cstring: 0x1f15
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__objc_methname: 0xa70
-  __TEXT.__oslogstring: 0x34
+2016.0.0.0.0
+  __TEXT.__text: 0x6ec4
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x244
+  __TEXT.__cstring: 0x21dc
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x410
+  __TEXT.__objc_methname: 0xaea
+  __TEXT.__oslogstring: 0x75
+  __TEXT.__ustring: 0xe
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0x1c7
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__auth_got: 0x198
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__cfstring: 0x1de0
+  __TEXT.__objc_methtype: 0x1d6
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__cfstring: 0x1fc0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x2880
   __DATA_CONST.__objc_dictobj: 0x21c0
   __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_selrefs: 0x310
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E380B476-55A7-3C19-868E-8C4723C758F1
-  Functions: 70
-  Symbols:   305
-  CStrings:  619
+  UUID: E2F30DF3-8671-3EB9-A3BF-F244A2918DC9
+  Functions: 84
+  Symbols:   360
+  CStrings:  656
 
Symbols:
+ -[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]
+ -[ICDeviceAccessManager displayAlertForControlWithNotification:completionBlock:]
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table8
+ _CFErrorCopyDescription
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _TCCAccessResetForBundleId
+ __63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke.89
+ __66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke.cold.1
+ __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke.128
+ __69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2.cold.1
+ __74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.70
+ __74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.cold.1
+ __76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke.cold.1
+ ___63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke
+ ___66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke
+ ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2
+ ___74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke
+ ___76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke
+ ___90-[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]_block_invoke
+ ___block_descriptor_32_e20_v16?0^{__CFError=}8l
+ ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
+ ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8r40l8
+ __block_literal_global.130
+ __block_literal_global.73
+ __os_feature_enabled_impl
+ __os_log_default
+ _kTCCServiceExternalCameraMedia
+ _objc_msgSend$displayAlertForControlWithNotification:completionBlock:
+ _tcc_attributed_entity_get_path
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_authorization_value
+ _tcc_authorization_record_get_service
+ _tcc_authorization_record_get_subject_attributed_entity
+ _tcc_authorization_record_get_subject_identity
+ _tcc_credential_create_for_process_with_audit_token
+ _tcc_identity_create
+ _tcc_identity_get_identifier
+ _tcc_message_options_create
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_message_options_set_request_usage_string_policy
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_identity
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_server_message_request_authorization
+ _tcc_server_message_request_authorization_change
+ _tcc_server_message_set_authorization_value
+ _tcc_service_get_name
+ _tcc_service_singleton_for_CF_name
+ _tcc_service_singleton_for_name
- GCC_except_table20
- GCC_except_table27
- GCC_except_table30
- _objc_release_x22
CStrings:
+ "(check) ---> New kTCCServiceExternalCameraMedia Service"
+ "(check) Authorization Right: %llu"
+ "(check) Granted %@ access to *contents* on external device"
+ "(check) User denied or disabled %@ access to *contents* on external device"
+ "(prompt) ---> New kTCCServiceExternalCameraMedia Service"
+ "(prompt) Granted %@ access to *contents* on external device"
+ "(prompt) User denied or disabled %@ access to *contents* on external device"
+ "(reset) ---> New kTCCServiceExternalCameraMedia Service"
+ "???"
+ "Bundle:%s -- value: %llu"
+ "ImageCapture"
+ "No work performed in new TCC path"
+ "TCCServiceExternalCameraMedia_iOS"
+ "captureUserIntentForControlWithBundleIdentifier:withNotification:"
+ "displayAlertForControlWithNotification:completionBlock:"
+ "entity"
+ "kTCCServiceExternalCameraMedia"
+ "tcc_server_message_get_authorization_records_by_service error %@"
+ "v16@?0^{__CFError=}8"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "v32@0:8@16@?24"
+ "value"

```
