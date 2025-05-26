## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-466.23.1.1.0
-  __TEXT.__text: 0x5fcf0
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x6124
+466.31.0.0.0
+  __TEXT.__text: 0x61644
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x6274
   __TEXT.__const: 0x2b0
-  __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__cstring: 0x405a
-  __TEXT.__oslogstring: 0x3b0e
+  __TEXT.__gcc_except_tab: 0x808
+  __TEXT.__cstring: 0x414f
+  __TEXT.__oslogstring: 0x3d57
+  __TEXT.__dlopen_cstrs: 0x71
   __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x19fc
-  __TEXT.__objc_classname: 0x12d0
-  __TEXT.__objc_methname: 0x146b8
-  __TEXT.__objc_methtype: 0x3d4d
-  __TEXT.__objc_stubs: 0x10200
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__const: 0x1240
+  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__objc_classname: 0x12f2
+  __TEXT.__objc_methname: 0x14d34
+  __TEXT.__objc_methtype: 0x3f18
+  __TEXT.__objc_stubs: 0x10500
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x12b8
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x14ad8
-  __DATA_CONST.__objc_selrefs: 0x4cb8
+  __DATA_CONST.__objc_const: 0x14d58
+  __DATA_CONST.__objc_selrefs: 0x4da8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x6e8
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__objc_const: 0x22d8
-  __AUTH_CONST.__cfstring: 0x3dc0
+  __AUTH_CONST.__cfstring: 0x3e60
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH.__objc_data: 0x1d10
-  __DATA.__objc_ivar: 0x640
-  __DATA.__data: 0x1468
-  __DATA.__bss: 0x140
+  __DATA.__objc_ivar: 0x668
+  __DATA.__data: 0x14c8
+  __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2563
-  Symbols:   9637
-  CStrings:  4850
+  Functions: 2612
+  Symbols:   9789
+  CStrings:  4930
 
