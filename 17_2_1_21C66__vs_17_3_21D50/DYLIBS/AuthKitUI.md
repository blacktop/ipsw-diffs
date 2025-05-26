## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-466.7.12.0.0
-  __TEXT.__text: 0x5be10
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x5e7c
-  __TEXT.__const: 0x2d8
-  __TEXT.__cstring: 0x3c50
-  __TEXT.__gcc_except_tab: 0x724
-  __TEXT.__oslogstring: 0x34a3
+466.7.15.0.0
+  __TEXT.__text: 0x5fbf8
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x60d4
+  __TEXT.__const: 0x2d0
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__cstring: 0x405a
+  __TEXT.__oslogstring: 0x3a99
   __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x1944
-  __TEXT.__objc_classname: 0x120d
-  __TEXT.__objc_methname: 0x13e9e
-  __TEXT.__objc_methtype: 0x3c79
-  __TEXT.__objc_stubs: 0xfbc0
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x1140
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__unwind_info: 0x1a20
+  __TEXT.__objc_classname: 0x12ac
+  __TEXT.__objc_methname: 0x1459a
+  __TEXT.__objc_methtype: 0x3d4d
+  __TEXT.__objc_stubs: 0x10140
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__const: 0x1240
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1a8
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x13658
-  __DATA_CONST.__objc_selrefs: 0x4af0
+  __DATA_CONST.__objc_const: 0x14a80
+  __DATA_CONST.__objc_selrefs: 0x4c78
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__objc_const: 0x2128
-  __AUTH_CONST.__cfstring: 0x3940
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__objc_const: 0x2290
+  __AUTH_CONST.__cfstring: 0x3dc0
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH.__objc_data: 0x1b30
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH.__objc_data: 0x1cc0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x688
-  __DATA.__objc_superrefs: 0x250
-  __DATA.__objc_ivar: 0x618
-  __DATA.__data: 0x1408
+  __DATA.__objc_classrefs: 0x6e0
+  __DATA.__objc_superrefs: 0x260
+  __DATA.__objc_ivar: 0x640
+  __DATA.__data: 0x1468
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2454
-  Symbols:   9259
-  CStrings:  4697
+  Functions: 2554
+  Symbols:   9611
+  CStrings:  4834
 
