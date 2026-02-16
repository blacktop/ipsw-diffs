## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-525.326.4.1.0
-  __TEXT.__text: 0xc5c24
+525.475.13.1.0
+  __TEXT.__text: 0xc8068
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x8334
+  __TEXT.__objc_methlist: 0x844c
   __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x14a8
-  __TEXT.__cstring: 0x50e8
-  __TEXT.__oslogstring: 0x4c38
+  __TEXT.__gcc_except_tab: 0x14ec
+  __TEXT.__cstring: 0x5005
+  __TEXT.__oslogstring: 0x4e7a
   __TEXT.__dlopen_cstrs: 0x163
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xac

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1530
-  __TEXT.__objc_classname: 0x1532
-  __TEXT.__objc_methname: 0x17641
-  __TEXT.__objc_methtype: 0x47df
-  __TEXT.__objc_stubs: 0x12380
-  __DATA_CONST.__got: 0xd00
-  __DATA_CONST.__const: 0x24d8
-  __DATA_CONST.__objc_classlist: 0x388
+  __TEXT.__unwind_info: 0x1568
+  __TEXT.__objc_classname: 0x1618
+  __TEXT.__objc_methname: 0x17974
+  __TEXT.__objc_methtype: 0x4841
+  __TEXT.__objc_stubs: 0x12680
+  __DATA_CONST.__got: 0xd20
+  __DATA_CONST.__const: 0x2518
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c40
+  __DATA_CONST.__objc_selrefs: 0x5cf8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x4e40
-  __AUTH_CONST.__objc_const: 0x17148
+  __AUTH_CONST.__cfstring: 0x4ea0
+  __AUTH_CONST.__objc_const: 0x177c8
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x2068
+  __AUTH.__objc_data: 0x20b8
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x74c
-  __DATA.__data: 0x19d0
+  __DATA.__objc_ivar: 0x760
+  __DATA.__data: 0x18c0
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B3171EB3-1242-3384-8AC1-A63379ABBEC0
-  Functions: 2712
-  Symbols:   11065
-  CStrings:  6174
+  UUID: 2BFF8DBC-7338-3BCB-8BDE-4A8777274C18
+  Functions: 2738
+  Symbols:   11136
+  CStrings:  6217
 
