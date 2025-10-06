## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1394.82.1.0.0
-  __TEXT.__text: 0x31470
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x29c4
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x854
-  __TEXT.__cstring: 0x1de4
-  __TEXT.__oslogstring: 0x2480
+1394.100.151.0.1
+  __TEXT.__text: 0x2fca4
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x2a4c
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x860
+  __TEXT.__cstring: 0x1944
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__unwind_info: 0xfe8
-  __TEXT.__objc_classname: 0x92e
-  __TEXT.__objc_methname: 0x60a1
-  __TEXT.__objc_methtype: 0x1b18
-  __TEXT.__objc_stubs: 0x4020
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x1ae0
+  __TEXT.__oslogstring: 0x2333
+  __TEXT.__unwind_info: 0xfdc
+  __TEXT.__objc_classname: 0x912
+  __TEXT.__objc_methname: 0x60c1
+  __TEXT.__objc_methtype: 0x1af1
+  __TEXT.__objc_stubs: 0x3fe0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x19f8
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6808
-  __DATA_CONST.__objc_selrefs: 0x1798
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__cfstring: 0x1880
+  __DATA_CONST.__objc_const: 0x6840
+  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x2e0
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__cfstring: 0x1840
   __AUTH_CONST.__objc_const: 0x558
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2e8
-  __DATA.__objc_superrefs: 0x1a0
-  __DATA.__objc_ivar: 0x254
-  __DATA.__data: 0xa88
-  __DATA.__bss: 0x188
-  __DATA_DIRTY.__const: 0x2a0
+  __DATA.__objc_ivar: 0x250
+  __DATA.__data: 0xa98
+  __DATA.__bss: 0x178
+  __DATA_DIRTY.__const: 0x260
   __DATA_DIRTY.__objc_const: 0x13f8
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0xd0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35F52253-9CD0-35E6-9635-DE6B3EFCB205
-  Functions: 1301
-  Symbols:   4593
-  CStrings:  2090
+  UUID: B8FC90A9-B796-3655-ABE2-66FC73EFA26D
+  Functions: 1288
+  Symbols:   4569
+  CStrings:  2059
 
