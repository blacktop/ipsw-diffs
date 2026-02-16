## MechPasscode

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x150a4
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x290
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x1ff7
-  __TEXT.__objc_methname: 0xb91
+2005.100.174.0.0
+  __TEXT.__text: 0x14ba8
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x2b8
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x2160
+  __TEXT.__objc_methname: 0xcb2
   __TEXT.__oslogstring: 0x39d
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methtype: 0x19b
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x3b0
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__objc_methtype: 0x1b1
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x290
   __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x498
-  __DATA.__objc_selrefs: 0x3e8
+  __DATA.__objc_selrefs: 0x428
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 336E082C-1EAC-3EBC-8948-FA92AD692582
-  Functions: 440
-  Symbols:   340
-  CStrings:  486
+  UUID: EEBD78AE-6A86-3946-814E-73D06E523F37
+  Functions: 505
+  Symbols:   369
+  CStrings:  496
 
Symbols:
+ _ACMContextCredentialGetPropertyEx
+ _LACCredentialPassphrase
+ _LACErrorCodeAuthenticationFailed
+ _LACErrorCodeDoublePressRequired
+ _LACErrorCodeInternal
+ _LACErrorCodeSystemCancel
+ _LACErrorCodeUserCancel
+ _LACErrorSubcodeCredentialExpired
+ _LACEvaluationRequestPayloadKeyDTOEnvironment
+ _LACEventParamPasscodeVerified
+ _LACEventPassphrase
+ _LACEventPassword
+ _LACEventPushButton
+ _LACPolicyOptionDTO
+ _LACPolicyOptionMaxPasscodeFailures
+ _LACPolicyOptionSharedValidity
+ _LACPolicyOptionSkipDoublePress
+ _LACResultEnteredPassphrase
+ _LACResultPassedPasscode
+ _LACResultPushButtonPressed
+ _LACResultSecondaryPushButtonPressed
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACMutableEvaluationEventValuePasscodeStatus
+ _objc_opt_new
+ _objc_release_x10
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x28
- _OBJC_CLASS_$_LAPasscodeHelper
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "ACMContextCredentialGetPropertyEx"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "_dtoEnvironment"
+ "_runWithHints:eventHandler:activationCompletion:reply:"
+ "_startPasscodeMechanismWithHints:eventHandler:activationCompletion:reply:"
+ "_startSecureIntentWithOptions:eventHandler:reply:"
+ "errorWithCode:debugDescription:"
+ "errorWithCode:subcode:debugDescription:"
+ "eventHandler"
+ "featureFlagPresentationContextEnabled"
+ "handleEvaluationEvent:value:"
+ "payload"
+ "runWithHints:eventHandler:activationCompletion:reply:"
+ "runWithHints:eventHandler:reply:"
+ "setVerificationResult:"
+ "v48@0:8@16@24@?32@?40"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "ACMContextCredentialGetProperty"
- "_startPasscodeMechanismWithHints:eventsDelegate:reply:"
- "_startSecureIntentWithOptions:eventsDelegate:reply:"
- "dtoEnvironment"
- "errorWithCode:message:"
- "errorWithCode:subcode:message:"

```
