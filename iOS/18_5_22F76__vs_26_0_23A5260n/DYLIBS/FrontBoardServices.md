## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-943.6.1.0.0
-  __TEXT.__text: 0x97b5c
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x7ee0
+993.0.0.0.0
+  __TEXT.__text: 0xa2194
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x84b8
   __TEXT.__const: 0x260
-  __TEXT.__cstring: 0xb89e
-  __TEXT.__oslogstring: 0x374a
-  __TEXT.__gcc_except_tab: 0x2080
-  __TEXT.__unwind_info: 0x2968
-  __TEXT.__objc_classname: 0x1312
-  __TEXT.__objc_methname: 0xf4d2
-  __TEXT.__objc_methtype: 0x329a
-  __TEXT.__objc_stubs: 0xa320
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x2df8
-  __DATA_CONST.__objc_classlist: 0x460
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __TEXT.__cstring: 0xc805
+  __TEXT.__oslogstring: 0x3c64
+  __TEXT.__gcc_except_tab: 0x23e0
+  __TEXT.__unwind_info: 0x2b20
+  __TEXT.__objc_classname: 0x1424
+  __TEXT.__objc_methname: 0x101eb
+  __TEXT.__objc_methtype: 0x3598
+  __TEXT.__objc_stubs: 0xaec0
+  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__const: 0x2f70
+  __DATA_CONST.__objc_classlist: 0x490
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3918
-  __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x3cc0
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x890
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x93c0
-  __AUTH_CONST.__objc_const: 0xf340
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__cfstring: 0xa120
+  __AUTH_CONST.__objc_const: 0xffd0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x9e8
-  __DATA.__data: 0x17d0
-  __DATA.__bss: 0x3a8
-  __DATA_DIRTY.__objc_data: 0x1db0
-  __DATA_DIRTY.__bss: 0x198
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0xa60
+  __DATA.__data: 0x19b0
+  __DATA.__bss: 0x398
+  __DATA_DIRTY.__objc_data: 0x2030
+  __DATA_DIRTY.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5499075-AB01-3028-BCB5-3D19F26FF7ED
-  Functions: 4063
-  Symbols:   12920
-  CStrings:  6385
+  UUID: CE6D649A-38D4-355E-8485-B2DAB80F368C
+  Functions: 4272
+  Symbols:   13576
+  CStrings:  6825
 
