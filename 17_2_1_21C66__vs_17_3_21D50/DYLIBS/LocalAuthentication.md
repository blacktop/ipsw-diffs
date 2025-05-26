## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0x2d124
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x24f4
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x7cc
-  __TEXT.__cstring: 0x1731
+1394.82.1.0.0
+  __TEXT.__text: 0x31470
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x29c4
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x854
+  __TEXT.__cstring: 0x1de4
+  __TEXT.__oslogstring: 0x2480
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2333
-  __TEXT.__unwind_info: 0xe94
-  __TEXT.__objc_classname: 0x79c
-  __TEXT.__objc_methname: 0x5785
-  __TEXT.__objc_methtype: 0x1a0f
-  __TEXT.__objc_stubs: 0x3ae0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__unwind_info: 0xfe8
+  __TEXT.__objc_classname: 0x92e
+  __TEXT.__objc_methname: 0x60a1
+  __TEXT.__objc_methtype: 0x1b18
+  __TEXT.__objc_stubs: 0x4020
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x1ae0
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5ae0
-  __DATA_CONST.__objc_selrefs: 0x1540
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x458
+  __DATA_CONST.__objc_const: 0x6808
+  __DATA_CONST.__objc_selrefs: 0x1798
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__cfstring: 0x1880
+  __AUTH_CONST.__objc_const: 0x558
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH.__objc_data: 0x410
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x288
-  __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x22c
-  __DATA.__data: 0x9c8
-  __DATA.__bss: 0x178
-  __DATA_DIRTY.__const: 0x280
+  __DATA.__objc_classrefs: 0x2e8
+  __DATA.__objc_superrefs: 0x1a0
+  __DATA.__objc_ivar: 0x254
+  __DATA.__data: 0xa88
+  __DATA.__bss: 0x188
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0x13f8
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0xd0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1170
-  Symbols:   4156
-  CStrings:  1730
+  Functions: 1301
+  Symbols:   4593
+  CStrings:  1894
 
