## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/Versions/A/MechanismBase`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x12a70
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x10c4
-  __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__cstring: 0xca1
-  __TEXT.__oslogstring: 0xaa2
+1656.100.223.0.0
+  __TEXT.__text: 0x13a98
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x142c
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x354
+  __TEXT.__cstring: 0xcaf
+  __TEXT.__oslogstring: 0xada
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x588
-  __TEXT.__objc_classname: 0x272
-  __TEXT.__objc_methname: 0x30b8
-  __TEXT.__objc_methtype: 0xa19
-  __TEXT.__objc_stubs: 0x21c0
-  __DATA_CONST.__got: 0x198
+  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__objc_classname: 0x282
+  __TEXT.__objc_methname: 0x334b
+  __TEXT.__objc_methtype: 0xa72
+  __TEXT.__objc_stubs: 0x23c0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb38
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x3f18
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__const: 0x8f0
+  __AUTH_CONST.__cfstring: 0xaa0
+  __AUTH_CONST.__objc_const: 0x35a0
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x1f8
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0x420
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F94758F2-3774-348E-B626-716C642F4EAA
-  Functions: 468
-  Symbols:   1297
-  CStrings:  1014
+  UUID: E8C93435-0766-30AB-98B3-B95FC1148E41
+  Functions: 485
+  Symbols:   1345
+  CStrings:  1051
 
