## icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

-2020.2.2.0.0
-  __TEXT.__text: 0x322c
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x680
+2112.0.0.0.0
+  __TEXT.__text: 0x2ab0
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x95b
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__cstring: 0x7ef
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__objc_methname: 0x69d
+  __TEXT.__objc_methname: 0x7cf
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methtype: 0x115
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0xf8
-  __DATA_CONST.__cfstring: 0x7e0
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x108
   __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_selrefs: 0x230
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7630E5C9-7BE3-32F1-AD88-2B537E3B6C8E
-  Functions: 27
-  Symbols:   193
-  CStrings:  215
+  UUID: 749C8726-7A1A-3454-84F9-810336660273
+  Functions: 25
+  Symbols:   186
+  CStrings:  211
 
Symbols:
+ _objc_msgSend$_xpcConnection
+ _objc_msgSend$captureReadUserIntentForBundleIdentifier:withNotification:
+ _objc_msgSend$captureUserIntentForConnection:accessType:shouldPrompt:
+ _objc_msgSend$captureUserIntentForControlWithBundleIdentifier:withNotification:
+ _objc_msgSend$getControlNotifiedStatusWithBundleIdentifier:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$setControlNotifiedStatus:withBundleIdentifier:
- GCC_except_table11
- __63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke.89
- ___63-[ICRemotePrefManager checkFilesAndFoldersAccess:shouldPrompt:]_block_invoke
- ___block_descriptor_40_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
- ___block_descriptor_48_e8_32o40r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8r40l8
- _tcc_authorization_record_get_authorization_right
- _tcc_credential_create_for_process_with_audit_token
- _tcc_message_options_create
- _tcc_message_options_set_reply_handler_policy
- _tcc_message_options_set_request_usage_string_policy
- _tcc_server_create
- _tcc_server_message_request_authorization
- _tcc_server_message_request_authorization_change
- _tcc_service_singleton_for_name
CStrings:
+ "(good news) ---> New kTCCServiceExternalCameraMedia Service"
+ "_xpcConnection"
+ "captureReadUserIntentForBundleIdentifier:withNotification:"
+ "captureUserIntentForConnection:accessType:shouldPrompt:"
+ "captureUserIntentForControlWithBundleIdentifier:withNotification:"
+ "getControlNotifiedStatusWithBundleIdentifier:"
+ "isEqualToString:"
+ "setControlNotifiedStatus:withBundleIdentifier:"
- "(check) Authorization Right: %llu"
- "(check) Granted %@ access to *contents* on external device"
- "(check) User denied or disabled %@ access to *contents* on external device"
- "(prompt) ---> New kTCCServiceExternalCameraMedia Service"
- "(prompt) Granted %@ access to *contents* on external device"
- "(prompt) User denied or disabled %@ access to *contents* on external device"
- "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"

```