Symbols:
+ -[AKAppleIDFollowUpServerUIPresenter _fetchCurrentFollowUpItem].cold.2
+ -[AKAppleIDFollowUpServerUIPresenter _performClientCompletionWithServerResponse:additionalData:error:]
+ -[AKAppleIDFollowUpServerUIPresenter followUpProvider]
+ -[AKAppleIDFollowUpServerUIPresenter presentServerUIWithContext:withCompletion:withResponse:]
+ -[AKAppleIDFollowUpServerUIPresenter setFollowUpProvider:]
+ -[AKBiometricRatchetUIContext _findMappedDeeplinkFor:withKey:]
+ -[AKBiometricRatchetUIContext _findMappedDeeplinkFor:withKey:].cold.1
+ -[AKBiometricRatchetUIContext embeddedUIPresentationMode]
+ -[AKBiometricRatchetUIContext embeddedUIRightNavButtonTitle]
+ -[AKBiometricRatchetUIContext initWithAttributes:presentationContext:]
+ -[AKBiometricRatchetUIContext initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:embeddedUIPresentationMode:embeddedUIRightNavButtonTitle:]
+ -[AKBiometricRatchetiOSUIProvider _dismissRatchetUIForContext:viewController:]
+ -[AKBiometricRatchetiOSUIProvider _dismissRatchetUIForContext:viewController:].cold.1
+ -[AKBiometricRatchetiOSUIProvider _dismissRatchetUIForContext:viewController:].cold.2
+ -[AKBiometricRatchetiOSUIProvider _makeRatchetOptions:]
+ -[AKBiometricRatchetiOSUIProvider _presentEmbeddedRatchetUIWithOptions:]
+ -[AKBiometricRatchetiOSUIProvider _presentEmbeddedRatchetUIWithOptions:].cold.1
+ -[AKBiometricRatchetiOSUIProvider _presentEmbeddedRatchetUIWithOptions:].cold.2
+ -[AKBiometricRatchetiOSUIProvider _presentEmbeddedRatchetUIWithOptions:].cold.3
+ -[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]
+ -[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:].cold.1
+ -[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:].cold.2
+ -[AKBiometricRatchetiOSUIProvider _rightNavButtonTapped]
+ -[AKBiometricRatchetiOSUIProvider dealloc]
+ -[AKBiometricRatchetiOSUIProvider dealloc].cold.1
+ -[AKBiometricRatchetiOSUIProvider ratchetArmCompletion]
+ -[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:]
+ -[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:].cold.1
+ -[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:].cold.2
+ -[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:].cold.3
+ -[AKBiometricRatchetiOSUIProvider ratchetViewController]
+ -[AKBiometricRatchetiOSUIProvider ratchet]
+ -[AKBiometricRatchetiOSUIProvider setRatchet:]
+ -[AKBiometricRatchetiOSUIProvider setRatchetArmCompletion:]
+ -[AKBiometricRatchetiOSUIProvider setRatchetViewController:]
+ -[AKInAppAuthenticationRemoteUIProvider presentBasicLoginUIAsViewWithCompletion:].cold.2
+ -[AKInAppAuthenticationRemoteUIProvider proximitySetupSelectedAccount:completion:]
+ -[AKModalSignInViewController _beginObservingTextFieldDidChangeNotifications]
+ -[AKModalSignInViewController _endObservingTextFieldDidChangeNotifications]
+ -[AKModalSignInViewController _textFieldDidChange:]
+ -[AKModalSignInViewController _updateSignInButtonEnabled:]
+ -[AKModalSignInViewController dealloc]
+ -[AKModalSignInViewController viewWillAppear:]
+ _AKADPCohortHeaderKey
+ _AKBiometricRatchetEmbedPresentationModeModal
+ _AKBiometricRatchetEmbedPresentationModePush
+ _LocalAuthenticationEmbeddedUILibraryCore
+ _LocalAuthenticationEmbeddedUILibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_AKAppleIDFollowUpServerUIPresenter._presentingClientResponseCompletion
+ _OBJC_IVAR_$_AKAppleIDFollowUpServerUIPresenter.followUpProvider
+ _OBJC_IVAR_$_AKBiometricRatchetHook._biometricRatchetController
+ _OBJC_IVAR_$_AKBiometricRatchetUIContext._embeddedUIPresentationMode
+ _OBJC_IVAR_$_AKBiometricRatchetUIContext._embeddedUIRightNavButtonTitle
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._contextViewController
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._dispatchGroup
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._ratchet
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._ratchetArmCompletion
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._ratchetViewController
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UITextFieldTextDidChangeNotification
+ __OBJC_$_PROP_LIST_AKFollowupExtensionlessServerUIProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LARatchetViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LARatchetViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_LARatchetViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LARatchetViewControllerDelegate
+ __OBJC_PROTOCOL_$_LARatchetViewControllerDelegate
+ ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.91
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.168
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.172
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.172.cold.1
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.179
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.185
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.185.cold.1
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.40
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke_2
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke_2.cold.1
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.149
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.154
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.153
+ ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.163
+ ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.145
+ ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.145.cold.1
+ ___78-[AKBiometricRatchetiOSUIProvider _dismissRatchetUIForContext:viewController:]_block_invoke
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.157
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.158
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.71
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.76
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.80
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.87
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.87.cold.1
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.87.cold.2
+ ___83-[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]_block_invoke
+ ___83-[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]_block_invoke.cold.1
+ ___83-[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]_block_invoke.cold.2
+ ___83-[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]_block_invoke.cold.3
+ ___83-[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:]_block_invoke
+ ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.93
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.116
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.117
+ ___LocalAuthenticationEmbeddedUILibraryCore_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e46_v24?0"AKBiometricRatchetResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e34_v24?0"NSDictionary"8"NSError"16lr48l8r56l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e46_v24?0"AKBiometricRatchetResult"8"NSError"16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e5_v8?0lw72l8r64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80w_e5_v8?0lw80l8r72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.46
+ ___getLARatchetViewControllerClass_block_invoke
+ _audit_stringLocalAuthenticationEmbeddedUI
+ _getLARatchetViewControllerClass.softClass
+ _objc_getProperty
+ _objc_msgSend$_beginObservingTextFieldDidChangeNotifications
+ _objc_msgSend$_dismissRatchetUIForContext:viewController:
+ _objc_msgSend$_endObservingTextFieldDidChangeNotifications
+ _objc_msgSend$_makeRatchetOptions:
+ _objc_msgSend$_performClientCompletionWithServerResponse:additionalData:error:
+ _objc_msgSend$_presentEmbeddedRatchetUIWithOptions:
+ _objc_msgSend$_presentRatchetUIWithContext:options:completion:
+ _objc_msgSend$_updateSignInButtonEnabled:
+ _objc_msgSend$embeddedUIPresentationMode
+ _objc_msgSend$embeddedUIRightNavButtonTitle
+ _objc_msgSend$evaluateAndPresentViewController
+ _objc_msgSend$evaluateAndShowViewController
+ _objc_msgSend$followUpProvider
+ _objc_msgSend$initWithAttributes:presentationContext:
+ _objc_msgSend$makeViewControllerWithOptions:
+ _objc_msgSend$object
+ _objc_msgSend$presentServerUIWithContext:withCompletion:
+ _objc_msgSend$ratchet
+ _objc_msgSend$ratchetArmCompletion
+ _objc_msgSend$ratchetViewController
+ _objc_msgSend$rightNavButtonTapped
+ _objc_msgSend$setFollowUpProvider:
+ _objc_msgSend$setRatchet:
+ _objc_msgSend$setRatchetArmCompletion:
+ _objc_msgSend$setRatchetViewController:
+ _objc_retain_x27
+ _objc_setProperty_atomic
- -[AKBiometricRatchetHook _findMappedDeeplinkFor:withKey:]
- -[AKBiometricRatchetHook _findMappedDeeplinkFor:withKey:].cold.1
- -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.1
- -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.2
- -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.3
- ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.89
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.166
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.170
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.170.cold.1
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.177
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.183
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.183.cold.1
- ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68
- ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68.cold.1
- ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68.cold.2
- ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.72
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.146
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.147
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.149
- ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.161
- ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.143
- ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.143.cold.1
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.155
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.156
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.69
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.74
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.78
- ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78
- ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78.cold.1
- ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78.cold.2
- ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.91
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.113
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.114
- ___block_descriptor_56_e8_32s40bs48r_e46_v24?0"AKBiometricRatchetResult"8"NSError"16lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72w_e5_v8?0lw72l8r48l8r56l8s32l8s40l8r64l8
- ___block_literal_global.41
- _objc_msgSend$initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:
CStrings:
+ "\v"
+ "\x16"
+ "-[AKBiometricRatchetiOSUIProvider _presentRatchetUIWithContext:options:completion:]_block_invoke"
+ "-[AKBiometricRatchetiOSUIProvider ratchetViewController:didFinishWithResult:error:]"
+ "@\"<AKFollowUpProvider>\""
+ "@\"<AKFollowUpProvider>\"16@0:8"
+ "@\"AKBiometricRatchetController\""
+ "@\"LARatchet\""
+ "@\"LARatchetViewController\""
+ "@124@0:8@16@24@32@40B48B52@56@64B72@76@84@92@100@108@116"
+ "AKBiometricRatchetiOSUIProvider deallocated"
+ "BIOMETRIC_RATCHET_EMBEDDEDUI_PRESENTATION_MODE"
+ "BIOMETRIC_RATCHET_EMBEDDEDUI_RIGHT_NAVBUTTON_TITLE"
+ "Client did not provide a followUpProvider, defaulting to the AuthKit default one, which will only work with follow ups posted by AuthKit."
+ "Dismissing modally presented ratchet"
+ "Handing the server response to the calling client"
+ "LARatchetViewController"
+ "LARatchetViewControllerDelegate"
+ "Modal"
+ "Popping pushed ratchet"
+ "Present embedded ratchet with options: %@"
+ "Push"
+ "Pushing %@ onto %@"
+ "Pushing %@ onto %@ and presenting on %@"
+ "Ratchet presenting modally"
+ "Ratchet presenting push, %@"
+ "Ratchet returning result: %@, error: %@"
+ "T@\"<AKFollowUpProvider>\",&"
+ "T@\"<AKFollowUpProvider>\",&,VfollowUpProvider"
+ "T@\"LARatchet\",&,N,V_ratchet"
+ "T@\"LARatchetViewController\",&,N,V_ratchetViewController"
+ "T@\"NSString\",R,C,N,V_embeddedUIPresentationMode"
+ "T@\"NSString\",R,C,N,V_embeddedUIRightNavButtonTitle"
+ "T@?,C,N,V_ratchetArmCompletion"
+ "_beginObservingTextFieldDidChangeNotifications"
+ "_biometricRatchetController"
+ "_contextViewController"
+ "_dismissRatchetUIForContext:viewController:"
+ "_dispatchGroup"
+ "_embeddedUIPresentationMode"
+ "_embeddedUIRightNavButtonTitle"
+ "_endObservingTextFieldDidChangeNotifications"
+ "_makeRatchetOptions:"
+ "_performClientCompletionWithServerResponse:additionalData:error:"
+ "_presentEmbeddedRatchetUIWithOptions:"
+ "_presentRatchetUIWithContext:options:completion:"
+ "_presentingClientResponseCompletion"
+ "_ratchet"
+ "_ratchetArmCompletion"
+ "_ratchetViewController"
+ "_rightNavButtonTapped"
+ "_textFieldDidChange:"
+ "_updateSignInButtonEnabled:"
+ "embeddedUIPresentationMode"
+ "embeddedUIRightNavButtonTitle"
+ "evaluateAndPresentViewController"
+ "evaluateAndShowViewController"
+ "followUpProvider"
+ "initWithAttributes:presentationContext:"
+ "initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:embeddedUIPresentationMode:embeddedUIRightNavButtonTitle:"
+ "makeViewControllerWithOptions:"
+ "object"
+ "presentServerUIWithContext:withCompletion:withResponse:"
+ "presentationMode"
+ "ratchet"
+ "ratchetArmCompletion"
+ "ratchetViewController"
+ "ratchetViewController didFinishWithResult: result: %@, error: %@"
+ "ratchetViewController:didFinishWithResult:error:"
+ "ratchetViewControllerDidAppear:"
+ "returning result: %@, error: %@"
+ "rightNavBarButtonTitle"
+ "rightNavButtonTapped"
+ "setFollowUpProvider:"
+ "setRatchet:"
+ "setRatchetArmCompletion:"
+ "setRatchetViewController:"
+ "softlink:o:path:/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI"
+ "v24@0:8@\"<AKFollowUpProvider>\"16"
+ "v24@0:8@\"LARatchetViewController\"16"
+ "v40@0:8@\"AKExtensionlessFollowUpHelperContext\"16@?<v@?B@\"NSError\">24@?<v@?@\"NSHTTPURLResponse\"@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"LARatchetViewController\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@0:8@16@?24@?32"
- "-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke"
- "BIOMETRIC_RATCHET_QUICK_EXIT"

```
