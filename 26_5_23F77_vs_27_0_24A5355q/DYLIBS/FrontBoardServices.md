## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-1000.4.11.0.0
-  __TEXT.__text: 0xa2544
-  __TEXT.__auth_stubs: 0x10c0
+1145.0.0.0.0
+  __TEXT.__text: 0x989f0
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x8618
+  __TEXT.__objc_methlist: 0x8638
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xcbfd
-  __TEXT.__oslogstring: 0x3d7d
-  __TEXT.__gcc_except_tab: 0x22c4
-  __TEXT.__unwind_info: 0x2eb8
-  __TEXT.__objc_classname: 0x145f
-  __TEXT.__objc_methname: 0x105e4
-  __TEXT.__objc_methtype: 0x35a6
-  __TEXT.__objc_stubs: 0xb220
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x3030
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __TEXT.__cstring: 0xc0cb
+  __TEXT.__oslogstring: 0x3b78
+  __TEXT.__gcc_except_tab: 0x1e30
+  __TEXT.__unwind_info: 0x2b10
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3110
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3de8
+  __DATA_CONST.__objc_selrefs: 0x3d48
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0xa3e0
-  __AUTH_CONST.__objc_const: 0x10330
+  __DATA_CONST.__got: 0x738
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0xa280
+  __AUTH_CONST.__objc_const: 0x100b8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x870
   __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0xa60
-  __DATA.__data: 0x19b4
-  __DATA.__bss: 0x3a8
-  __DATA_DIRTY.__objc_data: 0x2080
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA.__objc_ivar: 0xa58
+  __DATA.__data: 0x1a14
+  __DATA.__bss: 0x2f0
+  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D784C2AB-3079-3F2F-AE2E-1B12852F9A9B
-  Functions: 4450
-  Symbols:   14147
-  CStrings:  6940
+  UUID: 82FFE4CF-B965-3567-908A-2CB84DC4EC8D
+  Functions: 4373
+  Symbols:   13882
+  CStrings:  3237
 