Symbols:
+ +[FBSInvocation initialize]
+ +[FBSInvocationReply initialize]
+ +[FBSInvocationReply replyWithParameters:]
+ +[FBSInvocationTarget targetWithInterface:handler:]
+ +[FBSInvocationTarget targetWithInterface:handler:].cold.1
+ +[FBSInvocationTarget targetWithInterface:handler:].cold.2
+ +[FBSOrientationObserver activeInterfaceOrientation]
+ +[FBSOrientationObserver activeInterfaceOrientation].cold.1
+ +[FBSOrientationServiceSpecification identifier]
+ +[FBSOrientationServiceSpecification interface]
+ +[FBSOrientationServiceSpecification serviceQuality]
+ +[FBSOrientationUpdate supportsBSXPCSecureCoding]
+ +[FBSProcessExecutableSlice arm64]
+ +[FBSProcessExecutableSlice arm64e]
+ +[FBSProcessExecutableSlice initialize]
+ +[FBSProcessExecutableSlice sliceWithType:]
+ +[FBSProcessExecutableSlice sliceWithType:subtype:]
+ +[FBSSceneSettingsCore propagateSetting:]
+ +[FBSSettingsDiff diffByApplyingDiff:toDiff:]
+ +[FBSSettingsDiff diffByApplyingDiff:toDiff:].cold.1
+ +[FBSWorkspace _findDomainSpecification]
+ +[FBSWorkspace _findDomainSpecification].cold.1
+ +[FBSWorkspace _findDomainSpecification].cold.2
+ +[FBSWorkspace _findDomainSpecification].cold.3
+ +[FBSWorkspace _startWorkspaceListener]
+ +[FBSWorkspace _startWorkspaceListener].cold.1
+ +[FBSWorkspace defaultShellEndpoint]
+ +[FBSWorkspace defaultShellEndpoint].cold.1
+ +[FBSWorkspace startViewServiceDomain]
+ +[FBSWorkspace startViewServiceDomain].cold.1
+ +[FBSWorkspace startViewServiceDomain].cold.2
+ +[FBSWorkspace startViewServiceDomain].cold.3
+ +[FBSWorkspace startViewServiceDomain].cold.4
+ +[FBSWorkspaceCoupler _sharedInstance]
+ +[FBSWorkspaceCoupler _sharedInstance].cold.1
+ +[FBSWorkspaceService(SynchronousLocalSupport) localServiceWithIdentifier:]
+ +[FBSWorkspaceService(SynchronousLocalSupport) localServiceWithIdentifier:].cold.1
+ +[FBSWorkspaceService(SynchronousLocalSupport) localService]
+ -[FBSCAContextSceneLayer initWithCAContextID:renderID:level:]
+ -[FBSComponentScene remoteTargetForProtocol:]
+ -[FBSDisplayConfigurationRequest disableFrameDoubling]
+ -[FBSInvocation .cxx_destruct]
+ -[FBSInvocation _createReplyBlockWithSignature:arguments:handler:]
+ -[FBSInvocation _createReplyBlockWithSignature:arguments:handler:].cold.1
+ -[FBSInvocation _createReplyBlockWithSignature:arguments:handler:].cold.2
+ -[FBSInvocation _createReplyBlockWithSignature:arguments:handler:].cold.3
+ -[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]
+ -[FBSInvocation _invokeWithTarget:loggingID:replyHandler:].cold.1
+ -[FBSInvocation _invokeWithTarget:loggingID:replyHandler:].cold.2
+ -[FBSInvocation _invokeWithTarget:loggingID:replyHandler:].cold.3
+ -[FBSInvocation _invokeWithTarget:loggingID:replyHandler:].cold.4
+ -[FBSInvocation cannotResolveForReason:]
+ -[FBSInvocation cannotResolveForReason:].cold.1
+ -[FBSInvocation compatibleWithTarget:]
+ -[FBSInvocation context]
+ -[FBSInvocation dealloc]
+ -[FBSInvocation dealloc].cold.1
+ -[FBSInvocation debugDescriptionWithMultilinePrefix:]
+ -[FBSInvocation debugDescription]
+ -[FBSInvocation decodeWithCoder:]
+ -[FBSInvocation decodeWithCoder:].cold.1
+ -[FBSInvocation decodeWithCoder:].cold.2
+ -[FBSInvocation decodeWithCoder:].cold.3
+ -[FBSInvocation decodeWithCoder:].cold.4
+ -[FBSInvocation decodeWithCoder:].cold.5
+ -[FBSInvocation decodeWithCoder:].cold.6
+ -[FBSInvocation decodeWithCoder:].cold.7
+ -[FBSInvocation descriptionWithMultilinePrefix:]
+ -[FBSInvocation description]
+ -[FBSInvocation encodeWithCoder:]
+ -[FBSInvocation initWithInvocation:interface:]
+ -[FBSInvocation initWithInvocation:interface:].cold.1
+ -[FBSInvocation initWithInvocation:interface:].cold.2
+ -[FBSInvocation initWithInvocation:interface:].cold.3
+ -[FBSInvocation initWithInvocation:interface:].cold.4
+ -[FBSInvocation initWithInvocation:interface:].cold.5
+ -[FBSInvocation initWithInvocation:interface:].cold.6
+ -[FBSInvocation initWithInvocation:interface:].cold.7
+ -[FBSInvocation initWithInvocation:interface:].cold.8
+ -[FBSInvocation initWithInvocation:interface:].cold.9
+ -[FBSInvocation invokeWithReceiver:replyHandler:]
+ -[FBSInvocation invokeWithTarget:replyHandler:]
+ -[FBSInvocation invoked]
+ -[FBSInvocation membersForCoder]
+ -[FBSInvocation resolve]
+ -[FBSInvocation resolve].cold.1
+ -[FBSInvocation selectorName]
+ -[FBSInvocation selector]
+ -[FBSInvocation succinctDescriptionBuilder]
+ -[FBSInvocation(FBSComponentScene) extension]
+ -[FBSInvocation(FBSComponentScene) extension].cold.1
+ -[FBSInvocationReply .cxx_destruct]
+ -[FBSInvocationReply membersForCoder]
+ -[FBSInvocationTarget .cxx_destruct]
+ -[FBSInvocationTarget forwardInvocation:]
+ -[FBSInvocationTarget forwardInvocation:].cold.1
+ -[FBSInvocationTarget methodSignatureForSelector:]
+ -[FBSInvocationTarget methodSignatureForSelector:].cold.1
+ -[FBSMutableDisplayConfigurationRequest setDisableFrameDoubling:]
+ -[FBSMutableSceneUpdate setPreviousSettings:]
+ -[FBSMutableSceneUpdate setSettings:]
+ -[FBSMutableSceneUpdate setSettingsDiff:]
+ -[FBSMutableSceneUpdate setTransitionContext:]
+ -[FBSOrientationObserver _initWithClient:callbackQueue:]
+ -[FBSOrientationObserver _lock_getAndSetFreshestUpdateGivenUpdate:]
+ -[FBSOrientationObserver _lock_setHandler:]
+ -[FBSOrientationObserverClient _connectionActivated:]
+ -[FBSOrientationObserverClient _connectionInvalidated:]
+ -[FBSOrientationObserverClient _connection]
+ -[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]
+ -[FBSOrientationObserverClient _lock_activate]
+ -[FBSOrientationObserverClient _lock_activate].cold.1
+ -[FBSOrientationObserverClient _lock_invalidate]
+ -[FBSOrientationObserverClient _lock_remoteTarget]
+ -[FBSOrientationObserverClient _setDelegate:]
+ -[FBSOrientationObserverClient activate]
+ -[FBSOrientationObserverClient activeOrientationDidUpdate:]
+ -[FBSOrientationObserverClient dealloc]
+ -[FBSOrientationObserverClient dealloc].cold.1
+ -[FBSOrientationObserverClient initWithDelegate:]
+ -[FBSOrientationObserverClient initWithDelegate:].cold.1
+ -[FBSOrientationUpdate encodeWithBSXPCCoder:]
+ -[FBSOrientationUpdate initWithBSXPCCoder:]
+ -[FBSProcess _watchdog:terminationRequestForError:]
+ -[FBSProcess versionedPID]
+ -[FBSProcessExecutableSlice description]
+ -[FBSProcessExecutableSlice membersForCoder]
+ -[FBSProcessExecutableSlice subtype]
+ -[FBSProcessExecutableSlice type]
+ -[FBSProcessWatchdog isActive]
+ -[FBSPseudoSceneUpdater .cxx_destruct]
+ -[FBSPseudoSceneUpdater _initWithCallOutQueue:]
+ -[FBSPseudoSceneUpdater _initWithCallOutQueue:].cold.1
+ -[FBSPseudoSceneUpdater _initWithCallOutQueue:].cold.2
+ -[FBSPseudoSceneUpdater scene:invalidateWithTransitionContext:]
+ -[FBSPseudoSceneUpdater scene:sendInvocation:]
+ -[FBSPseudoSceneUpdater scene:sendInvocation:].cold.1
+ -[FBSPseudoSceneUpdater sendBatchedMessages]
+ -[FBSScene _beginUpdate].cold.2
+ -[FBSScene _callOutQueue_ensureCoalesceClientSettingsUpdates:]
+ -[FBSScene _callOutQueue_maybeCoalesceClientSettingsUpdates:]
+ -[FBSScene _callOutQueue_maybeCoalesceClientSettingsUpdates:].cold.1
+ -[FBSScene _updateClientSettings:].cold.3
+ -[FBSScene invalidate:]
+ -[FBSScene sendBatchedMessages]
+ -[FBSScene sendInvocation:]
+ -[FBSScene sendInvocation:].cold.1
+ -[FBSScene targetForInvocation:]
+ -[FBSSceneLayer initWithContextID:renderID:level:]
+ -[FBSSceneLayer initWithContextID:renderID:level:].cold.1
+ -[FBSSceneLayer renderID]
+ -[FBSSceneObserver extension]
+ -[FBSSceneObserver initWithComponent:extension:]
+ -[FBSSceneSettings jetsamMode]
+ -[FBSSceneSettings setJetsamMode:]
+ -[FBSSceneSettingsCore jetsamPriority]
+ -[FBSSceneSettingsCore setJetsamPriority:]
+ -[FBSSceneSpecification disablesClientBatching]
+ -[FBSSceneTransitionContext addUpdateCompletion:]
+ -[FBSSceneTransitionContext captureCompletions]
+ -[FBSSceneTransitionContext dealloc]
+ -[FBSSceneTransitionContext dealloc].cold.1
+ -[FBSSceneTransitionContextCore isBarrier]
+ -[FBSSceneTransitionContextCore setBarrier:]
+ -[FBSSceneUpdate copyWithZone:]
+ -[FBSSceneUpdate debugDescription]
+ -[FBSSceneUpdate descriptionBuilderWithMultilinePrefix:]
+ -[FBSSceneUpdate descriptionWithMultilinePrefix:]
+ -[FBSSceneUpdate description]
+ -[FBSSceneUpdate mutableCopyWithZone:]
+ -[FBSSceneUpdate succinctDescriptionBuilder]
+ -[FBSSceneUpdate succinctDescription]
+ -[FBSServiceFacilityClient _lock_invalidate].cold.1
+ -[FBSServiceFacilityClient initWithConfigurator:].cold.5
+ -[FBSSettingsDiff succinctDescriptionBuilder]
+ -[FBSSettingsDiff succinctDescription]
+ -[FBSWorkspace _initWithCoupler:options:]
+ -[FBSWorkspace _initWithCoupler:options:].cold.1
+ -[FBSWorkspace _initWithCoupler:options:].cold.2
+ -[FBSWorkspace _initWithCoupler:options:].cold.3
+ -[FBSWorkspace _initWithCoupler:options:].cold.4
+ -[FBSWorkspace _invalidateWithCompletion:]
+ -[FBSWorkspace _invalidateWithCompletion:].cold.1
+ -[FBSWorkspace _queue_registerSource:].cold.1
+ -[FBSWorkspace _registerSourceEndpoint:].cold.1
+ -[FBSWorkspace callOutQueue]
+ -[FBSWorkspace dealloc].cold.1
+ -[FBSWorkspace machQueue]
+ -[FBSWorkspace pseudoSceneWithIdentifier:specification:]
+ -[FBSWorkspace pseudoSceneWithIdentifier:specification:].cold.1
+ -[FBSWorkspace pseudoSceneWithIdentifier:specification:].cold.2
+ -[FBSWorkspaceCoupler .cxx_destruct]
+ -[FBSWorkspaceCoupler _enqueueClientConnectionBlock:]
+ -[FBSWorkspaceCoupler _isSharedInstance]
+ -[FBSWorkspaceCoupler _setWorkspace:]
+ -[FBSWorkspaceCoupler _setWorkspace:].cold.1
+ -[FBSWorkspaceCoupler _setWorkspace:].cold.2
+ -[FBSWorkspaceCoupler _workspace]
+ -[FBSWorkspaceCoupler _workspace].cold.1
+ -[FBSWorkspaceCoupler dealloc]
+ -[FBSWorkspaceCoupler dealloc].cold.1
+ -[FBSWorkspaceCoupler init]
+ -[FBSWorkspaceCoupler invalidate]
+ -[FBSWorkspaceCoupler invalidate].cold.1
+ -[FBSWorkspaceInitializationOptions isDefaultShellEndpointEnabled]
+ -[FBSWorkspaceInitializationOptions isEndpointMonitoringEnabled]
+ -[FBSWorkspaceInitializationOptions setDefaultShellEndpointEnabled:]
+ -[FBSWorkspaceInitializationOptions setEndpointMonitoringEnabled:]
+ -[FBSWorkspaceInitializationOptions setValue:forKey:]
+ -[FBSWorkspaceSceneRequestOptions clientIdentity]
+ -[FBSWorkspaceSceneRequestOptions setClientIdentity:]
+ -[FBSWorkspaceScenesClient _createSceneWithIdentity:parameters:].cold.4
+ -[FBSWorkspaceScenesClient _createSceneWithIdentity:parameters:].cold.5
+ -[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:]
+ -[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:].cold.1
+ -[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:].cold.2
+ -[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:].cold.3
+ -[FBSWorkspaceScenesClient _queue_invalidateScene:withTransitionContext:completion:].cold.1
+ -[FBSWorkspaceScenesClient _queue_invalidate]
+ -[FBSWorkspaceScenesClient _queue_updateScene:withSettings:diff:transitionContext:completion:].cold.1
+ -[FBSWorkspaceScenesClient queue_invalidate]
+ -[FBSWorkspaceScenesClient scene:invalidateWithTransitionContext:]
+ -[FBSWorkspaceScenesClient scene:sendInvocation:]
+ -[FBSWorkspaceScenesClient scene:sendInvocation:].cold.1
+ -[FBSWorkspaceScenesClient scene:sendMessage:withResponse:].cold.1
+ -[FBSWorkspaceScenesClient sceneID:handleInvocation:completion:]
+ -[FBSWorkspaceScenesClient sceneID:updateWithSettingsDiff:transitionContext:completion:].cold.1
+ -[FBSWorkspaceScenesClient sendBatchedMessages]
+ -[FBSWorkspaceService identifier]
+ -[NSInvocation(FBSInvocation) fbs_getObjectForValue:atIndex:]
+ -[NSInvocation(FBSInvocation) fbs_getObjectForValue:atIndex:].cold.1
+ -[NSInvocation(FBSInvocation) fbs_getObjectForValue:atIndex:].cold.2
+ -[NSInvocation(FBSInvocation) fbs_getObjectForValue:atIndex:].cold.3
+ -[NSInvocation(FBSInvocation) fbs_getObjectForValue:atIndex:].cold.4
+ -[_FBSScenesClientHostEvent .cxx_destruct]
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:]
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:].cold.1
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:].cold.2
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:].cold.3
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:].cold.4
+ -[_FBSScenesClientHostEvent coalesceEvent:skipped:].cold.5
+ -[_FBSScenesClientHostEvent coalesceEvents:]
+ -[_FBSScenesClientHostEvent complete]
+ -[_FBSScenesClientHostEvent dealloc]
+ -[_FBSScenesClientHostEvent dealloc].cold.1
+ -[_FBSScenesClientHostEvent invalidate]
+ -[_FBSScenesClientHostEvent setDiff:]
+ -[_FBSScenesClientHostEvent setIdentity:]
+ GCC_except_table104
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table132
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table16
+ GCC_except_table181
+ GCC_except_table28
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table77
+ GCC_except_table86
+ GCC_except_table90
+ GCC_except_table91
+ _BSErrorExceptionDescriptionKey
+ _BSXPCAutoCodingInitialize
+ _BSXPCLegacyCoding
+ _BSXPCSecureCoding
+ _FBLogSceneInvocation
+ _FBLogSceneInvocation.__logObj
+ _FBLogSceneInvocation.cold.1
+ _FBLogSceneInvocation.onceToken
+ _FBSDebugOptionKeyPreferredCPU
+ _FBSSceneActivityModeIsValid
+ _FBSSceneJetsamModeIsValid
+ _FBSSceneJetsamPriorityCreate
+ _FBSSceneJetsamPriorityCreate.cold.1
+ _FBSSceneJetsamPriorityDefault
+ _FBSSceneJetsamPriorityGetJetsamMode
+ _FBSSceneJetsamPriorityGetResourceElevation
+ _FBSSceneJetsamPriorityUpdateElevation
+ _FBSWorkspaceInitialize.__initializeLock
+ _FBSWorkspaceInitialize.__initialized
+ _NSStringFromFBSSceneJetsamPriority
+ _NSStringFromFBSSceneResourceMode
+ _NSXPCSecureCoding
+ _OBJC_CLASS_$_BSServiceCompoundQueue
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceQueue
+ _OBJC_CLASS_$_FBSInvocation
+ _OBJC_CLASS_$_FBSInvocationReply
+ _OBJC_CLASS_$_FBSInvocationTarget
+ _OBJC_CLASS_$_FBSMutableSceneUpdate
+ _OBJC_CLASS_$_FBSOrientationServiceSpecification
+ _OBJC_CLASS_$_FBSPlistCollection
+ _OBJC_CLASS_$_FBSProcessExecutableSlice
+ _OBJC_CLASS_$_FBSWorkspaceCoupler
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSMethodSignature
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$__FBSScenesClientHostEvent
+ _OBJC_IVAR_$_FBSDisplayConfigurationRequest._disableFrameDoubling
+ _OBJC_IVAR_$_FBSInvocation._context
+ _OBJC_IVAR_$_FBSInvocation._encoding
+ _OBJC_IVAR_$_FBSInvocation._invoked
+ _OBJC_IVAR_$_FBSInvocation._objects
+ _OBJC_IVAR_$_FBSInvocation._protocolName
+ _OBJC_IVAR_$_FBSInvocation._reply
+ _OBJC_IVAR_$_FBSInvocation._resolved
+ _OBJC_IVAR_$_FBSInvocation._selectorName
+ _OBJC_IVAR_$_FBSInvocationReply._parameters
+ _OBJC_IVAR_$_FBSInvocationTarget._handler
+ _OBJC_IVAR_$_FBSInvocationTarget._interface
+ _OBJC_IVAR_$_FBSOrientationObserver._lock
+ _OBJC_IVAR_$_FBSOrientationObserver._lock_freshestUpdate
+ _OBJC_IVAR_$_FBSOrientationObserver._lock_handler
+ _OBJC_IVAR_$_FBSOrientationObserverClient._calloutQueue
+ _OBJC_IVAR_$_FBSOrientationObserverClient._endpoint
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_connection
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_interest
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_invalidated
+ _OBJC_IVAR_$_FBSProcessExecutableSlice._subtype
+ _OBJC_IVAR_$_FBSProcessExecutableSlice._type
+ _OBJC_IVAR_$_FBSPseudoSceneUpdater._callOutQueue
+ _OBJC_IVAR_$_FBSScene._callout_updateDepth
+ _OBJC_IVAR_$_FBSSceneLayer._renderID
+ _OBJC_IVAR_$_FBSSceneObserver._extension
+ _OBJC_IVAR_$_FBSWorkspace._isSingleton
+ _OBJC_IVAR_$_FBSWorkspace._psuedoSceneUpdater
+ _OBJC_IVAR_$_FBSWorkspace._queue_invalidated
+ _OBJC_IVAR_$_FBSWorkspaceCoupler._lock
+ _OBJC_IVAR_$_FBSWorkspaceCoupler._lock_clientConnectionBlocks
+ _OBJC_IVAR_$_FBSWorkspaceCoupler._lock_invalidated
+ _OBJC_IVAR_$_FBSWorkspaceCoupler._lock_workspace
+ _OBJC_IVAR_$_FBSWorkspaceInitializationOptions._defaultShellEndpointEnabled
+ _OBJC_IVAR_$_FBSWorkspaceInitializationOptions._endpointMonitoringEnabled
+ _OBJC_IVAR_$_FBSWorkspaceSceneRequestOptions._clientIdentity
+ _OBJC_IVAR_$_FBSWorkspaceScenesClient._hostEventLock
+ _OBJC_IVAR_$_FBSWorkspaceScenesClient._hostEvent_pendingEvents
+ _OBJC_IVAR_$_FBSWorkspaceScenesClient._invalidated
+ _OBJC_IVAR_$__FBSScenesClientHostEvent._canCoalesce
+ _OBJC_IVAR_$__FBSScenesClientHostEvent._completion
+ _OBJC_IVAR_$__FBSScenesClientHostEvent._diff
+ _OBJC_IVAR_$__FBSScenesClientHostEvent._identity
+ _OBJC_METACLASS_$_BSServiceQueue
+ _OBJC_METACLASS_$_FBSInvocation
+ _OBJC_METACLASS_$_FBSInvocationReply
+ _OBJC_METACLASS_$_FBSInvocationTarget
+ _OBJC_METACLASS_$_FBSMutableSceneUpdate
+ _OBJC_METACLASS_$_FBSOrientationServiceSpecification
+ _OBJC_METACLASS_$_FBSPlistCollection
+ _OBJC_METACLASS_$_FBSProcessExecutableSlice
+ _OBJC_METACLASS_$_FBSWorkspaceCoupler
+ _OBJC_METACLASS_$__FBSScenesClientHostEvent
+ _RBSAppViewServiceSessionVendingEntitlement
+ __BSAutoMember
+ __CFXPCCreateCFObjectFromXPCObject
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSInvocation_$_FBSInvocation
+ __OBJC_$_CATEGORY_NSInvocation_$_FBSInvocation
+ __OBJC_$_CLASS_METHODS_FBSInvocation
+ __OBJC_$_CLASS_METHODS_FBSInvocationReply
+ __OBJC_$_CLASS_METHODS_FBSOrientationObserver
+ __OBJC_$_CLASS_METHODS_FBSOrientationServiceSpecification
+ __OBJC_$_CLASS_METHODS_FBSOrientationUpdate
+ __OBJC_$_CLASS_METHODS_FBSProcessExecutableSlice
+ __OBJC_$_CLASS_METHODS_FBSWorkspaceCoupler
+ __OBJC_$_CLASS_METHODS_FBSWorkspaceService(SynchronousLocalSupport)
+ __OBJC_$_CLASS_PROP_LIST_FBSOrientationServiceSpecification
+ __OBJC_$_INSTANCE_METHODS_FBSInvocation(FBSComponentScene)
+ __OBJC_$_INSTANCE_METHODS_FBSInvocationReply
+ __OBJC_$_INSTANCE_METHODS_FBSInvocationTarget
+ __OBJC_$_INSTANCE_METHODS_FBSMutableSceneUpdate
+ __OBJC_$_INSTANCE_METHODS_FBSProcessExecutableSlice
+ __OBJC_$_INSTANCE_METHODS_FBSWorkspaceCoupler
+ __OBJC_$_INSTANCE_METHODS__FBSScenesClientHostEvent
+ __OBJC_$_INSTANCE_VARIABLES_FBSInvocation
+ __OBJC_$_INSTANCE_VARIABLES_FBSInvocationReply
+ __OBJC_$_INSTANCE_VARIABLES_FBSInvocationTarget
+ __OBJC_$_INSTANCE_VARIABLES_FBSProcessExecutableSlice
+ __OBJC_$_INSTANCE_VARIABLES_FBSPseudoSceneUpdater
+ __OBJC_$_INSTANCE_VARIABLES_FBSWorkspaceCoupler
+ __OBJC_$_INSTANCE_VARIABLES__FBSScenesClientHostEvent
+ __OBJC_$_PROP_LIST_FBSInvocation
+ __OBJC_$_PROP_LIST_FBSInvocationReply
+ __OBJC_$_PROP_LIST_FBSMutableSceneUpdate
+ __OBJC_$_PROP_LIST_FBSOrientationObserverClient
+ __OBJC_$_PROP_LIST_FBSProcess.116
+ __OBJC_$_PROP_LIST_FBSProcessExecutableSlice
+ __OBJC_$_PROP_LIST_FBSSceneSettings.186
+ __OBJC_$_PROP_LIST_FBSSceneTransitionContext.191
+ __OBJC_$_PROP_LIST_FBSSceneUpdate
+ __OBJC_$_PROP_LIST_FBSWorkspaceCoupler
+ __OBJC_$_PROP_LIST_FBSWorkspaceService
+ __OBJC_$_PROP_LIST__FBSScenesClientHostEvent
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSInvocationSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSOrientationServiceClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSOrientationServiceServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSInvocationSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSOrientationServiceClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSOrientationServiceServerInterface
+ __OBJC_$_PROTOCOL_REFS_BSXPCAutoCoding
+ __OBJC_$_PROTOCOL_REFS_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_REFS_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_REFS_FBSInvocationSending
+ __OBJC_CLASS_PROTOCOLS_$_FBSInvocation
+ __OBJC_CLASS_PROTOCOLS_$_FBSInvocationReply
+ __OBJC_CLASS_PROTOCOLS_$_FBSOrientationObserverClient
+ __OBJC_CLASS_PROTOCOLS_$_FBSOrientationUpdate
+ __OBJC_CLASS_PROTOCOLS_$_FBSSceneUpdate
+ __OBJC_CLASS_PROTOCOLS_$_FBSWorkspaceCoupler
+ __OBJC_CLASS_PROTOCOLS_$__FBSScenesClientHostEvent
+ __OBJC_CLASS_RO_$_FBSInvocation
+ __OBJC_CLASS_RO_$_FBSInvocationReply
+ __OBJC_CLASS_RO_$_FBSInvocationTarget
+ __OBJC_CLASS_RO_$_FBSMutableSceneUpdate
+ __OBJC_CLASS_RO_$_FBSOrientationServiceSpecification
+ __OBJC_CLASS_RO_$_FBSPlistCollection
+ __OBJC_CLASS_RO_$_FBSProcessExecutableSlice
+ __OBJC_CLASS_RO_$_FBSWorkspaceCoupler
+ __OBJC_CLASS_RO_$__FBSScenesClientHostEvent
+ __OBJC_LABEL_PROTOCOL_$_BSXPCAutoCoding
+ __OBJC_LABEL_PROTOCOL_$_FBSComponentSceneSupport
+ __OBJC_LABEL_PROTOCOL_$_FBSInvocationReceiving
+ __OBJC_LABEL_PROTOCOL_$_FBSInvocationSending
+ __OBJC_LABEL_PROTOCOL_$_FBSOrientationServiceClientInterface
+ __OBJC_LABEL_PROTOCOL_$_FBSOrientationServiceServerInterface
+ __OBJC_METACLASS_RO_$_FBSInvocation
+ __OBJC_METACLASS_RO_$_FBSInvocationReply
+ __OBJC_METACLASS_RO_$_FBSInvocationTarget
+ __OBJC_METACLASS_RO_$_FBSMutableSceneUpdate
+ __OBJC_METACLASS_RO_$_FBSOrientationServiceSpecification
+ __OBJC_METACLASS_RO_$_FBSPlistCollection
+ __OBJC_METACLASS_RO_$_FBSProcessExecutableSlice
+ __OBJC_METACLASS_RO_$_FBSWorkspaceCoupler
+ __OBJC_METACLASS_RO_$__FBSScenesClientHostEvent
+ __OBJC_PROTOCOL_$_BSXPCAutoCoding
+ __OBJC_PROTOCOL_$_FBSComponentSceneSupport
+ __OBJC_PROTOCOL_$_FBSInvocationReceiving
+ __OBJC_PROTOCOL_$_FBSInvocationSending
+ __OBJC_PROTOCOL_$_FBSOrientationServiceClientInterface
+ __OBJC_PROTOCOL_$_FBSOrientationServiceServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_FBSOrientationServiceClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_FBSOrientationServiceServerInterface
+ ___27+[FBSInvocation initialize]_block_invoke
+ ___32+[FBSInvocationReply initialize]_block_invoke
+ ___33-[FBSInvocation encodeWithCoder:]_block_invoke
+ ___36+[FBSWorkspace defaultShellEndpoint]_block_invoke
+ ___36+[FBSWorkspace defaultShellEndpoint]_block_invoke.cold.1
+ ___36-[FBSWorkspace _registerSourcePeer:]_block_invoke.191
+ ___36-[FBSWorkspace _registerSourcePeer:]_block_invoke.cold.2
+ ___38+[FBSWorkspaceCoupler _sharedInstance]_block_invoke
+ ___39+[FBSProcessExecutableSlice initialize]_block_invoke
+ ___40-[FBSInvocation cannotResolveForReason:]_block_invoke
+ ___42-[FBSDisplayConfigurationRequest isEqual:]_block_invoke_7
+ ___42-[FBSServiceFacilityClient _lock_activate]_block_invoke.92
+ ___42-[FBSWorkspace _invalidateWithCompletion:]_block_invoke
+ ___45-[FBSComponentScene remoteTargetForProtocol:]_block_invoke
+ ___46-[FBSInvocation initWithInvocation:interface:]_block_invoke
+ ___46-[FBSInvocation initWithInvocation:interface:]_block_invoke.cold.1
+ ___46-[FBSInvocation initWithInvocation:interface:]_block_invoke_2
+ ___47+[FBSOrientationServiceSpecification interface]_block_invoke
+ ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.34
+ ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.36
+ ___49-[FBSWorkspaceScenesClient scene:sendInvocation:]_block_invoke
+ ___49-[FBSWorkspaceScenesClient scene:sendInvocation:]_block_invoke_2
+ ___49-[FBSWorkspaceScenesClient scene:sendInvocation:]_block_invoke_3
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.140
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.147
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.150
+ ___51-[_FBSScenesClientHostEvent coalesceEvent:skipped:]_block_invoke
+ ___52+[FBSOrientationObserver activeInterfaceOrientation]_block_invoke
+ ___53-[FBSInvocation debugDescriptionWithMultilinePrefix:]_block_invoke
+ ___53-[FBSInvocation debugDescriptionWithMultilinePrefix:]_block_invoke_2
+ ___58-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]_block_invoke
+ ___58-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]_block_invoke.146
+ ___58-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]_block_invoke.154
+ ___58-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]_block_invoke_2
+ ___58-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]_block_invoke_3
+ ___60-[FBSWorkspaceScenesClient createSceneFutureWithDefinition:]_block_invoke.217
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.232
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.240
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.cold.3
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.1
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.2
+ ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.242.cold.3
+ ___64-[FBSWorkspaceScenesClient sceneID:handleInvocation:completion:]_block_invoke
+ ___65-[FBSWorkspaceScenesClient sendActions:toWorkspaceID:completion:]_block_invoke_2
+ ___65-[FBSWorkspaceScenesClient sendActions:toWorkspaceID:completion:]_block_invoke_3
+ ___66-[FBSInvocation _createReplyBlockWithSignature:arguments:handler:]_block_invoke
+ ___66-[FBSInvocation _createReplyBlockWithSignature:arguments:handler:]_block_invoke.cold.1
+ ___66-[FBSWorkspaceScenesClient scene:invalidateWithTransitionContext:]_block_invoke
+ ___66-[FBSWorkspaceScenesClient scene:invalidateWithTransitionContext:]_block_invoke.cold.1
+ ___66-[FBSWorkspaceScenesClient scene:invalidateWithTransitionContext:]_block_invoke.cold.2
+ ___67-[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:]_block_invoke
+ ___67-[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:]_block_invoke.cold.1
+ ___67-[FBSWorkspaceScenesClient _executeCalloutFromHostEvent:withBlock:]_block_invoke.cold.2
+ ___71-[FBSWorkspaceScenesClient sceneID:sendActions:toExtension:completion:]_block_invoke.cold.1
+ ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke
+ ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_2
+ ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_3
+ ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_4
+ ___73-[FBSOrientationObserverClient activeInterfaceOrientationWithCompletion:]_block_invoke
+ ___73-[FBSOrientationObserverClient activeInterfaceOrientationWithCompletion:]_block_invoke.cold.1
+ ___76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.129
+ ___76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke_4
+ ___77-[FBSWorkspaceScenesClient _sceneID:destroyWithTransitionContext:completion:]_block_invoke
+ ___82-[FBSOpenApplicationService _openApplication:withOptions:clientHandle:completion:]_block_invoke.71
+ ___82-[FBSOpenApplicationService _openApplication:withOptions:clientHandle:completion:]_block_invoke.71.cold.1
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.177
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.190
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.194
+ ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_2.182
+ ___88-[FBSWorkspaceScenesClient sceneID:updateWithSettingsDiff:transitionContext:completion:]_block_invoke
+ ___92-[FBSWorkspaceScenesClient createSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke_2
+ ___92-[FBSWorkspaceScenesClient createSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke_3
+ ___92-[FBSWorkspaceScenesClient createSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke_4
+ ___92-[FBSWorkspaceScenesClient createSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke_5
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.337
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.337.cold.1
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.341
+ ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.cold.1
+ ___94-[FBSWorkspaceScenesClient _queue_updateScene:withSettings:diff:transitionContext:completion:]_block_invoke_2.cold.1
+ ___95-[FBSScene _callOutQueue_didCreateWithTransitionContext:alternativeCreationCallout:completion:]_block_invoke_3
+ ___95-[FBSScene _callOutQueue_didCreateWithTransitionContext:alternativeCreationCallout:completion:]_block_invoke_4
+ ___95-[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke.295
+ ___FBLogSceneInvocation_block_invoke
+ ___NSMakeSpecialForwardingCaptureBlock
+ ____ingestPropertiesFromSettingsSubclass_block_invoke.399
+ ____realizeSettingsExtension_block_invoke.259
+ ____realizeSettingsExtension_block_invoke.278
+ ____realizeSettingsExtension_block_invoke.285
+ ____realizeSettingsExtension_block_invoke.285.cold.1
+ ____realizeSettingsExtension_block_invoke.285.cold.2
+ ____realizeSettingsExtension_block_invoke.298
+ ____realizeSettingsExtension_block_invoke_2.261
+ ____realizeSettingsExtension_block_invoke_2.281
+ ____realizeSettingsExtension_block_invoke_2.300
+ ____realizeSettingsExtension_block_invoke_3.263
+ ____realizeSettingsExtension_block_invoke_3.283
+ ____realizeSettingsExtension_block_invoke_3.302
+ ____realizeSettingsExtension_block_invoke_4.304
+ ____realizeSettingsExtension_block_invoke_5.306
+ ____realizeSettingsExtension_block_invoke_6.308
+ ____realizeSettingsExtension_block_invoke_7
+ ____realizeSettingsExtension_block_invoke_7.310
+ ___block_descriptor_32_e38_v16?0"<BSXPCAutoCodingConfiguring>"8l
+ ___block_descriptor_40_e8_32s_e15_v32?0Q816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e21_f16?0"FBSSettings"8ls32l8
+ ___block_descriptor_40_e8_32s_e24_v20?0"FBSSettings"8f16ls32l8
+ ___block_descriptor_40_e8_32s_e35_v16?0"FBSMutableSceneParameters"8ls32l8
+ ___block_descriptor_40_e8_32s_e40_v24?0"FBSInvocationReply"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e42_v24?0"FBSOrientationUpdate"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e43_B24?0"FBSInvocation"8"<BSXPCEncoding>"16ls32l8
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e40_v16?0"<BSBlockSentinelSignalContext>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"FBSInvocationReply"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"FBSOrientationUpdate"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e41_v16?0"FBSWorkspaceSceneUpdateResponse"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionInternalConfiguring>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e30_v16?0"<BSErrorConfiguring>"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e40_v16?0"<BSBlockSentinelSignalContext>"8ls32l8u48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e12_v24?0q8^B16ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e22_v16?0"NSInvocation"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s_e40_v24?0"FBSInvocationReply"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.133
+ ___block_literal_global.143
+ ___block_literal_global.149
+ ___block_literal_global.152
+ ___block_literal_global.219
+ ___block_literal_global.22
+ ___block_literal_global.225
+ ___block_literal_global.26
+ ___block_literal_global.295
+ ___getCALayerGetRenderIdSymbolLoc_block_invoke
+ __interfaceFromProtocol
+ __realizeSettingsExtension.cold.34
+ __realizeSettingsExtension.cold.35
+ __serviceQualityForFBSDisplayLayoutQOS
+ __sharedInstance.__sharedInstance
+ __sharedInstance.onceToken
+ __vetProtocolMethod
+ __vetProtocolMethod.cold.1
+ __vetProtocolMethod.cold.2
+ __vetProtocolMethod.cold.3
+ __vetProtocolMethod.cold.4
+ __vetProtocolMethod.cold.5
+ __vetProtocolMethod.cold.6
+ __xpc_type_array
+ _activeInterfaceOrientation.client
+ _activeInterfaceOrientation.onceToken
+ _class_getProperty
+ _defaultShellEndpoint.__DefaultShellEndpoint
+ _defaultShellEndpoint.onceToken
+ _getCALayerGetRenderIdSymbolLoc
+ _getCALayerGetRenderIdSymbolLoc.ptr
+ _interface._interface
+ _objc_msgSend$_cTypeString
+ _objc_msgSend$_callOutQueue_ensureCoalesceClientSettingsUpdates:
+ _objc_msgSend$_callOutQueue_maybeCoalesceClientSettingsUpdates:
+ _objc_msgSend$_classForObjectAtArgumentIndex:
+ _objc_msgSend$_connectionActivated:
+ _objc_msgSend$_connectionInvalidated:
+ _objc_msgSend$_findDomainSpecification
+ _objc_msgSend$_initWithCallOutQueue:
+ _objc_msgSend$_initWithClient:callbackQueue:
+ _objc_msgSend$_initWithCoupler:options:
+ _objc_msgSend$_initWithEndpoint:calloutQueue:delegate:
+ _objc_msgSend$_isSharedInstance
+ _objc_msgSend$_lock_getAndSetFreshestUpdateGivenUpdate:
+ _objc_msgSend$_lock_remoteTarget
+ _objc_msgSend$_lock_setHandler:
+ _objc_msgSend$_registerSourceEndpoint:
+ _objc_msgSend$_sharedInstance
+ _objc_msgSend$_signatureForBlockAtArgumentIndex:
+ _objc_msgSend$_watchdog:terminationRequestForError:
+ _objc_msgSend$_workspace
+ _objc_msgSend$activeOrientationDidUpdate:
+ _objc_msgSend$arguments
+ _objc_msgSend$background
+ _objc_msgSend$blockArguments
+ _objc_msgSend$blockReturnValue
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bs_getValue:ofSize:
+ _objc_msgSend$cancel
+ _objc_msgSend$cannotResolveForReason:
+ _objc_msgSend$charValue
+ _objc_msgSend$classForCoder
+ _objc_msgSend$coder
+ _objc_msgSend$compatibleWithTarget:
+ _objc_msgSend$copyApplyingDiff:
+ _objc_msgSend$decodeCollectionOfClass:containingClass:forKey:
+ _objc_msgSend$decodeDictionaryOfClass:forKey:
+ _objc_msgSend$decodeUInt64ForKey:
+ _objc_msgSend$diffByApplyingDiff:toDiff:
+ _objc_msgSend$disablesClientBatching
+ _objc_msgSend$domainForIdentifier:
+ _objc_msgSend$encodeUInt64:forKey:
+ _objc_msgSend$enumerateObjectsWithBlock:
+ _objc_msgSend$enumerateSortedWithBlock:
+ _objc_msgSend$extension
+ _objc_msgSend$fbs_getObjectForValue:atIndex:
+ _objc_msgSend$getArgument:atIndex:
+ _objc_msgSend$handleForAuditToken:error:
+ _objc_msgSend$handleForIdentifier:pidVersion:error:
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$indexOfObjectIdenticalTo:
+ _objc_msgSend$initWithComponent:extension:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$invalidate:
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invokeWithReceiver:replyHandler:
+ _objc_msgSend$invokeWithTarget:
+ _objc_msgSend$isBlock
+ _objc_msgSend$isDefaultShellEndpointEnabled
+ _objc_msgSend$isEndpointMonitoringEnabled
+ _objc_msgSend$isObject
+ _objc_msgSend$isVoid
+ _objc_msgSend$jetsamPriority
+ _objc_msgSend$lastArgument
+ _objc_msgSend$launchIdentifiers
+ _objc_msgSend$layer
+ _objc_msgSend$localServiceWithIdentifier:
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$methodForSelector:
+ _objc_msgSend$methodSignature
+ _objc_msgSend$numberOfArguments
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$objectContainedClasses
+ _objc_msgSend$performAfter:withBlock:
+ _objc_msgSend$performAsyncAndWait:
+ _objc_msgSend$pseudoSceneWithIdentifier:specification:
+ _objc_msgSend$queueWithDispatchQueue:targetQueue:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$registerOrientationInterest:completion:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$requestActiveOrientation
+ _objc_msgSend$requestActiveOrientationCompletion:
+ _objc_msgSend$resolve
+ _objc_msgSend$returnValue
+ _objc_msgSend$scene:invalidateWithTransitionContext:
+ _objc_msgSend$scene:sendInvocation:
+ _objc_msgSend$sceneID:handleInvocation:completion:
+ _objc_msgSend$sceneID:invalidateWithContext:clientError:
+ _objc_msgSend$sendBatchedMessages
+ _objc_msgSend$sendInvocation:
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setDefaultShellEndpointEnabled:
+ _objc_msgSend$setEndpointMonitoringEnabled:
+ _objc_msgSend$setJetsamPriority:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setSupportedCodings:
+ _objc_msgSend$setUpdateCompletions:
+ _objc_msgSend$shortValue
+ _objc_msgSend$signatureWithObjCTypes:
+ _objc_msgSend$sliceWithType:subtype:
+ _objc_msgSend$startWorkspaceDomainListener
+ _objc_msgSend$stringValue
+ _objc_msgSend$targetForInvocation:
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$updateClientSettings:withTransitionContext:
+ _objc_msgSend$updateCompletions
+ _objc_msgSend$versionedPID
+ _objc_msgSend$viewServiceConfiguration
+ _property_copyAttributeList
+ _soft_CALayerGetRenderId
+ _soft_CALayerGetRenderId.cold.1
- +[FBSDispatchSerialQueue _mainQueue]
- +[FBSDispatchSerialQueue _mainQueue].cold.1
- +[FBSPseudoSceneUpdater sharedInstance]
- +[FBSPseudoSceneUpdater sharedInstance].cold.1
- +[FBSScene pseudoSceneWithIdentifier:specification:].cold.1
- +[FBSScene pseudoSceneWithIdentifier:specification:].cold.2
- +[FBSSerialQueue _queueWithSerialDispatchQueue:]
- +[FBSSerialQueue _queueWithSerialDispatchQueue:].cold.1
- +[FBSSerialQueue mainDispatchQueue]
- +[FBSSerialQueue queueWithDispatchQueue:]
- +[FBSSerialQueue queueWithDispatchQueue:].cold.1
- +[FBSSerialQueue queueWithDispatchQueue:].cold.2
- +[FBSSerialQueue queueWithMainRunLoopModes:]
- +[FBSSerialQueue queueWithMainRunLoopModes:].cold.1
- +[FBSSerialQueue queueWithMainRunLoopModes:].cold.2
- +[FBSWorkspace _registerBlockForWorkspaceCreation:]
- +[FBSWorkspace _sharedWorkspaceIfExists]
- -[FBSDispatchSerialQueue .cxx_destruct]
- -[FBSDispatchSerialQueue _initWithQueue:]
- -[FBSDispatchSerialQueue assertBarrierOnQueue]
- -[FBSDispatchSerialQueue assertBarrierOnQueue].cold.1
- -[FBSDispatchSerialQueue backingQueueIfExists]
- -[FBSDispatchSerialQueue description]
- -[FBSDispatchSerialQueue hash]
- -[FBSDispatchSerialQueue isEqual:]
- -[FBSDispatchSerialQueue performAfter:withBlock:]
- -[FBSDispatchSerialQueue performAsync:]
- -[FBSDispatchSerialQueue performAsync:withHandoff:]
- -[FBSMainRunLoopSerialQueue .cxx_destruct]
- -[FBSMainRunLoopSerialQueue _initWithModes:]
- -[FBSMainRunLoopSerialQueue _initWithModes:].cold.1
- -[FBSMainRunLoopSerialQueue _initWithModes:].cold.2
- -[FBSMainRunLoopSerialQueue _performNextFromRunLoopSource]
- -[FBSMainRunLoopSerialQueue _queue_performAsync:]
- -[FBSMainRunLoopSerialQueue _targetQueue_performNextIfPossible]
- -[FBSMainRunLoopSerialQueue assertBarrierOnQueue]
- -[FBSMainRunLoopSerialQueue assertBarrierOnQueue].cold.1
- -[FBSMainRunLoopSerialQueue dealloc]
- -[FBSMainRunLoopSerialQueue description]
- -[FBSMainRunLoopSerialQueue hash]
- -[FBSMainRunLoopSerialQueue isEqual:]
- -[FBSMainRunLoopSerialQueue performAfter:withBlock:]
- -[FBSMainRunLoopSerialQueue performAsync:]
- -[FBSMainRunLoopSerialQueue performAsync:withHandoff:]
- -[FBSOrientationObserverClient _getActiveInterfaceOrientationSynchronously:withCompletion:]
- -[FBSOrientationObserverClient configureConnectMessage:]
- -[FBSOrientationObserverClient handleMessage:withType:]
- -[FBSOrientationObserverClient handleMessage:withType:].cold.1
- -[FBSOrientationObserverClient initWithDelegate:calloutQueue:]
- -[FBSProcess _watchdog:terminationRequestForViolatedProvision:error:]
- -[FBSScene _callOutQueue_coalesceClientSettingsUpdates:]
- -[FBSScene _callOutQueue_coalesceClientSettingsUpdates:].cold.1
- -[FBSScene invalidate].cold.1
- -[FBSSceneLayer initWithContextID:level:]
- -[FBSSceneLayer initWithContextID:level:].cold.1
- -[FBSSceneObserver initWithComponent:]
- -[FBSSceneSettingsCore jetsamMode]
- -[FBSSceneSettingsCore setJetsamMode:]
- -[FBSSerialQueue assertBarrierOnQueue]
- -[FBSSerialQueue assertOnQueue]
- -[FBSSerialQueue backingQueueIfExists]
- -[FBSSerialQueue init]
- -[FBSSerialQueue performAfter:withBlock:]
- -[FBSSerialQueue performAsync:]
- -[FBSSerialQueue performAsync:withHandoff:]
- -[FBSWorkspace _activate]
- -[FBSWorkspace _consumeSharedLock_activateWithAlreadyHeldLock:]
- -[FBSWorkspace _initWithOptions:]
- -[FBSWorkspace _initWithOptions:].cold.1
- -[FBSWorkspace _initWithOptions:].cold.2
- -[FBSWorkspace _initWithOptions:].cold.3
- -[FBSWorkspace _initWithOptions:].cold.4
- -[FBSWorkspace _initWithOptions:].cold.5
- -[FBSWorkspace serviceForEndpoint:withIdentifier:].cold.1
- -[FBSWorkspaceInitializationOptions _setStartsInactive:]
- -[FBSWorkspaceInitializationOptions _startsInactive]
- -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.1
- -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.2
- -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.3
- -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.4
- -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.5
- -[FBSWorkspaceServiceDispatchingQueue .cxx_destruct]
- -[FBSWorkspaceServiceDispatchingQueue _initWithTargetQueue:callOutQueue:]
- -[FBSWorkspaceServiceDispatchingQueue _initWithTargetQueue:callOutQueue:].cold.1
- -[FBSWorkspaceServiceDispatchingQueue _initWithTargetQueue:callOutQueue:].cold.2
- -[FBSWorkspaceServiceDispatchingQueue _initWithTargetQueue:callOutQueue:].cold.3
- -[FBSWorkspaceServiceDispatchingQueue assertBarrierOnQueue]
- -[FBSWorkspaceServiceDispatchingQueue backingQueueIfExists]
- -[FBSWorkspaceServiceDispatchingQueue performAsync:]
- -[FBSWorkspaceServiceDispatchingQueue performAsync:withHandoff:]
- GCC_except_table108
- GCC_except_table109
- GCC_except_table115
- GCC_except_table119
- GCC_except_table128
- GCC_except_table144
- GCC_except_table145
- GCC_except_table40
- GCC_except_table80
- GCC_except_table87
- GCC_except_table88
- _CFRunLoopAddSource
- _CFRunLoopGetMain
- _CFRunLoopSourceCreate
- _CFRunLoopSourceInvalidate
- _CFRunLoopSourceSignal
- _CFRunLoopWakeUp
- _FBSOrientationObserverMessageKeyDuration
- _FBSOrientationObserverMessageKeyOrientationInterest
- _FBSOrientationObserverMessageKeyRotationDirection
- _FBSOrientationObserverMessageKeySequenceNumber
- _FBSOrientationObserverMessageKeyUIOrientation
- _FBSOrientationObserverServiceIdentifier
- _FBSSerialQueueRunLoopSourceHandler
- _FBSViewServicesEntitlement
- _FBSWorkspaceInitialize.initialized
- _OBJC_CLASS_$_FBSDispatchSerialQueue
- _OBJC_CLASS_$_FBSMainRunLoopSerialQueue
- _OBJC_CLASS_$_FBSWorkspaceServiceDispatchingQueue
- _OBJC_IVAR_$_FBSDispatchSerialQueue._main
- _OBJC_IVAR_$_FBSDispatchSerialQueue._queue
- _OBJC_IVAR_$_FBSMainRunLoopSerialQueue._main_callingOut
- _OBJC_IVAR_$_FBSMainRunLoopSerialQueue._modes
- _OBJC_IVAR_$_FBSMainRunLoopSerialQueue._queue
- _OBJC_IVAR_$_FBSMainRunLoopSerialQueue._queue_blocks
- _OBJC_IVAR_$_FBSMainRunLoopSerialQueue._source
- _OBJC_IVAR_$_FBSOrientationObserver._freshestUpdate
- _OBJC_IVAR_$_FBSOrientationObserver._handler
- _OBJC_IVAR_$_FBSOrientationObserver._queue
- _OBJC_IVAR_$_FBSOrientationObserverClient._interest
- _OBJC_IVAR_$_FBSWorkspaceInitializationOptions._startsInactive
- _OBJC_IVAR_$_FBSWorkspaceServiceDispatchingQueue._callOutQueue
- _OBJC_IVAR_$_FBSWorkspaceServiceDispatchingQueue._targetQueue
- _OBJC_METACLASS_$_FBSDispatchSerialQueue
- _OBJC_METACLASS_$_FBSMainRunLoopSerialQueue
- _OBJC_METACLASS_$_FBSWorkspaceServiceDispatchingQueue
- __MergedGlobals
- __OBJC_$_CLASS_METHODS_FBSPseudoSceneUpdater
- __OBJC_$_CLASS_METHODS_FBSSerialQueue
- __OBJC_$_INSTANCE_METHODS_FBSDispatchSerialQueue
- __OBJC_$_INSTANCE_METHODS_FBSMainRunLoopSerialQueue
- __OBJC_$_INSTANCE_METHODS_FBSSerialQueue
- __OBJC_$_INSTANCE_METHODS_FBSWorkspaceServiceDispatchingQueue
- __OBJC_$_INSTANCE_VARIABLES_FBSDispatchSerialQueue
- __OBJC_$_INSTANCE_VARIABLES_FBSMainRunLoopSerialQueue
- __OBJC_$_INSTANCE_VARIABLES_FBSWorkspaceServiceDispatchingQueue
- __OBJC_$_PROP_LIST_FBSProcess.112
- __OBJC_$_PROP_LIST_FBSSceneSettings.192
- __OBJC_$_PROP_LIST_FBSSceneTransitionContext.165
- __OBJC_$_PROP_LIST_FBSSerialQueue
- __OBJC_$_PROP_LIST_FBSWorkspaceServiceDispatchingQueue
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_REFS_BSServiceDispatchingQueue
- __OBJC_CLASS_PROTOCOLS_$_FBSSerialQueue
- __OBJC_CLASS_PROTOCOLS_$_FBSWorkspaceServiceDispatchingQueue
- __OBJC_CLASS_RO_$_FBSDispatchSerialQueue
- __OBJC_CLASS_RO_$_FBSMainRunLoopSerialQueue
- __OBJC_CLASS_RO_$_FBSWorkspaceServiceDispatchingQueue
- __OBJC_LABEL_PROTOCOL_$_BSServiceDispatchingQueue
- __OBJC_METACLASS_RO_$_FBSDispatchSerialQueue
- __OBJC_METACLASS_RO_$_FBSMainRunLoopSerialQueue
- __OBJC_METACLASS_RO_$_FBSWorkspaceServiceDispatchingQueue
- __OBJC_PROTOCOL_$_BSServiceDispatchingQueue
- __QOSClassForFBSDisplayLayoutQOS
- ___33-[FBSOrientationObserver handler]_block_invoke
- ___36+[FBSDispatchSerialQueue _mainQueue]_block_invoke
- ___36-[FBSOrientationObserver invalidate]_block_invoke
- ___37-[FBSOrientationObserver setHandler:]_block_invoke
- ___39+[FBSPseudoSceneUpdater sharedInstance]_block_invoke
- ___40-[FBSMainRunLoopSerialQueue description]_block_invoke
- ___41+[FBSSerialQueue queueWithDispatchQueue:]_block_invoke
- ___42-[FBSMainRunLoopSerialQueue performAsync:]_block_invoke
- ___42-[FBSServiceFacilityClient _lock_activate]_block_invoke.91
- ___43-[FBSWorkspace monitor:didReceiveEndpoint:]_block_invoke
- ___46-[FBSWorkspaceService sendActions:completion:]_block_invoke.270
- ___46-[FBSWorkspaceService sendActions:completion:]_block_invoke.cold.2
- ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.31
- ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.33
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.157
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.164
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.167
- ___51-[FBSWorkspaceScenesClient sendActions:completion:]_block_invoke_2
- ___52-[FBSMainRunLoopSerialQueue performAfter:withBlock:]_block_invoke
- ___52-[FBSScene updateClientSettingsWithTransitionBlock:]_block_invoke
- ___52-[FBSWorkspaceServiceDispatchingQueue performAsync:]_block_invoke
- ___58-[FBSOrientationObserver handleOrientationResetForClient:]_block_invoke
- ___58-[FBSOrientationObserverClient activeInterfaceOrientation]_block_invoke
- ___59-[FBSWorkspaceScenesClient scene:sendMessage:withResponse:]_block_invoke_10
- ___59-[FBSWorkspaceScenesClient scene:sendMessage:withResponse:]_block_invoke_7
- ___59-[FBSWorkspaceScenesClient scene:sendMessage:withResponse:]_block_invoke_8
- ___59-[FBSWorkspaceScenesClient scene:sendMessage:withResponse:]_block_invoke_9
- ___59-[FBSWorkspaceScenesClient sceneID:sendMessage:completion:]_block_invoke_3
- ___60-[FBSOrientationObserverClient registerOrientationInterest:]_block_invoke_2
- ___60-[FBSWorkspaceScenesClient createSceneFutureWithDefinition:]_block_invoke.141
- ___62-[FBSOrientationObserver _getAndSetFreshestUpdateGivenUpdate:]_block_invoke
- ___62-[FBSOrientationObserver _getAndSetFreshestUpdateGivenUpdate:]_block_invoke.cold.1
- ___62-[FBSOrientationObserverClient initWithDelegate:calloutQueue:]_block_invoke
- ___63-[FBSMainRunLoopSerialQueue _targetQueue_performNextIfPossible]_block_invoke
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.153
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.157
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.162
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_2.163
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_3.cold.1
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_3.cold.2
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_3.cold.3
- ___63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke_4
- ___63-[FBSWorkspaceScenesClient willTerminateWithTransitionContext:]_block_invoke_2
- ___64-[FBSWorkspaceServiceDispatchingQueue performAsync:withHandoff:]_block_invoke
- ___71-[FBSWorkspaceScenesClient sceneID:sendActions:toExtension:completion:]_block_invoke_2
- ___71-[FBSWorkspaceScenesClient sceneID:sendActions:toExtension:completion:]_block_invoke_2.cold.1
- ___76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.146
- ___82-[FBSOpenApplicationService _openApplication:withOptions:clientHandle:completion:]_block_invoke.68
- ___82-[FBSOpenApplicationService _openApplication:withOptions:clientHandle:completion:]_block_invoke.68.cold.1
- ___84-[FBSWorkspaceScenesClient _queue_invalidateScene:withTransitionContext:completion:]_block_invoke_6
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.101
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.115
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.119
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_2.106
- ___91-[FBSOrientationObserverClient _getActiveInterfaceOrientationSynchronously:withCompletion:]_block_invoke
- ___91-[FBSOrientationObserverClient _getActiveInterfaceOrientationSynchronously:withCompletion:]_block_invoke.cold.1
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke.197
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke_2.198
- ___93-[FBSWorkspaceScenesClient _callOutQueue_sendDidCreateForScene:transitionContext:completion:]_block_invoke_2.cold.1
- ___94-[FBSWorkspaceScenesClient _queue_updateScene:withSettings:diff:transitionContext:completion:]_block_invoke.cold.1
- ___95-[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:]_block_invoke.221
- ___Block_byref_object_copy_.61
- ___Block_byref_object_dispose_.62
- ___FBSSERIALQUEUE_IS_CALLING_OUT_TO_A_BLOCK__
- ____ingestPropertiesFromSettingsSubclass_block_invoke.392
- ____realizeSettingsExtension_block_invoke.255
- ____realizeSettingsExtension_block_invoke.273
- ____realizeSettingsExtension_block_invoke.280
- ____realizeSettingsExtension_block_invoke.280.cold.1
- ____realizeSettingsExtension_block_invoke.280.cold.2
- ____realizeSettingsExtension_block_invoke.293
- ____realizeSettingsExtension_block_invoke_2.257
- ____realizeSettingsExtension_block_invoke_2.276
- ____realizeSettingsExtension_block_invoke_2.295
- ____realizeSettingsExtension_block_invoke_3.259
- ____realizeSettingsExtension_block_invoke_3.278
- ____realizeSettingsExtension_block_invoke_3.297
- ____realizeSettingsExtension_block_invoke_4.299
- ____realizeSettingsExtension_block_invoke_5.301
- ____realizeSettingsExtension_block_invoke_6.303
- ___block_descriptor_36_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_40_e8_32bs_e40_v16?0"<BSBlockSentinelSignalContext>"8ls32l8
- ___block_descriptor_40_e8_32r_e30_v16?0"FBSOrientationUpdate"8lr32l8
- ___block_descriptor_40_e8_32s_e23_v16?0"FBSXPCMessage"8ls32l8
- ___block_descriptor_41_e8_32s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e23_v16?0"FBSXPCMessage"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e41_v16?0"FBSWorkspaceSceneUpdateResponse"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e40_v16?0"<BSBlockSentinelSignalContext>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_literal_global.150
- ___block_literal_global.160
- ___block_literal_global.169
- ___block_literal_global.179
- ___block_literal_global.23
- __mainQueue.mainQueue
- __mainQueue.onceToken
- _dispatch_assert_queue_barrier
- _dispatch_async_and_wait
- _dispatch_block_create
- _kCFRunLoopCommonModes
- _objc_msgSend$_callOutQueue_coalesceClientSettingsUpdates:
- _objc_msgSend$_getActiveInterfaceOrientationSynchronously:withCompletion:
- _objc_msgSend$_queueWithSerialDispatchQueue:
- _objc_msgSend$_sharedWorkspaceIfExists
- _objc_msgSend$_startsInactive
- _objc_msgSend$_watchdog:terminationRequestForViolatedProvision:error:
- _objc_msgSend$appendQueue:withName:
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$assertOnQueue
- _objc_msgSend$backingQueueIfExists
- _objc_msgSend$initWithComponent:
- _objc_msgSend$initWithDelegate:calloutQueue:
- _objc_msgSend$isFloatingPoint
- _objc_msgSend$loadRBSLaunchIdentifiers
- _objc_msgSend$monitor:didReceiveEndpoint:
- _objc_msgSend$performAsync:withHandoff:
- _objc_msgSend$setHandler:
- _objc_msgSend$setTargetQueue:
- _objc_msgSend$startListener
- _sharedInstance.updater
- _xpc_dictionary_handoff_reply
CStrings:
+ "(invoked)"
+ "(unknown - %li)"
+ "-[<%@> %@]"
+ "-[FBSInvocation _invokeWithTarget:loggingID:replyHandler:]"
+ "-[FBSInvocation initWithInvocation:interface:]_block_invoke"
+ "0x%llx"
+ ":16@0:8"
+ "<%@; type: %d; subtype: %d>"
+ "<%p>: activeInterfaceOrientationWithCompletion error: %{public}@"
+ "<FBSWorkspaceScenesClient:%p %@> is explicitly invalidated"
+ "@\"BSObjCProtocol\""
+ "@\"BSServiceCompoundQueue\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceQueue\""
+ "@\"BSServiceQueue\"16@0:8"
+ "@\"BSXPCCoder\""
+ "@\"FBSOrientationUpdate\"16@0:8"
+ "@\"FBSProcessTerminationRequest\"32@0:8@\"FBSProcessWatchdog\"16@\"NSError\"24"
+ "@\"FBSPseudoSceneUpdater\""
+ "@20@0:8i16"
+ "@24@0:8@\"FBSInvocation\"16"
+ "@24@0:8@\"Protocol\"16"
+ "@24@0:8i16i20"
+ "@32@0:8@16q24"
+ "@36@0:8I16Q20d28"
+ "An exception was thrown while decoding."
+ "An underlying error occurred."
+ "B24@?0@\"FBSInvocation\"8@\"<BSXPCEncoding>\"16"
+ "BSServiceQueue"
+ "BSXPCAutoCoding"
+ "C"
+ "CALayerGetRenderId"
+ "Cannot activate an invalidated client. Create a new client."
+ "Connection failed."
+ "Created %@"
+ "Creating orientation service connection with %@"
+ "Destroy failed."
+ "Exception caught decoding parameters in reply block for %@: %@"
+ "Exception caught decoding parameters of %{public}@: %{public}@"
+ "FBLocalSynchronousSceneClientProvider"
+ "FBSComponentSceneSupport"
+ "FBSInvocation"
+ "FBSInvocation.m"
+ "FBSInvocationReceiving"
+ "FBSInvocationReply"
+ "FBSInvocationSending"
+ "FBSInvocationTarget"
+ "FBSMutableSceneUpdate"
+ "FBSOrientationObserverClient.m"
+ "FBSOrientationObserverClientCallout"
+ "FBSOrientationServiceClientInterface"
+ "FBSOrientationServiceServerInterface"
+ "FBSOrientationServiceSpecification"
+ "FBSPlistCollection"
+ "FBSProcessExecutableSlice"
+ "FBSSceneJetsamModeIsValid(mode)"
+ "FBSSceneJetsamPriority FBSSceneJetsamPriorityCreate(FBSSceneJetsamMode, FBSSceneResourceElevation)"
+ "FBSSceneResources.m"
+ "FBSSceneTransitionContext.m"
+ "FBSWorkspace can't find launchIdentifier for viewService domain. Connections using `identityForManagedEndpointOfProcessIdentity:` may behave oddly."
+ "FBSWorkspace cannot connect peer due to previous invalidation : %@"
+ "FBSWorkspace failed to start FBWorkspaceDomain. Connections using `identityForManagedEndpointOfProcessIdentity:` may behave oddly or not at all."
+ "FBSWorkspace ignoring registration of source after invalidation : %@"
+ "FBSWorkspace: default shell endpoint is disabled."
+ "FBSWorkspace: endpoint monitoring is disabled."
+ "FBSWorkspace:%p deallocing."
+ "FBSWorkspace:%p invalidating."
+ "FBSWorkspaceCoupler"
+ "FBSWorkspaceCoupler:%p deallocing."
+ "FBSWorkspaceCoupler:%p invalidating."
+ "Failed to decode CF object from xpc object in %@"
+ "Failed to resolve default shell endpoint for %{public}@."
+ "Invalid scene."
+ "Invocation failed."
+ "Invocation failed: %@"
+ "Invocation has already been resolved"
+ "Invocation of @selector(%@) was dropped."
+ "Method encoding mismatch"
+ "No FBSScene exists for provided identity."
+ "No associated method was found for invocation of %@"
+ "No extension named \"%@\" exists."
+ "No method found for @selector(%{public}@) in <%{public}@>"
+ "No protocol found for \"%@\""
+ "No receiver found for this message."
+ "No scene exists for identity: %{public}@"
+ "No selector \"%@\" found in <%@>"
+ "No selector found for \"%@\""
+ "Parameter is not supported: %@"
+ "Property \"%@\" of extension \"%@\" is inappropriately implemented with a backing ivar. Was this an accidental auto-synthesis?"
+ "Pseudo scenes do not support sending invocations"
+ "RVv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Receiver does not implement selector."
+ "Reply block deallocated without being called"
+ "Response not possible."
+ "S16@0:8"
+ "Scene is not currently connected."
+ "Scene is not valid"
+ "Scene remnant does not exist"
+ "SceneInvocation"
+ "SynchronousLocalSupport"
+ "T@\"BSServiceDispatchQueue\",R,N"
+ "T@\"BSServiceQueue\",&,N,V_callOutQueue"
+ "T@\"BSServiceQueue\",R,N"
+ "T@\"BSServiceQueue\",R,N,V_queue"
+ "T@\"FBSSceneTransitionContext\",C,D,N"
+ "T@\"FBSSettings<FBSMutableSettings>\",C,D,N"
+ "T@\"FBSSettingsDiff\",C,D,N"
+ "T@\"NSArray\",?,C,D,N"
+ "T@\"NSArray\",?,C,N"
+ "T@\"NSError\",&,D,N"
+ "TB,D,N"
+ "TB,D,N,GisBarrier"
+ "TB,N,GisBarrier"
+ "TB,N,GisDefaultShellEndpointEnabled,V_defaultShellEndpointEnabled"
+ "TB,N,GisEndpointMonitoringEnabled,V_endpointMonitoringEnabled"
+ "TB,R,N,V_disableFrameDoubling"
+ "TQ,R,D,N"
+ "TS,D,N"
+ "TS,N"
+ "TS,R,D,N"
+ "Tc,D,N"
+ "Tc,R,N"
+ "Ti,R,N,V_subtype"
+ "Ti,R,N,V_type"
+ "Unable to create endpoint for machName %{public}@, service: %{public}@."
+ "Unable to decode invocation."
+ "Unable to decode struct: %@"
+ "Unable to handle invocation."
+ "Unable to route invocation."
+ "Unsupported parameter: %@"
+ "Update failed."
+ "Value for '%@' was of unexpected class %@. Expected %@."
+ "Value for '%@' was unexpectedly nil. Expected %@."
+ "Vv24@0:8@\"FBSOrientationUpdate\"16"
+ "Vv24@0:8@?16"
+ "Vv24@0:8@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">16"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">24"
+ "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSInvocation\"24@?<v@?@\"FBSInvocationReply\"@\"NSError\">32"
+ "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\"@\"NSError\">32"
+ "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneTransitionContext\"24@\"NSError\"32"
+ "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneTransitionContext\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32"
+ "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneParameters<__nonnull__>\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "[%{public}@] Ignoring update for disconnected scene."
+ "[%{public}@] Invoking %{public}@ on target: %{public}@"
+ "[%{public}@] No matching scene to invalidate for this identity."
+ "[%{public}@] Pseudo scenes do not support sending invocations."
+ "[%{public}@] Scene create completion block was not called. Working around what is likely rdar://62751231."
+ "[+%d]"
+ "[3@\"BSServiceDispatchQueue\"]"
+ "[_bs_assert_object isKindOfClass:BSServiceQueueClass]"
+ "[arguments count] == ([signature numberOfArguments] - blockOffset)"
+ "[replyArguments count] == (numberOfArguments - 1)"
+ "_FBSScenesClientHostEvent"
+ "__PreferredCPU"
+ "_cTypeString"
+ "_callOutQueue_ensureCoalesceClientSettingsUpdates:"
+ "_callOutQueue_maybeCoalesceClientSettingsUpdates:"
+ "_callout_updateDepth"
+ "_canCoalesce"
+ "_classForObjectAtArgumentIndex:"
+ "_connectionActivated:"
+ "_connectionInvalidated:"
+ "_createReplyBlockWithSignature:arguments:handler:"
+ "_defaultShellEndpointEnabled"
+ "_disableEndpointMonitoring"
+ "_disableFrameDoubling"
+ "_encoding"
+ "_endpointMonitoringEnabled"
+ "_enqueueClientConnectionBlock:"
+ "_executeCalloutFromHostEvent:withBlock:"
+ "_findDomainSpecification"
+ "_hostEventLock"
+ "_hostEvent_pendingEvents"
+ "_initWithCallOutQueue:"
+ "_initWithClient:callbackQueue:"
+ "_initWithCoupler:options:"
+ "_initWithEndpoint:calloutQueue:delegate:"
+ "_invalidateWithCompletion:"
+ "_invokeWithTarget:loggingID:replyHandler:"
+ "_invoked"
+ "_isSharedInstance"
+ "_isSingleton"
+ "_lock_clientConnectionBlocks"
+ "_lock_freshestUpdate"
+ "_lock_getAndSetFreshestUpdateGivenUpdate:"
+ "_lock_handler"
+ "_lock_interest"
+ "_lock_remoteTarget"
+ "_lock_setHandler:"
+ "_lock_workspace"
+ "_objects"
+ "_protocolName"
+ "_psuedoSceneUpdater"
+ "_queue_invalidateScene:withTransitionContext:completion:"
+ "_queue_invalidated"
+ "_queue_updateScene:withSettings:diff:transitionContext:completion:"
+ "_renderID"
+ "_resolved"
+ "_selectorName"
+ "_setDelegate:"
+ "_setWorkspace:"
+ "_sharedInstance"
+ "_signatureForBlockAtArgumentIndex:"
+ "_subtype"
+ "_watchdog:terminationRequestForError:"
+ "a block can only be the last argument of a message"
+ "activeOrientationDidUpdate:"
+ "addUpdateCompletion:"
+ "after invalidation, we should be killing all internal registration attempts before we get here"
+ "arguments"
+ "arm64"
+ "arm64_(%i)"
+ "arm64_all"
+ "arm64_any"
+ "arm64e"
+ "arm64v8"
+ "attempt to access _workspace on coupler before the workspace has checked in"
+ "awakeFromCoder"
+ "barrier"
+ "block != ((void *)0)"
+ "block argument is a collection but does not define a contained class"
+ "block is not the last argument"
+ "block may only be the last argument"
+ "block return value is not void"
+ "block signature returned nil"
+ "blockArguments"
+ "blockReturnValue"
+ "blocks may not contain other blocks"
+ "boolForKey:"
+ "bs_getValue:ofSize:"
+ "cannot begin a new update re-entrantly"
+ "cannot decode parameters due to unrealized specification class with name '%@'. Is this specification class exposed to the client?"
+ "cannot send invocations until activated"
+ "cannot set workspace on invalid coupler : coupler=%@ workspace=%p"
+ "cannotResolveForReason:"
+ "captureCompletions"
+ "charValue"
+ "classForCoder"
+ "coalesceEvent:skipped:"
+ "coder"
+ "com.apple.frontboard.orientation-observer"
+ "compatibleWithTarget:"
+ "copyApplyingDiff:"
+ "coupler"
+ "deallocation of un-resolved invocation"
+ "decodeCollectionOfClass:containingClass:forKey:"
+ "decodeDictionaryOfClass:forKey:"
+ "decodeUInt64ForKey:"
+ "decodeWithCoder:"
+ "defaultShellEndpointEnabled"
+ "diff"
+ "diff class mismatch"
+ "diffByApplyingDiff:toDiff:"
+ "disableFrameDoubling"
+ "disablesClientBatching"
+ "domain containing workspace-service is not part of viewServiceConfiguration : found=%@ config=%@"
+ "domain differs from the one actually started : started=%@ discovered=%@"
+ "domainForIdentifier:"
+ "elevated"
+ "encodeUInt64:forKey:"
+ "endpointMonitoringEnabled"
+ "enumerateObjectsWithBlock:"
+ "enumerateSortedWithBlock:"
+ "event != ((void *)0)"
+ "event != self"
+ "event deallocated with a completion"
+ "expected != nil"
+ "explicit flush"
+ "f16@?0@\"FBSSettings\"8"
+ "failed to find workspace-service defining domain"
+ "fbs_getObjectForValue:atIndex:"
+ "focal"
+ "getArgument:atIndex:"
+ "handleForAuditToken:error:"
+ "handleForIdentifier:pidVersion:error:"
+ "identifierWithPid:"
+ "identity not set on coalescable event"
+ "idle"
+ "if present, the next event is always at index 0"
+ "if we own the defaultShellMachName (%@) then %@ must be registered there"
+ "indexOfObjectIdenticalTo:"
+ "initWithCAContextID:renderID:level:"
+ "initWithComponent:extension:"
+ "initWithContextID:renderID:level:"
+ "initWithDelegate:"
+ "initWithInvocation:interface:"
+ "invalidate:"
+ "invocation"
+ "invocation was invoked twice"
+ "invocationWithMethodSignature:"
+ "invokeWithReceiver:replyHandler:"
+ "invokeWithTarget:"
+ "invokeWithTarget:replyHandler:"
+ "invoked"
+ "isActive"
+ "isBarrier"
+ "isBlock"
+ "isDefaultShellEndpointEnabled"
+ "isEndpointMonitoringEnabled"
+ "isObject"
+ "isVoid"
+ "jetsamPriority"
+ "lastArgument"
+ "launchIdentifiers"
+ "localService"
+ "localServiceWithIdentifier:"
+ "longLongValue"
+ "longValue"
+ "machQueue"
+ "membersForCoder"
+ "method"
+ "method argument is a collection but does not define a contained class"
+ "method return value must be void"
+ "methodForSelector:"
+ "methodSignature"
+ "must have one and only one domain specify %@ : bootstrapConfigurationDomains=%@"
+ "must have one and only one domain specify %@ : viewServiceConfigurationDomains=%@"
+ "must invalidate before dealloc"
+ "no method found for %@ in %@"
+ "no value class found for dictionary parameter"
+ "non-plist collections are not yet supported; see __FBSPlistCollection__"
+ "numberOfArguments"
+ "numberWithFloat:"
+ "numberWithLong:"
+ "numberWithLongLong:"
+ "numberWithShort:"
+ "numberWithUnsignedShort:"
+ "objectContainedClasses"
+ "only void returning methods are supported"
+ "outSkipped != ((void*)0)"
+ "parameter type is not supported"
+ "parent"
+ "performAsyncAndWait:"
+ "priority"
+ "queueWithDispatchQueue:targetQueue:"
+ "queueWithName:serviceQuality:"
+ "registerOrientationInterest:completion:"
+ "remoteTargetForProtocol:"
+ "removeObjectsInArray:"
+ "renderID"
+ "reply handler is expected"
+ "requestActiveOrientation"
+ "requestActiveOrientationCompletion:"
+ "resolve"
+ "return value is not void for @selector(%@) in <%@>"
+ "returnValue"
+ "rid"
+ "scene opts out of batching"
+ "scene:invalidateWithTransitionContext:"
+ "scene:sendInvocation:"
+ "sceneID:handleInvocation:completion:"
+ "sceneID:invalidateWithContext:clientError:"
+ "selectorName"
+ "sendBatchedMessages"
+ "sendInvocation:"
+ "setArgument:atIndex:"
+ "setBarrier:"
+ "setDefaultShellEndpointEnabled:"
+ "setDisableFrameDoubling:"
+ "setEndpointMonitoringEnabled:"
+ "setJetsamPriority:"
+ "setPreviousSettings:"
+ "setSelector:"
+ "setSupportedCodings:"
+ "setUpdateCompletions:"
+ "setValue:forKey:"
+ "shortValue"
+ "signature"
+ "signatureWithObjCTypes:"
+ "sliceWithType:"
+ "sliceWithType:subtype:"
+ "startViewServiceDomain"
+ "startWorkspaceDomainListener"
+ "stringValue"
+ "struct is too large"
+ "struct is too large: %@"
+ "subtype"
+ "targetForInvocation:"
+ "targetWithInterface:handler:"
+ "this instance may not invalidate"
+ "this process does not link FrontBoard so cannot utilize the local workspace service"
+ "too many nested updates"
+ "transition context deallocated with dangling completions"
+ "uint64_t soft_CALayerGetRenderId(CALayer *__strong)"
+ "unsignedCharValue"
+ "updateCompletions"
+ "v16@?0@\"<BSXPCAutoCodingConfiguring>\"8"
+ "v16@?0@\"FBSMutableSceneParameters\"8"
+ "v16@?0@\"NSInvocation\"8"
+ "v20@0:8S16"
+ "v20@?0@\"FBSSettings\"8f16"
+ "v24@0:8@\"FBSInvocation\"16"
+ "v24@0:8@\"NSObject<BSXPCDecoding>\"16"
+ "v24@0:8@\"NSObject<BSXPCEncoding>\"16"
+ "v24@?0@\"FBSInvocationReply\"8@\"NSError\"16"
+ "v24@?0@\"FBSOrientationUpdate\"8@\"NSError\"16"
+ "v32@0:8@\"FBSScene\"16@\"FBSInvocation\"24"
+ "v32@0:8@\"FBSScene\"16@\"FBSSceneTransitionContext\"24"
+ "v32@0:8@\"NSSet\"16#24"
+ "v32@?0Q8@16^B24"
+ "versionedPID"
+ "viewServiceConfiguration"
+ "void _vetProtocolMethod(BSObjCMethod *__strong _Nonnull)"
+ "workspace already set on coupler : coupler=%@ existing=%p new=%p"
- "\r"
- "<%p>: _getActiveInterfaceOrientationSynchronously:withCompletion - nil reply payload."
- "<%p>: handleMessage:withType: - invalid sequenceNumber: %lu for orientation change."
- "@\"<BSServiceDispatchingQueue>\""
- "@\"FBSProcessTerminationRequest\"40@0:8@\"FBSProcessWatchdog\"16@\"FBSProcessExecutionProvision\"24@\"NSError\"32"
- "@\"FBSSerialQueue\""
- "@\"FBSSerialQueue\"16@0:8"
- "BSServiceDispatchingQueue"
- "FBSDispatchSerialQueue"
- "FBSMainRunLoopSerialQueue"
- "FBSSerialQueue.m"
- "FBSWorkspace failed to start FBWorkspaceDomain. Connections using `identityForManagedEndpointOfProcessIdentity:` may behave oddly."
- "FBSWorkspaceService cannot be used until the core FBSWorkspace is initialized"
- "FBSWorkspaceServiceDispatchingQueue"
- "Failed to resolve default shell endpoint for %{public}@. This workspace way have limited functionality."
- "No FBSScene exists with provided identifier"
- "RVv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "T@\"FBSSerialQueue\",&,N,V_callOutQueue"
- "T@\"FBSSerialQueue\",R,N,V_queue"
- "T@\"NSError\",?,&,D,N"
- "TB,N,S_setStartsInactive:,V_startsInactive"
- "Vv40@0:8@\"FBSSceneIdentity\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\"@\"NSError\">32"
- "Vv40@0:8@\"FBSSceneIdentity\"16@\"FBSSceneTransitionContext\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"FBSSceneIdentity\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32"
- "Vv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneParameters\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"FBSSceneIdentity\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "[3@\"NSObject<OS_dispatch_queue>\"]"
- "[_bs_assert_object isKindOfClass:FBSSerialQueueClass]"
- "[modes count] > 0"
- "^{__CFRunLoopSource=}"
- "_activate"
- "_callOutQueue_coalesceClientSettingsUpdates:"
- "_freshestUpdate"
- "_getActiveInterfaceOrientationSynchronously:withCompletion:"
- "_initWithModes:"
- "_initWithOptions:"
- "_initWithTargetQueue:callOutQueue:"
- "_interest"
- "_main"
- "_main_callingOut"
- "_modes"
- "_queueWithSerialDispatchQueue:"
- "_queue_blocks"
- "_registerBlockForWorkspaceCreation:"
- "_setStartsInactive:"
- "_sharedWorkspaceIfExists"
- "_startsInactive"
- "_targetQueue"
- "_watchdog:terminationRequestForViolatedProvision:error:"
- "appendQueue:withName:"
- "arrayWithCapacity:"
- "assertOnQueue"
- "backingQueueIfExists"
- "callingOut"
- "cannot call completion of sendActions to %@ without a reference to the workspace"
- "cannot decode parameters due to unrealized specification class with name '%@'"
- "com.apple.UIKit.vends-view-services"
- "com.apple.frontboardservices.orientation-observer"
- "com.apple.frontboardservices.orientationobserver"
- "dealloc is not allowed on FBSWorkspace"
- "dispatchQueue"
- "enqueued"
- "failed to create source"
- "failure in %@ of <%@:%p> (%@:%i)"
- "impossible to reconnect '%@' : remnant=%@"
- "initWithComponent:"
- "initWithContextID:level:"
- "initWithDelegate:calloutQueue:"
- "interest"
- "isFloatingPoint"
- "it is not (yet) appropriate to call -invalidate: on this scene"
- "loadRBSLaunchIdentifiers"
- "main"
- "mainDispatchQueue"
- "mode (%@) is not a string"
- "modes"
- "must have one and only one domain specify %@ : domains=%@"
- "not-found"
- "not-waiting"
- "performAsync:withHandoff:"
- "queueWithDispatchQueue:"
- "queueWithMainRunLoopModes:"
- "rotation-direction"
- "sequence-number"
- "serialQueue"
- "setTargetQueue:"
- "startListener"
- "targetQueue != ((void *)0)"
- "threading violation: expected the main thread"
- "uiorientation"
- "v28@0:8B16@?20"
- "v32@0:8@?<v@?>16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8d16@?24"

```
