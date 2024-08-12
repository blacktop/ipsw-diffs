## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-380.1.0.0.0
-  __TEXT.__text: 0x48164
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x2960
+383.0.0.0.0
+  __TEXT.__text: 0x4a2ac
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x2a64
   __TEXT.__const: 0x1124
-  __TEXT.__gcc_except_tab: 0xffc
-  __TEXT.__oslogstring: 0x7c02
-  __TEXT.__cstring: 0x4a98
+  __TEXT.__gcc_except_tab: 0x10b0
+  __TEXT.__oslogstring: 0x7fec
+  __TEXT.__cstring: 0x4e7f
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1250
-  __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methname: 0x7c33
-  __TEXT.__objc_methtype: 0x18b0
-  __TEXT.__objc_stubs: 0x4680
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x2900
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__objc_classname: 0x6eb
+  __TEXT.__objc_methname: 0x811b
+  __TEXT.__objc_methtype: 0x18c9
+  __TEXT.__objc_stubs: 0x4940
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x2b98
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c50
+  __DATA_CONST.__objc_selrefs: 0x1d38
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x808
+  __AUTH_CONST.__auth_got: 0x810
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x9388
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0x3240
+  __AUTH_CONST.__objc_const: 0x9530
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x780
-  __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x298
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0x1038
-  __DATA.__bss: 0xe9
+  __DATA.__bss: 0x109
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_DIRTY.__objc_data: 0x960
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
+  - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1808
-  Symbols:   2579
-  CStrings:  2854
+  Functions: 1856
+  Symbols:   2640
+  CStrings:  2938
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_AACustodianController
+ _OBJC_CLASS_$_AACustodianRecoveryRequestContext
+ _OBJC_CLASS_$_AAFExponentialRetryScheduler
+ _OBJC_CLASS_$_CDPCustodianRecoveryController
+ _OBJC_METACLASS_$_CDPCustodianRecoveryController
+ _SetupAssistantLibrary
+ _SetupAssistantLibraryCore
+ __BYSetupAssistantNeedsToRun
+ _getBYSetupAssistantNeedsToRunSymbolLoc
+ _kCDPAnalyticsEscrowRecordCreationNotAttemptedEvent
+ _kCDPAnalyticsiCSCUpdateFinishEvent
+ _kCDPAnalyticsiCSCUpdateStartEvent
+ _kCDP_AKAuthenticationNewAccountCreated
+ _scanf
CStrings:
+ "\tcontextType: %!l(MISSING)d"
+ "\tisSharediPad: %!d(MISSING)\n"
+ "\tisTTSURecovery: %!d(MISSING)\n"
+ "\tnewAccountCreated: %!d(MISSING)\n"
+ "\"CDPContext: a new account was just created, setting up CDPContext=%!l(MISSING)d\""
+ "\"Custodian recovery session started sessionID: %!@(MISSING), error: %!@(MISSING)\""
+ "\"Failed to obtain recoverySession with error: %!@(MISSING)\""
+ "\"Local Secret Updated after retry: %!{(MISSING)BOOL}d. UIProxy: %!@(MISSING). Context: %!@(MISSING)\""
+ "\"Processing Local Secret Change failed: %!@(MISSING). Attempting one retry.\""
+ "\"Retrying Local Secret Change failed: %!@(MISSING).\""
+ "\"ShouldClearRKCacheAfterGeneration: %!{(MISSING)BOOL}d\""
+ "%!@(MISSING): setting context type to be CDPContextTypeAccountRecovery with flowID=%!@(MISSING)"
+ "/AppleInternal/Library/Frameworks/SetupAssistant.framework/SetupAssistant"
+ "/System/Library/Frameworks/SetupAssistant.framework/SetupAssistant"
+ "/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "@\"AACustodianController\""
+ "@\"Attempting to fetch custodian recovery keys\""
+ "@\"Custodian recovery info failed validation with error: %!@(MISSING)\""
+ "@\"Custodian recovery info validated, safe to dismiss the view\""
+ "@\"Failed to fetch recovery keys for sessionID: %!@(MISSING) with error: %!@(MISSING)\""
+ "@\"Successfuly obtained custodian recovery session: %!@(MISSING)\""
+ "@\"Successfuly obtained recovery keys for sessionID: %!@(MISSING)\""
+ "@\"Successfuly validated custodian recovery code for custodian with UUID: %!@(MISSING)\""
+ "@\"Validation of custodian recovery code for custodian with UUID: %!@(MISSING) failed with error: %!@(MISSING)\""
+ "AKNewAccountCreated"
+ "AccountCreation"
+ "AccountRecovery"
+ "B16@?0@\"NSError\"8"
+ "BYSetupAssistantNeedsToRun"
+ "CDPCustodianRecoveryController"
+ "ClearRKCacheAfterGeneration"
+ "Enter the recovery code provided by your custodian: "
+ "Error: %!s(MISSING)\n"
+ "Recovery code validated."
+ "Recovery completed"
+ "Recovery failed with error: %!s(MISSING)"
+ "Reenter the recovery code provided by your custodian: "
+ "TB,R,N,V_newAccountCreated"
+ "TB,V_didAttemptSecureBackupEnablement"
+ "TB,V_willAttemptAsyncSecureBackupEnablement"
+ "The recovery code is not valid"
+ "UTF8String"
+ "Validating recovery info..."
+ "Validating the recovery code..."
+ "_custodianController"
+ "_didAttemptSecureBackupEnablement"
+ "_fetchRecoveryInfoWithCompletion:"
+ "_handleCloudDataProtectionStateWithCompletion:"
+ "_newAccountCreated"
+ "_newAccountCreated"
+ "_recoverySession"
+ "_willAttemptAsyncSecureBackupEnablement"
+ "cdp_indicatesDaemonConnectionWasInterrupted"
+ "com.apple.corecdp.iCSCUpdateFinish"
+ "com.apple.corecdp.iCSCUpdateStart"
+ "com.apple.corecdp.icscCreationNotAttempted"
+ "didAttemptSecureBackupEnablement"
+ "fetchCustodianRecoveryKeysWithSessionID:completion:"
+ "initWithMaxRetries:"
+ "isBuddyFinished"
+ "isSubsetOfContextTypeSignIn:"
+ "newAccountCreated"
+ "scheduleTask:shouldRetry:completionHandler:"
+ "setDidAttemptSecureBackupEnablement:"
+ "setOwnerAppleID:"
+ "setRecoveryCode:"
+ "setRecoverySessionID:"
+ "setWillAttemptAsyncSecureBackupEnablement:"
+ "shouldClearRKCacheAfterGeneration"
+ "showCustodianOSInstructionScreen:validator:"
+ "showCustodianProvidedCodeEntryScreen:controller:validator:"
+ "showRecoveryContactStartingScreen:validator:"
+ "showRemoteDeviceCodeEntryScreen:validator:"
+ "showRemoteDeviceListScreen:validator:"
+ "startCustodianRecoveryWithContext:completion:"
+ "startRecoverySessionWithCompletion:"
+ "stringWithUTF8String:"
+ "v16@?0@?<v@?@@\"NSError\">8"
+ "v24@?0@\"AACustodianDataRecoveryKeys\"8@\"NSError\"16"
+ "v24@?0@\"AACustodianRecoveryRequestContext\"8@\"NSError\"16"
+ "v24@?0@\"CDPCustodianRecoveryInfo\"8@\"NSError\"16"
+ "v24@?0@8@\"NSError\"16"
+ "validateCode:controller:completion:"
+ "validateCustodianRecoveryCodeWithContext:completion:"
+ "validateRecoveryCode:withCompletion:"
+ "willAttemptAsyncSecureBackupEnablement"
- "\tisSharediPad: %!d(MISSING)"
- "\tisTTSURecoveryu: %!d(MISSING)"

```