Symbols:
+ +[LARatchetErrorBuilder _errorWithCode:debugDescription:]
+ +[LARatchetErrorBuilder _errorWithCode:userInfo:]
+ +[LARatchetErrorBuilder beforeFirstUnlockWithUserInfo:]
+ +[LARatchetErrorBuilder biometryNotEnrolledWithUserInfo:]
+ +[LARatchetErrorBuilder errorNotArmedWithRatchetState:]
+ +[LARatchetErrorBuilder genericErrorWithDebugDescription:]
+ +[LARatchetErrorBuilder genericErrorWithUnderlyingError:]
+ +[LARatchetErrorBuilder notInteractiveErrorWithUserInfo:]
+ +[LARatchetErrorBuilder passcodeNotSetWithUserInfo:]
+ +[LARatchetErrorBuilder ratchetErrorWithError:]
+ +[LARatchetErrorBuilder userCustomCancelErrorWithUserInfo:]
+ +[LARatchetManager sharedInstance]
+ -[LAContext optionAuthenticationCallbackReason]
+ -[LAContext optionAuthenticationCallbackURL]
+ -[LAContext optionAuthenticationIdentifier]
+ -[LAContext optionBeginRatchetLocalizedText]
+ -[LAContext optionBeginRatchetLocalizedTitle]
+ -[LAContext optionBeginRatchetShowsLocationWarning]
+ -[LAContext optionBeginSecurityDelayImmediately]
+ -[LAContext optionCountdownLocalizedText]
+ -[LAContext optionDTO]
+ -[LAContext optionFallbackToNoAuthentication]
+ -[LAContext optionNoCountdownUI]
+ -[LAContext optionUseShortExpirationTimer]
+ -[LAContext setOptionAuthenticationCallbackReason:]
+ -[LAContext setOptionAuthenticationCallbackURL:]
+ -[LAContext setOptionAuthenticationIdentifier:]
+ -[LAContext setOptionBeginRatchetLocalizedText:]
+ -[LAContext setOptionBeginRatchetLocalizedTitle:]
+ -[LAContext setOptionBeginRatchetShowsLocationWarning:]
+ -[LAContext setOptionBeginSecurityDelayImmediately:]
+ -[LAContext setOptionCountdownLocalizedText:]
+ -[LAContext setOptionDTO:]
+ -[LAContext setOptionFallbackToNoAuthentication:]
+ -[LAContext setOptionNoCountdownUI:]
+ -[LAContext setOptionUseShortExpirationTimer:]
+ -[LARatchet .cxx_destruct]
+ -[LARatchet addObserver:]
+ -[LARatchet armWithOptions:completion:]
+ -[LARatchet cancelWithReason:completion:]
+ -[LARatchet identifier]
+ -[LARatchet initWithIdentifier:]
+ -[LARatchet removeObserver:]
+ -[LARatchet setContext:]
+ -[LARatchet stateWithCompletion:]
+ -[LARatchetEndpointProvider endpoint:]
+ -[LARatchetManager .cxx_destruct]
+ -[LARatchetManager _armPolicy]
+ -[LARatchetManager _optionForRatchetOption:]
+ -[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]
+ -[LARatchetManager _remoteObjectProxyWithErrorHandler:]
+ -[LARatchetManager addObserver:]
+ -[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]
+ -[LARatchetManager cancelCurrentRatchetWithReason:completion:]
+ -[LARatchetManager checkCanEnableFeatureWithCompletion:]
+ -[LARatchetManager currentRatchetWithCompletion:]
+ -[LARatchetManager disableFeatureWithContext:completion:]
+ -[LARatchetManager enableFeatureWithCompletion:]
+ -[LARatchetManager enableFeatureWithReply:]
+ -[LARatchetManager init]
+ -[LARatchetManager isFeatureAvailable]
+ -[LARatchetManager isFeatureEnabled]
+ -[LARatchetManager isFeatureSupported]
+ -[LARatchetManager isRatchetFeatureEnabled]
+ -[LARatchetManager notificationCenter:didReceiveNotification:]
+ -[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]
+ -[LARatchetManager ratchetState]
+ -[LARatchetManager removeObserver:]
+ -[LARatchetManager reset]
+ -[LARatchetManager stateInContext:completion:]
+ -[LARatchetManager stateWithCompletion:]
+ -[LARatchetState .cxx_destruct]
+ -[LARatchetState description]
+ -[LARatchetState duration]
+ -[LARatchetState initWithRawValue:value:uuid:]
+ -[LARatchetState initWithState:]
+ -[LARatchetState isEqual:]
+ -[LARatchetState rawValue]
+ -[LARatchetState uuid]
+ -[LARatchetState value]
+ -[LARatchetStateValue duration]
+ -[LARatchetStateValue initInternal]
+ -[LARatchetStateValue initWithDuration:]
+ -[LARatchetStateValue isEqual:]
+ -[LARatchetStateValueArmed duration]
+ -[LARatchetStateValueCollapsed duration]
+ -[LARatchetStateValueExpired duration]
+ -[LARatchetStateValueReady duration]
+ -[LARatchetStateValueWaitingForCoolOff duration]
+ -[LARatchetStateValueWaitingForSecondAuthentication duration]
+ GCC_except_table40
+ _CFStringCompare
+ _LACDTORatchetStateDurationInfinite
+ _LACDarwinNotificationRatchetStateDidChange
+ _LACLogDTOClient
+ _LADarwinNotificationRatchetStateDidChange
+ _LARatchetErrorDomain
+ _LARatchetErrorUserInfoKeyState
+ _NSStringFromLARatchetStateDuration
+ _NSStringFromLARatchetStateRawValue
+ _OBJC_CLASS_$_LACDTORatchetState
+ _OBJC_CLASS_$_LACDTOServiceXPCClient
+ _OBJC_CLASS_$_LACDarwinNotificationCenter
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_LARatchetEndpointProvider
+ _OBJC_CLASS_$_LARatchetErrorBuilder
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_CLASS_$_LARatchetState
+ _OBJC_CLASS_$_LARatchetStateValue
+ _OBJC_CLASS_$_LARatchetStateValueArmed
+ _OBJC_CLASS_$_LARatchetStateValueCollapsed
+ _OBJC_CLASS_$_LARatchetStateValueExpired
+ _OBJC_CLASS_$_LARatchetStateValueNotStarted
+ _OBJC_CLASS_$_LARatchetStateValueReady
+ _OBJC_CLASS_$_LARatchetStateValueWaitingForCoolOff
+ _OBJC_CLASS_$_LARatchetStateValueWaitingForSecondAuthentication
+ _OBJC_IVAR_$_LARatchet._context
+ _OBJC_IVAR_$_LARatchet._identifier
+ _OBJC_IVAR_$_LARatchet._ratchetManager
+ _OBJC_IVAR_$_LARatchetManager._notificationCenter
+ _OBJC_IVAR_$_LARatchetManager._observers
+ _OBJC_IVAR_$_LARatchetManager._remoteObjectProxy
+ _OBJC_IVAR_$_LARatchetState._rawValue
+ _OBJC_IVAR_$_LARatchetState._uuid
+ _OBJC_IVAR_$_LARatchetState._value
+ _OBJC_IVAR_$_LARatchetStateValue._duration
+ _OBJC_METACLASS_$_LARatchet
+ _OBJC_METACLASS_$_LARatchetEndpointProvider
+ _OBJC_METACLASS_$_LARatchetErrorBuilder
+ _OBJC_METACLASS_$_LARatchetManager
+ _OBJC_METACLASS_$_LARatchetState
+ _OBJC_METACLASS_$_LARatchetStateValue
+ _OBJC_METACLASS_$_LARatchetStateValueArmed
+ _OBJC_METACLASS_$_LARatchetStateValueCollapsed
+ _OBJC_METACLASS_$_LARatchetStateValueExpired
+ _OBJC_METACLASS_$_LARatchetStateValueNotStarted
+ _OBJC_METACLASS_$_LARatchetStateValueReady
+ _OBJC_METACLASS_$_LARatchetStateValueWaitingForCoolOff
+ _OBJC_METACLASS_$_LARatchetStateValueWaitingForSecondAuthentication
+ __OBJC_$_CLASS_METHODS_LARatchetErrorBuilder
+ __OBJC_$_CLASS_METHODS_LARatchetManager
+ __OBJC_$_INSTANCE_METHODS_LARatchet
+ __OBJC_$_INSTANCE_METHODS_LARatchetEndpointProvider
+ __OBJC_$_INSTANCE_METHODS_LARatchetManager
+ __OBJC_$_INSTANCE_METHODS_LARatchetState
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValue
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueArmed
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueCollapsed
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueExpired
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueReady
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueWaitingForCoolOff
+ __OBJC_$_INSTANCE_METHODS_LARatchetStateValueWaitingForSecondAuthentication
+ __OBJC_$_INSTANCE_VARIABLES_LARatchet
+ __OBJC_$_INSTANCE_VARIABLES_LARatchetManager
+ __OBJC_$_INSTANCE_VARIABLES_LARatchetState
+ __OBJC_$_INSTANCE_VARIABLES_LARatchetStateValue
+ __OBJC_$_PROP_LIST_LARatchet
+ __OBJC_$_PROP_LIST_LARatchetEndpointProvider
+ __OBJC_$_PROP_LIST_LARatchetManager
+ __OBJC_$_PROP_LIST_LARatchetState
+ __OBJC_$_PROP_LIST_LARatchetStateValueArmed
+ __OBJC_$_PROP_LIST_LARatchetStateValueCollapsed
+ __OBJC_$_PROP_LIST_LARatchetStateValueExpired
+ __OBJC_$_PROP_LIST_LARatchetStateValueReady
+ __OBJC_$_PROP_LIST_LARatchetStateValueWaitingForCoolOff
+ __OBJC_$_PROP_LIST_LARatchetStateValueWaitingForSecondAuthentication
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOServiceXPCEndpointProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDarwinNotificationCenterObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOServiceXPCEndpointProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDarwinNotificationCenterObserver
+ __OBJC_$_PROTOCOL_REFS_LACDTOServiceXPCEndpointProvider
+ __OBJC_$_PROTOCOL_REFS_LACDarwinNotificationCenterObserver
+ __OBJC_CLASS_PROTOCOLS_$_LARatchetEndpointProvider
+ __OBJC_CLASS_PROTOCOLS_$_LARatchetManager
+ __OBJC_CLASS_RO_$_LARatchet
+ __OBJC_CLASS_RO_$_LARatchetEndpointProvider
+ __OBJC_CLASS_RO_$_LARatchetErrorBuilder
+ __OBJC_CLASS_RO_$_LARatchetManager
+ __OBJC_CLASS_RO_$_LARatchetState
+ __OBJC_CLASS_RO_$_LARatchetStateValue
+ __OBJC_CLASS_RO_$_LARatchetStateValueArmed
+ __OBJC_CLASS_RO_$_LARatchetStateValueCollapsed
+ __OBJC_CLASS_RO_$_LARatchetStateValueExpired
+ __OBJC_CLASS_RO_$_LARatchetStateValueNotStarted
+ __OBJC_CLASS_RO_$_LARatchetStateValueReady
+ __OBJC_CLASS_RO_$_LARatchetStateValueWaitingForCoolOff
+ __OBJC_CLASS_RO_$_LARatchetStateValueWaitingForSecondAuthentication
+ __OBJC_LABEL_PROTOCOL_$_LACDTOServiceXPCEndpointProvider
+ __OBJC_LABEL_PROTOCOL_$_LACDarwinNotificationCenterObserver
+ __OBJC_METACLASS_RO_$_LARatchet
+ __OBJC_METACLASS_RO_$_LARatchetEndpointProvider
+ __OBJC_METACLASS_RO_$_LARatchetErrorBuilder
+ __OBJC_METACLASS_RO_$_LARatchetManager
+ __OBJC_METACLASS_RO_$_LARatchetState
+ __OBJC_METACLASS_RO_$_LARatchetStateValue
+ __OBJC_METACLASS_RO_$_LARatchetStateValueArmed
+ __OBJC_METACLASS_RO_$_LARatchetStateValueCollapsed
+ __OBJC_METACLASS_RO_$_LARatchetStateValueExpired
+ __OBJC_METACLASS_RO_$_LARatchetStateValueNotStarted
+ __OBJC_METACLASS_RO_$_LARatchetStateValueReady
+ __OBJC_METACLASS_RO_$_LARatchetStateValueWaitingForCoolOff
+ __OBJC_METACLASS_RO_$_LARatchetStateValueWaitingForSecondAuthentication
+ __OBJC_PROTOCOL_$_LACDTOServiceXPCEndpointProvider
+ __OBJC_PROTOCOL_$_LACDarwinNotificationCenterObserver
+ ___32-[LARatchetManager ratchetState]_block_invoke
+ ___34+[LARatchetManager sharedInstance]_block_invoke
+ ___36-[LARatchetManager isFeatureEnabled]_block_invoke
+ ___38-[LARatchetEndpointProvider endpoint:]_block_invoke
+ ___38-[LARatchetManager isFeatureAvailable]_block_invoke
+ ___38-[LARatchetManager isFeatureSupported]_block_invoke
+ ___39-[LARatchet armWithOptions:completion:]_block_invoke
+ ___40-[LARatchetManager stateWithCompletion:]_block_invoke
+ ___40-[LARatchetManager stateWithCompletion:]_block_invoke.15
+ ___40-[LARatchetManager stateWithCompletion:]_block_invoke.15.cold.1
+ ___40-[LARatchetManager stateWithCompletion:]_block_invoke.cold.1
+ ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke
+ ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke.20
+ ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke.cold.1
+ ___46-[LARatchetManager stateInContext:completion:]_block_invoke
+ ___48-[LARatchetManager enableFeatureWithCompletion:]_block_invoke
+ ___56-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke
+ ___56-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke.17
+ ___56-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke.cold.1
+ ___57-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke
+ ___57-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke.21
+ ___57-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke.cold.1
+ ___62-[LARatchetManager notificationCenter:didReceiveNotification:]_block_invoke
+ ___62-[LARatchetManager notificationCenter:didReceiveNotification:]_block_invoke_2
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.123
+ ___69-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke
+ ___69-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke.23
+ ___69-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke.cold.1
+ ___79-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]_block_invoke
+ ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke
+ ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke.28
+ ___80-[LARatchetManager _performArmRequestWithIdentifier:context:options:completion:]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e36_v24?0"LARatchetState"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e36_v24?0"LARatchetState"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e40_v24?0"LACDTORatchetState"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e26_"NSMutableDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e36_v24?0"LARatchetState"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_literal_global.11
+ ___block_literal_global.13
+ ___block_literal_global.222
+ ___block_literal_global.5
+ ___block_literal_global.9
+ __dispatch_main_q
+ _objc_msgSend$_armPolicy
+ _objc_msgSend$_errorWithCode:debugDescription:
+ _objc_msgSend$_errorWithCode:userInfo:
+ _objc_msgSend$_optionForRatchetOption:
+ _objc_msgSend$_performArmRequestWithIdentifier:context:options:completion:
+ _objc_msgSend$_remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$addObserver:notification:
+ _objc_msgSend$beforeFirstUnlockWithUserInfo:
+ _objc_msgSend$biometryNotEnrolledWithUserInfo:
+ _objc_msgSend$cancelArmRequestWithIdentifier:reason:completion:
+ _objc_msgSend$cancelPendingEvaluationWithRatchetIdentifier:reason:completion:
+ _objc_msgSend$checkCanEnableFeatureWithCompletion:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$disableFeatureWithContext:completion:
+ _objc_msgSend$duration
+ _objc_msgSend$enableFeatureWithCompletion:
+ _objc_msgSend$enableFeatureWithReply:
+ _objc_msgSend$error:hasCode:subcode:
+ _objc_msgSend$errorNotArmedWithRatchetState:
+ _objc_msgSend$genericErrorWithDebugDescription:
+ _objc_msgSend$genericErrorWithUnderlyingError:
+ _objc_msgSend$hasObserver:
+ _objc_msgSend$initInternal
+ _objc_msgSend$initWithDuration:
+ _objc_msgSend$initWithEndpointProvider:
+ _objc_msgSend$initWithRawValue:value:uuid:
+ _objc_msgSend$initWithState:
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isFeatureSupported
+ _objc_msgSend$notInteractiveErrorWithUserInfo:
+ _objc_msgSend$passcodeNotSetWithUserInfo:
+ _objc_msgSend$performArmRequestWithIdentifier:context:options:completion:
+ _objc_msgSend$ratchetErrorWithError:
+ _objc_msgSend$ratchetState
+ _objc_msgSend$ratchetStateDidChange:
+ _objc_msgSend$ratchetStateWithCompletion:
+ _objc_msgSend$rawValue
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$stateInContext:completion:
+ _objc_msgSend$stateWithCompletion:
+ _objc_msgSend$userCustomCancelErrorWithUserInfo:
+ _sharedInstance.sharedInstance
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.114
- ___block_literal_global.213
CStrings:
+ "%ds"
+ "%s context:%{public}@ options:%{public}@"
+ "%s finished with error: %{public}@"
+ "%s finished with result: %{public}@, error: %{public}@"
+ "%s finished with state: %{public}@"
+ "%s identifier:%{public}@, reason:%{public}@"
+ "%s returned %s"
+ "%s returned %{public}@"
+ "-[LARatchetManager addObserver:]"
+ "-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]"
+ "-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke"
+ "-[LARatchetManager checkCanEnableFeatureWithCompletion:]"
+ "-[LARatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke"
+ "-[LARatchetManager disableFeatureWithContext:completion:]"
+ "-[LARatchetManager disableFeatureWithContext:completion:]_block_invoke"
+ "-[LARatchetManager enableFeatureWithReply:]"
+ "-[LARatchetManager enableFeatureWithReply:]_block_invoke"
+ "-[LARatchetManager isFeatureAvailable]"
+ "-[LARatchetManager isFeatureEnabled]"
+ "-[LARatchetManager isFeatureSupported]"
+ "-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]"
+ "-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]_block_invoke"
+ "-[LARatchetManager ratchetState]"
+ "-[LARatchetManager removeObserver:]"
+ "-[LARatchetManager stateInContext:completion:]"
+ "-[LARatchetManager stateInContext:completion:]_block_invoke"
+ "-[LARatchetManager stateWithCompletion:]"
+ "-[LARatchetManager stateWithCompletion:]_block_invoke"
+ "; "
+ "<%@ %p; %@>"
+ "@\"<LACDTOServiceXPCClient>\""
+ "@\"<LACDarwinNotificationCenter>\""
+ "@\"LARatchetManager\""
+ "@\"LARatchetStateValue\""
+ "@\"NSXPCListenerEndpoint\"24@0:8^@16"
+ "@24@0:8d16"
+ "@40@0:8q16@24@32"
+ "Collapsed"
+ "INF"
+ "LACDTOServiceXPCEndpointProvider"
+ "LACDarwinNotificationCenterObserver"
+ "LARatchet"
+ "LARatchetEndpointProvider"
+ "LARatchetErrorBuilder"
+ "LARatchetManager"
+ "LARatchetState"
+ "LARatchetStateValue"
+ "LARatchetStateValueArmed"
+ "LARatchetStateValueCollapsed"
+ "LARatchetStateValueExpired"
+ "LARatchetStateValueNotStarted"
+ "LARatchetStateValueReady"
+ "LARatchetStateValueWaitingForCoolOff"
+ "LARatchetStateValueWaitingForSecondAuthentication"
+ "NotStarted"
+ "Platform not supported"
+ "Ratchet not ready"
+ "RatchetState"
+ "Ready"
+ "T@\"LARatchetState\",R,N"
+ "T@\"LARatchetStateValue\",R,N,V_value"
+ "T@\"NSString\",R,N,V_uuid"
+ "Td,R,N"
+ "This method has been deprecated"
+ "Tq,R,N,V_rawValue"
+ "WaitingForCoolOff"
+ "WaitingForSecondAuthentication"
+ "Will notify %d observers about new state: %{public}@"
+ "_armPolicy"
+ "_duration"
+ "_errorWithCode:debugDescription:"
+ "_errorWithCode:userInfo:"
+ "_notificationCenter"
+ "_optionForRatchetOption:"
+ "_performArmRequestWithIdentifier:context:options:completion:"
+ "_ratchetManager"
+ "_rawValue"
+ "_remoteObjectProxyWithErrorHandler:"
+ "addObserver:notification:"
+ "armWithOptions:completion:"
+ "beforeFirstUnlockWithUserInfo:"
+ "biometryNotEnrolledWithUserInfo:"
+ "cancelArmRequestWithIdentifier:reason:completion:"
+ "cancelCurrentRatchetWithReason:completion:"
+ "cancelPendingEvaluationWithRatchetIdentifier:reason:completion:"
+ "cancelWithReason:completion:"
+ "checkCanEnableFeatureWithCompletion:"
+ "com.apple.LocalAuthentication.LARatchetErrorDomain"
+ "com.apple.LocalAuthentication.ratchet.StateDidChange"
+ "com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag"
+ "com.apple.private.LocalAuthentication.Storage.SetDSLMode"
+ "com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled"
+ "componentsJoinedByString:"
+ "currentRatchetWithCompletion:"
+ "disableFeatureWithContext:completion:"
+ "duration"
+ "duration: %@"
+ "enableFeatureWithCompletion:"
+ "enableFeatureWithReply:"
+ "endpoint:"
+ "error:hasCode:subcode:"
+ "errorNotArmedWithRatchetState:"
+ "genericErrorWithDebugDescription:"
+ "genericErrorWithUnderlyingError:"
+ "hasObserver:"
+ "initInternal"
+ "initWithDuration:"
+ "initWithEndpointProvider:"
+ "initWithIdentifier:"
+ "initWithRawValue:value:uuid:"
+ "initWithState:"
+ "isFeatureAvailable"
+ "isFeatureEnabled"
+ "isFeatureEnabled returned %s"
+ "isFeatureSupported"
+ "isRatchetFeatureEnabled"
+ "kLAServiceTypeRatchet"
+ "notInteractiveErrorWithUserInfo:"
+ "notificationCenter:didReceiveNotification:"
+ "optionAuthenticationCallbackReason"
+ "optionAuthenticationCallbackURL"
+ "optionAuthenticationIdentifier"
+ "optionBeginRatchetLocalizedText"
+ "optionBeginRatchetLocalizedTitle"
+ "optionBeginRatchetShowsLocationWarning"
+ "optionBeginSecurityDelayImmediately"
+ "optionCountdownLocalizedText"
+ "optionDTO"
+ "optionFallbackToNoAuthentication"
+ "optionNoCountdownUI"
+ "optionUseShortExpirationTimer"
+ "passcodeNotSetWithUserInfo:"
+ "performArmRequestWithIdentifier:context:options:completion:"
+ "q24@0:8q16"
+ "ratchetErrorWithError:"
+ "ratchetState"
+ "ratchetStateDidChange:"
+ "ratchetStateWithCompletion:"
+ "rawValue"
+ "rawValue: %@"
+ "removeObserver:"
+ "reset"
+ "setOptionAuthenticationCallbackReason:"
+ "setOptionAuthenticationCallbackURL:"
+ "setOptionAuthenticationIdentifier:"
+ "setOptionBeginRatchetLocalizedText:"
+ "setOptionBeginRatchetLocalizedTitle:"
+ "setOptionBeginRatchetShowsLocationWarning:"
+ "setOptionBeginSecurityDelayImmediately:"
+ "setOptionCountdownLocalizedText:"
+ "setOptionDTO:"
+ "setOptionFallbackToNoAuthentication:"
+ "setOptionNoCountdownUI:"
+ "setOptionUseShortExpirationTimer:"
+ "stateInContext:completion:"
+ "stateWithCompletion:"
+ "userCustomCancelErrorWithUserInfo:"
+ "uuid: %@"
+ "v24@?0@\"LACDTORatchetState\"8@\"NSError\"16"
+ "v24@?0@\"LARatchetState\"8@\"NSError\"16"
+ "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
+ "v32@0:8@16^{__CFString=}24"

```
