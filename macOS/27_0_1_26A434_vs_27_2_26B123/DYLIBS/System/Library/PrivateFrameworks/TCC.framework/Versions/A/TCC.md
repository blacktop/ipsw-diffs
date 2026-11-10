## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC`

```diff

-913.3.3.0.0
-  __TEXT.__text: 0x1e794
+921.0.1.0.0
+  __TEXT.__text: 0x1efe8
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x3b0
-  __TEXT.__cstring: 0x3913
-  __TEXT.__oslogstring: 0x2464
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__cstring: 0x3a52
+  __TEXT.__oslogstring: 0x2552
+  __TEXT.__unwind_info: 0x718
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa40
+  __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1f68
-  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__const: 0x1ff8
+  __AUTH_CONST.__cfstring: 0x17c0
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 764
-  Symbols:   1168
-  CStrings:  721
+  Functions: 777
+  Symbols:   1180
+  CStrings:  733
 
Symbols:
+ TCCCopyIconIdentifierForService
+ _TCCCopyIconIdentifierForService
+ __TCCCopyIconIdentifierForService_block_invoke_2
+ ___TCCCopyIconIdentifierForService_block_invoke
+ ___TCCCopyIconIdentifierForService_block_invoke_2
+ ___tcc_authorization_bundle_identifier_report_use_block_invoke
+ __tcc_authorization_bundle_identifier_report_use_block_invoke
+ _tcc_authorization_bundle_identifier_report_use
+ _tcc_authorization_record_get_eligible_for_reprompt
+ _tcc_authorization_record_set_eligible_for_reprompt
+ _tcc_message_options_set_attributed_bundle_identifier
+ tcc_message_options_encode_to_dictionary
CStrings:
+ "%s: error creating a UTF-8 string from the attributed bundle identifier, reporting use unattributed"
+ "%{public}s Requesting icon identifier for %s"
+ "%{public}s: identifier for %{public}s return NULL"
+ "Eligible For Reprompt, "
+ "TCCCopyIconIdentifierForService"
+ "TCCCopyIconIdentifierForService() Sync IPC"
+ "TCCCopyIconIdentifierForService_block_invoke"
+ "TCCCopyIconIdentifierForService_block_invoke_2"
+ "TCCD_MSG_MESSAGE_ELIGIBLE_FOR_REPROMPT"
+ "TCCD_MSG_MESSAGE_OPTION_ATTRIBUTED_BUNDLE_IDENTIFIER_KEY"
+ "iconIdentifier"
+ "tcc_authorization_bundle_identifier_report_use_block_invoke"
```