Symbols:
+ +[LARatchetErrorBuilder deviceTypeNotSupportedWithUserInfo:]
+ +[LARatchetManager _optionForRatchetOption:]
+ +[LARatchetManager optionsForRatchetArmOptions:]
+ +[LARatchetManager ratchetErrorForError:]
+ +[LARatchetManager ratchetResultForResult:]
+ -[LAContext evaluateCorePolicy:options:reply:]
+ -[LAContext optionCallerIconPath]
+ -[LAContext optionMaxCredentialAge]
+ -[LAContext setOptionCallerIconPath:]
+ -[LAContext setOptionMaxCredentialAge:]
+ -[LARatchetManager createContext]
+ -[LARatchetObserverWrapper .cxx_destruct]
+ -[LARatchetObserverWrapper hash]
+ -[LARatchetObserverWrapper initWithObserver:]
+ -[LARatchetObserverWrapper isEqual:]
+ -[LARatchetObserverWrapper observer]
+ -[LARatchetObserverWrapper ratchetStateDidChange:]
+ -[LARatchetObserverWrapper setObserver:]
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table88
+ _LACPolicyOptionAuthenticationCallbackReason
+ _LACPolicyOptionAuthenticationCallbackURL
+ _LACPolicyOptionAuthenticationReason
+ _LACPolicyOptionBeginRatchetLocalizedText
+ _LACPolicyOptionBeginRatchetLocalizedTitle
+ _LACPolicyOptionBeginRatchetShowsLocationWarning
+ _LACPolicyOptionBeginSecurityDelayImmediately
+ _LACPolicyOptionCountdownLocalizedText
+ _LACPolicyOptionCustomRatchetCancelLocalizedTitle
+ _LACPolicyOptionFallbackToNoAuthentication
+ _LACPolicyOptionNoCountdownUI
+ _LACPolicyOptionNotInteractive
+ _LACPolicyOptionUseShortExpirationTimer
+ _LACResultContext
+ _LACResultPassedBiometry
+ _LACResultPassedPasscode
+ _LACResultRatchetState
+ _LARatchetManagerObserverAssociatedObjectKey
+ _OBJC_CLASS_$_LACDTORatchetManager
+ _OBJC_CLASS_$_LARatchetObserverWrapper
+ _OBJC_IVAR_$_LARatchetManager._coreManager
+ _OBJC_IVAR_$_LARatchetObserverWrapper._observer
+ _OBJC_METACLASS_$_LARatchetObserverWrapper
+ __OBJC_$_INSTANCE_METHODS_LARatchetObserverWrapper
+ __OBJC_$_INSTANCE_VARIABLES_LARatchetObserverWrapper
+ __OBJC_$_PROP_LIST_LARatchetObserverWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTORatchetObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTORatchetObserver
+ __OBJC_$_PROTOCOL_REFS_LACContextProviding
+ __OBJC_$_PROTOCOL_REFS_LACDTORatchetObserver
+ __OBJC_CLASS_PROTOCOLS_$_LARatchetObserverWrapper
+ __OBJC_CLASS_RO_$_LARatchetObserverWrapper
+ __OBJC_LABEL_PROTOCOL_$_LACContextProviding
+ __OBJC_LABEL_PROTOCOL_$_LACDTORatchetObserver
+ __OBJC_METACLASS_RO_$_LARatchetObserverWrapper
+ __OBJC_PROTOCOL_$_LACContextProviding
+ __OBJC_PROTOCOL_$_LACDTORatchetObserver
+ ___43-[LARight authorizeWithOptions:completion:]_block_invoke.96
+ ___43-[LARight checkCanAuthorizeWithCompletion:]_block_invoke.87
+ ___51-[LARight authorizeWithLocalizedReason:completion:]_block_invoke.75
+ ___56-[LAAuthenticationBiometricMethod runBiometricOperation]_block_invoke.112
+ ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.90
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.124
+ ___70-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:]_block_invoke.105
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e40_v24?0"LACDTORatchetState"8"NSError"16lw48l8s40l8s32l8
+ ___block_literal_global.150
+ ___block_literal_global.212
+ ___block_literal_global.223
+ _objc_msgSend$deviceTypeNotSupportedWithUserInfo:
+ _objc_msgSend$initWithContextProvider:
+ _objc_msgSend$initWithObserver:
+ _objc_msgSend$optionsForRatchetArmOptions:
+ _objc_msgSend$ratchetErrorForError:
+ _objc_msgSend$ratchetResultForResult:
+ _objc_msgSend$reset
+ _objc_setAssociatedObject
- -[LARatchetEndpointProvider endpoint:]
- -[LARatchetManager _armPolicy]
- -[LARatchetManager _optionForRatchetOption:]
- -[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]
- -[LARatchetManager _remoteObjectProxyWithErrorHandler:]
- -[LARatchetManager notificationCenter:didReceiveNotification:]
- GCC_except_table40
- GCC_except_table57
- GCC_except_table59
- GCC_except_table63
- GCC_except_table70
- GCC_except_table72
- GCC_except_table87
- _CFStringCompare
- _LACDarwinNotificationRatchetStateDidChange
- _LACLogDTOClient
- _OBJC_CLASS_$_LACDTOServiceXPCClient
- _OBJC_CLASS_$_LACDarwinNotificationCenter
- _OBJC_CLASS_$_LARatchetEndpointProvider
- _OBJC_IVAR_$_LARatchetManager._notificationCenter
- _OBJC_IVAR_$_LARatchetManager._observers
- _OBJC_IVAR_$_LARatchetManager._remoteObjectProxy
- _OBJC_METACLASS_$_LARatchetEndpointProvider
- __OBJC_$_INSTANCE_METHODS_LARatchetEndpointProvider
- __OBJC_$_PROP_LIST_LARatchetEndpointProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOServiceXPCEndpointProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDarwinNotificationCenterObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOServiceXPCEndpointProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACDarwinNotificationCenterObserver
- __OBJC_$_PROTOCOL_REFS_LACDTOServiceXPCEndpointProvider
- __OBJC_$_PROTOCOL_REFS_LACDarwinNotificationCenterObserver
- __OBJC_CLASS_PROTOCOLS_$_LARatchetEndpointProvider
- __OBJC_CLASS_RO_$_LARatchetEndpointProvider
- __OBJC_LABEL_PROTOCOL_$_LACDTOServiceXPCEndpointProvider
- __OBJC_LABEL_PROTOCOL_$_LACDarwinNotificationCenterObserver
- __OBJC_METACLASS_RO_$_LARatchetEndpointProvider
- __OBJC_PROTOCOL_$_LACDTOServiceXPCEndpointProvider
- __OBJC_PROTOCOL_$_LACDarwinNotificationCenterObserver
- ___32-[LARatchetManager ratchetState]_block_invoke
- ___36-[LARatchetManager isFeatureEnabled]_block_invoke
- ___38-[LARatchetEndpointProvider endpoint:]_block_invoke
- ___38-[LARatchetManager isFeatureAvailable]_block_invoke
- ___38-[LARatchetManager isFeatureSupported]_block_invoke
- ___40-[LARatchetManager stateWithCompletion:]_block_invoke.15
- ___40-[LARatchetManager stateWithCompletion:]_block_invoke.15.cold.1
- ___40-[LARatchetManager stateWithCompletion:]_block_invoke.cold.1
- ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke.20
- ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke.cold.1
- ___43-[LARight authorizeWithOptions:completion:]_block_invoke.95
- ___43-[LARight checkCanAuthorizeWithCompletion:]_block_invoke.86
- ___51-[LARight authorizeWithLocalizedReason:completion:]_block_invoke.74
- ___56-[LAAuthenticationBiometricMethod runBiometricOperation]_block_invoke.111
- ___56-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke.17
- ___56-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke.cold.1
- ___57-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke.21
- ___57-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke.cold.1
- ___62-[LARatchetManager notificationCenter:didReceiveNotification:]_block_invoke
- ___62-[LARatchetManager notificationCenter:didReceiveNotification:]_block_invoke_2
- ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.87
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.123
- ___69-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke.23
- ___69-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke.cold.1
- ___70-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:]_block_invoke.102
- ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke
- ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke.28
- ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke_2
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32bs_e36_v24?0"LARatchetState"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e36_v24?0"LARatchetState"8"NSError"16lw32l8
- ___block_descriptor_48_e8_32bs40w_e40_v24?0"LACDTORatchetState"8"NSError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e26_"NSMutableDictionary"8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e36_v24?0"LARatchetState"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
- ___block_literal_global.11
- ___block_literal_global.13
- ___block_literal_global.149
- ___block_literal_global.209
- ___block_literal_global.222
- ___block_literal_global.5
- ___block_literal_global.9
- __dispatch_main_q
- _objc_msgSend$_armPolicy
- _objc_msgSend$_performArmRequestWithIdentifier:context:options:completion:
- _objc_msgSend$_remoteObjectProxyWithErrorHandler:
- _objc_msgSend$addObserver:notification:
- _objc_msgSend$cancelPendingEvaluationWithRatchetIdentifier:reason:completion:
- _objc_msgSend$enableFeatureWithCompletion:
- _objc_msgSend$hasObserver:
- _objc_msgSend$initWithEndpointProvider:
- _objc_msgSend$ratchetStateWithCompletion:
CStrings:
+ "@\"<LACContext>\"16@0:8"
+ "@\"<LARatchetObserver>\""
+ "@\"LACDTORatchetManager\""
+ "LACContextProviding"
+ "LACDTORatchetObserver"
+ "LARatchetObserverWrapper"
+ "T@\"<LARatchetObserver>\",W,V_observer"
+ "T@\"NSString\",?,R,C"
+ "_coreManager"
+ "createContext"
+ "deviceTypeNotSupportedWithUserInfo:"
+ "dumpStatusWithCompletion:"
+ "evaluateCorePolicy:options:reply:"
+ "initWithContextProvider:"
+ "optionCallerIconPath"
+ "optionMaxCredentialAge"
+ "optionsForRatchetArmOptions:"
+ "ratchetErrorForError:"
+ "ratchetResultForResult:"
+ "setOptionCallerIconPath:"
+ "setOptionMaxCredentialAge:"
+ "v24@0:8@\"LACDTORatchetState\"16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "%s context:%{public}@ options:%{public}@"
- "%s finished with error: %{public}@"
- "%s finished with result: %{public}@, error: %{public}@"
- "%s finished with state: %{public}@"
- "%s identifier:%{public}@, reason:%{public}@"
- "%s returned %s"
- "%s returned %{public}@"
- "-[LARatchetManager addObserver:]"
- "-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]"
- "-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke"
- "-[LARatchetManager checkCanEnableFeatureWithCompletion:]"
- "-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke"
- "-[LARatchetManager disableFeatureWithContext:completion:]"
- "-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke"
- "-[LARatchetManager enableFeatureWithReply:]"
- "-[LARatchetManager enableFeatureWithReply:]_block_invoke"
- "-[LARatchetManager isFeatureAvailable]"
- "-[LARatchetManager isFeatureEnabled]"
- "-[LARatchetManager isFeatureSupported]"
- "-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]"
- "-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]_block_invoke"
- "-[LARatchetManager ratchetState]"
- "-[LARatchetManager removeObserver:]"
- "-[LARatchetManager stateInContext:completion:]"
- "-[LARatchetManager stateInContext:completion:]_block_invoke"
- "-[LARatchetManager stateWithCompletion:]"
- "-[LARatchetManager stateWithCompletion:]_block_invoke"
- "@\"<LACDTOServiceXPCClient>\""
- "@\"<LACDarwinNotificationCenter>\""
- "@\"NSXPCListenerEndpoint\"24@0:8^@16"
- "LACDTOServiceXPCEndpointProvider"
- "LACDarwinNotificationCenterObserver"
- "LARatchetEndpointProvider"
- "Platform not supported"
- "Will notify %d observers about new state: %{public}@"
- "_armPolicy"
- "_notificationCenter"
- "_performArmRequestWithIdentifier:context:options:completion:"
- "_remoteObjectProxyWithErrorHandler:"
- "addObserver:notification:"
- "cancelPendingEvaluationWithRatchetIdentifier:reason:completion:"
- "endpoint:"
- "hasObserver:"
- "initWithEndpointProvider:"
- "isFeatureEnabled returned %s"
- "kLAServiceTypeRatchet"
- "notificationCenter:didReceiveNotification:"
- "ratchetStateWithCompletion:"
- "v24@?0@\"LARatchetState\"8@\"NSError\"16"
- "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
- "v32@0:8@16^{__CFString=}24"

```
