## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-525.250.5.0.0
-  __TEXT.__text: 0xc5288
+525.250.9.0.0
+  __TEXT.__text: 0xc591c
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x832c
-  __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x13d0
+  __TEXT.__objc_methlist: 0x8334
+  __TEXT.__const: 0x266
+  __TEXT.__gcc_except_tab: 0x14a8
   __TEXT.__cstring: 0x50e8
-  __TEXT.__oslogstring: 0x4b7d
+  __TEXT.__oslogstring: 0x4c38
   __TEXT.__dlopen_cstrs: 0x163
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xac

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1520
+  __TEXT.__unwind_info: 0x1530
   __TEXT.__objc_classname: 0x1532
-  __TEXT.__objc_methname: 0x174e7
+  __TEXT.__objc_methname: 0x175f6
   __TEXT.__objc_methtype: 0x47df
-  __TEXT.__objc_stubs: 0x12200
-  __DATA_CONST.__got: 0xcb0
-  __DATA_CONST.__const: 0x24d0
+  __TEXT.__objc_stubs: 0x12320
+  __DATA_CONST.__got: 0xcd8
+  __DATA_CONST.__const: 0x24d8
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5be0
+  __DATA_CONST.__objc_selrefs: 0x5c28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x4e20
+  __AUTH_CONST.__cfstring: 0x4e40
   __AUTH_CONST.__objc_const: 0x17148
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E42B9E35-909A-390F-A7B4-EE450CC7CE36
-  Functions: 2711
-  Symbols:   11039
-  CStrings:  6156
+  UUID: AB0230D0-4289-3985-8A18-CF0749165834
+  Functions: 2712
+  Symbols:   11055
+  CStrings:  6171
 
Symbols:
+ -[AKAppleIDFollowUpServerUIPresenter _authContextForPresentationUsingHelper:]
+ -[AKAppleIDFollowUpServerUIPresenter _presentServerUIUsingContext:withCompletion:]
+ -[AKInAppAuthenticationRemoteUIDelegate _addPrivacyConsentVersionToRequest:context:]
+ GCC_except_table31
+ _AKAppleAccountConsentShownKey
+ _AKAppleAccountConsentVersionKey
+ _AKAppleIDAuthenticationAppProvidedContextSimpleProfile
+ _OBJC_CLASS_$_OBBundle
+ _OBJC_CLASS_$_OBPrivacyFlow
+ ___52-[AKInAppAuthenticationRemoteUIDelegate _showAlert:]_block_invoke.85
+ ___82-[AKAppleIDFollowUpServerUIPresenter _presentServerUIUsingContext:withCompletion:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48w_e27_v24?0"NSURL"8"NSError"16lw48l8s40l8s32l8
+ _kAppleIDPrivacyConsentBundleID
+ _objc_msgSend$_addPrivacyConsentVersionToRequest:context:
+ _objc_msgSend$_authContextForPresentationUsingHelper:
+ _objc_msgSend$_presentServerUIUsingContext:withCompletion:
+ _objc_msgSend$_shouldSendSigningHeadersForServerUI
+ _objc_msgSend$addValue:forHTTPHeaderField:
+ _objc_msgSend$contentVersion
+ _objc_msgSend$flowWithBundle:
+ _objc_msgSend$isPrivacyVersionSavingEnabled
+ _objc_msgSend$setAppProvidedContext:
+ _objc_msgSend$setServiceType:
+ _objc_msgSend$set_shouldSendSigningHeadersForServerUI:
- -[AKAppleIDFollowUpServerUIPresenter _authContextWithAltDSID:account:]
- -[AKAppleIDFollowUpServerUIPresenter _presentServerUIWithCompletion:]
- _AAUISignOutErrorDomain
- ___52-[AKInAppAuthenticationRemoteUIDelegate _showAlert:]_block_invoke.82
- ___69-[AKAppleIDFollowUpServerUIPresenter _presentServerUIWithCompletion:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56bs64w_e27_v24?0"NSURL"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
- _objc_msgSend$_authContextWithAltDSID:account:
- _objc_msgSend$_presentServerUIWithCompletion:
CStrings:
+ "%lu"
+ "Added privacy consent version header: %@"
+ "Exception during privacy consent version detection: %@"
+ "Failed to create OBBundle for identifier: %@"
+ "Failed to create OBPrivacyFlow for bundle: %@"
+ "_addPrivacyConsentVersionToRequest:context:"
+ "_authContextForPresentationUsingHelper:"
+ "_presentServerUIUsingContext:withCompletion:"
+ "_shouldSendSigningHeadersForServerUI"
+ "addValue:forHTTPHeaderField:"
+ "contentVersion"
+ "flowWithBundle:"
+ "isPrivacyVersionSavingEnabled"
+ "setAppProvidedContext:"
+ "setServiceType:"
+ "set_shouldSendSigningHeadersForServerUI:"
- "_authContextWithAltDSID:account:"
- "_presentServerUIWithCompletion:"

```
