## RemotePaymentPassActionsMessagesExtension

> `/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1353.0.0.0.0
-  __TEXT.__text: 0x8974
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x8d8
-  __TEXT.__const: 0x58
+1354.0.0.0.0
+  __TEXT.__text: 0x92d0
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0x8f0
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x7bd
-  __TEXT.__objc_methname: 0x2903
-  __TEXT.__oslogstring: 0x10a9
+  __TEXT.__cstring: 0x815
+  __TEXT.__objc_methname: 0x2a32
+  __TEXT.__oslogstring: 0x1315
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0xdd6
-  __TEXT.__unwind_info: 0x2a0
-  __DATA_CONST.__const: 0x390
+  __TEXT.__unwind_info: 0x2c0
+  __DATA_CONST.__const: 0x480
   __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x278
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x218
   __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0xaa8
+  __DATA.__objc_selrefs: 0xb10
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/Messages.framework/Messages
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit
   - /System/Library/PrivateFrameworks/NanoPassKitUI.framework/NanoPassKitUI
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 148
-  Symbols:   166
-  CStrings:  593
+  Functions: 156
+  Symbols:   172
+  CStrings:  614
 
Symbols:
+ _NPKPreferencesGetValue
+ _NPKRemotePassActionSkipFamilyCircleVerification
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _PKOSVariantSubsystem
+ _dispatch_get_global_queue
+ _os_variant_has_internal_ui
CStrings:
+ "B16@?0@\"FAFamilyMember\"8"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "Error: NPKRemotePassActionCompanionConversationManager: Failed to fetch family circle to verify sender: %@"
+ "Error: NPKRemotePassActionCompanionConversationManager: Unable to resolve a handle for the conversation; refusing to treat sender as a family member."
+ "Error: Refusing to present a payment sheet: sender is not a verified member of the family circle!"
+ "Notice: NPKRemotePassActionCompanionConversationManager: Skipping Family Circle verification due to internal-only debug override."
+ "Notice: NPKRemotePassActionCompanionConversationManager: Verified family circle membership for handle: %{private}@, isFamilyMember: %d"
+ "_shouldSkipFamilyCircleVerification"
+ "appleID"
+ "appleIDAliases"
+ "boolValue"
+ "caseInsensitiveCompare:"
+ "indexOfObjectPassingTest:"
+ "memberForPhoneNumber:"
+ "members"
+ "npkIsPhoneNumber"
+ "pk_containsObjectPassingTest:"
+ "setCachePolicy:"
+ "startRequestWithCompletionHandler:"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
+ "verifyFamilyCircleMembershipForConversation:completion:"
```
