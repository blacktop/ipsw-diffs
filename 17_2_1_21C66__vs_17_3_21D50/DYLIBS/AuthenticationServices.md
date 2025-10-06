## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-617.1.17.10.9
-  __TEXT.__text: 0x54fe4
+617.2.4.10.7
+  __TEXT.__text: 0x55678
   __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x5528
-  __TEXT.__cstring: 0x49f6
+  __TEXT.__objc_methlist: 0x5548
+  __TEXT.__cstring: 0x4a96
   __TEXT.__const: 0x714
   __TEXT.__oslogstring: 0x22ec
-  __TEXT.__ustring: 0x7884
+  __TEXT.__ustring: 0x78ca
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__constg_swiftt: 0x1bc

   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1c68
+  __TEXT.__unwind_info: 0x1c84
   __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_classname: 0x1c25
-  __TEXT.__objc_methname: 0x145ff
+  __TEXT.__objc_methname: 0x1474b
   __TEXT.__objc_methtype: 0x42c4
-  __TEXT.__objc_stubs: 0xd860
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x1560
+  __TEXT.__objc_stubs: 0xd940
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xafe0
-  __DATA_CONST.__objc_selrefs: 0x4068
+  __DATA_CONST.__objc_const: 0xb000
+  __DATA_CONST.__objc_selrefs: 0x40a0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x4020
+  __AUTH_CONST.__cfstring: 0x4100
   __AUTH_CONST.__objc_const: 0x3050
   __AUTH_CONST.__const: 0x13b8
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x7c8
   __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x840
+  __DATA.__objc_classrefs: 0x848
   __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x670
+  __DATA.__objc_ivar: 0x674
   __DATA.__data: 0x15e8
   __DATA.__bss: 0x6c0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22057062-B708-37B1-8A3C-47A201B1975F
-  Functions: 2489
-  Symbols:   8727
-  CStrings:  4491
+  UUID: 9A723BF8-F383-3BD2-A8D2-C9726FB5A497
+  Functions: 2496
+  Symbols:   8752
+  CStrings:  4511
 
Symbols:
+ -[ASCredentialPickerPaneViewController _messageOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed]
+ -[ASCredentialPickerPaneViewController _titleOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed]
+ -[ASCredentialRequestConfirmButtonSubPane _shouldAllowFallbackToPasscodeAuthentication]
+ GCC_except_table79
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_IVAR_$_ASCredentialPickerPaneViewController._numberOfFailedBiometryAttempts
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke.315
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke_2
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke_3
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke_4
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.293
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.294
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.301
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.301.cold.1
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.303
+ ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.103
+ ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.95
+ ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.330
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.82
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.85
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.85.cold.1
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_literal_global.100
+ ___block_literal_global.105
+ ___block_literal_global.136
+ ___block_literal_global.145
+ ___block_literal_global.168
+ ___block_literal_global.200
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.296
+ ___block_literal_global.300
+ ___block_literal_global.314
+ ___block_literal_global.329
+ ___block_literal_global.334
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.54
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.98
+ _objc_msgSend$_messageOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed
+ _objc_msgSend$_shouldAllowFallbackToPasscodeAuthentication
+ _objc_msgSend$_titleOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed
+ _objc_msgSend$evaluatePolicy:options:error:
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$setPreferredAction:
+ _objc_msgSend$sharedApplication
- GCC_except_table77
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.278
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.279
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.286
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.286.cold.1
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.288
- ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.100
- ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.92
- ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.302
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.78
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.81
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.81.cold.1
- ___block_literal_global.133
- ___block_literal_global.142
- ___block_literal_global.165
- ___block_literal_global.197
- ___block_literal_global.274
- ___block_literal_global.277
- ___block_literal_global.281
- ___block_literal_global.285
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.51
- ___block_literal_global.90
- ___block_literal_global.95
CStrings:
+ "Learn More"
+ "Passcode Not Allowed"
+ "Stolen Device Protection is active."
+ "Stolen Device Protection is enabled and biometry is required."
+ "_messageOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed"
+ "_numberOfFailedBiometryAttempts"
+ "_shouldAllowFallbackToPasscodeAuthentication"
+ "_titleOfAlertForFailedBiometryAttemptWhenPasscodeFallbackIsNotAllowed"
+ "evaluatePolicy:options:error:"
+ "https://support.apple.com/en-us/HT212510"
+ "openURL:options:completionHandler:"
+ "setPreferredAction:"
+ "sharedApplication"

```
