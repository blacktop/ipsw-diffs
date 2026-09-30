## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x58e0
+2005.100.174.0.0
+  __TEXT.__text: 0x5f04
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x834
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x792
-  __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__oslogstring: 0x47c
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x1bea
-  __TEXT.__objc_methtype: 0xadf
-  __TEXT.__objc_stubs: 0x1260
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x158
+  __TEXT.__objc_methlist: 0x874
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0x7cc
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__oslogstring: 0x4cc
+  __TEXT.__unwind_info: 0x210
+  __TEXT.__objc_classname: 0x123
+  __TEXT.__objc_methname: 0x1c1e
+  __TEXT.__objc_methtype: 0xa94
+  __TEXT.__objc_stubs: 0x1320
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x750
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x240
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x1110
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__objc_const: 0x1108
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa8
-  __DATA.__data: 0x240
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBD9C43E-B725-3B02-B537-2B0CC21D91E7
-  Functions: 148
-  Symbols:   724
-  CStrings:  621
+  UUID: D14E9AB3-C347-39B9-961D-A779C15D18EE
+  Functions: 155
+  Symbols:   749
+  CStrings:  633
 
Symbols:
+ -[AuthenticationInProgress evaluationRequest]
+ -[AuthenticationInProgress initWithMechanism:uiDelegate:request:reply:]
+ -[AuthenticationInProgress isBiometric]
+ -[AuthenticationInProgress originator]
+ -[AuthenticationManager _biometryActiveReason]
+ -[AuthenticationManager authenticateForRequest:uiDelegate:mechanism:reply:]
+ -[AuthenticationManager isBiometryIdle]
+ -[AuthenticationManager runWhenBiometryIsIdle:]
+ -[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:]
+ -[ContextPlugin createInternalInfoWithPolicy:policyOptions:request:]
+ -[ContextPlugin evaluateACL:operation:options:uiDelegate:request:reply:]
+ -[ContextPlugin evaluatePolicy:options:uiDelegate:request:reply:]
+ -[ContextPlugin evaluateRequest:uiDelegate:reply:]
+ -[ContextPlugin externalizedContextProvider]
+ -[ContextPlugin externalizedContextWithError:]
+ -[DaemonProxy agentProxyWithErrorHandler:]
+ _LACEventFromBiometryType
+ _LACLogContext
+ _OBJC_CLASS_$_LACAgentProxyWithErrorHandler
+ _OBJC_CLASS_$_LACAuthenticationUIManagerFactory
+ _OBJC_CLASS_$_LACBiometryHelper
+ _OBJC_CLASS_$_LACConcurrencyUtilities
+ _OBJC_CLASS_$_LACDevice
+ _OBJC_CLASS_$_LACExternalizedContextProvider
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACPasscodeHelper
+ _OBJC_IVAR_$_AuthenticationInProgress._biometric
+ _OBJC_IVAR_$_AuthenticationInProgress._evaluationRequest
+ _OBJC_IVAR_$_ContextPlugin._externalizedContextProvider
+ _OBJC_IVAR_$_DaemonProxy._errorHandler
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizingXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizingXPC
+ __OBJC_PROTOCOL_$_LACContextExternalizingXPC
+ ___42-[DaemonProxy agentProxyWithErrorHandler:]_block_invoke
+ ___47-[AuthenticationManager runWhenBiometryIsIdle:]_block_invoke
+ ___53-[AuthenticationInProgress runWithCompletionHandler:]_block_invoke.36
+ ___84-[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:]_block_invoke
+ ___84-[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_literal_global.88
+ _objc_autorelease
+ _objc_msgSend$_biometryActiveReason
+ _objc_msgSend$contextExternalizer
+ _objc_msgSend$createInternalInfo:skipCallerIdentification:callerBundleId:request:
+ _objc_msgSend$daemonQueue
+ _objc_msgSend$evaluateACL:operation:options:uiDelegate:request:reply:
+ _objc_msgSend$evaluatePolicy:options:uiDelegate:request:reply:
+ _objc_msgSend$featureFlagPresentationContextEnabled
+ _objc_msgSend$initWithAgentProxy:errorHandler:
+ _objc_msgSend$initWithExternalizer:
+ _objc_msgSend$initWithMechanism:uiDelegate:request:reply:
+ _objc_msgSend$isBiometric
+ _objc_msgSend$makeCustomUIManagerForRequest:uiDelegate:
+ _objc_msgSend$originator
+ _objc_msgSend$pendingAuthentication
+ _objc_msgSend$runWithHints:eventHandler:reply:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_storeWeak
- -[AuthenticationInProgress initWithMechanism:policy:uiDelegate:originator:request:internalInfo:reply:]
- -[AuthenticationInProgress originatorPid]
- -[AuthenticationInProgress originatorUid]
- -[AuthenticationManager authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:request:mechanism:reply:]
- -[AuthenticationManager runWhenIdle:]
- -[ContextPlugin cachedExternalizedContext]
- -[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:]
- -[ContextPlugin createInternalInfoWithPolicy:policyOptions:request:originator:]
- -[ContextPlugin evaluateACL:operation:options:uiDelegate:originator:request:reply:]
- -[ContextPlugin evaluatePolicy:options:uiDelegate:originator:request:reply:]
- -[ContextPlugin evaluateRequest:uiDelegate:originator:reply:]
- -[DaemonProxy agentProxy]
- -[RemoteContext dealloc].cold.1
- _OBJC_CLASS_$_LACCachedExternalizedContext
- _OBJC_CLASS_$_LACClientInfoProvider
- _OBJC_CLASS_$_LAPasscodeHelper
- _OBJC_CLASS_$_LAUtils
- _OBJC_IVAR_$_AuthenticationInProgress._clientInfo
- _OBJC_IVAR_$_AuthenticationInProgress._originatorId
- _OBJC_IVAR_$_AuthenticationInProgress._originatorPid
- _OBJC_IVAR_$_AuthenticationInProgress._originatorUid
- _OBJC_IVAR_$_AuthenticationInProgress._policy
- _OBJC_IVAR_$_ContextPlugin._cachedExternalizedContext
- ___25-[DaemonProxy agentProxy]_block_invoke
- ___37-[AuthenticationManager runWhenIdle:]_block_invoke
- ___95-[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:]_block_invoke
- ___95-[ContextPlugin createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:]_block_invoke_2
- ___block_literal_global.74
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$cApiOrigin
- _objc_msgSend$cachedExternalizationDelegate
- _objc_msgSend$createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:
- _objc_msgSend$evaluateACL:operation:options:uiDelegate:originator:request:reply:
- _objc_msgSend$evaluatePolicy:options:uiDelegate:originator:request:reply:
- _objc_msgSend$infoForXPCClient:evaluationOptions:
- _objc_msgSend$initWithExternalizationDelegate:
- _objc_msgSend$initWithMechanism:policy:uiDelegate:originator:request:internalInfo:reply:
- _objc_msgSend$queue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "!"
+ "@\"<LACContextUIDelegate>\""
+ "@\"LACExternalizedContextProvider\""
+ "@24@0:8@?16"
+ "@40@0:8q16@24@32"
+ "@44@0:8@16B24@28@36"
+ "@48@0:8@16@24@32@?40"
+ "Biometry is idle"
+ "Biometry is not idle, %{public}@"
+ "LACContextExternalizingXPC"
+ "T@\"<LACEvaluationRequest>\",R,N,V_evaluationRequest"
+ "T@\"<LACXPCClient>\",R,N"
+ "T@\"LACExternalizedContextProvider\",R,N,V_externalizedContextProvider"
+ "TB,R,N"
+ "TB,R,N,GisBiometric,V_biometric"
+ "Tq,R,N"
+ "_biometric"
+ "_biometryActiveReason"
+ "_errorHandler"
+ "_evaluationRequest"
+ "_externalizedContextProvider"
+ "action scheduled when biometry is idle, %u blocks in queue, %{public}@"
+ "agentProxyWithErrorHandler:"
+ "authenticateForRequest:uiDelegate:mechanism:reply:"
+ "biometric"
+ "biometry is idle"
+ "contextExternalizer"
+ "createInternalInfo:skipCallerIdentification:callerBundleId:request:"
+ "createInternalInfoWithPolicy:policyOptions:request:"
+ "daemonQueue"
+ "evaluateACL:operation:options:uiDelegate:request:reply:"
+ "evaluatePolicy:options:uiDelegate:request:reply:"
+ "evaluateRequest:uiDelegate:reply:"
+ "evaluationRequest"
+ "externalizedContextProvider"
+ "externalizedContextWithError:"
+ "featureFlagPresentationContextEnabled"
+ "initWithAgentProxy:errorHandler:"
+ "initWithExternalizer:"
+ "initWithMechanism:uiDelegate:request:reply:"
+ "isBiometric"
+ "isBiometryIdle"
+ "makeCustomUIManagerForRequest:uiDelegate:"
+ "originator"
+ "pending %@"
+ "runWhenBiometryIsIdle:"
+ "runWithHints:eventHandler:reply:"
+ "running %@"
+ "v40@0:8@\"EvaluationRequest\"16@\"<LACContextUIDelegate>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v56@0:8q16@24@32@40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
- "@\"<LAUIDelegate>\""
- "@\"LACCachedExternalizedContext\""
- "@\"LACClientInfo\""
- "@48@0:8q16@24@32@40"
- "@52@0:8@16B24@28@36@44"
- "@72@0:8@16q24@32@40@48@56@?64"
- "CApiOrigin"
- "T@\"LACCachedExternalizedContext\",R,N,V_cachedExternalizedContext"
- "TI,R,N,V_originatorUid"
- "Ti,R,N,V_originatorPid"
- "Tq,R,N,V_originatorId"
- "Tq,R,N,V_policy"
- "_cachedExternalizedContext"
- "_clientInfo"
- "_originatorId"
- "_originatorPid"
- "_originatorUid"
- "_policy"
- "agentProxy"
- "authenticateForPolicy:constraintData:internalInfo:uiDelegate:originator:request:mechanism:reply:"
- "biometry is now idle, %u blocks in queue"
- "cApiOrigin"
- "cachedExternalizationDelegate"
- "cachedExternalizedContext"
- "createInternalInfo:skipCallerIdentification:callerBundleId:request:originator:"
- "createInternalInfoWithPolicy:policyOptions:request:originator:"
- "evaluateACL:operation:options:uiDelegate:originator:request:reply:"
- "evaluatePolicy:options:uiDelegate:originator:request:reply:"
- "evaluateRequest:uiDelegate:originator:reply:"
- "i"
- "i16@0:8"
- "infoForXPCClient:evaluationOptions:"
- "initWithExternalizationDelegate:"
- "initWithMechanism:policy:uiDelegate:originator:request:internalInfo:reply:"
- "originatorPid"
- "originatorUid"
- "queue"
- "runWhenIdle:"
- "synchronousExternalizedContextWithError:"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LACOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v64@0:8q16@24@32@40@48@?56"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v80@0:8q16@24@32@40@48@56@64@?72"

```
