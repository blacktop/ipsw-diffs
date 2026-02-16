## ModuleACM

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x21c6c
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x2540
-  __TEXT.__objc_methlist: 0x4a4
+2005.100.174.0.0
+  __TEXT.__text: 0x21a40
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0x2620
+  __TEXT.__objc_methlist: 0x4ac
   __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0x544
-  __TEXT.__cstring: 0x2b3e
-  __TEXT.__objc_methname: 0x2762
-  __TEXT.__oslogstring: 0xb13
+  __TEXT.__gcc_except_tab: 0x478
+  __TEXT.__cstring: 0x2ca7
+  __TEXT.__objc_methname: 0x2732
+  __TEXT.__oslogstring: 0xb51
   __TEXT.__objc_classname: 0x56
   __TEXT.__ustring: 0x1e
-  __TEXT.__objc_methtype: 0x62a
+  __TEXT.__objc_methtype: 0x617
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x630
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__unwind_info: 0x620
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x290
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xb78
   __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x88
+  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0xa20
+  __DATA.__objc_selrefs: 0xa58
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x2

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50A8ECBA-7371-361E-83C5-857075DA67BE
-  Functions: 576
-  Symbols:   421
-  CStrings:  1072
+  UUID: 131A2A51-41D4-3BC5-B531-A3DA8A0337DA
+  Functions: 641
+  Symbols:   441
+  CStrings:  1083
 
