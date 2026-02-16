## FamilyControlsObjC

> `/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC`

```diff

-1223.80.2.0.0
-  __TEXT.__text: 0x2500
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x2b0
+1223.100.11.0.0
+  __TEXT.__text: 0x2a18
+  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x2e0
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__gcc_except_tab: 0x48
   __TEXT.__cstring: 0x12e
-  __TEXT.__oslogstring: 0x278
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__oslogstring: 0x340
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_classname: 0xa1
-  __TEXT.__objc_methname: 0x942
+  __TEXT.__objc_methname: 0xa6f
   __TEXT.__objc_methtype: 0x18a
-  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x6e0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x250
+  __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x548
+  __AUTH_CONST.__objc_const: 0x558
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78809F36-F367-38ED-A584-187B9F0E900F
-  Functions: 69
-  Symbols:   344
-  CStrings:  159
+  UUID: F244D1F3-1EFB-3F16-B681-12BCCD9486FB
+  Functions: 80
+  Symbols:   366
+  CStrings:  165
 
Symbols:
+ -[FOAuthorizationCenter requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:]
+ -[FOAuthorizationCenter requestDataAccessAuthorizationForRecordIdentifier:completionHandler:]
+ _OUTLINED_FUNCTION_5
+ ___110-[FOAuthorizationCenter requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:]_block_invoke
+ ___110-[FOAuthorizationCenter requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:]_block_invoke.cold.1
+ ___110-[FOAuthorizationCenter requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:]_block_invoke_2
+ ___110-[FOAuthorizationCenter requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:]_block_invoke_2.cold.1
+ ___93-[FOAuthorizationCenter requestDataAccessAuthorizationForRecordIdentifier:completionHandler:]_block_invoke
+ ___93-[FOAuthorizationCenter requestDataAccessAuthorizationForRecordIdentifier:completionHandler:]_block_invoke.cold.1
+ ___93-[FOAuthorizationCenter requestDataAccessAuthorizationForRecordIdentifier:completionHandler:]_block_invoke_2
+ ___93-[FOAuthorizationCenter requestDataAccessAuthorizationForRecordIdentifier:completionHandler:]_block_invoke_2.cold.1
+ _objc_msgSend$requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:replyHandler:
+ _objc_msgSend$requestDataAccessAuthorizationWithRecordIdentifier:replyHandler:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "Failed to request approval to replace third party data access authorization with error: %{public}@"
+ "Failed to request data access authorization for record identifier: %{public}@ with error: %{public}@"
+ "requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:completionHandler:"
+ "requestApprovalToReplaceThirdPartyDataAccessAuthorizationForMember:replyHandler:"
+ "requestDataAccessAuthorizationForRecordIdentifier:completionHandler:"
+ "requestDataAccessAuthorizationWithRecordIdentifier:replyHandler:"

```
