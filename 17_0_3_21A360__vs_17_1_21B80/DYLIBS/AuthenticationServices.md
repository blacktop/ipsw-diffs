## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x547dc
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x54e8
-  __TEXT.__cstring: 0x4966
+616.2.9.10.10
+  __TEXT.__text: 0x54c80
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x5518
+  __TEXT.__cstring: 0x4996
   __TEXT.__const: 0x714
-  __TEXT.__oslogstring: 0x22a0
+  __TEXT.__oslogstring: 0x22ec
   __TEXT.__ustring: 0x765a
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__dlopen_cstrs: 0xad

   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1c44
+  __TEXT.__unwind_info: 0x1c50
   __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_classname: 0x1c25
-  __TEXT.__objc_methname: 0x143af
-  __TEXT.__objc_methtype: 0x41e8
-  __TEXT.__objc_stubs: 0xd6e0
+  __TEXT.__objc_methname: 0x1454f
+  __TEXT.__objc_methtype: 0x4263
+  __TEXT.__objc_stubs: 0xd7e0
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x1530
+  __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xaf60
-  __DATA_CONST.__objc_selrefs: 0x3ff8
+  __DATA_CONST.__objc_const: 0xafc0
+  __DATA_CONST.__objc_selrefs: 0x4048
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__cfstring: 0x3f80
   __AUTH_CONST.__objc_const: 0x3050
-  __AUTH_CONST.__const: 0x1340
+  __AUTH_CONST.__const: 0x1360
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x820
+  __DATA.__objc_classrefs: 0x838
   __DATA.__objc_superrefs: 0x2f8
   __DATA.__objc_ivar: 0x66c
   __DATA.__data: 0x15e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7FF4AD28-80EA-3B3C-866B-347F1C88D6EA
-  Functions: 2477
-  Symbols:   8681
-  CStrings:  4462
+  UUID: A11F021F-822F-319C-A301-196BADCA1B03
+  Functions: 2485
+  Symbols:   8711
+  CStrings:  4476
 
Symbols:
+ -[ASAuthorizationViewController _replaceRequestPaneViewControllerWithExpandedLoginChoiceList:]
+ -[ASAuthorizationViewController requestPaneViewControllerNeedsReload:]
+ -[ASPublicKeyCredentialManager completeAssertionWithExternalPasskeyForUUID:usingCredential:]
+ -[ASPublicKeyCredentialManager getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:]
+ -[_ASAccountSharingGroupMemberDataManager fetchContactForUserHandle:].cold.1
+ _OBJC_CLASS_$_CNEmailAddressUtilities
+ _OBJC_CLASS_$_CNPhoneNumber
+ _OBJC_CLASS_$_WBSPrimaryAppleAccountObserver
+ _WBSKeychainSyncStatusMayHaveChangedNotification
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.100
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.98
+ ___74-[ASCredentialPickerPaneViewController _keychainSyncStatusMayHaveChanged:]_block_invoke
+ ___89-[ASPublicKeyCredentialManager _queryExternalLoginChoicesForOperation:completionHandler:]_block_invoke_3
+ ___block_descriptor_32_e52_"NSString"16?0"ASCPublicKeyCredentialDescriptor"8l
+ ___block_descriptor_49_e8_32s40s_e73_"ASCPlatformPublicKeyCredentialLoginChoice"16?0"SFCredentialIdentity"8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_literal_global.276
+ ___block_literal_global.290
+ ___block_literal_global.77
+ ___block_literal_global.81
+ ___block_literal_global.96
+ _ascCredentialRequestTypesAllPasskey
+ _ascCredentialRequestTypesAllPublicKey
+ _objc_msgSend$_replaceRequestPaneViewControllerWithExpandedLoginChoiceList:
+ _objc_msgSend$isStringEmailAddress:
+ _objc_msgSend$isUsingICloud
+ _objc_msgSend$phoneNumberWithStringValue:
+ _objc_msgSend$predicateForContactsMatchingEmailAddress:
+ _objc_msgSend$predicateForContactsMatchingPhoneNumber:
+ _objc_msgSend$requestPaneViewControllerNeedsReload:
+ _objc_msgSend$setIsExternal:
+ _objc_msgSend$sharedObserver
- _ASKeychainSyncStatusMayHaveChangedNotification
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.95
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.97
- ___UIApplicationLinkedOnOrAfter
- ___block_descriptor_40_e8_32s_e73_"ASCPlatformPublicKeyCredentialLoginChoice"16?0"SFCredentialIdentity"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_literal_global.268
- ___block_literal_global.282
- ___block_literal_global.78
- ___block_literal_global.82
- ___block_literal_global.91
- ___block_literal_global.93
- _objc_msgSend$hasPrimaryAppleAccount
CStrings:
+ "@\"NSString\"16@?0@\"ASCPublicKeyCredentialDescriptor\"8"
+ "Found multiple contacts matching handle %{private}@. Returning first match."
+ "_replaceRequestPaneViewControllerWithExpandedLoginChoiceList:"
+ "completeAssertionWithExternalPasskeyForUUID:usingCredential:"
+ "getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:"
+ "isStringEmailAddress:"
+ "isUsingICloud"
+ "phoneNumberWithStringValue:"
+ "predicateForContactsMatchingEmailAddress:"
+ "predicateForContactsMatchingPhoneNumber:"
+ "requestPaneViewControllerNeedsReload:"
+ "setIsExternal:"
+ "sharedObserver"
+ "v32@0:8@\"NSUUID\"16@\"ASCPlatformPublicKeyCredentialAssertion\"24"
+ "v40@0:8@\"WBSGlobalFrameIdentifier\"16@\"NSString\"24@?<v@?B>32"
- "hasPrimaryAppleAccount"

```
