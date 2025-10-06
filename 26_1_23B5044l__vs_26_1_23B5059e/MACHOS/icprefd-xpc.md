## icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

-2020.1.5.0.0
-  __TEXT.__text: 0x2a4c
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x740
+2020.1.6.0.0
+  __TEXT.__text: 0x322c
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x7ef
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__cstring: 0x95b
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__objc_methname: 0x78b
+  __TEXT.__objc_methname: 0x69d
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methtype: 0x115
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x150
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__cfstring: 0x7e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x228
+  __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3675E345-F48E-3996-9404-C54EC70AA859
-  Functions: 25
-  Symbols:   186
-  CStrings:  210
+  UUID: 913A7C8B-5D88-333F-B5F9-5CAADEB053E5
+  Functions: 27
+  Symbols:   193
+  CStrings:  215
 
Symbols:
+ GCC_except_table11
+ __63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke.89
+ ___63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke
+ ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
+ ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8r40l8
+ _objc_msgSend$captureUserIntentForBundleIdentifier:withNotification:
+ _tcc_authorization_record_get_authorization_right
+ _tcc_credential_create_for_process_with_audit_token
+ _tcc_message_options_create
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_message_options_set_request_usage_string_policy
+ _tcc_server_create
+ _tcc_server_message_request_authorization
+ _tcc_server_message_request_authorization_change
+ _tcc_service_singleton_for_name
- _objc_msgSend$_xpcConnection
- _objc_msgSend$captureReadUserIntentForBundleIdentifier:withNotification:
- _objc_msgSend$captureUserIntentForConnection:accessType:
- _objc_msgSend$captureUserIntentForControlWithBundleIdentifier:withNotification:
- _objc_msgSend$getControlNotifiedStatusWithBundleIdentifier:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$setControlNotifiedStatus:withBundleIdentifier:
- _objc_release_x22
CStrings:
+ "(check) Authorization Right: %llu"
+ "(check) Granted %@ access to *contents* on external device"
+ "(check) User denied or disabled %@ access to *contents* on external device"
+ "(prompt) ---> New kTCCServiceExternalCameraMedia Service"
+ "(prompt) Granted %@ access to *contents* on external device"
+ "(prompt) User denied or disabled %@ access to *contents* on external device"
+ "captureUserIntentForBundleIdentifier:withNotification:"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
- "(good news) ---> New kTCCServiceExternalCameraMedia Service"
- "_xpcConnection"
- "captureReadUserIntentForBundleIdentifier:withNotification:"
- "captureUserIntentForConnection:accessType:"
- "captureUserIntentForControlWithBundleIdentifier:withNotification:"
- "getControlNotifiedStatusWithBundleIdentifier:"
- "isEqualToString:"
- "setControlNotifiedStatus:withBundleIdentifier:"

```
