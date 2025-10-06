## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0xa6d4
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xbec
+1394.62.1.0.0
+  __TEXT.__text: 0xd244
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0xe7c
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x769
-  __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x38c
-  __TEXT.__objc_classname: 0x171
-  __TEXT.__objc_methname: 0x2749
-  __TEXT.__objc_methtype: 0x86d
-  __TEXT.__objc_stubs: 0x1900
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x3a8
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__cstring: 0xa43
+  __TEXT.__oslogstring: 0xccd
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__objc_classname: 0x1f7
+  __TEXT.__objc_methname: 0x2e82
+  __TEXT.__objc_methtype: 0x8e0
+  __TEXT.__objc_stubs: 0x1f80
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b98
-  __DATA_CONST.__objc_selrefs: 0x8e0
+  __DATA_CONST.__objc_const: 0x1f40
+  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x4c8
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x160
+  __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_classrefs: 0x138
+  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50A48D07-DE2E-3D57-ADE9-5656BF7E7ADA
-  Functions: 301
-  Symbols:   1192
-  CStrings:  788
+  UUID: 556B2537-3C18-3FAF-A4B1-A55464C80CC7
+  Functions: 368
+  Symbols:   1449
+  CStrings:  941
 
Symbols:
+ -[MechanismAssertion additionalDescription]
+ -[MechanismAssertionClientProcessVisible .cxx_destruct]
+ -[MechanismAssertionClientProcessVisible _assertInStateWithProcessState:]
+ -[MechanismAssertionClientProcessVisible _assertInStateWithProcessState:].cold.1
+ -[MechanismAssertionClientProcessVisible _assertInStateWithProcessState:].cold.2
+ -[MechanismAssertionClientProcessVisible _callerName]
+ -[MechanismAssertionClientProcessVisible _configureMonitor:]
+ -[MechanismAssertionClientProcessVisible _handleStateUpdate:monitor:process:]
+ -[MechanismAssertionClientProcessVisible _handleStateUpdate:monitor:process:].cold.1
+ -[MechanismAssertionClientProcessVisible _handleStateUpdate:monitor:process:].cold.2
+ -[MechanismAssertionClientProcessVisible _rbsProcessHandleWithError:]
+ -[MechanismAssertionClientProcessVisible _rbsStateDescriptor]
+ -[MechanismAssertionClientProcessVisible _setupProcessHandle]
+ -[MechanismAssertionClientProcessVisible _setupProcessHandle].cold.1
+ -[MechanismAssertionClientProcessVisible assertInState]
+ -[MechanismAssertionClientProcessVisible assertInState].cold.1
+ -[MechanismAssertionClientProcessVisible initWithMechanism:trackedBundleID:trackedPID:]
+ -[MechanismAssertionClientProcessVisible startMonitoring]
+ -[MechanismAssertionClientProcessVisible stopMonitoring]
+ -[MechanismAssertionHolding .cxx_destruct]
+ -[MechanismAssertionHolding additionalDescription]
+ -[MechanismAssertionHolding dropWithReason:]
+ -[MechanismAssertionHolding initWithMechanism:object:]
+ -[MechanismAssertionHolding object]
+ -[MechanismAssertionWithDarwinNotifications .cxx_destruct]
+ -[MechanismAssertionWithDarwinNotifications _notificationNameForInState:]
+ -[MechanismAssertionWithDarwinNotifications _notificationTokenForInState:]
+ -[MechanismAssertionWithDarwinNotifications _registerDarwinNotificationForInState:]
+ -[MechanismAssertionWithDarwinNotifications _registerDarwinNotificationForInState:].cold.1
+ -[MechanismAssertionWithDarwinNotifications _unregisterDarwinNotificationForInstate:]
+ -[MechanismAssertionWithDarwinNotifications assertInState]
+ -[MechanismAssertionWithDarwinNotifications handleAssertionFailureWithReason:error:]
+ -[MechanismAssertionWithDarwinNotifications handleAssertionSuccessWithReason:]
+ -[MechanismAssertionWithDarwinNotifications inStateNotificationName]
+ -[MechanismAssertionWithDarwinNotifications initWithMechanism:inStateNotificationName:outStateNotificationName:]
+ -[MechanismAssertionWithDarwinNotifications outStateNotificationName]
+ -[MechanismAssertionWithDarwinNotifications startMonitoring]
+ -[MechanismAssertionWithDarwinNotifications stopMonitoring]
+ -[MechanismBase _acquireAssertionsWithReason:error:]
+ -[MechanismBase _dropAssertionsWithReason:]
+ -[MechanismBase addAssertion:]
+ -[MechanismBase canRecoverFromError:request:]
+ -[MechanismBase failureLimit]
+ -[MechanismBase failuresInfoDictionaryWithError:]
+ -[MechanismBase failures]
+ -[MechanismBase handleUIEvent:params:]
+ -[MechanismBase maxGlobalCredentialAge]
+ -[MechanismBase setFailureLimit:]
+ -[MechanismBase setFailures:]
+ -[MechanismBase willTryToRecover]
+ -[MechanismBiometry biolockout]
+ -[MechanismBiometry canRecoverFromError:request:]
+ -[MechanismBiometry isFallbackVisible]
+ -[MechanismBiometry setBiolockout:]
+ -[MechanismBiometry willTryToRecover]
+ -[MechanismKofN canRecoverFromError:request:]
+ -[MechanismKofN mechanismPruningMechanismsWithEventIdentifier:]
+ -[RemoteUIActivator _activateFrontBoardUIWithParams:]
+ -[RemoteUIActivator _activateFrontBoardUIWithParams:].cold.1
+ -[RemoteUIActivator _activateSpringBoardUIWithParams:]
+ GCC_except_table46
+ GCC_except_table6
+ GCC_except_table9
+ _FBSOpenApplicationOptionKeyActivateSuspended
+ _FBSOpenApplicationOptionKeyLaunchIntent
+ _FBSOpenApplicationOptionKeyPayloadURL
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _FBSOpenApplicationOptionKeyUnlockDevice
+ _FBSOpenApplicationWithNewScene
+ _OBJC_CLASS_$_FBSOpenApplicationOptions
+ _OBJC_CLASS_$_FBSOpenApplicationService
+ _OBJC_CLASS_$_LACMobileGestalt
+ _OBJC_CLASS_$_LAUtils
+ _OBJC_CLASS_$_MechanismAssertionClientProcessVisible
+ _OBJC_CLASS_$_MechanismAssertionHolding
+ _OBJC_CLASS_$_MechanismAssertionWithDarwinNotifications
+ _OBJC_CLASS_$_MechanismBiometry
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _OBJC_IVAR_$_MechanismAssertionClientProcessVisible._bundleID
+ _OBJC_IVAR_$_MechanismAssertionClientProcessVisible._monitor
+ _OBJC_IVAR_$_MechanismAssertionClientProcessVisible._pid
+ _OBJC_IVAR_$_MechanismAssertionClientProcessVisible._processHandle
+ _OBJC_IVAR_$_MechanismAssertionClientProcessVisible._processHandleError
+ _OBJC_IVAR_$_MechanismAssertionHolding._object
+ _OBJC_IVAR_$_MechanismAssertionWithDarwinNotifications._inStateNotificationName
+ _OBJC_IVAR_$_MechanismAssertionWithDarwinNotifications._inStateToken
+ _OBJC_IVAR_$_MechanismAssertionWithDarwinNotifications._isInState
+ _OBJC_IVAR_$_MechanismAssertionWithDarwinNotifications._outStateNotificationName
+ _OBJC_IVAR_$_MechanismAssertionWithDarwinNotifications._outStateToken
+ _OBJC_IVAR_$_MechanismBase._failureLimit
+ _OBJC_IVAR_$_MechanismBase._failures
+ _OBJC_IVAR_$_MechanismBase._maxGlobalCredentialAge
+ _OBJC_IVAR_$_MechanismBiometry._biolockout
+ _OBJC_METACLASS_$_MechanismAssertionClientProcessVisible
+ _OBJC_METACLASS_$_MechanismAssertionHolding
+ _OBJC_METACLASS_$_MechanismAssertionWithDarwinNotifications
+ _OBJC_METACLASS_$_MechanismBiometry
+ __OBJC_$_INSTANCE_METHODS_MechanismAssertionClientProcessVisible
+ __OBJC_$_INSTANCE_METHODS_MechanismAssertionHolding
+ __OBJC_$_INSTANCE_METHODS_MechanismAssertionWithDarwinNotifications
+ __OBJC_$_INSTANCE_METHODS_MechanismBiometry
+ __OBJC_$_INSTANCE_VARIABLES_MechanismAssertionClientProcessVisible
+ __OBJC_$_INSTANCE_VARIABLES_MechanismAssertionHolding
+ __OBJC_$_INSTANCE_VARIABLES_MechanismAssertionWithDarwinNotifications
+ __OBJC_$_INSTANCE_VARIABLES_MechanismBiometry
+ __OBJC_$_PROP_LIST_MechanismAssertionHolding
+ __OBJC_$_PROP_LIST_MechanismAssertionWithDarwinNotifications
+ __OBJC_$_PROP_LIST_MechanismBiometry
+ __OBJC_CLASS_RO_$_MechanismAssertionClientProcessVisible
+ __OBJC_CLASS_RO_$_MechanismAssertionHolding
+ __OBJC_CLASS_RO_$_MechanismAssertionWithDarwinNotifications
+ __OBJC_CLASS_RO_$_MechanismBiometry
+ __OBJC_METACLASS_RO_$_MechanismAssertionClientProcessVisible
+ __OBJC_METACLASS_RO_$_MechanismAssertionHolding
+ __OBJC_METACLASS_RO_$_MechanismAssertionWithDarwinNotifications
+ __OBJC_METACLASS_RO_$_MechanismBiometry
+ ___53-[RemoteUIActivator _activateFrontBoardUIWithParams:]_block_invoke
+ ___57-[MechanismAssertionClientProcessVisible startMonitoring]_block_invoke
+ ___60-[MechanismAssertionClientProcessVisible _configureMonitor:]_block_invoke
+ ___60-[MechanismAssertionClientProcessVisible _configureMonitor:]_block_invoke_2
+ ___63-[MechanismKofN mechanismPruningMechanismsWithEventIdentifier:]_block_invoke
+ ___63-[MechanismKofN mechanismPruningMechanismsWithEventIdentifier:]_block_invoke_2
+ ___83-[MechanismAssertionWithDarwinNotifications _registerDarwinNotificationForInState:]_block_invoke
+ ___block_descriptor_40_e8_32w_e40_v16?0"<RBSProcessMonitorConfiguring>"8lw32l8
+ ___block_descriptor_40_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
+ ___block_descriptor_48_e8_32s40s_e20_"MechanismBase"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_q8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40w_e8_v12?0i8lw40l8s32l8
+ __unnamed_array_storage
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_acquireAssertionsWithReason:error:
+ _objc_msgSend$_activateFrontBoardUIWithParams:
+ _objc_msgSend$_activateSpringBoardUIWithParams:
+ _objc_msgSend$_assertInStateWithProcessState:
+ _objc_msgSend$_callerName
+ _objc_msgSend$_configureMonitor:
+ _objc_msgSend$_dropAssertionsWithReason:
+ _objc_msgSend$_handleStateUpdate:monitor:process:
+ _objc_msgSend$_notificationNameForInState:
+ _objc_msgSend$_notificationTokenForInState:
+ _objc_msgSend$_rbsProcessHandleWithError:
+ _objc_msgSend$_rbsStateDescriptor
+ _objc_msgSend$_registerDarwinNotificationForInState:
+ _objc_msgSend$_setupProcessHandle
+ _objc_msgSend$_unregisterDarwinNotificationForInstate:
+ _objc_msgSend$acquireWithReason:error:
+ _objc_msgSend$additionalDescription
+ _objc_msgSend$canRecoverFromError:request:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$currentState
+ _objc_msgSend$descriptor
+ _objc_msgSend$dispatchOnServer:
+ _objc_msgSend$endowmentNamespaces
+ _objc_msgSend$firstObject
+ _objc_msgSend$handleForIdentifier:error:
+ _objc_msgSend$handleForPredicate:error:
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$inStateNotificationName
+ _objc_msgSend$invalidate
+ _objc_msgSend$isAND
+ _objc_msgSend$isFallbackVisible
+ _objc_msgSend$matchesProcess:
+ _objc_msgSend$mechanismPruningMechanismsWithEventIdentifier:
+ _objc_msgSend$monitorWithConfiguration:
+ _objc_msgSend$openApplication:withOptions:completion:
+ _objc_msgSend$options
+ _objc_msgSend$optionsWithDictionary:
+ _objc_msgSend$outStateNotificationName
+ _objc_msgSend$predicateMatchingBundleIdentifier:
+ _objc_msgSend$processPredicate
+ _objc_msgSend$serviceWithDefaultShellEndpoint
+ _objc_msgSend$setEndowmentNamespaces:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPredicates:
+ _objc_msgSend$setStateDescriptor:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$state
+ _objc_msgSend$taskState
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$usesFrontBoardServicesForRemoteUI
+ _objc_msgSend$willTryToRecover
+ _objc_retain_x9
- -[MechanismBase holdAssertionUntilFinished:]
- GCC_except_table7
- _OBJC_CLASS_$_LAMobileGestalt
- _OBJC_IVAR_$_MechanismBase._assertions
- _objc_msgSend$removeAllObjects
CStrings:
+ "\x01"
+ "\x01\x13"
+ "\x05!1\x11\x12\x115"
+ "\""
+ "%@ is no longer visible"
+ "%@ was confirmed visible"
+ "%@://%@"
+ "%@[%u]"
+ "%{public}@ failed to assert %{public}@ (not scheduled, taskState: %d)"
+ "%{public}@ failed to assert %{public}@ (scheduled but not visible)"
+ "%{public}@ failed to identify the process for monitoring: %{public}@"
+ "%{public}@ received update:%@ monitor:%@ process: %@"
+ "%{public}@ started monitoring %{public}@ for state changes"
+ "%{public}@ stopped monitoring %{public}@ for state changes"
+ "%{public}@ successfully asserted %{public}@ (confirmed task scheduled and visible)"
+ "%{public}@ successfully asserted %{public}@ (failed to get the process handle: %{public}@)"
+ "%{public}@ successfully asserted a bundle-less caller (%{public}@)"
+ "%{public}@ will start monitoring %{public}@"
+ ", holding %@"
+ "-[MechanismAssertionClientProcessVisible _handleStateUpdate:monitor:process:]"
+ "-[RemoteUIActivator _activateFrontBoardUIWithParams:]"
+ "<%@ on %@%@>"
+ "@"
+ "@\"MechanismBase\"8@?0"
+ "@\"RBSProcessHandle\""
+ "@\"RBSProcessMonitor\""
+ "@24@0:8^@16"
+ "@36@0:8@16@24i32"
+ "@40@0:8@16@24@32"
+ "Activating remote UI for %{public}@ via FB with options %{public}@"
+ "Application launch failed with error: %@"
+ "Application launch succeeded"
+ "Assertion failed"
+ "B24@0:8q16"
+ "B32@0:8@16@24"
+ "Client process moved to background."
+ "Client process was suspended."
+ "Failed to register %{public}@: %u"
+ "GlobalCredential"
+ "Ignoring expected deactivation with error: %@"
+ "MechanismAssertionClientProcessVisible"
+ "MechanismAssertionClientProcessVisible.m"
+ "MechanismAssertionHolding"
+ "MechanismAssertionWithDarwinNotifications"
+ "MechanismBiometry"
+ "T@\"NSArray\",R,N"
+ "T@\"NSNumber\",&,N,V_failureLimit"
+ "T@\"NSString\",R,N,V_inStateNotificationName"
+ "T@\"NSString\",R,N,V_outStateNotificationName"
+ "T@,R,N,V_object"
+ "TB,N,V_biolockout"
+ "TI,R,N,V_maxGlobalCredentialAge"
+ "TQ,N,V_failures"
+ "URLWithString:"
+ "UTF8String"
+ "[process matchesProcess:_processHandle]"
+ "^i20@0:8B16"
+ "_acquireAssertionsWithReason:error:"
+ "_activateFrontBoardUIWithParams:"
+ "_activateSpringBoardUIWithParams:"
+ "_assertInStateWithProcessState:"
+ "_biolockout"
+ "_bundleID"
+ "_callerName"
+ "_configureMonitor:"
+ "_dropAssertionsWithReason:"
+ "_failureLimit"
+ "_failures"
+ "_handleStateUpdate:monitor:process:"
+ "_inStateNotificationName"
+ "_inStateToken"
+ "_isInState"
+ "_maxGlobalCredentialAge"
+ "_monitor"
+ "_notificationNameForInState:"
+ "_notificationTokenForInState:"
+ "_object"
+ "_outStateNotificationName"
+ "_outStateToken"
+ "_processHandle"
+ "_processHandleError"
+ "_rbsProcessHandleWithError:"
+ "_rbsStateDescriptor"
+ "_registerDarwinNotificationForInState:"
+ "_setupProcessHandle"
+ "_unregisterDarwinNotificationForInstate:"
+ "aQA\""
+ "addAssertion:"
+ "additionalDescription"
+ "assertion added to a running mechanism"
+ "biolockout"
+ "canRecoverFromError:request:"
+ "com.apple.frontboard.visibility"
+ "containsObject:"
+ "currentState"
+ "descriptor"
+ "dispatchOnServer:"
+ "endowmentNamespaces"
+ "failureLimit"
+ "failures"
+ "failuresInfoDictionaryWithError:"
+ "firstObject"
+ "handleForIdentifier:error:"
+ "handleForPredicate:error:"
+ "handleUIEvent:params:"
+ "identifierWithPid:"
+ "inStateNotificationName"
+ "initWithMechanism:inStateNotificationName:outStateNotificationName:"
+ "initWithMechanism:object:"
+ "initWithMechanism:trackedBundleID:trackedPID:"
+ "invalidate"
+ "isFallbackVisible"
+ "matchesProcess:"
+ "maxGlobalCredentialAge"
+ "mechanism finished"
+ "mechanism starting"
+ "mechanismPruningMechanismsWithEventIdentifier:"
+ "monitor == _monitor"
+ "monitorWithConfiguration:"
+ "object"
+ "openApplication:withOptions:completion:"
+ "options"
+ "optionsWithDictionary:"
+ "outStateNotificationName"
+ "pid %u"
+ "predicateMatchingBundleIdentifier:"
+ "processPredicate"
+ "q8@?0"
+ "received %@"
+ "serviceWithDefaultShellEndpoint"
+ "setBiolockout:"
+ "setEndowmentNamespaces:"
+ "setFailureLimit:"
+ "setFailures:"
+ "setObject:forKeyedSubscript:"
+ "setPredicates:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "state"
+ "taskState"
+ "unsignedIntValue"
+ "usesFrontBoardServicesForRemoteUI"
+ "v12@?0i8"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v24@?0@\"BSProcessHandle\"8@\"NSError\"16"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "willTryToRecover"
- "\x05!1\x11\x126"
- "<%@ on %@>"
- "T@\"NSMutableArray\",R,N,V_assertions"
- "_assertions"
- "aQC"
- "holdAssertionUntilFinished:"
- "holding assertion: %@"
- "removeAllObjects"
- "v24@0:8q16"

```
