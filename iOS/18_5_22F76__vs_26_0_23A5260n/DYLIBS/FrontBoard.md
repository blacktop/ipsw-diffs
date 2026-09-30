## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-943.6.1.0.0
-  __TEXT.__text: 0x83b88
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0x5c38
-  __TEXT.__const: 0x378
-  __TEXT.__cstring: 0xab61
-  __TEXT.__oslogstring: 0x58f5
-  __TEXT.__gcc_except_tab: 0x14b0
-  __TEXT.__dlopen_cstrs: 0x1b2
-  __TEXT.__unwind_info: 0x1fc0
-  __TEXT.__objc_classname: 0x10ed
-  __TEXT.__objc_methname: 0xf784
-  __TEXT.__objc_methtype: 0x38a7
-  __TEXT.__objc_stubs: 0xb3c0
-  __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0x26b8
+993.0.0.0.0
+  __TEXT.__text: 0x8c9bc
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x5b10
+  __TEXT.__const: 0x314
+  __TEXT.__cstring: 0xb0e4
+  __TEXT.__oslogstring: 0x5ea4
+  __TEXT.__gcc_except_tab: 0x18c8
+  __TEXT.__dlopen_cstrs: 0x20a
+  __TEXT.__unwind_info: 0x2170
+  __TEXT.__objc_classname: 0x11cf
+  __TEXT.__objc_methname: 0xf5e6
+  __TEXT.__objc_methtype: 0x3847
+  __TEXT.__objc_stubs: 0xb100
+  __DATA_CONST.__got: 0x900
+  __DATA_CONST.__const: 0x2708
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3798
+  __DATA_CONST.__objc_selrefs: 0x3780
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x818
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x86a0
-  __AUTH_CONST.__objc_const: 0xb590
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x8dc0
+  __AUTH_CONST.__objc_const: 0xb820
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x918
-  __DATA.__data: 0x1b00
-  __DATA.__bss: 0x238
-  __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0x1d0
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_ivar: 0x94c
+  __DATA.__data: 0x1d40
+  __DATA.__bss: 0x210
+  __DATA_DIRTY.__objc_data: 0xeb0
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50E42E97-14F8-3A6C-89C2-F17B92A375A3
-  Functions: 2958
-  Symbols:   10297
-  CStrings:  5866
+  UUID: 3996E018-DDF6-3A8E-8DE6-55CD78E038F4
+  Functions: 3046
+  Symbols:   10512
+  CStrings:  6022
 