Symbols:
+ +[AKBiometricRatchetUtility armingMethodFromRatchetResult:]
+ +[AKBiometricRatchetUtility ratchetIdentifier]
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:]
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.1
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.2
+ +[AKBiometricRatchetUtility resultForSuccessfulArmingFromResponse:]
+ +[AKBiometricRatchetUtility resultForSuccessfulArmingFromResponse:].cold.1
+ +[AKBiometricRatchetUtility setRatchetIdentifier:]
+ +[AKBiometricRatchetUtility setRatchetIdentifier:].cold.1
+ +[AKBiometricRatchetUtility stateFromLARatchetState:]
+ -[AKBiometricRatchetHook .cxx_destruct]
+ -[AKBiometricRatchetHook _armBiometricRatchetWithServerAttributes:completion:]
+ -[AKBiometricRatchetHook _armBiometricRatchetWithServerAttributes:completion:].cold.1
+ -[AKBiometricRatchetHook _biometricRatchetUIContextFromAttributes:]
+ -[AKBiometricRatchetHook _biometricRatchetUIContextFromAttributes:].cold.1
+ -[AKBiometricRatchetHook _biometricRatchetUIContextFromAttributes:].cold.2
+ -[AKBiometricRatchetHook _findMappedDeeplinkFor:withKey:]
+ -[AKBiometricRatchetHook _findMappedDeeplinkFor:withKey:].cold.1
+ -[AKBiometricRatchetHook _updateResponseWithContext]
+ -[AKBiometricRatchetHook _updateResponseWithRatchetResult:]
+ -[AKBiometricRatchetHook delegate]
+ -[AKBiometricRatchetHook processElement:attributes:objectModel:completion:]
+ -[AKBiometricRatchetHook processObjectModel:completion:]
+ -[AKBiometricRatchetHook serverHookResponse]
+ -[AKBiometricRatchetHook setDelegate:]
+ -[AKBiometricRatchetHook setServerHookResponse:]
+ -[AKBiometricRatchetHook shouldMatchElement:]
+ -[AKBiometricRatchetHook shouldMatchModel:]
+ -[AKBiometricRatchetUIContext .cxx_destruct]
+ -[AKBiometricRatchetUIContext _assertValidPresentingViewController]
+ -[AKBiometricRatchetUIContext _assertValidPresentingViewController].cold.1
+ -[AKBiometricRatchetUIContext bioRatchetUIProvider]
+ -[AKBiometricRatchetUIContext debugDescription]
+ -[AKBiometricRatchetUIContext initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:]
+ -[AKBiometricRatchetUIContext initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:]
+ -[AKBiometricRatchetUIContext presentRatchetUIWithCompletion:]
+ -[AKBiometricRatchetUIContext presentRatchetUIWithCompletion:].cold.1
+ -[AKBiometricRatchetUIContext presentingViewController]
+ -[AKBiometricRatchetUIContext setBioRatchetUIProvider:]
+ -[AKBiometricRatchetUIContext setPresentingViewController:]
+ -[AKBiometricRatchetiOSUIProvider .cxx_destruct]
+ -[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]
+ -[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:].cold.1
+ -[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:].cold.2
+ -[AKBiometricRatchetiOSUIProvider _displayFindMyDisablementFailedErrorWithContext:]
+ -[AKBiometricRatchetiOSUIProvider _displayFindMyDisablementFailedErrorWithContext:].cold.1
+ -[AKBiometricRatchetiOSUIProvider _displayFindMyDisablementFailedErrorWithContext:].cold.2
+ -[AKBiometricRatchetiOSUIProvider initWithContext:]
+ -[AKBiometricRatchetiOSUIProvider initWithContext:].cold.1
+ -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]
+ -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.1
+ -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.2
+ -[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:].cold.3
+ -[AKDTOBiometryHook .cxx_destruct]
+ -[AKDTOBiometryHook _performDTOBiometricsWithServerAttributes:completion:]
+ -[AKDTOBiometryHook _performDTOBiometricsWithServerAttributes:completion:].cold.1
+ -[AKDTOBiometryHook _updateResponseWithContext]
+ -[AKDTOBiometryHook delegate]
+ -[AKDTOBiometryHook processElement:attributes:objectModel:completion:]
+ -[AKDTOBiometryHook processObjectModel:completion:]
+ -[AKDTOBiometryHook serverHookResponse]
+ -[AKDTOBiometryHook setDelegate:]
+ -[AKDTOBiometryHook setServerHookResponse:]
+ -[AKDTOBiometryHook shouldMatchElement:]
+ -[AKDTOBiometryHook shouldMatchModel:]
+ _AKBiometricRatchetSafetyCheckMetaContext
+ _AKSpyglassAppURL
+ _CFPreferencesSetAppValue
+ _CFPreferencesSynchronize
+ _LARatchetErrorUserInfoKeyState
+ _OBJC_CLASS_$_AFUtilities
+ _OBJC_CLASS_$_AKBiometricRatchetContext
+ _OBJC_CLASS_$_AKBiometricRatchetController
+ _OBJC_CLASS_$_AKBiometricRatchetHook
+ _OBJC_CLASS_$_AKBiometricRatchetResult
+ _OBJC_CLASS_$_AKBiometricRatchetUIContext
+ _OBJC_CLASS_$_AKBiometricRatchetUtility
+ _OBJC_CLASS_$_AKBiometricRatchetiOSUIProvider
+ _OBJC_CLASS_$_AKDTOBiometryHook
+ _OBJC_CLASS_$_AKRatchetState
+ _OBJC_CLASS_$_AKRatchetStateData
+ _OBJC_CLASS_$_FMDFMIPManager
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_AKBiometricRatchetHook._context
+ _OBJC_IVAR_$_AKBiometricRatchetHook._delegate
+ _OBJC_IVAR_$_AKBiometricRatchetHook._serverHookResponse
+ _OBJC_IVAR_$_AKBiometricRatchetUIContext._bioRatchetUIProvider
+ _OBJC_IVAR_$_AKBiometricRatchetUIContext._presentingViewController
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._context
+ _OBJC_IVAR_$_AKBiometricRatchetiOSUIProvider._findMyManager
+ _OBJC_IVAR_$_AKDTOBiometryHook._context
+ _OBJC_IVAR_$_AKDTOBiometryHook._delegate
+ _OBJC_IVAR_$_AKDTOBiometryHook._serverHookResponse
+ _OBJC_METACLASS_$_AKBiometricRatchetContext
+ _OBJC_METACLASS_$_AKBiometricRatchetHook
+ _OBJC_METACLASS_$_AKBiometricRatchetUIContext
+ _OBJC_METACLASS_$_AKBiometricRatchetUtility
+ _OBJC_METACLASS_$_AKBiometricRatchetiOSUIProvider
+ _OBJC_METACLASS_$_AKDTOBiometryHook
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_CLASS_METHODS_AKBiometricRatchetUtility
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetHook
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetUIContext
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetiOSUIProvider
+ __OBJC_$_INSTANCE_METHODS_AKDTOBiometryHook
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetHook
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetUIContext
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetiOSUIProvider
+ __OBJC_$_INSTANCE_VARIABLES_AKDTOBiometryHook
+ __OBJC_$_PROP_LIST_AKBiometricRatchetHook
+ __OBJC_$_PROP_LIST_AKBiometricRatchetUIContext
+ __OBJC_$_PROP_LIST_AKBiometricRatchetiOSUIProvider
+ __OBJC_$_PROP_LIST_AKDTOBiometryHook
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKBiometricRatchetUIProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKBiometricRatchetUIProvider
+ __OBJC_$_PROTOCOL_REFS_AKBiometricRatchetUIProvider
+ __OBJC_CLASS_PROTOCOLS_$_AKBiometricRatchetHook
+ __OBJC_CLASS_PROTOCOLS_$_AKBiometricRatchetUIContext
+ __OBJC_CLASS_PROTOCOLS_$_AKBiometricRatchetiOSUIProvider
+ __OBJC_CLASS_PROTOCOLS_$_AKDTOBiometryHook
+ __OBJC_CLASS_RO_$_AKBiometricRatchetHook
+ __OBJC_CLASS_RO_$_AKBiometricRatchetUIContext
+ __OBJC_CLASS_RO_$_AKBiometricRatchetUtility
+ __OBJC_CLASS_RO_$_AKBiometricRatchetiOSUIProvider
+ __OBJC_CLASS_RO_$_AKDTOBiometryHook
+ __OBJC_LABEL_PROTOCOL_$_AKBiometricRatchetUIProvider
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetHook
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetUIContext
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetUtility
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetiOSUIProvider
+ __OBJC_METACLASS_RO_$_AKDTOBiometryHook
+ __OBJC_PROTOCOL_$_AKBiometricRatchetUIProvider
+ ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.89
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.166
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.170
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.170.cold.1
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.177
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.183
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.183.cold.1
+ ___43-[AKBasicLoginViewController _loginOptions]_block_invoke.55
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68.cold.1
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.68.cold.2
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.72
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.cold.1
+ ___71-[AKASAuthorizationProvider performAuthorizationWithCompletionHandler:]_block_invoke.25
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.146
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.148
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.150
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.152
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.149
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.151
+ ___74-[AKDTOBiometryHook _performDTOBiometricsWithServerAttributes:completion:]_block_invoke
+ ___74-[AKDTOBiometryHook _performDTOBiometricsWithServerAttributes:completion:]_block_invoke.cold.1
+ ___74-[AKDTOBiometryHook _performDTOBiometricsWithServerAttributes:completion:]_block_invoke.cold.2
+ ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.161
+ ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.143
+ ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.143.cold.1
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.51
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.51.cold.1
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.55
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.55.cold.1
+ ___78-[AKBiometricRatchetHook _armBiometricRatchetWithServerAttributes:completion:]_block_invoke
+ ___78-[AKBiometricRatchetHook _armBiometricRatchetWithServerAttributes:completion:]_block_invoke.cold.1
+ ___78-[AKBiometricRatchetHook _armBiometricRatchetWithServerAttributes:completion:]_block_invoke.cold.2
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.155
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.156
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.69
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.74
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.78
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78.cold.1
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.78.cold.2
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.cold.1
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.cold.2
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.cold.3
+ ___82-[AKBiometricRatchetiOSUIProvider _disableFindMyIfRequiredWithContext:completion:]_block_invoke.cold.4
+ ___83-[AKBiometricRatchetiOSUIProvider _displayFindMyDisablementFailedErrorWithContext:]_block_invoke
+ ___83-[AKBiometricRatchetiOSUIProvider _displayFindMyDisablementFailedErrorWithContext:]_block_invoke.cold.1
+ ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.91
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.41
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.46
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.48
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.47
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.49
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_3.45
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.113
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.114
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.115
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0q8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e46_v24?0"AKBiometricRatchetResult"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r72w_e5_v8?0lw72l8r48l8r56l8s32l8s40l8r64l8
+ ___block_literal_global.141
+ ___block_literal_global.71
+ __unnamed_array_storage.54
+ _exit
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _objc_msgSend$_armBiometricRatchetWithServerAttributes:completion:
+ _objc_msgSend$_biometricRatchetUIContextFromAttributes:
+ _objc_msgSend$_disableFindMyIfRequiredWithContext:completion:
+ _objc_msgSend$_displayFindMyDisablementFailedErrorWithContext:
+ _objc_msgSend$_findMappedDeeplinkFor:withKey:
+ _objc_msgSend$_performDTOBiometricsWithServerAttributes:completion:
+ _objc_msgSend$_updateResponseWithContext
+ _objc_msgSend$_updateResponseWithRatchetResult:
+ _objc_msgSend$armWithContext:completion:
+ _objc_msgSend$armWithOptions:completion:
+ _objc_msgSend$armingMethodFromRatchetResult:
+ _objc_msgSend$beginRatchetBody
+ _objc_msgSend$beginRatchetTitle
+ _objc_msgSend$bioRatchetUIProvider
+ _objc_msgSend$calloutReason
+ _objc_msgSend$countdownText
+ _objc_msgSend$debugDescription
+ _objc_msgSend$deeplinkURL
+ _objc_msgSend$disableLocationDisplayWithCompletion:
+ _objc_msgSend$fallbackToNoAuth
+ _objc_msgSend$findMyErrorMessage
+ _objc_msgSend$findMyErrorTitle
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithDuration:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithRatchetState:armingMethod:
+ _objc_msgSend$initWithRawState:data:
+ _objc_msgSend$initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:
+ _objc_msgSend$isDTOEnabled
+ _objc_msgSend$metaContext
+ _objc_msgSend$presentRatchetUIWithCompletion:
+ _objc_msgSend$presentationContextForHook:
+ _objc_msgSend$ratchetIdentifier
+ _objc_msgSend$ratchetState
+ _objc_msgSend$rawState
+ _objc_msgSend$rawValue
+ _objc_msgSend$requireDisableLocationWithCompletion:
+ _objc_msgSend$resultForNonArmingFromError:
+ _objc_msgSend$resultForSuccessfulArmingFromResponse:
+ _objc_msgSend$showsLocationWarning
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$stateFromLARatchetState:
+ _objc_msgSend$toString:
+ _objc_msgSend$value
- ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.86
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.163
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.167
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.167.cold.1
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.174
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.180
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.180.cold.1
- ___43-[AKBasicLoginViewController _loginOptions]_block_invoke.52
- ___71-[AKASAuthorizationProvider performAuthorizationWithCompletionHandler:]_block_invoke.22
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.143
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.144
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.145
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.149
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.146
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.148
- ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.158
- ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.140
- ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.140.cold.1
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.48
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.48.cold.1
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.52
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.52.cold.1
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.152
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.153
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.66
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.71
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.75
- ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.88
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.38
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.40
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.45
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.41
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.46
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_3.42
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.110
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.111
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.112
- ___block_literal_global.138
- ___block_literal_global.68
- __unnamed_array_storage.51
CStrings:
+ "\x01\x11"
+ "%@ \tpresentationContext: %@,\n"
+ "%s (%d) called"
+ "+[AKBiometricRatchetUtility setRatchetIdentifier:]"
+ "-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke"
+ "@\"<AKBiometricRatchetUIProvider>\""
+ "@\"AKBiometricRatchetUIContext\""
+ "@\"FMDFMIPManager\""
+ "@108@0:8@16@24@32@40B48B52@56@64B72@76@84@92@100"
+ "@56@0:8@16@24@32@40B48B52"
+ "AKBiometricRatchetHook"
+ "AKBiometricRatchetIdentifierKey"
+ "AKBiometricRatchetUIContext"
+ "AKBiometricRatchetUIProvider"
+ "AKBiometricRatchetUtility"
+ "AKBiometricRatchetiOSUIProvider"
+ "AKBiometricRatchetiOSUIProvider.m"
+ "AKDTOBiometryHook"
+ "ALERT_DEFAULT_BUTTON"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_BODY"
+ "BIOMETRIC_RATCHET_BEGIN_RATCHET_TITLE"
+ "BIOMETRIC_RATCHET_CALLOUT_REASON"
+ "BIOMETRIC_RATCHET_CALLOUT_REASON_TEXT"
+ "BIOMETRIC_RATCHET_COUNTDOWN_TEXT"
+ "BIOMETRIC_RATCHET_FALLBACK_ALERT_SUBTITLE"
+ "BIOMETRIC_RATCHET_FALLBACK_TEXT"
+ "BIOMETRIC_RATCHET_FIND_MY_ERROR_MESSAGE"
+ "BIOMETRIC_RATCHET_FIND_MY_ERROR_TITLE"
+ "BIOMETRIC_RATCHET_QUICK_EXIT"
+ "Bio Ratchet UI Provider initialized"
+ "Biometry failed, sending failure response back to IdMS"
+ "Biometry succeeded, sending success response back to IdMS"
+ "Calling bioRatchetUIProvider to present the ratchet arming UI"
+ "Cannot determine if disable is required due to error: %@"
+ "DTO feature not enabled, no arming required, sending success back"
+ "DTO_BIOMETRY_FALLBACK_ALERT_SUBTITLE"
+ "Disabling FM not required via idms - idms is handling the logic to determine with operations need this"
+ "Disabling FindyMy not required via FindMy as it might already be in the blackout period"
+ "Error during arming ratchet: %@"
+ "Localizable-DTO"
+ "Presenting view controller is missing! Things don't look good!"
+ "Ratchet is armed with state: %@"
+ "Ratchet is in unexpected error - %@, underlying error - %@"
+ "Ratchet is not armed - error: %@, ratchet state: %@"
+ "Received response from arming ratchet call: %@"
+ "Require disable returned unknown, no-op"
+ "SAFETY_CHECK"
+ "T@\"<AKBiometricRatchetUIProvider>\",&,N,V_bioRatchetUIProvider"
+ "URL not found for key: %@"
+ "User picked OK"
+ "User selected Quick Exit, calling exit(0) on purpose"
+ "_armBiometricRatchetWithServerAttributes:completion:"
+ "_bioRatchetUIProvider"
+ "_biometricRatchetUIContextFromAttributes:"
+ "_disableFindMyIfRequiredWithContext:completion:"
+ "_displayFindMyDisablementFailedErrorWithContext:"
+ "_findMappedDeeplinkFor:withKey:"
+ "_findMyManager"
+ "_performDTOBiometricsWithServerAttributes:completion:"
+ "_updateResponseWithContext"
+ "_updateResponseWithRatchetResult:"
+ "ak:biometrics"
+ "ak:bioratchet"
+ "armWithContext:completion:"
+ "armWithOptions:completion:"
+ "armingMethodFromRatchetResult:"
+ "beginRatchetBody"
+ "beginRatchetTitle"
+ "bioRatchetUIProvider"
+ "biometricRatchetUIContext - passing nil presentation context"
+ "biometricRatchetUIContext - passing presentation context - %@"
+ "calloutReason"
+ "countdownText"
+ "deeplink"
+ "deeplinkType"
+ "deeplinkURL"
+ "disableFM"
+ "disableFMErrorMessage"
+ "disableFMErrorTitle"
+ "disableFindMy failed with error - %@"
+ "disableLocationDisplay failed with error - %@"
+ "disableLocationDisplay suceeded"
+ "disableLocationDisplayWithCompletion:"
+ "does not respondToSelector disableLocationDisplayWithCompletion"
+ "does not respondToSelector requireDisableLocationWithCompletion"
+ "fallback"
+ "fallbackText"
+ "fallbackToNoAuth"
+ "findMyErrorMessage"
+ "findMyErrorTitle"
+ "initWithBool:"
+ "initWithDuration:"
+ "initWithIdentifier:"
+ "initWithRatchetState:armingMethod:"
+ "initWithRawState:data:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
+ "initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:"
+ "initWithReason:calloutReason:deeplinkURL:presentationContext:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
+ "initing iOS bio ratchet UI provider with context: %@"
+ "isDTOEnabled"
+ "metaContext"
+ "nil presentingViewController"
+ "prefs:root=APPLE_ACCOUNT"
+ "presentBiometricRatchetArmingUIWithCompletion with context: %@"
+ "presentRatchetUIWithCompletion:"
+ "presentationContextForHook:"
+ "presentingViewController - %@"
+ "ratchet identifier is: %@"
+ "ratchetIdentifier"
+ "ratchetState"
+ "rawState"
+ "rawValue"
+ "requireDisableLocationWithCompletion:"
+ "result != nil || error != nil"
+ "resultForNonArmingFromError:"
+ "resultForSuccessfulArmingFromResponse:"
+ "setBioRatchetUIProvider:"
+ "setRatchetIdentifier:"
+ "showsLocationWarning"
+ "standardUserDefaults"
+ "stateFromLARatchetState:"
+ "toString:"
+ "undefined"
+ "urlBagKey"
+ "v24@0:8@?<v@?@\"AKBiometricRatchetResult\"@\"NSError\">16"
+ "v24@?0@\"AKBiometricRatchetResult\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "value"

```