Symbols:
+ +[MechanismContext sharedInstance].cold.1
+ +[RemoteUIManager sharedInstance].cold.1
+ -[MechanismBase _eventWithParams:reply:]
+ -[MechanismBase canRecoverFromAvailabilityError:request:]
+ -[MechanismBase instanceId]
+ -[MechanismBase responseEventWithParams:timeout:reply:]
+ -[MechanismBaseComposite .cxx_destruct]
+ -[MechanismBaseComposite canRecoverFromAvailabilityError:request:]
+ -[MechanismBaseComposite initWithEventIdentifier:remoteViewController:k:ofSubmechanisms:request:]
+ -[MechanismBaseComposite isAND]
+ -[MechanismBaseComposite isAvailableForPurpose:error:]
+ -[MechanismBaseComposite isOR]
+ -[MechanismBaseComposite k]
+ -[MechanismBaseComposite n]
+ -[MechanismBaseComposite setAND:]
+ -[MechanismBaseComposite setK:]
+ -[MechanismBaseComposite setN:]
+ -[MechanismBaseComposite setOR:]
+ -[MechanismBaseComposite setSubmechanisms:]
+ -[MechanismBaseComposite submechanisms]
+ -[MechanismBiometry canRecoverFromAvailabilityError:request:]
+ -[MechanismBiometry checkLockoutState:isEffectiveLockoutForMatchWithPurpose:]
+ -[MechanismTouchIDWatch pause:forEvent:error:].cold.1
+ -[MechanismUI checkHasPendingUIRequestsWithCompletion:]
+ -[MechanismUI connectRemoteUI:requestID:reply:]
+ -[MechanismUI connectRemoteUI:requestID:reply:].cold.1
+ -[MechanismUI connectRemoteUI:requestID:reply:].cold.2
+ -[RemoteUIManager checkHasPendingUIRequestsWithCompletion:]
+ -[RemoteUIManager connectRemoteUI:requestID:reply:]
+ -[RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]
+ -[RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]
+ -[RemoteUIParams identifier]
+ -[RemoteUIParams requestID]
+ -[RemoteUIParams setRequestID:]
+ -[_RemoteUIManager _assignPendingRequest:reply:]
+ -[_RemoteUIManager checkHasPendingUIRequestsWithCompletion:]
+ -[_RemoteUIManager connectRemoteUI:requestID:reply:]
+ -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]
+ -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:].cold.1
+ -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:].cold.2
+ -[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]
+ GCC_except_table45
+ GCC_except_table62
+ GCC_except_table75
+ GCC_except_table83
+ LA_LOG_MechanismKofN.cold.1
+ LA_LOG_MechanismUI.cold.1
+ OBJC_IVAR_$_MechanismBaseComposite._AND
+ OBJC_IVAR_$_MechanismBaseComposite._OR
+ OBJC_IVAR_$_MechanismBaseComposite._k
+ OBJC_IVAR_$_MechanismBaseComposite._n
+ OBJC_IVAR_$_MechanismBaseComposite._submechanisms
+ OBJC_IVAR_$_MechanismUI._remoteUIShouldIdle
+ OBJC_IVAR_$_RemoteUIParams._requestID
+ OBJC_IVAR_$__RemoteUIManager._request
+ _LACErrorCancelledByHigherPriorityAuthenticationKey
+ _LACErrorCodeInternal
+ _LACErrorSubcodeInterruptedByAnotherEvaluation
+ _LACErrorSubcodeRequestMismatch
+ _LACEvaluationRequestPayloadKeyConcurrentIdleUIListener
+ _LACPolicyOptionAHPMode
+ _LACPolicyOptionBiometryLockoutRecovery
+ _LACPolicyOptionBiometryLockoutRecoveryRetries
+ _LACPolicyOptionDisableConcurrentEvaluation
+ _LACPolicyOptionFallbackVisible
+ _NSDictionaryWithDescriptionFromLACEventParams
+ _NSStringFromLACEvent
+ _OBJC_CLASS_$_LACBackgroundTask
+ _OBJC_CLASS_$_LACBackgroundTaskResult
+ _OBJC_CLASS_$_LACConcurrentEvaluationHelper
+ _OBJC_CLASS_$_MechanismBaseComposite
+ _OBJC_METACLASS_$_MechanismBaseComposite
+ __35-[MechanismUI uiSuccessWithResult:]_block_invoke.62
+ __39-[RemoteUIActivator _connectToUIAgent:]_block_invoke.22
+ __39-[RemoteUIActivator _connectToUIAgent:]_block_invoke.22.cold.1
+ __42-[RemoteUIActivator activateUIWithParams:]_block_invoke.10
+ __42-[RemoteUIActivator activateUIWithParams:]_block_invoke.10.cold.1
+ __52-[MechanismUI _transitionToController:internalInfo:]_block_invoke.127
+ __52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke.140
+ __55-[MechanismBase responseEventWithParams:timeout:reply:]_block_invoke.151
+ __79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.113
+ __79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.118
+ __79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.122
+ __79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_MechanismBaseComposite
+ __OBJC_$_INSTANCE_VARIABLES_MechanismBaseComposite
+ __OBJC_$_PROP_LIST_MechanismBaseComposite
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACRemoteUIHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUIMechanism
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACRemoteUIHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUIMechanism
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_REFS_LACUIMechanism
+ __OBJC_CLASS_PROTOCOLS_$_MechanismBaseComposite
+ __OBJC_CLASS_RO_$_MechanismBaseComposite
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteUIHost
+ __OBJC_LABEL_PROTOCOL_$_LACUIMechanism
+ __OBJC_METACLASS_RO_$_MechanismBaseComposite
+ __OBJC_PROTOCOL_$_LACContextExternalizing
+ __OBJC_PROTOCOL_$_LACRemoteUIHost
+ __OBJC_PROTOCOL_$_LACUIMechanism
+ ___51-[RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke
+ ___52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke
+ ___55-[MechanismBase responseEventWithParams:timeout:reply:]_block_invoke
+ ___55-[MechanismBase responseEventWithParams:timeout:reply:]_block_invoke_2
+ ___59-[RemoteUIManager checkHasPendingUIRequestsWithCompletion:]_block_invoke
+ ___73-[RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:]_block_invoke
+ ___78-[RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke
+ ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke
+ ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_48_e8_32bs40w_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24l
+ ___block_descriptor_48_e8_32r40w_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"LACBackgroundTaskResult"8l
+ ___block_descriptor_48_e8_32s40bs_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24l
+ ___block_descriptor_48_e8_32s40w_e40_v16?0?<v?"LACBackgroundTaskResult">8l
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0l
+ ___block_descriptor_66_e8_32s40s48bs56w_e5_v8?0l
+ ___copy_helper_block_e8_32r40w
+ ___destroy_helper_block_e8_32r40w
+ __block_literal_global.13
+ __block_literal_global.131
+ __block_literal_global.172
+ __block_literal_global.249
+ _objc_msgSend$_assignPendingRequest:reply:
+ _objc_msgSend$_eventWithParams:reply:
+ _objc_msgSend$analyticsData
+ _objc_msgSend$anonymousListenerWithIdentifier:
+ _objc_msgSend$authenticationRequirementsForUIController:
+ _objc_msgSend$canRecoverFromAvailabilityError:request:
+ _objc_msgSend$checkHasPendingUIRequestsWithCompletion:
+ _objc_msgSend$connectRemoteUI:requestID:reply:
+ _objc_msgSend$connectionToViewServiceInvalidatedForIdentifier:reply:
+ _objc_msgSend$daemonQueue
+ _objc_msgSend$dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:
+ _objc_msgSend$dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:
+ _objc_msgSend$error
+ _objc_msgSend$errorWithCode:subcode:debugDescription:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithError:
+ _objc_msgSend$initWithValue:
+ _objc_msgSend$initWithWorker:
+ _objc_msgSend$instanceId
+ _objc_msgSend$isConcurrentEvaluationEnabled
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$payload
+ _objc_msgSend$requestID
+ _objc_msgSend$runWithTimeout:queue:completion:
+ _objc_msgSend$setRequestID:
+ _objc_msgSend$userInfo
+ _objc_msgSend$value
- -[MechanismBase canRecoverFromError:request:]
- -[MechanismBiometry canRecoverFromError:request:]
- -[MechanismKofN canRecoverFromError:request:]
- -[MechanismKofN initWithK:ofSubmechanisms:serial:request:].cold.1
- -[MechanismKofN isAND]
- -[MechanismKofN isOR]
- -[MechanismKofN k]
- -[MechanismKofN n]
- -[MechanismKofN submechanisms]
- -[MechanismTouchIDWatch isAND]
- -[MechanismTouchIDWatch isOR]
- -[MechanismTouchIDWatch k]
- -[MechanismTouchIDWatch n]
- -[MechanismTouchIDWatch submechanisms]
- -[MechanismUI _authenticationRequirementsForMechanism:uiController:]
- -[MechanismUI checkClearForIdleExitWithCompletion:]
- -[MechanismUI connectRemoteUI:reply:]
- -[MechanismUI connectRemoteUI:reply:].cold.1
- -[RemoteUIManager checkClearForIdleExitWithCompletion:]
- -[RemoteUIManager connectRemoteUI:reply:]
- -[RemoteUIManager connectionToViewServiceInvalidated:]
- -[RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]
- -[_RemoteUIManager _assignPendingMechanism:reply:]
- -[_RemoteUIManager checkClearForIdleExitWithCompletion:]
- -[_RemoteUIManager connectRemoteUI:reply:]
- -[_RemoteUIManager connectionToViewServiceInvalidated:]
- -[_RemoteUIManager connectionToViewServiceInvalidated:].cold.1
- -[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]
- GCC_except_table53
- GCC_except_table66
- GCC_except_table74
- OBJC_IVAR_$_MechanismKofN.AND
- OBJC_IVAR_$_MechanismKofN.OR
- OBJC_IVAR_$_MechanismKofN.k
- OBJC_IVAR_$_MechanismKofN.n
- OBJC_IVAR_$_MechanismKofN.submechanisms
- OBJC_IVAR_$_MechanismTouchIDWatch.AND
- OBJC_IVAR_$_MechanismTouchIDWatch.OR
- OBJC_IVAR_$_MechanismTouchIDWatch.k
- OBJC_IVAR_$_MechanismTouchIDWatch.n
- OBJC_IVAR_$_MechanismTouchIDWatch.submechanisms
- OBJC_IVAR_$__RemoteUIManager._uiMechanism
- _OBJC_CLASS_$_Request
- __35-[MechanismUI uiSuccessWithResult:]_block_invoke.57
- __39-[RemoteUIActivator _connectToUIAgent:]_block_invoke.19
- __39-[RemoteUIActivator _connectToUIAgent:]_block_invoke.19.cold.1
- __42-[RemoteUIActivator activateUIWithParams:]_block_invoke.7
- __42-[RemoteUIActivator activateUIWithParams:]_block_invoke.7.cold.1
- __42-[_RemoteUIManager connectRemoteUI:reply:]_block_invoke.135
- __52-[MechanismUI _transitionToController:internalInfo:]_block_invoke.117
- __68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.108
- __68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.113
- __68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.117
- __68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke.cold.1
- __OBJC_$_PROP_LIST_MechanismTouchIDWatch
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LARemoteUIHost
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAUIMechanism
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_METHOD_TYPES_LARemoteUIHost
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAUIMechanism
- __OBJC_$_PROTOCOL_REFS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_REFS_LAUIMechanism
- __OBJC_CLASS_PROTOCOLS_$_MechanismKofN
- __OBJC_CLASS_PROTOCOLS_$_MechanismTouchIDWatch
- __OBJC_LABEL_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_LABEL_PROTOCOL_$_LARemoteUIHost
- __OBJC_LABEL_PROTOCOL_$_LAUIMechanism
- __OBJC_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_PROTOCOL_$_LARemoteUIHost
- __OBJC_PROTOCOL_$_LAUIMechanism
- ___41-[RemoteUIManager connectRemoteUI:reply:]_block_invoke
- ___42-[_RemoteUIManager connectRemoteUI:reply:]_block_invoke
- ___54-[RemoteUIManager connectionToViewServiceInvalidated:]_block_invoke
- ___55-[RemoteUIManager checkClearForIdleExitWithCompletion:]_block_invoke
- ___56-[_RemoteUIManager checkClearForIdleExitWithCompletion:]_block_invoke
- ___67-[RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke
- ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke
- ___68-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:reply:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40w_e60_v32?0"<LAUIMechanism>"8"<LABackoffCounter>"16"NSError"24l
- ___block_descriptor_48_e8_32s40bs_e60_v32?0"<LAUIMechanism>"8"<LABackoffCounter>"16"NSError"24l
- ___block_descriptor_48_e8_32s40s_e14_"NSError"8?0l
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0l
- __block_literal_global.10
- __block_literal_global.126
- __block_literal_global.164
- __block_literal_global.246
- _objc_msgSend$_assignPendingMechanism:reply:
- _objc_msgSend$_authenticationRequirementsForMechanism:uiController:
- _objc_msgSend$canRecoverFromError:request:
- _objc_msgSend$checkClearForIdleExitWithCompletion:
- _objc_msgSend$connectRemoteUI:reply:
- _objc_msgSend$connectionToViewServiceInvalidated:
- _objc_msgSend$current
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$dismissRemoteUI:uiMechanism:uiDisappeared:reply:
- _objc_msgSend$dismissRemoteUIWasInvalidated:completionHandler:
- _objc_msgSend$errorNotSupported
- _objc_msgSend$interactive
CStrings:
+ "$"
+ "%u-%u"
+ "-[MechanismUI connectRemoteUI:requestID:reply:]"
+ "@\"<LACBackoffCounter>\""
+ "@\"<LACContextExternalizing>\""
+ "@\"<LACRemoteUI>\""
+ "@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\""
+ "@\"RemoteUIParams\""
+ "@56@0:8q16q24Q32@40@48"
+ "B32@0:8q16q24"
+ "Connection failed with error %{public}@"
+ "Current request identifier: %u is different from the connection identifier: %@"
+ "LACContextExternalizing"
+ "LACRemoteUIHost"
+ "LACUIMechanism"
+ "MechanismBaseComposite"
+ "Q\x81A\""
+ "Request mismatch: %@ != %@"
+ "RequestId"
+ "Sending custom UI event %d (%@) with params: %{public}@"
+ "T@\"<LACBackoffCounter>\",&,N,V_backoffCounter"
+ "T@\"<LACContextExternalizing>\",R,W,N,V_cachedExternalizationDelegate"
+ "T@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\",&,N,V_uiMechanism"
+ "T@\"NSArray\",&,N,V_submechanisms"
+ "T@\"NSString\",R,N"
+ "TB,N,GisAND,V_AND"
+ "TB,N,GisOR,V_OR"
+ "TI,N,V_requestID"
+ "TI,R,N,V_instanceId"
+ "TQ,N,V_k"
+ "TQ,N,V_n"
+ "_AND"
+ "_OR"
+ "_assignPendingRequest:reply:"
+ "_eventWithParams:reply:"
+ "_n"
+ "_remoteUIShouldIdle"
+ "_requestID"
+ "_submechanisms"
+ "analyticsData"
+ "anonymousListenerWithIdentifier:"
+ "authenticationRequirementsForUIController:"
+ "canRecoverFromAvailabilityError:request:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "checkLockoutState:isEffectiveLockoutForMatchWithPurpose:"
+ "connectRemoteUI:requestID:reply:"
+ "connectionToViewServiceInvalidatedForIdentifier: %@"
+ "connectionToViewServiceInvalidatedForIdentifier:reply:"
+ "daemonQueue"
+ "dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:"
+ "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
+ "error"
+ "errorWithCode:subcode:debugDescription:"
+ "identifier"
+ "initWithError:"
+ "initWithEventIdentifier:remoteViewController:k:ofSubmechanisms:request:"
+ "initWithValue:"
+ "initWithWorker:"
+ "instanceId"
+ "isConcurrentEvaluationEnabled"
+ "isEqualToString:"
+ "numberWithUnsignedInt:"
+ "payload"
+ "requestID"
+ "responseEventWithParams:timeout:reply:"
+ "runWithTimeout:queue:completion:"
+ "setAND:"
+ "setK:"
+ "setN:"
+ "setOR:"
+ "setRequestID:"
+ "setSubmechanisms:"
+ "userInfo"
+ "v16@?0@\"LACBackgroundTaskResult\"8"
+ "v16@?0@?<v@?@\"LACBackgroundTaskResult\">8"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v32@0:8@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@?0@\"<LACUIMechanism>\"8@\"<LACBackoffCounter>\"16@\"NSError\"24"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v40@0:8@16d24@?32"
+ "v48@0:8@\"<LACRemoteUI>\"16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24B32B36@?<v@?>40"
+ "v48@0:8@16@24B32B36@?40"
+ "value"
- "%@ is pending"
- "%@ is running"
- "-[MechanismUI connectRemoteUI:reply:]"
- "@\"<LABackoffCounter>\""
- "@\"<LAContextExternalizationProt>\""
- "@\"<LARemoteUI>\""
- "@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\""
- "@\"NSError\"8@?0"
- "LAContextExternalizationProt"
- "LARemoteUIHost"
- "LAUIMechanism"
- "Not clear for idle exit because %@."
- "Sending custom UI event %d with params: %{public}@"
- "T@\"<LABackoffCounter>\",&,N,V_backoffCounter"
- "T@\"<LAContextExternalizationProt>\",R,W,N,V_cachedExternalizationDelegate"
- "T@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\",&,N,V_uiMechanism"
- "T@\"NSArray\",R,N,Vsubmechanisms"
- "TB,R,N,GisAND,VAND"
- "TB,R,N,GisOR,VOR"
- "TQ,R,N,Vk"
- "TQ,R,N,Vn"
- "UI idle-exit check failed: %{public}@"
- "UI idle-exit check: clear for %.0f ms (%@, %@)"
- "_assignPendingMechanism:reply:"
- "_authenticationRequirementsForMechanism:uiController:"
- "aqA\""
- "canRecoverFromError:request:"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "connectionToViewServiceInvalidated"
- "connectionToViewServiceInvalidated:"
- "current"
- "dateWithTimeIntervalSinceNow:"
- "dismissRemoteUI:uiMechanism:uiDisappeared:reply:"
- "dismissRemoteUIWasInvalidated:completionHandler:"
- "errorNotSupported"
- "interactive"
- "of a new interactive request from %@"
- "q32@0:8@16q24"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v32@0:8@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\"16@?<v@?B@\"NSError\">24"
- "v32@?0@\"<LAUIMechanism>\"8@\"<LABackoffCounter>\"16@\"NSError\"24"
- "v44@0:8@\"<LARemoteUI>\"16@\"MechanismUI<LAUIMechanism><LARemoteUIHost>\"24B32@?<v@?>36"
- "v44@0:8@16@24B32@?36"

```