Symbols:
+ +[FBLocalSynchronousSceneClientProvider(SharedInstance) sharedInstance]
+ +[FBProcess userInitiatedWorkloop]
+ +[FBProcess userInitiatedWorkloop].cold.1
+ +[FBSceneEventQueue executeWhenIdle:]
+ +[FBSceneEventQueue executeWhenIdle:].cold.1
+ +[FBSceneEventQueue isIdleWorkSuspended]
+ +[FBSceneEventQueue suspendIdleWorkForReason:]
+ +[FBSceneSynchronizer detachedSynchronizerWithIdentifier:]
+ +[FBSceneSynchronizer detachedSynchronizerWithIdentifier:].cold.1
+ +[FBSceneSynchronizer detachedSynchronizerWithIdentifier:].cold.2
+ +[FBSceneSynchronizer synchronizerForViewServiceWithProcessIdentifier:]
+ +[FBSceneSynchronizer synchronizerForViewServiceWithProcessIdentifier:].cold.1
+ +[FBSceneWorkspace workspaceWithIdentifier:].cold.1
+ +[FBServiceClientAuthenticator _authenticateAuditToken:entitlement:credentials:error:]
+ +[FBWorkspaceAssertionAttributes assertsVisibilityAttributes]
+ +[FBWorkspaceAssertionAttributes assertsVisibilityAttributes].cold.1
+ +[FBWorkspaceAssertionAttributes attributeForJetsamBand:]
+ +[FBWorkspaceAssertionAttributes baseAttributes]
+ +[FBWorkspaceAssertionAttributes baseAttributes].cold.1
+ +[FBWorkspaceDomain nullEndpoint]
+ +[FBWorkspaceDomain nullEndpoint].cold.1
+ +[FBWorkspaceDomain(Debugging) debugDescription]
+ +[FBWorkspaceDomain(FBSWorkspace) startWorkspaceDomainListener]
+ +[FBWorkspaceEventDispatcher callOutQueue]
+ -[FBInterfaceOrientationService initialize]
+ -[FBInterfaceOrientationService startService]
+ -[FBInterfaceOrientationServiceServer _connectionInvalidated:]
+ -[FBInterfaceOrientationServiceServer _currentConnection]
+ -[FBInterfaceOrientationServiceServer _initWithDomain:service:]
+ -[FBInterfaceOrientationServiceServer _lock_noteInterfaceOrientationChanged:animationSettings:direction:]
+ -[FBInterfaceOrientationServiceServer _lock_registerOrientationInterest:connection:completion:]
+ -[FBInterfaceOrientationServiceServer _lock_sendMessageToInterestedClients:]
+ -[FBInterfaceOrientationServiceServer connections]
+ -[FBInterfaceOrientationServiceServer initialize]
+ -[FBInterfaceOrientationServiceServer interestedConnections]
+ -[FBInterfaceOrientationServiceServer invalidate]
+ -[FBInterfaceOrientationServiceServer listener:didReceiveConnection:withContext:]
+ -[FBInterfaceOrientationServiceServer listener]
+ -[FBInterfaceOrientationServiceServer pendingConnections]
+ -[FBInterfaceOrientationServiceServer registerOrientationInterest:completion:]
+ -[FBInterfaceOrientationServiceServer requestActiveOrientationCompletion:]
+ -[FBInterfaceOrientationServiceServer requestActiveOrientation]
+ -[FBInterfaceOrientationServiceServer startService]
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:]
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:].cold.1
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:].cold.2
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:].cold.3
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:].cold.4
+ -[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:].cold.5
+ -[FBLocalSynchronousSceneClientProvider _invalidateSceneInfo:transitionContext:]
+ -[FBLocalSynchronousSceneClientProvider _invalidate]
+ -[FBLocalSynchronousSceneClientProvider _invalidate].cold.1
+ -[FBLocalSynchronousSceneClientProvider _invalidate].cold.2
+ -[FBLocalSynchronousSceneClientProvider _invalidate].cold.3
+ -[FBLocalSynchronousSceneClientProvider _invalidate].cold.4
+ -[FBLocalSynchronousSceneClientProvider _sendToHost:updatedClientSettings:withDiff:transitionContext:]
+ -[FBLocalSynchronousSceneClientProvider _sendToHost:updatedClientSettings:withDiff:transitionContext:].cold.1
+ -[FBLocalSynchronousSceneClientProvider _sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:]
+ -[FBLocalSynchronousSceneClientProvider _sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:].cold.1
+ -[FBLocalSynchronousSceneClientProvider _sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:].cold.2
+ -[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:]
+ -[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:].cold.1
+ -[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:].cold.2
+ -[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:].cold.3
+ -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:]
+ -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:].cold.1
+ -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:].cold.2
+ -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:].cold.3
+ -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:].cold.4
+ -[FBLocalSynchronousSceneClientProvider dealloc].cold.1
+ -[FBLocalSynchronousSceneClientProvider host:didInvalidateWithTransitionContext:completion:].cold.3
+ -[FBLocalSynchronousSceneClientProvider host:didReceiveActions:forExtension:].cold.1
+ -[FBLocalSynchronousSceneClientProvider host:didReceiveActions:forExtension:].cold.2
+ -[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:].cold.3
+ -[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:].cold.4
+ -[FBLocalSynchronousSceneClientProvider host:sendInvocation:withReply:]
+ -[FBLocalSynchronousSceneClientProvider host:sendInvocation:withReply:].cold.1
+ -[FBLocalSynchronousSceneClientProvider host:sendInvocation:withReply:].cold.2
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.16
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.17
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.18
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.19
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.20
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.21
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.22
+ -[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:].cold.23
+ -[FBLocalSynchronousSceneClientProvider requestSceneWithOptions:completion:].cold.2
+ -[FBLocalSynchronousSceneClientProvider scene:didReceiveActions:forExtension:].cold.1
+ -[FBLocalSynchronousSceneClientProvider scene:didReceiveActions:forExtension:].cold.2
+ -[FBLocalSynchronousSceneClientProvider scene:didUpdateClientSettings:withDiff:transitionContext:].cold.1
+ -[FBLocalSynchronousSceneClientProvider scene:didUpdateClientSettings:withDiff:transitionContext:].cold.2
+ -[FBLocalSynchronousSceneClientProvider scene:invalidateWithTransitionContext:]
+ -[FBLocalSynchronousSceneClientProvider scene:invalidateWithTransitionContext:].cold.1
+ -[FBLocalSynchronousSceneClientProvider scene:invalidateWithTransitionContext:].cold.2
+ -[FBLocalSynchronousSceneClientProvider scene:sendInvocation:]
+ -[FBLocalSynchronousSceneClientProvider scene:sendInvocation:].cold.1
+ -[FBLocalSynchronousSceneClientProvider scene:sendInvocation:].cold.2
+ -[FBLocalSynchronousSceneClientProvider scene:sendMessage:withResponse:].cold.1
+ -[FBLocalSynchronousSceneClientProvider sendBatchedMessages]
+ -[FBLocalSynchronousSceneClientProvider unregisterHost:].cold.3
+ -[FBLocalSynchronousSceneClientProvider unregisterHost:].cold.4
+ -[FBProcess _bootstrapAndExec].cold.4
+ -[FBProcess _initWithProcessManager:identity:handle:executionContext:]
+ -[FBProcess _initWithProcessManager:identity:handle:executionContext:].cold.1
+ -[FBProcess _initWithProcessManager:identity:handle:executionContext:].cold.2
+ -[FBProcess _watchdog:terminationRequestForError:]
+ -[FBProcess workspaceState]
+ -[FBProcessCPUStatistics initWithProcessHandle:].cold.3
+ -[FBProcessManager _bootstrapProcessWithHandle:synchronously:error:].cold.3
+ -[FBProcessManager _initWithWorkspaceDomain:]
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.1
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.2
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.3
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.4
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.5
+ -[FBProcessManager _initWithWorkspaceDomain:].cold.6
+ -[FBProcessManager _registerProcessForViewServiceWithProcessHandle:error:]
+ -[FBProcessManager dealloc].cold.1
+ -[FBProcessManager domain:didReceiveConnection:withContext:]
+ -[FBProcessManager domain:didReceiveConnection:withContext:].cold.1
+ -[FBProcessManager domain:didReceiveConnection:withContext:].cold.2
+ -[FBProcessManager eventDispatcher]
+ -[FBProcessManager incomingWorkspaceEndpoint]
+ -[FBProcessManager legacySceneManagerCreatingIfNecessary:]
+ -[FBProcessManager noteProcessAssertionStateDidChange:].cold.2
+ -[FBProcessManager registerProcessForAuditToken:].cold.3
+ -[FBProcessManager registerProcessForAuditToken:].cold.4
+ -[FBProcessManager registerProcessForAuditToken:].cold.5
+ -[FBProcessManager registerProcessForAuditToken:].cold.6
+ -[FBProcessManager syncLocalSceneClientProvider]
+ -[FBProcessWatchdog _getPolicyWallTime:cpuTime:]
+ -[FBProcessWatchdog activate].cold.1
+ -[FBProcessWatchdog deactivate]
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.4
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.5
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.6
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.7
+ -[FBScene _deactivateClient:withContext:]
+ -[FBScene _deactivateClient:withContext:].cold.1
+ -[FBScene _deactivateClient:withContext:].cold.2
+ -[FBScene _iterateObservers:]
+ -[FBScene clientToken:deactivateWithContext:]
+ -[FBScene clientToken:handleInvocation:withReply:]
+ -[FBScene hostProcess]
+ -[FBScene prepareSnapshotWithConfigurator:]
+ -[FBScene prepareSnapshot]
+ -[FBScene sendInvocation:]
+ -[FBScene sendInvocation:].cold.1
+ -[FBScene targetForInvocation:]
+ -[FBSceneEventQueue _noteQueueDidLock]
+ -[FBSceneEventQueue _relinquishIdleLockIfAppropriate]
+ -[FBSceneEventQueue executeOrAppend:]
+ -[FBSceneLayer initWithContextID:renderID:]
+ -[FBSceneLayer renderID]
+ -[FBSceneLayerManager _rebuildLayers]
+ -[FBSceneLayerManager _removeSuspendAssertion:]
+ -[FBSceneLayerManager _suspendUpdatesWithReason:]
+ -[FBSceneManager _initWithProcessManager:]
+ -[FBSceneManager _invalidate]
+ -[FBSceneManager _isSameAsWorkspace:]
+ -[FBSceneManager createScene:]
+ -[FBSceneManager dealloc].cold.1
+ -[FBSceneManagerObserver _initWithObserver:workspace:]
+ -[FBSceneManagerObserver initWithDelegate:workspace:]
+ -[FBSceneManagerObserver initWithObserver:workspace:]
+ -[FBSceneManagerObserver sceneManager:didCommitUpdateForScene:transactionID:]
+ -[FBSceneManagerObserver sceneManager:willCommitUpdateForScene:transactionID:]
+ -[FBSceneManagerObserver sceneManager:willUpdateScene:withSettings:transitionContext:]
+ -[FBSceneObserver initWithComponent:extension:]
+ -[FBSceneObserver receiverWantsInactiveUpdates]
+ -[FBSceneObserver sceneObserverWantsUpdatesFromInactiveScenes]
+ -[FBSceneSnapshot _baseTransformForSnapshotConfig:rootConfig:]
+ -[FBSceneSnapshot _collectLayersToSnapshotFromScene:withSnapshotConfig:rootConfig:]
+ -[FBSceneSnapshot _initWithScene:configuration:]
+ -[FBSceneSnapshot configuration]
+ -[FBSceneSnapshot initWithScene:context:]
+ -[FBSceneSnapshot scene]
+ -[FBSceneSnapshotContext applyContext:]
+ -[FBSceneSnapshotContext applyContext:].cold.1
+ -[FBSceneSnapshotContext clientAllowsProtectedContent]
+ -[FBSceneSnapshotContext initWithScene:configurator:]
+ -[FBSceneSnapshotContext initWithScene:configurator:].cold.1
+ -[FBSceneSnapshotContext setUserInfo:]
+ -[FBSceneSnapshotContext userInfo]
+ -[FBSceneSynchronizer .cxx_destruct]
+ -[FBSceneSynchronizer _dispatcher]
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:]
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:].cold.1
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:].cold.2
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:].cold.3
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:].cold.4
+ -[FBSceneSynchronizer _initWithIdentifier:workspaceQueue:dispatcher:].cold.5
+ -[FBSceneSynchronizer _setProcessHandle:]
+ -[FBSceneSynchronizer _setProcessHandle:].cold.1
+ -[FBSceneSynchronizer _setProcessHandle:].cold.2
+ -[FBSceneSynchronizer _setProcessHandle:].cold.3
+ -[FBSceneSynchronizer _setWaitingForConnect]
+ -[FBSceneSynchronizer _workspaceQueue]
+ -[FBSceneSynchronizer callOutQueue]
+ -[FBSceneSynchronizer description]
+ -[FBSceneSynchronizer machQueue]
+ -[FBSceneSynchronizer performAsyncOnSendingQueue:]
+ -[FBSceneSynchronizer processHandle]
+ -[FBSceneSynchronizer serviceQueue]
+ -[FBSceneWorkspace _initWithProcessManager:identifier:]
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.1
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.2
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.3
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.4
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.5
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.6
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.7
+ -[FBSceneWorkspace _initWithProcessManager:identifier:].cold.8
+ -[FBSceneWorkspace _iterateObservers:]
+ -[FBSceneWorkspace _legacyWorkspace]
+ -[FBSceneWorkspace didAddScene:]
+ -[FBSceneWorkspace didReceiveSceneRequest:fromHandle:].cold.2
+ -[FBSceneWorkspace didReceiveSceneRequest:fromHandle:].cold.3
+ -[FBSceneWorkspace didReceiveSceneRequest:fromHandle:].cold.4
+ -[FBSceneWorkspace initWithIdentifier:].cold.1
+ -[FBSceneWorkspace processManager]
+ -[FBSceneWorkspace scene:didApplyUpdate:]
+ -[FBSceneWorkspace scene:didCompleteUpdate:]
+ -[FBSceneWorkspace scene:didPrepareUpdate:]
+ -[FBSceneWorkspace scene:willUpdateSettings:]
+ -[FBSceneWorkspace sceneDidInvalidate:]
+ -[FBSceneWorkspace setIdentity:]
+ -[FBSceneWorkspace setIdentity:].cold.1
+ -[FBSceneWorkspace setIdentity:].cold.2
+ -[FBSceneWorkspace setIdentity:].cold.3
+ -[FBSceneWorkspace setIdentity:].cold.4
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:]
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:].cold.1
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:].cold.2
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:].cold.3
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:].cold.4
+ -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:].cold.5
+ -[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]
+ -[FBWorkspace _domain]
+ -[FBWorkspace _incomingEndpointPromise]
+ -[FBWorkspace _initWithDispatcher:process:]
+ -[FBWorkspace _initWithDispatcher:process:].cold.1
+ -[FBWorkspace _initWithDispatcher:process:].cold.2
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:].cold.1
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:].cold.2
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:].cold.3
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:].cold.4
+ -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:].cold.5
+ -[FBWorkspace _processCallOutQueue_requestScene:]
+ -[FBWorkspace _synchronizer]
+ -[FBWorkspace host:sendInvocation:withReply:]
+ -[FBWorkspace sceneID:handleInvocation:completion:]
+ -[FBWorkspace sceneID:handleInvocation:completion:].cold.1
+ -[FBWorkspace sceneID:invalidateWithContext:clientError:]
+ -[FBWorkspace sceneID:invalidateWithContext:clientError:].cold.1
+ -[FBWorkspace setSynchronizer:]
+ -[FBWorkspace state]
+ -[FBWorkspace synchronizer]
+ -[FBWorkspaceAssertionAttributes .cxx_destruct]
+ -[FBWorkspaceAssertionAttributes assertionAttributesForLaunchIntent:]
+ -[FBWorkspaceAssertionAttributes assertionAttributesForWorkspaceState:]
+ -[FBWorkspaceAssertionAttributes injectorAttributes]
+ -[FBWorkspaceConnection _acquireAssertionForWorkspaceScene:withState:]
+ -[FBWorkspaceConnectionsStateStore _initWithIdentifier:].cold.2
+ -[FBWorkspaceConnectionsStateStore setState:].cold.3
+ -[FBWorkspaceDomain _assertionAttrs]
+ -[FBWorkspaceDomain _initWithCoupler:specification:]
+ -[FBWorkspaceDomain _initWithCoupler:specification:].cold.1
+ -[FBWorkspaceDomain _initWithCoupler:specification:].cold.2
+ -[FBWorkspaceDomain _initWithCoupler:specification:].cold.3
+ -[FBWorkspaceDomain _listenerEndpoint]
+ -[FBWorkspaceDomain _listenerEndpoint].cold.1
+ -[FBWorkspaceDomain _lock_listener]
+ -[FBWorkspaceDomain coupler]
+ -[FBWorkspaceDomain dealloc].cold.1
+ -[FBWorkspaceDomain endpointPromise]
+ -[FBWorkspaceDomain injectEndpointToFBSWorkspace]
+ -[FBWorkspaceDomain injectEndpointToFBSWorkspace].cold.1
+ -[FBWorkspaceDomain injectEndpointToFBSWorkspace].cold.2
+ -[FBWorkspaceDomain setIndirectConnectionDelegate:]
+ -[FBWorkspaceDomain setIndirectConnectionDelegate:].cold.1
+ -[FBWorkspaceDomain setIndirectConnectionDelegate:].cold.2
+ -[FBWorkspaceDomain specification]
+ -[FBWorkspaceEndpointPromise .cxx_destruct]
+ -[FBWorkspaceEndpointPromise _domainIdentifier]
+ -[FBWorkspaceEndpointPromise _domainIdentifier].cold.1
+ -[FBWorkspaceEndpointPromise _initWithDomain:identifier:endpoint:]
+ -[FBWorkspaceEndpointPromise description]
+ -[FBWorkspaceEndpointPromise endpoint]
+ -[FBWorkspaceEndpointPromise initWithEndpoint:]
+ -[FBWorkspaceEndpointPromise isResolvedNullEndpoint]
+ -[FBWorkspaceEventDispatcher _callOutQueue_dispatchHandshakeFromSource:toTarget:]
+ -[FBWorkspaceEventDispatcher _callOutQueue_dispatchSceneRequestsFromSource:toTarget:]
+ -[FBWorkspaceEventDispatcher _callOutQueue_handleSceneRequest:fromSource:]
+ -[FBWorkspaceEventDispatcher _callOutQueue_noteHandshakeFromSource:withRemnants:]
+ -[FBWorkspaceEventDispatcher _initWithDomain:]
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:]
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.1
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.2
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.3
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.4
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.5
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.6
+ -[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:].cold.7
+ -[FBWorkspaceEventDispatcher _noteReceivedInvalidationHandlerForAssertion:]
+ -[FBWorkspaceEventDispatcher _noteSourceDidInvalidate:withPIDNumber:]
+ -[FBWorkspaceEventDispatcher _noteSourceDidInvalidate:withPIDNumber:].cold.1
+ -[FBWorkspaceEventDispatcher canCreateLocalSceneWithIdentity:]
+ -[FBWorkspaceEventDispatcher dealloc]
+ -[FBWorkspaceEventDispatcher dealloc].cold.1
+ -[FBWorkspaceEventDispatcher domain]
+ -[FBWorkspaceEventDispatcher handleLocalSceneRequest:]
+ -[FBWorkspaceEventDispatcher noteHandshakeFromSource:withRemnants:].cold.7
+ -[FBWorkspaceEventDispatcher registerSourceWithProcessHandle:].cold.5
+ -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:]
+ -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:].cold.1
+ -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:].cold.2
+ -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:].cold.3
+ -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:].cold.4
+ -[FBWorkspaceEventDispatcherSource enqueueSceneRequest:].cold.5
+ -[FBWorkspaceEventDispatcherSource noteHandshakeWithRemnants:].cold.5
+ -[FBWorkspaceEventDispatcherSource noteHandshakeWithRemnants:].cold.6
+ -[FBWorkspaceEventDispatcherSource noteHandshakeWithRemnants:].cold.7
+ -[FBWorkspaceIncomingConnection workspaceLock_setConnection:].cold.3
+ -[FBWorkspaceScene _workspaceQueue_updateAssertion].cold.1
+ -[FBWorkspaceScene workspace:handleInvocation:fromConnection:withReply:]
+ -[FBWorkspaceScene workspace:sendInvocation:withReply:]
+ -[FBWorkspaceSceneRequest clientIdentity]
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:]
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:].cold.1
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:].cold.2
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:].cold.3
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:].cold.4
+ -[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:].cold.5
+ -[RBSAssertion(FBWorkspace) fb_setWorkspaceState:]
+ -[RBSAssertion(FBWorkspace) fb_workspaceState]
+ -[_FBLocalSceneInfo .cxx_destruct]
+ -[_FBLocalSceneInfo initWithScene:]
+ -[_FBLocalSceneInfo initWithScene:].cold.1
+ -[_FBLocalSceneInfo init]
+ -[_FBLocalSceneInfo setPendingTransitionContext:]
+ GCC_except_table127
+ GCC_except_table14
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table22
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table91
+ OBJC_IVAR_$_FBProcess._processManager
+ _BSSelfTaskHasEntitlement
+ _FBLogTransaction
+ _FBLogTransaction.__logObj
+ _FBLogTransaction.cold.1
+ _FBLogTransaction.onceToken
+ _FBSProcessWatchdogErrorDomain
+ _FBSSceneJetsamPriorityGetJetsamMode
+ _FBSSceneJetsamPriorityGetResourceElevation
+ _FBSceneIdleEventQueue
+ _FBSceneIdleEventQueue.__IdleEventQueue
+ _FBSceneIdleEventQueue.cold.1
+ _FBSceneIdleEventQueue.onceToken
+ _FBWorkspaceJetsamBandIsValid
+ _FBWorkspaceProcessRoleIsValid
+ _FBWorkspaceSceneErrorCreate
+ _FBWorkspaceSceneErrorDomain
+ _FBWorkspaceStateCombine
+ _FBWorkspaceStateCompare
+ _FBWorkspaceStateCreate
+ _FBWorkspaceStateEqual
+ _FBWorkspaceStateGetJetsamBand
+ _FBWorkspaceStateGetProcessRole
+ _FBWorkspaceStateGetVisibility
+ _FBWorkspaceStateNone
+ _NSStringFromFBWorkspaceDomainSelfAssertRuntime
+ _NSStringFromFBWorkspaceProcessRole
+ _NSStringFromFBWorkspaceSceneErrorCode
+ _NSStringFromFBWorkspaceState
+ _OBJC_CLASS_$_BSServiceCompoundQueue
+ _OBJC_CLASS_$_BSServiceConnectionEndpointInjector
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_FBSOrientationServiceSpecification
+ _OBJC_CLASS_$_FBSOrientationUpdate
+ _OBJC_CLASS_$_FBSProcessExecutableSlice
+ _OBJC_CLASS_$_FBSSceneClientSettingsDiff
+ _OBJC_CLASS_$_FBSWorkspaceCoupler
+ _OBJC_CLASS_$_FBSWorkspaceSceneRequestOptions
+ _OBJC_CLASS_$_FBSceneSynchronizer
+ _OBJC_CLASS_$_FBWorkspaceAssertionAttributes
+ _OBJC_CLASS_$_FBWorkspaceEndpointPromise
+ _OBJC_CLASS_$__FBLocalSceneInfo
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._listener
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_connections
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_interestedConnections
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_interfaceOrientation
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_pendingConnections
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_sequenceNumber
+ _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._lock_serviceSuspended
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._callOutQueue_workspace
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._clientFutureHostsBeingSynchronized
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._clientFutureScenesBeingSynchronized
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._coupler
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._currentProcess
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._eventDispatcher
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._invalidated
+ _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._pendingScenes
+ _OBJC_IVAR_$_FBProcessManager._bootstrapLock_invalidated
+ _OBJC_IVAR_$_FBProcessManager._eventDispatcher
+ _OBJC_IVAR_$_FBProcessManager._lock_invalidated
+ _OBJC_IVAR_$_FBProcessManager._lock_legacySceneManager
+ _OBJC_IVAR_$_FBProcessManager._lock_syncLocalSceneClientProvider
+ _OBJC_IVAR_$_FBProcessManager._stateCaptureAssertion
+ _OBJC_IVAR_$_FBProcessWatchdog._unblockSignal
+ _OBJC_IVAR_$_FBScene._eventQueue
+ _OBJC_IVAR_$_FBScene._updateSuspendIdleWork
+ _OBJC_IVAR_$_FBSceneEventQueue._idleEventLock
+ _OBJC_IVAR_$_FBSceneLayer._renderID
+ _OBJC_IVAR_$_FBSceneLayerManager._needsRebuildLayers
+ _OBJC_IVAR_$_FBSceneLayerManager._suspendAssertions
+ _OBJC_IVAR_$_FBSceneManager._invalidated
+ _OBJC_IVAR_$_FBSceneObserver._extension
+ _OBJC_IVAR_$_FBSceneSnapshot._config
+ _OBJC_IVAR_$_FBSceneSnapshotContext._clientAllowsProtectedContent
+ _OBJC_IVAR_$_FBSceneSnapshotContext._userInfo
+ _OBJC_IVAR_$_FBSceneSynchronizer._dispatcher
+ _OBJC_IVAR_$_FBSceneSynchronizer._identifier
+ _OBJC_IVAR_$_FBSceneSynchronizer._lock
+ _OBJC_IVAR_$_FBSceneSynchronizer._lock_process
+ _OBJC_IVAR_$_FBSceneSynchronizer._lock_waitingForConnect
+ _OBJC_IVAR_$_FBSceneSynchronizer._serviceQueue
+ _OBJC_IVAR_$_FBSceneSynchronizer._workspaceQueue
+ _OBJC_IVAR_$_FBSceneWorkspace._processManager
+ _OBJC_IVAR_$_FBWorkspace._invalidated
+ _OBJC_IVAR_$_FBWorkspace._lock_outgoingEndpointPromise
+ _OBJC_IVAR_$_FBWorkspace._synchronizer
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._UIAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activeAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgActiveAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgLaunchAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgUserInitiatedAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgUtilityAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgFocalAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgLaunchAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgNonFocalAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgSupportLaunchAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgSuspendedAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgUtilityAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._focalAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._injectorAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._interactiveAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._nonUIAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._opportunisticAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._utLaunchAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._utilityAttributes
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._visibilityAttribute
+ _OBJC_IVAR_$_FBWorkspaceConnectionsStateStore._queue_invalidated
+ _OBJC_IVAR_$_FBWorkspaceDomain._coupler
+ _OBJC_IVAR_$_FBWorkspaceDomain._endpointPromise
+ _OBJC_IVAR_$_FBWorkspaceDomain._icdLock
+ _OBJC_IVAR_$_FBWorkspaceDomain._icdLock_indirectConnectionDelegate
+ _OBJC_IVAR_$_FBWorkspaceDomain._icdLock_pendingIndirectConnectionBlocks
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock_activation
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock_injectEndpointToFBSWorkspace
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock_invalidated
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock_listener
+ _OBJC_IVAR_$_FBWorkspaceDomain._lock_registration
+ _OBJC_IVAR_$_FBWorkspaceDomain._specification
+ _OBJC_IVAR_$_FBWorkspaceEndpointPromise._domainIdentifier
+ _OBJC_IVAR_$_FBWorkspaceEndpointPromise._lock
+ _OBJC_IVAR_$_FBWorkspaceEndpointPromise._lock_domain
+ _OBJC_IVAR_$_FBWorkspaceEndpointPromise._lock_endpoint
+ _OBJC_IVAR_$_FBWorkspaceEventDispatcher._domain
+ _OBJC_IVAR_$_FBWorkspaceEventDispatcherSource._invalidationLock
+ _OBJC_IVAR_$_FBWorkspaceEventDispatcherSource._lock_invalidationBlock
+ _OBJC_IVAR_$_FBWorkspaceScene._queue_eventsCompleteSignal
+ _OBJC_IVAR_$_FBWorkspaceScene._queue_inFlightDeactivationEvents
+ _OBJC_IVAR_$_FBWorkspaceScene._queue_workspaceState
+ _OBJC_IVAR_$_FBWorkspaceSceneRequest._clientIdentity
+ _OBJC_IVAR_$__FBLocalSceneInfo._scene
+ _OBJC_IVAR_$__FBLocalSceneInfo.hasHandledSceneCreate
+ _OBJC_IVAR_$__FBLocalSceneInfo.hasSentFBSWorkspaceDelegateSceneCreate
+ _OBJC_IVAR_$__FBLocalSceneInfo.pendingTransitionContext
+ _OBJC_METACLASS_$_FBSProcessExecutableSlice
+ _OBJC_METACLASS_$_FBSceneSynchronizer
+ _OBJC_METACLASS_$_FBWorkspaceAssertionAttributes
+ _OBJC_METACLASS_$_FBWorkspaceEndpointPromise
+ _OBJC_METACLASS_$__FBLocalSceneInfo
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _UnblockClientLibrary
+ _UnblockClientLibrary.cold.1
+ _UnblockClientLibraryCore.frameworkLibrary
+ __FBSNSStringFromUBIssueType
+ __OBJC_$_CLASS_METHODS_FBLocalSynchronousSceneClientProvider(SharedInstance)
+ __OBJC_$_CLASS_METHODS_FBSceneEventQueue
+ __OBJC_$_CLASS_METHODS_FBSceneSynchronizer
+ __OBJC_$_CLASS_METHODS_FBWorkspaceDomain(Debugging|FBSWorkspace)
+ __OBJC_$_INSTANCE_METHODS_FBSceneSynchronizer
+ __OBJC_$_INSTANCE_METHODS_FBWorkspaceAssertionAttributes
+ __OBJC_$_INSTANCE_METHODS_FBWorkspaceEndpointPromise
+ __OBJC_$_INSTANCE_METHODS__FBLocalSceneInfo
+ __OBJC_$_INSTANCE_VARIABLES_FBSceneSynchronizer
+ __OBJC_$_INSTANCE_VARIABLES_FBWorkspaceAssertionAttributes
+ __OBJC_$_INSTANCE_VARIABLES_FBWorkspaceEndpointPromise
+ __OBJC_$_INSTANCE_VARIABLES__FBLocalSceneInfo
+ __OBJC_$_PROP_LIST_FBInterfaceOrientationServiceServer
+ __OBJC_$_PROP_LIST_FBMutableSceneSnapshotConfiguration
+ __OBJC_$_PROP_LIST_FBSceneSnapshotConfiguration
+ __OBJC_$_PROP_LIST_FBSceneSnapshotConfigurator
+ __OBJC_$_PROP_LIST_FBSceneSynchronizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBMutableSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSInvocationSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSOrientationServiceServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSceneManagerSceneCreating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSceneSnapshotConfigurator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBWorkspaceDomainConnectionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBMutableSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSInvocationSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSOrientationServiceServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneManagerSceneCreating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneSnapshotConfigurator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBWorkspaceDomainConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_FBMutableSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_REFS_FBSComponentSceneSupport
+ __OBJC_$_PROTOCOL_REFS_FBSInvocationReceiving
+ __OBJC_$_PROTOCOL_REFS_FBSInvocationSending
+ __OBJC_$_PROTOCOL_REFS_FBSceneManagerSceneCreating
+ __OBJC_$_PROTOCOL_REFS_FBSceneSnapshotConfiguration
+ __OBJC_$_PROTOCOL_REFS_FBSceneSnapshotConfigurator
+ __OBJC_$_PROTOCOL_REFS_FBSceneSnapshotInternalConfiguration
+ __OBJC_$_PROTOCOL_REFS_FBWorkspaceDomainConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_FBInterfaceOrientationServiceServer
+ __OBJC_CLASS_RO_$_FBSceneSynchronizer
+ __OBJC_CLASS_RO_$_FBWorkspaceAssertionAttributes
+ __OBJC_CLASS_RO_$_FBWorkspaceEndpointPromise
+ __OBJC_CLASS_RO_$__FBLocalSceneInfo
+ __OBJC_LABEL_PROTOCOL_$_FBMutableSceneSnapshotConfiguration
+ __OBJC_LABEL_PROTOCOL_$_FBSComponentSceneSupport
+ __OBJC_LABEL_PROTOCOL_$_FBSInvocationReceiving
+ __OBJC_LABEL_PROTOCOL_$_FBSInvocationSending
+ __OBJC_LABEL_PROTOCOL_$_FBSOrientationServiceServerInterface
+ __OBJC_LABEL_PROTOCOL_$_FBSceneManagerSceneCreating
+ __OBJC_LABEL_PROTOCOL_$_FBSceneSnapshotConfiguration
+ __OBJC_LABEL_PROTOCOL_$_FBSceneSnapshotConfigurator
+ __OBJC_LABEL_PROTOCOL_$_FBSceneSnapshotInternalConfiguration
+ __OBJC_LABEL_PROTOCOL_$_FBWorkspaceDomainConnectionDelegate
+ __OBJC_METACLASS_RO_$_FBSceneSynchronizer
+ __OBJC_METACLASS_RO_$_FBWorkspaceAssertionAttributes
+ __OBJC_METACLASS_RO_$_FBWorkspaceEndpointPromise
+ __OBJC_METACLASS_RO_$__FBLocalSceneInfo
+ __OBJC_PROTOCOL_$_FBMutableSceneSnapshotConfiguration
+ __OBJC_PROTOCOL_$_FBSComponentSceneSupport
+ __OBJC_PROTOCOL_$_FBSInvocationReceiving
+ __OBJC_PROTOCOL_$_FBSInvocationSending
+ __OBJC_PROTOCOL_$_FBSOrientationServiceServerInterface
+ __OBJC_PROTOCOL_$_FBSceneManagerSceneCreating
+ __OBJC_PROTOCOL_$_FBSceneSnapshotConfiguration
+ __OBJC_PROTOCOL_$_FBSceneSnapshotConfigurator
+ __OBJC_PROTOCOL_$_FBSceneSnapshotInternalConfiguration
+ __OBJC_PROTOCOL_$_FBWorkspaceDomainConnectionDelegate
+ ___100-[FBWorkspaceScene _workspaceQueue_sendSceneCreateToClient:parameters:transitionContext:completion:]_block_invoke.cold.1
+ ___104-[FBWorkspaceScene _workspaceQueue_decrementInFlightUpdatesForAction:allowThrottling:externallyManaged:]_block_invoke
+ ___105-[FBInterfaceOrientationServiceServer _lock_noteInterfaceOrientationChanged:animationSettings:direction:]_block_invoke
+ ___116-[FBLocalSynchronousSceneClientProvider _sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:]_block_invoke
+ ___116-[FBLocalSynchronousSceneClientProvider _sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:]_block_invoke.225
+ ___119-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:]_block_invoke
+ ___119-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:]_block_invoke_2
+ ___119-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:]_block_invoke_3
+ ___184-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke
+ ___184-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_2
+ ___184-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_3
+ ___184-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_4
+ ___184-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_5
+ ___24-[FBSceneLayer isEqual:]_block_invoke_6
+ ___26-[FBScene sendInvocation:]_block_invoke
+ ___26-[FBScene sendInvocation:]_block_invoke_2
+ ___27-[FBWorkspace sendActions:]_block_invoke.41
+ ___29-[FBProcessWatchdog activate]_block_invoke
+ ___29-[FBProcessWatchdog activate]_block_invoke.7
+ ___29-[FBProcessWatchdog activate]_block_invoke.7.cold.1
+ ___29-[FBProcessWatchdog activate]_block_invoke.9
+ ___29-[FBProcessWatchdog activate]_block_invoke_2
+ ___30-[FBProcess _bootstrapAndExec]_block_invoke.118
+ ___30-[FBProcess _bootstrapAndExec]_block_invoke_2.119
+ ___32-[FBSceneWorkspace didAddScene:]_block_invoke
+ ___33+[FBWorkspaceDomain nullEndpoint]_block_invoke
+ ___34+[FBProcess userInitiatedWorkloop]_block_invoke
+ ___34-[FBSystemShell _initWithOptions:]_block_invoke.31
+ ___35-[FBProcessManager _removeProcess:]_block_invoke.183
+ ___35-[FBWorkspaceDomain _lock_listener]_block_invoke
+ ___38-[FBWorkspace _setIncomingConnection:]_block_invoke
+ ___39-[FBProcess _notePendingExitForReason:]_block_invoke.77
+ ___39-[FBSceneWorkspace sceneDidInvalidate:]_block_invoke
+ ___39-[FBSceneWorkspace sceneDidInvalidate:]_block_invoke_2
+ ___40-[FBScene _joinUpdate:block:completion:]_block_invoke.195
+ ___41-[FBScene _deactivateClient:withContext:]_block_invoke
+ ___41-[FBSceneWorkspace scene:didApplyUpdate:]_block_invoke
+ ___41-[FBWorkspace _noteProcessDidInvalidate:]_block_invoke_3
+ ___43-[FBScene _dispatchClientMessageWithBlock:]_block_invoke
+ ___43-[FBSceneWorkspace scene:didPrepareUpdate:]_block_invoke
+ ___43-[FBWorkspace _initWithDispatcher:process:]_block_invoke
+ ___44-[FBSceneWorkspace scene:didCompleteUpdate:]_block_invoke
+ ___45-[FBProcessManager _initWithWorkspaceDomain:]_block_invoke
+ ___45-[FBProcessManager _initWithWorkspaceDomain:]_block_invoke_2
+ ___45-[FBProcessManager _initWithWorkspaceDomain:]_block_invoke_3
+ ___45-[FBProcessManager _initWithWorkspaceDomain:]_block_invoke_4
+ ___45-[FBWorkspace host:sendInvocation:withReply:]_block_invoke
+ ___45-[FBWorkspaceConnectionsStateStore setState:]_block_invoke.cold.4
+ ___45-[FBWorkspaceEventDispatcher registerTarget:]_block_invoke.80
+ ___46+[FBSceneEventQueue suspendIdleWorkForReason:]_block_invoke
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke.287
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke.292
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke.294
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke.312
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_2
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_2.293
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_2.295
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_3
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_3.296
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_3.cold.1
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_3.cold.2
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_4
+ ___46-[FBScene _applySettingsUpdateWithCompletion:]_block_invoke_5
+ ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.176
+ ___48+[FBWorkspaceAssertionAttributes baseAttributes]_block_invoke
+ ___48-[FBProcessCPUStatistics initWithProcessHandle:]_block_invoke
+ ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.239
+ ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.243
+ ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke_2.cold.2
+ ___49-[FBSceneLayerManager _suspendUpdatesWithReason:]_block_invoke
+ ___49-[FBWorkspace _processCallOutQueue_requestScene:]_block_invoke
+ ___49-[FBWorkspaceDomain injectEndpointToFBSWorkspace]_block_invoke
+ ___50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.320
+ ___50-[FBScene clientToken:handleInvocation:withReply:]_block_invoke
+ ___54-[FBProcessManager _bootstrap_consumeLock_addProcess:]_block_invoke.179
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.338
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.345
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.348
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke_2
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke_3
+ ___54-[FBScene clientToken:didReceiveActions:forExtension:]_block_invoke.362
+ ___54-[FBScene clientToken:didReceiveActions:forExtension:]_block_invoke.cold.1
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.245
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.254
+ ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.108
+ ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.124
+ ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.125
+ ___55-[FBProcessManager noteProcessAssertionStateDidChange:]_block_invoke.118
+ ___55-[FBSceneWorkspace _initWithProcessManager:identifier:]_block_invoke
+ ___55-[FBSceneWorkspace _initWithProcessManager:identifier:]_block_invoke.34
+ ___55-[FBSceneWorkspace _initWithProcessManager:identifier:]_block_invoke.45
+ ___55-[FBWorkspaceScene workspace:sendInvocation:withReply:]_block_invoke
+ ___55-[FBWorkspaceScene workspace:sendInvocation:withReply:]_block_invoke_2
+ ___55-[FBWorkspaceScene workspace:sendInvocation:withReply:]_block_invoke_3
+ ___55-[FBWorkspaceScene workspace:sendInvocation:withReply:]_block_invoke_4
+ ___55-[FBWorkspaceScene workspace:sendInvocation:withReply:]_block_invoke_4.cold.1
+ ___56-[FBProcess _lock_consumeLock_executeTerminationRequest]_block_invoke.291
+ ___59-[FBWorkspaceOutgoingConnection workspaceLock_setEndpoint:]_block_invoke.76
+ ___61+[FBWorkspaceAssertionAttributes assertsVisibilityAttributes]_block_invoke
+ ___61-[FBWorkspaceIncomingConnection workspaceLock_setConnection:]_block_invoke.52
+ ___61-[FBWorkspaceIncomingConnection workspaceLock_setConnection:]_block_invoke.57
+ ___63-[FBInterfaceOrientationServiceServer _initWithDomain:service:]_block_invoke
+ ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.177
+ ___68-[FBProcessManager _bootstrapProcessWithHandle:synchronously:error:]_block_invoke
+ ___71-[FBLocalSynchronousSceneClientProvider host:sendInvocation:withReply:]_block_invoke
+ ___72-[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:]_block_invoke
+ ___72-[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:]_block_invoke.cold.1
+ ___73-[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:]_block_invoke
+ ___74-[FBScene clientToken:didUpdateClientSettings:withDiff:transitionContext:]_block_invoke.cold.1
+ ___74-[FBScene clientToken:didUpdateClientSettings:withDiff:transitionContext:]_block_invoke_2
+ ___75-[FBWorkspaceEventDispatcher _noteReceivedInvalidationHandlerForAssertion:]_block_invoke
+ ___76-[FBLocalSynchronousSceneClientProvider requestSceneWithOptions:completion:]_block_invoke
+ ___76-[FBLocalSynchronousSceneClientProvider requestSceneWithOptions:completion:]_block_invoke_2
+ ___76-[FBLocalSynchronousSceneClientProvider requestSceneWithOptions:completion:]_block_invoke_2.cold.1
+ ___78-[FBLocalSynchronousSceneClientProvider sendActions:toWorkspaceID:completion:]_block_invoke
+ ___78-[FBProcessManager _bootstrapProcessWithExecutionContext:synchronously:error:]_block_invoke_6
+ ___79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.118
+ ___80-[FBLocalSynchronousSceneClientProvider _invalidateSceneInfo:transitionContext:]_block_invoke
+ ___80-[FBLocalSynchronousSceneClientProvider _invalidateSceneInfo:transitionContext:]_block_invoke_2
+ ___81-[FBInterfaceOrientationServiceServer listener:didReceiveConnection:withContext:]_block_invoke
+ ___81-[FBInterfaceOrientationServiceServer listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___81-[FBWorkspaceEventDispatcher _callOutQueue_dispatchHandshakeFromSource:toTarget:]_block_invoke
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke.132
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke_2
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke_2.133
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke_3
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke_3.136
+ ___85-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:]_block_invoke_4
+ ___86-[FBWorkspaceEventDispatcher _initWithDomain:connectionStore:preregisteredWorkspaces:]_block_invoke
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.105
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.111
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke_2.107
+ ___90-[FBLocalSynchronousSceneClientProvider _sendSceneCreateFBSWorkspaceDelegateForSceneInfo:]_block_invoke.cold.1
+ ___98-[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:]_block_invoke
+ ___98-[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:]_block_invoke_2
+ ___98-[FBLocalSynchronousSceneClientProvider _initWithWorkspaceCoupler:currentProcess:eventDispatcher:]_block_invoke_2.cold.1
+ ___FBLogTransaction_block_invoke
+ ___FBSceneIdleEventQueue_block_invoke
+ ___FBWorkspaceSceneErrorCreate_block_invoke
+ ___FBWorkspaceState
+ ___UnblockClientLibraryCore_block_invoke
+ ___WorkspacesLock
+ ___block_descriptor_32_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_32_e33_v32?0"FBSSceneIdentity"816^B24l
+ ___block_descriptor_40_e8_32bs_e46_v16?0"<FBSWorkspaceServiceServerInterface>"8ls32l8
+ ___block_descriptor_40_e8_32s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"<FBSOrientationServiceClientInterface>"8ls32l8
+ ___block_descriptor_40_e8_32s_e52_v32?0"FBSSceneIdentity"8"_FBLocalSceneInfo"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_40_e8_32w_e48_v16?0"<BSSimpleAssertionInvalidationContext>"8lw32l8
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_40_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
+ ___block_descriptor_44_e8_32s_e58_v16?0"<BSServiceConnectionEndpointInjectorConfiguring>"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e40_v24?0"FBSInvocationReply"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"FBSInvocationReply"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"FBSWorkspace"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e42_v16?0"FBWorkspaceEventDispatcherSource"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e30_v16?0"<BSErrorConfiguring>"8ls32l8
+ ___block_descriptor_50_e8_32s40s_e25_v16?0"FBSceneObserver"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"FBScene"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"FBSScene"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e46_v16?0"<FBSWorkspaceServiceServerInterface>"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e47_v16?0"<FBWorkspaceDomainConnectionDelegate>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e29_v24?0"NSError"8"NSArray"16ls32l8w56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e30_v16?0"<BSErrorConfiguring>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8u56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
+ ___block_literal_global.135
+ ___block_literal_global.14
+ ___block_literal_global.158
+ ___block_literal_global.166
+ ___block_literal_global.174
+ ___block_literal_global.182
+ ___block_literal_global.197
+ ___block_literal_global.198
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.241
+ ___block_literal_global.254
+ ___block_literal_global.258
+ ___block_literal_global.338
+ ___block_literal_global.347
+ ___block_literal_global.381
+ ___block_literal_global.80
+ ___block_literal_global.89
+ ___getUBStuckServiceClass_block_invoke
+ ___getUBStuckServiceClass_block_invoke.cold.1
+ ___getUBUnblockClientClass_block_invoke
+ ___getUBUnblockClientClass_block_invoke.cold.1
+ __initWithProcessManager:identifier:.onceToken
+ _activate.__UnblockEntitled
+ _activate.onceToken
+ _assertsVisibilityAttributes.attrs
+ _assertsVisibilityAttributes.onceToken
+ _audit_stringUnblockClient
+ _baseAttributes.attrs
+ _baseAttributes.onceToken
+ _getUBStuckServiceClass.softClass
+ _getUBUnblockClientClass.softClass
+ _initWithProcessHandle:.entitled
+ _initWithProcessHandle:.onceToken
+ _nullEndpoint.nullEndpoint
+ _nullEndpoint.onceToken
+ _objc_msgSend$_activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:
+ _objc_msgSend$_authenticateAuditToken:entitlement:credentials:error:
+ _objc_msgSend$_connectionInvalidated:
+ _objc_msgSend$_currentConnection
+ _objc_msgSend$_enqueueClientConnectionBlock:
+ _objc_msgSend$_findDomainSpecification
+ _objc_msgSend$_getPolicyWallTime:cpuTime:
+ _objc_msgSend$_initWithDomain:service:
+ _objc_msgSend$_initWithObserver:workspace:
+ _objc_msgSend$_initWithProcessHandle:invalidationBlock:
+ _objc_msgSend$_initWithProcessManager:
+ _objc_msgSend$_initWithProcessManager:identity:handle:executionContext:
+ _objc_msgSend$_invalidate
+ _objc_msgSend$_isSameAsWorkspace:
+ _objc_msgSend$_isSharedInstance
+ _objc_msgSend$_lock_noteInterfaceOrientationChanged:animationSettings:direction:
+ _objc_msgSend$_lock_registerOrientationInterest:connection:completion:
+ _objc_msgSend$_lock_sendMessageToInterestedClients:
+ _objc_msgSend$_processCallOutQueue_requestScene:
+ _objc_msgSend$_reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:
+ _objc_msgSend$_rebuildLayers
+ _objc_msgSend$_registerProcessForViewServiceWithProcessHandle:error:
+ _objc_msgSend$_removeSuspendAssertion:
+ _objc_msgSend$_sharedInstance
+ _objc_msgSend$_suspendUpdatesWithReason:
+ _objc_msgSend$_terminateWithRequest:forWatchdog:
+ _objc_msgSend$_watchdog:shouldTerminateWithDeclineReason:
+ _objc_msgSend$_watchdog:terminationRequestForError:
+ _objc_msgSend$activeOrientationDidUpdate:
+ _objc_msgSend$addEndpoint:
+ _objc_msgSend$appendInt64:
+ _objc_msgSend$appendInt64:counterpart:
+ _objc_msgSend$assertBarrierOnQueue
+ _objc_msgSend$callOutQueue
+ _objc_msgSend$cancel
+ _objc_msgSend$cannotResolveForReason:
+ _objc_msgSend$captureCompletions
+ _objc_msgSend$clientAllowsProtectedContent
+ _objc_msgSend$clientToken:deactivateWithContext:
+ _objc_msgSend$clientToken:handleInvocation:withReply:
+ _objc_msgSend$compatibleWithTarget:
+ _objc_msgSend$didAddScene:
+ _objc_msgSend$domain:didReceiveConnection:withContext:
+ _objc_msgSend$eventDispatcher
+ _objc_msgSend$executeOrAppend:
+ _objc_msgSend$executeWhenIdle:
+ _objc_msgSend$extension
+ _objc_msgSend$fb_setWorkspaceState:
+ _objc_msgSend$fb_workspaceState
+ _objc_msgSend$fbsSceneForScene:
+ _objc_msgSend$forceLookupIdentifer:error:
+ _objc_msgSend$handleForAuditToken:error:
+ _objc_msgSend$host:sendInvocation:withReply:
+ _objc_msgSend$hostProcess
+ _objc_msgSend$identityForInjectedEndpointToProcessIdentity:
+ _objc_msgSend$incomingWorkspaceEndpoint
+ _objc_msgSend$initForPid:threadID:timeElapsed:incidentUUID:
+ _objc_msgSend$initWithClientIdentity:targetIdentifier:options:completion:
+ _objc_msgSend$initWithContextID:renderID:
+ _objc_msgSend$initWithDelegate:workspace:
+ _objc_msgSend$initWithObserver:workspace:
+ _objc_msgSend$initWithOrientation:sequenceNumber:duration:rotationDirection:
+ _objc_msgSend$initWithReason:invalidatedWithContextBlock:
+ _objc_msgSend$initWithScene:configurator:
+ _objc_msgSend$initWithScene:context:
+ _objc_msgSend$initialize
+ _objc_msgSend$injectorWithConfigurator:
+ _objc_msgSend$invokeWithReceiver:replyHandler:
+ _objc_msgSend$isBSServiceConnectionError
+ _objc_msgSend$issueType
+ _objc_msgSend$jetsamPriority
+ _objc_msgSend$launchIdentifiers
+ _objc_msgSend$legacySceneManagerCreatingIfNecessary:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$queueWithDispatchQueue:targetQueue:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$queueWithName:serviceQuality:targetQueue:
+ _objc_msgSend$recover:stackshotData:replyQueue:callback:
+ _objc_msgSend$recoveryConfidence
+ _objc_msgSend$recoveryStatus
+ _objc_msgSend$relinquish
+ _objc_msgSend$renderID
+ _objc_msgSend$requestSceneWithOptions:completion:
+ _objc_msgSend$resolve
+ _objc_msgSend$scene:didApplyUpdate:
+ _objc_msgSend$scene:didCompleteUpdate:
+ _objc_msgSend$scene:didPrepareUpdate:
+ _objc_msgSend$sceneID:handleInvocation:completion:
+ _objc_msgSend$sceneObserverWantsUpdatesFromInactiveScenes
+ _objc_msgSend$serviceQueue
+ _objc_msgSend$serviceWithClass:
+ _objc_msgSend$setInitialClientSettings:
+ _objc_msgSend$setInitialSettings:
+ _objc_msgSend$setOrientation:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setSequenceNumber:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$suspendIdleWorkForReason:
+ _objc_msgSend$syncLocalSceneClientProvider
+ _objc_msgSend$synchronizer
+ _objc_msgSend$userInitiatedWorkloop
+ _objc_msgSend$workspaceState
+ _userInitiatedWorkloop.onceToken
+ _userInitiatedWorkloop.queue
- +[FBDisplayManager mainDisplay]
- +[FBLocalSynchronousSceneClientProvider sharedInstance]
- +[FBLocalSynchronousSceneClientProvider sharedInstance].cold.1
- +[FBProcess createCurrentProcess]
- +[FBProcess createCurrentProcess].cold.1
- +[FBProcess createProcessWithExecutionContext:]
- +[FBProcess createProcessWithExecutionContext:].cold.1
- +[FBProcess createProcessWithExecutionContext:].cold.2
- +[FBProcess createProcessWithHandle:]
- +[FBProcess createProcessWithHandle:].cold.1
- +[FBProcess createProcessWithHandle:].cold.2
- +[FBProcess rbInteractionWorkloop]
- +[FBProcess rbInteractionWorkloop].cold.1
- +[FBProcessExecutableSlice arm64]
- +[FBProcessExecutableSlice arm64e]
- +[FBProcessExecutableSlice sliceWithType:]
- +[FBSceneManager sharedInstance].cold.1
- +[FBServiceClientAuthenticator _authenticateAuditToken:entitlement:credentials:error:withResult:]
- +[FBWorkspaceConnectionsStateStore _unlinkAllForIdentifier:]
- +[FBWorkspaceConnectionsStateStore _unlinkAllForIdentifier:].cold.1
- +[FBWorkspaceConnectionsStateStore _unlinkAllForIdentifier:].cold.2
- +[FBWorkspaceDomain debugDescription]
- +[FBWorkspaceDomain endpoint]
- +[FBWorkspaceDomain sharedInstance]
- +[FBWorkspaceDomain sharedInstance].cold.1
- +[FBWorkspaceDomain startListener]
- +[FBWorkspaceEventDispatcher sharedInstance]
- +[FBWorkspaceEventDispatcher sharedInstance].cold.1
- -[FBDisplayManager mainDisplay]
- -[FBInterfaceOrientationServiceServer _prerequisiteMilestones]
- -[FBInterfaceOrientationServiceServer _queue_handleRegisterOrientationInterest:fromClient:]
- -[FBInterfaceOrientationServiceServer _queue_handleRequestActiveOrientation:fromClient:]
- -[FBInterfaceOrientationServiceServer _queue_updateInterest:forClient:withMessage:]
- -[FBInterfaceOrientationServiceServer initWithIdentifier:queue:]
- -[FBInterfaceOrientationServiceServer noteClientDidConnect:withMessage:]
- -[FBInterfaceOrientationServiceServer noteClientDidDisconnect:]
- -[FBInterfaceOrientationServiceServer noteDidReceiveMessage:withType:fromClient:]
- -[FBLocalSynchronousSceneClientProvider _init]
- -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:completion:]
- -[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:completion:].cold.1
- -[FBProcess _initWithIdentity:handle:executionContext:]
- -[FBProcess _initWithIdentity:handle:executionContext:].cold.1
- -[FBProcess _initWithIdentity:handle:executionContext:].cold.2
- -[FBProcess _watchdog:terminationRequestForViolatedProvision:error:]
- -[FBProcess assertionState]
- -[FBProcessExecutableSlice description]
- -[FBProcessExecutableSlice subtype]
- -[FBProcessExecutableSlice type]
- -[FBProcessManager init].cold.1
- -[FBScene _adjustInitialSettings:]
- -[FBScene _adjustInitialSettings:].cold.1
- -[FBScene _adjustInitialSettings:].cold.2
- -[FBScene _applyUpdate:postStateApplicator:completion:]
- -[FBScene _applyUpdate:postStateApplicator:completion:].cold.1
- -[FBScene _deactivateForClientError:]
- -[FBScene _deactivateForClientError:].cold.1
- -[FBScene _deactivateForClientError:].cold.2
- -[FBScene client]
- -[FBSceneEventQueue _noteWillExecuteEvent:]
- -[FBSceneEventQueue delegate]
- -[FBSceneEventQueue setDelegate:]
- -[FBSceneLayer initWithContextID:]
- -[FBSceneManager _isSynchronizingSceneUpdates]
- -[FBSceneManager createSceneWithIdentifier:settings:initialClientSettings:clientProvider:transitionContext:]
- -[FBSceneManager createSceneWithIdentifier:settings:initialClientSettings:clientProvider:transitionContext:].cold.1
- -[FBSceneManagerObserver _initWithObserver:supportLegacy:]
- -[FBSceneManagerObserver _internalObserver]
- -[FBSceneManagerObserver delegateReceivesSceneActions]
- -[FBSceneManagerObserver initWithDelegate:supportLegacy:]
- -[FBSceneManagerObserver initWithObserver:supportLegacy:]
- -[FBSceneManagerObserver isInternalObserver]
- -[FBSceneManagerObserver sceneManager:createDefaultTransitionContextForScene:]
- -[FBSceneManagerObserver sceneManager:scene:didReceiveActions:]
- -[FBSceneManagerObserver sceneManager:scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
- -[FBSceneManagerObserver sceneManager:updateForScene:appliedWithContext:]
- -[FBSceneManagerObserver sceneManager:updateForScene:completedWithContext:error:]
- -[FBSceneManagerObserver sceneManager:updateForScene:preparedWithContext:]
- -[FBSceneManagerObserver sceneManager:willDestroyScene:]
- -[FBSceneManagerObserver sceneManagerDidEndSceneUpdateSynchronization:]
- -[FBSceneManagerObserver sceneManagerWillBeginSceneUpdateSynchronization:]
- -[FBSceneMonitor .cxx_destruct]
- -[FBSceneMonitor _effectiveBehaviors]
- -[FBSceneMonitor _evaluateEffectiveMonitorBehaviors]
- -[FBSceneMonitor _initWithSceneManager:sceneID:]
- -[FBSceneMonitor _initWithSceneManager:sceneID:].cold.1
- -[FBSceneMonitor _setEffectiveMonitorBehaviors:]
- -[FBSceneMonitor _updateAllSceneStateIgnoringDelegate]
- -[FBSceneMonitor _updateExternalScenes:]
- -[FBSceneMonitor _updateScenePairingState:]
- -[FBSceneMonitor _updateSceneSettings:]
- -[FBSceneMonitor behaviors]
- -[FBSceneMonitor dealloc]
- -[FBSceneMonitor dealloc].cold.1
- -[FBSceneMonitor delegate]
- -[FBSceneMonitor description]
- -[FBSceneMonitor initWithScene:]
- -[FBSceneMonitor initWithScene:].cold.1
- -[FBSceneMonitor initWithSceneID:]
- -[FBSceneMonitor invalidate]
- -[FBSceneMonitor isPairedWithExternalSceneID:]
- -[FBSceneMonitor scene:didApplyUpdateWithContext:]
- -[FBSceneMonitor scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
- -[FBSceneMonitor sceneID]
- -[FBSceneMonitor sceneLayerManagerDidUpdateLayers:]
- -[FBSceneMonitor sceneManager:didCreateScene:]
- -[FBSceneMonitor sceneManager:didDestroyScene:]
- -[FBSceneMonitor sceneManager:willDestroyScene:]
- -[FBSceneMonitor sceneManagerDidEndSceneUpdateSynchronization:]
- -[FBSceneMonitor sceneManagerWillBeginSceneUpdateSynchronization:]
- -[FBSceneMonitor sceneSettings]
- -[FBSceneMonitor scene]
- -[FBSceneMonitor setBehaviors:]
- -[FBSceneMonitor setDelegate:]
- -[FBSceneMonitorBehaviors copyWithZone:]
- -[FBSceneMonitorBehaviors isEqual:]
- -[FBSceneMonitorBehaviors monitorsClientSettings]
- -[FBSceneMonitorBehaviors monitorsPairingStatus]
- -[FBSceneMonitorBehaviors monitorsSettings]
- -[FBSceneMonitorBehaviors setMonitorsClientSettings:]
- -[FBSceneMonitorBehaviors setMonitorsPairingStatus:]
- -[FBSceneMonitorBehaviors setMonitorsSettings:]
- -[FBSceneObserver initWithComponent:]
- -[FBSceneSnapshot _baseTransformForSnapshotContext:rootContext:]
- -[FBSceneSnapshot _collectLayersToSnapshotFromScene:withSnapshotContext:rootContext:]
- -[FBSceneSnapshot initWithScene:snapshotContext:]
- -[FBSceneSnapshotContext initWithScene:]
- -[FBSceneSnapshotContext initWithScene:].cold.1
- -[FBSceneSnapshotContext setClientExtendedData:]
- -[FBSceneSnapshotContext setExpirationDate:]
- -[FBSceneSnapshotContext setOrientation:]
- -[FBSceneSnapshotContext setScale:]
- -[FBSceneSnapshotContext setSettings:]
- -[FBSceneWorkspace _beginSynchronizationBlock]
- -[FBSceneWorkspace _createSceneWithDefinition:settings:initialClientSettings:transitionContext:fromRemnant:usingClientProvider:completion:].cold.26
- -[FBSceneWorkspace _endSynchronizationBlock]
- -[FBSceneWorkspace _endSynchronizationBlock].cold.1
- -[FBSceneWorkspace _endSynchronizationBlock].cold.2
- -[FBSceneWorkspace _enqueueEventForScene:withName:block:]
- -[FBSceneWorkspace _enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:]
- -[FBSceneWorkspace _enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:].cold.1
- -[FBSceneWorkspace _eventForScene:withName:block:]
- -[FBSceneWorkspace _executeEventWhenIdle:]
- -[FBSceneWorkspace _executeNextIdleEventIfAppropriate]
- -[FBSceneWorkspace _executeWhenIdle:]
- -[FBSceneWorkspace _initWithIdentifier:legacy:]
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.1
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.2
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.3
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.4
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.5
- -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.6
- -[FBSceneWorkspace _initWithLegacySceneManager:]
- -[FBSceneWorkspace _isSynchronizingSceneUpdates]
- -[FBSceneWorkspace _synchronizeChanges:]
- -[FBSceneWorkspace eventQueueDidDrain:]
- -[FBSceneWorkspace eventQueueDidUnlock:]
- -[FBSceneWorkspace invalidate].cold.2
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:].cold.1
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:].cold.2
- -[FBSceneWorkspace scene:didReceiveActions:forExtension:]
- -[FBSceneWorkspace scene:didReceiveActions:forExtension:].cold.1
- -[FBSceneWorkspace scene:didReceiveActions:forExtension:].cold.2
- -[FBSceneWorkspace scene:didUpdateClientSettings:]
- -[FBSceneWorkspace scene:didUpdateClientSettings:].cold.1
- -[FBSceneWorkspace scene:didUpdateClientSettings:].cold.2
- -[FBSceneWorkspace scene:didUpdateClientSettings:].cold.3
- -[FBSceneWorkspace scene:enqueueCalloutsToObserversWithEventName:block:]
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:]
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.1
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.2
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.3
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.4
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.5
- -[FBSceneWorkspace scene:handleUpdate:withCompletion:].cold.6
- -[FBSceneWorkspace scene:performCalloutsToObservers:]
- -[FBServiceClientAuthenticator authenticateAuditToken:forEntitlement:withResult:]
- -[FBServiceClientAuthenticator authenticateAuditToken:withResult:]
- -[FBServiceClientAuthenticator authenticateClient:withResult:]
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:]
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:].cold.1
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:].cold.2
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:].cold.3
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:].cold.4
- -[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:].cold.5
- -[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]
- -[FBWorkspace _callOutQueue_requestScene:]
- -[FBWorkspace _connectionQueue]
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:].cold.1
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:].cold.2
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:].cold.3
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:].cold.4
- -[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:].cold.5
- -[FBWorkspace _queue]
- -[FBWorkspace assertionState]
- -[FBWorkspace createServiceQueue]
- -[FBWorkspace initWithParentProcess:]
- -[FBWorkspace initWithParentProcess:].cold.1
- -[FBWorkspace test_rejectAllSceneClients]
- -[FBWorkspace test_setRejectAllSceneClients:]
- -[FBWorkspaceConnection _workspaceScene:acquireAssertionWithState:]
- -[FBWorkspaceConnectionsStateStore _lastUsedBuffer]
- -[FBWorkspaceConnectionsStateStore _setFailureModeForNextWrite:]
- -[FBWorkspaceDomain _ensureAttributes]
- -[FBWorkspaceDomain _init]
- -[FBWorkspaceDomain _init].cold.1
- -[FBWorkspaceDomain _init].cold.2
- -[FBWorkspaceDomain _init].cold.3
- -[FBWorkspaceDomain _init].cold.4
- -[FBWorkspaceDomain _listener]
- -[FBWorkspaceDomain allowsDirectConnections]
- -[FBWorkspaceDomain assertionAttributesForWorkspaceState:].cold.1
- -[FBWorkspaceDomain endpoint]
- -[FBWorkspaceDomain nullEndpoint]
- -[FBWorkspaceDomain selfAssertionAttributesForWorkspaceState:].cold.2
- -[FBWorkspaceDomain startListener]
- -[FBWorkspaceEventDispatcher _flushCalloutsWithCompletion:]
- -[FBWorkspaceEventDispatcher _flushCalloutsWithCompletion:].cold.1
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:]
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.1
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.2
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.3
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.4
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.5
- -[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:].cold.6
- -[FBWorkspaceEventDispatcher _mainThread_dispatchHandshakeFromSource:toTarget:]
- -[FBWorkspaceEventDispatcher _mainThread_dispatchSceneRequestsFromSource:toTarget:]
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:]
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:].cold.1
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:].cold.2
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:].cold.3
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:].cold.4
- -[FBWorkspaceEventDispatcherSource _initWithProcessHandle:underlyingAssertion:].cold.5
- -[FBWorkspaceRegistration identifier]
- -[FBWorkspaceSceneRequest initWithTargetIdentifier:options:completion:]
- -[FBWorkspaceSceneRequest initWithTargetIdentifier:options:completion:].cold.1
- -[FBWorkspaceSceneRequest initWithTargetIdentifier:options:completion:].cold.2
- -[FBWorkspaceServiceDispatchingQueue .cxx_destruct]
- -[FBWorkspaceServiceDispatchingQueue _initWithTargetQueue:]
- -[FBWorkspaceServiceDispatchingQueue _initWithTargetQueue:].cold.1
- -[FBWorkspaceServiceDispatchingQueue assertBarrierOnQueue]
- -[FBWorkspaceServiceDispatchingQueue backingQueueIfExists]
- -[FBWorkspaceServiceDispatchingQueue performAsync:]
- -[FBWorkspaceServiceDispatchingQueue performAsync:withHandoff:]
- -[RBSAssertion(FBWorkspace) fb_setWorkspaceAssertionState:]
- -[RBSAssertion(FBWorkspace) fb_workspaceAssertionState]
- -[_FBSystemAppSceneInfo .cxx_destruct]
- -[_FBSystemAppSceneInfo FBSScene]
- -[_FBSystemAppSceneInfo hasHandledSceneCreate]
- -[_FBSystemAppSceneInfo hasSentFBSWorkspaceDelegateSceneCreate]
- -[_FBSystemAppSceneInfo pendingTransitionContext]
- -[_FBSystemAppSceneInfo setFBSScene:]
- -[_FBSystemAppSceneInfo setHasHandledSceneCreate:]
- -[_FBSystemAppSceneInfo setHasSentFBSWorkspaceDelegateSceneCreate:]
- -[_FBSystemAppSceneInfo setPendingTransitionContext:]
- GCC_except_table117
- GCC_except_table118
- GCC_except_table119
- GCC_except_table120
- GCC_except_table121
- GCC_except_table135
- GCC_except_table136
- GCC_except_table137
- GCC_except_table138
- GCC_except_table140
- GCC_except_table20
- GCC_except_table32
- GCC_except_table54
- GCC_except_table56
- GCC_except_table61
- _BSDispatchTimeWithInterval
- _FBSOrientationObserverMessageKeyDuration
- _FBSOrientationObserverMessageKeyOrientationInterest
- _FBSOrientationObserverMessageKeyRotationDirection
- _FBSOrientationObserverMessageKeySequenceNumber
- _FBSOrientationObserverMessageKeyUIOrientation
- _FBSOrientationObserverServiceIdentifier
- _FBSystemShellReadyNotification
- _FBWorkspaceAssertionStateCombine
- _FBWorkspaceAssertionStateIsForeground
- _FBWorkspaceLogCommon
- _FBWorkspaceLogCommon.__logObj
- _FBWorkspaceLogCommon.cold.1
- _FBWorkspaceLogCommon.onceToken
- _FBWorkspaceLogScene
- _FBWorkspaceLogScene.__logObj
- _FBWorkspaceLogScene.cold.1
- _FBWorkspaceLogScene.onceToken
- _FBWorkspaceLogSceneDeactivation
- _FBWorkspaceLogSceneDeactivation.__logObj
- _FBWorkspaceLogSceneDeactivation.cold.1
- _FBWorkspaceLogSceneDeactivation.onceToken
- _FBWorkspaceLogSceneHost
- _FBWorkspaceLogSceneHost.__logObj
- _FBWorkspaceLogSceneHost.cold.1
- _FBWorkspaceLogSceneHost.onceToken
- _FBWorkspaceLogSceneLayout
- _FBWorkspaceLogSceneLayout.__logObj
- _FBWorkspaceLogSceneLayout.cold.1
- _FBWorkspaceLogSceneLayout.onceToken
- _FBWorkspaceLogSnapshot
- _FBWorkspaceLogSnapshot.__logObj
- _FBWorkspaceLogSnapshot.cold.1
- _FBWorkspaceLogSnapshot.onceToken
- _FBWorkspaceLogTransaction
- _FBWorkspaceLogTransaction.__logObj
- _FBWorkspaceLogTransaction.cold.1
- _FBWorkspaceLogTransaction.onceToken
- _FBWorkspaceLogTransactionVerbose
- _FBWorkspaceLogTransactionVerbose.__logObj
- _FBWorkspaceLogTransactionVerbose.cold.1
- _FBWorkspaceLogTransactionVerbose.onceToken
- _FBWorkspaceLoggingSubsystem
- _FBWorkspaceTestsDomain
- _NSStringFromFBSSceneActivityMode
- _NSStringFromFBWorkspaceAssertionState
- _OBJC_CLASS_$_FBSSceneClientSettingsDiffInspector
- _OBJC_CLASS_$_FBSSerialQueue
- _OBJC_CLASS_$_FBSceneMonitor
- _OBJC_CLASS_$_FBSceneMonitorBehaviors
- _OBJC_CLASS_$_FBWorkspaceServiceDispatchingQueue
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$__FBSystemAppSceneInfo
- _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._interestedClients
- _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._interfaceOrientation
- _OBJC_IVAR_$_FBInterfaceOrientationServiceServer._sequenceNumber
- _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._callOutQueue
- _OBJC_IVAR_$_FBLocalSynchronousSceneClientProvider._workspaceInitialized
- _OBJC_IVAR_$_FBProcessExecutableSlice._subtype
- _OBJC_IVAR_$_FBProcessExecutableSlice._type
- _OBJC_IVAR_$_FBSceneEventQueue._delegate
- _OBJC_IVAR_$_FBSceneManagerObserver._didCommitDEPRECATED2
- _OBJC_IVAR_$_FBSceneManagerObserver._didCreateDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._didCreateSceneDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._didReceiveActionsDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._didSynchronizeLEGACY
- _OBJC_IVAR_$_FBSceneManagerObserver._didUpdateClientSettingsDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._internalObserver
- _OBJC_IVAR_$_FBSceneManagerObserver._supportLegacy
- _OBJC_IVAR_$_FBSceneManagerObserver._updateAppliedDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._updateCompletedDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._updatePreparedDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._willDestroyDEPRECATED
- _OBJC_IVAR_$_FBSceneManagerObserver._willSynchronizeLEGACY
- _OBJC_IVAR_$_FBSceneMonitor._delegate
- _OBJC_IVAR_$_FBSceneMonitor._delegateMonitorBehaviors
- _OBJC_IVAR_$_FBSceneMonitor._diffInspector
- _OBJC_IVAR_$_FBSceneMonitor._effectiveMonitorBehaviors
- _OBJC_IVAR_$_FBSceneMonitor._externalSceneIDs
- _OBJC_IVAR_$_FBSceneMonitor._givenMonitorBehaviors
- _OBJC_IVAR_$_FBSceneMonitor._identityToken
- _OBJC_IVAR_$_FBSceneMonitor._invalidated
- _OBJC_IVAR_$_FBSceneMonitor._isSynchronizing
- _OBJC_IVAR_$_FBSceneMonitor._pairedExternalSceneIDs
- _OBJC_IVAR_$_FBSceneMonitor._scene
- _OBJC_IVAR_$_FBSceneMonitor._sceneID
- _OBJC_IVAR_$_FBSceneMonitor._sceneManager
- _OBJC_IVAR_$_FBSceneMonitor._sceneSettings
- _OBJC_IVAR_$_FBSceneMonitor._updateExternalScenesAfterSync
- _OBJC_IVAR_$_FBSceneMonitor._updateSettingsAfterSync
- _OBJC_IVAR_$_FBSceneMonitorBehaviors._monitorsClientSettings
- _OBJC_IVAR_$_FBSceneMonitorBehaviors._monitorsPairingStatus
- _OBJC_IVAR_$_FBSceneMonitorBehaviors._monitorsSettings
- _OBJC_IVAR_$_FBSceneWorkspace._eventQueue
- _OBJC_IVAR_$_FBSceneWorkspace._pendingIdleEvents
- _OBJC_IVAR_$_FBSceneWorkspace._supportsLegacy
- _OBJC_IVAR_$_FBSystemShell._observerToken
- _OBJC_IVAR_$_FBWorkspace._lock_activeAssertionState
- _OBJC_IVAR_$_FBWorkspace._lock_invalidated
- _OBJC_IVAR_$_FBWorkspace._lock_outgoingEndpoint
- _OBJC_IVAR_$_FBWorkspace._queue
- _OBJC_IVAR_$_FBWorkspace._workspaceQueue
- _OBJC_IVAR_$_FBWorkspaceDomain._activation
- _OBJC_IVAR_$_FBWorkspaceDomain._bgActiveAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._bgLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._bgUserInitiatedAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._bgUtilityAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._bootstrapConfigured
- _OBJC_IVAR_$_FBWorkspaceDomain._fgFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgNonFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSupportFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSupportLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSupportNonFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSupportSuspendedAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSupportUtilityAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgSuspendedAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._fgUtilityAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._identifier
- _OBJC_IVAR_$_FBWorkspaceDomain._injectorAttributes
- _OBJC_IVAR_$_FBWorkspaceDomain._listener
- _OBJC_IVAR_$_FBWorkspaceDomain._machName
- _OBJC_IVAR_$_FBWorkspaceDomain._nullEndpoint
- _OBJC_IVAR_$_FBWorkspaceDomain._registration
- _OBJC_IVAR_$_FBWorkspaceDomain._utLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceEventDispatcherSource._underlyingAssertion
- _OBJC_IVAR_$_FBWorkspaceScene._queue_activityMode
- _OBJC_IVAR_$_FBWorkspaceScene._queue_assertionState
- _OBJC_IVAR_$_FBWorkspaceScene._queue_inFlightLifecycleEvents
- _OBJC_IVAR_$_FBWorkspaceServiceDispatchingQueue._targetQueue
- _OBJC_IVAR_$__FBSystemAppSceneInfo.FBSScene
- _OBJC_IVAR_$__FBSystemAppSceneInfo.hasHandledSceneCreate
- _OBJC_IVAR_$__FBSystemAppSceneInfo.hasSentFBSWorkspaceDelegateSceneCreate
- _OBJC_IVAR_$__FBSystemAppSceneInfo.pendingTransitionContext
- _OBJC_METACLASS_$_FBSceneMonitor
- _OBJC_METACLASS_$_FBSceneMonitorBehaviors
- _OBJC_METACLASS_$_FBWorkspaceServiceDispatchingQueue
- _OBJC_METACLASS_$__FBSystemAppSceneInfo
- __OBJC_$_CLASS_METHODS_FBLocalSynchronousSceneClientProvider
- __OBJC_$_CLASS_METHODS_FBWorkspaceDomain
- __OBJC_$_CLASS_METHODS_FBWorkspaceEventDispatcher
- __OBJC_$_CLASS_METHODS_FBWorkspaceRegistration
- __OBJC_$_INSTANCE_METHODS_FBProcessExecutableSlice
- __OBJC_$_INSTANCE_METHODS_FBSceneMonitor
- __OBJC_$_INSTANCE_METHODS_FBSceneMonitorBehaviors
- __OBJC_$_INSTANCE_METHODS_FBWorkspaceServiceDispatchingQueue
- __OBJC_$_INSTANCE_METHODS__FBSystemAppSceneInfo
- __OBJC_$_INSTANCE_VARIABLES_FBProcessExecutableSlice
- __OBJC_$_INSTANCE_VARIABLES_FBSceneMonitor
- __OBJC_$_INSTANCE_VARIABLES_FBSceneMonitorBehaviors
- __OBJC_$_INSTANCE_VARIABLES_FBWorkspaceServiceDispatchingQueue
- __OBJC_$_INSTANCE_VARIABLES__FBSystemAppSceneInfo
- __OBJC_$_PROP_LIST_FBDisplayManager
- __OBJC_$_PROP_LIST_FBProcessExecutableSlice
- __OBJC_$_PROP_LIST_FBSceneEventQueue
- __OBJC_$_PROP_LIST_FBSceneMonitor
- __OBJC_$_PROP_LIST_FBSceneMonitorBehaviors
- __OBJC_$_PROP_LIST_FBWorkspaceConnectionsStateStore
- __OBJC_$_PROP_LIST_FBWorkspaceRegistration
- __OBJC_$_PROP_LIST_FBWorkspaceServiceDispatchingQueue
- __OBJC_$_PROP_LIST__FBSystemAppSceneInfo
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSceneEventQueueDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneLayerManagerObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneManagerInternalObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneEventQueueDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneLayerManagerObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneManagerInternalObserver
- __OBJC_$_PROTOCOL_REFS_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_REFS_FBSceneEventQueueDelegate
- __OBJC_$_PROTOCOL_REFS_FBSceneLayerManagerObserver
- __OBJC_$_PROTOCOL_REFS_FBSceneManagerInternalObserver
- __OBJC_CLASS_PROTOCOLS_$_FBSceneMonitor
- __OBJC_CLASS_PROTOCOLS_$_FBSceneMonitorBehaviors
- __OBJC_CLASS_PROTOCOLS_$_FBWorkspaceServiceDispatchingQueue
- __OBJC_CLASS_RO_$_FBSceneMonitor
- __OBJC_CLASS_RO_$_FBSceneMonitorBehaviors
- __OBJC_CLASS_RO_$_FBWorkspaceServiceDispatchingQueue
- __OBJC_CLASS_RO_$__FBSystemAppSceneInfo
- __OBJC_LABEL_PROTOCOL_$_BSServiceDispatchingQueue
- __OBJC_LABEL_PROTOCOL_$_FBSceneEventQueueDelegate
- __OBJC_LABEL_PROTOCOL_$_FBSceneLayerManagerObserver
- __OBJC_LABEL_PROTOCOL_$_FBSceneManagerInternalObserver
- __OBJC_METACLASS_RO_$_FBSceneMonitor
- __OBJC_METACLASS_RO_$_FBSceneMonitorBehaviors
- __OBJC_METACLASS_RO_$_FBWorkspaceServiceDispatchingQueue
- __OBJC_METACLASS_RO_$__FBSystemAppSceneInfo
- __OBJC_PROTOCOL_$_BSServiceDispatchingQueue
- __OBJC_PROTOCOL_$_FBSceneEventQueueDelegate
- __OBJC_PROTOCOL_$_FBSceneLayerManagerObserver
- __OBJC_PROTOCOL_$_FBSceneManagerInternalObserver
- ___102-[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke
- ___102-[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.109
- ___114-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:]_block_invoke
- ___114-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:]_block_invoke_2
- ___114-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:]_block_invoke_3
- ___124-[FBSceneWorkspace _enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:]_block_invoke
- ___124-[FBSceneWorkspace _enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:]_block_invoke_2
- ___139-[FBSceneWorkspace _createSceneWithDefinition:settings:initialClientSettings:transitionContext:fromRemnant:usingClientProvider:completion:]_block_invoke
- ___179-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke
- ___179-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_2
- ___179-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_3
- ___179-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_4
- ___179-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:]_block_invoke_5
- ___24-[FBProcessManager init]_block_invoke
- ___24-[FBProcessManager init]_block_invoke.21
- ___24-[FBProcessManager init]_block_invoke_2
- ___24-[FBProcessManager init]_block_invoke_3
- ___27-[FBWorkspace sendActions:]_block_invoke.99
- ___28-[FBSceneMonitor invalidate]_block_invoke
- ___30-[FBProcess _bootstrapAndExec]_block_invoke.122
- ___30-[FBProcess _bootstrapAndExec]_block_invoke_2.123
- ___30-[FBWorkspaceDomain _listener]_block_invoke
- ___30-[FBWorkspaceDomain _listener]_block_invoke_2
- ___32+[FBSceneManager sharedInstance]_block_invoke
- ___34+[FBProcess rbInteractionWorkloop]_block_invoke
- ___34-[FBSystemShell _initWithOptions:]_block_invoke.36
- ___34-[FBSystemShell _initWithOptions:]_block_invoke.38
- ___35+[FBWorkspaceDomain sharedInstance]_block_invoke
- ___35-[FBProcessManager _removeProcess:]_block_invoke.112
- ___35-[FBSceneMonitorBehaviors isEqual:]_block_invoke
- ___35-[FBSceneMonitorBehaviors isEqual:]_block_invoke_2
- ___35-[FBSceneMonitorBehaviors isEqual:]_block_invoke_3
- ___37-[FBWorkspace initWithParentProcess:]_block_invoke
- ___38-[FBWorkspaceDomain _ensureAttributes]_block_invoke
- ___39-[FBProcess _notePendingExitForReason:]_block_invoke.84
- ___40-[FBScene _joinUpdate:block:completion:]_block_invoke.202
- ___40-[FBSceneMonitor _updateExternalScenes:]_block_invoke
- ___40-[FBSceneMonitor _updateExternalScenes:]_block_invoke_2
- ___42-[FBWorkspace _callOutQueue_requestScene:]_block_invoke
- ___43-[FBSceneMonitor _updateScenePairingState:]_block_invoke
- ___44+[FBWorkspaceEventDispatcher sharedInstance]_block_invoke
- ___44-[FBSceneWorkspace _endSynchronizationBlock]_block_invoke
- ___45-[FBWorkspaceEventDispatcher registerTarget:]_block_invoke.68
- ___46-[FBLocalSynchronousSceneClientProvider _init]_block_invoke
- ___46-[FBScene clientToken:didInvalidateWithError:]_block_invoke
- ___46-[FBSceneWorkspace _beginSynchronizationBlock]_block_invoke
- ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.180
- ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke
- ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke.24
- ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke.38
- ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.247
- ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.254
- ___50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.324
- ___50-[FBSceneWorkspace scene:didUpdateClientSettings:]_block_invoke
- ___50-[FBSceneWorkspace scene:didUpdateClientSettings:]_block_invoke_2
- ___50-[FBSceneWorkspace scene:didUpdateClientSettings:]_block_invoke_3
- ___50-[FBSceneWorkspace scene:didUpdateClientSettings:]_block_invoke_4
- ___51-[FBWorkspaceConnectionsStateStore _lastUsedBuffer]_block_invoke
- ___51-[FBWorkspaceServiceDispatchingQueue performAsync:]_block_invoke
- ___53-[FBSceneWorkspace scene:performCalloutsToObservers:]_block_invoke
- ___53-[FBSceneWorkspace scene:performCalloutsToObservers:]_block_invoke_2
- ___54-[FBProcessManager _bootstrap_consumeLock_addProcess:]_block_invoke.108
- ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.333
- ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.1
- ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.2
- ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.3
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.372
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_2.381
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke.258
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke.280
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_2
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_2.262
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_2.281
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_3
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_3.263
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_4
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_4.cold.1
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_5
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_6
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_7
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_7.cold.1
- ___54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_7.cold.2
- ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke_2
- ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.109
- ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.111
- ___55+[FBLocalSynchronousSceneClientProvider sharedInstance]_block_invoke
- ___55-[FBProcessManager noteProcessAssertionStateDidChange:]_block_invoke.54
- ___55-[FBScene _applyUpdate:postStateApplicator:completion:]_block_invoke
- ___55-[FBScene _applyUpdate:postStateApplicator:completion:]_block_invoke.168
- ___55-[FBScene _applyUpdate:postStateApplicator:completion:]_block_invoke.cold.1
- ___55-[FBScene _applyUpdate:postStateApplicator:completion:]_block_invoke_2
- ___55-[FBScene _applyUpdate:postStateApplicator:completion:]_block_invoke_3
- ___56-[FBProcess _lock_consumeLock_executeTerminationRequest]_block_invoke.295
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.337
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.343
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.351
- ___59-[FBWorkspaceEventDispatcher _flushCalloutsWithCompletion:]_block_invoke
- ___59-[FBWorkspaceOutgoingConnection workspaceLock_setEndpoint:]_block_invoke.75
- ___61-[FBWorkspaceIncomingConnection workspaceLock_setConnection:]_block_invoke.56
- ___62-[FBWorkspaceEventDispatcher registerSourceWithProcessHandle:]_block_invoke.cold.1
- ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.208
- ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.208.cold.1
- ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.208.cold.2
- ___63-[FBWorkspaceServiceDispatchingQueue performAsync:withHandoff:]_block_invoke
- ___64-[FBWorkspaceConnectionsStateStore _setFailureModeForNextWrite:]_block_invoke
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_2
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.cold.1
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.cold.2
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.cold.3
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.cold.4
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.cold.5
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_4
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_5
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_6
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_7
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_8
- ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_9
- ___78-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]_block_invoke
- ___78-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]_block_invoke.176
- ___78-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]_block_invoke_2
- ___78-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]_block_invoke_2.177
- ___78-[FBWorkspace _noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:]_block_invoke_3
- ___79-[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:]_block_invoke
- ___79-[FBWorkspaceEventDispatcher _initWithConnectionStore:preregisteredWorkspaces:]_block_invoke_2
- ___79-[FBWorkspaceEventDispatcher _mainThread_dispatchHandshakeFromSource:toTarget:]_block_invoke
- ___79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.103
- ___88-[FBInterfaceOrientationServiceServer _queue_handleRequestActiveOrientation:fromClient:]_block_invoke
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.91
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.97
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.98
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke_2.93
- ___92-[FBLocalSynchronousSceneClientProvider host:didInvalidateWithTransitionContext:completion:]_block_invoke
- ___92-[FBLocalSynchronousSceneClientProvider host:didInvalidateWithTransitionContext:completion:]_block_invoke_2
- ___92-[FBSceneMonitor scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke
- ___92-[FBSceneMonitor scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke_2
- ___99-[FBInterfaceOrientationServiceServer noteInterfaceOrientationChanged:animationSettings:direction:]_block_invoke
- ___99-[FBInterfaceOrientationServiceServer noteInterfaceOrientationChanged:animationSettings:direction:]_block_invoke.5
- ___FBWorkspaceAssertionState
- ___FBWorkspaceLogCommon_block_invoke
- ___FBWorkspaceLogSceneDeactivation_block_invoke
- ___FBWorkspaceLogSceneHost_block_invoke
- ___FBWorkspaceLogSceneLayout_block_invoke
- ___FBWorkspaceLogScene_block_invoke
- ___FBWorkspaceLogSnapshot_block_invoke
- ___FBWorkspaceLogTransactionVerbose_block_invoke
- ___FBWorkspaceLogTransaction_block_invoke
- ___LegacyManager
- ___WorkspacesMutationLock
- ___block_descriptor_32_e32_v16?0"FBSceneManagerObserver"8l
- ___block_descriptor_40_e8_32bs_e25_v16?0"FBSceneObserver"8ls32l8
- ___block_descriptor_40_e8_32bs_e32_v16?0"FBSceneManagerObserver"8ls32l8
- ___block_descriptor_40_e8_32s_e12_v24?08^B16ls32l8
- ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_40_e8_32s_e32_v16?0"FBSceneManagerObserver"8ls32l8
- ___block_descriptor_40_e8_32s_e52_v24?0"FBSceneObserver"8"FBSceneManagerObserver"16ls32l8
- ___block_descriptor_40_e8_32s_e56_v32?0"FBSSceneIdentity"8"_FBSystemAppSceneInfo"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8
- ___block_descriptor_40_e8_32w_e9_v16?0^v8lw32l8
- ___block_descriptor_41_e8_32s_e32_v16?0"FBSceneManagerObserver"8ls32l8
- ___block_descriptor_42_e8_32s_e52_v24?0"FBSceneObserver"8"FBSceneManagerObserver"16ls32l8
- ___block_descriptor_48_e8_32s40s_e22_v24?0"NSString"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionInternalConfiguring>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e52_v24?0"FBSceneObserver"8"FBSceneManagerObserver"16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_64_e8_32r_e33_v16?0"NSObject<OS_xpc_object>"8lr32l8
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e46_v16?0"<FBSWorkspaceServiceServerInterface>"8ls56l8s32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r_e27_v16?0"BSSimpleAssertion"8ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8u64l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_76_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s56s64bs72bs_e5_v8?0ls64l8s32l8s72l8s40l8s48l8s56l8
- ___block_descriptor_82_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
- ___block_descriptor_82_e8_32s40s48s56s64s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s72l8s40l8s80l8s48l8s56l8s64l8
- ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.10
- ___block_literal_global.11
- ___block_literal_global.111
- ___block_literal_global.121
- ___block_literal_global.144
- ___block_literal_global.162
- ___block_literal_global.178
- ___block_literal_global.190
- ___block_literal_global.200
- ___block_literal_global.201
- ___block_literal_global.22
- ___block_literal_global.246
- ___block_literal_global.299
- ___block_literal_global.4
- ___block_literal_global.7
- ___block_literal_global.87
- __ensureAttributes.onceToken
- __initWithIdentifier:legacy:.onceToken
- __listener.onceToken
- _objc_msgSend$FBSScene
- _objc_msgSend$_activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:
- _objc_msgSend$_authenticateAuditToken:entitlement:credentials:error:withResult:
- _objc_msgSend$_baseTransformForSnapshotContext:rootContext:
- _objc_msgSend$_callOutQueue_requestScene:
- _objc_msgSend$_collectLayersToSnapshotFromScene:withSnapshotContext:rootContext:
- _objc_msgSend$_evaluateEffectiveMonitorBehaviors
- _objc_msgSend$_initWithConnectionStore:preregisteredWorkspaces:
- _objc_msgSend$_initWithIdentifier:
- _objc_msgSend$_initWithIdentity:handle:executionContext:
- _objc_msgSend$_initWithObserver:supportLegacy:
- _objc_msgSend$_initWithProcessHandle:underlyingAssertion:
- _objc_msgSend$_initWithSceneManager:sceneID:
- _objc_msgSend$_initWithTargetQueue:
- _objc_msgSend$_internalObserver
- _objc_msgSend$_isInTransaction
- _objc_msgSend$_isSynchronizingSceneUpdates
- _objc_msgSend$_mainThread_dispatchHandshakeFromSource:toTarget:
- _objc_msgSend$_mainThread_dispatchSceneRequestsFromSource:toTarget:
- _objc_msgSend$_queueWithSerialDispatchQueue:
- _objc_msgSend$_queue_handleRegisterOrientationInterest:fromClient:
- _objc_msgSend$_queue_handleRequestActiveOrientation:fromClient:
- _objc_msgSend$_queue_updateInterest:forClient:withMessage:
- _objc_msgSend$_reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:
- _objc_msgSend$_registerBlockForWorkspaceCreation:
- _objc_msgSend$_sendSceneCreateFBSWorkspaceDelegateForSceneInfo:
- _objc_msgSend$_setEffectiveMonitorBehaviors:
- _objc_msgSend$_sharedWorkspaceIfExists
- _objc_msgSend$_updateAllSceneStateIgnoringDelegate
- _objc_msgSend$_updateExternalScenes:
- _objc_msgSend$_updateScenePairingState:
- _objc_msgSend$_updateSceneSettings:
- _objc_msgSend$acceptsClientScenes
- _objc_msgSend$addObserverForName:object:queue:usingBlock:
- _objc_msgSend$appendBool:counterpart:
- _objc_msgSend$appendFlag:withName:
- _objc_msgSend$assertOnQueue
- _objc_msgSend$assertionState
- _objc_msgSend$authenticateAuditToken:forEntitlement:withResult:
- _objc_msgSend$backingQueueIfExists
- _objc_msgSend$contentState
- _objc_msgSend$createCurrentProcess
- _objc_msgSend$createProcessWithExecutionContext:
- _objc_msgSend$createProcessWithHandle:
- _objc_msgSend$defaultIdentityForProcessIdentity:
- _objc_msgSend$delegateReceivesSceneActions
- _objc_msgSend$eventQueueDidDrain:
- _objc_msgSend$eventQueueDidUnlock:
- _objc_msgSend$externalSceneID
- _objc_msgSend$fb_fallbackSpecification
- _objc_msgSend$fb_setWorkspaceAssertionState:
- _objc_msgSend$fb_workspaceAssertionState
- _objc_msgSend$flushAllEvents
- _objc_msgSend$flushEvents:
- _objc_msgSend$handleSceneRequest:fromSource:
- _objc_msgSend$hasHandledSceneCreate
- _objc_msgSend$hasSandboxAccessForIdentifier:
- _objc_msgSend$hasSentFBSWorkspaceDelegateSceneCreate
- _objc_msgSend$identifierForName:
- _objc_msgSend$initWithContextID:
- _objc_msgSend$initWithDelegate:supportLegacy:
- _objc_msgSend$initWithObserver:supportLegacy:
- _objc_msgSend$initWithScene:snapshotContext:
- _objc_msgSend$initWithTargetIdentifier:options:completion:
- _objc_msgSend$inspectDiff:withContext:
- _objc_msgSend$intValue
- _objc_msgSend$isInternalObserver
- _objc_msgSend$loadRBSLaunchIdentifiers
- _objc_msgSend$mainDispatchQueue
- _objc_msgSend$monitorsClientSettings
- _objc_msgSend$monitorsPairingStatus
- _objc_msgSend$monitorsSettings
- _objc_msgSend$noteHandshakeFromSource:withRemnants:
- _objc_msgSend$numberWithUnsignedChar:
- _objc_msgSend$observePreferredSceneHostIdentifierWithBlock:
- _objc_msgSend$observePreferredSceneHostIdentityWithBlock:
- _objc_msgSend$pendingEvents
- _objc_msgSend$pendingTransitionContext
- _objc_msgSend$preferredSceneHostIdentifier
- _objc_msgSend$preferredSceneHostIdentity
- _objc_msgSend$rbInteractionWorkloop
- _objc_msgSend$registerProcessForHandle:
- _objc_msgSend$registerSourceWithProcessHandle:
- _objc_msgSend$registerTarget:
- _objc_msgSend$registrationWithIdentifier:options:
- _objc_msgSend$relinquishLock:
- _objc_msgSend$removeAllObservers
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$scene:deactivateAndInvalidate:withContext:block:
- _objc_msgSend$scene:didReceiveActions:forExtension:
- _objc_msgSend$scene:enqueueCalloutsToObserversWithEventName:block:
- _objc_msgSend$scene:handleUpdate:withCompletion:
- _objc_msgSend$scene:performCalloutsToObservers:
- _objc_msgSend$sceneManager:didCommitUpdateForScene:transactionID:success:
- _objc_msgSend$sceneManager:didCreateScene:
- _objc_msgSend$sceneManager:didCreateScene:withClient:
- _objc_msgSend$sceneManager:scene:didReceiveActions:
- _objc_msgSend$sceneManager:scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:
- _objc_msgSend$sceneManager:updateForScene:appliedWithContext:
- _objc_msgSend$sceneManager:updateForScene:completedWithContext:error:
- _objc_msgSend$sceneManager:updateForScene:preparedWithContext:
- _objc_msgSend$sceneManager:willDestroyScene:
- _objc_msgSend$sceneManagerDidEndSceneUpdateSynchronization:
- _objc_msgSend$sceneManagerWillBeginSceneUpdateSynchronization:
- _objc_msgSend$sceneMonitor:pairingStatusDidChangeForExternalSceneIDs:
- _objc_msgSend$sceneMonitor:sceneClientSettingsDidChangeWithDiff:transitionContext:
- _objc_msgSend$sceneMonitor:sceneSettingsDidChangeWithDiff:previousSettings:
- _objc_msgSend$sceneMonitor:sceneWasCreated:
- _objc_msgSend$sceneMonitor:sceneWasDestroyed:
- _objc_msgSend$setFBSScene:
- _objc_msgSend$setHasHandledSceneCreate:
- _objc_msgSend$setHasSentFBSWorkspaceDelegateSceneCreate:
- _objc_msgSend$setMonitorsClientSettings:
- _objc_msgSend$setMonitorsPairingStatus:
- _objc_msgSend$setMonitorsSettings:
- _objc_msgSend$setPendingTransitionContext:
- _objc_msgSend$setServiceQuality:
- _objc_msgSend$setState:
- _objc_msgSend$setTargetDispatchingQueue:
- _objc_msgSend$setTargetQueue:
- _objc_msgSend$setWithSet:
- _objc_msgSend$sliceWithType:subtype:
- _objc_msgSend$tokenFromAuditTokenRef:
- _objc_msgSend$unionSet:
- _objc_retain_x6
- _rbInteractionWorkloop.onceToken
- _rbInteractionWorkloop.queue
- _xpc_dictionary_get_uint64
- _xpc_dictionary_handoff_reply
- _xpc_dictionary_set_double
- _xpc_dictionary_set_uint64
CStrings:
+ "\n\""
+ "%@ is reserved"
+ "%@ is stuck (%@)"
+ "%@-%@[%u]"
+ "%{public}@ Enqueueing a cancel for a new connection (%p) to a workspace server that is in the process of exiting."
+ "%{public}@ Fallback lookup of processHandle is a mismatch : %{public}@ != %{public}@"
+ "%{public}@ Initial launch state: %{public}@."
+ "%{public}@ Terminating stuck process."
+ "%{public}@ Unblock returned an error: %{public}@"
+ "%{public}@ Unblock returned no result."
+ "%{public}@ Unblock returned with issue: %{public}@; confidence: %{public}@; status: %{public}@"
+ "%{public}@ Unexpectedly attempted to assign a new connection (%p) to a workspace server with an existing connection."
+ "%{public}@ Watchdog for %{public}@ is still active after %.1fs, notifying Unblock."
+ "%{public}@ Workspace assertion acquired: %{public}@"
+ "%{public}@ Workspace state did change: %{public}@ --> %{public}@ (%@)."
+ "(unknown - %ld)"
+ "+[FBSceneEventQueue executeWhenIdle:]"
+ "+[FBSceneEventQueue suspendIdleWorkForReason:]"
+ "-[FBScene _iterateObservers:]"
+ "-[FBScene sendInvocation:]"
+ "-[FBScene targetForInvocation:]"
+ "-[FBSceneEventQueue _relinquishIdleLockIfAppropriate]"
+ "-[FBSceneLayerManager _rebuildLayers]"
+ "-[FBSceneLayerManager _suspendUpdatesWithReason:]"
+ "-[FBSceneLayerManager _suspendUpdatesWithReason:]_block_invoke"
+ "-[FBSceneSnapshot _initWithScene:configuration:]"
+ "-[FBSceneWorkspace _initWithProcessManager:identifier:]"
+ "-[FBSceneWorkspace setIdentity:]"
+ "0x%llx"
+ "<FBSceneSynchronizer:%p %@>"
+ "<FBSceneSynchronizer:%p %@[%i]>"
+ "<FBWorkspaceEndpointPromise:%@ (%@)>"
+ "<FBWorkspaceEndpointPromise:%@ (null)>"
+ "<FBWorkspaceEndpointPromise:%@>"
+ "@\"<FBSProcess>\""
+ "@\"<FBSceneSnapshotInternalConfiguration>\""
+ "@\"<FBWorkspaceDomainConnectionDelegate>\""
+ "@\"BSEventQueueLock\""
+ "@\"BSServiceCompoundQueue\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceQueue\"16@0:8"
+ "@\"FBLocalSynchronousSceneClientProvider\""
+ "@\"FBSOrientationUpdate\"16@0:8"
+ "@\"FBSProcessExecutableSlice\""
+ "@\"FBSProcessTerminationRequest\"32@0:8@\"FBSProcessWatchdog\"16@\"NSError\"24"
+ "@\"FBSSceneSettings\"16@0:8"
+ "@\"FBSWorkspace\""
+ "@\"FBSWorkspaceCoupler\""
+ "@\"FBSceneSynchronizer\""
+ "@\"FBWorkspaceDomain\""
+ "@\"FBWorkspaceEndpointPromise\""
+ "@\"FBWorkspaceEventDispatcher\""
+ "@\"NSDate\"16@0:8"
+ "@\"RBSAttribute\""
+ "@24@0:8@\"FBSInvocation\"16"
+ "@28@0:8I16Q20"
+ "@48@0:8@16@24@32@?40"
+ "AB"
+ "Active"
+ "B20@0:8C16"
+ "B32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
+ "B48@0:8@16@24Q32o^@40"
+ "BG"
+ "Cannot create a local scene future for workspace \"%@\"."
+ "Cannot create a local scene future with identity=%@ as no default workspace is defined."
+ "Cannot request a local scene with identifier=%@ as no default workspace is defined."
+ "Class getUBStuckServiceClass(void)_block_invoke"
+ "Class getUBUnblockClientClass(void)_block_invoke"
+ "Client was unable to decode scene parameters"
+ "Debugging"
+ "Domain is missing %@ service, not creating interface orientation server."
+ "FBLocalSynchronousSceneClientProvider:%p deallocing."
+ "FBLocalSynchronousSceneClientProvider:%p invalidating."
+ "FBMutableSceneSnapshotConfiguration"
+ "FBProcess:%@"
+ "FBProcessManager-%p"
+ "FBProcessManager-sharedInstance"
+ "FBProcessManager:%p deallocing."
+ "FBProcessWatchdog.m"
+ "FBSComponentSceneSupport"
+ "FBSInvocationReceiving"
+ "FBSInvocationSending"
+ "FBSOrientationServiceServerInterface"
+ "FBSWorkspace"
+ "FBSceneEventQueue.m"
+ "FBSceneManagerSceneCreating"
+ "FBSceneSnapshotConfiguration"
+ "FBSceneSnapshotConfigurator"
+ "FBSceneSnapshotInternalConfiguration"
+ "FBSceneSynchronizer"
+ "FBSceneSynchronizer.m"
+ "FBWorkspace-%@"
+ "FBWorkspaceAssertionAttributes"
+ "FBWorkspaceDomain: Enqueuing new direct workspace connection %p with remoteToken=%{public}@"
+ "FBWorkspaceDomain: Invalidating defunct indirect connection %p with remoteToken=%{public}@"
+ "FBWorkspaceDomain: Invalidating enqueued direct connection %p with remoteToken=%{public}@"
+ "FBWorkspaceDomain: Invalidating pended indirect connection %p with remoteToken=%{public}@"
+ "FBWorkspaceDomain: Unable to register new direct connection with remoteToken=%{public}@ because the service doesn't declare support for direct connections"
+ "FBWorkspaceDomain: Unable to validate new incoming connection because the remote was unknown : connection=%@"
+ "FBWorkspaceDomain: injecting saved endowment"
+ "FBWorkspaceDomain: registering saved endowment %{public}@"
+ "FBWorkspaceDomain:%p deallocing."
+ "FBWorkspaceDomainConnectionDelegate"
+ "FBWorkspaceEndpointPromise"
+ "FBWorkspaceEventDispatcher:%p deallocing."
+ "Failed to begin tracking vpid %{public}@ as %{public}@"
+ "Focal"
+ "Ignoring double local source handshake"
+ "Ignoring invalid source handshake for %{public}i"
+ "Ignoring scene request from local source as we've already been invalidated"
+ "Immediately invalidating new source %{public}@ due to previous dispatcher invalidation : %{public}@"
+ "Interactive"
+ "Jetsam-Active"
+ "Jetsam-Background"
+ "Jetsam-FGSupport"
+ "Jetsam-Focal"
+ "Jetsam-Foreground"
+ "Jetsam-Opportunistic"
+ "Jetsam-UISupport"
+ "Jetsam-Utility"
+ "Jetsam-Utility2"
+ "Jetsam-Utility3"
+ "Legacy FBSceneManager does not support client scene futures"
+ "Local scene future %{public}@ has out-of-date clientSettings : %@"
+ "Local scene future %{public}@ was activated with modified settings : %@"
+ "LocalSynchronousSceneClientProvider failed to receive workspace creation."
+ "No client scene exists"
+ "Opportunistic"
+ "ProcessManager has been invalidated."
+ "Registering orientation interest for %@ "
+ "RunningBoard returned a currentProcess with no identity : %@"
+ "RunningBoard returned no identity for a processHandle : %@"
+ "Scene create failed"
+ "Scene creation failed"
+ "Scene invalidation failed."
+ "Scene reconnect failed"
+ "Scene was invalidated by the client."
+ "Scene was not created."
+ "SceneIdleEvents"
+ "Service has been unsuspended."
+ "SharedInstance"
+ "SuspendIdleWork"
+ "T@\"<FBSProcess>\",R,C,N"
+ "T@\"<FBSceneSnapshotConfiguration>\",R,C,N,V_config"
+ "T@\"BSServiceDispatchQueue\",R,N,V_queue"
+ "T@\"BSServiceDispatchQueue\",R,N,V_workspaceQueue"
+ "T@\"BSServiceQueue\",R,N"
+ "T@\"BSServiceQueue\",R,N,V_serviceQueue"
+ "T@\"BSSettings\",R,C,N,V_clientExtendedData"
+ "T@\"FBSProcessExecutableSlice\",&,D,N"
+ "T@\"FBSProcessExecutableSlice\",&,N,V_overrideExecutableSlice"
+ "T@\"FBSSceneClientIdentity\",R,C,N,V_clientIdentity"
+ "T@\"FBSSceneSettings\",R,C,N,V_settings"
+ "T@\"FBSceneSynchronizer\",&,N,V_synchronizer"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_expirationDate"
+ "T@\"NSObject<OS_dispatch_workloop>\",R,&,N"
+ "T@\"NSSet\",C,N"
+ "T@,&,N"
+ "T@,&,N,V_userInfo"
+ "T@,R,N"
+ "TB,N,GisOpaque"
+ "TB,R,N,GisOpaque"
+ "TB,R,N,V_clientAllowsProtectedContent"
+ "TQ,R,N,V_renderID"
+ "This process will acquire %{public}@ workspace self-assertions."
+ "Tq,R,N,V_orientation"
+ "T{?=I},N,Gfb_workspaceState,Sfb_setWorkspaceState:"
+ "T{?=I},R,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
+ "UBStuckService"
+ "UBUnblockClient"
+ "Unable to resolve vpid %{public}@: %{public}@"
+ "Unregistering orientation interest for %@ "
+ "Updating self-assertion for unified workspace priority: %{public}@"
+ "Utility"
+ "Vv24@0:8@?16"
+ "Vv24@0:8@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">16"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">24"
+ "Workspace-Active"
+ "Workspace-Focal"
+ "Workspace-Interactive"
+ "Workspace-NonUI"
+ "Workspace-Opportunistic"
+ "Workspace-UI"
+ "Workspace-Utility"
+ "WorkspaceReconnect"
+ "["
+ "[%@] workspace delegate %@ mutated settings: %@"
+ "[%{public}@] Aborted invocation due to connection mismatch : connection=%@ expected=%@"
+ "[%{public}@] Dropping invocations for non-active scene."
+ "[%{public}@] Explicit client invalidation."
+ "[%{public}@] Ignoring invocations due to token mismatch (probably due to prior deactivation). expected=%p received=%p"
+ "[%{public}@] Scene creation failed: %{public}@"
+ "[%{public}@] Scene state did change: %{public}@."
+ "[%{public}@] Send invocations timed out."
+ "[%{public}@] Sending scene reconnect."
+ "[%{public}@] Unable to deliver invocation because no scene exists with this identity."
+ "[%{public}@] Unable to invalidate because no scene exists with this identity."
+ "[%{public}@] Update was a no-op."
+ "[[error domain] isEqualToString:FBSceneErrorDomain]"
+ "[_pendingScenes containsObject:scene]"
+ "[self _legacyWorkspace]"
+ "]"
+ "_FBLocalSceneInfo"
+ "_UIAttributes"
+ "_activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:"
+ "_activeAttributes"
+ "_authenticateAuditToken:entitlement:credentials:error:"
+ "_bootstrapLock_invalidated"
+ "_callOutQueue_workspace"
+ "_clientAllowsProtectedContent"
+ "_clientFutureHostsBeingSynchronized"
+ "_clientFutureScenesBeingSynchronized"
+ "_config"
+ "_connectionInvalidated:"
+ "_coupler"
+ "_currentConnection"
+ "_deactivateClient:withContext:"
+ "_dispatcher"
+ "_domainIdentifier"
+ "_endpointPromise"
+ "_enqueueClientConnectionBlock:"
+ "_eventDispatcher"
+ "_extension"
+ "_findDomainSpecification"
+ "_focalAttributes"
+ "_getPolicyWallTime:cpuTime:"
+ "_icdLock"
+ "_icdLock_indirectConnectionDelegate"
+ "_icdLock_pendingIndirectConnectionBlocks"
+ "_idleEventLock"
+ "_initWithCoupler:specification:"
+ "_initWithDispatcher:process:"
+ "_initWithDomain:connectionStore:preregisteredWorkspaces:"
+ "_initWithDomain:service:"
+ "_initWithIdentifier:workspaceQueue:dispatcher:"
+ "_initWithObserver:workspace:"
+ "_initWithProcessHandle:invalidationBlock:"
+ "_initWithProcessManager:"
+ "_initWithProcessManager:identifier:"
+ "_initWithProcessManager:identity:handle:executionContext:"
+ "_initWithWorkspaceCoupler:currentProcess:eventDispatcher:"
+ "_initWithWorkspaceDomain:"
+ "_interactiveAttributes"
+ "_invalidate"
+ "_invalidateWithCompletion:"
+ "_invalidationLock"
+ "_isSameAsWorkspace:"
+ "_isSharedInstance"
+ "_listenerEndpoint"
+ "_lock_activation"
+ "_lock_connections"
+ "_lock_domain"
+ "_lock_endpoint"
+ "_lock_injectEndpointToFBSWorkspace"
+ "_lock_interestedConnections"
+ "_lock_interfaceOrientation"
+ "_lock_invalidationBlock"
+ "_lock_legacySceneManager"
+ "_lock_listener"
+ "_lock_noteInterfaceOrientationChanged:animationSettings:direction:"
+ "_lock_outgoingEndpointPromise"
+ "_lock_pendingConnections"
+ "_lock_process"
+ "_lock_registerOrientationInterest:connection:completion:"
+ "_lock_registration"
+ "_lock_sendMessageToInterestedClients:"
+ "_lock_sequenceNumber"
+ "_lock_serviceSuspended"
+ "_lock_syncLocalSceneClientProvider"
+ "_lock_waitingForConnect"
+ "_needsRebuildLayers"
+ "_nonUIAttributes"
+ "_noteProcessBootstrapped:withHandle:assertion:outgoingEndpointPromise:"
+ "_noteSourceDidInvalidate:withPIDNumber:"
+ "_opportunisticAttributes"
+ "_pendingScenes"
+ "_processCallOutQueue_requestScene:"
+ "_queue_eventsCompleteSignal"
+ "_queue_inFlightDeactivationEvents"
+ "_queue_invalidated"
+ "_queue_workspaceState"
+ "_reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:"
+ "_reallyRegisterProcessForHandle: returned a mismatched vpid : requested=%@ actual=%@ handle=%@"
+ "_rebuildLayers"
+ "_registerProcessForViewServiceWithProcessHandle:error:"
+ "_removeSuspendAssertion:"
+ "_renderID"
+ "_sendToHost:updatedClientSettings:withDiff:transitionContext:"
+ "_sendToSceneWithInfo:updatedSettings:withDiff:transitionContext:completion:"
+ "_serviceQueue"
+ "_setProcessHandle:"
+ "_sharedInstance"
+ "_specification"
+ "_suspendAssertions"
+ "_suspendUpdatesWithReason:"
+ "_synchronizer"
+ "_unblockSignal"
+ "_updateSuspendIdleWork"
+ "_userInfo"
+ "_utilityAttributes"
+ "_visibilityAttribute"
+ "_watchdog:terminationRequestForError:"
+ "activation"
+ "activeOrientationDidUpdate:"
+ "addEndpoint:"
+ "all scenes must be invalidated before the syncLocal provider can invalidate"
+ "already have an indirectConnectionDelegate : existing=%@ new=%@"
+ "already invalidated"
+ "already registered scene for %@ is not in the pending set: %@"
+ "already tracking a scene with identity %@"
+ "appendInt64:"
+ "appendInt64:counterpart:"
+ "applyContext:"
+ "asked for the listenerEndpoint before the processConnectionDelegate is registered"
+ "assertion acquired"
+ "assertion acquisition failed!"
+ "assertion dropped"
+ "assertion superseded"
+ "attemp to set state after invalidation"
+ "attempt to `applyContext:` for id='%@' to scene with id='%@'"
+ "attempt to enqueue scene request after invalidation"
+ "attempt to handshake after invalidation"
+ "attempt to set an indirectConnectionDelegate after invalidation : new=%@"
+ "awaiting concrete target"
+ "b2"
+ "bogus jetsam offset %u"
+ "call scene:didUpdateSettings: instead"
+ "cancel"
+ "cannot currently support actions from a local host during the sync phase of connection : %@"
+ "cannot currently support actions from a local scene during the sync phase of connection : %@"
+ "cannot currently support invalidating from a local host during the sync phase of connection : %@"
+ "cannot currently support invalidations from a local scene during the sync phase of connection : %@"
+ "cannot currently support invocations from a local scene during the sync phase of connection : %@"
+ "cannot currently support messages from a local scene during the sync phase of connection : %@"
+ "cannot currently support updates from a local scene during the sync phase of connection : %@"
+ "cannot currently support updating from a local host during the sync phase of connection : %@"
+ "cannot deactivate a scene while content state is changing"
+ "cannot deactivate a scene while it is updating"
+ "cannot deactivate while updating"
+ "cannot update a scene while it is deactivating"
+ "cannot update from a local host while the scene is still pending : %@"
+ "cannotResolveForReason:"
+ "captureCompletions"
+ "client-invalidated"
+ "clientAllowsProtectedContent"
+ "clientToken:deactivateWithContext:"
+ "clientToken:handleInvocation:withReply:"
+ "com.apple.frontboard.detached-scene-synchronizer<%@>"
+ "com.apple.frontboard.process.user-initiated"
+ "com.apple.frontboard.systemappservices"
+ "com.apple.private.unblock"
+ "com.apple.runningboard.process-state"
+ "compatibleWithTarget:"
+ "configuration"
+ "configureParameters"
+ "connections"
+ "deactivation"
+ "deadlock"
+ "definitive"
+ "detachedSynchronizerWithIdentifier:"
+ "didAddScene:"
+ "dispatcher"
+ "domain:didReceiveConnection:withContext:"
+ "endpointPromise"
+ "entitled"
+ "eventDispatcher"
+ "executeOrAppend:"
+ "executeWhenIdle:"
+ "extension"
+ "failed to lookup viewService process with pid=%i : error=%{public}@"
+ "failed to register viewService process %{public}@ : error=%{public}@"
+ "fb_setWorkspaceState:"
+ "fb_workspaceState"
+ "finish-task"
+ "finishUpdate"
+ "forceLookupIdentifer:error:"
+ "handleForAudiToken: returned a mismatched vpid : requested=%@ actual=%@ handle=%@"
+ "handleForAuditToken:error:"
+ "host:sendInvocation:withReply:"
+ "identityForInjectedEndpointToProcessIdentity:"
+ "idleEvent"
+ "illegal operation after invalidation"
+ "incomingWorkspaceEndpoint"
+ "indirect-correlation"
+ "info != nil"
+ "init is not allowed on FBProcessManager"
+ "init is not allowed on FBWorkspace"
+ "initForPid:threadID:timeElapsed:incidentUUID:"
+ "initWithClientIdentity:targetIdentifier:options:completion:"
+ "initWithContextID:renderID:"
+ "initWithDelegate:workspace:"
+ "initWithObserver:workspace:"
+ "initWithOrientation:sequenceNumber:duration:rotationDirection:"
+ "initWithReason:invalidatedWithContextBlock:"
+ "initWithScene:configurator:"
+ "initWithScene:context:"
+ "initialize"
+ "injectEndpointToFBSWorkspace"
+ "injectorWithConfigurator:"
+ "interestedConnections"
+ "internally-stuck"
+ "invalidate must be called before deallocing"
+ "invalidationBlock"
+ "invokeWithReceiver:replyHandler:"
+ "isBSServiceConnectionError"
+ "isIdleWorkSuspended"
+ "isInvalidated == YES"
+ "issueType"
+ "jetsamPriority"
+ "launchIdentifiers"
+ "legacySceneManagerCreatingIfNecessary:"
+ "machQueue"
+ "missing workspace service"
+ "must call _invalidateWithCompletion: before dealloc"
+ "must have already sent the scene create: %@"
+ "must not have an assertion if we're invalidated"
+ "needsRebuild"
+ "never nil if created by FBWorkspaceDomain"
+ "new processHandle=%@ mismatches previous=%@"
+ "no FBSScene for active FBScene"
+ "numberWithUnsignedInt:"
+ "opportunistic"
+ "pendingConnections"
+ "performAsyncOnSendingQueue:"
+ "prepareSnapshot"
+ "prepareSnapshotWithConfigurator:"
+ "processManager"
+ "queueWithDispatchQueue:targetQueue:"
+ "queueWithName:serviceQuality:"
+ "queueWithName:serviceQuality:targetQueue:"
+ "r"
+ "recover:stackshotData:replyQueue:callback:"
+ "recovered"
+ "recoveryConfidence"
+ "recoveryStatus"
+ "registerOrientationInterest:completion:"
+ "relinquish"
+ "remnant"
+ "renderID"
+ "request"
+ "requestActiveOrientation"
+ "requestActiveOrientationCompletion:"
+ "resolve"
+ "scene is not active"
+ "scene is not currently mutable"
+ "scene-creation-failed"
+ "scene:didApplyUpdate:"
+ "scene:didCompleteUpdate:"
+ "scene:didPrepareUpdate:"
+ "scene:invalidateWithTransitionContext:"
+ "scene:sendInvocation:"
+ "sceneID:handleInvocation:completion:"
+ "sceneID:invalidateWithContext:clientError:"
+ "sceneObserverWantsUpdatesFromInactiveScenes"
+ "sceneUpdate"
+ "send-message-failed"
+ "sendBatchedMessages"
+ "sendInvocation:"
+ "serviceQueue"
+ "serviceWithClass:"
+ "setIndirectConnectionDelegate:"
+ "setInitialClientSettings:"
+ "setInitialSettings:"
+ "setQueue:"
+ "setSequenceNumber:"
+ "setSynchronizer:"
+ "setTarget:"
+ "setUserInfo:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient"
+ "somehow already initializing this host? host=%@ : beingInitialized=%@"
+ "somehow already initializing this scene? scene=%@ : beingInitialized=%@"
+ "something bad happened that removed the host prematurely from the initializing set : host=%@ beingInitialized=%@"
+ "something bad happened that removed the scene prematurely from the initializing set : scene=%@ beingInitialized=%@"
+ "source"
+ "startWorkspaceDomainListener"
+ "store"
+ "suspendAssertions"
+ "suspendIdleWorkForReason:"
+ "syncLocalSceneClientProvider"
+ "synchronizer"
+ "synchronizerForViewServiceWithProcessIdentifier:"
+ "targetForInvocation:"
+ "the currentProcess may never have remnants"
+ "this instance may not invalidate"
+ "thread-exhaustion"
+ "trying to unregister a local host during the sync phase of connection : %@"
+ "undefined"
+ "unknown processClass for currentProcessHandle : %@"
+ "unknown(%i)"
+ "unrecovered"
+ "userInitiatedWorkloop"
+ "v16@?0@\"<BSServiceConnectionEndpointInjectorConfiguring>\"8"
+ "v16@?0@\"<BSSimpleAssertionInvalidationContext>\"8"
+ "v16@?0@\"<FBSOrientationServiceClientInterface>\"8"
+ "v16@?0@\"<FBWorkspaceDomainConnectionDelegate>\"8"
+ "v16@?0@\"FBWorkspaceEventDispatcherSource\"8"
+ "v16@?0@8"
+ "v20@0:8{?=I}16"
+ "v24@0:8@\"FBSInvocation\"16"
+ "v24@0:8@\"FBSSceneIdentity\"16"
+ "v24@0:8@\"FBSSceneSnapshotContext\"16"
+ "v24@0:8@\"NSSet\"16"
+ "v24@?0@\"FBSInvocationReply\"8@\"NSError\"16"
+ "v24@?0@\"FBSScene\"8@\"NSError\"16"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v32@0:8@\"<NSObject>\"16@\"FBSSceneTransitionContext\"24"
+ "v32@0:8@\"FBSScene\"16@\"FBSInvocation\"24"
+ "v32@0:8@\"FBSScene\"16@\"FBSSceneTransitionContext\"24"
+ "v32@0:8@\"NSSet\"16#24"
+ "v32@0:8o^d16o^d24"
+ "v32@?0@\"FBSSceneIdentity\"8@\"_FBLocalSceneInfo\"16^B24"
+ "v32@?0@\"FBSSceneIdentity\"8@16^B24"
+ "v36@0:8I16@20@?28"
+ "v40@0:8@\"<FBSceneHost>\"16@\"FBSInvocation\"24@?<v@?@\"FBSInvocationReply\"@\"NSError\">32"
+ "v40@0:8@\"<NSObject>\"16@\"FBSInvocation\"24@?<v@?@\"FBSInvocationReply\"@\"NSError\">32"
+ "v40@0:8@\"FBWorkspaceDomain\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
+ "void *UnblockClientLibrary(void)"
+ "we should never get a scene request without a clientIdentity specified by the time it gets through the dispatcher : %@"
+ "workspace assertion but no workspace state"
+ "workspace's process bootstrapped without a handle but still had a valid outgoing endpoint promise : process=%@ endpointPromise=%@"
+ "workspaceCoupler"
+ "workspaceDomain"
+ "workspaceQueue"
+ "workspaceState"
+ "{?=\"contentStateDidChange\"B\"didUpdateSettings\"B\"updatePreparedLEGACY\"B\"updateAppliedLEGACY\"B\"updateCompletedLEGACY\"B\"didUpdateClientSettings\"B\"clientSettingsUpdatedLEGACY\"B\"willActivate\"B\"didActivate\"B\"willDeactivateWithError\"B\"willDeactivateWithContext\"B\"didInvalidate\"B\"didInvalidateWithContext\"B\"clientDidConnect\"B\"handleActions\"B\"wantsInactiveUpdates\"B}"
+ "{?=\"rawValue\"I}"
+ "{?=I}16@0:8"
+ "\xf0A"
- "\v"
- "![scene _isInTransaction]"
- "!_inTransaction"
- "!_midUpdate"
- "%{public}@ Cannot acquire assertion until we have a target."
- "%{public}@ Initial launch assertion state: %{public}@."
- "%{public}@ Launch assertion supersedes update of workspace assertion to %{public}@."
- "%{public}@ Launch assertion will be superseded by workspace assertion."
- "%{public}@ Now acquiring workspace assertion with state: %{public}@."
- "%{public}@ Unexpectedly attempted to assign a new connection to a workspace server with an existing connection."
- "%{public}@ Workspace assertion state did change: %{public}@ (acquireAssertion = %{BOOL}u)."
- "-[FBLocalSynchronousSceneClientProvider _init]_block_invoke"
- "-[FBLocalSynchronousSceneClientProvider host:didInvalidateWithTransitionContext:completion:]"
- "-[FBLocalSynchronousSceneClientProvider host:didReceiveActions:forExtension:]"
- "-[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:]"
- "-[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:]"
- "-[FBLocalSynchronousSceneClientProvider scene:didReceiveActions:forExtension:]"
- "-[FBLocalSynchronousSceneClientProvider scene:didUpdateClientSettings:withDiff:transitionContext:]"
- "-[FBLocalSynchronousSceneClientProvider unregisterHost:]"
- "-[FBSceneSnapshot initWithScene:snapshotContext:]"
- "-[FBSceneWorkspace _beginSynchronizationBlock]"
- "-[FBSceneWorkspace _endSynchronizationBlock]"
- "-[FBSceneWorkspace _enqueueEventForScene:withName:block:]"
- "-[FBSceneWorkspace _enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:]"
- "-[FBSceneWorkspace _executeEventWhenIdle:]"
- "-[FBSceneWorkspace _executeNextIdleEventIfAppropriate]"
- "-[FBSceneWorkspace _initWithIdentifier:legacy:]"
- "-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]"
- "-[FBSceneWorkspace scene:didReceiveActions:forExtension:]"
- "-[FBSceneWorkspace scene:didUpdateClientSettings:]"
- "-[FBSceneWorkspace scene:handleUpdate:withCompletion:]"
- "-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_6"
- "."
- "/\v"
- "3`"
- "<%@; type: %d; subtype: %d>"
- "@\"<FBSceneEventQueueDelegate>\""
- "@\"<FBSceneMonitorDelegate>\""
- "@\"FBProcessExecutableSlice\""
- "@\"FBSMutableSceneSettings\""
- "@\"FBSProcessTerminationRequest\"40@0:8@\"FBSProcessWatchdog\"16@\"FBSProcessExecutionProvision\"24@\"NSError\"32"
- "@\"FBSSceneClientSettingsDiffInspector\""
- "@\"FBSSceneTransitionContext\"32@0:8@\"FBSceneManager\"16@\"FBScene\"24"
- "@\"FBSSerialQueue\""
- "@\"FBSSerialQueue\"16@0:8"
- "@\"FBSceneMonitorBehaviors\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@28@0:8@16B24"
- "@56@0:8@16@24@32@40@48"
- "BSServiceDispatchingQueue"
- "BackgroundActive"
- "BackgroundUtility"
- "Begin scene update synchronization."
- "C16@0:8"
- "Client is nil"
- "ClientConnected"
- "Common"
- "Dropping actions since manager delegate does not implement handler: %{public}@"
- "End scene update synchronization."
- "FBLocalSynchronousSceneClientProvider should not deallocate"
- "FBOrientationServiceServer"
- "FBSScene"
- "FBSWorkspaceSceneRequestOptions"
- "FBSceneDeactivate"
- "FBSceneEventQueueDelegate"
- "FBSceneLayerManagerObserver"
- "FBSceneManagerInternalObserver"
- "FBSceneMonitor"
- "FBSceneMonitor.m"
- "FBSceneMonitorBehaviors"
- "FBSceneUpdate"
- "FBSystemShellReadyNotification"
- "FBWorkspaceDomain: Registering new direct workspace connection with remoteToken=%{public}@"
- "FBWorkspaceDomain: Unable to assign new incoming connection to a process because the remote was unknown : connection=%@"
- "FBWorkspaceDomain: Unable to register new direct workspace connection with remoteToken=%{public}@ because the service doesn't declare support for direct connections"
- "FBWorkspaceDomain: registering saved endowment for workspace endpoint : %{public}@"
- "FBWorkspaceServiceDispatchingQueue"
- "FBWorkspaceTests"
- "ForegroundFocal"
- "ForegroundNonFocal"
- "ForegroundSupportFocal"
- "ForegroundSupportNonFocal"
- "ForegroundSupportSuspended"
- "ForegroundSupportUtility"
- "ForegroundSuspended"
- "ForegroundUtility"
- "Ignoring invalid source registration for %{public}i"
- "Initial settings may only be adjusted at create time before any transactions have begun."
- "NSDictionary"
- "RBSProcessIdentity"
- "SceneDeactivation"
- "SceneHost"
- "SceneLayout"
- "Snapshot"
- "T@\"<FBSceneEventQueueDelegate>\",W,N,V_delegate"
- "T@\"<FBSceneMonitorDelegate>\",W,N,V_delegate"
- "T@\"BSSettings\",C,N,V_clientExtendedData"
- "T@\"FBProcessExecutableSlice\",&,D,N"
- "T@\"FBProcessExecutableSlice\",&,N,V_overrideExecutableSlice"
- "T@\"FBSScene\",&,N,VFBSScene"
- "T@\"FBSSceneSettings\",C,N,V_settings"
- "T@\"FBSSceneTransitionContext\",&,N,VpendingTransitionContext"
- "T@\"FBSSerialQueue\",R,N,V_queue"
- "T@\"FBSceneMonitorBehaviors\",C,N,V_givenMonitorBehaviors"
- "T@\"FBWorkspaceConnectionsState\",C,N"
- "T@\"NSDate\",&,N,V_expirationDate"
- "TB,N,Stest_setRejectAllSceneClients:,V_test_rejectAllSceneClients"
- "TB,N,V_monitorsClientSettings"
- "TB,N,V_monitorsPairingStatus"
- "TB,N,V_monitorsSettings"
- "TB,N,VhasHandledSceneCreate"
- "TB,N,VhasSentFBSWorkspaceDelegateSceneCreate"
- "TB,R,N,V_acceptsClientScenes"
- "TC,N,Gfb_workspaceAssertionState,Sfb_setWorkspaceAssertionState:"
- "TC,R,N"
- "Td,N"
- "This process will acquire workspace self-assertions (enhanced: %{bool}u)"
- "Ti,R,N,V_subtype"
- "Ti,R,N,V_type"
- "Tq,N,V_orientation"
- "TransactionVerbose"
- "Unable to establish XPC connection."
- "Updating self-assertion for unified workspace state: %{public}@"
- "Workspace-BackgroundActive"
- "Workspace-BackgroundUtility"
- "Workspace-ForegroundActive"
- "Workspace-ForegroundFocal"
- "Workspace-ForegroundSupportActive"
- "Workspace-ForegroundSupportFocal"
- "Workspace-ForegroundSupportSuspendable"
- "Workspace-ForegroundSupportUtility"
- "Workspace-ForegroundSuspendable"
- "Workspace-ForegroundUtility"
- "[%@] manager delegate %@ mutated settings: %@"
- "[%{public}@] Handing all actions to legacy delegate: %@"
- "[%{public}@] Pretending scene creation was successful, even though we got no response (<rdar://problem/62751231>). This does *not* mean there is a problem in FrontBoard, only that we are working around a bug in UIKit."
- "[%{public}@] Scene activity mode did change: %{public}@ (transient)."
- "[%{public}@] Scene activity mode did change: %{public}@."
- "[%{public}@] Scene assertion state did change: %{public}@."
- "[%{public}@] client invalidated"
- "[_bs_assert_object isKindOfClass:FBSWorkspaceSceneRequestOptionsClass]"
- "[_bs_assert_object isKindOfClass:FBWorkspaceConnectionsStateStoreClass]"
- "[_bs_assert_object isKindOfClass:FBWorkspaceEventDispatcherSourceClass]"
- "[_bs_assert_object isKindOfClass:FBWorkspaceRegistrationClass]"
- "[_bs_assert_object isKindOfClass:FBWorkspaceSceneRequestClass]"
- "[_bs_assert_object isKindOfClass:NSDictionaryClass]"
- "[_bs_assert_object isKindOfClass:RBSProcessIdentityClass]"
- "[_eventQueue isEmpty]"
- "_FBSystemAppSceneInfo"
- "_activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSource:withResult:"
- "_activation"
- "_adjustInitialSettings:"
- "_applyUpdate:postStateApplicator:completion:"
- "_authenticateAuditToken:entitlement:credentials:error:withResult:"
- "_baseTransformForSnapshotContext:rootContext:"
- "_bootstrapConfigured"
- "_callOutQueue_requestScene:"
- "_collectLayersToSnapshotFromScene:withSnapshotContext:rootContext:"
- "_deactivateForClientError:"
- "_delegateMonitorBehaviors"
- "_didCommitDEPRECATED2"
- "_didCreateDEPRECATED"
- "_didCreateSceneDEPRECATED"
- "_didReceiveActionsDEPRECATED"
- "_didSynchronizeLEGACY"
- "_didUpdateClientSettingsDEPRECATED"
- "_diffInspector"
- "_effectiveBehaviors"
- "_effectiveMonitorBehaviors"
- "_endSynchronizationBlock"
- "_enqueueObserverCallouts:forScene:eventName:preferInternal:sceneObserverBlock:sceneManagerObserverBlock:"
- "_evaluateEffectiveMonitorBehaviors"
- "_externalSceneIDs"
- "_fgSupportFocalAttributes"
- "_fgSupportNonFocalAttributes"
- "_fgSupportSuspendedAttributes"
- "_fgSupportUtilityAttributes"
- "_givenMonitorBehaviors"
- "_inTransaction == NO"
- "_initWithConnectionStore:preregisteredWorkspaces:"
- "_initWithIdentifier:legacy:"
- "_initWithIdentity:handle:executionContext:"
- "_initWithObserver:supportLegacy:"
- "_initWithProcessHandle:underlyingAssertion:"
- "_initWithSceneManager:sceneID:"
- "_initWithTargetQueue:"
- "_interestedClients"
- "_internalObserver"
- "_invalidated == __objc_yes"
- "_isSynchronizing"
- "_isSynchronizingSceneUpdates"
- "_lastUsedBuffer"
- "_lock_activeAssertionState"
- "_lock_outgoingEndpoint"
- "_machName"
- "_mainThread_dispatchHandshakeFromSource:toTarget:"
- "_mainThread_dispatchSceneRequestsFromSource:toTarget:"
- "_monitorsClientSettings"
- "_monitorsPairingStatus"
- "_monitorsSettings"
- "_noteProcessBootstrapped:withHandle:assertion:outgoingEndpoint:"
- "_nullEndpoint"
- "_observerToken"
- "_pairedExternalSceneIDs"
- "_pendingIdleEvents"
- "_queueWithSerialDispatchQueue:"
- "_queue_activityMode"
- "_queue_assertionState"
- "_queue_handleRegisterOrientationInterest:fromClient:"
- "_queue_handleRequestActiveOrientation:fromClient:"
- "_queue_inFlightLifecycleEvents"
- "_queue_updateInterest:forClient:withMessage:"
- "_reallyActivateApplication:requestID:options:serviceInstance:source:originalSource:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:"
- "_registerBlockForWorkspaceCreation:"
- "_registration"
- "_selfAssertRuntime != BSSettingFlagNo"
- "_sequenceNumber"
- "_setEffectiveMonitorBehaviors:"
- "_settings == newSettings"
- "_sharedWorkspaceIfExists"
- "_subtype"
- "_supportLegacy"
- "_supportsLegacy"
- "_targetQueue"
- "_underlyingAssertion"
- "_updateAllSceneStateIgnoringDelegate"
- "_updateAppliedDEPRECATED"
- "_updateCompletedDEPRECATED"
- "_updateExternalScenes:"
- "_updateExternalScenesAfterSync"
- "_updatePreparedDEPRECATED"
- "_updateScenePairingState:"
- "_updateSceneSettings:"
- "_updateSettingsAfterSync"
- "_watchdog:terminationRequestForViolatedProvision:error:"
- "_willDestroyDEPRECATED"
- "_willSynchronizeLEGACY"
- "_workspaceInitialized"
- "addObserverForName:object:queue:usingBlock:"
- "appendBool:counterpart:"
- "appendFlag:withName:"
- "applySettings"
- "arm64"
- "arm64_(%i)"
- "arm64_all"
- "arm64_any"
- "arm64e"
- "arm64v8"
- "assertOnQueue"
- "assertionAttributesForWorkspaceState:"
- "assertionState"
- "authenticateAuditToken:forEntitlement:withResult:"
- "authenticateAuditToken:withResult:"
- "authenticateClient:withResult:"
- "backingQueueIfExists"
- "beginSync"
- "behaviors"
- "c"
- "cannot note invalidation of %@ without a reference to the workspace"
- "cannot perform scene update without first beginning a transaction"
- "cannot update a deactivating scene"
- "clientProvider != nil"
- "com.apple.FrontBoard.workspace"
- "com.apple.frontboard.process.rb-interaction"
- "com.apple.frontboard.workspace-events.registration"
- "com.apple.frontboard.workspace-service.fallback"
- "contentStateDidChange-sceneObserver"
- "createCurrentProcess"
- "createProcessWithExecutionContext:"
- "createProcessWithHandle:"
- "createSceneFutureWithDefinition:completion:"
- "createSceneWithIdentifier:settings:initialClientSettings:clientProvider:transitionContext:"
- "createServiceQueue"
- "creating a sync-local client scene future is not supported"
- "dealloc is not allowed on FBWorkspaceDomain"
- "defaultIdentityForProcessIdentity:"
- "delegateReceivesSceneActions"
- "didDeactivate-sceneObserver"
- "didDestroyScene-sceneManager"
- "didInvalidate-sceneObserver"
- "didReceiveActions"
- "didReceiveActionsCompletion"
- "didUpdateClientSettings"
- "didUpdateClientSettingsCompletion"
- "didUpdateSettings"
- "endSync"
- "eventQueue"
- "eventQueueDidDrain:"
- "eventQueueDidUnlock:"
- "external"
- "fb_setWorkspaceAssertionState:"
- "fb_workspaceAssertionState"
- "flushAllEvents"
- "flushEvents:"
- "handleActions-cleanup"
- "handleActions-sceneObserver"
- "handleDidUpdateClientSettings"
- "i32@0:8@16@?24"
- "i32@0:8^{?=[8I]}16@?24"
- "i40@0:8^{?=[8I]}16@24@?32"
- "i56@0:8@16@24Q32o^@40@?48"
- "identifierForName:"
- "if we own the defaultShellMachName (%@) then %@ must be registered there"
- "initWithContextID:"
- "initWithDelegate:supportLegacy:"
- "initWithObserver:supportLegacy:"
- "initWithParentProcess:"
- "initWithScene:snapshotContext:"
- "initWithSceneID:"
- "initWithTargetIdentifier:options:completion:"
- "inspectDiff:withContext:"
- "intValue"
- "invalid identifier for workspace : %@"
- "isInternalObserver"
- "isPairedWithExternalSceneID:"
- "loadRBSLaunchIdentifiers"
- "mainDispatchQueue"
- "mainDisplay"
- "monitorsClientSettings"
- "monitorsPairingStatus"
- "monitorsSettings"
- "numberWithUnsignedChar:"
- "observePreferredSceneHostIdentifierWithBlock:"
- "observePreferredSceneHostIdentityWithBlock:"
- "pendingEvents"
- "performAsync:withHandoff:"
- "performCallouts"
- "preferredSceneHostIdentifier"
- "preferredSceneHostIdentity"
- "rbInteractionWorkloop"
- "registrationWithIdentifier:options:"
- "relinquishLock:"
- "removeAllObservers"
- "removeObjectAtIndex:"
- "requested attributes for FBWorkspaceAssertionState %@"
- "requesting a sync-local client scene is not supported"
- "scene && ![scene _isInTransaction]"
- "scene && (scene == [_allScenesByID objectForKey:[scene identifier]])"
- "scene == [_allScenesByID objectForKey:[scene identifier]]"
- "scene:deactivateAndInvalidate:withContext:block:"
- "scene:enqueueCalloutsToObserversWithEventName:block:"
- "scene:handleUpdate:withCompletion:"
- "scene:performCalloutsToObservers:"
- "sceneDeactivation"
- "sceneDidActivate"
- "sceneManager"
- "sceneManager:createDefaultTransitionContextForScene:"
- "sceneManager:didCommitUpdateForScene:transactionID:success:"
- "sceneManager:didCreateScene:withClient:"
- "sceneManager:scene:didReceiveActions:"
- "sceneManager:scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "sceneManager:updateForScene:appliedWithContext:"
- "sceneManager:updateForScene:completedWithContext:error:"
- "sceneManager:updateForScene:preparedWithContext:"
- "sceneManager:willDestroyScene:"
- "sceneManagerDidEndSceneUpdateSynchronization:"
- "sceneManagerWillBeginSceneUpdateSynchronization:"
- "sceneMonitor:pairingStatusDidChangeForExternalSceneIDs:"
- "sceneMonitor:sceneClientSettingsDidChangeWithDiff:transitionContext:"
- "sceneMonitor:sceneSettingsDidChangeWithDiff:previousSettings:"
- "sceneMonitor:sceneWasCreated:"
- "sceneMonitor:sceneWasDestroyed:"
- "sceneMutationCompletion"
- "sceneRemoval"
- "sceneUpdateCompleted"
- "sceneUpdatePrepared"
- "sceneUpdateSend"
- "sending workspace sync-local actions is not supported"
- "setBehaviors:"
- "setClientExtendedData:"
- "setExpirationDate:"
- "setFBSScene:"
- "setHasHandledSceneCreate:"
- "setHasSentFBSWorkspaceDelegateSceneCreate:"
- "setMonitorsClientSettings:"
- "setMonitorsPairingStatus:"
- "setMonitorsSettings:"
- "setPendingTransitionContext:"
- "setServiceQuality:"
- "setTargetDispatchingQueue:"
- "setTargetQueue:"
- "setWithSet:"
- "sliceWithType:"
- "startListener"
- "sync-local `createSceneFutureWithDefinition:` is not yet implemented"
- "sync-local `requestSceneWithOptions:` is not yet implemented"
- "sync-local `sendActions:` is not yet implemented"
- "targetQueue != ((void *)0)"
- "test_rejectAllSceneClients"
- "test_setRejectAllSceneClients:"
- "the scene must match our own mapped scene : %@ != %@"
- "this deprecated class only supports legacy scenes"
- "this object shouldn't go away"
- "tokenFromAuditTokenRef:"
- "trying to register a local scene for an already known identifier : %@ -> previous=%@"
- "unbalanced call to %s"
- "unionSet:"
- "update != nil"
- "updateComplete"
- "v16@?0@\"NSNotification\"8"
- "v16@?0@?<v@?>8"
- "v16@?0^v8"
- "v20@0:8C16"
- "v24@0:8@\"FBSceneEventQueue\"16"
- "v24@0:8@\"FBSceneLayerManager\"16"
- "v24@0:8@\"FBSceneManager\"16"
- "v24@0:8@?<v@?>16"
- "v24@?0@\"FBSceneObserver\"8@\"FBSceneManagerObserver\"16"
- "v24@?0@\"NSString\"8^B16"
- "v24@?0@8^B16"
- "v32@0:8@\"FBScene\"16@?<v@?@\"FBSceneObserver\"@\"FBSceneManagerObserver\">24"
- "v32@0:8@?16@24"
- "v32@0:8@?<v@?>16@\"NSObject<OS_xpc_object>\"24"
- "v32@?0@\"FBSSceneIdentity\"8@\"_FBSystemAppSceneInfo\"16^B24"
- "v36@0:8I16@20@28"
- "v40@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"FBScene\"16@\"NSSet\"24#32"
- "v40@0:8@\"FBScene\"16@\"NSString\"24@?<v@?@\"FBSceneObserver\">32"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"<FBSceneClient>\"32"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSceneUpdateContext\"32"
- "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"NSSet\"32"
- "v44@0:8@\"FBScene\"16B24@\"FBSSceneTransitionContext\"28@?<v@?>36"
- "v44@0:8@\"FBSceneManager\"16@\"FBScene\"24Q32B40"
- "v44@0:8@16@24Q32B40"
- "v44@0:8@16B24@28@?36"
- "v48@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSceneUpdateContext\"32@\"NSError\"40"
- "v56@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSSceneClientSettingsDiff\"32@\"FBSSceneClientSettings\"40@\"FBSSceneTransitionContext\"48"
- "v56@0:8@16@24@32@40@48"
- "willInvalidate/willDestroy"
- "willRemoveScene-sceneManager"
- "workspace assertion but no workspace assertion state"
- "workspace's process bootstrapped without a handle but still had a valid outgoing endpoint : process=%@ endpoint=%@"
- "workspace-endpoint-injection"
- "workspaceAssertionState"
- "{?=\"contentStateDidChange\"B\"didUpdateSettings\"B\"updatePreparedLEGACY\"B\"updateAppliedLEGACY\"B\"updateCompletedLEGACY\"B\"didUpdateClientSettings\"B\"clientSettingsUpdatedLEGACY\"B\"willActivate\"B\"didActivate\"B\"willDeactivateWithError\"B\"willDeactivateWithContext\"B\"didInvalidate\"B\"didInvalidateWithContext\"B\"clientDidConnect\"B\"handleActions\"B}"
- "{CGAffineTransform=dddddd}32@0:8@16@24"
- "\xc1"
- "\xf01"
- "\xf0\xf0\xa1"

```
