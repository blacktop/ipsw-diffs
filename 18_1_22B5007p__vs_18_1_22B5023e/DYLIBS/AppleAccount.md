## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1002.0.0.0.0
-  __TEXT.__text: 0xbe360
+1005.0.0.0.0
+  __TEXT.__text: 0xbee68
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x8f94
+  __TEXT.__objc_methlist: 0x8ff4
   __TEXT.__const: 0x1b00
-  __TEXT.__cstring: 0xbb57
-  __TEXT.__oslogstring: 0xd819
-  __TEXT.__gcc_except_tab: 0x2170
+  __TEXT.__cstring: 0xbc95
+  __TEXT.__oslogstring: 0xd8ba
+  __TEXT.__gcc_except_tab: 0x219c
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__unwind_info: 0x24f8
-  __TEXT.__objc_classname: 0x1c3c
-  __TEXT.__objc_methname: 0x1349b
-  __TEXT.__objc_methtype: 0x29c7
-  __TEXT.__objc_stubs: 0xada0
-  __DATA_CONST.__got: 0xbf8
-  __DATA_CONST.__const: 0x30c8
-  __DATA_CONST.__objc_classlist: 0x738
+  __TEXT.__unwind_info: 0x2508
+  __TEXT.__objc_classname: 0x1c59
+  __TEXT.__objc_methname: 0x13607
+  __TEXT.__objc_methtype: 0x29f0
+  __TEXT.__objc_stubs: 0xae60
+  __DATA_CONST.__got: 0xc00
+  __DATA_CONST.__const: 0x3168
+  __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4498
+  __DATA_CONST.__objc_selrefs: 0x44d8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4f00
-  __AUTH_CONST.__cfstring: 0xb080
-  __AUTH_CONST.__objc_const: 0x21028
+  __AUTH_CONST.__cfstring: 0xb180
+  __AUTH_CONST.__objc_const: 0x21100
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xaf4
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xaf8
   __DATA.__data: 0x12a0
-  __DATA.__bss: 0x370
+  __DATA.__bss: 0x358
   __DATA.__common: 0x69
-  __DATA_DIRTY.__objc_data: 0x4600
+  __DATA_DIRTY.__objc_data: 0x4740
   __DATA_DIRTY.__data: 0x60
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__bss: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3873
-  Symbols:   5440
-  CStrings:  6483
+  Functions: 3882
+  Symbols:   5455
+  CStrings:  6510
 
Symbols:
+ _AAOBBeneficiaryIconName
+ _OBJC_CLASS_$_AAAuthenticationErrorHandler
+ _OBJC_METACLASS_$_AAAuthenticationErrorHandler
+ __AAUrlBagInheritanceConfigKey
+ __AAUrlBagLCInviteAcceptanceKey
+ _kAAProfilePictureCacheURL
CStrings:
+ "@40@0:8@16Q24Q32"
+ "AAAuthenticationErrorHandler"
+ "AADataclassManager failed to maintain ref to self."
+ "AAProfilePictureCacheURL"
+ "Account save with dataclass actions had success (%!@(MISSING)) for account (%!@(MISSING)) with dataclass actions: %!@(MISSING)"
+ "BENEFICIARY_ACCEPTED_INVITE_DETAIL_TEXT"
+ "BENEFICIARY_ACCEPTED_INVITE_TITLE"
+ "Encountered error when saving with dataclass actions: %!@(MISSING)"
+ "INHERITANCE_ADDED_MESSAGES_BUBBLE_BODY"
+ "INHERITANCE_ADDED_MESSAGES_BUBBLE_TITLE"
+ "INHERITANCE_ADDED_MESSAGE_DETAIL_TEXT"
+ "INHERITANCE_INVITED_MESSAGES_BUBBLE_BODY"
+ "INHERITANCE_INVITED_MESSAGES_BUBBLE_TITLE"
+ "INHERITANCE_INVITED_MESSAGE_DETAIL_TEXT"
+ "INHERITANCE_INVITE_COMPLETE_MESSAGE_AFTER_MESSAGING"
+ "INHERITANCE_INVITE_COMPLETE_TITLE"
+ "LCInvite: No IdMS feature flag found. is OS FeatureFlag Enabled %!d(MISSING)"
+ "LCInvite: Returning LCInviteAcceptance from urlbag: %!@(MISSING)"
+ "LCInvite: inheritanceCfgs from urlbag: %!@(MISSING)"
+ "LCInviteAcceptance"
+ "PreflightSave completed retry."
+ "PreflightSave failed with recoverable / xpc error, retrying once..."
+ "T@\"ACAccountStore\",&,N,V_store"
+ "T@\"NSString\",R,N,V_profilePictureCacheURL"
+ "Unable to build list of dataclasses and actions for enablement %!@(MISSING)"
+ "_buildAutoEnableableDataclassesAndActionsForAccount:dataclassesForEnablement:completion:"
+ "_preflightSaveWithAuthResults:account:withCompletion:"
+ "_profilePictureCacheURL"
+ "ak_isUserCancelError"
+ "handleAuthenticationError:resetAuthenticatedOnAlertFailure:forAccount:inStore:completion:"
+ "initWithAcceptedViewForBenefactorInfo:"
+ "initWithBenefactorInfo:"
+ "initWithBeneficiaryName:accessKeyShareType:inviteType:"
+ "inviteAcceptance"
+ "isLCInviteAcceptanceEnabled"
+ "isRCUpsellEnabled"
+ "legacy_contact_header"
+ "profilePictureCacheURL"
+ "provisioningResponse"
+ "saveAccount:withHandler:"
+ "setStore:"
+ "store"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v52@0:8@16B24@28@36@?44"
- "Failed to enable dataclasses for account %!@(MISSING) with error %!@(MISSING)"
- "Failed to save account with dataclasses enabled, error: %!@(MISSING)"
- "INHERITANCE_INVITE_MESSAGE_BUBBLE"
- "INHERITANCE_INVITE_MESSAGE_DETAIL_TEXT"
- "INHERITANCE_MESSAGES_BUBBLE_INVITE_BODY"
- "INHERITANCE_MESSAGES_BUBBLE_INVITE_BODY_NO_NAME"
- "INHERITANCE_MESSAGES_BUBBLE_TITLE"
- "Successfully enabled dataclasses for account (%!@(MISSING)) with dataclass actions: %!@(MISSING)"
- "Successfully enabled datclasses for account %!@(MISSING)"
- "Unable to build list of dataclasses and actions for enablement."
- "XPC call to urlConfigurationWithCompletion failed due to error: %!@(MISSING)."
- "_buildAutoEnableableDataclassesAndActionsForAccount:dataclassesForEnablement:"
- "_messageForContact:"
- "initWithBenefactorFullName:firstName:handle:benefactorInfo:"
- "initWithBenefactorHandle:"
- "initWithBenefactorName:handle:"

```
