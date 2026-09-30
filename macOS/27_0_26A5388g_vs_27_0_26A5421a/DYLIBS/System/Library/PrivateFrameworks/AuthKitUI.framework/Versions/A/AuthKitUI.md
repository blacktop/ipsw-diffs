## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x1168f0
-  __TEXT.__objc_methlist: 0xc060
+559.0.0.0.0
+  __TEXT.__text: 0x1191e8
+  __TEXT.__objc_methlist: 0xc150
   __TEXT.__const: 0x11a4
-  __TEXT.__cstring: 0x68bb
-  __TEXT.__oslogstring: 0x5dd9
-  __TEXT.__gcc_except_tab: 0xc0c
+  __TEXT.__cstring: 0x690b
+  __TEXT.__oslogstring: 0x5f19
+  __TEXT.__gcc_except_tab: 0xc9c
   __TEXT.__dlopen_cstrs: 0x1d1
   __TEXT.__ustring: 0x28
   __TEXT.__constg_swiftt: 0x4ac

   __TEXT.__swift_as_entry: 0x80
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__unwind_info: 0x2998
+  __TEXT.__unwind_info: 0x2a10
   __TEXT.__eh_frame: 0x10f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7180
+  __DATA_CONST.__objc_selrefs: 0x7230
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0xed0
-  __AUTH_CONST.__const: 0x1fe0
-  __AUTH_CONST.__cfstring: 0x56e0
-  __AUTH_CONST.__objc_const: 0x1e800
+  __AUTH_CONST.__const: 0x2040
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x1e908
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0xdc8
   __AUTH.__objc_data: 0x2c00
   __AUTH.__data: 0x4b8
-  __DATA.__objc_ivar: 0xd80
+  __DATA.__objc_ivar: 0xd90
   __DATA.__data: 0x25c0
   __DATA.__bss: 0x1548
   __DATA.__common: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4549
-  Symbols:   10581
-  CStrings:  1450
+  Functions: 4579
+  Symbols:   10643
+  CStrings:  1459
 
Symbols:
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _OBKitDrainPendingHandlerWithPassword:error:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _OBKitLoginCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _cancelPendingPasswordHandler]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _handlePresentLoginAlertMappedError:completion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _presentOBKitBasicLoginUIWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitCancelActionWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitCreateActionWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitEscapeOffersWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitForgotActionWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext _showLoginAlertAndResetVCsWithTitle:message:completion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext context:needsPasswordWithCompletion:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext pendingPasswordHandler]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext setPendingPasswordHandler:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext setSignInCancelHandler:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext setSignInViewController:]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext signInCancelHandler]
+ -[AKAppleIDAuthenticationiCloudPrefPaneContext signInViewController]
+ -[AKModalSignInViewController disablePasswordAutoFill]
+ -[AKModalSignInViewController setDisablePasswordAutoFill:]
+ -[AKPrivateEmailViewController _presentServerUIWithLoadDelegate:urlConfiguration:error:]
+ GCC_except_table30
+ GCC_except_table42
+ GCC_except_table72
+ OBJC_IVAR_$_AKAppleIDAuthenticationiCloudPrefPaneContext._pendingPasswordHandler
+ OBJC_IVAR_$_AKAppleIDAuthenticationiCloudPrefPaneContext._signInCancelHandler
+ OBJC_IVAR_$_AKAppleIDAuthenticationiCloudPrefPaneContext._signInViewController
+ OBJC_IVAR_$_AKModalSignInViewController._disablePasswordAutoFill
+ __52-[AKPrivateEmailViewController _runPrivateEmailFlow]_block_invoke
+ ___70-[AKAppleIDAuthenticationiCloudPrefPaneContext _OBKitLoginCompletion:]_block_invoke
+ ___84-[AKAppleIDAuthenticationiCloudPrefPaneContext context:needsPasswordWithCompletion:]_block_invoke
+ ___86-[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitCancelActionWithCompletion:]_block_invoke
+ ___86-[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitCreateActionWithCompletion:]_block_invoke
+ ___86-[AKAppleIDAuthenticationiCloudPrefPaneContext _setupOBKitForgotActionWithCompletion:]_block_invoke
+ ___86-[AKAppleIDAuthenticationiCloudPrefPaneContext dismissServerProvidedUIWithCompletion:]_block_invoke_2
+ ___88-[AKAppleIDAuthenticationiCloudPrefPaneContext _presentOBKitBasicLoginUIWithCompletion:]_block_invoke
+ ___88-[AKPrivateEmailViewController _presentServerUIWithLoadDelegate:urlConfiguration:error:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e40_v24?0"AKURLConfiguration"8"NSError"16l
+ ___block_descriptor_56_e8_32bs40r48w_e59_v44?0"NSString"8"NSString"16"NSNumber"24B32"NSError"36l
+ ___copy_helper_block_e8_32b40r48w
+ ___destroy_helper_block_e8_32s40r48w
+ _objc_msgSend$_OBKitDrainPendingHandlerWithPassword:error:
+ _objc_msgSend$_OBKitLoginCompletion:
+ _objc_msgSend$_cancelPendingPasswordHandler
+ _objc_msgSend$_handlePresentLoginAlertMappedError:completion:
+ _objc_msgSend$_presentOBKitBasicLoginUIWithCompletion:
+ _objc_msgSend$_presentServerUIWithLoadDelegate:urlConfiguration:error:
+ _objc_msgSend$_setupOBKitCancelActionWithCompletion:
+ _objc_msgSend$_setupOBKitCreateActionWithCompletion:
+ _objc_msgSend$_setupOBKitEscapeOffersWithCompletion:
+ _objc_msgSend$_setupOBKitForgotActionWithCompletion:
+ _objc_msgSend$_showLoginAlertAndResetVCsWithTitle:message:completion:
+ _objc_msgSend$isFeatureEnabled:
+ _objc_msgSend$pendingPasswordHandler
+ _objc_msgSend$setHideCreateButton:
+ _objc_msgSend$setIsPasswordEditable:
+ _objc_msgSend$setPendingPasswordHandler:
+ _objc_msgSend$setSharingType:
+ _objc_msgSend$setSignInCancelHandler:
+ _objc_msgSend$setSignInViewController:
+ _objc_msgSend$setTitleText:
+ _objc_msgSend$setUrlConfiguration:
+ _objc_msgSend$signInCancelHandler
+ _objc_msgSend$signInViewController
+ _objc_msgSend$url
+ _objc_msgSend$urlConfigurationForKey:fromCache:completion:
- GCC_except_table55
- ___52-[AKPrivateEmailViewController _runPrivateEmailFlow]_block_invoke_2
- _objc_msgSend$urlAtKey:
CStrings:
+ "APPLE_ID_REBRAND"
+ "Both OBKit and legacy sign-in VCs are nil; skipping switch on 2FA dismiss."
+ "Completion on basic login UI instance. Create requested"
+ "Completion on basic login UI instance. Forgot requested"
+ "Login Alert called: error %@"
+ "Nil LoadDelegate for key=%@, error=%@"
+ "No URL for key=%@, cannot present HME UI. error=%@"
+ "Presenting OBKit basic login UI."
+ "Superseding pending password handler with user-canceled."
+ "appleAccountLogoBlue"
+ "v24@?0@\"AKURLConfiguration\"8@\"NSError\"16"
- "Login  Alert called: error %@ "
- "Nil LoadDelegate for cfg:%@,\nurl=%@,\nkey=%@"
```