Symbols:
+ _ACMContextCredentialGetPropertyEx
+ _LACCredentialExtractablePassword
+ _LACErrorCodeRetryAfterFailure
+ _LACErrorInfoKeyAvailableMechanisms
+ _LACErrorInfoKeyBiometryDatabaseHash
+ _LACErrorInfoKeyBiometryType
+ _LACErrorInfoKeyMechanismTree
+ _LACEvaluationRequestPayloadKeyConcurrentEvaluationConfig
+ _LACEventPasscode
+ _LACEventPassphrase
+ _LACEventPassword
+ _LACEventPearl
+ _LACEventPushButton
+ _LACEventPushButtonSecondary
+ _LACEventTouchID
+ _LACLogConcurrentEvaluations
+ _LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet
+ _LACPolicyOptionCallerAuditTokenUsage
+ _LACPolicyOptionCheckApplePayEnabled
+ _LACPolicyOptionEventProcessing
+ _LACPolicyStockholm
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _OBJC_CLASS_$_LACAuthenticationUIManagerFactory
+ _OBJC_CLASS_$_LACConcurrentEvaluationConfiguration
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_MechanismUI_PC
+ _OBJC_CLASS_$_RemoteUIManager
+ _objc_retainAutoreleasedReturnValue
- _LAAvailableMechanisms
- _LABiometryDatabaseHash
- _LAErrorInfoBiometryType
- _LAMechanismTree
- _OBJC_CLASS_$_LAPasscodeHelper
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "@24@0:8^@16"
+ "ACMContextCredentialGetPropertyEx"
+ "B72@0:8q16@24@32@40@48@56@?64"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "Offloading request rid: %i"
+ "Resuming offloaded request rid: %i"
+ "_evaluateACL:operation:options:uiDelegate:request:callerName:callerBundleId:reply:"
+ "_evaluateCtkPolicy:options:uiDelegate:request:reply:"
+ "_evaluateOperation:aclRef:options:uiDelegate:request:validate:callerName:callerBundleId:reply:"
+ "_handleAcmRequirement:policy:constraintData:operation:internalInfo:uiDelegate:request:reply:"
+ "_handleCTKACL:tokenId:operation:options:request:callerName:callerBundleId:reply:"
+ "_mechanismForACMRequirement:acmContextRecord:policy:internalInfo:uiDelegate:request:reply:"
+ "_validateACL:evaluateOperation:options:uiDelegate:request:callerName:callerBundleId:reply:"
+ "_validateOperation:aclRef:evaluateOperation:options:uiDelegate:request:reply:"
+ "_validateOperations:aclRef:evaluateOperation:options:uiDelegate:request:currentResult:reply:"
+ "_validatePassword:options:uiDelegate:request:callerName:callerBundleId:reply:"
+ "authenticateForRequest:uiDelegate:mechanism:reply:"
+ "client"
+ "createInternalInfo:skipCallerIdentification:callerBundleId:request:"
+ "createInternalInfoWithPolicy:policyOptions:request:"
+ "evaluateACL:operation:options:uiDelegate:request:callerName:callerBundleId:reply:"
+ "evaluateACL:operation:options:uiDelegate:request:reply:"
+ "evaluatePolicy:options:uiDelegate:request:reply:"
+ "externalizedContextProvider"
+ "externalizedContextWithError:"
+ "featureFlagPresentationContextEnabled"
+ "finishedAuthenticationForPolicy:constraintData:operation:internalInfo:uiDelegate:request:availabilityEvents:result:error:reply:"
+ "identifier"
+ "initWithACMContext:contextExternalizer:"
+ "initWithNonUiMechanism:request:uiManager:"
+ "makeManagerForRequest:uiDelegate:remoteUIManager:"
+ "mechanismForACMRequirement:acmContextRecord:policy:internalInfo:uiDelegate:request:reply:"
+ "mechanismForApplicationPasswordMode:acmContextRecord:options:internalInfo:uiDelegate:request:reply:"
+ "setIsEvaluationOffloaded:"
+ "v56@0:8q16@24@32@40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v72@0:8q16@24@32@40@48@56@?64"
+ "v72@0:8r^{__ACMRequirement=}16@24q32@40@48@56@?64"
+ "v80@0:8r^{__ACMRequirement=}16q24@32@40@48@56@64@?72"
+ "v84@0:8@16@24@32@40@48B56@60@68@?76"
+ "v96@0:8q16@24@32@40@48@56@64@72@80@?88"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "ACMContextCredentialGetProperty"
- "B80@0:8q16@24@32@40@48@56@64@?72"
- "_evaluateACL:operation:options:uiDelegate:originator:request:callerName:callerBundleId:reply:"
- "_evaluateCtkPolicy:options:uiDelegate:originator:request:reply:"
- "_evaluateOperation:aclRef:options:uiDelegate:originator:request:validate:callerName:callerBundleId:reply:"
- "_handleAcmRequirement:policy:constraintData:operation:internalInfo:uiDelegate:originator:request:reply:"
- "_handleCTKACL:tokenId:operation:options:originator:request:callerName:callerBundleId:reply:"
- "_mechanismForACMRequirement:acmContextRecord:policy:internalInfo:uiDelegate:originator:request:reply:"
- "_validateACL:evaluateOperation:options:uiDelegate:originator:request:callerName:callerBundleId:reply:"
- "_validateOperation:aclRef:evaluateOperation:options:uiDelegate:originator:request:reply:"
- "_validateOperations:aclRef:evaluateOperation:options:uiDelegate:originator:request:currentResult:reply:"
- "_validatePassword:options:uiDelegate:originator:request:callerName:callerBundleId:reply:"
- "authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:request:mechanism:reply:"
- "cachedExternalizedContext"
- "createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:"
- "createInternalInfoWithPolicy:policyOptions:request:originator:"
- "evaluateACL:operation:options:uiDelegate:originator:request:callerName:callerBundleId:reply:"
- "evaluateACL:operation:options:uiDelegate:originator:request:reply:"
- "evaluatePolicy:options:uiDelegate:originator:request:reply:"
- "finishedAuthenticationForPolicy:constraintData:operation:internalInfo:uiDelegate:originator:request:availabilityEvents:result:error:reply:"
- "initWithACMContext:cachedExternalizationDelegate:"
- "mechanismForACMRequirement:acmContextRecord:policy:internalInfo:uiDelegate:originator:request:reply:"
- "mechanismForApplicationPasswordMode:acmContextRecord:options:internalInfo:uiDelegate:originator:request:reply:"
- "v104@0:8q16@24@32@40@48@56@64@72@80@88@?96"
- "v64@0:8q16@24@32@40@48@?56"
- "v80@0:8q16@24@32@40@48@56@64@?72"
- "v80@0:8r^{__ACMRequirement=}16@24q32@40@48@56@64@?72"
- "v88@0:8@16@24@32@40@48@56@64@72@?80"
- "v88@0:8r^{__ACMRequirement=}16q24@32@40@48@56@64@72@?80"
- "v92@0:8@16@24@32@40@48@56B64@68@76@?84"

```
