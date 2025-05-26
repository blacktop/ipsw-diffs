## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

-98.0.0.0.0
-  __TEXT.__text: 0x1568
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x104
+101.0.0.0.0
+  __TEXT.__text: 0x1a94
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x16b
-  __TEXT.__oslogstring: 0x22d
-  __TEXT.__unwind_info: 0xbc
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__cstring: 0x1a1
+  __TEXT.__oslogstring: 0x2e4
+  __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x44f
+  __TEXT.__objc_methname: 0x48f
   __TEXT.__objc_methtype: 0x7e
-  __TEXT.__objc_stubs: 0x440
+  __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x118
-  __DATA_CONST.__objc_selrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x188
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x40
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x148
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x40
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x198
   __DATA.__data: 0x60
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x90
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 28
-  Symbols:   195
-  CStrings:  88
+  Functions: 33
+  Symbols:   223
+  CStrings:  95
 
Symbols:
+ +[ATTrackingManager _TCCServer]
+ +[ATTrackingManager _performTCCAccessRequest]
+ +[ATTrackingManager _performTCCPreflightRequest]
+ GCC_except_table11
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table9
+ __TCCServer.onceToken
+ __TCCServer.server
+ ___31+[ATTrackingManager _TCCServer]_block_invoke
+ ___45+[ATTrackingManager _performTCCAccessRequest]_block_invoke
+ ___48+[ATTrackingManager _performTCCPreflightRequest]_block_invoke
+ ___block_descriptor_48_e8_32r_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16lr32l8
+ ___block_literal_global.33
+ _objc_msgSend$_TCCServer
+ _objc_msgSend$_performTCCAccessRequest
+ _objc_msgSend$_performTCCPreflightRequest
+ _objc_release_x1
+ _objc_release_x24
+ _objc_retainBlock
+ _objc_retain_x1
+ _tcc_authorization_record_get_authorization_right
+ _tcc_credential_singleton_for_self
+ _tcc_message_options_create
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_message_options_set_request_prompt_policy
+ _tcc_server_create
+ _tcc_server_message_request_authorization
+ _tcc_service_singleton_for_CF_name
- GCC_except_table7
- _TCCAccessPreflight
- _TCCAccessRequest
- ___71+[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:]_block_invoke
- ___block_descriptor_48_e8_32bs_e8_v12?0C8ls32l8
CStrings:
+ "[%@] Performing TCC Access Preflight Request."
+ "[%@] Performing TCC Access Request."
+ "[%@] Received error invoking TCC access request."
+ "[%@] Received error invoking TCC preflight request."
+ "_TCCServer"
+ "_performTCCAccessRequest"
+ "_performTCCPreflightRequest"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
- "v12@?0C8"

```
