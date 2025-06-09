## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x16810
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x1c80
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x3d4
-  __TEXT.__cstring: 0x100e
-  __TEXT.__oslogstring: 0x1398
-  __TEXT.__unwind_info: 0x710
-  __TEXT.__objc_classname: 0x3f3
-  __TEXT.__objc_methname: 0x4a46
-  __TEXT.__objc_methtype: 0xecb
-  __TEXT.__objc_stubs: 0x3700
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x890
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0xa0
+2005.0.13.0.0
+  __TEXT.__text: 0x18494
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x1e10
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0x404
+  __TEXT.__cstring: 0x108b
+  __TEXT.__oslogstring: 0x14e1
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__objc_classname: 0x407
+  __TEXT.__objc_methname: 0x4e8e
+  __TEXT.__objc_methtype: 0xf33
+  __TEXT.__objc_stubs: 0x3a60
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1180
+  __DATA_CONST.__objc_selrefs: 0x1230
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x4eb8
-  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x54c8
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0x780
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x25c
+  __DATA.__data: 0x720
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B1A0E9F-62AF-38FB-9776-9C23D2853272
-  Functions: 603
-  Symbols:   2422
-  CStrings:  1432
+  UUID: 29902E9E-39FC-305A-88FE-23E8D919C52D
+  Functions: 641
+  Symbols:   2551
+  CStrings:  1479
 