Symbols:
+ +[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState]
+ +[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState].cold.1
+ +[FBSActiveInterfaceOrientationState supportsBSXPCSecureCoding]
+ +[FBSActiveInterfaceOrientationStateUpdate supportsBSXPCSecureCoding]
+ +[FBSDisplayPixelDensity _densityForPixelsPerInch:]
+ +[FBSDisplayPixelDensity supportsSecureCoding]
+ +[FBSSceneClientSettings _extensionsAreLocal]
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:]
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.1
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.2
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.3
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.4
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.5
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.6
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.7
+ +[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:].cold.8
+ +[FBSSceneIdentityToken tokenWithHostVPID:viewServiceSessionIdentifier:]
+ +[FBSSceneIdentityToken tokenWithHostVPID:viewServiceSessionIdentifier:].cold.1
+ +[FBSSceneIdentityToken tokenWithHostVPID:viewServiceSessionIdentifier:].cold.2
+ +[FBSSceneIdentityToken tokenWithHostVPID:viewServiceSessionIdentifier:].cold.3
+ +[FBSSceneSettingsCore configureSetting:]
+ +[FBSSettings _extensionsAreLocal]
+ -[FBSActiveInterfaceOrientationObserver .cxx_destruct]
+ -[FBSActiveInterfaceOrientationObserver _activateWithStateUpdateHandler:registerInterest:]
+ -[FBSActiveInterfaceOrientationObserver _handleActiveInterfaceOrientationStateUpdate:]
+ -[FBSActiveInterfaceOrientationObserver _initWithClient:callbackQueue:]
+ -[FBSActiveInterfaceOrientationObserver _legacy_activeInterfaceOrientationStateUpdateWithCompletion:]
+ -[FBSActiveInterfaceOrientationObserver _legacy_updateStateUpdateHandler:]
+ -[FBSActiveInterfaceOrientationObserver _lock_resolveAndStoreFreshestUpdate:forced:]
+ -[FBSActiveInterfaceOrientationObserver _resolveAndStoreFreshestUpdate:forced:]
+ -[FBSActiveInterfaceOrientationObserver _setUpdateHandler:]
+ -[FBSActiveInterfaceOrientationObserver activateWithStateUpdateHandler:]
+ -[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationStateWithCompletion:]
+ -[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState]
+ -[FBSActiveInterfaceOrientationObserver client:handleActiveInterfaceOrientationStateUpdate:]
+ -[FBSActiveInterfaceOrientationObserver dealloc]
+ -[FBSActiveInterfaceOrientationObserver dealloc].cold.1
+ -[FBSActiveInterfaceOrientationObserver handleActiveInterfaceOrientationStateResetForClient:]
+ -[FBSActiveInterfaceOrientationObserver init]
+ -[FBSActiveInterfaceOrientationObserver invalidate]
+ -[FBSActiveInterfaceOrientationState .cxx_destruct]
+ -[FBSActiveInterfaceOrientationState _initWithDisplayIdentity:interfaceOrientation:]
+ -[FBSActiveInterfaceOrientationState _initWithDisplayIdentity:interfaceOrientation:].cold.1
+ -[FBSActiveInterfaceOrientationState appendDescriptionToStream:]
+ -[FBSActiveInterfaceOrientationState copyWithZone:]
+ -[FBSActiveInterfaceOrientationState description]
+ -[FBSActiveInterfaceOrientationState displayIdentity]
+ -[FBSActiveInterfaceOrientationState encodeWithBSXPCCoder:]
+ -[FBSActiveInterfaceOrientationState hash]
+ -[FBSActiveInterfaceOrientationState initWithBSXPCCoder:]
+ -[FBSActiveInterfaceOrientationState interfaceOrientation]
+ -[FBSActiveInterfaceOrientationState isEqual:]
+ -[FBSActiveInterfaceOrientationStateUpdate .cxx_destruct]
+ -[FBSActiveInterfaceOrientationStateUpdate _initWithState:animationDuration:rotationDirection:sequenceNumber:]
+ -[FBSActiveInterfaceOrientationStateUpdate animationDuration]
+ -[FBSActiveInterfaceOrientationStateUpdate appendDescriptionToStream:]
+ -[FBSActiveInterfaceOrientationStateUpdate asLegacyOrientationUpdate]
+ -[FBSActiveInterfaceOrientationStateUpdate copyWithZone:]
+ -[FBSActiveInterfaceOrientationStateUpdate description]
+ -[FBSActiveInterfaceOrientationStateUpdate encodeWithBSXPCCoder:]
+ -[FBSActiveInterfaceOrientationStateUpdate hash]
+ -[FBSActiveInterfaceOrientationStateUpdate initWithBSXPCCoder:]
+ -[FBSActiveInterfaceOrientationStateUpdate isEqual:]
+ -[FBSActiveInterfaceOrientationStateUpdate rotationDirection]
+ -[FBSActiveInterfaceOrientationStateUpdate sequenceNumber]
+ -[FBSActiveInterfaceOrientationStateUpdate state]
+ -[FBSApplicationDataStoreRepositoryClient _clearAllPrefetchedObjectsForApplication:]
+ -[FBSApplicationDataStoreRepositoryClient _setChangeInFlight:forAllPrefetchedKeysInApplication:]
+ -[FBSComponentScene scene].cold.1
+ -[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:pixelDensity:latency:originatingConfiguration:validityCheck:]
+ -[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:pixelDensity:latency:originatingConfiguration:validityCheck:].cold.1
+ -[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:pixelDensity:latency:originatingConfiguration:validityCheck:].cold.2
+ -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:]
+ -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:].cold.1
+ -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:].cold.2
+ -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:].cold.3
+ -[FBSDisplayConfiguration pixelDensity]
+ -[FBSDisplayConfigurationBuilder setPixelDensity:]
+ -[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:alwaysConnected:root:]
+ -[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:alwaysConnected:root:].cold.1
+ -[FBSDisplayIdentity isAlwaysConnected]
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:]
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.1
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.2
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.3
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.4
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.5
+ -[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:].cold.6
+ -[FBSDisplayMonitor _lock_alwaysConnectedConfigurations]
+ -[FBSDisplayMonitor alwaysConnectedIdentities]
+ -[FBSDisplayPixelDensity appendDescriptionToStream:]
+ -[FBSDisplayPixelDensity copyWithZone:]
+ -[FBSDisplayPixelDensity description]
+ -[FBSDisplayPixelDensity encodeWithCoder:]
+ -[FBSDisplayPixelDensity encodeWithXPCDictionary:]
+ -[FBSDisplayPixelDensity horizontalPixelsPerInch]
+ -[FBSDisplayPixelDensity initWithCoder:]
+ -[FBSDisplayPixelDensity initWithHorizontalPixelsPerInch:verticalPixelsPerInch:]
+ -[FBSDisplayPixelDensity initWithXPCDictionary:]
+ -[FBSDisplayPixelDensity isEqual:]
+ -[FBSDisplayPixelDensity supportsBSXPCSecureCoding]
+ -[FBSDisplayPixelDensity verticalPixelsPerInch]
+ -[FBSDisplaySource _initWithDisplay:isMainDisplay:alwaysConnected:triggers:monitor:]
+ -[FBSDisplaySource _initWithDisplay:isMainDisplay:alwaysConnected:triggers:monitor:].cold.1
+ -[FBSDisplaySource _initWithDisplay:isMainDisplay:alwaysConnected:triggers:monitor:].cold.2
+ -[FBSDisplaySource _initWithDisplay:isMainDisplay:alwaysConnected:triggers:monitor:].cold.3
+ -[FBSDisplaySource isAlwaysConnected]
+ -[FBSOrientationObserver _initWithObserver:]
+ -[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]
+ -[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:].cold.1
+ -[FBSOrientationObserverClient _isInterested]
+ -[FBSOrientationObserverClient _server:registerInterest:]
+ -[FBSOrientationObserverClient activeInterfaceOrientationStateDidChange:]
+ -[FBSOrientationObserverClient activeInterfaceOrientationStateUpdateWithCompletion:]
+ -[FBSOrientationObserverClient activeInterfaceOrientationState]
+ -[FBSOrientationObserverClient isActive]
+ -[FBSOrientationObserverClient registerInterest]
+ -[FBSOrientationObserverClient unregisterInterest]
+ -[FBSScene _callOutQueue_addExtensions:removeExtensions:fromHost:]
+ -[FBSScene addLocalExtensions:]
+ -[FBSScene removeLocalExtensions:]
+ -[FBSSceneUpdate addUpdateCompletion:]
+ -[FBSSceneUpdate addUpdateCompletion:].cold.1
+ -[FBSSceneUpdate dealloc]
+ -[FBSSceneUpdate dealloc].cold.1
+ -[FBSSceneUpdate init]
+ -[FBSSceneUpdate takeUpdateCompletions]
+ -[FBSSceneUpdate updateCompletionsCount]
+ -[FBSSetting _finishInitializing].cold.1
+ GCC_except_table110
+ GCC_except_table69
+ OBJC_IVAR_$_FBSSceneUpdate._updateCompletions
+ _BSGetVersionedPID
+ _FBSCADisplayAlwaysConnected
+ _FBSCADisplayToDisplayTypes
+ _FBSCADisplayToDisplayTypes.cold.1
+ _FBSObjCTypeIsActuallyBOOL
+ _NSStringFromBSVersionedPID
+ _OBJC_CLASS_$_AITransactionLog$loadHelper_x8
+ _OBJC_CLASS_$_BSDescriptionStream
+ _OBJC_CLASS_$_BSServiceInitiatingConnection
+ _OBJC_CLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_CLASS_$_BSServiceListenerConnection
+ _OBJC_CLASS_$_FBSActiveInterfaceOrientationObserver
+ _OBJC_CLASS_$_FBSActiveInterfaceOrientationState
+ _OBJC_CLASS_$_FBSActiveInterfaceOrientationStateUpdate
+ _OBJC_CLASS_$_FBSDisplayPixelDensity
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationObserver._callbackQueue
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationObserver._client
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationObserver._lock
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationObserver._lock_freshestUpdate
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationObserver._lock_updateHandler
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationState._displayIdentity
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationState._interfaceOrientation
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationStateUpdate._animationDuration
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationStateUpdate._rotationDirection
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationStateUpdate._sequenceNumber
+ _OBJC_IVAR_$_FBSActiveInterfaceOrientationStateUpdate._state
+ _OBJC_IVAR_$_FBSApplicationInfo._entitlements
+ _OBJC_IVAR_$_FBSDisplayConfiguration._pixelDensity
+ _OBJC_IVAR_$_FBSDisplayConfigurationBuilder._lock_pixelDensity
+ _OBJC_IVAR_$_FBSDisplayConfigurationBuilder._lock_pixelDensitySet
+ _OBJC_IVAR_$_FBSDisplayIdentity._alwaysConnected
+ _OBJC_IVAR_$_FBSDisplayMonitor._lock_alwaysConnectedSources
+ _OBJC_IVAR_$_FBSDisplayPixelDensity._horizontalPixelsPerInch
+ _OBJC_IVAR_$_FBSDisplayPixelDensity._verticalPixelsPerInch
+ _OBJC_IVAR_$_FBSDisplaySource._isMainDisplay
+ _OBJC_IVAR_$_FBSOrientationObserver._handler
+ _OBJC_IVAR_$_FBSOrientationObserver._observer
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_delegate
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_isActive
+ _OBJC_IVAR_$_FBSOrientationObserverClient._lock_isInterested
+ _OBJC_IVAR_$_FBSSceneObserver._componentRespondsToInvalidate
+ _OBJC_IVAR_$_FBSSceneObserver._componentRespondsToPrivateActions
+ _OBJC_IVAR_$_FBSSceneUpdate._haveCompletionsBeenTaken
+ _OBJC_IVAR_$_FBSSceneUpdate._lock
+ _OBJC_METACLASS_$_FBSActiveInterfaceOrientationObserver
+ _OBJC_METACLASS_$_FBSActiveInterfaceOrientationState
+ _OBJC_METACLASS_$_FBSActiveInterfaceOrientationStateUpdate
+ _OBJC_METACLASS_$_FBSDisplayPixelDensity
+ __OBJC_$_CLASS_METHODS_FBSActiveInterfaceOrientationObserver
+ __OBJC_$_CLASS_METHODS_FBSActiveInterfaceOrientationState
+ __OBJC_$_CLASS_METHODS_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_$_CLASS_METHODS_FBSDisplayPixelDensity
+ __OBJC_$_CLASS_PROP_LIST_FBSDisplayPixelDensity
+ __OBJC_$_INSTANCE_METHODS_FBSActiveInterfaceOrientationObserver
+ __OBJC_$_INSTANCE_METHODS_FBSActiveInterfaceOrientationState
+ __OBJC_$_INSTANCE_METHODS_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_$_INSTANCE_METHODS_FBSDisplayPixelDensity
+ __OBJC_$_INSTANCE_VARIABLES_FBSActiveInterfaceOrientationObserver
+ __OBJC_$_INSTANCE_VARIABLES_FBSActiveInterfaceOrientationState
+ __OBJC_$_INSTANCE_VARIABLES_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_$_INSTANCE_VARIABLES_FBSDisplayPixelDensity
+ __OBJC_$_PROP_LIST_FBSActiveInterfaceOrientationObserver
+ __OBJC_$_PROP_LIST_FBSActiveInterfaceOrientationState
+ __OBJC_$_PROP_LIST_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_$_PROP_LIST_FBSApplicationPlaceholderProgress.189
+ __OBJC_$_PROP_LIST_FBSDisplayLayoutElement.183
+ __OBJC_$_PROP_LIST_FBSDisplayPixelDensity
+ __OBJC_$_PROP_LIST_FBSProcess.115
+ __OBJC_$_PROP_LIST_FBSSceneClientSettings.74
+ __OBJC_$_PROP_LIST_FBSSceneSettings.187
+ __OBJC_$_PROP_LIST_FBSSceneTransitionContext.170
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_REFS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_REFS_FBSOrientationServiceClientInterface
+ __OBJC_$_PROTOCOL_REFS_FBSOrientationServiceServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_FBSActiveInterfaceOrientationObserver
+ __OBJC_CLASS_PROTOCOLS_$_FBSActiveInterfaceOrientationState
+ __OBJC_CLASS_PROTOCOLS_$_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_CLASS_PROTOCOLS_$_FBSDisplayPixelDensity
+ __OBJC_CLASS_RO_$_FBSActiveInterfaceOrientationObserver
+ __OBJC_CLASS_RO_$_FBSActiveInterfaceOrientationState
+ __OBJC_CLASS_RO_$_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_CLASS_RO_$_FBSDisplayPixelDensity
+ __OBJC_LABEL_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_METACLASS_RO_$_FBSActiveInterfaceOrientationObserver
+ __OBJC_METACLASS_RO_$_FBSActiveInterfaceOrientationState
+ __OBJC_METACLASS_RO_$_FBSActiveInterfaceOrientationStateUpdate
+ __OBJC_METACLASS_RO_$_FBSDisplayPixelDensity
+ __OBJC_PROTOCOL_$_BSDescriptionStreaming
+ ___101-[FBSActiveInterfaceOrientationObserver _legacy_activeInterfaceOrientationStateUpdateWithCompletion:]_block_invoke
+ ___101-[FBSActiveInterfaceOrientationObserver _legacy_activeInterfaceOrientationStateUpdateWithCompletion:]_block_invoke_2
+ ___30-[FBSApplicationLibrary _load]_block_invoke.182
+ ___31-[FBSScene addLocalExtensions:]_block_invoke
+ ___34-[FBSDisplayPixelDensity isEqual:]_block_invoke
+ ___34-[FBSDisplayPixelDensity isEqual:]_block_invoke_2
+ ___34-[FBSScene removeLocalExtensions:]_block_invoke
+ ___36-[FBSWorkspace _registerSourcePeer:]_block_invoke.190
+ ___37-[FBSOrientationObserver setHandler:]_block_invoke
+ ___39-[FBSDisplaySource _lock_noteConnected]_block_invoke.151
+ ___46-[FBSActiveInterfaceOrientationState isEqual:]_block_invoke
+ ___46-[FBSActiveInterfaceOrientationState isEqual:]_block_invoke_2
+ ___46-[FBSDisplayMonitor alwaysConnectedIdentities]_block_invoke
+ ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.31
+ ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.33
+ ___48-[FBSApplicationLibrary applicationsDidInstall:]_block_invoke.240
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.155
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.162
+ ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.165
+ ___52-[FBSActiveInterfaceOrientationStateUpdate isEqual:]_block_invoke
+ ___52-[FBSActiveInterfaceOrientationStateUpdate isEqual:]_block_invoke_2
+ ___52-[FBSActiveInterfaceOrientationStateUpdate isEqual:]_block_invoke_3
+ ___52-[FBSActiveInterfaceOrientationStateUpdate isEqual:]_block_invoke_4
+ ___52-[FBSDisplayPixelDensity appendDescriptionToStream:]_block_invoke
+ ___57-[FBSOrientationObserverClient _server:registerInterest:]_block_invoke
+ ___62-[FBSDisplaySource _lock_noteUpdatedForTransformInvalidation:]_block_invoke.164
+ ___66-[FBSScene _callOutQueue_addExtensions:removeExtensions:fromHost:]_block_invoke
+ ___66-[FBSScene _callOutQueue_addExtensions:removeExtensions:fromHost:]_block_invoke.115
+ ___66-[FBSScene _callOutQueue_addExtensions:removeExtensions:fromHost:]_block_invoke.cold.1
+ ___70-[FBSWorkspaceScenesClient initWithPeer:queue:calloutQueue:workspace:]_block_invoke
+ ___70-[FBSWorkspaceScenesClient initWithPeer:queue:calloutQueue:workspace:]_block_invoke_2
+ ___72+[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState]_block_invoke
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke.153
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke.153.cold.1
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke.154
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke.159
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke_2
+ ___74-[FBSWorkspaceScenesClient initWithEndpoint:queue:calloutQueue:workspace:]_block_invoke_3
+ ___76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.144
+ ___84-[FBSOrientationObserverClient activeInterfaceOrientationStateUpdateWithCompletion:]_block_invoke
+ ___84-[FBSOrientationObserverClient activeInterfaceOrientationStateUpdateWithCompletion:]_block_invoke.cold.1
+ ___87-[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationStateWithCompletion:]_block_invoke
+ ___87-[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationStateWithCompletion:]_block_invoke_2
+ ___90-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]_block_invoke
+ ___90-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]_block_invoke_2
+ ___90-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]_block_invoke_3
+ ___90-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]_block_invoke_4
+ ___90-[FBSOrientationObserverClient _initWithEndpoint:connectionContext:calloutQueue:delegate:]_block_invoke_5
+ ___92-[FBSActiveInterfaceOrientationObserver client:handleActiveInterfaceOrientationStateUpdate:]_block_invoke
+ ___93-[FBSActiveInterfaceOrientationObserver handleActiveInterfaceOrientationStateResetForClient:]_block_invoke
+ ___94-[FBSApplicationLibrary _handleApplicationStateDidChange:notifyForUpdateInsteadOfReplacement:]_block_invoke.241
+ ____ingestPropertiesFromSettingsSubclass_block_invoke.398
+ ____realizeSettingsExtension_block_invoke.258
+ ____realizeSettingsExtension_block_invoke.277
+ ____realizeSettingsExtension_block_invoke.284
+ ____realizeSettingsExtension_block_invoke.284.cold.1
+ ____realizeSettingsExtension_block_invoke.284.cold.2
+ ____realizeSettingsExtension_block_invoke.297
+ ____realizeSettingsExtension_block_invoke_2.260
+ ____realizeSettingsExtension_block_invoke_2.280
+ ____realizeSettingsExtension_block_invoke_2.299
+ ____realizeSettingsExtension_block_invoke_3.262
+ ____realizeSettingsExtension_block_invoke_3.282
+ ____realizeSettingsExtension_block_invoke_3.301
+ ____realizeSettingsExtension_block_invoke_4.303
+ ____realizeSettingsExtension_block_invoke_5.305
+ ____realizeSettingsExtension_block_invoke_6.307
+ ____realizeSettingsExtension_block_invoke_7.309
+ ___block_descriptor_32_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8l
+ ___block_descriptor_32_e53_"FBSDisplayIdentity"16?0"FBSDisplayConfiguration"8l
+ ___block_descriptor_40_e8_32bs_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8ls32l8
+ ___block_descriptor_40_e8_32bs_e50_v16?0"FBSActiveInterfaceOrientationStateUpdate"8ls32l8
+ ___block_descriptor_40_e8_32s_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_40_e8_32s_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_40_e8_32w_e62_v24?0"FBSActiveInterfaceOrientationStateUpdate"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e50_v16?0"FBSActiveInterfaceOrientationStateUpdate"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e62_v24?0"FBSActiveInterfaceOrientationStateUpdate"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8u48l8
+ ___block_descriptor_56_e8_32s40s48s_e48_v16?0"<BSServiceConnectionCommonConfiguring>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8u48l8s40l8
+ ___block_literal_global.148
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.180
+ ___block_literal_global.218
+ ___block_literal_global.224
+ ___block_literal_global.294
+ ___block_literal_global.40
+ ___block_literal_global.59
+ __initWithDisplay:isMainDisplay:alwaysConnected:triggers:monitor:.__instanceCounter
+ _activeInterfaceOrientationState.client
+ _activeInterfaceOrientationState.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_activateWithStateUpdateHandler:registerInterest:
+ _objc_msgSend$_callOutQueue_addExtensions:removeExtensions:fromHost:
+ _objc_msgSend$_clearAllPrefetchedObjectsForApplication:
+ _objc_msgSend$_densityForPixelsPerInch:
+ _objc_msgSend$_extensionsAreLocal
+ _objc_msgSend$_handleActiveInterfaceOrientationStateUpdate:
+ _objc_msgSend$_initWithDisplayIdentity:interfaceOrientation:
+ _objc_msgSend$_initWithDisplays:mainDisplay:bookendObserver:transformer:
+ _objc_msgSend$_initWithEndpoint:connectionContext:calloutQueue:delegate:
+ _objc_msgSend$_initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:pixelDensity:latency:originatingConfiguration:validityCheck:
+ _objc_msgSend$_initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:
+ _objc_msgSend$_initWithObserver:
+ _objc_msgSend$_initWithState:animationDuration:rotationDirection:sequenceNumber:
+ _objc_msgSend$_initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:alwaysConnected:root:
+ _objc_msgSend$_legacy_activeInterfaceOrientationStateUpdateWithCompletion:
+ _objc_msgSend$_legacy_updateStateUpdateHandler:
+ _objc_msgSend$_lock_alwaysConnectedConfigurations
+ _objc_msgSend$_lock_resolveAndStoreFreshestUpdate:forced:
+ _objc_msgSend$_removeSceneExtension:
+ _objc_msgSend$_resolveAndStoreFreshestUpdate:forced:
+ _objc_msgSend$_server:registerInterest:
+ _objc_msgSend$_setChangeInFlight:forAllPrefetchedKeysInApplication:
+ _objc_msgSend$_setUpdateHandler:
+ _objc_msgSend$activeInterfaceOrientationState
+ _objc_msgSend$activeInterfaceOrientationStateDidChange:
+ _objc_msgSend$activeInterfaceOrientationStateUpdate
+ _objc_msgSend$activeInterfaceOrientationStateUpdateWithCompletion:
+ _objc_msgSend$animationDuration
+ _objc_msgSend$appendProem:block:
+ _objc_msgSend$appendUnsignedInteger:
+ _objc_msgSend$appendUnsignedInteger:counterpart:
+ _objc_msgSend$asLegacyOrientationUpdate
+ _objc_msgSend$bs_CGSizeValue
+ _objc_msgSend$bs_valueWithCGSize:
+ _objc_msgSend$client:handleActiveInterfaceOrientationStateUpdate:
+ _objc_msgSend$configure:
+ _objc_msgSend$decodeCGSizeForKey:
+ _objc_msgSend$descriptionForRootObject:
+ _objc_msgSend$displayIdentity
+ _objc_msgSend$encodeCGSize:forKey:
+ _objc_msgSend$encodeContext:
+ _objc_msgSend$handleActiveInterfaceOrientationStateResetForClient:
+ _objc_msgSend$horizontalPixelsPerInch
+ _objc_msgSend$immediateMessagingRemoteTargetWithLaunchingAssertionAttributes:
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$initWithHorizontalPixelsPerInch:verticalPixelsPerInch:
+ _objc_msgSend$isActive
+ _objc_msgSend$isAlwaysConnected
+ _objc_msgSend$isEqualToOrderedSet:
+ _objc_msgSend$mainDisplay
+ _objc_msgSend$minusOrderedSet:
+ _objc_msgSend$pixelsPerInch
+ _objc_msgSend$registerInterest
+ _objc_msgSend$registerInterestWithCompletion:
+ _objc_msgSend$rotationDirection
+ _objc_msgSend$setLocalTarget:
+ _objc_msgSend$setMultiplexer:
+ _objc_msgSend$setNullPreserving:
+ _objc_msgSend$takeUpdateCompletions
+ _objc_msgSend$tokenWithHostVPID:directEndpointTarget:workspace:identifier:
+ _objc_msgSend$tokenWithHostVPID:viewServiceSessionIdentifier:
+ _objc_msgSend$unregisterInterest
+ _objc_msgSend$userInteractiveMultiplexer
+ _objc_msgSend$verticalPixelsPerInch
+ _objc_release_x10
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- +[FBSDeviceEmulationConfiguration _forceIsD22ChecksToPass]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]
- +[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt].cold.1
- +[FBSDeviceEmulationConfiguration _sharedDefaults]
- +[FBSDeviceEmulationConfiguration _sharedDefaults].cold.1
- +[FBSDeviceEmulationConfiguration customScaleFactorX]
- +[FBSDeviceEmulationConfiguration customScaleFactorY]
- +[FBSDeviceEmulationConfiguration customTranslationOffsetX]
- +[FBSDeviceEmulationConfiguration customTranslationOffsetY]
- +[FBSDeviceEmulationConfiguration deviceEmulationVersion]
- +[FBSDeviceEmulationConfiguration emulatedArtworkSubtype]
- +[FBSDeviceEmulationConfiguration emulatedDeviceBezelImageName]
- +[FBSDeviceEmulationConfiguration emulatedDeviceBounds]
- +[FBSDeviceEmulationConfiguration emulatedDeviceClass]
- +[FBSDeviceEmulationConfiguration emulatedDeviceImageContainingBundle]
- +[FBSDeviceEmulationConfiguration emulatedDeviceMaskImageName]
- +[FBSDeviceEmulationConfiguration emulatedDisplayCornerRadius]
- +[FBSDeviceEmulationConfiguration emulatedHomeButtonType]
- +[FBSDeviceEmulationConfiguration hasEmulatedDeviceBounds]
- +[FBSDeviceEmulationConfiguration isEmulatedDevice]
- +[FBSDeviceEmulationConfiguration rootLayerBackgroundColorString]
- +[FBSDeviceEmulationConfiguration scalingStyle]
- +[FBSOrientationObserver activeInterfaceOrientation].cold.1
- +[FBSProfileManager sharedInstance]
- +[FBSProfileManager sharedInstance].cold.1
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:]
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.1
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.2
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.3
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.4
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.5
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.6
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.7
- +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.8
- +[FBSSceneIdentityToken tokenWithHostPID:viewServiceSessionIdentifier:].cold.1
- +[FBSSceneIdentityToken tokenWithHostPID:viewServiceSessionIdentifier:].cold.2
- +[FBSSceneIdentityToken tokenWithHostPID:viewServiceSessionIdentifier:].cold.3
- -[FBSApplicationInfo isEnabled]
- -[FBSApplicationProvisioningProfile .cxx_destruct]
- -[FBSApplicationProvisioningProfile UUID]
- -[FBSApplicationProvisioningProfile allowsApplicationIdentifierEntitlement:]
- -[FBSApplicationProvisioningProfile descriptionBuilderWithMultilinePrefix:]
- -[FBSApplicationProvisioningProfile descriptionWithMultilinePrefix:]
- -[FBSApplicationProvisioningProfile description]
- -[FBSApplicationProvisioningProfile expirationDate]
- -[FBSApplicationProvisioningProfile initWithSignerIdentity:profile:]
- -[FBSApplicationProvisioningProfile isAppleInternalProfile]
- -[FBSApplicationProvisioningProfile isBeta]
- -[FBSApplicationProvisioningProfile isFreeDeveloperProfile]
- -[FBSApplicationProvisioningProfile provisionsAllDevices]
- -[FBSApplicationProvisioningProfile signerIdentity]
- -[FBSApplicationProvisioningProfile succinctDescriptionBuilder]
- -[FBSApplicationProvisioningProfile succinctDescription]
- -[FBSApplicationTrustFacade .cxx_destruct]
- -[FBSApplicationTrustFacade trustStateForApplication:]
- -[FBSApplicationTrustFacade trustStateForApplication:].cold.1
- -[FBSApplicationTrustFacade trustStateForApplication:].cold.2
- -[FBSDeviceEmulationDefaults _bindAndRegisterDefaults]
- -[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:latency:originatingConfiguration:validityCheck:]
- -[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:latency:originatingConfiguration:validityCheck:].cold.1
- -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:assertIfInvalid:]
- -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:assertIfInvalid:].cold.1
- -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:assertIfInvalid:].cold.2
- -[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:assertIfInvalid:].cold.3
- -[FBSDisplayConfiguration displayID]
- -[FBSDisplayConfiguration initWithCADisplay:isMainDisplay:]
- -[FBSDisplayConfiguration initWithCADisplay:isMainDisplay:].cold.1
- -[FBSDisplayConfiguration initWithCADisplay:isMainDisplay:].cold.2
- -[FBSDisplayConfiguration isConnected]
- -[FBSDisplayConfiguration orientation]
- -[FBSDisplayConfiguration referenceBounds]
- -[FBSDisplayConfiguration uniqueID]
- -[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:root:]
- -[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:root:].cold.1
- -[FBSDisplayMonitor _initWithBookendObserver:transformer:].cold.2
- -[FBSDisplayMonitor _initWithBookendObserver:transformer:].cold.3
- -[FBSDisplayMonitor _initWithBookendObserver:transformer:].cold.4
- -[FBSDisplayMonitor _initWithBookendObserver:transformer:].cold.5
- -[FBSDisplayMonitor _initWithBookendObserver:transformer:].cold.6
- -[FBSDisplaySource initWithDisplay:alwaysConnected:triggers:monitor:]
- -[FBSDisplaySource initWithDisplay:alwaysConnected:triggers:monitor:].cold.1
- -[FBSDisplaySource initWithDisplay:alwaysConnected:triggers:monitor:].cold.2
- -[FBSDisplaySource initWithDisplay:alwaysConnected:triggers:monitor:].cold.3
- -[FBSLegacySignatureValidationService .cxx_destruct]
- -[FBSLegacySignatureValidationService _initializeProfiles:]
- -[FBSLegacySignatureValidationService _workQueue_expirationDateForProvisioningProfile]
- -[FBSLegacySignatureValidationService _workQueue_signatureNeedsExplicitUserTrust]
- -[FBSLegacySignatureValidationService initWithApplicationInfo:andProvisioningProfiles:isManaged:]
- -[FBSLegacySignatureValidationService initWithApplicationInfo:andProvisioningProfiles:isManaged:].cold.1
- -[FBSLegacySignatureValidationService trustStateForApplication:]
- -[FBSLegacySignatureValidationService trustStateForApplication:].cold.1
- -[FBSOrientationObserver _getAndSetFreshestUpdateGivenUpdate:forced:]
- -[FBSOrientationObserver _initWithClient:callbackQueue:]
- -[FBSOrientationObserver _lock_getAndSetFreshestUpdateGivenUpdate:forced:]
- -[FBSOrientationObserver _lock_setHandler:]
- -[FBSOrientationObserver client:handleOrientationUpdate:]
- -[FBSOrientationObserver dealloc]
- -[FBSOrientationObserver dealloc].cold.1
- -[FBSOrientationObserver handleOrientationResetForClient:]
- -[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]
- -[FBSOrientationObserverClient _server:registerOrientationInterest:]
- -[FBSOrientationObserverClient activeInterfaceOrientationWithCompletion:]
- -[FBSOrientationObserverClient activeInterfaceOrientation]
- -[FBSOrientationObserverClient activeOrientationDidUpdate:]
- -[FBSOrientationObserverClient registerOrientationInterest:]
- -[FBSProfileManager .cxx_destruct]
- -[FBSProfileManager _managedAppsChangedNotification:]
- -[FBSProfileManager _reloadProfiles]
- -[FBSProfileManager _workQueue_reloadManagedApplicationBundleIDs]
- -[FBSProfileManager _workQueue_reloadProfiles]
- -[FBSProfileManager _workQueue_reloadProfiles].cold.1
- -[FBSProfileManager dealloc]
- -[FBSProfileManager init]
- -[FBSProfileManager isManaged:]
- -[FBSProfileManager isStarted]
- -[FBSProfileManager profilesForSignerIdentity:]
- -[FBSProfileManager startService]
- -[FBSScene contexts]
- -[FBSScene display]
- -[FBSScene fbsDisplay]
- -[FBSSceneTransitionContext addUpdateCompletion:]
- -[FBSSceneTransitionContext captureCompletions]
- -[FBSSceneTransitionContext dealloc]
- -[FBSSceneTransitionContext dealloc].cold.1
- -[FBSSystemService reboot]
- -[FBSSystemService shutdown]
- -[FBSWorkspace _queue_scenesClientForEndpoint:creatingIfNecessary:].cold.3
- -[FBSWorkspaceSceneRequestOptions isKeyboardScene]
- -[FBSWorkspaceSceneRequestOptions setKeyboardScene:]
- GCC_except_table104
- GCC_except_table122
- GCC_except_table123
- GCC_except_table132
- GCC_except_table146
- GCC_except_table147
- GCC_except_table148
- GCC_except_table149
- GCC_except_table150
- GCC_except_table151
- GCC_except_table152
- GCC_except_table153
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table182
- GCC_except_table21
- GCC_except_table28
- GCC_except_table43
- GCC_except_table48
- GCC_except_table51
- GCC_except_table52
- GCC_except_table54
- GCC_except_table55
- GCC_except_table60
- GCC_except_table61
- GCC_except_table66
- GCC_except_table70
- GCC_except_table72
- GCC_except_table89
- GCC_except_table90
- GCC_except_table91
- _CFBooleanGetTypeID
- _CFBooleanGetValue
- _CFGetTypeID
- _CFNotificationCenterAddObserver
- _CFNotificationCenterRemoveEveryObserver
- _FBLogAppLaunch
- _FBLogAppLaunch.__logObj
- _FBLogAppLaunch.cold.1
- _FBLogAppLaunch.onceToken
- _FBSDisplayTagToFBSDisplayType
- _FBSOrientationObserverInterestAll
- _FBSProcessResourceAllowanceMakeWithValue
- _FBSProcessResourceAllowanceValue
- _MGGetBoolAnswer
- _ManagedConfigurationLibrary
- _ManagedConfigurationLibrary.cold.1
- _ManagedConfigurationLibraryCore
- _ManagedConfigurationLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_BSAbstractDefaultDomain
- _OBJC_CLASS_$_FBSApplicationProvisioningProfile
- _OBJC_CLASS_$_FBSApplicationTrustFacade
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_FBSDeviceEmulationDefaults
- _OBJC_CLASS_$_FBSLegacySignatureValidationService
- _OBJC_CLASS_$_FBSProfileManager
- _OBJC_IVAR_$_FBSApplicationInfo._enabled
- _OBJC_IVAR_$_FBSApplicationInfo._lazy_entitlements
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._UUID
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._allowedApplicationIdentifierEntitlement
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._appleInternalProfile
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._beta
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._expirationDate
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._freeDeveloperProfile
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._provisionsAllDevices
- _OBJC_IVAR_$_FBSApplicationProvisioningProfile._signerIdentity
- _OBJC_IVAR_$_FBSApplicationTrustFacade._authoritativeProvider
- _OBJC_IVAR_$_FBSApplicationTrustFacade._legacyProvider
- _OBJC_IVAR_$_FBSApplicationTrustFacade._modernProvider
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._appInfo
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._hasFreeDeveloperProvisioningProfile
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._hasUniversalProvisioningProfile
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._isManaged
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._provisioningProfiles
- _OBJC_IVAR_$_FBSLegacySignatureValidationService._workQueue
- _OBJC_IVAR_$_FBSOrientationObserver._callback_queue
- _OBJC_IVAR_$_FBSOrientationObserver._client
- _OBJC_IVAR_$_FBSOrientationObserver._lock
- _OBJC_IVAR_$_FBSOrientationObserver._lock_freshestUpdate
- _OBJC_IVAR_$_FBSOrientationObserver._lock_handler
- _OBJC_IVAR_$_FBSOrientationObserverClient._delegate
- _OBJC_IVAR_$_FBSOrientationObserverClient._lock_interest
- _OBJC_IVAR_$_FBSProfileManager._started
- _OBJC_IVAR_$_FBSProfileManager._workQueue
- _OBJC_IVAR_$_FBSProfileManager._workQueue_managedApplicationBundleIDs
- _OBJC_IVAR_$_FBSProfileManager._workQueue_profilesBySignerIdentity
- _OBJC_IVAR_$_FBSSceneObserver._respondsToPrivateActions
- _OBJC_IVAR_$_FBSWorkspaceSceneRequestOptions._keyboardScene
- _OBJC_METACLASS_$_BSAbstractDefaultDomain
- _OBJC_METACLASS_$_FBSApplicationProvisioningProfile
- _OBJC_METACLASS_$_FBSApplicationTrustFacade
- _OBJC_METACLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_METACLASS_$_FBSDeviceEmulationDefaults
- _OBJC_METACLASS_$_FBSLegacySignatureValidationService
- _OBJC_METACLASS_$_FBSProfileManager
- _OUTLINED_FUNCTION_72
- _OUTLINED_FUNCTION_73
- _OUTLINED_FUNCTION_74
- _SecurityLibrary
- _SecurityLibrary.cold.1
- _SecurityLibraryCore
- _SecurityLibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_FBSDeviceEmulationConfiguration
- __OBJC_$_CLASS_METHODS_FBSProfileManager
- __OBJC_$_CLASS_PROP_LIST_FBSDeviceEmulationConfiguration
- __OBJC_$_INSTANCE_METHODS_FBSApplicationProvisioningProfile
- __OBJC_$_INSTANCE_METHODS_FBSApplicationTrustFacade
- __OBJC_$_INSTANCE_METHODS_FBSDeviceEmulationDefaults
- __OBJC_$_INSTANCE_METHODS_FBSLegacySignatureValidationService
- __OBJC_$_INSTANCE_METHODS_FBSProfileManager
- __OBJC_$_INSTANCE_VARIABLES_FBSApplicationProvisioningProfile
- __OBJC_$_INSTANCE_VARIABLES_FBSApplicationTrustFacade
- __OBJC_$_INSTANCE_VARIABLES_FBSLegacySignatureValidationService
- __OBJC_$_INSTANCE_VARIABLES_FBSProfileManager
- __OBJC_$_PROP_LIST_FBSApplicationPlaceholderProgress.190
- __OBJC_$_PROP_LIST_FBSApplicationProvisioningProfile
- __OBJC_$_PROP_LIST_FBSApplicationTrustFacade
- __OBJC_$_PROP_LIST_FBSDeviceEmulationDefaults
- __OBJC_$_PROP_LIST_FBSDisplayLayoutElement.184
- __OBJC_$_PROP_LIST_FBSLegacySignatureValidationService
- __OBJC_$_PROP_LIST_FBSProcess.116
- __OBJC_$_PROP_LIST_FBSProfileManager
- __OBJC_$_PROP_LIST_FBSSceneClientSettings.72
- __OBJC_$_PROP_LIST_FBSSceneSettings.186
- __OBJC_$_PROP_LIST_FBSSceneTransitionContext.191
- __OBJC_CLASS_PROTOCOLS_$_FBSApplicationTrustFacade
- __OBJC_CLASS_PROTOCOLS_$_FBSLegacySignatureValidationService
- __OBJC_CLASS_RO_$_FBSApplicationProvisioningProfile
- __OBJC_CLASS_RO_$_FBSApplicationTrustFacade
- __OBJC_CLASS_RO_$_FBSDeviceEmulationConfiguration
- __OBJC_CLASS_RO_$_FBSDeviceEmulationDefaults
- __OBJC_CLASS_RO_$_FBSLegacySignatureValidationService
- __OBJC_CLASS_RO_$_FBSProfileManager
- __OBJC_METACLASS_RO_$_FBSApplicationProvisioningProfile
- __OBJC_METACLASS_RO_$_FBSApplicationTrustFacade
- __OBJC_METACLASS_RO_$_FBSDeviceEmulationConfiguration
- __OBJC_METACLASS_RO_$_FBSDeviceEmulationDefaults
- __OBJC_METACLASS_RO_$_FBSLegacySignatureValidationService
- __OBJC_METACLASS_RO_$_FBSProfileManager
- ___30-[FBSApplicationLibrary _load]_block_invoke.183
- ___30-[FBSProfileManager isStarted]_block_invoke
- ___31-[FBSProfileManager isManaged:]_block_invoke
- ___33-[FBSProfileManager startService]_block_invoke
- ___34-[FBSApplicationInfo entitlements]_block_invoke
- ___34-[FBSApplicationInfo entitlements]_block_invoke.cold.1
- ___35+[FBSProfileManager sharedInstance]_block_invoke
- ___36-[FBSProfileManager _reloadProfiles]_block_invoke
- ___36-[FBSWorkspace _registerSourcePeer:]_block_invoke.191
- ___39-[FBSDisplaySource _lock_noteConnected]_block_invoke.148
- ___46-[FBSProfileManager _workQueue_reloadProfiles]_block_invoke
- ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.34
- ___47-[FBSProcessResourceProvision _beginMonitoring]_block_invoke.36
- ___47-[FBSProfileManager profilesForSignerIdentity:]_block_invoke
- ___48-[FBSApplicationLibrary applicationsDidInstall:]_block_invoke.241
- ___50+[FBSDeviceEmulationConfiguration _sharedDefaults]_block_invoke
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.140
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.147
- ___51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.150
- ___52+[FBSOrientationObserver activeInterfaceOrientation]_block_invoke
- ___53-[FBSProfileManager _managedAppsChangedNotification:]_block_invoke
- ___57-[FBSOrientationObserver client:handleOrientationUpdate:]_block_invoke
- ___58-[FBSOrientationObserver handleOrientationResetForClient:]_block_invoke
- ___62+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaGestalt]_block_invoke
- ___62-[FBSDisplaySource _lock_noteUpdatedForTransformInvalidation:]_block_invoke.161
- ___63+[FBSDeviceEmulationConfiguration _isEmulatedDeviceViaDefaults]_block_invoke
- ___64-[FBSLegacySignatureValidationService trustStateForApplication:]_block_invoke
- ___64-[FBSLegacySignatureValidationService trustStateForApplication:]_block_invoke_2
- ___64-[FBSLegacySignatureValidationService trustStateForApplication:]_block_invoke_2.cold.1
- ___67-[FBSOrientationObserver activeInterfaceOrientationWithCompletion:]_block_invoke_2
- ___68-[FBSOrientationObserverClient _server:registerOrientationInterest:]_block_invoke
- ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke
- ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_2
- ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_3
- ___72-[FBSOrientationObserverClient _initWithEndpoint:calloutQueue:delegate:]_block_invoke_4
- ___73-[FBSOrientationObserverClient activeInterfaceOrientationWithCompletion:]_block_invoke
- ___73-[FBSOrientationObserverClient activeInterfaceOrientationWithCompletion:]_block_invoke.cold.1
- ___76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.129
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.184
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.198
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.202
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.cold.1
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_2.189
- ___88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke_4.cold.1
- ___94-[FBSApplicationLibrary _handleApplicationStateDidChange:notifyForUpdateInsteadOfReplacement:]_block_invoke.242
- ___FBLogAppLaunch_block_invoke
- ___ManagedConfigurationLibraryCore_block_invoke
- ___NSDictionary0__struct
- ___SecurityLibraryCore_block_invoke
- ____ingestPropertiesFromSettingsSubclass_block_invoke.399
- ____realizeSettingsExtension_block_invoke.259
- ____realizeSettingsExtension_block_invoke.278
- ____realizeSettingsExtension_block_invoke.285
- ____realizeSettingsExtension_block_invoke.285.cold.1
- ____realizeSettingsExtension_block_invoke.285.cold.2
- ____realizeSettingsExtension_block_invoke.298
- ____realizeSettingsExtension_block_invoke_2.261
- ____realizeSettingsExtension_block_invoke_2.281
- ____realizeSettingsExtension_block_invoke_2.300
- ____realizeSettingsExtension_block_invoke_3.263
- ____realizeSettingsExtension_block_invoke_3.283
- ____realizeSettingsExtension_block_invoke_3.302
- ____realizeSettingsExtension_block_invoke_4.304
- ____realizeSettingsExtension_block_invoke_5.306
- ____realizeSettingsExtension_block_invoke_6.308
- ____realizeSettingsExtension_block_invoke_7.310
- ___block_descriptor_40_e8_32s_e11_v24?0q8q16ls32l8
- ___block_descriptor_40_e8_32s_e9_B16?0^v8ls32l8
- ___block_descriptor_40_e8_32w_e42_v24?0"FBSOrientationUpdate"8"NSError"16lw32l8
- ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
- ___block_descriptor_48_e8_32bs40w_e30_v16?0"FBSOrientationUpdate"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e42_v24?0"FBSOrientationUpdate"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e50_v16?0"<BSServiceConnectionInternalConfiguring>"8ls32l8s40l8s48l8
- ___block_literal_global.133
- ___block_literal_global.143
- ___block_literal_global.149
- ___block_literal_global.152
- ___block_literal_global.166
- ___block_literal_global.177
- ___block_literal_global.219
- ___block_literal_global.225
- ___block_literal_global.25
- ___block_literal_global.295
- ___block_literal_global.3
- ___block_literal_global.67
- ___getMCManagedAppsChangedNotificationSymbolLoc_block_invoke
- ___getMCProfileConnectionClass_block_invoke
- ___getMCProfileConnectionClass_block_invoke.cold.1
- ___getMISAppApprovalStateSymbolLoc_block_invoke
- ___getMISEnumerateInstalledProvisioningProfilesSymbolLoc_block_invoke
- ___getMISProfileGetValueSymbolLoc_block_invoke
- ___getMISProvisioningProfileGetDeveloperCertificatesSymbolLoc_block_invoke
- ___getMISProvisioningProfileGetEntitlementsSymbolLoc_block_invoke
- ___getMISProvisioningProfileGetExpirationDateSymbolLoc_block_invoke
- ___getMISProvisioningProfileGetUUIDSymbolLoc_block_invoke
- ___getMISProvisioningProfileGrantsEntitlementSymbolLoc_block_invoke
- ___getMISProvisioningProfileIsAppleInternalProfileSymbolLoc_block_invoke
- ___getMISProvisioningProfileProvisionsAllDevicesSymbolLoc_block_invoke
- ___getMISQueryBlacklistForBundleSymbolLoc_block_invoke
- ___getMISQueryBlacklistForCdHashSymbolLoc_block_invoke
- ___getMISValidateUPPSymbolLoc_block_invoke
- ___getSecCertificateCopySubjectSummarySymbolLoc_block_invoke
- ___getSecCertificateCreateWithDataSymbolLoc_block_invoke
- ___kCFBooleanFalse
- __handleProfilesChangedNotification
- __isEmulatedDeviceViaDefaults.isEmulatedViaDefaults
- __isEmulatedDeviceViaDefaults.onceToken
- __isEmulatedDeviceViaGestalt.onceToken
- __isEmulatedDeviceViaGestalt.sIsEmulatedDevice
- __sharedDefaults.onceToken
- __sharedDefaults.sEmulationDefaults
- _activeInterfaceOrientation.client
- _activeInterfaceOrientation.onceToken
- _dispatch_assert_queue$V2
- _getMCManagedAppsChangedNotification
- _getMCManagedAppsChangedNotification.cold.1
- _getMCManagedAppsChangedNotificationSymbolLoc
- _getMCManagedAppsChangedNotificationSymbolLoc.ptr
- _getMCProfileConnectionClass
- _getMCProfileConnectionClass.softClass
- _getMISAppApprovalStateSymbolLoc
- _getMISAppApprovalStateSymbolLoc.ptr
- _getMISEnumerateInstalledProvisioningProfilesSymbolLoc
- _getMISEnumerateInstalledProvisioningProfilesSymbolLoc.ptr
- _getMISProfileGetValueSymbolLoc
- _getMISProfileGetValueSymbolLoc.ptr
- _getMISProvisioningProfileGetDeveloperCertificatesSymbolLoc
- _getMISProvisioningProfileGetDeveloperCertificatesSymbolLoc.ptr
- _getMISProvisioningProfileGetEntitlementsSymbolLoc
- _getMISProvisioningProfileGetEntitlementsSymbolLoc.ptr
- _getMISProvisioningProfileGetExpirationDateSymbolLoc
- _getMISProvisioningProfileGetExpirationDateSymbolLoc.ptr
- _getMISProvisioningProfileGetUUIDSymbolLoc
- _getMISProvisioningProfileGetUUIDSymbolLoc.ptr
- _getMISProvisioningProfileGrantsEntitlementSymbolLoc
- _getMISProvisioningProfileGrantsEntitlementSymbolLoc.ptr
- _getMISProvisioningProfileIsAppleInternalProfileSymbolLoc
- _getMISProvisioningProfileIsAppleInternalProfileSymbolLoc.ptr
- _getMISProvisioningProfileProvisionsAllDevicesSymbolLoc
- _getMISProvisioningProfileProvisionsAllDevicesSymbolLoc.ptr
- _getMISQueryBlacklistForBundleSymbolLoc
- _getMISQueryBlacklistForBundleSymbolLoc.ptr
- _getMISQueryBlacklistForCdHashSymbolLoc
- _getMISQueryBlacklistForCdHashSymbolLoc.ptr
- _getMISValidateUPPSymbolLoc
- _getMISValidateUPPSymbolLoc.ptr
- _getSecCertificateCopySubjectSummarySymbolLoc
- _getSecCertificateCopySubjectSummarySymbolLoc.ptr
- _getSecCertificateCreateWithDataSymbolLoc
- _getSecCertificateCreateWithDataSymbolLoc.ptr
- _gotLoadHelper_x8$_OBJC_CLASS_$_AITransactionLog
- _initWithDisplay:alwaysConnected:triggers:monitor:.__instanceCounter
- _objc_msgSend$_appIDEntitlement
- _objc_msgSend$_bindProperty:withDefaultKey:toDefaultValue:options:
- _objc_msgSend$_getAndSetFreshestUpdateGivenUpdate:forced:
- _objc_msgSend$_initWithDomain:
- _objc_msgSend$_initWithEndpoint:calloutQueue:delegate:
- _objc_msgSend$_initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:latency:originatingConfiguration:validityCheck:
- _objc_msgSend$_initWithImmutableDisplay:originalDisplay:assertIfInvalid:
- _objc_msgSend$_initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:root:
- _objc_msgSend$_initializeProfiles:
- _objc_msgSend$_isEmulatedDeviceViaDefaults
- _objc_msgSend$_isEmulatedDeviceViaGestalt
- _objc_msgSend$_lock_getAndSetFreshestUpdateGivenUpdate:forced:
- _objc_msgSend$_lock_setHandler:
- _objc_msgSend$_reloadProfiles
- _objc_msgSend$_server:registerOrientationInterest:
- _objc_msgSend$_sharedDefaults
- _objc_msgSend$_synchronize:
- _objc_msgSend$_workQueue_expirationDateForProvisioningProfile
- _objc_msgSend$_workQueue_reloadManagedApplicationBundleIDs
- _objc_msgSend$_workQueue_reloadProfiles
- _objc_msgSend$_workQueue_signatureNeedsExplicitUserTrust
- _objc_msgSend$activeInterfaceOrientation
- _objc_msgSend$activeInterfaceOrientationWithCompletion:
- _objc_msgSend$activeOrientationDidUpdate:
- _objc_msgSend$allowsApplicationIdentifierEntitlement:
- _objc_msgSend$bezelImageName
- _objc_msgSend$bundleProxyForIdentifier:
- _objc_msgSend$bundleWithURL:
- _objc_msgSend$cacheInfoWithData:hashType:
- _objc_msgSend$cachedCDHashInfo
- _objc_msgSend$cachedCodeDirectoryHash
- _objc_msgSend$cachedCodeDirectoryHashType
- _objc_msgSend$client:handleOrientationUpdate:
- _objc_msgSend$customScaleFactorX
- _objc_msgSend$customScaleFactorY
- _objc_msgSend$customTranslationOffsetX
- _objc_msgSend$customTranslationOffsetY
- _objc_msgSend$date
- _objc_msgSend$emulatedArtworkSubtype
- _objc_msgSend$emulatedDeviceBounds
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedDisplayHeight
- _objc_msgSend$emulatedDisplayWidth
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$enableEmulation
- _objc_msgSend$entitlements
- _objc_msgSend$expirationDate
- _objc_msgSend$forceIsD22ChecksToPass
- _objc_msgSend$handleForIdentifier:error:
- _objc_msgSend$handleOrientationResetForClient:
- _objc_msgSend$handler
- _objc_msgSend$hasSuffix:
- _objc_msgSend$imageContainingBundleIdentifier
- _objc_msgSend$initWithApplicationInfo:andProvisioningProfiles:isManaged:
- _objc_msgSend$initWithCADisplay:
- _objc_msgSend$initWithSignerIdentity:profile:
- _objc_msgSend$isAppleInternalProfile
- _objc_msgSend$isBeta
- _objc_msgSend$isEmulatedDevice
- _objc_msgSend$isFreeDeveloperProfile
- _objc_msgSend$isManaged:
- _objc_msgSend$managedAppIDs
- _objc_msgSend$maskImageName
- _objc_msgSend$orientation
- _objc_msgSend$profilesForSignerIdentity:
- _objc_msgSend$provisionsAllDevices
- _objc_msgSend$registerOrientationInterest:
- _objc_msgSend$registerOrientationInterest:completion:
- _objc_msgSend$remoteTargetWithLaunchingAssertionAttributes:
- _objc_msgSend$requestActiveOrientation
- _objc_msgSend$requestActiveOrientationCompletion:
- _objc_msgSend$rootLayerBackgroundColorString
- _objc_msgSend$scalingStyle
- _objc_msgSend$setAuthoritative:
- _objc_msgSend$setCachedCDHashInfo:
- _objc_msgSend$setUpdateCompletions:
- _objc_msgSend$sharedConnection
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$tokenWithHostPID:directEndpointTarget:workspace:identifier:
- _objc_msgSend$trustedCodeSigningIdentities
- _objc_msgSend$updateCompletions
- _objc_msgSend$valueForKey:
- _objc_release_x2
- _os_variant_has_internal_diagnostics
- _sharedInstance.__instance
- _sharedInstance.__once
- _soft_MISAppApprovalState
- _soft_MISAppApprovalState.cold.1
- _soft_MISEnumerateInstalledProvisioningProfiles
- _soft_MISEnumerateInstalledProvisioningProfiles.cold.1
- _soft_MISProfileGetValue
- _soft_MISProfileGetValue.cold.1
- _soft_MISProvisioningProfileGetDeveloperCertificates
- _soft_MISProvisioningProfileGetDeveloperCertificates.cold.1
- _soft_MISProvisioningProfileGetEntitlements
- _soft_MISProvisioningProfileGetEntitlements.cold.1
- _soft_MISProvisioningProfileGetExpirationDate
- _soft_MISProvisioningProfileGetExpirationDate.cold.1
- _soft_MISProvisioningProfileGetUUID
- _soft_MISProvisioningProfileGetUUID.cold.1
- _soft_MISProvisioningProfileGrantsEntitlement
- _soft_MISProvisioningProfileGrantsEntitlement.cold.1
- _soft_MISProvisioningProfileIsAppleInternalProfile
- _soft_MISProvisioningProfileIsAppleInternalProfile.cold.1
- _soft_MISProvisioningProfileProvisionsAllDevices
- _soft_MISProvisioningProfileProvisionsAllDevices.cold.1
- _soft_MISQueryBlacklistForBundle
- _soft_MISQueryBlacklistForBundle.cold.1
- _soft_MISQueryBlacklistForCdHash
- _soft_MISQueryBlacklistForCdHash.cold.1
- _soft_MISValidateUPP
- _soft_MISValidateUPP.cold.1
- _soft_SecCertificateCopySubjectSummary
- _soft_SecCertificateCopySubjectSummary.cold.1
- _soft_SecCertificateCreateWithData
- _soft_SecCertificateCreateWithData.cold.1
CStrings:
+ "\"%@\" is not of type FBSDisplayConfiguration"
+ "%@->/%@:%@"
+ "%@/pseudo:%@"
+ "%@/view-service:%@"
+ "%@<%p>"
+ "-[FBSComponentScene scene]"
+ "0@`"
+ "<%p> Received orientation update %{public}@ with a sequence number less than the last update received %{public}@."
+ "<%p> Received orientation update: %{public}@ that we're forcefully updating"
+ "<%p> activeInterfaceOrientationStateUpdateWithCompletion error: %{public}@"
+ "@\"FBSDisplayIdentity\"16@?0@\"FBSDisplayConfiguration\"8"
+ "Cannot access scene as it has been invalidated and deallocated"
+ "Completions have already been taken for this update. Are you adding a completion too late?"
+ "Current mode is nil"
+ "Display tags (%li) do not contain display type \"%@\""
+ "Extension added twice: %@"
+ "FBSActiveInterfaceOrientationObserver.m"
+ "FBSActiveInterfaceOrientationState.m"
+ "FBSDisplayConfiguration cannot be initialized as requested because: %@ : %@"
+ "FBSDisplayConfiguration cannot be initialized as requested because: %{public}@ : %{public}@"
+ "FBSDisplayConfiguration.m"
+ "FBSDisplayIdentity.m"
+ "FBSDisplayTypes.m"
+ "FBSSceneUpdate.m"
+ "Invalid bounds"
+ "Invalid connection type \"%@\""
+ "Invalid display type \"%@\""
+ "Invalid nativeBounds"
+ "Invalid overscan compensation \"%@\""
+ "Invalid pixelRect"
+ "Invalid safe overscan ratio \"%@\""
+ "There should be no more update completions."
+ "[%@] Adding extension (from %@): \"%@\""
+ "[%u]"
+ "[displays count] > 0"
+ "always connected displays cannot debounce nor disconnect : %@"
+ "alwaysConnected"
+ "animationDuration"
+ "calloutQueue != ((void *)0)"
+ "com.apple.frontBoardServices.activeInterfaceOrientationObserver.callback"
+ "constructing configuration failed : identity=%@ configChanged=%i currentMode=%@ preferredMode=%@ otherModes=%@ cloningSupported=%i overscanned=%i overscanCompensation=%@ safeOverscanRatio=%@ pixelSize=%@ nativeBounds=%@ bounds=%@ pixelDensity=%@ : base=%@"
+ "default value for BOOL setting \"%@\" must be a boolean"
+ "horizontal"
+ "host"
+ "invalid host pid : %@"
+ "invalid host vpid=%@"
+ "pixelDensity"
+ "pixelsPerInch"
+ "v16@?0@\"<BSServiceConnectionCommonConfiguring>\"8"
+ "v16@?0@\"<BSServiceConnectionInitiatingOptions>\"8"
+ "v16@?0@\"<BSServiceInitiatingConnectionConfiguring>\"8"
+ "v16@?0@\"<BSServiceListenerConnectionConfiguring>\"8"
+ "v16@?0@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\"8"
+ "v16@?0@\"BSServiceListenerConnection<BSServiceConnectionContext>\"8"
+ "v16@?0@\"FBSActiveInterfaceOrientationStateUpdate\"8"
+ "v24@?0@\"FBSActiveInterfaceOrientationStateUpdate\"8@\"NSError\"16"
+ "vertical"
+ "void FBSCADisplayToDisplayTypes(CADisplay *__strong _Nonnull, BOOL, BOOL * _Nullable, FBSDisplayType * _Nullable, FBSDisplayConnectionType * _Nullable, BOOL * _Nullable)"
+ "we failed to make an always connected display for %@"
- "#16@0:8"
- "#24@0:8@16"
- "%i(%p)"
- "%i->%@/%@:%@"
- "%i/psuedo:%@"
- "%i/view-service:%@"
- "%{public}@: Error loading provisioning profiles: %{public}@"
- "*"
- "-[FBSOrientationObserver dealloc]"
- ".cxx_destruct"
- "/AppleInternal/Library/Frameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "/AppleInternal/Library/Frameworks/Security.framework/Security"
- "/System/AppleInternal/Library/Frameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "/System/AppleInternal/Library/Frameworks/Security.framework/Security"
- "/System/Library/Frameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "/System/Library/Frameworks/Security.framework/Security"
- "/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "/System/Library/PrivateFrameworks/Security.framework/Security"
- ":16@0:8"
- "<%p> Received orientation update: %{public}@ with a sequence number less than the last update received %{public}@."
- "<%p> Registering interest for orientation updates."
- "<%p> Unregistering interest for orientation updates."
- "<%p>: Received orientation update: %{public}@ that we're forcefully updating"
- "<%p>: activeInterfaceOrientationWithCompletion error: %{public}@"
- "@"
- "@\"<BSInvalidatable>\""
- "@\"<BSInvalidatable>\"24@0:8@\"FBSDisplayLayoutElement\"16"
- "@\"<BSInvalidatable>\"24@0:8@\"NSString\"16"
- "@\"<BSXPCServiceConnectionMessage>\""
- "@\"<FBSApplicationDataStoreRepositoryClient>\""
- "@\"<FBSApplicationTrustDataProvider>\""
- "@\"<FBSComponentScene>\""
- "@\"<FBSDisplayObserving>\""
- "@\"<FBSDisplayTransformer>\""
- "@\"<FBSOrientationObserverClientDelegate>\""
- "@\"<FBSProcess>\""
- "@\"<FBSProcess>\"16@0:8"
- "@\"<FBSProcessExecutionProvisionDelegate>\""
- "@\"<FBSProcessInternal>\""
- "@\"<FBSSceneAgentProxy>\"16@0:8"
- "@\"<FBSSceneClientAgent>\""
- "@\"<FBSSceneComponent>\""
- "@\"<FBSSceneComponent>\"24@0:8#16"
- "@\"<FBSSceneDelegate>\""
- "@\"<FBSSceneHandle>\""
- "@\"<FBSSceneObserver>\""
- "@\"<FBSSceneSnapshotRequestDelegate>\""
- "@\"<FBSSceneUpdater>\""
- "@\"<FBSWorkspaceDelegate>\""
- "@\"<FBSWorkspaceServiceClientInterface>\""
- "@\"<FBSWorkspaceServiceTarget>\""
- "@\"<FBSceneClientProcess>\"16@0:8"
- "@\"<NSCopying>\""
- "@\"<_FBSMISInterfaceWrapper>\""
- "@\"BKSAnimationFenceHandle\""
- "@\"BKSAnimationFenceHandle\"16@0:8"
- "@\"BKSProcessAssertion\""
- "@\"BKSTerminationAssertion\""
- "@\"BSAbsoluteMachTimer\""
- "@\"BSActionResponder\""
- "@\"BSAnimationSettings\"16@0:8"
- "@\"BSAtomicSignal\""
- "@\"BSAuditToken\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSKeyedSettings\""
- "@\"BSKeyedSettings\"16@0:8"
- "@\"BSMachPortTaskNameRight\""
- "@\"BSMachPortTaskNameRight\"16@0:8"
- "@\"BSMutableKeyedSettings\""
- "@\"BSMutableSettings\""
- "@\"BSObjCProtocol\""
- "@\"BSProcessHandle\""
- "@\"BSProcessHandle\"16@0:8"
- "@\"BSServiceCompoundQueue\""
- "@\"BSServiceConnection\""
- "@\"BSServiceConnection<BSServiceConnectionHost>\""
- "@\"BSServiceConnectionEndpoint\""
- "@\"BSServiceConnectionEndpointMonitor\""
- "@\"BSServiceConnectionListener\""
- "@\"BSServiceDispatchQueue\""
- "@\"BSServiceInterface\""
- "@\"BSServiceQuality\""
- "@\"BSServiceQueue\""
- "@\"BSServiceQueue\"16@0:8"
- "@\"BSSettings\""
- "@\"BSSettings\"16@0:8"
- "@\"BSSettingsDiff\""
- "@\"BSXPCCoder\""
- "@\"CAContext\""
- "@\"CADisplay\""
- "@\"FBProcessExecutionContext\"16@0:8"
- "@\"FBSApplicationInfo\""
- "@\"FBSApplicationInfo\"24@0:8@\"BSAuditToken\"16"
- "@\"FBSApplicationInfo\"24@0:8@\"NSString\"16"
- "@\"FBSApplicationLibrary\""
- "@\"FBSApplicationLibraryConfiguration\""
- "@\"FBSApplicationPlaceholder\""
- "@\"FBSApplicationPlaceholderProgress\""
- "@\"FBSDisplayConfiguration\""
- "@\"FBSDisplayConfiguration\"16@0:8"
- "@\"FBSDisplayIdentity\""
- "@\"FBSDisplayLayout\""
- "@\"FBSDisplayLayout\"16@0:8"
- "@\"FBSDisplayMode\""
- "@\"FBSDisplayMonitor\""
- "@\"FBSDisplaySource\""
- "@\"FBSMutableSceneParameters\""
- "@\"FBSOpenApplicationService\""
- "@\"FBSOrientationObserverClient\""
- "@\"FBSOrientationUpdate\""
- "@\"FBSOrientationUpdate\"16@0:8"
- "@\"FBSProcessAssertion\""
- "@\"FBSProcessExecutionPolicy\""
- "@\"FBSProcessExecutionStrategy\""
- "@\"FBSProcessTerminationRequest\"32@0:8@\"FBSProcessWatchdog\"16@\"NSError\"24"
- "@\"FBSProcessWatchdog\""
- "@\"FBSProcessWatchdogPolicy\""
- "@\"FBSPseudoSceneUpdater\""
- "@\"FBSScene\""
- "@\"FBSScene\"24@0:8@\"FBSClientSceneFutureDefinition\"16"
- "@\"FBSScene\"24@0:8@\"FBSSceneIdentity\"16"
- "@\"FBSSceneActivitySession\"32@0:8@\"NSString\"16@\"FBSProcessExecutionPolicy\"24"
- "@\"FBSSceneClientIdentity\""
- "@\"FBSSceneClientIdentity\"16@0:8"
- "@\"FBSSceneClientSettings\""
- "@\"FBSSceneClientSettings\"16@0:8"
- "@\"FBSSceneClientSettingsDiff\""
- "@\"FBSSceneDefinition\""
- "@\"FBSSceneDefinition\"16@0:8"
- "@\"FBSSceneHostHandle\""
- "@\"FBSSceneIdentity\""
- "@\"FBSSceneIdentityToken\""
- "@\"FBSSceneIdentityToken\"16@0:8"
- "@\"FBSSceneMessage\""
- "@\"FBSSceneParameters\""
- "@\"FBSSceneParameters\"16@0:8"
- "@\"FBSSceneSettings\""
- "@\"FBSSceneSettings\"16@0:8"
- "@\"FBSSceneSettingsDiff\""
- "@\"FBSSceneSnapshotContext\""
- "@\"FBSSceneSnapshotRequestHandle\""
- "@\"FBSSceneSpecification\""
- "@\"FBSSceneSpecification\"16@0:8"
- "@\"FBSSceneTransitionContext\""
- "@\"FBSSceneUpdate\""
- "@\"FBSSceneUpdate\"16@0:8"
- "@\"FBSSettings\""
- "@\"FBSSettings<FBSMutableSettings>\""
- "@\"FBSSettingsDiff\""
- "@\"FBSSignatureValidationService\""
- "@\"FBSSystemAppProxy\""
- "@\"FBSWorkspace\""
- "@\"FBSWorkspaceScenesClientIdentifier\""
- "@\"FBSceneUpdateContext\"16@0:8"
- "@\"FBWatchdogTransitionContext\"16@0:8"
- "@\"IOSurface\""
- "@\"LSApplicationIdentity\""
- "@\"LSApplicationProxy\""
- "@\"LSApplicationWorkspace\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCountedSet\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSError\"16@0:8"
- "@\"NSError\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableOrderedSet\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<NSCopying>\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSOrderedSet\""
- "@\"NSProgress\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSSet\"24@0:8@\"NSSet\"16"
- "@\"NSSet\"32@0:8@\"FBSScene\"16@\"NSSet\"24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSString\"24@0:8Q16"
- "@\"NSString\"32@0:8@\"BSSettings\"16Q24"
- "@\"NSString\"40@0:8q16@24Q32"
- "@\"NSString\"48@0:8@\"BSSettings\"16q24@32Q40"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"RBSProcessHandle\""
- "@\"RBSProcessHandle\"16@0:8"
- "@\"RBSProcessIdentity\""
- "@\"RBSProcessIdentity\"16@0:8"
- "@\"_FBSDisplayLayoutService\""
- "@\"_FBSDisplayLayoutServiceAssertion\""
- "@\"_FBSSnapshotContext\""
- "@148@0:8I16{CATransform3D=dddddddddddddddd}20"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@224@0:8@16@24@32@40I48B52q56@64@72@80B88B92q96{CGSize=dd}104{CGSize=dd}120{CGRect={CGPoint=dd}{CGSize=dd}}136{CGRect={CGPoint=dd}{CGSize=dd}}168d200@208q216"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"<FBSComponentScene>\"16"
- "@24@0:8@\"FBSInvocation\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@24@0:8@\"Protocol\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8I16I20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8i16i20"
- "@24@0:8o^@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@28@0:8@16c24"
- "@28@0:8I16d20"
- "@28@0:8i16@20"
- "@32@0:8#16#24"
- "@32@0:8:16#24"
- "@32@0:8:16@24"
- "@32@0:8@\"NSString\"16@\"NSString\"24"
- "@32@0:8@16#24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8@?16@?24"
- "@32@0:8Q16@24"
- "@32@0:8d16@24"
- "@32@0:8q16@?24"
- "@32@0:8q16d24"
- "@32@0:8{CGSize=dd}16"
- "@36@0:8@16@24B32"
- "@36@0:8@16c24@?28"
- "@36@0:8I16Q20d28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16d24@?32"
- "@40@0:8@16d24q32"
- "@40@0:8B16B20@24@32"
- "@40@0:8Q16@24@32"
- "@40@0:8q16@24Q32"
- "@40@0:8q16Q24@?32"
- "@40@0:8q16q24@32"
- "@40@0:8q16q24q32"
- "@40@0:8{?=qQQ}16"
- "@40@0:8{CGSize=dd}16d32"
- "@44@0:8i16@20@28@36"
- "@48@0:8@16q24@32Q40"
- "@48@0:8q16Q24d32q40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CGSize=dd}16d32d40"
- "@52@0:8@16B24B28B32q36@?44"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8Q16Q24Q32d40q48q56"
- "@72@0:8@16{CGSize=dd}24{CGRect={CGPoint=dd}{CGSize=dd}}40"
- "@72@0:8q16B24I28q32I40i44B48@52B60@64"
- "@92@0:8Q16Q24Q32d40d48q56q64q72B80q84"
- "@?"
- "@?16@0:8"
- "App info objects must match or we've done something wrong."
- "AppLaunch"
- "Authoritative and modern states were divergent - authoritative: %@, modern: %@"
- "B"
- "B16@0:8"
- "B16@?0^v8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"FBSSceneSnapshotRequest\"16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B24@0:8o^@16"
- "B24@0:8o^Q16"
- "B24@0:8o^{?=qQQ}16"
- "B24@0:8q16"
- "B32@0:8@\"FBSProcessWatchdog\"16o^@24"
- "B32@0:8@\"FBSSceneSnapshotRequest\"16@\"FBSSceneSnapshotContext\"24"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B32@0:8@16^q24"
- "B32@0:8@16o^@24"
- "B32@0:8Q16@?24"
- "B40@0:8@\"NSString\"16@\"NSString\"24^@32"
- "B40@0:8@16@24^@32"
- "B48@0:8@\"BSDescriptionBuilder\"16q24@32Q40"
- "B48@0:8@16q24@32Q40"
- "B56@0:8@\"BSSettings\"16@\"BSDescriptionBuilder\"24q32@40Q48"
- "B56@0:8@16@24q32@40Q48"
- "BSDescriptionProviding"
- "BSInterfaceOrientationMapResolving"
- "BSInvalidatable"
- "BSObjCProtocol"
- "BSServiceConnection"
- "BSServiceConnectionEndpointMonitorDelegate"
- "BSServiceConnectionListenerDelegate"
- "BSSettingDescriptionProvider"
- "BSXPCAutoCoding"
- "BSXPCCoding"
- "BSXPCSecureCoding"
- "Boolean soft_MISProvisioningProfileGrantsEntitlement(MISProfileRef, CFStringRef, CFTypeRef)"
- "Boolean soft_MISProvisioningProfileIsAppleInternalProfile(MISProfileRef)"
- "Boolean soft_MISProvisioningProfileProvisionsAllDevices(MISProfileRef)"
- "C"
- "CAContext"
- "CFArrayRef soft_MISProvisioningProfileGetDeveloperCertificates(MISProfileRef)"
- "CFDateRef soft_MISProvisioningProfileGetExpirationDate(MISProfileRef)"
- "CFDictionaryRef soft_MISProvisioningProfileGetEntitlements(MISProfileRef)"
- "CFStringRef soft_MISProvisioningProfileGetUUID(MISProfileRef)"
- "CFStringRef soft_SecCertificateCopySubjectSummary(SecCertificateRef)"
- "CFTypeRef soft_MISProfileGetValue(MISProfileRef, CFStringRef)"
- "CGImage"
- "CGImageBuilder"
- "Class getMCProfileConnectionClass(void)_block_invoke"
- "FBSALOToken"
- "FBSApplicationDataStoreClientFactory"
- "FBSApplicationDataStoreMonitor"
- "FBSApplicationDataStoreRepositoryClient"
- "FBSApplicationDataStoreRepositoryClientObserver"
- "FBSApplicationIdentifying"
- "FBSApplicationInfoProvider"
- "FBSApplicationLibraryConfiguration"
- "FBSApplicationPlaceholderProgress"
- "FBSApplicationProvisioningProfile"
- "FBSApplicationTrustDataProvider"
- "FBSApplicationTrustFacade"
- "FBSApplicationTrustFacade.m"
- "FBSApplicationUninstallOptions"
- "FBSBasicSceneAgent"
- "FBSBasicSceneClientAgent"
- "FBSBasicSceneHostAgent"
- "FBSBezelImageName"
- "FBSBundleInfo"
- "FBSCAContextSceneLayer"
- "FBSClientSceneFutureDefinition"
- "FBSComponentScene"
- "FBSComponentSceneSupport"
- "FBSCoreSettingsExtension"
- "FBSCustomXScaleFactor"
- "FBSCustomXTranslationOffset"
- "FBSCustomYScaleFactor"
- "FBSCustomYTranslationOffset"
- "FBSDataResetRequest"
- "FBSDerivedSettingsExtension"
- "FBSDeviceEmulationBackgroundColorString"
- "FBSDeviceEmulationConfiguration"
- "FBSDeviceEmulationDefaults"
- "FBSDeviceEmulationScalingStyle"
- "FBSDisplay.m"
- "FBSDisplayConfiguration cannot be initialized as requested : %@"
- "FBSDisplayConfiguration cannot be initialized as requested : %{public}@"
- "FBSDisplayConfigurationBuilder"
- "FBSDisplayConfigurationRequest"
- "FBSDisplayIdentity"
- "FBSDisplayLayout"
- "FBSDisplayLayoutMonitor"
- "FBSDisplayLayoutMonitorClientInterface"
- "FBSDisplayLayoutMonitorConfiguration"
- "FBSDisplayLayoutPublisher"
- "FBSDisplayLayoutPublishing"
- "FBSDisplayLayoutTransitionContext"
- "FBSDisplayMonitor"
- "FBSDisplaySource"
- "FBSEmulatedArtworkSubtype"
- "FBSEmulatedDeviceClass"
- "FBSEmulatedDisplayCornerRadius"
- "FBSEmulatedDisplayHeight"
- "FBSEmulatedDisplayWidth"
- "FBSEmulatedHomeButtonType"
- "FBSEnableDeviceEmulation"
- "FBSExtensionInfo"
- "FBSForceIsD22ChecksToPass"
- "FBSImageContainingBundleIdentifier"
- "FBSInvocationReceiving"
- "FBSInvocationReply"
- "FBSInvocationSending"
- "FBSInvocationTarget"
- "FBSKeyboardProxyLayer"
- "FBSLazyApplicationInfoProvider"
- "FBSLegacySignatureValidationService"
- "FBSLegacySignatureValidationService.m"
- "FBSMaskImageName"
- "FBSMutableDisplayConfigurationRequest"
- "FBSMutableProcessExecutionStrategy"
- "FBSMutableSceneClientSettings"
- "FBSMutableSceneDefinition"
- "FBSMutableSceneIdentity"
- "FBSMutableSceneParameters"
- "FBSMutableSceneSettings"
- "FBSMutableSceneUpdate"
- "FBSMutableSetting"
- "FBSMutableSetting_Internal"
- "FBSMutableSettings"
- "FBSObjectProxy"
- "FBSOpenApplicationServiceServerInterface"
- "FBSOpenApplicationServiceSpecification"
- "FBSOrientationObserver"
- "FBSOrientationObserver.m"
- "FBSOrientationObserverClient"
- "FBSOrientationObserverClientDelegate"
- "FBSOrientationServiceClientInterface"
- "FBSOrientationServiceServerInterface"
- "FBSOrientationServiceSpecification"
- "FBSOrientationUpdate"
- "FBSPlistCollection"
- "FBSProcess"
- "FBSProcessAssertion"
- "FBSProcessExecutionProvisionDelegate"
- "FBSProcessHandle"
- "FBSProcessIdentity"
- "FBSProcessInternal"
- "FBSProcessResourceProvision"
- "FBSProcessWatchdog"
- "FBSProfileManager"
- "FBSPseudoSceneUpdater"
- "FBSScene"
- "FBSSceneAction"
- "FBSSceneAgent"
- "FBSSceneAgentProxy"
- "FBSSceneClientAgent"
- "FBSSceneClientIdentifying"
- "FBSSceneClientIdentity"
- "FBSSceneClientSettingsCore"
- "FBSSceneClientSettingsDiff"
- "FBSSceneClientSettingsDiffInspector"
- "FBSSceneComponent"
- "FBSSceneCreating"
- "FBSSceneDefinition"
- "FBSSceneEvent"
- "FBSSceneExtensible"
- "FBSSceneExtension"
- "FBSSceneHandle"
- "FBSSceneHostAgent"
- "FBSSceneHostHandle"
- "FBSSceneObserver"
- "FBSSceneObserverConfiguring"
- "FBSSceneObserver_Internal"
- "FBSSceneSettingsCore"
- "FBSSceneSettingsDiff"
- "FBSSceneSettingsDiffInspector"
- "FBSSceneSnapshotAction"
- "FBSSceneSnapshotContext"
- "FBSSceneSnapshotRequest"
- "FBSSceneSnapshotRequestAction"
- "FBSSceneSnapshotRequestDelegate"
- "FBSSceneSnapshotRequestHandle"
- "FBSSceneTransitionContext"
- "FBSSceneTransitionContext.m"
- "FBSSceneTransitionContextCore"
- "FBSSceneUpdate"
- "FBSSceneUpdater"
- "FBSSceneUpdaterDelegate"
- "FBSSerialQueue"
- "FBSServiceFacility"
- "FBSServiceFacilityClient"
- "FBSServiceFacilityClientConfiguring"
- "FBSServiceFacilityClientMessaging"
- "FBSSettings"
- "FBSSettingsDiff"
- "FBSSettingsDiffInspector"
- "FBSSettingsExtension"
- "FBSSettingsSubclass"
- "FBSShutdownOptions"
- "FBSSignatureValidationService"
- "FBSSystemAppProxy"
- "FBSSystemService"
- "FBSSystemServiceSpecification"
- "FBSUIApplicationLayoutElement"
- "FBSWorkspace"
- "FBSWorkspaceCoupler"
- "FBSWorkspaceCreateSceneResponse"
- "FBSWorkspaceDestroySceneResponse"
- "FBSWorkspaceInitializationOptions"
- "FBSWorkspaceResponse"
- "FBSWorkspaceSceneRemnant"
- "FBSWorkspaceSceneRequestOptions"
- "FBSWorkspaceSceneUpdateResponse"
- "FBSWorkspaceScenesClientIdentifier"
- "FBSWorkspaceScenesSource"
- "FBSWorkspaceService"
- "FBSWorkspaceServiceClientInterface"
- "FBSWorkspaceServiceServerInterface"
- "FBSWorkspaceServiceSpecification"
- "FBSWorkspaceServiceTarget"
- "FBSXPCMessage"
- "Failed to verify universal provisioning profile %{public}@ with error %lld"
- "FrontBoardServices"
- "GenericReboot"
- "GenericShutdown"
- "I"
- "I16@0:8"
- "I24@0:8@16"
- "IOSurface"
- "LPEMOption"
- "LSApplicationWorkspaceObserverProtocol"
- "Legacy and modern states were divergent - legacy: %@, modern: %@"
- "Loaded profiles after %.2fs: %{public}@"
- "LocalProvision"
- "MCManagedAppsChangedNotification"
- "MCProfileConnection"
- "MISAppApprovalState"
- "MISEnumerateInstalledProvisioningProfiles"
- "MISError soft_MISEnumerateInstalledProvisioningProfiles(CFOptionFlags, _Bool (^__strong)(MISProfileRef))"
- "MISProfileGetValue"
- "MISProvisioningProfileGetDeveloperCertificates"
- "MISProvisioningProfileGetEntitlements"
- "MISProvisioningProfileGetExpirationDate"
- "MISProvisioningProfileGetUUID"
- "MISProvisioningProfileGrantsEntitlement"
- "MISProvisioningProfileIsAppleInternalProfile"
- "MISProvisioningProfileProvisionsAllDevices"
- "MISQueryBlacklistForBundle"
- "MISQueryBlacklistForCdHash"
- "MISState soft_MISAppApprovalState(CFStringRef, CFDictionaryRef)"
- "MISValidateUPP"
- "ManagedConfigurationSoftLinking.m"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "NSStringFromLSInstallPhase:"
- "NSStringFromLSInstallState:"
- "NSStringFromLSInstallType:"
- "No profiles loaded."
- "Q16@0:8"
- "Q24@0:8@\"FBSApplicationInfo\"16"
- "Q24@0:8@16"
- "RVv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "RVv48@0:8@16@24@32@?40"
- "Reloading provisioning profiles..."
- "S16@0:8"
- "SecCertificateCopySubjectSummary"
- "SecCertificateCreateWithData"
- "SecCertificateRef soft_SecCertificateCreateWithData(CFAllocatorRef, CFDataRef)"
- "SecuritySoftLinking.m"
- "SynchronousLocalSupport"
- "T#,&,N,V_applicationInfoClass"
- "T#,&,N,V_applicationPlaceholderClass"
- "T#,N,V_applicationInfoSubclass"
- "T#,R"
- "T#,R,N"
- "T@\"<FBSApplicationIdentifying>\",R,N,V_identifier"
- "T@\"<FBSApplicationPlaceholderProgress>\",R,N"
- "T@\"<FBSDisplayObserving>\",R,W,N"
- "T@\"<FBSDisplayTransformer>\",R,N,V_transformer"
- "T@\"<FBSProcess>\",R,W,N,V_process"
- "T@\"<FBSProcess>\",W,N,V_process"
- "T@\"<FBSProcessExecutionProvisionDelegate>\",W,N,V_delegate"
- "T@\"<FBSProcessInternal>\",R,W,N,V_process"
- "T@\"<FBSSceneDelegate>\",W,N"
- "T@\"<FBSSceneHandle>\",R,W,N,V_scene"
- "T@\"<FBSSceneHandle>\",W,N,V_scene"
- "T@\"<FBSSceneSnapshotRequestDelegate>\",W,N,V_delegate"
- "T@\"<FBSSceneUpdater>\",R,N,V_lock_updater"
- "T@\"<FBSWorkspaceDelegate>\",R,N"
- "T@\"<FBSWorkspaceDelegate>\",R,N,V_delegate"
- "T@\"<FBSceneClientProcess>\",&,D,N"
- "T@\"<FBSceneClientProcess>\",?,&,N"
- "T@\"<NSCopying>\",W,N,V_localContext"
- "T@\"BKSAnimationFenceHandle\",&,D,N"
- "T@\"BKSAnimationFenceHandle\",&,N"
- "T@\"BKSProcessAssertion\",R,N,V_assertion"
- "T@\"BSAnimationSettings\",C,D,N"
- "T@\"BSAnimationSettings\",C,N"
- "T@\"BSAuditToken\",R,N"
- "T@\"BSAuditToken\",R,N,V_auditToken"
- "T@\"BSKeyedSettings\",&,N"
- "T@\"BSKeyedSettings\",?,&,D,N"
- "T@\"BSKeyedSettings\",?,&,N"
- "T@\"BSMachPortTaskNameRight\",R,&,N"
- "T@\"BSMachPortTaskNameRight\",R,&,N,V_taskNameRight"
- "T@\"BSMutableKeyedSettings\",R,C,N,V_payload"
- "T@\"BSMutableSettings\",R,C,N,V_otherSettings"
- "T@\"BSProcessHandle\",&,D,N"
- "T@\"BSProcessHandle\",&,N"
- "T@\"BSProcessHandle\",R,&,N"
- "T@\"BSServiceConnectionEndpoint\",R,C,N"
- "T@\"BSServiceConnectionEndpoint\",R,C,N,V_endpoint"
- "T@\"BSServiceConnectionEndpoint\",R,N"
- "T@\"BSServiceConnectionEndpoint\",R,N,V_defaultShellEndpoint"
- "T@\"BSServiceDispatchQueue\",R,N"
- "T@\"BSServiceInterface\",R,C,N"
- "T@\"BSServiceQuality\",R,C,N"
- "T@\"BSServiceQuality\",R,N,V_serviceQuality"
- "T@\"BSServiceQueue\",&,N,V_callOutQueue"
- "T@\"BSServiceQueue\",R,N"
- "T@\"BSServiceQueue\",R,N,V_queue"
- "T@\"BSSettings\",C,N,V_clientExtendedData"
- "T@\"BSSettings\",R,C,N"
- "T@\"CAContext\",R,D,N"
- "T@\"CAContext\",R,N"
- "T@\"FBProcessExecutionContext\",?,&,D,N"
- "T@\"FBProcessExecutionContext\",?,&,N"
- "T@\"FBSApplicationLibrary\",W,N,V_appLibrary"
- "T@\"FBSApplicationPlaceholder\",R,W,N,V_placeholder"
- "T@\"FBSDisplayConfiguration\",&,N,V_displayConfiguration"
- "T@\"FBSDisplayConfiguration\",C,N"
- "T@\"FBSDisplayConfiguration\",R,C,D,N"
- "T@\"FBSDisplayConfiguration\",R,C,N"
- "T@\"FBSDisplayConfiguration\",R,C,N,V_noEqual_originatingConfiguration"
- "T@\"FBSDisplayConfiguration\",R,N,V_displayConfiguration"
- "T@\"FBSDisplayIdentity\",R,C,N"
- "T@\"FBSDisplayIdentity\",R,C,N,V_identity"
- "T@\"FBSDisplayLayout\",R,N"
- "T@\"FBSDisplayMode\",R,C,N"
- "T@\"FBSDisplayMode\",R,C,N,V_currentMode"
- "T@\"FBSMutableSceneParameters\",R,N,V_parameters"
- "T@\"FBSProcessExecutionPolicy\",C,N,V_executionPolicy"
- "T@\"FBSProcessExecutionPolicy\",R,N,V_policy"
- "T@\"FBSProcessExecutionStrategy\",C,N,V_strategy"
- "T@\"FBSProcessWatchdogPolicy\",R,C,N,V_policy"
- "T@\"FBSScene\",&,N,V_scene"
- "T@\"FBSSceneClientIdentity\",C,D,N"
- "T@\"FBSSceneClientIdentity\",C,N,V_clientIdentity"
- "T@\"FBSSceneClientSettings\",C,D,N"
- "T@\"FBSSceneClientSettings\",C,N,V_clientSettings"
- "T@\"FBSSceneClientSettings\",C,N,V_initialClientSettings"
- "T@\"FBSSceneClientSettings\",R,N"
- "T@\"FBSSceneClientSettingsDiff\",&,N,V_clientSettingsDiff"
- "T@\"FBSSceneDefinition\",R,N,V_definition"
- "T@\"FBSSceneHostHandle\",R,N"
- "T@\"FBSSceneIdentity\",C,D,N"
- "T@\"FBSSceneIdentity\",C,N,V_identity"
- "T@\"FBSSceneIdentity\",R,C,N,V_identity"
- "T@\"FBSSceneIdentity\",R,N,V_identity"
- "T@\"FBSSceneIdentityToken\",C,D,N"
- "T@\"FBSSceneIdentityToken\",C,N"
- "T@\"FBSSceneIdentityToken\",R,C,D,N"
- "T@\"FBSSceneIdentityToken\",R,D,N"
- "T@\"FBSSceneIdentityToken\",R,N"
- "T@\"FBSSceneIdentityToken\",R,N,V_identityToken"
- "T@\"FBSSceneMessage\",C,N,V_message"
- "T@\"FBSSceneParameters\",R,C,N,V_parameters"
- "T@\"FBSSceneSettings\",&,N,V_initialSettings"
- "T@\"FBSSceneSettings\",C,D,N"
- "T@\"FBSSceneSettings\",C,N,V_settings"
- "T@\"FBSSceneSettings\",R,C,N,V_settings"
- "T@\"FBSSceneSettings\",R,N"
- "T@\"FBSSceneSettingsDiff\",&,N,V_settingsDiff"
- "T@\"FBSSceneSnapshotContext\",R,N"
- "T@\"FBSSceneSpecification\",C,D,N"
- "T@\"FBSSceneSpecification\",C,D,N,S_setSpecification:"
- "T@\"FBSSceneSpecification\",C,N,V_specification"
- "T@\"FBSSceneSpecification\",R,C,N,V_specification"
- "T@\"FBSSceneSpecification\",R,N"
- "T@\"FBSSceneSpecification\",R,N,V_specification"
- "T@\"FBSSceneTransitionContext\",&,N,V_transitionContext"
- "T@\"FBSSceneTransitionContext\",C,D,N"
- "T@\"FBSSceneUpdate\",?,&,D,N"
- "T@\"FBSSceneUpdate\",?,&,N"
- "T@\"FBSSettings<FBSMutableSettings>\",C,D,N"
- "T@\"FBSSettingsDiff\",C,D,N"
- "T@\"FBSWorkspaceService\",R,N"
- "T@\"FBSceneUpdateContext\",?,&,D,N"
- "T@\"FBSceneUpdateContext\",?,&,N"
- "T@\"FBWatchdogTransitionContext\",?,&,D,N"
- "T@\"FBWatchdogTransitionContext\",?,&,N"
- "T@\"IOSurface\",R,N"
- "T@\"LSApplicationIdentity\",R,C,N,V_applicationIdentity"
- "T@\"LSApplicationIdentity\",R,N,V_identity"
- "T@\"LSApplicationProxy\",&,N,G_proxy,S_setProxy:"
- "T@\"NSArray\",&,N,V_prefetchedKeys"
- "T@\"NSArray\",?,C,D,N"
- "T@\"NSArray\",?,C,N"
- "T@\"NSArray\",C,N,V_provisions"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_elements"
- "T@\"NSArray\",R,N,V_customMachServices"
- "T@\"NSArray\",R,N,V_deviceFamilies"
- "T@\"NSArray\",R,N,V_externalAccessoryProtocols"
- "T@\"NSArray\",R,N,V_requiredCapabilities"
- "T@\"NSArray\",R,N,V_tags"
- "T@\"NSBundle\",R,N"
- "T@\"NSData\",R,N,V_cachedCodeDirectoryHash"
- "T@\"NSDate\",R,N,V_expirationDate"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSDictionary\",C,N,V_payload"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_environmentVariables"
- "T@\"NSError\",&,D,N"
- "T@\"NSError\",?,&,N"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSNumber\",R,N,V_downloaderDSID"
- "T@\"NSNumber\",R,N,V_itemID"
- "T@\"NSNumber\",R,N,V_purchaserDSID"
- "T@\"NSObject<NSCopying>\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_callOutQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_calloutQueue"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_payload"
- "T@\"NSOrderedSet\",C,D,N"
- "T@\"NSOrderedSet\",R,C,D,N"
- "T@\"NSOrderedSet\",R,N,V_layers"
- "T@\"NSSet\",C,D,N"
- "T@\"NSSet\",C,N"
- "T@\"NSSet\",C,N,V_layersToExclude"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,C,N,V_availableModes"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_domainIdentifier"
- "T@\"NSString\",C,N,V_explanation"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_instanceIdentifier"
- "T@\"NSString\",C,N,V_label"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_reason"
- "T@\"NSString\",C,N,V_sceneID"
- "T@\"NSString\",C,N,V_strategyName"
- "T@\"NSString\",C,N,V_workspaceIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,D,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,G_appIDEntitlement,V_appIDEntitlement"
- "T@\"NSString\",R,C,N,V_UUID"
- "T@\"NSString\",R,C,N,V_bundleID"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_bundleType"
- "T@\"NSString\",R,C,N,V_bundleVersion"
- "T@\"NSString\",R,C,N,V_deviceName"
- "T@\"NSString\",R,C,N,V_displayName"
- "T@\"NSString\",R,C,N,V_extensionIdentifier"
- "T@\"NSString\",R,C,N,V_hardwareIdentifier"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_preferenceDomain"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSString\",R,C,N,V_sceneID"
- "T@\"NSString\",R,C,N,V_sdkVersion"
- "T@\"NSString\",R,C,N,V_shortVersionString"
- "T@\"NSString\",R,C,N,V_signerIdentity"
- "T@\"NSString\",R,C,N,V_stringRepresentation"
- "T@\"NSString\",R,C,N,V_typeIdentifier"
- "T@\"NSString\",R,C,N,V_workspaceIdentifier"
- "T@\"NSString\",R,N,V_bundleId"
- "T@\"NSString\",R,N,V_teamIdentifier"
- "T@\"NSURL\",R,C,N,V_advertisingAttributionReportEndpoint"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_bundleContainerURL"
- "T@\"NSURL\",R,N,V_bundleURL"
- "T@\"NSURL\",R,N,V_dataContainerURL"
- "T@\"NSURL\",R,N,V_executableURL"
- "T@\"NSURL\",R,N,V_sandboxURL"
- "T@\"NSUUID\",R,C,N,V_cacheGUID"
- "T@\"RBSProcessHandle\",?,&,D,N"
- "T@\"RBSProcessHandle\",?,&,N"
- "T@\"RBSProcessIdentity\",R,&,N"
- "T@\"RBSProcessIdentity\",R,C,N,V_processIdentity"
- "T@\"_FBSCDHashCacheInfo\",&"
- "T@\"_FBSSnapshotContext\",R,C,N,V_context"
- "T@?,C,D,N"
- "T@?,C,N"
- "T@?,C,N,V_applicationIdentityFilter"
- "T@?,C,N,V_completion"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_installedApplicationFilter"
- "T@?,C,N,V_placeholderFilter"
- "T@?,C,N,V_placeholderIdentityFilter"
- "T@?,C,N,V_requestHandler"
- "T@?,C,N,V_transitionHandler"
- "TB,?,D,N"
- "TB,?,D,N,GisRunningBoardAssertionDisabled"
- "TB,?,N"
- "TB,?,N,GisRunningBoardAssertionDisabled"
- "TB,D,N"
- "TB,D,N,GisBackgrounded"
- "TB,D,N,GisBarrier"
- "TB,D,N,GisClientFuture"
- "TB,D,N,GisForeground"
- "TB,D,N,GisOccluded"
- "TB,N,G_isInstalling,S_setInstalling:,V_installing"
- "TB,N,G_isPendingUninstall,S_setPendingUninstall:,V_pendingUninstall"
- "TB,N,G_isTentativeUninstall,S_setTentativeUninstall:,V_tentativeUninstall"
- "TB,N,G_isUninstalling,S_setUninstalling:,V_uninstalling"
- "TB,N,GisBarrier"
- "TB,N,GisClientFuture"
- "TB,N,GisClientFuture,V_clientFuture"
- "TB,N,GisCustomPolicy,V_customPolicy"
- "TB,N,GisDefaultShellEndpointEnabled,V_defaultShellEndpointEnabled"
- "TB,N,GisEndpointMonitoringEnabled,V_endpointMonitoringEnabled"
- "TB,N,GisForeground"
- "TB,N,GisKeyboardScene,V_keyboardScene"
- "TB,N,GisOccluded"
- "TB,N,GisOpaque,V_opaque"
- "TB,N,GisPersonaAware,V_personaAware"
- "TB,N,GisUIApplicationElement,V_application"
- "TB,N,GisUserInitiated,V_userInitiated"
- "TB,N,V_allowConcurrentLoading"
- "TB,N,V_allowsProtectedContent"
- "TB,N,V_authoritative"
- "TB,N,V_fillsDisplayBounds"
- "TB,N,V_keyboardFocus"
- "TB,N,V_needsUserInteractivePriority"
- "TB,N,V_showsArchiveOption"
- "TB,R"
- "TB,R,D,GisExpired"
- "TB,R,D,N,GisForeground"
- "TB,R,D,N,GisStarted"
- "TB,R,N"
- "TB,R,N,G_forceIsD22ChecksToPass"
- "TB,R,N,GisActivated"
- "TB,R,N,GisAppleInternalProfile,V_appleInternalProfile"
- "TB,R,N,GisBackgrounded"
- "TB,R,N,GisBeta,V_beta"
- "TB,R,N,GisBlocked,V_blocked"
- "TB,R,N,GisBlockedForScreenTimeExpiration"
- "TB,R,N,GisCancellable"
- "TB,R,N,GisCarDisplay"
- "TB,R,N,GisCarInstrumentsDisplay"
- "TB,R,N,GisCloningSupported,V_cloningSupported"
- "TB,R,N,GisConfigured,V_configured"
- "TB,R,N,GisEmulatedDevice"
- "TB,R,N,GisEnabled,V_enabled"
- "TB,R,N,GisExitsOnSuspend"
- "TB,R,N,GisExternal"
- "TB,R,N,GisExternal,V_external"
- "TB,R,N,GisFreeDeveloperProfile,V_freeDeveloperProfile"
- "TB,R,N,GisFreeDeveloperProvisioningProfileValidated,V_freeDeveloperProvisioningProfileValidated"
- "TB,R,N,GisInvalidated,V_invalidated"
- "TB,R,N,GisLocal,V_local"
- "TB,R,N,GisMainDisplay"
- "TB,R,N,GisMonitoring,V_monitoring"
- "TB,R,N,GisOpen,V_open"
- "TB,R,N,GisOverscanned,V_overscanned"
- "TB,R,N,GisPausable"
- "TB,R,N,GisPrioritizable"
- "TB,R,N,GisProvisioningProfileValidated,V_provisioningProfileValidated"
- "TB,R,N,GisRestricted,V_restricted"
- "TB,R,N,GisResumable"
- "TB,R,N,GisRunning"
- "TB,R,N,GisTransitioning"
- "TB,R,N,GisUIApplicationElement"
- "TB,R,N,GisUIKitMainLike"
- "TB,R,N,GisUIKitMainLike,V_mainLike"
- "TB,R,N,GisUPPProvisioningProfileValidated,V_uppProvisioningProfileValidated"
- "TB,R,N,GisUsingNetwork"
- "TB,R,N,GisViolated,V_violated"
- "TB,R,N,GwasBuiltWithTSAN,V_builtWithTSAN"
- "TB,R,N,V_allowsProtectedContent"
- "TB,R,N,V_direct"
- "TB,R,N,V_disableFrameDoubling"
- "TB,R,N,V_everActivated"
- "TB,R,N,V_hasViewServicesEntitlement"
- "TB,R,N,V_provisionsAllDevices"
- "TB,R,N,V_requiresPersistentWiFi"
- "TB,R,N,V_supportsMultiwindow"
- "TI,D,N"
- "TI,N,V_bksFlags"
- "TI,N,V_bksReason"
- "TI,R,D,N"
- "TI,R,N"
- "TI,R,N,V_cachedCodeDirectoryHashType"
- "TI,R,N,V_contextID"
- "TI,R,N,V_noEqual_seed"
- "TQ,N,V_options"
- "TQ,N,V_sequenceNumber"
- "TQ,N,V_supportedInterfaceOrientations"
- "TQ,R"
- "TQ,R,D,N"
- "TQ,R,N"
- "TQ,R,N,V_activationCount"
- "TQ,R,N,V_expectedFinalInstallPhase"
- "TQ,R,N,V_installPhase"
- "TQ,R,N,V_installState"
- "TQ,R,N,V_sequenceNumber"
- "TQ,R,N,V_type"
- "TS,D,N"
- "TS,N"
- "TS,R,D,N"
- "T^{CGImage=},R,N"
- "Tc,?,N"
- "Tc,D,N"
- "Tc,R,N"
- "Td,D,N"
- "Td,N"
- "Td,N,V_duration"
- "Td,N,V_expirationInterval"
- "Td,N,V_scale"
- "Td,R,D,N"
- "Td,R,N"
- "Td,R,N,V_lastModifiedDate"
- "Td,R,N,V_latency"
- "Td,R,N,V_percentComplete"
- "Td,R,N,V_pointScale"
- "Td,R,N,V_refreshRate"
- "Tf,R,N,V_minimumBrightnessLevel"
- "Ti,D,N"
- "Ti,R,N"
- "Ti,R,N,V_pid"
- "Ti,R,N,V_subtype"
- "Ti,R,N,V_type"
- "Tq,D,N"
- "Tq,N"
- "Tq,N,V_LPEMOption"
- "Tq,N,V_backlightLevel"
- "Tq,N,V_backlightState"
- "Tq,N,V_exceptionCode"
- "Tq,N,V_graphicsPolicy"
- "Tq,N,V_interfaceOrientation"
- "Tq,N,V_jetsamPolicy"
- "Tq,N,V_level"
- "Tq,N,V_mode"
- "Tq,N,V_options"
- "Tq,N,V_orientation"
- "Tq,N,V_rebootType"
- "Tq,N,V_reportType"
- "Tq,N,V_rotationDirection"
- "Tq,N,V_schedulingPolicy"
- "Tq,N,V_source"
- "Tq,R,D,N"
- "Tq,R,N"
- "Tq,R,N,V_gamut"
- "Tq,R,N,V_hdr"
- "Tq,R,N,V_hdrMode"
- "Tq,R,N,V_overscanCompensation"
- "Tq,R,N,V_ratingRank"
- "Tq,R,N,V_screenTimePolicy"
- "Tq,R,N,V_state"
- "Tq,R,N,V_tags"
- "Trust"
- "TrustCDHashCache"
- "T{?=qQQ},N,V_allowance"
- "T{CATransform3D=dddddddddddddddd},R,N,V_baseTransform"
- "T{CGPoint=dd},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},D,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds"
- "T{CGSize=dd},D,N"
- "T{CGSize=dd},N,V_snapshotSize"
- "T{CGSize=dd},R,N"
- "T{CGSize=dd},R,N,V_logicalScale"
- "T{CGSize=dd},R,N,V_nativePixelSize"
- "T{CGSize=dd},R,N,V_pixelSize"
- "T{CGSize=dd},R,N,V_safeOverscanRatio"
- "UIApplicationElement"
- "UIBackgroundModes"
- "UIKitMainLike"
- "UPPProvisioningProfileValidated"
- "UPPValidated"
- "URLHostAllowedCharacterSet"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unable to connect to endpoint : %@"
- "Vv16@0:8"
- "Vv24@0:8@\"FBSOrientationUpdate\"16"
- "Vv24@0:8@\"FBSSceneTransitionContext\"16"
- "Vv24@0:8@\"NSSet<__FBSWorkspaceSceneRemnant__>\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">16"
- "Vv32@0:8@\"FBSWorkspaceSceneRequestOptions\"16@?<v@?@\"FBSSceneIdentity\"@\"NSError\">24"
- "Vv32@0:8@\"FBSWorkspaceSceneRequestOptions\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSNumber\"16@?<v@?@\"FBSOrientationUpdate\"@\"NSError\">24"
- "Vv32@0:8@\"NSObject<OS_xpc_object>\"16@\"NSObject<OS_xpc_object>\"24"
- "Vv32@0:8@\"NSSet<__BSAction__>\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSInvocation\"24@?<v@?@\"FBSInvocationReply\"@\"NSError\">32"
- "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\"@\"NSError\">32"
- "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneTransitionContext\"24@\"NSError\"32"
- "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneTransitionContext\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32"
- "Vv40@0:8@\"NSString\"16@\"NSSet<__BSAction__>\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@16@24@32"
- "Vv40@0:8@16@24@?32"
- "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneParameters<__nonnull__>\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"FBSSceneSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@\"FBSSceneIdentity<__nonnull__>\"16@\"NSSet<__BSAction__>\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "Vv48@0:8@16@24@32@?40"
- "Vv56@0:8@\"NSString\"16@\"FBSOpenApplicationOptions\"24@\"BSProcessHandle\"32@\"NSString\"40@?<v@?@\"BSProcessHandle\"@\"NSError\">48"
- "Vv56@0:8@16@24@32@40@?48"
- "[%@] Adding extension: \"%@\""
- "[3@\"BSServiceDispatchQueue\"]"
- "[3@\"NSMutableSet\"]"
- "[3@\"NSObject<OS_xpc_object>\"]"
- "[3@\"_FBSDisplayLayoutService\"]"
- "[3Q]"
- "[_bs_assert_object isKindOfClass:BSServiceConnectionClass]"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_Bool soft_MISQueryBlacklistForBundle(CFStringRef _Nonnull, off_t, _Bool, struct MISBlacklistFlags * _Nullable, CFDataRef  _Nullable * _Nullable, MISBlacklistHashType * _Nullable, CFDictionaryRef  _Nullable const)"
- "_Bool soft_MISQueryBlacklistForCdHash(CFDataRef  _Nonnull const, MISBlacklistHashType, _Bool, struct MISBlacklistFlags * _Nullable, CFDictionaryRef  _Nullable const)"
- "_FBSCDHashCacheInfo"
- "_FBSCapturedSceneLayer"
- "_FBSDisplayLayoutEndpointServices"
- "_FBSDisplayLayoutService"
- "_FBSDisplayLayoutServiceAssertion"
- "_FBSMISInterfaceWrapper"
- "_FBSMISInterfaceWrapperImpl"
- "_FBSScenesClientHostEvent"
- "_FBSSnapshot"
- "_FBSSnapshotContext"
- "_FBSSnapshotLayer"
- "_FBSTestExitAction"
- "_LPEMOption"
- "_LSDescription"
- "_UUID"
- "_actionHandler"
- "_actions"
- "_activated"
- "_activationCount"
- "_active"
- "_addCompletions:"
- "_addElement:forKey:"
- "_addSceneExtension:"
- "_addSceneExtension:applyingSettings:"
- "_advertisingAttributionReportEndpoint"
- "_alignment"
- "_allPrefetchedChangesInFlightForApplication:"
- "_allSceneExtensions"
- "_allowConcurrentLoading"
- "_allowance"
- "_allowedApplicationIdentifierEntitlement"
- "_allowsProtectedContent"
- "_alwaysConnected"
- "_appIDEntitlement"
- "_appInfo"
- "_appLibrary"
- "_appendToDescriptionBuilder:"
- "_appleInternalProfile"
- "_application"
- "_applicationIdentity"
- "_applicationIdentityFilter"
- "_applicationInfoClass"
- "_applicationInfoSubclass"
- "_applicationPlaceholderClass"
- "_applicationTypeForProxy:"
- "_applicationTypeForRecord:"
- "_applicationWorkspace"
- "_applySafeValuesFromUntrustedSettings:"
- "_applySettings:"
- "_assertion"
- "_assertionState"
- "_auditToken"
- "_authoritative"
- "_authoritativeProvider"
- "_availableModes"
- "_backgroundModes"
- "_backlightLevel"
- "_backlightState"
- "_baseClass"
- "_baseTransform"
- "_baselineValue"
- "_beginMonitoring"
- "_beginMonitoringConstraints"
- "_beginUpdate"
- "_beta"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_bksFlags"
- "_bksReason"
- "_blocked"
- "_bounds"
- "_builtWithTSAN"
- "_bundleContainerURL"
- "_bundleID"
- "_bundleId"
- "_bundleIdentifier"
- "_bundleType"
- "_bundleURL"
- "_bundleVersion"
- "_cTypeString"
- "_caColorGamut"
- "_caDisplay"
- "_caHDRMode"
- "_caHeight"
- "_caPreferredScale"
- "_caRefreshRate"
- "_caWidth"
- "_cacheGUID"
- "_cachedCodeDirectoryHash"
- "_cachedCodeDirectoryHashType"
- "_callOutQueue"
- "_callOutQueue_agent"
- "_callOutQueue_agentMessageHandler"
- "_callOutQueue_agentSessions"
- "_callOutQueue_didCreateWithTransitionContext:alternativeCreationCallout:completion:"
- "_callOutQueue_didUpdateHostHandle:"
- "_callOutQueue_ensureCoalesceClientSettingsUpdates:"
- "_callOutQueue_invalidate"
- "_callOutQueue_maybeCoalesceClientSettingsUpdates:"
- "_callOutQueue_mutationLocked"
- "_callOutQueue_sendDidCreateForScene:transitionContext:completion:"
- "_callOutQueue_updateExtensionsFromSettings:toSettings:withDiff:"
- "_callOutQueue_willDestroyWithTransitionContext:completion:"
- "_callbackQueue"
- "_callback_queue"
- "_calloutQueue"
- "_calloutQueue_animationFence"
- "_calloutQueue_executeCalloutFromSource:withBlock:"
- "_calloutQueue_handleStoreInvalidated:"
- "_calloutQueue_handleValueChanged:"
- "_callout_coalesceUpdates"
- "_callout_sceneUpdate"
- "_callout_updateDepth"
- "_canPerformAction:"
- "_cancelWithResult:"
- "_canceled"
- "_cancellationAllowed"
- "_captureTime"
- "_changedLegacySettings"
- "_changedSettings"
- "_checkinService:"
- "_checkoutCount"
- "_checkoutServiceWithEndpoint:qos:"
- "_class"
- "_classForObjectAtArgumentIndex:"
- "_clearAction"
- "_client"
- "_clientExtendedData"
- "_clientFuture"
- "_clientIdentity"
- "_clientNeedsCheckin"
- "_clientSettings"
- "_clientSettingsByIdentity"
- "_clientSettingsDiff"
- "_clients"
- "_clients_immutable"
- "_clients_immutable_lock"
- "_clintSettingsHandler"
- "_cloningSupported"
- "_completion"
- "_completionHandler"
- "_completionQueue"
- "_completions"
- "_component"
- "_configOnly_interfaceTarget"
- "_configuration"
- "_configureConnection:"
- "_configureEnvironment:withInfo:isPreApex:"
- "_configureParameters:"
- "_configureWithScene:"
- "_configured"
- "_connection"
- "_connectionActivated:"
- "_connectionEndpointMonitor"
- "_connectionInterrupted:"
- "_connectionInvalidated:"
- "_connectionSeed"
- "_connectionType"
- "_consumedValue"
- "_containsAnySettingNamed:"
- "_containsKey:"
- "_containsSetting:"
- "_contextID"
- "_copyClearingProgenitor:"
- "_copyWithOverrideSize:"
- "_copyWithOverrideSize:scale:"
- "_copyWithOverrideSize:scale:refreshRate:"
- "_count"
- "_counterpartClass"
- "_createReplyBlockWithSignature:arguments:handler:"
- "_createSceneWithIdentity:parameters:"
- "_createTransitionContext"
- "_currentLayout"
- "_currentMode"
- "_customMachServices"
- "_customPolicy"
- "_dataContainerURL"
- "_defaultOpenApplicationService"
- "_defaultShellEndpoint"
- "_defaultShellEndpointEnabled"
- "_defaultValue"
- "_definition"
- "_delegate"
- "_delegateCalloutQueue"
- "_deprecated_displayType"
- "_deprecated_endpoint"
- "_deprecated_mutable"
- "_deprecated_qos"
- "_deprecated_singleton"
- "_description"
- "_descriptionProvider"
- "_deviceFamilies"
- "_deviceName"
- "_diff"
- "_diffClass"
- "_direct"
- "_dirty"
- "_disableFrameDoubling"
- "_dispatchToObserversWithBlock:"
- "_display"
- "_displayConfiguration"
- "_displayID"
- "_displayName"
- "_doInvalidate"
- "_doWithClassClient:"
- "_domainIdentifier"
- "_downloaderDSID"
- "_duration"
- "_elements"
- "_emptyMode"
- "_enabled"
- "_endSuppression"
- "_endTransition"
- "_endpoint"
- "_endpointForDisplayType:"
- "_endpointMonitoringEnabled"
- "_enqueueClientConnectionBlock:"
- "_environmentVariables"
- "_error"
- "_errorHandler"
- "_everActivated"
- "_evlock_attachment"
- "_evlock_rawConfiguration"
- "_evlock_reportedEffectiveConfigurations"
- "_evlock_reportedRawConfiguration"
- "_exceptionCode"
- "_executableURL"
- "_executeCalloutFromHostEvent:withBlock:"
- "_executeNextRequest"
- "_executionPolicy"
- "_expectedClass"
- "_expectedFinalInstallPhase"
- "_expirationDate"
- "_expirationInterval"
- "_expired"
- "_explanation"
- "_extension"
- "_extensionID"
- "_extensionIdentifier"
- "_external"
- "_externalAccessoryProtocols"
- "_externallyVisibleLock"
- "_facilityID"
- "_fillsDisplayBounds"
- "_findDomainSpecification"
- "_finishAllRequests"
- "_finishInitializing"
- "_forceIsD22ChecksToPass"
- "_frame"
- "_frameworkNameLoadingIfNeeded:"
- "_freeDeveloperProfile"
- "_freeDeveloperProvisioningProfileValidated"
- "_gamut"
- "_getAndSetFreshestUpdateGivenUpdate:forced:"
- "_graphicsPolicy"
- "_handle"
- "_handleConnect:"
- "_handleTerminationReply:targetDescription:withCompletion:"
- "_handled"
- "_handler"
- "_handshakeLock"
- "_handshakeLock_remoteTarget"
- "_hardwareIdentifier"
- "_hasAdditionalDescription"
- "_hasAgent"
- "_hasAnySceneExtension"
- "_hasFreeDeveloperProvisioningProfile"
- "_hasObserver:"
- "_hasUniversalProvisioningProfile"
- "_hasViewServicesEntitlement"
- "_hdr"
- "_hdrMode"
- "_height"
- "_host"
- "_hostEndpoint"
- "_hostEventLock"
- "_hostEvent_pendingEvents"
- "_hostHandle"
- "_identifier"
- "_identitiesForProxy:outRecord:"
- "_identityToken"
- "_ignoreOcclusionReasons"
- "_imageRef"
- "_immutableCADisplay"
- "_indirect_isEmpty"
- "_init"
- "_initForCurrentProcess"
- "_initWithApplicationProxy:identity:"
- "_initWithApplicationProxy:record:appIdentity:processIdentity:overrideURL:"
- "_initWithApplicationWorkspace:configuration:"
- "_initWithBookendObserver:transformer:"
- "_initWithBundleId:identity:client:"
- "_initWithBundleIdentifier:url:"
- "_initWithBundleProxy:bundleIdentifier:url:"
- "_initWithBundleProxy:overrideURL:"
- "_initWithBundleProxy:url:"
- "_initWithCADisplayMode:scale:rotation:"
- "_initWithCallOutQueue:"
- "_initWithClient:callbackQueue:"
- "_initWithConfiguration:"
- "_initWithConfiguration:singleton:needsDefaultPriority:mutable:displayType:mutableHandler:"
- "_initWithCoupler:options:"
- "_initWithDelegate:"
- "_initWithDomain:"
- "_initWithElements:"
- "_initWithEndpoint:"
- "_initWithEndpoint:calloutQueue:delegate:"
- "_initWithEndpoint:qos:"
- "_initWithHost:endpoint:target:workspace:identifier:"
- "_initWithIdentifier:connection:queue:calloutQueue:workspace:"
- "_initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:latency:originatingConfiguration:validityCheck:"
- "_initWithIdentity:parameters:"
- "_initWithImmutableDisplay:originalDisplay:assertIfInvalid:"
- "_initWithLayer:"
- "_initWithLocal:direct:identity:description:"
- "_initWithMISInterfaceWrapper:"
- "_initWithPayload:"
- "_initWithPlugInKitProxy:"
- "_initWithSerialQueue:"
- "_initWithTarget:identifier:"
- "_initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:root:"
- "_initWithType:context:responder:"
- "_initWithUpdater:identityToken:identity:parameters:hostHandle:"
- "_initWithWidth:height:preferredScale:scaleOverride:refreshRate:gamut:hdr:rotation:virtual:validityCheck:"
- "_initWithWidth:height:scale:refreshRate:gamut:hdr:"
- "_initialClientSettings"
- "_initialSettings"
- "_initializeProfiles:"
- "_initialized"
- "_installPhase"
- "_installState"
- "_installType"
- "_installedApplicationFilter"
- "_installing"
- "_instanceID"
- "_instanceIdentifier"
- "_instigatingUpdate"
- "_interface"
- "_interfaceOrientation"
- "_internalWorkspaceIdentifier"
- "_invalid"
- "_invalidateWithCompletion:"
- "_invalidated"
- "_invalidatedSignal"
- "_invalidationHandler"
- "_invokeWithTarget:loggingID:replyHandler:"
- "_invoked"
- "_isBSSettings"
- "_isChangeInFlightForPrefetchedKey:application:"
- "_isEmptyForCoding:"
- "_isEmulatedDeviceViaDefaults"
- "_isEmulatedDeviceViaGestalt"
- "_isEqualToSettings:"
- "_isInstalling"
- "_isManaged"
- "_isPendingUninstall"
- "_isSharedInstance"
- "_isSignifcant"
- "_isSignificantTransitionContext:"
- "_isSingleton"
- "_isTentativeUninstall"
- "_isUninstalling"
- "_isValid"
- "_isVirtualMode"
- "_itemID"
- "_iteratingObservers"
- "_jetsamPolicy"
- "_keyboardFocus"
- "_keyboardOwner"
- "_keyboardScene"
- "_label"
- "_lastModifiedDate"
- "_latency"
- "_layers"
- "_layersToExclude"
- "_lazy_entitlements"
- "_legacy"
- "_legacyDescriptionProvider"
- "_legacyDiff"
- "_legacyLocalDiff"
- "_legacyLocalSettings"
- "_legacyProvider"
- "_legacySetting"
- "_level"
- "_listener"
- "_loadFromProxy:"
- "_loadFromRecord:"
- "_local"
- "_localContext"
- "_localDiff"
- "_localSettings"
- "_lock"
- "_lock_activate"
- "_lock_activated"
- "_lock_allComponents"
- "_lock_allowsUnknown"
- "_lock_allowsUnknownDisplays"
- "_lock_attachment"
- "_lock_bookendObserver"
- "_lock_bounds"
- "_lock_canPostToBookendObserver"
- "_lock_clientConnectionBlocks"
- "_lock_clientSettings"
- "_lock_cloningSet"
- "_lock_cloningSupported"
- "_lock_components"
- "_lock_connection"
- "_lock_connectionDenied"
- "_lock_currentMode"
- "_lock_debounceToken"
- "_lock_delegate"
- "_lock_deprecated_handler"
- "_lock_deprecated_observerAssertions"
- "_lock_displayType"
- "_lock_displayTypeSet"
- "_lock_enumerateConnectedWithBlock:"
- "_lock_enumerateSourcesWithBlock:"
- "_lock_freshestUpdate"
- "_lock_geometrySet"
- "_lock_getAndSetFreshestUpdateGivenUpdate:forced:"
- "_lock_handler"
- "_lock_handlerAssertion"
- "_lock_hostHandle"
- "_lock_initialized"
- "_lock_interest"
- "_lock_invalidate"
- "_lock_invalidated"
- "_lock_keyedObservers"
- "_lock_layout"
- "_lock_layoutGeneration"
- "_lock_mainLike"
- "_lock_monitor"
- "_lock_nativeBounds"
- "_lock_noteConnected"
- "_lock_noteDisconnecting"
- "_lock_noteUpdatedForTransformInvalidation:"
- "_lock_observers"
- "_lock_otherModes"
- "_lock_overscanCompensation"
- "_lock_overscanSet"
- "_lock_overscanned"
- "_lock_pixelSize"
- "_lock_preferredMode"
- "_lock_rawConfiguration"
- "_lock_rawConfigurationOfLastTransition"
- "_lock_remoteTarget"
- "_lock_reportedEffectiveConfigurations"
- "_lock_reportedRawConfiguration"
- "_lock_safeOverscanRatio"
- "_lock_sanitizedModeForMode:"
- "_lock_sceneObservers"
- "_lock_secure"
- "_lock_service"
- "_lock_setHandler:"
- "_lock_setRawReportedConfiguration:effectiveReportedConfigurations:"
- "_lock_settings"
- "_lock_sourcesByDisplay"
- "_lock_uniqueIdentifier"
- "_lock_updater"
- "_lock_workspace"
- "_logTrustState:forApp:reason:"
- "_logicalScale"
- "_mainDisplay"
- "_mainDisplaySource"
- "_mainLike"
- "_managedAppsChangedNotification:"
- "_message"
- "_minimumBrightnessLevel"
- "_misInterfaceWrapper"
- "_mode"
- "_modernProvider"
- "_monitoring"
- "_mutable"
- "_mutableClass"
- "_mutableElementKeys"
- "_mutableLayout"
- "_mutableSettings"
- "_name"
- "_nameForDisplayType"
- "_nativeBounds"
- "_nativePixelSize"
- "_nativeRotation"
- "_needsCoW"
- "_needsUserInteractivePriority"
- "_noEqual_comparable"
- "_noEqual_originatingConfiguration"
- "_noEqual_seed"
- "_nonProtectedSurfaceRef"
- "_noteChangedSignificantly"
- "_noteDisconnected"
- "_noteViolatedWithError:"
- "_nullPreserving"
- "_objects"
- "_observeSetting:withBlock:"
- "_observer"
- "_observerAddress"
- "_observerInfo"
- "_observerQueue"
- "_observerQueue_tokensToBlocks"
- "_observers"
- "_observersLock"
- "_observing"
- "_opaque"
- "_open"
- "_openApplication:withOptions:clientHandle:completion:"
- "_options"
- "_orderedExtensions"
- "_orientation"
- "_otherModes"
- "_otherSettings"
- "_otherSettingsObserverInfo"
- "_outgoingRequestHandle"
- "_overrideTags:"
- "_overscanCompensation"
- "_overscanned"
- "_pauseWithResult:"
- "_payload"
- "_peer"
- "_pendedSendBlocks"
- "_pendingChangesToPrefetchedKeys"
- "_pendingUninstall"
- "_percentComplete"
- "_performAction:withResult:"
- "_performDelegateCallout:"
- "_personaAware"
- "_pid"
- "_pixelSize"
- "_placeholder"
- "_placeholderFilter"
- "_placeholderIdentityFilter"
- "_pointScale"
- "_policy"
- "_postInitialBookendObserverConnections"
- "_preferenceDomain"
- "_preferredMode"
- "_preferredScale"
- "_prefetchedDataLock"
- "_prefetchedKeyValues"
- "_prefetchedKeys"
- "_prepareForReuse"
- "_prerequisiteMilestones"
- "_previousSettings"
- "_prioritizeWithResult:"
- "_process"
- "_processHandle"
- "_processIdentity"
- "_progenitor"
- "_progress"
- "_propagatedSettings"
- "_propagating"
- "_protectedSurfaceRef"
- "_provisioningProfileValidated"
- "_provisioningProfiles"
- "_provisions"
- "_provisionsAllDevices"
- "_proxy"
- "_psuedoSceneUpdater"
- "_purchaserDSID"
- "_queue"
- "_queue_calculateValueConsumed:"
- "_queue_canPerformAction:"
- "_queue_evaluateConsumptionFromTimer:"
- "_queue_handleError:"
- "_queue_handleMessage:"
- "_queue_identifierToScenesSource"
- "_queue_invalidateScene:withTransitionContext:completion:"
- "_queue_invalidated"
- "_queue_isCloudDemoted"
- "_queue_noteAllowanceExhausted"
- "_queue_noteChangedSignificantly:"
- "_queue_observers"
- "_queue_progress"
- "_queue_registerSource:"
- "_queue_scenesClientForEndpoint:creatingIfNecessary:"
- "_queue_sendHandshake"
- "_queue_setProxy:force:"
- "_queue_stopMonitoring"
- "_queue_supportedActions"
- "_queue_unregisterSource:"
- "_queue_updateConsumption"
- "_queue_updateFromProgress"
- "_queue_updateScene:withSettings:diff:transitionContext:completion:"
- "_queuesByQOS"
- "_queues_connectionsByQOS"
- "_queues_xLayoutByQOS"
- "_ratingRank"
- "_reason"
- "_rebootType"
- "_reconnectingScenes"
- "_redacted"
- "_referenceFrame"
- "_referenceSizeDescription"
- "_refreshRate"
- "_registerSource:"
- "_registerSourceEndpoint:"
- "_registerSourcePeer:"
- "_reloadFromProxy:"
- "_reloadFromRecord:"
- "_reloadPlaceholdersNotificationFired"
- "_reloadProfiles"
- "_reloadProgress"
- "_remainsActionable"
- "_remoteTarget"
- "_removeAllSceneExtensions"
- "_removeElement:forKey:"
- "_removeSceneExtension:"
- "_removeVolatileSettings"
- "_renderID"
- "_reply"
- "_reportType"
- "_reportingLock"
- "_reportingLock_scenesByIdentity"
- "_requestHandler"
- "_requests"
- "_requiredCapabilities"
- "_requiresPersistentWiFi"
- "_resolved"
- "_responder"
- "_respondsToActions"
- "_respondsToClientSettings"
- "_respondsToHostHandle"
- "_respondsToInvalidate"
- "_respondsToPrivateActions"
- "_respondsToSettings"
- "_restricted"
- "_resumeWithResult:"
- "_rootIdentity"
- "_rotation"
- "_rotationDirection"
- "_safeOverscanRatio"
- "_sandboxURL"
- "_sanitizeAndValidatePayload"
- "_scale"
- "_scaleOverride"
- "_scaledSnapshotSize"
- "_scene"
- "_sceneExtensionNames"
- "_sceneID"
- "_scenesByIdentity"
- "_schedulingPolicy"
- "_screenTimePolicy"
- "_sdkVersion"
- "_secure"
- "_sendMessageType:withMessage:withReplyHandler:waitForReply:"
- "_sendPrefetchedKeys:withCompletion:"
- "_sendToObserversPlaceholderDidChangeSignificantly"
- "_sendToObserversPlaceholderProgressDidUpdate"
- "_sendUpdate:"
- "_sequenceNumber"
- "_server:registerOrientationInterest:"
- "_serviceQuality"
- "_serviceQueue"
- "_setChangeInFlight:forPrefetchedKey:application:"
- "_setClassClient:"
- "_setCounterpartClass:"
- "_setDelegate:"
- "_setInstalling:"
- "_setPendingUninstall:"
- "_setPrefetchedObjectIfNecessary:forKey:application:"
- "_setProxy:"
- "_setProxy:force:"
- "_setSpecification:"
- "_setTentativeUninstall:"
- "_setUninstalling:"
- "_setValue:forSetting:"
- "_setWorkspace:"
- "_setting"
- "_settingsClass"
- "_settingsDiff"
- "_settingsExtensionsForSceneExtension:"
- "_settingsHandler"
- "_sharedClient"
- "_sharedDefaults"
- "_sharedInstance"
- "_sharedLock_services"
- "_sharedLock_servicesRefCnt"
- "_sharedQueue"
- "_shortVersionString"
- "_showsArchiveOption"
- "_signatureForBlockAtArgumentIndex:"
- "_signatureVersion"
- "_signerIdentity"
- "_snapshotSize"
- "_sortElements"
- "_sortedSources"
- "_source"
- "_specialCollection"
- "_specification"
- "_startObservingProgress:withContext:"
- "_started"
- "_state"
- "_stateCaptureAssertion"
- "_stopMonitoring"
- "_stopMonitoringConstraints"
- "_stopObservingProgress:withContext:"
- "_strategy"
- "_strategyName"
- "_stringRepresentation"
- "_subSettingsForKey:local:createIfNeeded:"
- "_subtype"
- "_supportedInterfaceOrientations"
- "_supportsMultiwindow"
- "_suppressionCount"
- "_synchronizationQueue"
- "_synchronize:"
- "_synchronizedCaptureWithCompletion:"
- "_systemAppProxy"
- "_tags"
- "_target"
- "_taskNameRight"
- "_teamIdentifier"
- "_tentativeUninstall"
- "_terminateWithRequest:forWatchdog:"
- "_timer"
- "_timerFireCount"
- "_timerFireInterval"
- "_timestamp"
- "_transformDisplaysIfNecessaryFromDisplayConfiguration:"
- "_transformer"
- "_transitionContext"
- "_transitionHandler"
- "_transitionReasons"
- "_transitionsCount"
- "_type"
- "_typeIdentifier"
- "_uisHack"
- "_underlyingValueForSetting:"
- "_uninstalling"
- "_uniqueIdentifier"
- "_updatable"
- "_updateClientSettings:"
- "_updateForInitialization:forTransformInvalidation:"
- "_updateOption:forKey:"
- "_updateProgress"
- "_updateTransformsLock"
- "_uppProvisioningProfileValidated"
- "_userInitiated"
- "_validateApp:"
- "_validateAppStoreApp:"
- "_validateNonAppStoreApp:"
- "_violated"
- "_virtual"
- "_virtualDisplayConfigurationWithIdentifier:"
- "_volatile"
- "_watchdog"
- "_watchdog:shouldTerminateWithDeclineReason:"
- "_watchdog:terminationRequestForError:"
- "_width"
- "_workQueue"
- "_workQueue_addApplication:"
- "_workQueue_addPlaceholder:"
- "_workQueue_applicationForIdentity:"
- "_workQueue_expirationDateForProvisioningProfile"
- "_workQueue_identitiesByBundleID"
- "_workQueue_injectedAppIdentifiers"
- "_workQueue_installedApplicationsByIdentity"
- "_workQueue_managedApplicationBundleIDs"
- "_workQueue_pendingSynchronizationExecutionBlocks"
- "_workQueue_placeholderForIdentity:"
- "_workQueue_placeholdersByIdentity"
- "_workQueue_profilesBySignerIdentity"
- "_workQueue_reloadManagedApplicationBundleIDs"
- "_workQueue_reloadProfiles"
- "_workQueue_signatureNeedsExplicitUserTrust"
- "_workQueue_synchronizationActionCount"
- "_workQueue_usingNetwork"
- "_workspace"
- "_workspaceDelegate"
- "_workspaceIdentifier"
- "_xLayout"
- "actionClasses:"
- "actionHandler:"
- "actions:"
- "activate"
- "activateSceneFuture:completion:"
- "activateWithCompletion:"
- "activated"
- "activeInterfaceOrientation"
- "activeInterfaceOrientationWithCompletion:"
- "activeMessageBatch"
- "activeMultilinePrefix"
- "activeOrientationDidUpdate:"
- "activityMode"
- "add:"
- "addAction:"
- "addActions:"
- "addApplicationProxy:withOverrideURL:"
- "addApplicationRecord:"
- "addCommitHandler:forPhase:"
- "addCompletion:"
- "addElement:"
- "addEntriesFromDictionary:"
- "addFacility:"
- "addLayer:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:forKey:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserver:withConfiguration:"
- "addPrefetchedKeys:"
- "addPropagatedProperty:"
- "addPropagatedSetting:"
- "addPropagatedSettings:"
- "addProperty:"
- "addUpdateCompletion:"
- "advertisingAttributionReportEndpoint"
- "agent:registerMessageHandler:"
- "agent:sendMessage:withResponse:"
- "allInstalledApplications"
- "allKeys"
- "allObjects"
- "allPlaceholders"
- "allSettings"
- "allSettingsFromExtension:"
- "allSettingsFromProtocol:"
- "allValues"
- "alloc"
- "allocWithZone:"
- "allowCPUThrottling"
- "allowConcurrentLoading"
- "allowanceRemaining:"
- "allowsApplicationIdentifierEntitlement:"
- "allowsUnknownDisplays"
- "animationFence"
- "animationSettings"
- "annul"
- "anyObject"
- "appIDEntitlement"
- "appLibrary"
- "appState"
- "appTags"
- "appendArraySection:withName:multilinePrefix:skipIfEmpty:"
- "appendArraySection:withName:skipIfEmpty:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCGFloat:"
- "appendCGFloat:counterpart:"
- "appendCGRect:counterpart:"
- "appendCGSize:"
- "appendCGSize:counterpart:"
- "appendClass:"
- "appendClass:counterpart:"
- "appendClass:withName:"
- "appendDescriptionToBuilder:forFlag:object:ofSetting:"
- "appendDictionarySection:withName:multilinePrefix:skipIfEmpty:"
- "appendDouble:"
- "appendDouble:counterpart:"
- "appendDouble:withName:decimalPrecision:"
- "appendFloat:withName:"
- "appendFloat:withName:decimalPrecision:"
- "appendInteger:"
- "appendInteger:counterpart:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPoint:withName:"
- "appendPointer:withName:"
- "appendRect:withName:"
- "appendSize:withName:"
- "appendSizeT:"
- "appendSizeT:counterpart:"
- "appendString:counterpart:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUInt64:withName:"
- "appendUnsignedInt:withName:"
- "appendUnsignedInteger:withName:"
- "appleInternalProfile"
- "applicationDataStoreRepositoryClient:application:changedObject:forKey:"
- "applicationDataStoreRepositoryClient:storeInvalidatedForApplication:"
- "applicationIconDidChange:"
- "applicationIdentifier"
- "applicationIdentifiersWithAvailableStores"
- "applicationIdentifiersWithAvailableStoresForBundleID:"
- "applicationIdentitiesWithAvailableStores"
- "applicationIdentity"
- "applicationIdentityFilter"
- "applicationInfoClass"
- "applicationInfoForApplication:"
- "applicationInfoForAuditToken:"
- "applicationInfoForBundleIdentifier:"
- "applicationInfoSubclass"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationPlaceholderClass"
- "applicationProxyForBundleURL:"
- "applicationProxyForIdentifier:"
- "applicationStateDidChange:"
- "applicationType"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "applicationsWithAvailableStores"
- "applyClientSettings:"
- "applyParameters:"
- "applySettings:"
- "applyToMutableSettings:"
- "applyToSettings:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "archivedObjectForKey:"
- "archivedObjectForKey:withResult:"
- "arm64"
- "array"
- "arrayByAddingObject:"
- "arrayForKey:"
- "arrayWithArray:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "assertBarrierOnQueue"
- "assertionState"
- "attachContext:"
- "attachLayer:"
- "attachSceneContext:"
- "auditToken"
- "authoritative"
- "autorelease"
- "availableDataStores"
- "awakeFromCoder"
- "background"
- "backgroundWithUI"
- "backgrounded"
- "badgeValueForBundleID:"
- "barrier"
- "baseTransform"
- "beta"
- "beta-reports-active"
- "bezelImageName"
- "blockArguments"
- "blockReturnValue"
- "blocked"
- "blockedForScreenTimeExpiration"
- "bookendObserver"
- "boolForKey:"
- "boolForSetting:"
- "boolValue"
- "bootstrapConfiguration"
- "bs_CGFloatValue"
- "bs_array"
- "bs_errorWithDomain:code:configuration:"
- "bs_getValue:ofSize:"
- "bs_jobLabel"
- "bs_map:"
- "bs_objectsOfClass:"
- "bs_reduce:block:"
- "bs_safeNumberForKey:"
- "bs_safeObjectForKey:ofType:"
- "bs_secureDataFromObject:"
- "bs_secureDecodedFromData:"
- "bs_secureEncoded"
- "bs_secureObjectFromData:ofClass:"
- "bs_set"
- "bs_setSafeObject:forKey:"
- "bs_stringWithUTF8String:"
- "build"
- "buildCGImage"
- "buildConfigurationWithError:"
- "buildWithError:"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "builtOnOrAfterSDKVersion:"
- "builtWithTSAN"
- "bundleContainerURL"
- "bundleForClass:"
- "bundleIdentifierForIdentityString:error:"
- "bundleProxyForIdentifier:"
- "bundleProxyWithAuditToken:error:"
- "bundleType"
- "bundleVersion"
- "bundleWithURL:"
- "c"
- "c16@0:8"
- "caDisplay"
- "cacheGUID"
- "cacheInfoWithData:hashType:"
- "cachedCDHashInfo"
- "cachedCodeDirectoryHash"
- "cachedCodeDirectoryHashType"
- "canHaveAgent"
- "canOpenApplication:completion:"
- "canOpenApplication:reason:"
- "canPostToBookendObserver"
- "canSendResponse"
- "cancel"
- "cancelCoordinatorForAppWithBundleID:withReason:client:completion:"
- "cancelRequest"
- "cancelWithResult:"
- "cannotResolveForReason:"
- "canonicalExecutablePath"
- "capture"
- "captureCompletions"
- "carDisplay"
- "carInstrumentsDisplay"
- "changedSettings"
- "charValue"
- "characterAtIndex:"
- "characterIsMember:"
- "checkin"
- "checkout"
- "checkoutProxyWithEndpoint:"
- "class"
- "classForCoder"
- "cleanupClientPort:"
- "client:handleOrientationUpdate:"
- "clientCallbackQueue"
- "clientComponents"
- "clientFuture"
- "clientHandle_messageBuilder"
- "clientScene"
- "clientSettingNames:"
- "clientSettings:"
- "clientSettingsExtensions"
- "clientUpdateHandler:"
- "close"
- "closeSession:"
- "coalesceEvent:skipped:"
- "code"
- "codeSignatureVersion"
- "coder"
- "coderWithMessage:"
- "colorGamut"
- "com.apple.frontboard.applicationTrust.workQueue"
- "com.apple.frontboard.profileManager.taskQueue"
- "com.apple.frontboardservices.device_emulation"
- "com.apple.frontboardservices.orientationobserver.callback"
- "commitWithReason:"
- "compare:"
- "compare:options:"
- "compatibilityObject"
- "compatibleWithTarget:"
- "completionHandler"
- "component"
- "componentForExtension:ofClass:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "concurrent"
- "configurationForDefaultMainDisplayMonitor"
- "configurationForIdentity:"
- "configurationWithEndpoint:"
- "configureConnectMessage:"
- "configureConnection:"
- "configureParameters:"
- "configureSetting:"
- "configured"
- "conformsToExtension:"
- "conformsToProtocol:"
- "connectedIdentities"
- "connectionWithEndpoint:"
- "connectionWithEndpoint:clientContextBuilder:"
- "constructing configuration failed : identity=%@ configChanged=%i currentMode=%@ preferredMode=%@ otherModes=%@ cloningSupported=%i overscanned=%i overscanCompensation=%@ safeOverscanRatio=%@ pixelSize=%@ nativeBounds=%@ bounds=%@ : base=%@"
- "containsLegacySetting:"
- "containsObject:"
- "containsProperty:"
- "containsPropertyFromExtension:"
- "containsSetting:"
- "containsSettingNamed:"
- "containsValueForKey:"
- "contextId"
- "contextWithSceneID:settings:"
- "contexts"
- "copy"
- "copy:"
- "copyAddingCustomAttributes:"
- "copyApplyingDiff:"
- "copyAsReadWrite"
- "copyForSecureRendering"
- "copyWithOverrideBounds:"
- "copyWithOverrideMode:"
- "copyWithOverrideMode:pixelSize:nativeBounds:"
- "copyWithUniqueIdentifier:"
- "copyWithZone:"
- "correspondingApplicationRecord"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "counterpartAgent"
- "createClientPort"
- "createMessage"
- "createMessageWithCompletion:"
- "createReply"
- "createScene:"
- "createScene:completion:"
- "createSceneFutureWithDefinition:"
- "createSceneWithIdentity:parameters:transitionContext:completion:"
- "createSceneWithOptions:completion:"
- "currentContext"
- "currentHandler"
- "currentLayout"
- "currentPhase"
- "currentProcess"
- "currentProcessServicesDefaultShellEndpoint"
- "currentState"
- "currentThread"
- "customAttributeForKey:"
- "customMachServices"
- "customPolicy"
- "customScaleFactorX"
- "customScaleFactorY"
- "customTranslationOffsetX"
- "customTranslationOffsetY"
- "d"
- "d16@0:8"
- "dataContainerURL"
- "dataResetWithRequest:completion:"
- "dataStoreMonitor:didInvalidateApplication:"
- "dataStoreMonitor:didUpdateApplication:forKey:"
- "databaseWasRebuilt"
- "date"
- "deactivate"
- "dealloc"
- "decodeBoolForKey:"
- "decodeCollectionOfClass:containingClass:forKey:"
- "decodeDictionaryOfClass:forKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeStringForKey:"
- "decodeUInt64ForKey:"
- "decodeWithCoder:"
- "decodeXPCObjectOfType:forKey:"
- "defaultCenter"
- "defaultIdentityForProcessIdentity:"
- "defaultService"
- "defaultServiceForEndpoint:"
- "defaultShellEndpoint"
- "defaultShellEndpointEnabled"
- "defaultShellMachName"
- "definition"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionOfValue:forSetting:"
- "descriptionProvider"
- "descriptionWithMultilinePrefix:"
- "deserializeObjectForKey:ofType:"
- "deserializeObjectForKey:ofType:withResult:"
- "detachContext:"
- "detachLayer:"
- "detachSceneContext:"
- "deviceEmulationVersion"
- "deviceFamilies"
- "deviceFamily"
- "deviceManagementPolicy"
- "deviceManagementPolicyDidChange:"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveMessage:fromCounterpartAgent:withResponseSender:"
- "diffByApplyingDiff:toDiff:"
- "diffFromSettings:toSettings:"
- "disablesClientBatching"
- "displayBacklightLevel"
- "displayId"
- "displayMonitor:didConnectIdentity:withConfiguration:"
- "displayMonitor:didUpdateIdentity:withConfiguration:"
- "displayMonitor:willDisconnectIdentity:"
- "displayName"
- "displayType"
- "displays"
- "distantFuture"
- "domain"
- "domainForIdentifier:"
- "domainForMachName:"
- "domainIdentifier"
- "domainsContainingServiceIdentifier:"
- "doubleValue"
- "downloaderDSID"
- "elapsedCPUTimeForFrontBoard"
- "embeddedApplicationIdentifier"
- "emulatedArtworkSubtype"
- "emulatedDevice"
- "emulatedDeviceBezelImageName"
- "emulatedDeviceBounds"
- "emulatedDeviceClass"
- "emulatedDeviceImageContainingBundle"
- "emulatedDeviceMaskImageName"
- "emulatedDisplayCornerRadius"
- "emulatedDisplayHeight"
- "emulatedDisplayWidth"
- "emulatedHomeButtonType"
- "enableEmulation"
- "enabled"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeUInt64:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "encodeWithXPCDictionary:"
- "encodeXPCObject:forKey:"
- "encoding"
- "endpointForMachName:service:instance:"
- "endpointMonitoringEnabled"
- "entitlementValuesForKeys:"
- "entitlements"
- "enumerateKeyedObjectsWithBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithBlock:"
- "enumerateScenesWithBlock:"
- "enumerateSortedWithBlock:"
- "enumerateWithBlock:"
- "enumeratorWithOptions:"
- "environmentAliases"
- "environmentVariables"
- "errorHandler"
- "errorWithDomain:code:userInfo:"
- "evaluateWithInspector:context:"
- "everActivated"
- "executablePath"
- "executableURL"
- "execute"
- "executeRequestsWithHandler:completionHandler:expirationHandler:"
- "executionContext"
- "exitsOnSuspend"
- "expectedFinalInstallPhase"
- "expectsSecureRendering"
- "expirationDate"
- "expired"
- "extensionForBSObjCProtocol:"
- "extensionForProtocol:"
- "extensionIdentifier"
- "externalAccessoryProtocols"
- "f"
- "f16@0:8"
- "failed to create a main FBSDisplayConfiguration from CADisplay=%@ -> created=%@"
- "failed to create a non-main FBSDisplayConfiguration from CADisplay=%@ -> created=%@"
- "failed to find the main CADisplay"
- "failed to load entitlements for '%@' because we could not find the proxy"
- "fallbackFolderName"
- "fallbackIOSurface"
- "fallbackXPCEncodableClass"
- "fbsDisplay"
- "fbs_bundleIDFromAppID"
- "fbs_correspondingApplicationProxy"
- "fbs_correspondingApplicationRecord"
- "fbs_getObjectForValue:atIndex:"
- "fbs_isLaunchProhibited"
- "fbs_looksLikeAnIdentityString"
- "fbs_mediumDescription"
- "fbs_personaUniqueString"
- "fbs_processIdentityForApplicationIdentity:"
- "fbs_sceneClientIdentity"
- "fbs_shortDescription"
- "fbs_singleLineDescriptionOfBSActions"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "finalizeLayout"
- "findApplicationRecordFetchingPlaceholder:error:"
- "finishDecoding"
- "fireCompletion:error:"
- "fireCompletion:openAppErrorCode:"
- "firstObject"
- "flagForKey:"
- "flagForSetting:"
- "flags"
- "floatValue"
- "flush"
- "folderNames"
- "forceIsD22ChecksToPass"
- "forwardInvocation:"
- "forwardingTargetForSelector:"
- "frame:"
- "freeDeveloperProfile"
- "freeDeveloperProvisioningProfileValidated"
- "freeProfileValidated"
- "getArgument:atIndex:"
- "getValue:size:"
- "getter"
- "graphicsPolicy"
- "handle"
- "handleError:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleForAuditToken:error:"
- "handleForIdentifier:error:"
- "handleForIdentifier:pidVersion:error:"
- "handleForRequestType:context:"
- "handleMessage:withType:"
- "handleOrientationResetForClient:"
- "handlePrivateActions:"
- "handleWithAuditToken:"
- "handshakeWithRemnants:"
- "hasBeenSignalled"
- "hasEmulatedDeviceBounds"
- "hasEntitlement:"
- "hasPrefix:"
- "hasProtectedContent"
- "hasSuffix:"
- "hasViewServicesEntitlement"
- "hashTableWithOptions:"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "hostAuditToken"
- "hostComponents"
- "hostHandle"
- "hostScene"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8@\"NSString\"16o^I24"
- "i32@0:8@16o^I24"
- "i40@0:8@\"NSString\"16@\"NSDictionary\"24o^@32"
- "i40@0:8@16@24o^@32"
- "identifierWithHostEndpoint:"
- "identifierWithPeer:"
- "identifierWithPid:"
- "identities"
- "identityForBundleID:"
- "identityForEmbeddedApplicationIdentifier:"
- "identityForIdentifier:"
- "identityForIdentifier:workspaceIdentifier:"
- "identityForIdentifier:workspaceIdentifier:internalWorkspaceIdentifier:"
- "identityForInjectedEndpointToProcessIdentity:"
- "identityForLSApplicationIdentity:LSApplicationRecord:"
- "identityForManagedEndpointOfProcessIdentity:"
- "identityForProcessIdentity:"
- "identityOfCurrentProcess"
- "identityString"
- "identityStringsForApplicationWithBundleIdentifier:error:"
- "identityToken"
- "imageContainingBundleIdentifier"
- "immutableCopy"
- "immutableSubclass"
- "indexOfObjectIdenticalTo:"
- "indirect_defaultValue"
- "indirect_isLegacy"
- "indirect_isPropagating"
- "indirect_legacySetting"
- "indirect_name"
- "inefficient loading of all entitlements for '%@'"
- "info"
- "inheritedProtocols"
- "init"
- "initForReadingFromData:error:"
- "initWithAllowance:"
- "initWithApplicationInfo:andProvisioningProfiles:isManaged:"
- "initWithApplicationProxy:"
- "initWithApplicationRecord:"
- "initWithArray:"
- "initWithArray:copyItems:"
- "initWithBSXPCCoder:"
- "initWithBundleID:reason:acquisitionHandler:"
- "initWithBundleIdentifier:"
- "initWithBundleIdentifier:efficacy:name:context:withHandler:"
- "initWithBundleIdentifier:personaUniqueString:"
- "initWithCAContext:"
- "initWithCAContextID:level:"
- "initWithCAContextID:renderID:level:"
- "initWithCADisplay:"
- "initWithCADisplay:isMainDisplay:"
- "initWithCapacity:"
- "initWithChangesFromSettings:toSettings:"
- "initWithClient:"
- "initWithCoder:"
- "initWithComponent:extension:"
- "initWithConfiguration:"
- "initWithConfigurator:"
- "initWithContextID:baseTransform:"
- "initWithContextID:renderID:level:"
- "initWithDelegate:"
- "initWithDisplay:alwaysConnected:triggers:monitor:"
- "initWithDisplayConfiguration:layer:"
- "initWithDisplayConfiguration:layers:"
- "initWithDisplayType:"
- "initWithDisplayType:handler:"
- "initWithDisplayType:qualityOfService:handler:"
- "initWithDomain:code:userInfo:"
- "initWithEndpoint:"
- "initWithEndpoint:qos:observer:"
- "initWithEndpoint:queue:calloutQueue:workspace:"
- "initWithFormat:arguments:"
- "initWithIdentifier:"
- "initWithIdentifier:calloutQueue:"
- "initWithIdentifier:forReason:invalidationBlock:"
- "initWithIdentifier:queue:"
- "initWithIdentityString:"
- "initWithInfo:responder:"
- "initWithInitializationCompletion:"
- "initWithInvocation:interface:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithKeyboardContext:"
- "initWithKeyboardOwner:level:"
- "initWithLevel:keyboardOwner:"
- "initWithMessagePacker:"
- "initWithMessagePayload:"
- "initWithMode:options:reason:"
- "initWithName:process:policy:"
- "initWithName:scene:executionPolicy:"
- "initWithObject:"
- "initWithObjects:"
- "initWithObserver:"
- "initWithOptions:capacity:"
- "initWithOrientation:sequenceNumber:duration:rotationDirection:"
- "initWithPID:flags:reason:name:withHandler:"
- "initWithParameters:"
- "initWithPeer:queue:calloutQueue:workspace:"
- "initWithPlaceholder:queue:"
- "initWithQueue:"
- "initWithReason:"
- "initWithRequestType:context:"
- "initWithRequests:expirationInterval:responseHandler:"
- "initWithScene:"
- "initWithScene:extension:"
- "initWithSceneID:settings:"
- "initWithSerialQueue:"
- "initWithSettings:"
- "initWithSettings:allowsProtectedContent:"
- "initWithSignerIdentity:profile:"
- "initWithSnapshotContext:"
- "initWithSpecification:"
- "initWithTimeIntervalSinceReferenceDate:"
- "initWithTrackingContext:"
- "initWithTransformer:"
- "initWithWindowContext:"
- "initWithWorkspaceID:"
- "initWithXPCDictionary:"
- "initialClientSettings"
- "initialSettings"
- "initialize"
- "inspect:"
- "inspectChangesWithBlock:"
- "inspectDiff:withContext:"
- "inspectKeyedChangesWithBlock:"
- "inspectOtherChangesWithBlock:"
- "installProgress"
- "installType"
- "installedApplicationFilter"
- "installedApplicationForIdentity:"
- "installedApplicationForIdentityString:"
- "installedApplicationWithBundleIdentifier:"
- "installedApplicationWithBundleIdentifier:completionHandler:"
- "installedApplicationsForBundleIdentifier:"
- "installing"
- "instanceIdentifier"
- "instanceMethodForSelector:"
- "instanceMethodSignatureForSelector:"
- "instancesRespondToSelector:"
- "intValue"
- "integerValue"
- "interfaceOrientationForSupportedOrientations:preferredOrientation:"
- "interfaceWithIdentifier:"
- "internalWorkspaceIdentifier"
- "interruptionPolicy"
- "invalid host pid : %i"
- "invalid host pid=%i"
- "invalidate"
- "invalidate:"
- "invalidateSnapshotWithContext:"
- "invalidated"
- "invalidationHandler:"
- "invertInterface:"
- "invertedInterface"
- "invocationWithMethodSignature:"
- "invokeWithReceiver:replyHandler:"
- "invokeWithTarget:"
- "invokeWithTarget:replyHandler:"
- "invoked"
- "isActivated"
- "isActive"
- "isAirPlayDisplay"
- "isAppleInternalProfile"
- "isBSServiceConnectionError"
- "isBackgrounded"
- "isBarrier"
- "isBeta"
- "isBetaApp"
- "isBlock"
- "isBlocked"
- "isBlockedForScreenTimeExpiration"
- "isCAContextLayer"
- "isCancellable"
- "isCarDisplay"
- "isCarInstrumentsDisplay"
- "isClientFuture"
- "isCloningSupported"
- "isComplete"
- "isConfigured"
- "isConnected"
- "isContinuityDisplay"
- "isCopy"
- "isCustomPolicy"
- "isDaemon"
- "isDefaultShellEndpointEnabled"
- "isEmpty"
- "isEmulatedDevice"
- "isEnabled"
- "isEndpointMonitoringEnabled"
- "isEqual"
- "isEqual:"
- "isEqualToString:"
- "isExitsOnSuspend"
- "isExpired"
- "isExternal"
- "isFailed"
- "isForeground"
- "isFreeDeveloperProfile"
- "isFreeDeveloperProvisioningProfileValidated"
- "isHiddenDisplay"
- "isIgnoringOcclusions"
- "isInstalled"
- "isInvalidated"
- "isKeyboardLayer"
- "isKeyboardProxyLayer"
- "isKeyboardScene"
- "isKindOfClass:"
- "isLaunchProhibited"
- "isLocal"
- "isMainDisplay"
- "isMainRootDisplay"
- "isMainThread"
- "isManaged:"
- "isMemberOfClass:"
- "isMonitoring"
- "isMusicOnlyDisplay"
- "isNSArray__"
- "isNSDictionary__"
- "isNonLaunching"
- "isObject"
- "isOccluded"
- "isOpaque"
- "isOpen"
- "isOverscanned"
- "isPasscodeLockedOrBlocked"
- "isPausable"
- "isPersonaAware"
- "isPlaceholder"
- "isPrioritizable"
- "isPrivacySensitiveSetting:"
- "isProvisioningProfileValidated"
- "isProxy"
- "isReadOnly"
- "isReadWrite"
- "isReboot"
- "isRequired"
- "isResourceProvision"
- "isRestricted"
- "isRestrictedAirPlayDisplay"
- "isResumable"
- "isRootIdentity"
- "isRunning"
- "isRunningBoardAssertionDisabled"
- "isScheduled"
- "isServerProcess"
- "isShutdown"
- "isSignatureVersionSupportEndingSoon"
- "isSignatureVersionSupported"
- "isStarted"
- "isStruct"
- "isSubclassOfClass:"
- "isSubsetOfOrderedSet:"
- "isTransitioning"
- "isUIApplicationElement"
- "isUIKitMainLike"
- "isUPPProvisioningProfileValidated"
- "isUserInitiated"
- "isUsingNetwork"
- "isValid"
- "isViolated"
- "isVirtualized"
- "isVoid"
- "isWeak"
- "isiPodOnlyDisplay"
- "itemID"
- "jetsamMode"
- "jetsamPolicy"
- "jetsamPriority"
- "kb"
- "keyDescriptionForSetting:"
- "keyForSetting:"
- "keyPathsForValuesAffectingInstallPhase"
- "keyPathsForValuesAffectingInstallState"
- "keyboardOwner"
- "keyboardScene"
- "lastArgument"
- "lastModifiedDate"
- "lastObject"
- "lastPathComponent"
- "laterConfiguration:"
- "launchIdentifiers"
- "layerWithCAContext:"
- "layers"
- "layoutMonitor:didUpdateDisplayLayout:"
- "layoutMonitor:didUpdateDisplayLayout:withContext:"
- "length"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "localHandle"
- "localIdentity"
- "localService"
- "localServiceWithIdentifier:"
- "localizedDescription"
- "localizedFailureReason"
- "localizedName"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "logStep:byParty:phase:success:forBundleID:description:"
- "loggingIdentifier"
- "longLongValue"
- "longValue"
- "lowercaseLetterCharacterSet"
- "machQueue"
- "mainBundle"
- "mainConfiguration"
- "mainDisplay cannot debounce nor disconnect : %@"
- "mainDisplayInstanceIdentifier"
- "mainIdentity"
- "managedAppIDs"
- "mapTableWithKeyOptions:valueOptions:"
- "maskImageName"
- "matchesProperty:"
- "matchesPropertyName:"
- "membersForCoder"
- "messageWithBSXPCMessage:ownReply:"
- "messageWithPacker:"
- "messageWithPayload:"
- "methodForSelector:"
- "methodSignature"
- "methodSignatureForSelector:"
- "methods"
- "migrateIdentifier:toIdentifier:"
- "migrateToIdentity:error:"
- "migrateWithError:"
- "minimumBrightnessLevel"
- "minusSet:"
- "modifyBody:"
- "modifyProem:"
- "monitor:didReceiveEndpoint:"
- "monitor:willLoseEndpoint:"
- "monitorForService:"
- "monitorProcess:"
- "monitorWithConfiguration:"
- "mutableCopy"
- "mutableCopy:"
- "mutableCopyWithZone:"
- "mutableSettings"
- "mutableSubclass"
- "nativeCenter"
- "nativeOrientation"
- "needsMigration"
- "needsUserInteractivePriority"
- "networkUsageChanged:"
- "new"
- "noteClientDidConnect:withMessage:"
- "noteClientDidDisconnect:"
- "noteDidReceiveMessage:withType:fromClient:"
- "null"
- "nullEndpointForService:instance:"
- "numberForKey:"
- "numberOfArguments"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objCType"
- "objectAtIndex:"
- "objectClass"
- "objectContainedClasses"
- "objectEnumerator"
- "objectForKey:"
- "objectForKey:forApplication:"
- "objectForKey:withResult:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "objectProtocols"
- "objectsForInfoDictionaryKeys:"
- "objectsPassingTest:"
- "observeDidAddApplicationsWithBlock:"
- "observeDidAddPlaceholdersWithBlock:"
- "observeDidCancelPlaceholdersWithBlock:"
- "observeDidChangeNetworkUsageWithBlock:"
- "observeDidDemoteApplicationsWithBlock:"
- "observeDidRemoveApplicationsWithBlock:"
- "observeDidReplaceApplicationsWithBlock:"
- "observeDidUpdateApplicationsWithBlock:"
- "observeDisplayConfigurationWithBlock:"
- "observeFrameWithBlock:"
- "observeInterfaceOrientationWithBlock:"
- "observeIsBackgroundedWithBlock:"
- "observeIsForegroundWithBlock:"
- "observeLaunchProhibitedApps"
- "observeLayersWithBlock:"
- "observeLevelWithBlock:"
- "observeOcclusionsWithBlock:"
- "observeOtherSetting:withBlock:"
- "observePreferredInterfaceOrientationWithBlock:"
- "observePreferredLevelWithBlock:"
- "observePreferredSceneHostIdentifierWithBlock:"
- "observePreferredSceneHostIdentityWithBlock:"
- "observeProperty:withBlock:"
- "observeSetting:withBlock:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observers"
- "occluded"
- "opaque"
- "openApplication:options:clientPort:withResult:"
- "openApplication:options:withResult:"
- "openApplication:withOptions:clientHandle:completion:"
- "openApplication:withOptions:completion:"
- "openApplication:withOptions:originator:requestID:completion:"
- "openSessionWithName:executionPolicy:"
- "openURL:application:options:clientPort:withResult:"
- "optionsWithDelegate:"
- "optionsWithDictionary:"
- "orderedSet"
- "orderedSetWithArray:"
- "orderedSetWithObject:"
- "originatingConfiguration"
- "originatingProcess"
- "parametersForSpecification:"
- "path"
- "pathWithComponents:"
- "pause"
- "pauseCoordinatorForAppWithBundleID:completion:"
- "pauseWithResult:"
- "pendingUninstall"
- "performAfter:withBlock:"
- "performAsync:"
- "performAsyncAndWait:"
- "performRequestForScene:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSnapshotWithContext:"
- "personaAware"
- "personaType"
- "personaUniqueString"
- "pidForApplication:"
- "placeholderDidChangeSignificantly:"
- "placeholderFilter"
- "placeholderForIdentity:"
- "placeholderForIdentityString:"
- "placeholderIdentityFilter"
- "placeholderPercentCompleteDidChange:"
- "placeholderProgressDidUpdate:"
- "placeholderWithBundleIdentifier:"
- "placeholdersForBundleIdentifier:"
- "pluginIdentifier"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "policyForStrategy:withProvisions:"
- "policyWithName:forProvisions:"
- "policyWithProvisions:"
- "policyWithReason:flags:"
- "preferenceDomain"
- "preferredInterfaceOrientation"
- "preferredLevel"
- "preferredSceneHostIdentifier"
- "preferredSceneHostIdentity"
- "prefersProcessTaskSuspensionWhileSceneForeground"
- "prefetchedObjectIfAvailableForKey:application:outObject:"
- "prepareForReuse"
- "prettyProcessDescription"
- "prioritize"
- "prioritizeCoordinatorForAppWithBundleID:completion:"
- "prioritizeWithResult:"
- "processHandleForApplication:"
- "processHandleForBundleID:"
- "processInfo"
- "processName"
- "processorCount"
- "profileValidated"
- "profilesForSignerIdentity:"
- "progress"
- "propagateSetting:"
- "propagateToSceneWithDefinition:"
- "propagatedSettings"
- "properties"
- "propertyWithProperty:error:"
- "protocolForProtocol:"
- "protocolWithName:"
- "provision:wasViolatedWithError:"
- "provisionWithAllowance:"
- "provisionWithResourceType:timeInterval:"
- "provisioningProfileValidated"
- "provisionsAllDevices"
- "pseudoSceneWithIdentifier:specification:"
- "pseudoTokenWithIdentifier:"
- "publisher:didUpdateLayout:withTransition:"
- "publisherWithConfiguration:"
- "purchaserDSID"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8Q16q24"
- "qualityOfService"
- "queryForExecutableURL:withError:"
- "queueWithDispatchQueue:targetQueue:"
- "queueWithName:serviceQuality:"
- "queue_activate"
- "queue_canPerformAction:"
- "queue_clientDidConnect:withMessage:"
- "queue_clientDidDisconnect:"
- "queue_handleMessage:withType:fromClient:"
- "queue_isCancellationAllowed"
- "queue_isValid"
- "queue_supportedActions"
- "queue_updateProxy:"
- "raise:format:"
- "rangeOfString:"
- "ratingRank"
- "rbsHandle"
- "realToken"
- "reboot"
- "reconnectSceneWithIdentity:parameters:transitionContext:completion:"
- "referenceFrame"
- "registerOrientationInterest:"
- "registerOrientationInterest:completion:"
- "relativePriority"
- "release"
- "remoteProcess"
- "remoteTarget"
- "remoteTargetForProtocol:"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "remoteToken"
- "removabilityForAppWithIdentity:error:"
- "remove:"
- "removeAction:"
- "removeActions:"
- "removeAllLayers"
- "removeAllObjects"
- "removeAllObjectsForApplication:withCompletion:"
- "removeAllObservers"
- "removeAllSettings"
- "removeElement:"
- "removeFacility:"
- "removeLayer:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectForKey:forApplication:withCompletion:"
- "removeObjectIdenticalTo:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeObserver:forKeyPath:context:"
- "removeObserverForKey:"
- "removeObserverForToken:"
- "removePrefetchedKeys:withCompletion:"
- "removePropagatedProperty:"
- "removePropagatedSetting:"
- "removePropagatedSettings:"
- "removeProperty:"
- "requestActiveOrientation"
- "requestActiveOrientationCompletion:"
- "requestDestructionOfScene:withCompletion:"
- "requestForProcess:withLabel:"
- "requestHandler"
- "requestSceneCreationWithIdentifier:initialClientSettings:completion:"
- "requestSceneCreationWithInitialClientSettings:completion:"
- "requestSceneFromEndpoint:withOptions:completion:"
- "requestSceneWithOptions:completion:"
- "requiredCapabilities"
- "requiredDeviceCapabilities"
- "requiresPersistentWiFi"
- "resetWithRequest:completion:"
- "resolve"
- "resolveMachService:"
- "responderWithHandler:"
- "respondsToSelector:"
- "responseForError:"
- "restricted"
- "resumable"
- "resumeCoordinatorForAppWithBundleID:completion:"
- "resumeWithResult:"
- "retain"
- "retainCount"
- "returnValue"
- "root"
- "rootLayerBackgroundColorString"
- "runningBoardAssertionDisabled"
- "safeArchivedObjectForKey:ofType:"
- "safeArchivedObjectForKey:ofType:withResult:"
- "safeObjectForKey:ofType:"
- "safeObjectForKey:ofType:withResult:"
- "sandboxURL"
- "scalingStyle"
- "scene:didInitializeWithEvent:completion:"
- "scene:didReceiveActions:"
- "scene:didReceiveActions:forExtension:"
- "scene:didUpdateClientSettings:"
- "scene:didUpdateClientSettings:withDiff:transitionContext:"
- "scene:didUpdateHostHandle:"
- "scene:didUpdateSettings:"
- "scene:didUpdateWithDiff:transitionContext:completion:"
- "scene:handleActions:"
- "scene:handleEvent:withCompletion:"
- "scene:handlePrivateActions:"
- "scene:invalidateWithTransitionContext:"
- "scene:reviewEvent:withCompletion:"
- "scene:sendInvocation:"
- "scene:sendMessage:withResponse:"
- "scene:willInvalidateWithEvent:completion:"
- "sceneID:destroyWithTransitionContext:completion:"
- "sceneID:didReceiveActions:forExtension:"
- "sceneID:didUpdateClientSettingsWithDiff:transitionContext:completion:"
- "sceneID:handleInvocation:completion:"
- "sceneID:invalidateWithContext:clientError:"
- "sceneID:sendActions:toExtension:completion:"
- "sceneID:sendMessage:completion:"
- "sceneID:sendMessage:withResponse:"
- "sceneID:updateWithSettingsDiff:transitionContext:completion:"
- "sceneMessageErrorWithCode:"
- "sceneWillInvalidate:"
- "sceneWithIdentifier:"
- "sceneWithIdentity:"
- "scenes"
- "scheduleRepeatingWithFireInterval:repeatInterval:leewayInterval:queue:handler:"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "schedulingPolicy"
- "screenTimePolicy"
- "sdkVersion"
- "selectorName"
- "self"
- "send"
- "sendActions:"
- "sendActions:completion:"
- "sendActions:toExtension:"
- "sendActions:toWorkspaceID:completion:"
- "sendActions:withResult:"
- "sendBatchedMessages"
- "sendInvocation:"
- "sendMessage:withType:"
- "sendMessage:withType:replyHandler:waitForReply:timeout:"
- "sendMessage:withType:toClients:"
- "sendPrivateActions:"
- "sendReplyMessageWithPacker:"
- "sendResponse:"
- "sendSynchronously"
- "sentinelWithCompletion:"
- "sentinelWithSignalCount:signalHandler:"
- "serial"
- "serializeObject:forKey:"
- "serviceClass"
- "serviceClass:"
- "serviceClass:relativePriority:"
- "serviceForEndpoint:withIdentifier:"
- "serviceForIdentifier:"
- "serviceIdentifier"
- "serviceName"
- "serviceQueue"
- "serviceWithClass:"
- "serviceWithDefaultShellEndpoint"
- "serviceWithEndpoint:"
- "set"
- "setActions:"
- "setActivationHandler:"
- "setActivityMode:"
- "setAllowCPUThrottling:"
- "setAllowConcurrentLoading:"
- "setAllowance:"
- "setAllowsProtectedContent:"
- "setAllowsUnknownDisplays:"
- "setAnimationFence:"
- "setAnimationSettings:"
- "setAppLibrary:"
- "setApplicationIdentityFilter:"
- "setApplicationInfoClass:"
- "setApplicationInfoSubclass:"
- "setApplicationPlaceholderClass:"
- "setArchivedObject:forKey:"
- "setArgument:atIndex:"
- "setAuthoritative:"
- "setBacklightLevel:"
- "setBacklightState:"
- "setBadgeValue:"
- "setBadgeValue:forBundleID:"
- "setBarrier:"
- "setBatchingHandler:"
- "setBundleIdentifier:"
- "setCachedCDHashInfo:"
- "setCallOutQueue:"
- "setCalloutQueue:"
- "setClient:"
- "setClientExtendedData:"
- "setClientFuture:"
- "setClientIdentity:"
- "setClientMessagingExpectation:"
- "setClientProcess:"
- "setClientProcessHandle:"
- "setClientSettings:"
- "setClientSettingsDiff:"
- "setCloningNotSupported"
- "setCloningSupported:"
- "setCodeDescription:"
- "setCompletion:"
- "setCompletionHandler:"
- "setCurrentMode:preferredMode:otherModes:"
- "setCustomPolicy:"
- "setDefaultShellEndpointEnabled:"
- "setDefaultValue:"
- "setDelegate:"
- "setDescriptionProvider:"
- "setDictionary:"
- "setDisableFrameDoubling:"
- "setDisplay:"
- "setDisplayBacklightLevel:"
- "setDisplayConfiguration:"
- "setDisplayType:"
- "setDomain:"
- "setDomainIdentifier:"
- "setDuration:"
- "setEndpoint:"
- "setEndpointMonitoringEnabled:"
- "setEraseDataPlan:"
- "setError:"
- "setErrorHandler:"
- "setExceptionCode:"
- "setExecutionContext:"
- "setExecutionPolicy:"
- "setExpectsSecureRendering"
- "setExpirationInterval:"
- "setExpired:"
- "setExplanation:"
- "setFailureDescription:"
- "setFailureReason:"
- "setFillsDisplayBounds:"
- "setFlag:forKey:"
- "setFlag:forSetting:"
- "setFlags:"
- "setForeground:"
- "setFrame:"
- "setGraphicsPolicy:"
- "setHandler:"
- "setHasKeyboardFocus:"
- "setHdrMode:"
- "setHideProgress:"
- "setIdentifier:"
- "setIdentity:"
- "setInitialClientSettings:"
- "setInitialSettings:"
- "setInstalledApplicationFilter:"
- "setInstance:"
- "setInstanceIdentifier:"
- "setInterface:"
- "setInterfaceOrientation:"
- "setInterfaceTarget:"
- "setInternalWorkspaceIdentifier:"
- "setInterruptionHandler:"
- "setInterruptionPolicy:"
- "setInvalidationHandler:"
- "setJetsamMode:"
- "setJetsamPolicy:"
- "setJetsamPriority:"
- "setKeyboardFocusApplication:deferringToken:completion:"
- "setKeyboardFocusApplicationPID:completion:"
- "setKeyboardFocusApplicationPID:deferringToken:completion:"
- "setKeyboardFocusApplicationWithBundleID:pid:completion:"
- "setKeyboardScene:"
- "setLPEMOption:"
- "setLabel:"
- "setLayers:"
- "setLayersToExclude:"
- "setLevel:"
- "setLocalContext:"
- "setLogicalScale:"
- "setMessage:"
- "setMessageHandler:"
- "setMode:"
- "setName:"
- "setNativePixelSize:"
- "setNeedsUserInteractivePriority:"
- "setNullPreserving:"
- "setNullificationHandler:"
- "setObject:forKey:"
- "setObject:forKey:forApplication:withCompletion:"
- "setObject:forKeyedSubscript:"
- "setObject:forSetting:"
- "setOccluded:"
- "setOpaque:"
- "setOptions:"
- "setOrientation:"
- "setOriginatingProcess:"
- "setOtherSettings:"
- "setOverscanCompensation:"
- "setOverscanned:compensation:safeRatio:"
- "setParentUpdate:"
- "setPersonaAware:"
- "setPixelSize:nativeBounds:bounds:"
- "setPlaceholderFilter:"
- "setPlaceholderIdentityFilter:"
- "setPointScale:"
- "setPreferredInterfaceOrientation:"
- "setPreferredLevel:"
- "setPreferredSceneHostIdentifier:"
- "setPreferredSceneHostIdentity:"
- "setPrefersProcessTaskSuspensionWhileSceneForeground:"
- "setPrefetchedKeys:"
- "setPreviousSettings:"
- "setPrivacySensitive:"
- "setProcess:"
- "setPropagatedSettings:"
- "setPropagating:"
- "setProvisions:"
- "setQueue:"
- "setReason:"
- "setRebootType:"
- "setReferenceFrame:"
- "setRefreshRate:"
- "setReportType:"
- "setRequestHandler:"
- "setRequestUserConfirmation:"
- "setRequiresSecureCoding:"
- "setRotationDirection:"
- "setRunningBoardAssertionDisabled:"
- "setScale:"
- "setScene:"
- "setSceneID:"
- "setSchedulingPolicy:"
- "setSelector:"
- "setSequenceNumber:"
- "setServer:"
- "setService:"
- "setServiceQuality:"
- "setSettings:"
- "setSettingsDiff:"
- "setShowArchiveOption:"
- "setShowsArchiveOption:"
- "setSnapshotSize:"
- "setSource:"
- "setSpecification:"
- "setStrategy:"
- "setStrategyName:"
- "setSupportedCodings:"
- "setSupportedInterfaceOrientations:"
- "setTimeout:"
- "setTransitionContext:"
- "setTransitionHandler:"
- "setTransitionReasons:"
- "setUIApplicationElement:"
- "setUIKitMainLike"
- "setUnderlyingError:"
- "setUniqueIdentifier:"
- "setUpdateCompletions:"
- "setUpdateContext:"
- "setUseDebugDescription:"
- "setUserInfoValue:forKey:"
- "setUserInitiated:"
- "setValue:forKey:"
- "setValue:forProperty:"
- "setVolatile:"
- "setWatchdogTransitionContext:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWorkspaceIdentifier:"
- "setter"
- "settingChangedForKey:"
- "settingForProperty:"
- "settingForSubclassProperty:"
- "settingNames:"
- "settingWithName:settingsClass:extension:local:type:legacySetting:expectedClass:"
- "settings:"
- "settings:appendDescriptionToBuilder:forFlag:object:ofSetting:"
- "settings:keyDescriptionForSetting:"
- "settings:valueDescriptionForFlag:object:ofSetting:"
- "settingsByApplyingToMutableCopyOfSettings:"
- "settingsExtensions"
- "sharedConnection"
- "sharedInstance"
- "sharedMonitorForDisplayType:"
- "sharedService"
- "shortValue"
- "shortVersionString"
- "shouldAllowClientConnection:withMessage:"
- "shouldPreventLaunch"
- "showsArchiveOption"
- "shutdown"
- "shutdownWithOptions:"
- "siblingComponentOfClass:"
- "signal"
- "signalWithContext:"
- "signatureVersion"
- "signatureVersion:version:"
- "signatureVersionForApp:"
- "signatureWithObjCTypes:"
- "size"
- "sliceWithType:"
- "sliceWithType:subtype:"
- "snapshotRequest"
- "snapshotRequest:performWithContext:"
- "snapshotRequestAllowSnapshot:"
- "snapshotSize"
- "softLinkExtensionFrameworkInClient"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "sourceIdentifierForHostEndpoint:"
- "startService"
- "startViewServiceDomain"
- "startWorkspaceDomainListener"
- "started"
- "stopMonitoring"
- "storeForApplication:"
- "storeForApplicationIdentifier:"
- "storeForApplicationIdentity:"
- "strategyForSchedulingPolicy:graphicsPolicy:jetsamPolicy:"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringForKey:"
- "stringRepresentation"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToStrongObjectsMapTable"
- "structFlattenedMembers"
- "subclassExtension"
- "subclassExtensions"
- "substringFromIndex:"
- "substringToIndex:"
- "subtype"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "succinctDescriptionForObject:"
- "supportedInterfaceOrientations"
- "supportsAllInterfaceOrientations"
- "supportsBSXPCSecureCoding"
- "supportsBackgroundMode:"
- "supportsDeviceFamily:"
- "supportsExtendedColor"
- "supportsInterfaceOrientation:"
- "supportsMultiwindow"
- "supportsSecureCoding"
- "suppressLayoutForReason:"
- "synchronize"
- "synchronize:"
- "synchronizeWithCompletion:"
- "systemApplicationBundleIdentifier"
- "targetDescription"
- "targetForInvocation:"
- "targetWithInterface:handler:"
- "targetsClientEndpoint"
- "taskNameForPID:"
- "taskNameRight"
- "taskState"
- "teamID"
- "teamIdentifier"
- "tentativeUninstall"
- "terminateApplication:forReason:andReport:withDescription:"
- "terminateApplication:forReason:andReport:withDescription:completion:"
- "terminateApplicationGroup:forReason:andReport:withDescription:"
- "terminateApplicationGroup:forReason:andReport:withDescription:completion:"
- "terminationAssertionContext"
- "threadDictionary"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "tokenForCurrentProcess"
- "tokenWithHostEndpoint:workspace:identifier:"
- "tokenWithHostPID:directEndpointTarget:workspace:identifier:"
- "tokenWithHostPID:viewServiceSessionIdentifier:"
- "transformDisplayConfiguration:"
- "transientLocalClientSettings"
- "transientLocalSettings"
- "transition context deallocated with dangling completions"
- "transitionAssertionWithReason:"
- "transitionContextExtensions"
- "transitionHandler"
- "transitionReason"
- "transitioning"
- "trust states for %@ - legacy: %@, modern: %@, authoritative: %@"
- "trustStateForApplication:"
- "trustedCodeSigningIdentities"
- "typeIdentifier"
- "typeof (((typeof (MCManagedAppsChangedNotification) (*)(void))0)()) getMCManagedAppsChangedNotification(void)"
- "unauthoritativeTrustState"
- "uninstallAppWithIdentity:options:completion:"
- "uninstallApplication:completion:"
- "uninstallApplication:withOptions:completion:"
- "uninstallApplicationIdentity:withOptions:completion:"
- "uninstalling"
- "unionOrderedSet:"
- "unionSet:"
- "uniqueIdentifier"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateClientSettings:"
- "updateClientSettings:withTransitionContext:"
- "updateClientSettingsWithBlock:"
- "updateClientSettingsWithTransitionBlock:"
- "updateContext"
- "updateHandler:"
- "updateLayout:withTransition:"
- "updateProgress"
- "updateSettings:"
- "updateSettingsWithBlock:"
- "updateTransformsWithCompletion:"
- "updater:didReceiveActions:forExtension:"
- "updater:didReceiveMessage:withResponse:"
- "updater:didUpdateSettings:withDiff:transitionContext:completion:"
- "userInfo"
- "userInteractive"
- "userInteractiveWithoutUI"
- "v16@0:8"
- "v16@?0@\"FBSOrientationUpdate\"8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8c16"
- "v24@0:8#16"
- "v24@0:8:16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"<FBSApplicationDataStoreRepositoryClientObserver>\"16"
- "v24@0:8@\"<FBSComponentScene>\"16"
- "v24@0:8@\"<FBSDisplayLayoutPublisherObserving>\"16"
- "v24@0:8@\"<FBSceneClientProcess>\"16"
- "v24@0:8@\"BKSAnimationFenceHandle\"16"
- "v24@0:8@\"BSAnimationSettings\"16"
- "v24@0:8@\"BSKeyedSettings\"16"
- "v24@0:8@\"BSProcessHandle\"16"
- "v24@0:8@\"BSServiceConnectionEndpoint\"16"
- "v24@0:8@\"BSServiceInterface\"16"
- "v24@0:8@\"BSServiceQuality\"16"
- "v24@0:8@\"FBProcessExecutionContext\"16"
- "v24@0:8@\"FBSDisplayConfiguration\"16"
- "v24@0:8@\"FBSInvocation\"16"
- "v24@0:8@\"FBSOrientationObserverClient\"16"
- "v24@0:8@\"FBSScene\"16"
- "v24@0:8@\"FBSSceneActivitySession\"16"
- "v24@0:8@\"FBSSceneIdentityToken\"16"
- "v24@0:8@\"FBSSceneSpecification\"16"
- "v24@0:8@\"FBSSceneUpdate\"16"
- "v24@0:8@\"FBSceneUpdateContext\"16"
- "v24@0:8@\"FBWatchdogTransitionContext\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSObject<BSXPCDecoding>\"16"
- "v24@0:8@\"NSObject<BSXPCEncoding>\"16"
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"RBSProcessHandle\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<@\"NSSet\"@?@\"FBSScene\"@\"NSSet\">16"
- "v24@0:8@?<@\"NSString\"@?@>16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"FBSMutableSceneParameters\">16"
- "v24@0:8@?<v@?@\"FBSScene\">16"
- "v24@0:8@?<v@?@\"FBSScene\"@\"FBSSceneUpdate\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@?0@\"FBSOrientationUpdate\"8@\"NSError\"16"
- "v24@?0q8q16"
- "v28@0:8@16B24"
- "v28@0:8@16I24"
- "v28@0:8i16@?20"
- "v32@0:8#16@24"
- "v32@0:8:16@?24"
- "v32@0:8@\"<FBSApplicationDataStoreRepositoryClient>\"16@\"NSString\"24"
- "v32@0:8@\"<FBSSceneAgent>\"16@?<v@?@\"FBSSceneMessage\"@?<v@?@\"FBSSceneMessage\">>24"
- "v32@0:8@\"BSServiceConnectionEndpointMonitor\"16@\"BSServiceConnectionEndpoint\"24"
- "v32@0:8@\"FBSOrientationObserverClient\"16@\"FBSOrientationUpdate\"24"
- "v32@0:8@\"FBSProcessExecutionProvision\"16@\"NSError\"24"
- "v32@0:8@\"FBSProcessTerminationRequest\"16@\"FBSProcessWatchdog\"24"
- "v32@0:8@\"FBSScene\"16@\"FBSInvocation\"24"
- "v32@0:8@\"FBSScene\"16@\"FBSSceneHostHandle\"24"
- "v32@0:8@\"FBSScene\"16@\"FBSSceneTransitionContext\"24"
- "v32@0:8@\"FBSScene\"16@\"FBSSceneUpdate\"24"
- "v32@0:8@\"FBSScene\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"FBSWorkspaceSceneRequestOptions\"16@?<v@?@\"FBSScene\"@\"NSError\">24"
- "v32@0:8@\"FBSXPCMessage\"16q24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16#24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16#24"
- "v32@0:8@16:24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^v24"
- "v32@0:8@16q24"
- "v32@0:8@?16@24"
- "v32@0:8@?16q24"
- "v32@0:8Q16@?24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@16i24@?28"
- "v36@0:8B16@20@28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"<FBSSceneAgent>\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\"@\"NSError\">32"
- "v40@0:8@\"<FBSSceneHandle>\"16@\"FBSSceneEvent\"24@?<v@?>32"
- "v40@0:8@\"<FBSSceneHandle>\"16@\"FBSSceneEvent\"24@?<v@?@\"FBSSceneMessage\">32"
- "v40@0:8@\"<FBSSceneHandle>\"16@\"FBSSceneEvent\"24@?<v@?@?<v@?@\"FBSSceneMessage\"@\"NSError\">>32"
- "v40@0:8@\"<FBSSceneUpdater>\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\">32"
- "v40@0:8@\"<FBSSceneUpdater>\"16@\"NSSet\"24#32"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@\"FBSScene\"16@\"FBSSceneMessage\"24@?<v@?@\"FBSSceneMessage\"@\"NSError\">32"
- "v40@0:8@\"FBSScene\"16@\"NSSet\"24#32"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16#24@?32"
- "v40@0:8@16@24#32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8@?16@?24@?32"
- "v40@0:8Q16@24@32"
- "v40@0:8i16@?20@?28B36"
- "v40@0:8{?=qQQ}16"
- "v44@0:8@16@24I32@?36"
- "v44@0:8@16q24B32@36"
- "v44@0:8B16q20{CGSize=dd}28"
- "v44@0:8q16@?24@?32B40"
- "v44@0:8q16q24B32@36"
- "v48@0:8@\"<FBSApplicationDataStoreRepositoryClient>\"16@\"NSString\"24@32@\"NSString\"40"
- "v48@0:8@\"FBSScene\"16@\"FBSSceneClientSettings\"24@\"FBSSceneClientSettingsDiff\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@\"FBSXPCMessage\"16q24@?<v@?@\"FBSXPCMessage\">32B40d44"
- "v52@0:8@16@24@32I40@?44"
- "v52@0:8@16q24@?32B40d44"
- "v52@0:8@16q24B32@36@?44"
- "v52@0:8q16q24B32@36@?44"
- "v56@0:8@\"<FBSSceneUpdater>\"16@\"FBSSceneSettings\"24@\"FBSSceneSettingsDiff\"32@\"FBSSceneTransitionContext\"40@?<v@?@\"FBSWorkspaceSceneUpdateResponse\">48"
- "v56@0:8@16@24@32@40@?48"
- "v96@0:8{CGSize=dd}16{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64"
- "validateSignatureForPath:options:userInfo:"
- "valueDescriptionForFlag:object:ofSetting:"
- "valueForKey:"
- "valueForProperty:expectedClass:"
- "valueForSetting:"
- "valueForUndefinedSetting:"
- "valueWithBytes:objCType:"
- "valueWithCATransform3D:"
- "valueWithPointer:"
- "valueWithWeakObject:"
- "versionedPID"
- "viewServiceConfiguration"
- "void *ManagedConfigurationLibrary(void)"
- "void *SecurityLibrary(void)"
- "void soft_MISValidateUPP(CFStringRef, __strong dispatch_queue_t, void (^__strong)(MISState, int64_t))"
- "wantsConnectionDebouncing"
- "wasBuiltWithTSAN"
- "wasBuiltWithThreadSanitizer"
- "watchdogTransitionContext"
- "we failed to make a main display for %@ - created raw configuration=%@"
- "weakObjectValue"
- "weakObjectsHashTable"
- "weakToStrongObjectsMapTable"
- "willTerminateWithTransitionContext:"
- "workspace:didCreateScene:withTransitionContext:completion:"
- "workspace:didReceiveActions:"
- "workspace:willDestroyScene:withTransitionContext:completion:"
- "workspaceID:sendActions:completion:"
- "workspaceIdentifier"
- "workspaceService"
- "workspaceShouldExit:withTransitionContext:"
- "z5G/N9jcMdgPm8UegLwbKg"
- "zone"
- "{?=\"type\"q\"value\"Q\"reserved\"Q}"
- "{?=qQQ}16@0:8"
- "{CATransform3D=\"m11\"d\"m12\"d\"m13\"d\"m14\"d\"m21\"d\"m22\"d\"m23\"d\"m24\"d\"m31\"d\"m32\"d\"m33\"d\"m34\"d\"m41\"d\"m42\"d\"m43\"d\"m44\"d}"
- "{CATransform3D=dddddddddddddddd}16@0:8"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\xdaA"

```
