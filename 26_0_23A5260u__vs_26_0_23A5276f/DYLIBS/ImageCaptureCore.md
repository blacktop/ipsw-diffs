## ImageCaptureCore

> `/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore`

```diff

-2013.0.0.0.0
-  __TEXT.__text: 0x3c10c
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x391c
-  __TEXT.__const: 0x84
-  __TEXT.__gcc_except_tab: 0xe18
-  __TEXT.__cstring: 0x5e35
-  __TEXT.__oslogstring: 0x3f
-  __TEXT.__ustring: 0x478
-  __TEXT.__unwind_info: 0xcb0
+2016.0.0.0.0
+  __TEXT.__text: 0x3d8ac
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x3934
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x11b4
+  __TEXT.__cstring: 0x5f40
+  __TEXT.__oslogstring: 0x80
+  __TEXT.__ustring: 0x486
+  __TEXT.__unwind_info: 0xd00
   __TEXT.__objc_classname: 0x337
-  __TEXT.__objc_methname: 0x93c6
+  __TEXT.__objc_methname: 0x9440
   __TEXT.__objc_methtype: 0xee2
-  __TEXT.__objc_stubs: 0x6100
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xf28
+  __TEXT.__objc_stubs: 0x6120
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0xf70
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2488
+  __DATA_CONST.__objc_selrefs: 0x2498
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x28d8
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x78c0
+  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x79c0
   __AUTH_CONST.__objc_const: 0x4a18
   __AUTH_CONST.__objc_dictobj: 0x2238
   __AUTH_CONST.__objc_intobj: 0x750

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9D6A1E2C-064B-3046-8C78-21B1907257C6
-  Functions: 1389
-  Symbols:   4550
-  CStrings:  3869
+  UUID: 479F2F23-852E-37C9-A9A2-7451E696B92E
+  Functions: 1400
+  Symbols:   4607
+  CStrings:  3891
 
Symbols:
+ -[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]
+ -[ICDeviceAccessManager displayAlertForControlWithNotification:completionBlock:]
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table36
+ GCC_except_table39
+ _CFErrorCopyDescription
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.248
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.258
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.268
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.283
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.299
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke_2.300
+ ___58-[ICCameraFile requestReadDataAtOffset:length:completion:]_block_invoke.320
+ ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.172
+ ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.196
+ ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.205
+ ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.215
+ ___66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke
+ ___66-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCameras]_block_invoke.cold.1
+ ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke.130
+ ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2
+ ___69-[ICDeviceAccessManager updateBundleIdentifier:accessType:withState:]_block_invoke_2.cold.1
+ ___74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke
+ ___74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.72
+ ___74-[ICDeviceAccessManager updateApplicationWithBundleIdentifier:withStatus:]_block_invoke.cold.1
+ ___76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke
+ ___76-[ICDeviceAccessManager bundleIdentifiersAccessingExternalCamerasWithStatus]_block_invoke.cold.1
+ ___90-[ICDeviceAccessManager captureUserIntentForControlWithBundleIdentifier:withNotification:]_block_invoke
+ ___block_descriptor_32_e20_v16?0^{__CFError=}8l
+ ___block_descriptor_48_e8_32s40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr40l8s32l8
+ ___block_literal_global.132
+ ___block_literal_global.75
+ __os_feature_enabled_impl
+ __os_log_default
+ _kTCCServiceExternalCameraMedia
+ _objc_msgSend$displayAlertForControlWithNotification:completionBlock:
+ _tcc_attributed_entity_get_path
+ _tcc_authorization_record_get_authorization_value
+ _tcc_authorization_record_get_service
+ _tcc_authorization_record_get_subject_attributed_entity
+ _tcc_authorization_record_get_subject_identity
+ _tcc_identity_create
+ _tcc_identity_get_identifier
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_identity
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_server_message_set_authorization_value
+ _tcc_service_get_name
+ _tcc_service_singleton_for_CF_name
- GCC_except_table20
- GCC_except_table30
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.245
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.255
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.265
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.280
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.296
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke_2.297
- ___58-[ICCameraFile requestReadDataAtOffset:length:completion:]_block_invoke.317
- ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.169
- ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.193
- ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.202
- ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.212
CStrings:
+ "(check) ---> New kTCCServiceExternalCameraMedia Service"
+ "???"
+ "Bundle:%s -- value: %llu"
+ "HIF"
+ "ImageCapture"
+ "No work performed in new TCC path"
+ "TCCServiceExternalCameraMedia_iOS"
+ "captureUserIntentForControlWithBundleIdentifier:withNotification:"
+ "displayAlertForControlWithNotification:completionBlock:"
+ "entity"
+ "tcc_server_message_get_authorization_records_by_service error %@"
+ "v16@?0^{__CFError=}8"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "value"

```