Symbols:
+ -[MechanismBase requiresHostingControllerUiWithEventProcessing:]
+ -[MechanismBase requiresRemoteUIWithEventProcessing:]
+ -[MechanismBiometry failuresInfoDictionaryWithError:unboundMatch:]
+ -[MechanismBiometry isBiometryRequiredForPolicy]
+ -[MechanismKofN requiresHostingControllerUiWithEventProcessing:]
+ -[MechanismUI _activateListener:]
+ -[MechanismUI _hostedSceneConfigurationForRemoteUIController:endpoint:]
+ -[MechanismUI _invalidateListeners]
+ -[MechanismUI _setupMechanismForHostingController:listener:]
+ -[MechanismUI checkHasPendingUIRequestsForRemoteUI:completion:]
+ -[MechanismUI dealloc]
+ -[RemoteUIActivator _activateUserInterface:withParams:]
+ -[RemoteUIActivator _createInterface]
+ -[RemoteUIActivator _prepareUIListener]
+ -[RemoteUIActivator _processRequest:interface:]
+ -[RemoteUIActivator _workQueue]
+ -[RemoteUIActivator hasInvalidatedUIForRequest:]
+ -[RemoteUIActivator invalidateUIForRequest:]
+ -[RemoteUIActivator notificationManager]
+ -[RemoteUIActivator setNotificationManager:]
+ -[RemoteUIActivator_Legacy .cxx_destruct]
+ -[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]
+ -[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:].cold.1
+ -[RemoteUIActivator_Legacy _activateRemoteAlertHandle:activationContext:params:]
+ -[RemoteUIActivator_Legacy _activateSpringBoardUIWithParams:]
+ -[RemoteUIActivator_Legacy _dispatchRemoteAlertHandle:activationContext:params:]
+ -[RemoteUIActivator_Legacy _isActivationSuspended]
+ -[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]
+ -[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:].cold.1
+ -[RemoteUIActivator_Legacy _resumeActivationQueue]
+ -[RemoteUIActivator_Legacy _resumeActivationQueue].cold.1
+ -[RemoteUIActivator_Legacy _resumeActivationQueue].cold.2
+ -[RemoteUIActivator_Legacy _sbHandleWithDefinition:configurationContext:]
+ -[RemoteUIActivator_Legacy _sbHandleWithDefinition:configurationContext:].cold.1
+ -[RemoteUIActivator_Legacy _suspendActivationQueue]
+ -[RemoteUIActivator_Legacy _suspendActivationQueue].cold.1
+ -[RemoteUIActivator_Legacy _suspendActivationQueue].cold.2
+ -[RemoteUIActivator_Legacy activateUIWithParams:]
+ -[RemoteUIActivator_Legacy activatingHandle]
+ -[RemoteUIActivator_Legacy activationQueue]
+ -[RemoteUIActivator_Legacy activeHandle]
+ -[RemoteUIActivator_Legacy delegate]
+ -[RemoteUIActivator_Legacy hasInvalidatedUIForRequest:]
+ -[RemoteUIActivator_Legacy init]
+ -[RemoteUIActivator_Legacy invalidateUIForRequest:]
+ -[RemoteUIActivator_Legacy invalidateUIForRequest:].cold.1
+ -[RemoteUIActivator_Legacy notificationManager]
+ -[RemoteUIActivator_Legacy onActivationTimeout]
+ -[RemoteUIActivator_Legacy remoteAlertHandle:didInvalidateWithError:]
+ -[RemoteUIActivator_Legacy remoteAlertHandle:didInvalidateWithError:].cold.1
+ -[RemoteUIActivator_Legacy remoteAlertHandleDidActivate:]
+ -[RemoteUIActivator_Legacy remoteAlertHandleDidActivate:].cold.1
+ -[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:]
+ -[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:].cold.1
+ -[RemoteUIActivator_Legacy remoteAlertWasInvalidated]
+ -[RemoteUIActivator_Legacy setActivatingHandle:]
+ -[RemoteUIActivator_Legacy setActivationQueue:]
+ -[RemoteUIActivator_Legacy setActiveHandle:]
+ -[RemoteUIActivator_Legacy setDelegate:]
+ -[RemoteUIActivator_Legacy setNotificationManager:]
+ -[RemoteUIActivator_Legacy setOnActivationTimeout:]
+ -[RemoteUIActivator_Legacy setRemoteAlertWasInvalidated:]
+ -[RemoteUIManager anonymousListenerForHostedController:mechanism:reply:]
+ -[RemoteUIManager checkHasPendingUIRequestsForRemoteUI:completion:]
+ -[RemoteUIManager didSuccessfullyFinishForRequestId:]
+ -[RemoteUIManager prepareForHostedController:mechanism:reply:]
+ -[RemoteUIManager setNotificationManager:]
+ -[RemoteUIParams evaluationRequest]
+ -[RemoteUIParams hostedRemoteController]
+ -[RemoteUIParams initWithMechanism:]
+ -[RemoteUIParams initWithMechanism:hostedRemoteController:]
+ -[RemoteUIParams remoteUI]
+ -[RemoteUIParams setRemoteUI:]
+ -[_RemoteUIManager _activatePendingUIIfNeeded]
+ -[_RemoteUIManager _activatePendingUIIfNeeded].cold.1
+ -[_RemoteUIManager _anonymousListenerWithIdentifier:]
+ -[_RemoteUIManager anonymousListenerForHostedController:mechanism:reply:]
+ -[_RemoteUIManager checkHasPendingUIRequestsForRemoteUI:completion:]
+ -[_RemoteUIManager didSuccessfullyFinishForRequestId:]
+ -[_RemoteUIManager prepareForHostedController:mechanism:reply:]
+ -[_RemoteUIManager setNotificationManager:]
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table68
+ GCC_except_table7
+ _LACAngelHostedSceneIdentifierPasscode
+ _LACAngelHostedSceneIdentifierPassword
+ _LACAngelHostedSceneIdentifierPin
+ _LACErrorDomain
+ _LACLogUI
+ _LACUserInterfaceBundleIdentifierDefault
+ _OBJC_CLASS_$_LACACMHelper
+ _OBJC_CLASS_$_LACAngelConnectionProvider
+ _OBJC_CLASS_$_LACAngelHostedSceneConfiguration
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACTCCManager
+ _OBJC_CLASS_$_LACUserInterfaceFrontBoardAdapter
+ _OBJC_CLASS_$_LACUserInterfaceRemoteUIAdapter
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_RemoteUIActivator_Legacy
+ _OBJC_IVAR_$_MechanismUI._anonymousListeners
+ _OBJC_IVAR_$_RemoteUIActivator._activeInterfaces
+ _OBJC_IVAR_$_RemoteUIActivator._activeListeners
+ _OBJC_IVAR_$_RemoteUIActivator._activeObjectsLock
+ _OBJC_IVAR_$_RemoteUIActivator._notificationManager
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._activatingHandle
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._activationQueue
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._activationSuspended
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._activeHandle
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._activeInterfaces
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._delegate
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._notificationManager
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._onActivationTimeout
+ _OBJC_IVAR_$_RemoteUIActivator_Legacy._remoteAlertWasInvalidated
+ _OBJC_IVAR_$_RemoteUIParams._evaluationRequest
+ _OBJC_IVAR_$_RemoteUIParams._hostedRemoteController
+ _OBJC_IVAR_$_RemoteUIParams._identifier
+ _OBJC_IVAR_$_RemoteUIParams._remoteUI
+ _OBJC_IVAR_$_RemoteUIParams._uiRequest
+ _OBJC_IVAR_$__RemoteUIManager._pendingRequest
+ _OBJC_METACLASS_$_RemoteUIActivator_Legacy
+ __OBJC_$_INSTANCE_METHODS_RemoteUIActivator_Legacy
+ __OBJC_$_INSTANCE_VARIABLES_RemoteUIActivator_Legacy
+ __OBJC_$_PROP_LIST_LACCompanionAuthenticationService
+ __OBJC_$_PROP_LIST_RemoteUIActivator_Legacy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACCompanionAuthenticationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACCompanionAuthenticationService
+ __OBJC_$_PROTOCOL_REFS_LACCompanionAuthenticationService
+ __OBJC_CLASS_PROTOCOLS_$_RemoteUIActivator_Legacy
+ __OBJC_CLASS_RO_$_RemoteUIActivator_Legacy
+ __OBJC_LABEL_PROTOCOL_$_LACCompanionAuthenticationService
+ __OBJC_METACLASS_RO_$_RemoteUIActivator_Legacy
+ __OBJC_PROTOCOL_$_LACCompanionAuthenticationService
+ __OBJC_PROTOCOL_REFERENCE_$_LACCompanionAuthenticationService
+ ___100-[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]_block_invoke
+ ___22-[MechanismUI _showUI]_block_invoke.107
+ ___22-[MechanismUI _showUI]_block_invoke_5
+ ___22-[MechanismUI _showUI]_block_invoke_6
+ ___34-[MechanismUI event:params:reply:]_block_invoke.169
+ ___34-[MechanismUI event:params:reply:]_block_invoke_2.172
+ ___38-[MechanismBase pause:forEvent:error:]_block_invoke.138
+ ___40-[MechanismUI _startBackgroundMechanism]_block_invoke.121
+ ___42-[RemoteUIManager setNotificationManager:]_block_invoke
+ ___46-[_RemoteUIManager _activatePendingUIIfNeeded]_block_invoke
+ ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke
+ ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke.12
+ ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke.cold.1
+ ___51-[RemoteUIActivator_Legacy _suspendActivationQueue]_block_invoke
+ ___51-[RemoteUIActivator_Legacy _suspendActivationQueue]_block_invoke.cold.1
+ ___52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke.133
+ ___53-[RemoteUIManager didSuccessfullyFinishForRequestId:]_block_invoke
+ ___55-[RemoteUIActivator _activateUserInterface:withParams:]_block_invoke
+ ___59-[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:]_block_invoke
+ ___60-[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]_block_invoke
+ ___62-[RemoteUIManager prepareForHostedController:mechanism:reply:]_block_invoke
+ ___67-[RemoteUIManager checkHasPendingUIRequestsForRemoteUI:completion:]_block_invoke
+ ___72-[RemoteUIManager anonymousListenerForHostedController:mechanism:reply:]_block_invoke
+ ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.100
+ ___80-[RemoteUIActivator_Legacy _activateRemoteAlertHandle:activationContext:params:]_block_invoke
+ ___80-[RemoteUIActivator_Legacy _dispatchRemoteAlertHandle:activationContext:params:]_block_invoke
+ ___block_descriptor_40_e8_32s_e21_"RemoteUIParams"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0q8ls32l8
+ ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40bs48w_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e23_v16?0"NSXPCListener"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.140
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.37
+ ___block_literal_global.69
+ _objc_msgSend$_activateListener:
+ _objc_msgSend$_activatePendingUIIfNeeded
+ _objc_msgSend$_activateUserInterface:withParams:
+ _objc_msgSend$_anonymousListenerWithIdentifier:
+ _objc_msgSend$_createInterface
+ _objc_msgSend$_hostedSceneConfigurationForRemoteUIController:endpoint:
+ _objc_msgSend$_invalidateListeners
+ _objc_msgSend$_prepareUIListener
+ _objc_msgSend$_processRequest:interface:
+ _objc_msgSend$_setupMechanismForHostingController:listener:
+ _objc_msgSend$_workQueue
+ _objc_msgSend$activate
+ _objc_msgSend$anonymousListenerForHostedController:mechanism:reply:
+ _objc_msgSend$applicationOptionsForPayloadURL:softwareUpdate:
+ _objc_msgSend$applicationPayloadURLForBundleID:rootControllerName:parameters:
+ _objc_msgSend$authorizationStatusForService:auditToken:promptUser:
+ _objc_msgSend$checkHasPendingUIRequestsForRemoteUI:completion:
+ _objc_msgSend$delegate
+ _objc_msgSend$didSuccessfullyFinishForRequestId:
+ _objc_msgSend$evaluationRequest
+ _objc_msgSend$evaluationRequestIdentifier
+ _objc_msgSend$featureFlagLaunchAngelEnabled
+ _objc_msgSend$hasInvalidatedUIForRequest:
+ _objc_msgSend$hostedRemoteController
+ _objc_msgSend$initWithAngelIdentifier:sceneIdentifier:endpoint:requestId:
+ _objc_msgSend$initWithConnectionProvider:replyQueue:
+ _objc_msgSend$initWithMechanism:
+ _objc_msgSend$initWithMechanism:hostedRemoteController:
+ _objc_msgSend$initWithReplyQueue:
+ _objc_msgSend$invalidateUIForRequest:
+ _objc_msgSend$isCompanionDeviceAvailable
+ _objc_msgSend$isDTOPolicy:options:
+ _objc_msgSend$prepareForHostedController:mechanism:reply:
+ _objc_msgSend$processRequest:completion:
+ _objc_msgSend$remoteUI
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$requiresHostingControllerUiWithEventProcessing:
+ _objc_msgSend$requiresRemoteUIWithEventProcessing:
+ _objc_msgSend$setConnectionEndpoint:
+ _objc_msgSend$setNotificationManager:
+ _objc_msgSend$setRemoteUI:
+ _objc_msgSend$succeedAuthenticationWithDefaultResult
+ _objc_msgSend$terminateWithReason:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- +[RemoteUIActivator daemon]
- +[RemoteUIActivator setDaemon:]
- -[MechanismBase isRunningDTOPolicy]
- -[MechanismUI checkHasPendingUIRequestsWithCompletion:]
- -[RemoteUIActivator _activateFrontBoardUIWithParams:]
- -[RemoteUIActivator _activateFrontBoardUIWithParams:].cold.1
- -[RemoteUIActivator _activateRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator _activateSpringBoardUIWithParams:]
- -[RemoteUIActivator _dispatchRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator _isActivationSuspended]
- -[RemoteUIActivator _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]
- -[RemoteUIActivator _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:].cold.1
- -[RemoteUIActivator _resumeActivationQueue]
- -[RemoteUIActivator _resumeActivationQueue].cold.1
- -[RemoteUIActivator _resumeActivationQueue].cold.2
- -[RemoteUIActivator _sbHandleWithDefinition:configurationContext:]
- -[RemoteUIActivator _sbHandleWithDefinition:configurationContext:].cold.1
- -[RemoteUIActivator _suspendActivationQueue]
- -[RemoteUIActivator _suspendActivationQueue].cold.1
- -[RemoteUIActivator _suspendActivationQueue].cold.2
- -[RemoteUIActivator activatingHandle]
- -[RemoteUIActivator activationQueue]
- -[RemoteUIActivator activeHandle]
- -[RemoteUIActivator invalidated]
- -[RemoteUIActivator onActivationTimeout]
- -[RemoteUIActivator remoteAlertHandle:didInvalidateWithError:]
- -[RemoteUIActivator remoteAlertHandle:didInvalidateWithError:].cold.1
- -[RemoteUIActivator remoteAlertHandleDidActivate:]
- -[RemoteUIActivator remoteAlertHandleDidActivate:].cold.1
- -[RemoteUIActivator remoteAlertHandleDidDeactivate:]
- -[RemoteUIActivator remoteAlertHandleDidDeactivate:].cold.1
- -[RemoteUIActivator remoteAlertWasInvalidated]
- -[RemoteUIActivator setActivatingHandle:]
- -[RemoteUIActivator setActivationQueue:]
- -[RemoteUIActivator setActiveHandle:]
- -[RemoteUIActivator setOnActivationTimeout:]
- -[RemoteUIActivator setRemoteAlertWasInvalidated:]
- -[RemoteUIManager checkHasPendingUIRequestsWithCompletion:]
- -[RemoteUIManager prepareForRemoteViewControllerWithMechanism:reply:]
- -[RemoteUIParams setAuditTokenData:]
- -[RemoteUIParams setForSiri:]
- -[RemoteUIParams setForSoftwareUpdate:]
- -[RemoteUIParams setLsApplicationIdentity:]
- -[RemoteUIParams setPid:]
- -[RemoteUIParams setRequestID:]
- -[RemoteUIParams setUiMechanism:]
- -[RemoteUIParams setUserId:]
- -[_RemoteUIManager checkHasPendingUIRequestsWithCompletion:]
- -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:].cold.1
- -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:].cold.2
- -[_RemoteUIManager prepareForRemoteViewControllerWithMechanism:reply:]
- GCC_except_table30
- GCC_except_table35
- GCC_except_table39
- GCC_except_table40
- GCC_except_table46
- GCC_except_table67
- _FBSOpenApplicationOptionKeyActivateSuspended
- _FBSOpenApplicationOptionKeyLaunchIntent
- _FBSOpenApplicationOptionKeyPayloadURL
- _FBSOpenApplicationOptionKeyPromptUnlockDevice
- _FBSOpenApplicationOptionKeyUnlockDevice
- _FBSOpenApplicationWithNewScene
- _OBJC_CLASS_$_LAACMHelper
- _OBJC_CLASS_$_NSURL
- _OBJC_IVAR_$_RemoteUIActivator._activatingHandle
- _OBJC_IVAR_$_RemoteUIActivator._activationQueue
- _OBJC_IVAR_$_RemoteUIActivator._activationSuspended
- _OBJC_IVAR_$_RemoteUIActivator._activeHandle
- _OBJC_IVAR_$_RemoteUIActivator._onActivationTimeout
- _OBJC_IVAR_$_RemoteUIActivator._remoteAlertWasInvalidated
- _OBJC_IVAR_$_RemoteUIParams._auditTokenData
- _OBJC_IVAR_$_RemoteUIParams._forSiri
- _OBJC_IVAR_$_RemoteUIParams._forSoftwareUpdate
- _OBJC_IVAR_$_RemoteUIParams._lsApplicationIdentity
- _OBJC_IVAR_$_RemoteUIParams._pid
- _OBJC_IVAR_$_RemoteUIParams._requestID
- _OBJC_IVAR_$_RemoteUIParams._userId
- _OBJC_IVAR_$__RemoteUIManager._pendingUiMechanism
- _TCCAccessCheckAuditToken
- _TCCAccessPreflightWithAuditToken
- __OBJC_$_CLASS_METHODS_RemoteUIActivator
- __OBJC_$_CLASS_PROP_LIST_RemoteUIActivator
- __OBJC_$_PROP_LIST_LACOnenessService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACEvaluationRequestProcessor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACOnenessService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACEvaluationRequestProcessor
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACEvaluationRequestProcessor
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACOnenessService
- __OBJC_$_PROTOCOL_REFS_LACEvaluationRequestProcessor
- __OBJC_$_PROTOCOL_REFS_LACOnenessService
- __OBJC_LABEL_PROTOCOL_$_LACEvaluationRequestProcessor
- __OBJC_LABEL_PROTOCOL_$_LACOnenessService
- __OBJC_PROTOCOL_$_LACEvaluationRequestProcessor
- __OBJC_PROTOCOL_$_LACOnenessService
- __OBJC_PROTOCOL_REFERENCE_$_LACOnenessService
- ___22-[MechanismUI _showUI]_block_invoke.106
- ___34-[MechanismUI event:params:reply:]_block_invoke.160
- ___34-[MechanismUI event:params:reply:]_block_invoke_2.163
- ___38-[MechanismBase pause:forEvent:error:]_block_invoke.137
- ___40-[MechanismUI _startBackgroundMechanism]_block_invoke.120
- ___44-[RemoteUIActivator _suspendActivationQueue]_block_invoke
- ___44-[RemoteUIActivator _suspendActivationQueue]_block_invoke.cold.1
- ___52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke.135
- ___53-[RemoteUIActivator _activateFrontBoardUIWithParams:]_block_invoke
- ___59-[RemoteUIManager checkHasPendingUIRequestsWithCompletion:]_block_invoke
- ___69-[RemoteUIManager prepareForRemoteViewControllerWithMechanism:reply:]_block_invoke
- ___73-[RemoteUIActivator _activateRemoteAlertHandle:activationContext:params:]_block_invoke
- ___73-[RemoteUIActivator _dispatchRemoteAlertHandle:activationContext:params:]_block_invoke
- ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.110
- ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.117
- ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.cold.1
- ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke_2.118
- ___93-[RemoteUIActivator _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]_block_invoke
- ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e62_v32?0"<LACUIMechanism>"8"<LACBackoffCounter>"16"NSError"24lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e21_"RemoteUIParams"8?0ls32l8s40l8
- ___block_literal_global.112
- ___block_literal_global.139
- ___block_literal_global.153
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.165
- ___block_literal_global.70
- __daemon
- _kTCCAccessCheckOptionPrompt
- _objc_msgSend$URLWithString:
- _objc_msgSend$checkHasPendingUIRequestsWithCompletion:
- _objc_msgSend$controller
- _objc_msgSend$daemon
- _objc_msgSend$invalidated
- _objc_msgSend$isEnabled
- _objc_msgSend$isLocationBasedPolicy:
- _objc_msgSend$isSessionActive
- _objc_msgSend$isSupported
- _objc_msgSend$prepareForRemoteViewControllerWithMechanism:reply:
- _objc_msgSend$setAuditTokenData:
- _objc_msgSend$setForSiri:
- _objc_msgSend$setForSoftwareUpdate:
- _objc_msgSend$setLsApplicationIdentity:
- _objc_msgSend$setPid:
- _objc_msgSend$setRequestID:
- _objc_msgSend$setUiMechanism:
CStrings:
+ "%u"
+ "%u-%u-%li"
+ "-[RemoteUIActivator_Legacy _activateFrontBoardUIWithParams:]"
+ "-[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]"
+ "1"
+ "<RemoteUIParams ID:%@, SU: %d, Siri: %d, uid: %@, pid: %u, lsai: %d>"
+ "@\"<LACEvaluationRequest>\""
+ "@\"<LACLegacyNotificationPosting>\""
+ "@\"<LACLegacyNotificationPosting>\"16@0:8"
+ "@\"LACACMHelper\""
+ "@\"LACUserInterfaceRequest\""
+ "@\"NSMapTable\""
+ "@28@0:8@16B24"
+ "@32@0:8@16q24"
+ "@32@0:8q16@24"
+ "Activator completed rid: %d with error: %@"
+ "Activator did successfully finish request rid: %u"
+ "Activator invalidates interface: %@"
+ "Activator invalidates listener: %@"
+ "Activator registered interface: %@ for rid: %d"
+ "B20@0:8I16"
+ "Cancelled by a new connection"
+ "Hosted scene requested by: %{public}@"
+ "Invalidated by activator"
+ "Invalidation not implemented in the legacy activator"
+ "LACCompanionAuthenticationService"
+ "RemoteUI completed rid: %d"
+ "RemoteUIActivator_Legacy"
+ "RemoteUIActivator_Legacy.m"
+ "T@\"<LACEvaluationRequest>\",R,N,V_evaluationRequest"
+ "T@\"<LACLegacyNotificationPosting>\",&,N"
+ "T@\"<LACLegacyNotificationPosting>\",&,N,V_notificationManager"
+ "T@\"<LACRemoteUI>\",&,N,V_remoteUI"
+ "T@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\",R,N,V_uiMechanism"
+ "T@\"NSData\",R,N"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",R,N,V_identifier"
+ "TI,R,N"
+ "Ti,R,N"
+ "Tq,R,N,V_hostedRemoteController"
+ "_activateListener:"
+ "_activatePendingUIIfNeeded"
+ "_activateUserInterface:withParams:"
+ "_activeInterfaces"
+ "_activeListeners"
+ "_activeObjectsLock"
+ "_anonymousListenerWithIdentifier:"
+ "_anonymousListeners"
+ "_createInterface"
+ "_evaluationRequest"
+ "_hostedRemoteController"
+ "_hostedSceneConfigurationForRemoteUIController:endpoint:"
+ "_identifier"
+ "_invalidateListeners"
+ "_notificationManager"
+ "_pendingRequest"
+ "_prepareUIListener"
+ "_processRequest:interface:"
+ "_setupMechanismForHostingController:listener:"
+ "_uiRequest"
+ "activate"
+ "anonymousListenerForHostedController:mechanism:reply:"
+ "applicationOptionsForPayloadURL:softwareUpdate:"
+ "applicationPayloadURLForBundleID:rootControllerName:parameters:"
+ "authorizationStatusForService:auditToken:promptUser:"
+ "checkHasPendingUIRequestsForRemoteUI:completion:"
+ "com.apple.LocalAuthenticationUIService"
+ "didSuccessfullyFinishForRequestId:"
+ "evaluationRequest"
+ "evaluationRequestIdentifier"
+ "failuresInfoDictionaryWithError:unboundMatch:"
+ "featureFlagLaunchAngelEnabled"
+ "hasInvalidatedUIForRequest:"
+ "hostedRemoteController"
+ "initWithAngelIdentifier:sceneIdentifier:endpoint:requestId:"
+ "initWithConnectionProvider:replyQueue:"
+ "initWithMechanism:hostedRemoteController:"
+ "initWithReplyQueue:"
+ "invalidateUIForRequest:"
+ "isBiometryRequiredForPolicy"
+ "isCompanionDeviceAvailable"
+ "isDTOPolicy:options:"
+ "notificationManager"
+ "prepareForHostedController:mechanism:reply:"
+ "processRequest:completion:"
+ "remoteUI"
+ "removeAllObjects"
+ "removeObjectForKey:"
+ "requiresHostingControllerUiWithEventProcessing:"
+ "requiresRemoteUIWithEventProcessing:"
+ "setConnectionEndpoint:"
+ "setNotificationManager:"
+ "setRemoteUI:"
+ "terminateWithReason:"
+ "v16@?0@\"NSXPCListener\"8"
+ "v16@?0q8"
+ "v24@0:8@\"<LACLegacyNotificationPosting>\"16"
+ "v32@0:8@\"<LACRemoteUI>\"16@?<v@?q>24"
+ "v40@0:8q16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?@\"NSXPCListener\">32"
+ "v40@0:8q16@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"24@?<v@?B@\"NSError\">32"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "$"
- "%@://%@?%@=%u"
- "%u-%u"
- "-[RemoteUIActivator _activateFrontBoardUIWithParams:]"
- "-[RemoteUIActivator _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]"
- "<RemoteUIParams SU: %d, Siri: %d, uid: %@, pid: %u, lsai: %d>"
- "@\"<LACOnenessControlling>\"16@0:8"
- "@\"LAACMHelper\""
- "@\"NSData\""
- "B24@0:8@\"<LACEvaluationRequest>\"16"
- "LACEvaluationRequestProcessor"
- "LACOnenessService"
- "RemoteUIActivator.m"
- "T@\"<LACOnenessControlling>\",R,N"
- "T@\"<LADaemonXPC>\",&,N"
- "T@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\",&,N,V_uiMechanism"
- "T@\"NSData\",&,N,V_auditTokenData"
- "TB,N,V_forSiri"
- "TB,N,V_forSoftwareUpdate"
- "TB,N,V_lsApplicationIdentity"
- "TI,N,V_requestID"
- "Ti,N,V_pid"
- "URLWithString:"
- "_auditTokenData"
- "_forSiri"
- "_forSoftwareUpdate"
- "_lsApplicationIdentity"
- "_pendingUiMechanism"
- "_requestID"
- "canProcessRequest:"
- "checkHasPendingUIRequestsWithCompletion:"
- "controller"
- "daemon"
- "invalidated"
- "isEnabled"
- "isLocationBasedPolicy:"
- "isRunningDTOPolicy"
- "isSessionActive"
- "isSupported"
- "postProcessRequest:result:completion:"
- "prepareForRemoteViewControllerWithMechanism:reply:"
- "processRequest:configuration:completion:"
- "setAuditTokenData:"
- "setDaemon:"
- "setForSiri:"
- "setForSoftwareUpdate:"
- "setLsApplicationIdentity:"
- "setPid:"
- "setRequestID:"
- "setUiMechanism:"
- "useTransitionViewModel"
- "v20@0:8i16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v32@0:8@\"MechanismUI<LACUIMechanism><LACRemoteUIHost>\"16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"<LACEvaluationRequest>\"16@\"LACEvaluationResult\"24@?<v@?@\"LACEvaluationResult\">32"
- "v40@0:8@\"<LACEvaluationRequest>\"16@\"LACProcessingConfiguration\"24@?<v@?@\"LACEvaluationResult\">32"

```
