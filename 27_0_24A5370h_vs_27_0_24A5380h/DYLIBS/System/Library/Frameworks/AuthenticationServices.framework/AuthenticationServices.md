## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-  __TEXT.__text: 0x143894
-  __TEXT.__objc_methlist: 0x80ec
-  __TEXT.__cstring: 0xb578
+  __TEXT.__text: 0x143f5c
+  __TEXT.__objc_methlist: 0x813c
+  __TEXT.__cstring: 0xb5d8
   __TEXT.__const: 0x13f74
-  __TEXT.__gcc_except_tab: 0x12bc
-  __TEXT.__oslogstring: 0x34eb
+  __TEXT.__gcc_except_tab: 0x12c0
+  __TEXT.__oslogstring: 0x34db
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d36
   __TEXT.__swift5_typeref: 0x328e

   __TEXT.__swift_as_ret: 0x2cc
   __TEXT.__swift_as_cont: 0x508
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__unwind_info: 0x5d90
+  __TEXT.__unwind_info: 0x5db0
   __TEXT.__eh_frame: 0x6edc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a38
+  __DATA_CONST.__const: 0x1a60
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ce8
+  __DATA_CONST.__objc_selrefs: 0x4d18
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x10a8
+  __DATA_CONST.__got: 0x10b0
   __AUTH_CONST.__const: 0x9bf8
-  __AUTH_CONST.__cfstring: 0x4580
-  __AUTH_CONST.__objc_const: 0x10370
+  __AUTH_CONST.__cfstring: 0x45c0
+  __AUTH_CONST.__objc_const: 0x10390
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x16d0
-  __AUTH.__objc_data: 0x3d08
-  __AUTH.__data: 0x18f0
-  __DATA.__objc_ivar: 0x700
-  __DATA.__data: 0x3940
+  __AUTH.__objc_data: 0x3ac8
+  __AUTH.__data: 0x18d0
+  __DATA.__objc_ivar: 0x704
+  __DATA.__data: 0x39a0
   __DATA.__bss: 0x12530
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x510
+  __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8196
-  Symbols:   12283
-  CStrings:  1794
+  Functions: 8210
+  Symbols:   12312
+  CStrings:  1798
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ -[ASCredentialRequestButton accessibilityLabel]
+ -[ASCredentialRequestButton accessibilityTraits]
+ -[ASCredentialRequestButton isAccessibilityElement]
+ -[ASCredentialRequestConfirmButtonSubPane _evaluatePolicy:reason:reply:]
+ -[ASCredentialRequestConfirmButtonSubPane _performBiometricValidationAllowingPasscodeFallback:reply:]
+ -[ASCredentialRequestConfirmButtonSubPane _shouldUseInlineBiometricsView]
+ _OBJC_IVAR_$_ASCredentialRequestConfirmButtonSubPane._selectedLoginChoice
+ _UIAccessibilityTraitNotEnabled
+ ___72-[ASCredentialRequestConfirmButtonSubPane _evaluatePolicy:reason:reply:]_block_invoke
+ ___72-[ASCredentialRequestConfirmButtonSubPane _evaluatePolicy:reason:reply:]_block_invoke_2
+ ___75-[ASCredentialRequestConfirmButtonSubPane _authorizationButtonBioSelected:]_block_invoke
+ ___75-[ASCredentialRequestConfirmButtonSubPane _authorizationButtonBioSelected:]_block_invoke_2
+ ___86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2
+ ___block_descriptor_41_e8_32s_e22_v20?0B8"LAContext"12ls32l8
+ _objc_msgSend$_evaluatePolicy:reason:reply:
+ _objc_msgSend$_performBiometricValidationAllowingPasscodeFallback:reply:
+ _objc_msgSend$_shouldUseInlineBiometricsView
+ _objc_msgSend$passkeyHeaderWithTitle:subtitle:
+ _objc_msgSend$setFastAnimations:
+ _objc_msgSend$shouldCurrentProcessShowPasswordManagerServiceNames
+ _visibilityForLoginChoiceKind
- GCC_except_table31
- GCC_except_table33
- ___71-[ASCredentialRequestConfirmButtonSubPane _performCompanionValidation:]_block_invoke
- ___71-[ASCredentialRequestConfirmButtonSubPane _performCompanionValidation:]_block_invoke_2
CStrings:
+ "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2"
+ "An export is currently in progress. Please try again in a few minutes."
+ "Authentication in ASAuthorizationController credential picker failed with error: %{public}@"
+ "Export in progress"
+ "\xf1"
- "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke"
- "Companion authentication in ASAuthorizationController credential picker failed with error: %{public}@"
- "\xe1"

```