Symbols:
+ -[AKAuthorizationInputPaneViewController _accountDisplayNameForFirstParty]
+ -[AKAuthorizationInputPaneViewController _firstPartyUserProfileTableViewCell]
+ -[AKIcon _imageWithSystemName:size:masked:]
+ -[AKPDPBlobGenerationHook .cxx_destruct]
+ -[AKPDPBlobGenerationHook _extractPasswordFromObjectModel:]
+ -[AKPDPBlobGenerationHook _getAuthKitAccountForCurrentiCloudAccountWithError:]
+ -[AKPDPBlobGenerationHook _processPasswordCollection:clientInfo:completion:]
+ -[AKPDPBlobGenerationHook _setResponsePayloadWithContext:pdpBlob:]
+ -[AKPDPBlobGenerationHook account]
+ -[AKPDPBlobGenerationHook delegate]
+ -[AKPDPBlobGenerationHook initWithAccount:]
+ -[AKPDPBlobGenerationHook initWithAccount:ruiParser:]
+ -[AKPDPBlobGenerationHook processElement:attributes:objectModel:completion:]
+ -[AKPDPBlobGenerationHook processObjectModel:completion:]
+ -[AKPDPBlobGenerationHook ruiParser]
+ -[AKPDPBlobGenerationHook serverHookResponse]
+ -[AKPDPBlobGenerationHook setAccount:]
+ -[AKPDPBlobGenerationHook setDelegate:]
+ -[AKPDPBlobGenerationHook setRuiParser:]
+ -[AKPDPBlobGenerationHook setServerHookResponse:]
+ -[AKPDPBlobGenerationHook shouldMatchElement:]
+ -[AKPDPBlobGenerationHook shouldMatchModel:]
+ GCC_except_table167
+ GCC_except_table96
+ _AKClientInfoPasswordVersionKey
+ _AKNewPasswordKey
+ _AKPasswordCollectionActionKey
+ _AKPasswordFieldKey
+ _AKPasswordIterationKey
+ _AKPasswordSaltKey
+ _AKPasswordVerifierKey
+ _AKSerializedRecordKey
+ _OBJC_CLASS_$_AKAuthorizationLoginChoice
+ _OBJC_CLASS_$_AKPDPBlobGenerationContext
+ _OBJC_CLASS_$_AKPDPBlobGenerationHook
+ _OBJC_IVAR_$_AKIcon._systemName
+ _OBJC_IVAR_$_AKPDPBlobGenerationHook._account
+ _OBJC_IVAR_$_AKPDPBlobGenerationHook._delegate
+ _OBJC_IVAR_$_AKPDPBlobGenerationHook._ruiParser
+ _OBJC_IVAR_$_AKPDPBlobGenerationHook._serverHookResponse
+ _OBJC_METACLASS_$_AKPDPBlobGenerationHook
+ __OBJC_$_INSTANCE_METHODS_AKPDPBlobGenerationHook
+ __OBJC_$_INSTANCE_VARIABLES_AKPDPBlobGenerationHook
+ __OBJC_$_PROP_LIST_AKPDPBlobGenerationHook
+ __OBJC_CLASS_PROTOCOLS_$_AKPDPBlobGenerationHook
+ __OBJC_CLASS_RO_$_AKPDPBlobGenerationHook
+ __OBJC_METACLASS_RO_$_AKPDPBlobGenerationHook
+ ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.100
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.183
+ ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.187
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.194
+ ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.200
+ ___43-[AKBasicLoginViewController _loginOptions]_block_invoke.59
+ ___52-[AKInAppAuthenticationRemoteUIDelegate _showAlert:]_block_invoke.82
+ ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.37
+ ___71-[AKASAuthorizationProvider performAuthorizationWithCompletionHandler:]_block_invoke.25
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.160
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.161
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.162
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.166
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.163
+ ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.165
+ ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.178
+ ___75-[AKInAppAuthenticationRemoteUIProvider proximitySetupCompletedWithResult:]_block_invoke.203
+ ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.157
+ ___76-[AKPDPBlobGenerationHook _processPasswordCollection:clientInfo:completion:]_block_invoke
+ ___77-[AKAuthorizationInputPaneViewController _firstPartyUserProfileTableViewCell]_block_invoke
+ ___77-[AKAuthorizationInputPaneViewController _firstPartyUserProfileTableViewCell]_block_invoke_2
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.48
+ ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.52
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.169
+ ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.170
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.77
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.82
+ ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.86
+ ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.102
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.52
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.54
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.55
+ ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_3.56
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.124
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.125
+ ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.126
+ ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls48l8s32l8s40l8
+ ___block_literal_global.146
+ ___block_literal_global.44
+ ___block_literal_global.69
+ ___os_log_helper_16_2_3_8_112_8_64_8_64
+ _objc_msgSend$_accountDisplayNameForFirstParty
+ _objc_msgSend$_extractPasswordFromObjectModel:
+ _objc_msgSend$_firstPartyUserProfileTableViewCell
+ _objc_msgSend$_getAuthKitAccountForCurrentiCloudAccountWithError:
+ _objc_msgSend$_imageWithSystemName:size:masked:
+ _objc_msgSend$_processPasswordCollection:clientInfo:completion:
+ _objc_msgSend$_setResponsePayloadWithContext:pdpBlob:
+ _objc_msgSend$_systemImageNamed:
+ _objc_msgSend$account
+ _objc_msgSend$ak_redactedCopy
+ _objc_msgSend$altDSIDForAccount:
+ _objc_msgSend$configurationPreferringMulticolor
+ _objc_msgSend$generatePDPBlobWithContext:completion:
+ _objc_msgSend$iconSystemName
+ _objc_msgSend$imageWithSymbolConfiguration:
+ _objc_msgSend$initWithAccount:
+ _objc_msgSend$initWithPassword:clientInfo:telemetryFlowID:altDSID:error:
+ _objc_msgSend$initWithUser:site:
+ _objc_msgSend$isDBRTwoEnabled
+ _objc_msgSend$message
+ _objc_msgSend$parentViewController
+ _objc_msgSend$pdpStateValueForAccount:
+ _objc_msgSend$ruiParser
+ _objc_msgSend$setAppleIDAuth:
+ _objc_msgSend$setCreateAppleID:
+ _objc_msgSend$setRuiParser:
+ _objc_msgSend$srpIteration
+ _objc_msgSend$srpPasswordVersion
+ _objc_msgSend$srpSalt
+ _objc_msgSend$verifier
- GCC_except_table163
- GCC_except_table92
- _AKDTOLocalizationTable
- _OBJC_CLASS_$_NSStringDrawingContext
- ___100-[AKInAppAuthenticationRemoteUIProvider presentSecondFactorAlertWithError:title:message:completion:]_block_invoke.103
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.186
- ___112-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertWithError:title:message:waitForInteraction:completion:]_block_invoke.190
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.197
- ___120-[AKInAppAuthenticationRemoteUIProvider presentLoginAlertUIAsViewWithError:title:message:waitForInteraction:completion:]_block_invoke.203
- ___43-[AKBasicLoginViewController _loginOptions]_block_invoke.62
- ___52-[AKInAppAuthenticationRemoteUIDelegate _showAlert:]_block_invoke.85
- ___66-[AKBiometricRatchetiOSUIProvider presentRatchetUIWithCompletion:]_block_invoke.40
- ___71-[AKASAuthorizationProvider performAuthorizationWithCompletionHandler:]_block_invoke.28
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.163
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.165
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.167
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke.169
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.166
- ___72-[AKInAppAuthenticationRemoteUIProvider _actionsForLoginWithCompletion:]_block_invoke_2.168
- ___74-[AKInAppAuthenticationRemoteUIProvider _showPasswordFieldWithCompletion:]_block_invoke.181
- ___75-[AKInAppAuthenticationRemoteUIProvider proximitySetupCompletedWithResult:]_block_invoke.206
- ___76-[AKInAppAuthenticationRemoteUIProvider _showMaxAttemptAlertWithCompletion:]_block_invoke.160
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.51
- ___77-[AKAuthorizationViewController presentAuthenticationChoiceUIWithCompletion:]_block_invoke.55
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.172
- ___81-[AKInAppAuthenticationRemoteUIProvider _secondFactorActionsForAlert:completion:]_block_invoke.173
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.80
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.85
- ___81-[AKInAppAuthenticationRemoteUIProvider presentKeepUsingUIForAppleID:completion:]_block_invoke.89
- ___90-[AKInAppAuthenticationRemoteUIProvider presentIDPProvidedUIWithConfiguration:completion:]_block_invoke.105
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.55
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke.60
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_2.61
- ___91-[AKInAppAuthenticationRemoteUIProvider _configureProximityAuthLoginOptionsWithCompletion:]_block_invoke_3.59
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.127
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.128
- ___99-[AKInAppAuthenticationRemoteUIProvider presentBiometricOrPasscodeValidationForAppleID:completion:]_block_invoke.129
- ___block_literal_global.143
- ___block_literal_global.47
- ___block_literal_global.72
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_AuthKitUI
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_AuthKitUI
- _objc_msgSend$_configureTitleHeaderView
- _objc_msgSend$baselineOffset
- _objc_msgSend$boundingRectWithSize:options:attributes:context:
- _objc_msgSend$configurationWithScale:
- _objc_msgSend$descender
- _objc_msgSend$setWantsBaselineOffset:
CStrings:
+ "5"
+ "@\"AKAppleIDObjectModelFieldExtractor\""
+ "@24@0:8^@16"
+ "AKPDPBlobGenerationHook"
+ "Calling daemon to generate PDP blob for altDSID: %@"
+ "Failed to get AuthKit account for altDSID %{mask.hash}@: %@"
+ "No altDSID available for iCloud account"
+ "PDP blob generated successfully - blob length: %lu"
+ "PDP blob generation failed: %@"
+ "PDPBlobGenerationHook processing - PDP state is Active"
+ "PDPBlobGenerationHook skipped - PDP state is not Active (state: %lu)"
+ "Password collection hook disabled - DBR_TWO feature flag is off"
+ "Successfully generated password collection hook."
+ "T@\"AKAppleIDObjectModelFieldExtractor\",&,N,V_ruiParser"
+ "User is tapping Account cell displayed during First party sign in"
+ "_accountDisplayNameForFirstParty"
+ "_extractPasswordFromObjectModel:"
+ "_firstPartyUserProfileTableViewCell"
+ "_getAuthKitAccountForCurrentiCloudAccountWithError:"
+ "_imageWithSystemName:size:masked:"
+ "_processPasswordCollection:clientInfo:completion:"
+ "_ruiParser"
+ "_setResponsePayloadWithContext:pdpBlob:"
+ "_systemImageNamed:"
+ "_systemName"
+ "ak:collectPassword"
+ "ak_redactedCopy"
+ "altDSIDForAccount:"
+ "configurationPreferringMulticolor"
+ "generatePDPBlobWithContext:completion:"
+ "iconSystemName"
+ "imageWithSymbolConfiguration:"
+ "initWithAccount:ruiParser:"
+ "initWithPassword:clientInfo:telemetryFlowID:altDSID:error:"
+ "initWithUser:site:"
+ "isDBRTwoEnabled"
+ "newPassword"
+ "parentViewController"
+ "passwordField not provided in clientInfo"
+ "passwordVerifier"
+ "pdpStateValueForAccount:"
+ "ruiParser"
+ "serializedRecord"
+ "setAppleIDAuth:"
+ "setCreateAppleID:"
+ "setRuiParser:"
+ "srpIteration"
+ "srpPasswordVersion"
+ "srpSalt"
+ "verifier"
- "4"
- "Localizable-DTO"
- "baselineOffset"
- "boundingRectWithSize:options:attributes:context:"
- "configurationWithScale:"
- "descender"
- "info.circle.fill"
- "setWantsBaselineOffset:"

```
