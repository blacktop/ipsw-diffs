## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/Versions/A/FrontBoard`

```diff

-943.3.9.0.0
-  __TEXT.__text: 0x850f0
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x47d4
+943.5.17.0.0
+  __TEXT.__text: 0x85a78
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x5658
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x9eda
-  __TEXT.__oslogstring: 0x5372
-  __TEXT.__gcc_except_tab: 0x11b8
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__cstring: 0x9f5a
+  __TEXT.__oslogstring: 0x551b
+  __TEXT.__gcc_except_tab: 0x1190
+  __TEXT.__unwind_info: 0x1d10
   __TEXT.__objc_classname: 0xfed
-  __TEXT.__objc_methname: 0xe7f4
+  __TEXT.__objc_methname: 0xe859
   __TEXT.__objc_methtype: 0x3514
-  __TEXT.__objc_stubs: 0xa900
-  __DATA_CONST.__got: 0x868
+  __TEXT.__objc_stubs: 0xa940
+  __DATA_CONST.__got: 0x870
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3358
+  __DATA_CONST.__objc_selrefs: 0x3400
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x668
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x2ad0
-  __AUTH_CONST.__cfstring: 0x8060
-  __AUTH_CONST.__objc_const: 0xc6e8
+  __AUTH_CONST.__cfstring: 0x8120
+  __AUTH_CONST.__objc_const: 0xad90
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x8b8
+  __DATA.__objc_ivar: 0x8c0
   __DATA.__data: 0x1920
   __DATA.__bss: 0x1a8
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A17A117D-0F23-3092-8C33-E2F9A2FC01A5
-  Functions: 2682
-  Symbols:   6761
-  CStrings:  5535
+  UUID: F5E5F6EA-FFC0-3AB2-9880-FF9ADE31C716
+  Functions: 2819
+  Symbols:   6807
+  CStrings:  5557
 
Symbols:
+ +[FBApplicationDataStoreRepositoryServer sharedInstance].cold.1
+ +[FBApplicationProcessWatchdogPolicy defaultPolicy].cold.1
+ +[FBInterfaceOrientationService sharedInstance].cold.1
+ +[FBLocalSynchronousSceneClientProvider sharedInstance].cold.1
+ +[FBMainDisplayLayoutPublisher sharedInstance].cold.1
+ +[FBPreferences sharedInstance].cold.1
+ +[FBProcess calloutQueue].cold.1
+ +[FBProcess rbInteractionWorkloop].cold.1
+ +[FBSceneManager sharedInstance].cold.1
+ +[FBServiceClientAuthenticator sharedForegroundUIAppClientAuthenticator].cold.1
+ +[FBServiceClientAuthenticator sharedSystemClientAuthenticator].cold.1
+ +[FBServiceClientAuthenticator sharedUIAppClientAuthenticator].cold.1
+ +[FBSystemAppProxyServiceServer sharedInstance].cold.1
+ +[FBWorkspaceConnectionsStateStore hasSandboxAccessForIdentifier:]
+ +[FBWorkspaceConnectionsStateStore hasSandboxAccessForIdentifier:].cold.1
+ +[FBWorkspaceConnectionsStateStore hasSandboxAccessForIdentifier:].cold.2
+ +[FBWorkspaceConnectionsStateStore hasSandboxAccessForIdentifier:].cold.3
+ +[FBWorkspaceConnectionsStateStore identifierForName:]
+ +[FBWorkspaceDomain sharedInstance].cold.1
+ +[FBWorkspaceEventDispatcher sharedInstance].cold.1
+ +[FBWorkspaceEventQueue sharedInstance].cold.1
+ +[_FBDefaultFencingProvider sharedInstance].cold.1
+ -[FBPlistApplicationDataStoreRepository _isEligibleForSaving:].cold.1
+ -[FBProcess _bootstrapAndExec].cold.3
+ -[FBProcess _killForReason:andReport:withDescription:completion:].cold.3
+ -[FBProcess _launchDidComplete:finalizeBlock:].cold.1
+ -[FBProcess _launchDidComplete:finalizeBlock:].cold.2
+ -[FBProcess _launchDidComplete:finalizeBlock:].cold.3
+ -[FBProcess _lock_consumeLock_executeTerminationRequest].cold.3
+ -[FBProcess _lock_consumeLock_performGracefulKill].cold.2
+ -[FBProcess _notePendingExitForReason:].cold.1
+ -[FBProcess _processDidExitWithContext:].cold.2
+ -[FBProcess _terminateWithRequest:completion:].cold.3
+ -[FBProcess _terminateWithRequest:completion:].cold.4
+ -[FBProcess _terminateWithRequest:completion:].cold.5
+ -[FBProcess _updateStateWithBlock:].cold.1
+ -[FBProcess _updateStateWithBlock:].cold.2
+ -[FBProcess _updateStateWithBlock:].cold.3
+ -[FBProcess _watchdogReportType].cold.1
+ -[FBScene _activateWithTransitionContext:error:].cold.11
+ -[FBScene _activateWithTransitionContext:error:].cold.12
+ -[FBScene _activateWithTransitionContext:error:].cold.13
+ -[FBScene _adjustInitialSettings:].cold.2
+ -[FBScene _applySettingsUpdateWithCompletion:].cold.13
+ -[FBScene _applySettingsUpdateWithCompletion:].cold.14
+ -[FBScene _beginUpdate].cold.4
+ -[FBScene _deactivateForClientError:].cold.2
+ -[FBScene initWithDefiniton:remnant:settings:initialClientSettings:clientProvider:workspace:].cold.6
+ -[FBSceneLayerManager _initWithScene:].cold.2
+ -[FBSceneObserver scene:didReceiveActions:].cold.1
+ -[FBSceneObserver scene:willUpdateSettings:].cold.1
+ -[FBSceneWorkspace _createSceneWithDefinition:settings:initialClientSettings:transitionContext:fromRemnant:usingClientProvider:completion:].cold.26
+ -[FBSceneWorkspace _initWithIdentifier:legacy:].cold.6
+ -[FBSceneWorkspace scene:didUpdateClientSettings:].cold.3
+ -[FBSqliteApplicationDataStoreRepository _inAlternateSystemApp].cold.1
+ -[FBSqliteApplicationDataStoreRepository _isEligibleForSaving:].cold.1
+ -[FBSystemService _isAllowListedLaunchSuspendedApp:].cold.1
+ -[FBWorkspace _enableLegacyRequests:].cold.2
+ -[FBWorkspace _terminateGracefully:withTransitionContext:].cold.2
+ -[FBWorkspaceConnection _workspaceScene:enqueueConnectBlock:].cold.2
+ -[FBWorkspaceConnection workspaceLock_enqueueConnectBlock:].cold.2
+ -[FBWorkspaceDomain _init].cold.4
+ -[FBWorkspaceDomain reconnectShmemIdentifier]
+ -[FBWorkspaceScene _enqueueSceneCreateCompletionBlock:].cold.2
+ FBFrameworkBundle.cold.1
+ FBLogProcess.cold.1
+ FBLogProcessScene.cold.1
+ FBLogProcessWorkspace.cold.1
+ FBLogScene.cold.1
+ FBLogSceneMutation.cold.1
+ FBSystemAppBundleID.cold.1
+ FBWorkspaceLogCommon.cold.1
+ FBWorkspaceLogScene.cold.1
+ FBWorkspaceLogSceneDeactivation.cold.1
+ FBWorkspaceLogSceneHost.cold.1
+ FBWorkspaceLogSceneLayout.cold.1
+ FBWorkspaceLogSnapshot.cold.1
+ FBWorkspaceLogTransaction.cold.1
+ FBWorkspaceLogTransactionVerbose.cold.1
+ GCC_except_table114
+ GCC_except_table142
+ GCC_except_table155
+ GCC_except_table23
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table80
+ GCC_except_table83
+ OBJC_IVAR_$_FBWorkspaceDomain._reconnectShmemIdentifier
+ OBJC_IVAR_$_FBWorkspaceDomain._reconnectableWorkspaces
+ _BSLogAddStateCaptureBlockForUserRequestsOnlyWithTitle
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _SANDBOX_CHECK_NO_REPORT
+ __50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.307
+ __54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_2.279.cold.1
+ __54-[FBSceneWorkspace scene:handleUpdate:withCompletion:]_block_invoke_2.290.cold.2
+ __54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.79
+ __54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.123
+ __54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.125
+ __56-[FBProcess _lock_consumeLock_executeTerminationRequest]_block_invoke.276
+ __59-[FBWorkspaceOutgoingConnection workspaceLock_setEndpoint:]_block_invoke_2.cold.2
+ __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.213
+ __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.213.cold.1
+ __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.213.cold.2
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.335.cold.1
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.335.cold.2
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.335.cold.3
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.335.cold.4
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.335.cold.5
+ __79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.112
+ __79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.113
+ __88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.103
+ _objc_msgSend$hasSandboxAccessForIdentifier:
+ _objc_msgSend$identifierForName:
+ _sandbox_check
- -[FBScene _verifyIntegrityOfExtensionsInSettings:].cold.1
- -[FBScene _verifyIntegrityOfExtensionsInSettings:].cold.2
- -[FBSceneWorkspace _beginSynchronizationBlock].cold.1
- -[FBWorkspace _setIncomingConnection:].cold.1
- -[FBWorkspaceDomain endpointInjectorTargetingProcess:].cold.1
- -[FBWorkspaceDomain endpointInjectorTargetingProcess:].cold.2
- -[FBWorkspaceDomain machName]
- GCC_except_table110
- GCC_except_table137
- GCC_except_table154
- GCC_except_table26
- GCC_except_table40
- GCC_except_table42
- GCC_except_table44
- GCC_except_table45
- GCC_except_table56
- GCC_except_table57
- GCC_except_table63
- GCC_except_table65
- GCC_except_table79
- GCC_except_table82
- _BSLogAddStateCaptureBlockWithTitle
- __50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.310
- __54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.75
- __54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.119
- __54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.121
- __56-[FBProcess _lock_consumeLock_executeTerminationRequest]_block_invoke.279
- __57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.cold.1
- __57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.cold.2
- __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.206
- __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.206.cold.1
- __63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.206.cold.2
- __79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.108
- __79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.109
CStrings:
+ "%{public}@ Workspace assertion invalidated: %{public}@"
+ "%{public}@ Workspace assertion will expire."
+ "/\v"
+ "FBWorkspaceConnectionsStateStore: %@ denied for %@"
+ "FBWorkspaceConnectionsStateStore: error in sandbox_check %@ for %@ : errno=%i (%s)"
+ "FBWorkspaceDomain:%p no access to defaultShmemIdentifier \"%@\" - disabling reconnection support"
+ "FBWorkspaceDomain:%p unrecognized ReconnectShmemIdentifier \"%@\" - disabling reconnection support"
+ "ReconnectShmemIdentifier"
+ "Unable to establish XPC connection."
+ "Value for '%@' was unexpectedly nil. Expected %@."
+ "_reconnectShmemIdentifier"
+ "_reconnectableWorkspaces"
+ "hasSandboxAccessForIdentifier:"
+ "identifierForName:"
+ "improper length identifier : \"%@\""
+ "ipc-posix-shm-read-data"
+ "ipc-posix-shm-write-create"
+ "ipc-posix-shm-write-unlink"
+ "reconnectShmem"
+ "shmPath"
- "/\t"
- "[_bs_assert_object isKindOfClass:FBWorkspaceConnectionsStateClass]"
- "identifier is too long"

```
