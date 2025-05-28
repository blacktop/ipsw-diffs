## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x54d68
+617.1.17.10.9
+  __TEXT.__text: 0x54fe4
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_methlist: 0x5528
-  __TEXT.__cstring: 0x4996
+  __TEXT.__cstring: 0x49f6
   __TEXT.__const: 0x714
   __TEXT.__oslogstring: 0x22ec
-  __TEXT.__ustring: 0x765a
+  __TEXT.__ustring: 0x7884
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__swift5_typeref: 0x1b4
   __TEXT.__constg_swiftt: 0x1bc
+  __TEXT.__swift5_typeref: 0x1b4
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x108
   __TEXT.__swift5_fieldmd: 0x1d8
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__unwind_info: 0x1c68
   __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_classname: 0x1c25
-  __TEXT.__objc_methname: 0x145af
-  __TEXT.__objc_methtype: 0x4263
-  __TEXT.__objc_stubs: 0xd840
+  __TEXT.__objc_methname: 0x145ff
+  __TEXT.__objc_methtype: 0x42c4
+  __TEXT.__objc_stubs: 0xd860
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x1550
+  __DATA_CONST.__const: 0x1560
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xafe0
-  __DATA_CONST.__objc_selrefs: 0x4060
+  __DATA_CONST.__objc_selrefs: 0x4068
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__cfstring: 0x4020
   __AUTH_CONST.__objc_const: 0x3050
-  __AUTH_CONST.__const: 0x1360
+  __AUTH_CONST.__const: 0x13b8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2486
-  Symbols:   8719
-  CStrings:  3972
+  Functions: 2489
+  Symbols:   8727
+  CStrings:  3978
 
Symbols:
+ +[ASCredentialRequestIconGenerator _iconForPresentationContext:size:outIconStyle:]
+ -[ASAuthorizationViewController _shouldPresentCABLEAsInitialViewControllerForRequestTypes:shouldAllowSecurityKeysFromCABLEView:]
+ -[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]
+ GCC_except_table77
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.278
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.279
+ ___107-[ASCredentialPickerPaneViewController initWithPresentationContext:shouldExpandOtherLoginChoices:activity:]_block_invoke_2
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.286
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.286.cold.1
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.288
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.101
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.103
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.26.cold.1
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.27
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.29
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.37
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.30
+ ___57-[ASAuthorizationViewController _startCABLEAuthenticator]_block_invoke.81
+ ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.100
+ ___65-[ASAuthorizationViewController updateInterfaceWithLoginChoices:]_block_invoke_2
+ ___65-[ASAuthorizationViewController updateInterfaceWithLoginChoices:]_block_invoke_2.cold.1
+ ___66-[ASAuthorizationViewController _startCABLEClientWithLoginChoice:]_block_invoke.60
+ ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.92
+ ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.302
+ ___block_literal_global.133
+ ___block_literal_global.142
+ ___block_literal_global.165
+ ___block_literal_global.197
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.293
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.31
+ ___block_literal_global.315
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.41
+ ___block_literal_global.51
+ ___block_literal_global.57
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.84
+ ___block_literal_global.88
+ ___block_literal_global.95
+ ___block_literal_global.99
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AuthenticationServices
+ __swift_FORCE_LOAD_$_swiftWebKit
+ __swift_FORCE_LOAD_$_swiftWebKit_$_AuthenticationServices
+ _objc_msgSend$_iconForPresentationContext:size:outIconStyle:
+ _objc_msgSend$_shouldPresentCABLEAsInitialViewControllerForRequestTypes:shouldAllowSecurityKeysFromCABLEView:
+ _objc_msgSend$confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:
+ _objc_msgSend$serviceType
- +[ASCredentialRequestIconGenerator _iconForPresentationContext:size:]
- -[ASAuthorizationViewController _shouldPresentCABLEAsInitialViewControllerForPresentationContext:]
- -[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:]
- GCC_except_table76
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.246
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.247
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.254
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.254.cold.1
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.256
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.100
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.98
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.23
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.23.cold.1
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.24
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.31
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.27
- ___57-[ASAuthorizationViewController _startCABLEAuthenticator]_block_invoke.82
- ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.95
- ___65-[ASAuthorizationViewController updateInterfaceWithLoginChoices:]_block_invoke.4.cold.1
- ___65-[ASAuthorizationViewController updateInterfaceWithLoginChoices:]_block_invoke.7
- ___66-[ASAuthorizationViewController _startCABLEClientWithLoginChoice:]_block_invoke.61
- ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.87
- ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.270
- ___76-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:]_block_invoke
- ___block_literal_global.116
- ___block_literal_global.125
- ___block_literal_global.148
- ___block_literal_global.183
- ___block_literal_global.22
- ___block_literal_global.242
- ___block_literal_global.245
- ___block_literal_global.249
- ___block_literal_global.253
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.276
- ___block_literal_global.283
- ___block_literal_global.287
- ___block_literal_global.29
- ___block_literal_global.290
- ___block_literal_global.33
- ___block_literal_global.42
- ___block_literal_global.46
- ___block_literal_global.54
- ___block_literal_global.64
- ___block_literal_global.66
- ___block_literal_global.69
- ___block_literal_global.77
- ___block_literal_global.81
- ___block_literal_global.94
- ___block_literal_global.96
- _objc_msgSend$_iconForPresentationContext:size:
- _objc_msgSend$_shouldPresentCABLEAsInitialViewControllerForPresentationContext:
- _objc_msgSend$confirmButtonSubPaneDidFailBiometry:
CStrings:
+ "@48@0:8@16{CGSize=dd}24^q40"
+ "B28@0:8Q16B24"
+ "Choose an account to sign in to (app name)"
+ "Choose an account to sign in to (website)"
+ "_iconForPresentationContext:size:outIconStyle:"
+ "_shouldPresentCABLEAsInitialViewControllerForRequestTypes:shouldAllowSecurityKeysFromCABLEView:"
+ "confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:"
+ "serviceType"
+ "v28@0:8@\"ASCredentialRequestConfirmButtonSubPane\"16B24"
- "_iconForPresentationContext:size:"
- "_shouldPresentCABLEAsInitialViewControllerForPresentationContext:"
- "confirmButtonSubPaneDidFailBiometry:"

```
