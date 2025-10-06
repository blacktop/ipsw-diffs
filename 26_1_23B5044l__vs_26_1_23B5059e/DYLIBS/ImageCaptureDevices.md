## ImageCaptureDevices

> `/System/Library/PrivateFrameworks/ImageCaptureDevices.framework/ImageCaptureDevices`

```diff

-2020.1.5.0.0
-  __TEXT.__text: 0x1a30c
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x1cfc
+2020.1.6.0.0
+  __TEXT.__text: 0x18e40
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x1cc4
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x720
-  __TEXT.__cstring: 0x68e1
+  __TEXT.__gcc_except_tab: 0x5a8
+  __TEXT.__cstring: 0x6684
   __TEXT.__oslogstring: 0x75
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__unwind_info: 0x560
   __TEXT.__objc_classname: 0x236
-  __TEXT.__objc_methname: 0x45e2
+  __TEXT.__objc_methname: 0x44de
   __TEXT.__objc_methtype: 0x931
-  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__objc_stubs: 0x20e0
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f8
+  __DATA_CONST.__objc_selrefs: 0x12d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x2880
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x7160
+  __AUTH_CONST.__cfstring: 0x6fe0
   __AUTH_CONST.__objc_const: 0x2930
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x21c0
-  __AUTH.__objc_data: 0x5f0
+  __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x264
   __DATA.__data: 0x2b8
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x38
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5D857AB4-7E24-337B-B312-F0739B2797F4
-  Functions: 662
-  Symbols:   2135
-  CStrings:  2860
+  UUID: 599EA744-98C5-3538-B7E4-06A05902BD3F
+  Functions: 653
+  Symbols:   2101
+  CStrings:  2830
 
Symbols:
+ GCC_except_table33
+ GCC_except_table36
- -[ICDeviceAccessManager captureReadUserIntentForBundleIdentifier:withNotification:]
- -[ICDeviceAccessManager captureUserIntentForConnection:accessType:]
- -[ICDeviceAccessManager displayReadAlertForApplication:withNotification:completionBlock:]
- -[ICDeviceAccessManager getControlNotifiedStatusWithBundleIdentifier:]
- -[ICDeviceAccessManager setControlNotifiedStatus:withBundleIdentifier:]
- GCC_except_table30
- GCC_except_table34
- GCC_except_table37
- GCC_except_table43
- GCC_except_table48
- ___61-[ICDeviceAccessManager bundleIdentifier:stateForAccessType:]_block_invoke
- ___61-[ICDeviceAccessManager bundleIdentifier:stateForAccessType:]_block_invoke.cold.1
- ___67-[ICDeviceAccessManager captureUserIntentForConnection:accessType:]_block_invoke
- ___67-[ICDeviceAccessManager captureUserIntentForConnection:accessType:]_block_invoke.173
- ___83-[ICDeviceAccessManager captureReadUserIntentForBundleIdentifier:withNotification:]_block_invoke
- ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
- ___block_descriptor_56_e8_32s40s48r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8s40l8r48l8
- _objc_msgSend$displayReadAlertForApplication:withNotification:completionBlock:
- _tcc_authorization_record_get_authorization_right
- _tcc_credential_create_for_process_with_audit_token
- _tcc_message_options_create
- _tcc_message_options_set_reply_handler_policy
- _tcc_message_options_set_request_usage_string_policy
- _tcc_server_message_request_authorization
- _tcc_server_message_request_authorization_change
- _tcc_service_singleton_for_name
CStrings:
- "(check) Authorization Right: %llu"
- "(check) Granted %@ %@ access to *contents* on external device"
- "(check) User denied or disabled %@ %@ access to *contents* on external device"
- "(good news) ---> New kTCCServiceExternalCameraMedia Service"
- "(prompt) ---> New kTCCServiceExternalCameraMedia Service"
- "(prompt) Granted %@ %@ access to *contents* on external device"
- "(prompt) User denied or disabled %@ %@ access to *contents* on external device"
- "(set good news) ---> New kTCCServiceExternalCameraMedia Service: %@"
- "ICAuthorizationStatusNotDetermined"
- "ICGoodNewsStatusDictionary"
- "captureReadUserIntentForBundleIdentifier:withNotification:"
- "captureUserIntentForConnection:accessType:"
- "displayReadAlertForApplication:withNotification:completionBlock:"
- "getControlNotifiedStatusWithBundleIdentifier:"
- "kTCCServiceExternalCameraMedia"
- "read"
- "setControlNotifiedStatus:withBundleIdentifier:"
- "write"

```
