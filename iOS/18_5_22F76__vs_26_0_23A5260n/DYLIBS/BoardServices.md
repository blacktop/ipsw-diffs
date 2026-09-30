## BoardServices

> `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`

```diff

-694.5.5.0.0
-  __TEXT.__text: 0x49cd8
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x1a04
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x8f68
-  __TEXT.__cstring: 0x5903
-  __TEXT.__oslogstring: 0x2005
-  __TEXT.__dlopen_cstrs: 0x2ca
-  __TEXT.__unwind_info: 0x1758
-  __TEXT.__objc_classname: 0x79a
-  __TEXT.__objc_methname: 0x3c15
-  __TEXT.__objc_methtype: 0x12f5
-  __TEXT.__objc_stubs: 0x2340
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__objc_classlist: 0x118
+731.0.0.0.0
+  __TEXT.__text: 0x5e968
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x21c4
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0xbc4c
+  __TEXT.__cstring: 0x65cb
+  __TEXT.__oslogstring: 0x250c
+  __TEXT.__dlopen_cstrs: 0x330
+  __TEXT.__unwind_info: 0x1e10
+  __TEXT.__objc_classname: 0xafe
+  __TEXT.__objc_methname: 0x4939
+  __TEXT.__objc_methtype: 0x15e4
+  __TEXT.__objc_stubs: 0x2760
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x12e8
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf58
+  __DATA_CONST.__objc_selrefs: 0x1240
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x4500
-  __AUTH_CONST.__objc_const: 0x4888
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__objc_const: 0x5b20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x3e8
-  __DATA.__data: 0xcc0
-  __DATA.__bss: 0x8
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x20
-  __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__bss: 0x148
-  __DATA_DIRTY.__common: 0x50
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x46c
+  __DATA.__data: 0x1200
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__objc_ivar: 0x54
+  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A7671F1-E9FD-34FB-9B2C-AE112624BA0C
-  Functions: 719
-  Symbols:   3229
-  CStrings:  2291
+  UUID: CDDE8BC0-1E8A-3B27-94F0-333EE3C98D87
+  Functions: 933
+  Symbols:   4053
+  CStrings:  2733
 
Symbols:
+ +[BSRBSService _sharedInstanceCreatingIfNecessary:]
+ +[BSRBSService _sharedTestInstance]
+ +[BSRBSService debugDescriptionWithMultilinePrefix:]
+ +[BSRBSService debugDescription]
+ +[BSServiceCompoundQueue queueWithDispatchQueue:targetQueue:]
+ +[BSServiceConnection _connectionWithEndpoint:muxer:clientContextBuilder:]
+ +[BSServiceConnectionEndpoint _endpointForDomain:service:instance:]
+ +[BSServiceConnectionEndpoint endpointForMachName:targetUserIdentifier:service:instance:]
+ +[BSServiceConnectionListener _listenerWithManager:configuration:handler:]
+ +[BSServiceConnectionListener listenerWithConfiguration:handler:]
+ +[BSServiceConnectionListenerConfiguration configurationWithDomain:service:]
+ +[BSServiceConnectionListenerConfiguration configurationWithDomain:service:instance:]
+ +[BSServiceDispatchQueue _queueOfDispatchQueue:]
+ +[BSServiceDispatchQueue _queueWithDispatchQueue:]
+ +[BSServiceDispatchQueue mainQueue]
+ +[BSServiceDispatchQueue queueWithName:]
+ +[BSServiceDispatchQueue queueWithName:serviceQuality:]
+ +[BSServiceDispatchQueue queueWithName:serviceQuality:targetQueue:]
+ +[BSServiceDispatchQueue queueWithName:targetQueue:]
+ +[BSServiceInitiatingConnectionMultiplexer _defaultInstanceCreatingIfNecessary:]
+ +[BSServiceInitiatingConnectionMultiplexer _userInteractiveInstanceCreatingIfNecessary:]
+ +[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]
+ +[BSServiceInitiatingConnectionMultiplexer debugDescription]
+ +[BSServiceInitiatingConnectionMultiplexer defaultMultiplexer]
+ +[BSServiceInitiatingConnectionMultiplexer userInteractiveMultiplexer]
+ +[BSServiceInterface interfaceWithIdentifier:]
+ +[BSServiceInterface interfaceWithIdentifier:configurator:]
+ +[BSServiceListenerConnection _connectionFromIncomingConnection:requiresMessagingAfterHandshake:]
+ +[BSServiceListenerConnectionRevocationEvent eventForImplicit:]
+ +[BSServiceMainRunLoopQueue commonModesQueue]
+ +[BSServiceMainRunLoopQueue queueWithModes:]
+ +[BSServiceManager _sharedInstanceCreatingIfNecessary:]
+ +[BSServiceManager sharedInstanceIfCreated]
+ +[BSServiceManager sharedInstance]
+ +[BSServiceManager validateDynamicConfiguration:withDebugInfo:]
+ +[BSServiceQueue mainDispatchQueue]
+ +[BSServiceQueue queueWithDispatchQueue:]
+ +[BSServiceQueue queueWithMainRunLoopModes:]
+ +[BSServiceReplyFallbackQueue _queueWithReplyQueue:serviceQueue:]
+ +[BSServicesConfiguration _bootstrapConfigOfService:withEnv:info:]
+ +[BSServicesConfiguration _configOfService:fromPlist:isViewService:postfixBlock:]
+ +[BSServicesConfiguration _configOfService:withViewServiceDomainsDictionary:]
+ +[BSXPCServiceConnection _invalidateIncomingXPCConnection:withDisconnectMessage:]
+ +[BSXPCServiceConnection connectionWithEndpoint:]
+ +[BSXPCServiceConnectionEndpoint nullEndpoint]
+ +[BSXPCServiceConnectionListener listenerForSpecification:]
+ +[BSXPCServiceConnectionRootClientContext uniqueClientContextWithEndpoint:]
+ -[BSNSXPCTransport _setSendingQueue:]
+ -[BSNSXPCTransport setEventObserver:]
+ -[BSNSXPCTransport setSendingQueue:]
+ -[BSRBSService .cxx_destruct]
+ -[BSRBSService _callOutLock_noteEndpointsChangedForServices:]
+ -[BSRBSService debugDescriptionWithMultilinePrefix:]
+ -[BSRBSService debugDescription]
+ -[BSRBSService descriptionBuilderWithMultilinePrefix:]
+ -[BSRBSService descriptionWithMultilinePrefix:]
+ -[BSRBSService launchIdentifiersForMachName:]
+ -[BSRBSService registerMonitor:]
+ -[BSRBSService service:didLoseInheritances:]
+ -[BSRBSService service:didReceiveInheritances:]
+ -[BSRBSService succinctDescriptionBuilder]
+ -[BSRBSService succinctDescription]
+ -[BSService registerListener:forInstance:]
+ -[BSServiceCompoundQueue .cxx_destruct]
+ -[BSServiceCompoundQueue _performAsync:withHandoff:]
+ -[BSServiceCompoundQueue _xpcReplyQueue]
+ -[BSServiceCompoundQueue _xpcReplyQueue_performReply:]
+ -[BSServiceCompoundQueue assertBarrierOnQueue]
+ -[BSServiceCompoundQueue description]
+ -[BSServiceCompoundQueue dispatchQueue]
+ -[BSServiceCompoundQueue hash]
+ -[BSServiceCompoundQueue isEqual:]
+ -[BSServiceCompoundQueue performAfter:withBlock:]
+ -[BSServiceCompoundQueue performAsync:]
+ -[BSServiceCompoundQueue targetQueue]
+ -[BSServiceConnection _config:]
+ -[BSServiceConnection _connection]
+ -[BSServiceConnection _extractNSXPCConnectionWithConfigurator:assertionProvider:]
+ -[BSServiceConnection _initWithConfiguration:]
+ -[BSServiceConnection isValid]
+ -[BSServiceConnection loggingProem]
+ -[BSServiceConnection(NSXPCConnection) extractNSXPCConnectionWithViewServiceConfigurator:]
+ -[BSServiceConnectionEndpoint RBSTarget]
+ -[BSServiceConnectionEndpoint _initWithEndpoint:service:instance:]
+ -[BSServiceConnectionEndpoint _injectorDescription]
+ -[BSServiceConnectionEndpointInjectorConfiguration .cxx_destruct]
+ -[BSServiceConnectionEndpointInjectorConfiguration addEndpoint:]
+ -[BSServiceConnectionEndpointInjectorConfiguration init]
+ -[BSServiceConnectionEndpointInjectorConfiguration setAdditionalAttributes:]
+ -[BSServiceConnectionEndpointInjectorConfiguration setDomain:]
+ -[BSServiceConnectionEndpointInjectorConfiguration setInheritingEnvironment:]
+ -[BSServiceConnectionEndpointInjectorConfiguration setInstance:]
+ -[BSServiceConnectionEndpointInjectorConfiguration setService:]
+ -[BSServiceConnectionEndpointInjectorConfiguration setTarget:]
+ -[BSServiceConnectionListener specification]
+ -[BSServiceConnectionListenerConfiguration .cxx_destruct]
+ -[BSServiceConnectionListenerConfiguration initWithConfigurator:]
+ -[BSServiceConnectionListenerConfiguration setDelegate:]
+ -[BSServiceConnectionListenerConfiguration setDomain:]
+ -[BSServiceConnectionListenerConfiguration setInstance:]
+ -[BSServiceConnectionListenerConfiguration setService:]
+ -[BSServiceDispatchQueue .cxx_destruct]
+ -[BSServiceDispatchQueue _initWithQueue:asUserInteractive:shouldAssociate:]
+ -[BSServiceDispatchQueue _performAsync:withHandoff:]
+ -[BSServiceDispatchQueue _xpcReplyQueue]
+ -[BSServiceDispatchQueue _xpcReplyQueue_performReply:]
+ -[BSServiceDispatchQueue assertBarrierOnQueue]
+ -[BSServiceDispatchQueue description]
+ -[BSServiceDispatchQueue hash]
+ -[BSServiceDispatchQueue isEqual:]
+ -[BSServiceDispatchQueue performAfter:withBlock:]
+ -[BSServiceDispatchQueue performAsync:]
+ -[BSServiceDispatchQueue performAsyncAndWait:]
+ -[BSServiceDispatchQueue queue]
+ -[BSServiceDomain endpoint]
+ -[BSServiceDomain serviceWithIdentifier:]
+ -[BSServiceDomainSpecification _initWithIdentifier:machName:multiplexingType:xpcSubserviceName:start:launchIdentifiers:servicesByIdentifier:derivedServiceRestrictions:enableIfFeatureFlags:disableIfFeatureFlags:]
+ -[BSServiceDomainSpecification launchIdentifiers]
+ -[BSServiceDomainSpecification multiplexingType]
+ -[BSServiceInitiatingConnection _configure:]
+ -[BSServiceInitiatingConnection _initWithEndpoint:options:]
+ -[BSServiceInitiatingConnection configure:]
+ -[BSServiceInitiatingConnection initWithEndpoint:]
+ -[BSServiceInitiatingConnection initWithEndpoint:options:]
+ -[BSServiceInitiatingConnection remoteTargetWithLaunchingAssertionAttributes:]
+ -[BSServiceInitiatingConnectionMultiplexer .cxx_destruct]
+ -[BSServiceInitiatingConnectionMultiplexer _initAsUserInteractive:]
+ -[BSServiceInitiatingConnectionMultiplexer dealloc]
+ -[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]
+ -[BSServiceInitiatingConnectionMultiplexer debugDescription]
+ -[BSServiceInitiatingConnectionMultiplexer descriptionBuilderWithMultilinePrefix:]
+ -[BSServiceInitiatingConnectionMultiplexer descriptionWithMultilinePrefix:]
+ -[BSServiceInitiatingConnectionMultiplexer init]
+ -[BSServiceInitiatingConnectionMultiplexer newConnectionWithEndpoint:]
+ -[BSServiceInitiatingConnectionMultiplexer succinctDescriptionBuilder]
+ -[BSServiceInitiatingConnectionMultiplexer succinctDescription]
+ -[BSServiceListenerConnection _configure:]
+ -[BSServiceListenerConnection addEventObserver:]
+ -[BSServiceListenerConnection cancel]
+ -[BSServiceListenerConnection configure:]
+ -[BSServiceListenerConnection initiatingContext]
+ -[BSServiceListenerConnection isRevoked]
+ -[BSServiceListenerConnectionRevocationEvent isExplicitInitiatorInvalidation]
+ -[BSServiceMainRunLoopQueue .cxx_destruct]
+ -[BSServiceMainRunLoopQueue _initWithModes:]
+ -[BSServiceMainRunLoopQueue _performAsync:withHandoff:]
+ -[BSServiceMainRunLoopQueue _queue_performAsync:]
+ -[BSServiceMainRunLoopQueue assertBarrierOnQueue]
+ -[BSServiceMainRunLoopQueue dealloc]
+ -[BSServiceMainRunLoopQueue description]
+ -[BSServiceMainRunLoopQueue isEqual:]
+ -[BSServiceMainRunLoopQueue performAfter:withBlock:]
+ -[BSServiceMainRunLoopQueue performAsync:]
+ -[BSServiceManager RBSService]
+ -[BSServiceManager dealloc]
+ -[BSServiceQueue _performAsync:withHandoff:]
+ -[BSServiceQueue _xpcReplyQueue]
+ -[BSServiceQueue _xpcReplyQueue_performReply:]
+ -[BSServiceQueue assertBarrierOnQueue]
+ -[BSServiceQueue assertOnQueue]
+ -[BSServiceQueue init]
+ -[BSServiceQueue performAfter:withBlock:]
+ -[BSServiceQueue performAsync:]
+ -[BSServiceReplyFallbackQueue .cxx_destruct]
+ -[BSServiceReplyFallbackQueue _performAsync:withHandoff:]
+ -[BSServiceReplyFallbackQueue _xpcReplyQueue]
+ -[BSServiceReplyFallbackQueue _xpcReplyQueue_performReply:]
+ -[BSServiceReplyFallbackQueue assertBarrierOnQueue]
+ -[BSServiceReplyFallbackQueue description]
+ -[BSServiceReplyFallbackQueue hash]
+ -[BSServiceReplyFallbackQueue isEqual:]
+ -[BSServiceReplyFallbackQueue performAfter:withBlock:]
+ -[BSServiceReplyFallbackQueue performAsync:]
+ -[BSServicesConfigurationRegistration .cxx_destruct]
+ -[BSServicesConfigurationRegistration configuration]
+ -[BSServicesConfigurationRegistration descriptionBuilderWithMultilinePrefix:]
+ -[BSServicesConfigurationRegistration descriptionWithMultilinePrefix:]
+ -[BSServicesConfigurationRegistration description]
+ -[BSServicesConfigurationRegistration invalidate]
+ -[BSServicesConfigurationRegistration succinctDescriptionBuilder]
+ -[BSServicesConfigurationRegistration succinctDescription]
+ -[BSXPCServiceConnection _clientInvalidateWithType:]
+ -[BSXPCServiceConnection _defaultNameWithClientLoggingProem:as:onLock:]
+ -[BSXPCServiceConnection _handleParentDisconnectWithMessage:outRevocations:]
+ -[BSXPCServiceConnection _lock_invalidateWithDisconnectMessage:outChildRevocations:]
+ -[BSXPCServiceConnection _noteChildConnectionDidInvalidate:]
+ -[BSXPCServiceConnection activatedConnectionQueue]
+ -[BSXPCServiceConnection addObserverWithReason:forRevocation:]
+ -[BSXPCServiceConnection cancel]
+ -[BSXPCServiceConnection childrenGeneration]
+ -[BSXPCServiceConnection defaultNameWithClientLoggingProem:as:]
+ -[BSXPCServiceConnection isRevokedPeer]
+ -[BSXPCServiceConnection isValid]
+ -[BSXPCServiceConnection loggingProem]
+ -[BSXPCServiceConnection stateDump]
+ -[BSXPCServiceConnectionEndpoint .cxx_destruct]
+ -[BSXPCServiceConnectionEndpoint RBSTarget]
+ -[BSXPCServiceConnectionEndpoint _initWithXPCEndpoint:oneshot:nonLaunching:targetPID:withTargetDescription:]
+ -[BSXPCServiceConnectionEndpoint compare:]
+ -[BSXPCServiceConnectionEndpoint copyWithZone:]
+ -[BSXPCServiceConnectionEndpoint debugDescription]
+ -[BSXPCServiceConnectionEndpoint description]
+ -[BSXPCServiceConnectionEndpoint hash]
+ -[BSXPCServiceConnectionEndpoint initWithXPCEndpoint:oneshot:nonLaunching:targetPID:targetDescription:]
+ -[BSXPCServiceConnectionEndpoint init]
+ -[BSXPCServiceConnectionEndpoint isEqual:]
+ -[BSXPCServiceConnectionEndpoint isNullEndpoint]
+ -[BSXPCServiceConnectionEventHandler connectionHandleNoMoreChildren:withGeneration:]
+ -[BSXPCServiceConnectionEventHandler setCalloutContext:]
+ -[BSXPCServiceConnectionEventHandler setQueue:]
+ -[BSXPCServiceConnectionEventObservers .cxx_destruct]
+ -[BSXPCServiceConnectionEventObservers clearRevocations]
+ -[BSXPCServiceConnectionEventObservers consumeRevocations:]
+ -[BSXPCServiceConnectionEventObservers init]
+ -[BSXPCServiceConnectionListener _noteChildConnectionDidInvalidate:]
+ -[BSXPCServiceConnectionRootClientContext .cxx_destruct]
+ -[BSXPCServiceConnectionRootClientContext isClient]
+ -[BSXPCServiceConnectionRootClientContext isNonLaunching]
+ -[NSXPCConnection(BSNSXPCMessageSession) externalMessageSessionController]
+ -[_BSNSXPCCallbackTracking .cxx_destruct]
+ -[_BSNSXPCCallbackTracking captureConnection]
+ -[_BSNSXPCCallbackTracking dealloc]
+ -[_BSNSXPCCallbackTracking init]
+ -[_BSNSXPCCallbackTracking isInvalidationStillPending]
+ -[_BSNSXPCCallbackTracking sendError:isOnQueue:]
+ -[_BSNSXPCConnectionEvent description]
+ -[_BSNSXPCConnectionEvent init]
+ -[_BSNSXPCConnectionEvent isKnownToBeOnQueue]
+ -[_BSNSXPCConnectionEvent isLocalCancel]
+ -[_BSNSXPCConnectionEvent isPermanent]
+ -[_BSServiceConnectionConfiguration encodeContext:]
+ -[_BSServiceConnectionConfiguration init]
+ -[_BSServiceConnectionConfiguration setMultiplexer:]
+ -[_BSServiceConnectionConfiguration setQueue:]
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table95
+ _.str.140
+ _.str.218
+ _BSRBSAssertionGenerator_block_invoke
+ _BSServiceIsTesting
+ _BSServiceMainRunLoopSourceHandler
+ _BSServiceQualityFromBSServiceDomainMultiplexingType
+ _BSServiceSetIsTesting
+ _BSStringFromBOOL
+ _CFRelease
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFRunLoopSourceCreate
+ _CFRunLoopSourceInvalidate
+ _CFRunLoopSourceSignal
+ _CFRunLoopWakeUp
+ _NSAllMapTableValues
+ _NSRunLoopCommonModes
+ _NSStringFromBSServiceDomainMultiplexingType
+ _OBJC_CLASS_$_BSRBSService
+ _OBJC_CLASS_$_BSServiceCompoundQueue
+ _OBJC_CLASS_$_BSServiceConnectionEndpointInjectorConfiguration
+ _OBJC_CLASS_$_BSServiceConnectionListenerConfiguration
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceInitiatingConnection
+ _OBJC_CLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_CLASS_$_BSServiceListenerConnection
+ _OBJC_CLASS_$_BSServiceListenerConnectionRevocationEvent
+ _OBJC_CLASS_$_BSServiceMainRunLoopQueue
+ _OBJC_CLASS_$_BSServiceQueue
+ _OBJC_CLASS_$_BSServiceReplyFallbackQueue
+ _OBJC_CLASS_$_BSServicesConfigurationRegistration
+ _OBJC_CLASS_$_BSXPCServiceConnectionEndpoint
+ _OBJC_CLASS_$_BSXPCServiceConnectionEventObservers
+ _OBJC_CLASS_$_BSXPCServiceConnectionRootClientContext
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$__BSNSXPCCallbackTracking
+ _OBJC_CLASS_$__BSNSXPCConnectionEvent
+ _OBJC_IVAR_$_BSNSXPCTransport._callbackTracking
+ _OBJC_IVAR_$_BSNSXPCTransport._lock_cancelEnqueued
+ _OBJC_IVAR_$_BSNSXPCTransport._lock_cancelProcessed
+ _OBJC_IVAR_$_BSNSXPCTransport._queue
+ _OBJC_IVAR_$_BSNSXPCTransport._sendingQueue
+ _OBJC_IVAR_$_BSRBSService._callOutLock
+ _OBJC_IVAR_$_BSRBSService._callOutLock_serviceIdentifierToEndpointsToEnvironments
+ _OBJC_IVAR_$_BSRBSService._lock
+ _OBJC_IVAR_$_BSRBSService._lock_endpointToInheritances
+ _OBJC_IVAR_$_BSRBSService._lock_inheritanceToEndpoint
+ _OBJC_IVAR_$_BSRBSService._lock_machNameToLaunchIdentifiers
+ _OBJC_IVAR_$_BSRBSService._lock_serviceIdentifierToEndpoints
+ _OBJC_IVAR_$_BSRBSService._lock_serviceIdentifierToMonitors
+ _OBJC_IVAR_$_BSRBSService._underlying
+ _OBJC_IVAR_$_BSServiceConnectionEndpoint._underlyingEndpoint
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._description
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._lock_assertion
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._lock_invalidated
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_additionalAttributes
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_assertionGenerator
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_domain
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_endpoints
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_inheritingEnvironment
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_instance
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_manager
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_service
+ _OBJC_IVAR_$_BSServiceConnectionEndpointInjectorConfiguration._lock_target
+ _OBJC_IVAR_$_BSServiceConnectionEndpointMonitor._RBSService
+ _OBJC_IVAR_$_BSServiceConnectionListener._lock_handler
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock_configured
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock_delegate
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock_domain
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock_instance
+ _OBJC_IVAR_$_BSServiceConnectionListenerConfiguration._lock_service
+ _OBJC_IVAR_$_BSServiceDomainSpecification._launchIdentifiers
+ _OBJC_IVAR_$_BSServiceDomainSpecification._multiplexingType
+ _OBJC_IVAR_$_BSServiceDomainSpecification._xpcSubserviceName
+ _OBJC_IVAR_$_BSServiceInitiatingConnectionMultiplexer._lock
+ _OBJC_IVAR_$_BSServiceInitiatingConnectionMultiplexer._lock_endpointToOutgoingRootConnections
+ _OBJC_IVAR_$_BSServiceInitiatingConnectionMultiplexer._lock_invalidated
+ _OBJC_IVAR_$_BSServiceInitiatingConnectionMultiplexer._userInteractive
+ _OBJC_IVAR_$_BSServiceManager._dfMuxer
+ _OBJC_IVAR_$_BSServiceManager._lock_invalidated
+ _OBJC_IVAR_$_BSServiceManager._uiMuxer
+ _OBJC_IVAR_$_BSServiceQueue._userInteractive
+ _OBJC_IVAR_$_BSServicesConfigurationRegistration._configuration
+ _OBJC_IVAR_$_BSServicesConfigurationRegistration._registration
+ _OBJC_IVAR_$_BSXPCServiceConnection._lock_childrenGeneration
+ _OBJC_IVAR_$_BSXPCServiceConnection._lock_eventObservers
+ _OBJC_IVAR_$_BSXPCServiceConnection._lock_explicitlyRevoked
+ _OBJC_IVAR_$_BSXPCServiceConnectionEndpoint._nonLaunching
+ _OBJC_IVAR_$_BSXPCServiceConnectionEndpoint._oneshot
+ _OBJC_IVAR_$_BSXPCServiceConnectionEndpoint._targetDescription
+ _OBJC_IVAR_$_BSXPCServiceConnectionEndpoint._targetPID
+ _OBJC_IVAR_$_BSXPCServiceConnectionEndpoint._xpcEndpoint
+ _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._calloutContext
+ _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._queue
+ _OBJC_IVAR_$_BSXPCServiceConnectionEventObservers._lock
+ _OBJC_IVAR_$_BSXPCServiceConnectionEventObservers._lock_revocations
+ _OBJC_IVAR_$_BSXPCServiceConnectionListener._eDesc
+ _OBJC_IVAR_$_BSXPCServiceConnectionListener._isAnonymous
+ _OBJC_IVAR_$_BSXPCServiceConnectionListener._queue
+ _OBJC_IVAR_$_BSXPCServiceConnectionListener._specification
+ _OBJC_IVAR_$_BSXPCServiceConnectionRootClientContext._endpoint
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock_connection
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock_connectionReference
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock_errorHandler
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock_invalidated
+ _OBJC_IVAR_$__BSNSXPCCallbackTracking._lock_observer
+ _OBJC_IVAR_$__BSNSXPCConnectionEvent._code
+ _OBJC_IVAR_$__BSNSXPCConnectionEvent._onQueue
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._connection
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._instance
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._multiplexer
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._queue
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._queueOfTargetQueue
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._requiresMessagingAfterHandshake
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._service
+ _OBJC_IVAR_$__BSServiceConnectionConfiguration._state
+ _OBJC_METACLASS_$_BSRBSService
+ _OBJC_METACLASS_$_BSServiceCompoundQueue
+ _OBJC_METACLASS_$_BSServiceConnectionEndpointInjectorConfiguration
+ _OBJC_METACLASS_$_BSServiceConnectionListenerConfiguration
+ _OBJC_METACLASS_$_BSServiceDispatchQueue
+ _OBJC_METACLASS_$_BSServiceInitiatingConnection
+ _OBJC_METACLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_METACLASS_$_BSServiceListenerConnection
+ _OBJC_METACLASS_$_BSServiceListenerConnectionRevocationEvent
+ _OBJC_METACLASS_$_BSServiceMainRunLoopQueue
+ _OBJC_METACLASS_$_BSServiceQueue
+ _OBJC_METACLASS_$_BSServiceReplyFallbackQueue
+ _OBJC_METACLASS_$_BSServicesConfigurationRegistration
+ _OBJC_METACLASS_$_BSXPCServiceConnectionEndpoint
+ _OBJC_METACLASS_$_BSXPCServiceConnectionEventObservers
+ _OBJC_METACLASS_$_BSXPCServiceConnectionRootClientContext
+ _OBJC_METACLASS_$__BSNSXPCCallbackTracking
+ _OBJC_METACLASS_$__BSNSXPCConnectionEvent
+ __MergedGlobals.1
+ __OBJC_$_CATEGORY_NSXPCConnection_$_BSNSXPCMessageSession
+ __OBJC_$_CLASS_METHODS_BSRBSService
+ __OBJC_$_CLASS_METHODS_BSServiceCompoundQueue
+ __OBJC_$_CLASS_METHODS_BSServiceConnectionListenerConfiguration
+ __OBJC_$_CLASS_METHODS_BSServiceDispatchQueue
+ __OBJC_$_CLASS_METHODS_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_$_CLASS_METHODS_BSServiceMainRunLoopQueue
+ __OBJC_$_CLASS_METHODS_BSServiceQueue
+ __OBJC_$_CLASS_PROP_LIST_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_$_INSTANCE_METHODS_BSRBSService
+ __OBJC_$_INSTANCE_METHODS_BSServiceCompoundQueue
+ __OBJC_$_INSTANCE_METHODS_BSServiceConnectionEndpointInjectorConfiguration
+ __OBJC_$_INSTANCE_METHODS_BSServiceConnectionListenerConfiguration
+ __OBJC_$_INSTANCE_METHODS_BSServiceDispatchQueue
+ __OBJC_$_INSTANCE_METHODS_BSServiceInitiatingConnection
+ __OBJC_$_INSTANCE_METHODS_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_$_INSTANCE_METHODS_BSServiceListenerConnection
+ __OBJC_$_INSTANCE_METHODS_BSServiceListenerConnectionRevocationEvent
+ __OBJC_$_INSTANCE_METHODS_BSServiceMainRunLoopQueue
+ __OBJC_$_INSTANCE_METHODS_BSServiceQueue
+ __OBJC_$_INSTANCE_METHODS_BSServiceReplyFallbackQueue
+ __OBJC_$_INSTANCE_METHODS_BSServicesConfigurationRegistration
+ __OBJC_$_INSTANCE_METHODS_BSXPCServiceConnectionEndpoint
+ __OBJC_$_INSTANCE_METHODS_BSXPCServiceConnectionEventObservers
+ __OBJC_$_INSTANCE_METHODS_BSXPCServiceConnectionRootClientContext
+ __OBJC_$_INSTANCE_METHODS_NSXPCConnection(BSNSXPCMessageSession|forViewServicesOnly)
+ __OBJC_$_INSTANCE_METHODS__BSNSXPCCallbackTracking
+ __OBJC_$_INSTANCE_METHODS__BSNSXPCConnectionEvent
+ __OBJC_$_INSTANCE_VARIABLES_BSRBSService
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceCompoundQueue
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceConnectionEndpointInjectorConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceConnectionListenerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceDispatchQueue
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceMainRunLoopQueue
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceQueue
+ __OBJC_$_INSTANCE_VARIABLES_BSServiceReplyFallbackQueue
+ __OBJC_$_INSTANCE_VARIABLES_BSServicesConfigurationRegistration
+ __OBJC_$_INSTANCE_VARIABLES_BSXPCServiceConnectionEndpoint
+ __OBJC_$_INSTANCE_VARIABLES_BSXPCServiceConnectionEventObservers
+ __OBJC_$_INSTANCE_VARIABLES_BSXPCServiceConnectionRootClientContext
+ __OBJC_$_INSTANCE_VARIABLES__BSNSXPCCallbackTracking
+ __OBJC_$_INSTANCE_VARIABLES__BSNSXPCConnectionEvent
+ __OBJC_$_PROP_LIST_BSNSXPCConnectionHaltEvent
+ __OBJC_$_PROP_LIST_BSRBSService
+ __OBJC_$_PROP_LIST_BSServiceCompoundQueue
+ __OBJC_$_PROP_LIST_BSServiceConnectionContext_DEPRECATED
+ __OBJC_$_PROP_LIST_BSServiceDispatchQueue
+ __OBJC_$_PROP_LIST_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_$_PROP_LIST_BSServiceListenerConnection
+ __OBJC_$_PROP_LIST_BSServiceListenerConnectionRevocationEvent
+ __OBJC_$_PROP_LIST_BSServiceListenerConnectionRevocationEvent.45
+ __OBJC_$_PROP_LIST_BSServicesConfigurationRegistration
+ __OBJC_$_PROP_LIST__BSNSXPCConnectionEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSCancellable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDebugDescriptionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSNSXPCConnectionHaltEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSNSXPCConnectionInternalConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSNSXPCConnectionViewServiceConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSNSXPCSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionCommonConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionConfiguring_MessageBatching
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionContext_DEPRECATED
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionInitiatingOptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceInitiatingConnectionConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceListenerConnectionConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceListenerConnectionRevocationEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCServiceConnectionConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSCancellable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDebugDescriptionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSNSXPCConnectionHaltEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSNSXPCConnectionInternalConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSNSXPCConnectionViewServiceConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSNSXPCSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionCommonConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionConfiguring_MessageBatching
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionContext_DEPRECATED
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionInitiatingOptions
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceInitiatingConnectionConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceListenerConnectionConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceListenerConnectionRevocationEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCServiceConnectionConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSCancellable
+ __OBJC_$_PROTOCOL_REFS_BSDebugDescriptionProviding
+ __OBJC_$_PROTOCOL_REFS_BSNSXPCConnectionHaltEvent
+ __OBJC_$_PROTOCOL_REFS_BSNSXPCConnectionInternalConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSNSXPCConnectionViewServiceConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSNSXPCSending
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionConfiguring_MessageBatching
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionContext
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionHost
+ __OBJC_$_PROTOCOL_REFS_BSServiceInitiatingConnectionConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceInitiatingConnectionLegacyFrontBoardConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceListenerConnectionConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceListenerConnectionLegacyFrontBoardConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceListenerConnectionRevocationEvent
+ __OBJC_$_PROTOCOL_REFS_BSXPCServiceConnectionConfiguring
+ __OBJC_CLASS_PROTOCOLS_$_BSRBSService
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceConnectionEndpointInjectorConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceConnectionListenerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceDispatchQueue
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceInitiatingConnection
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceListenerConnection
+ __OBJC_CLASS_PROTOCOLS_$_BSServiceListenerConnectionRevocationEvent
+ __OBJC_CLASS_PROTOCOLS_$_BSServicesConfigurationRegistration
+ __OBJC_CLASS_PROTOCOLS_$_BSXPCServiceConnectionEndpoint
+ __OBJC_CLASS_PROTOCOLS_$__BSNSXPCConnectionEvent
+ __OBJC_CLASS_RO_$_BSRBSService
+ __OBJC_CLASS_RO_$_BSServiceCompoundQueue
+ __OBJC_CLASS_RO_$_BSServiceConnectionEndpointInjectorConfiguration
+ __OBJC_CLASS_RO_$_BSServiceConnectionListenerConfiguration
+ __OBJC_CLASS_RO_$_BSServiceDispatchQueue
+ __OBJC_CLASS_RO_$_BSServiceInitiatingConnection
+ __OBJC_CLASS_RO_$_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_CLASS_RO_$_BSServiceListenerConnection
+ __OBJC_CLASS_RO_$_BSServiceListenerConnectionRevocationEvent
+ __OBJC_CLASS_RO_$_BSServiceMainRunLoopQueue
+ __OBJC_CLASS_RO_$_BSServiceQueue
+ __OBJC_CLASS_RO_$_BSServiceReplyFallbackQueue
+ __OBJC_CLASS_RO_$_BSServicesConfigurationRegistration
+ __OBJC_CLASS_RO_$_BSXPCServiceConnectionEndpoint
+ __OBJC_CLASS_RO_$_BSXPCServiceConnectionEventObservers
+ __OBJC_CLASS_RO_$_BSXPCServiceConnectionRootClientContext
+ __OBJC_CLASS_RO_$__BSNSXPCCallbackTracking
+ __OBJC_CLASS_RO_$__BSNSXPCConnectionEvent
+ __OBJC_LABEL_PROTOCOL_$_BSCancellable
+ __OBJC_LABEL_PROTOCOL_$_BSDebugDescriptionProviding
+ __OBJC_LABEL_PROTOCOL_$_BSNSXPCConnectionHaltEvent
+ __OBJC_LABEL_PROTOCOL_$_BSNSXPCConnectionInternalConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSNSXPCConnectionViewServiceConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSNSXPCSending
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionCommonConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionConfiguring_MessageBatching
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionContext_DEPRECATED
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionInitiatingOptions
+ __OBJC_LABEL_PROTOCOL_$_BSServiceInitiatingConnectionConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceInitiatingConnectionLegacyFrontBoardConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceListenerConnectionConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceListenerConnectionLegacyFrontBoardConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceListenerConnectionRevocationEvent
+ __OBJC_LABEL_PROTOCOL_$_BSXPCServiceConnectionConfiguring
+ __OBJC_METACLASS_RO_$_BSRBSService
+ __OBJC_METACLASS_RO_$_BSServiceCompoundQueue
+ __OBJC_METACLASS_RO_$_BSServiceConnectionEndpointInjectorConfiguration
+ __OBJC_METACLASS_RO_$_BSServiceConnectionListenerConfiguration
+ __OBJC_METACLASS_RO_$_BSServiceDispatchQueue
+ __OBJC_METACLASS_RO_$_BSServiceInitiatingConnection
+ __OBJC_METACLASS_RO_$_BSServiceInitiatingConnectionMultiplexer
+ __OBJC_METACLASS_RO_$_BSServiceListenerConnection
+ __OBJC_METACLASS_RO_$_BSServiceListenerConnectionRevocationEvent
+ __OBJC_METACLASS_RO_$_BSServiceMainRunLoopQueue
+ __OBJC_METACLASS_RO_$_BSServiceQueue
+ __OBJC_METACLASS_RO_$_BSServiceReplyFallbackQueue
+ __OBJC_METACLASS_RO_$_BSServicesConfigurationRegistration
+ __OBJC_METACLASS_RO_$_BSXPCServiceConnectionEndpoint
+ __OBJC_METACLASS_RO_$_BSXPCServiceConnectionEventObservers
+ __OBJC_METACLASS_RO_$_BSXPCServiceConnectionRootClientContext
+ __OBJC_METACLASS_RO_$__BSNSXPCCallbackTracking
+ __OBJC_METACLASS_RO_$__BSNSXPCConnectionEvent
+ __OBJC_PROTOCOL_$_BSCancellable
+ __OBJC_PROTOCOL_$_BSDebugDescriptionProviding
+ __OBJC_PROTOCOL_$_BSNSXPCConnectionHaltEvent
+ __OBJC_PROTOCOL_$_BSNSXPCConnectionInternalConfiguring
+ __OBJC_PROTOCOL_$_BSNSXPCConnectionViewServiceConfiguring
+ __OBJC_PROTOCOL_$_BSNSXPCSending
+ __OBJC_PROTOCOL_$_BSServiceConnectionCommonConfiguring
+ __OBJC_PROTOCOL_$_BSServiceConnectionConfiguring_MessageBatching
+ __OBJC_PROTOCOL_$_BSServiceConnectionContext_DEPRECATED
+ __OBJC_PROTOCOL_$_BSServiceConnectionInitiatingOptions
+ __OBJC_PROTOCOL_$_BSServiceInitiatingConnectionConfiguring
+ __OBJC_PROTOCOL_$_BSServiceInitiatingConnectionLegacyFrontBoardConfiguring
+ __OBJC_PROTOCOL_$_BSServiceListenerConnectionConfiguring
+ __OBJC_PROTOCOL_$_BSServiceListenerConnectionLegacyFrontBoardConfiguring
+ __OBJC_PROTOCOL_$_BSServiceListenerConnectionRevocationEvent
+ __OBJC_PROTOCOL_$_BSXPCServiceConnectionConfiguring
+ ___102+[BSServiceConnection(NSXPCConnection) NSXPCConnectionWithEndpoint:clientContextBuilder:configurator:]_block_invoke
+ ___211-[BSServiceDomainSpecification _initWithIdentifier:machName:multiplexingType:xpcSubserviceName:start:launchIdentifiers:servicesByIdentifier:derivedServiceRestrictions:enableIfFeatureFlags:disableIfFeatureFlags:]_block_invoke
+ ___26-[BSNSXPCTransport cancel]_block_invoke_2
+ ___31-[BSServiceConnection activate]_block_invoke.247
+ ___31-[BSServiceConnection activate]_block_invoke.255
+ ___31-[BSServiceConnection activate]_block_invoke.259
+ ___31-[BSServiceConnection activate]_block_invoke.263
+ ___31-[BSServiceConnection activate]_block_invoke.264
+ ___31-[BSServiceConnection activate]_block_invoke.265
+ ___31-[BSServiceConnection activate]_block_invoke_2.249
+ ___32-[BSRBSService registerMonitor:]_block_invoke
+ ___35+[BSServiceDispatchQueue mainQueue]_block_invoke
+ ___35-[BSNSXPCTransport setTargetQueue:]_block_invoke_2
+ ___36+[BSServiceManager debugDescription]_block_invoke
+ ___37-[BSNSXPCTransport sendBarrierBlock:]_block_invoke
+ ___39-[BSServiceCompoundQueue performAsync:]_block_invoke
+ ___40-[BSServiceMainRunLoopQueue description]_block_invoke
+ ___41+[BSServiceQueue queueWithDispatchQueue:]_block_invoke
+ ___42-[BSService registerListener:forInstance:]_block_invoke
+ ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.101
+ ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.107
+ ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.111
+ ___42-[BSServiceDomain _initWithSpecification:]_block_invoke_2.103
+ ___42-[BSServiceMainRunLoopQueue performAsync:]_block_invoke
+ ___45+[BSServiceMainRunLoopQueue commonModesQueue]_block_invoke
+ ___45-[BSNSXPCTransport sendMessageWithReplySync:]_block_invoke
+ ___45-[BSNSXPCTransport sendMessageWithReplySync:]_block_invoke.207
+ ___45-[BSRBSService launchIdentifiersForMachName:]_block_invoke
+ ___45-[BSRBSService launchIdentifiersForMachName:]_block_invoke_2
+ ___46+[BSXPCServiceConnectionEndpoint nullEndpoint]_block_invoke
+ ___47-[BSRBSService service:didReceiveInheritances:]_block_invoke
+ ___48-[BSNSXPCTransport _sendMessage:asNotification:]_block_invoke_2
+ ___48-[BSServiceListenerConnection addEventObserver:]_block_invoke
+ ___48-[BSServiceListenerConnection addEventObserver:]_block_invoke_2
+ ___49+[BSServiceConnectionEndpointInjector _injector:]_block_invoke
+ ___49-[BSServiceCompoundQueue performAfter:withBlock:]_block_invoke
+ ___52-[BSRBSService debugDescriptionWithMultilinePrefix:]_block_invoke
+ ___52-[BSRBSService debugDescriptionWithMultilinePrefix:]_block_invoke_2
+ ___52-[BSRBSService debugDescriptionWithMultilinePrefix:]_block_invoke_3
+ ___52-[BSServiceCompoundQueue _performAsync:withHandoff:]_block_invoke
+ ___52-[BSServiceCompoundQueue _performAsync:withHandoff:]_block_invoke_2
+ ___52-[BSServiceMainRunLoopQueue performAfter:withBlock:]_block_invoke
+ ___54-[BSServiceManager extendAutomaticBootstrapCompletion]_block_invoke.125
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.212
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.217
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.225
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.229
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.230
+ ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke_2.231
+ ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke.45
+ ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke.47
+ ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke_2.48
+ ___58-[BSServiceMainRunLoopQueue _performNextFromRunLoopSource]_block_invoke
+ ___60-[BSXPCServiceConnection _noteChildConnectionDidInvalidate:]_block_invoke
+ ___61-[BSRBSService _callOutLock_noteEndpointsChangedForServices:]_block_invoke
+ ___62-[BSNSXPCTransport sendMessageWithReply:onQueue:replyHandler:]_block_invoke_2
+ ___62-[BSNSXPCTransport sendMessageWithReply:onQueue:replyHandler:]_block_invoke_3
+ ___62-[BSNSXPCTransport sendMessageWithReply:onQueue:replyHandler:]_block_invoke_4
+ ___62-[BSNSXPCTransport sendMessageWithReply:onQueue:replyHandler:]_block_invoke_5
+ ___62-[BSNSXPCTransport sendMessageWithReply:onQueue:replyHandler:]_block_invoke_6
+ ___63+[BSServiceListenerConnectionRevocationEvent eventForImplicit:]_block_invoke
+ ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.30
+ ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.33
+ ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.34
+ ___64+[BSServiceConnectionEndpointInjector injectorWithConfigurator:]_block_invoke
+ ___65+[BSServiceConnectionListener listenerWithConfiguration:handler:]_block_invoke
+ ___66+[BSServicesConfiguration _bootstrapConfigOfService:withEnv:info:]_block_invoke
+ ___69-[BSXPCServiceConnectionEventObservers addRevocationBlock:forReason:]_block_invoke
+ ___71+[BSServiceConnectionListener _listenerWithManager:legacyConfigurator:]_block_invoke
+ ___74+[BSServiceConnection _connectionWithEndpoint:muxer:clientContextBuilder:]_block_invoke
+ ___76+[BSServiceConnectionListenerConfiguration configurationWithDomain:service:]_block_invoke
+ ___76-[BSXPCServiceConnection _handleParentDisconnectWithMessage:outRevocations:]_block_invoke
+ ___77-[BSServicesConfigurationRegistration descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___79-[BSServiceManager _initWithRBSService:uiMuxer:dfMuxer:bootstrapConfiguration:]_block_invoke
+ ___79-[BSServiceManager _initWithRBSService:uiMuxer:dfMuxer:bootstrapConfiguration:]_block_invoke.59
+ ___80+[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]_block_invoke
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke.65
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke_2
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke_2.66
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke_3
+ ___80-[BSServiceInitiatingConnectionMultiplexer _lock_newRootConnectionWithEndpoint:]_block_invoke_4
+ ___80-[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]_block_invoke
+ ___80-[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]_block_invoke_2
+ ___80-[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]_block_invoke_3
+ ___80-[BSServiceInitiatingConnectionMultiplexer debugDescriptionWithMultilinePrefix:]_block_invoke_4
+ ___81+[BSServiceConnection(NSXPCConnection) NSXPCConnectionWithEndpoint:configurator:]_block_invoke
+ ___81+[BSServicesConfiguration _configOfService:fromPlist:isViewService:postfixBlock:]_block_invoke
+ ___81+[BSServicesConfiguration _configOfService:fromPlist:isViewService:postfixBlock:]_block_invoke.110
+ ___81+[BSServicesConfiguration _configOfService:fromPlist:isViewService:postfixBlock:]_block_invoke.130
+ ___81+[BSServicesConfiguration _configOfService:fromPlist:isViewService:postfixBlock:]_block_invoke.14
+ ___81+[BSXPCServiceConnection _invalidateIncomingXPCConnection:withDisconnectMessage:]_block_invoke
+ ___81+[BSXPCServiceConnection _invalidateIncomingXPCConnection:withDisconnectMessage:]_block_invoke_2
+ ___84-[BSXPCServiceConnectionEventHandler connectionHandleNoMoreChildren:withGeneration:]_block_invoke
+ ___85+[BSServiceConnectionListenerConfiguration configurationWithDomain:service:instance:]_block_invoke
+ ___92-[BSNSXPCTransport _initWithConnection:configurator:assertionProvider:outWrappedConnection:]_block_invoke
+ ___92-[BSNSXPCTransport _initWithConnection:configurator:assertionProvider:outWrappedConnection:]_block_invoke_2
+ ___BSSERVICEMAINRUNLOOPQUEUE_IS_CALLING_OUT_TO_A_BLOCK__
+ ___block_descriptor_32_e37_16?0"BSServiceConnectionEndpoint"8l
+ ___block_descriptor_32_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8l
+ ___block_descriptor_32_e75_q24?0"BSXPCServiceConnectionEndpoint"8"BSXPCServiceConnectionEndpoint"16l
+ ___block_descriptor_32_e76_"<BSInvalidatable>"40?0"RBSTarget"8"NSArray"16"NSString"24"NSString"32l
+ ___block_descriptor_36_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_ea8_32bs_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e58_v16?0"BSServiceConnectionEndpointInjectorConfiguration"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e69_v24?0"BSServiceConnectionListener"8"BSServiceListenerConnection"16ls32l8
+ ___block_descriptor_40_ea8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e40_16?0"BSXPCServiceConnectionEndpoint"8ls32l8
+ ___block_descriptor_40_ea8_32s_e42_v32?0"NSString"8"RBSMachEndpoint"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e69_v24?0"BSServiceConnectionListener"8"BSServiceListenerConnection"16ls32l8
+ ___block_descriptor_40_ea8_32w_e48_v16?0"<BSSimpleAssertionInvalidationContext>"8lw32l8
+ ___block_descriptor_48_ea8_32s40bs_e32_v16?0"BSXPCServiceConnection"8ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40bs_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e66_v24?0"BSXPCServiceConnection"8"BSXPCServiceConnectionMessage"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40s_e35_v20?0"BSXPCServiceConnection"8I16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls32l8
+ ___block_descriptor_48_ea8_32w40w_e8_v12?0B8lw32l8w40l8
+ ___block_descriptor_52_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e32_v16?0"BSXPCServiceConnection"8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e59_v24?0"BSXPCServiceConnection"8"BSXPCServiceConnection"16ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s_e44_v24?0"BSXPCServiceConnection"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40w48w_e27_v16?0"BSSimpleAssertion"8lw40l8w48l8s32l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_ea8_32s40bs48bs56w_e33_v16?0"NSObject<OS_xpc_object>"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_ea8_32s40s48s56bs_e39_v32?0"NSString"8"NSDictionary"16^B24ls56l8s32l8s40l8s48l8
+ ___block_literal_global.118
+ ___block_literal_global.127
+ ___block_literal_global.142
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.164
+ ___block_literal_global.194
+ ___block_literal_global.209
+ ___block_literal_global.213
+ ___block_literal_global.238
+ ___block_literal_global.267
+ ___block_literal_global.321
+ ___block_literal_global.49
+ ___block_literal_global.76
+ ___block_literal_global.81
+ ___getRBSAttributeClass_block_invoke
+ __initWithSpecification:.__uniqueCounter
+ _dispatch_assert_queue_barrier
+ _dispatch_async_and_wait
+ _dispatch_block_create
+ _getRBSAssertionClass.softClass
+ _getRBSAttributeClass
+ _getRBSAttributeClass.softClass
+ _objc_msgSend$_noteChildConnectionDidInvalidate:
+ _objc_msgSend$_performAsync:withHandoff:
+ _objc_msgSend$_setSendingQueue:
+ _objc_msgSend$_xpcReplyQueue
+ _objc_msgSend$_xpcReplyQueue_performReply:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendPointer:withName:
+ _objc_msgSend$appendQueue:withName:
+ _objc_msgSend$assertion
+ _objc_msgSend$bs_compactMap:
+ _objc_msgSend$builderWithClass:
+ _objc_msgSend$cancel
+ _objc_msgSend$connection:didHaltWithEvent:
+ _objc_msgSend$connection:revokedWithEvent:
+ _objc_msgSend$debugDescriptionWithMultilinePrefix:
+ _objc_msgSend$defaultMultiplexer
+ _objc_msgSend$encodeContext:
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$initWithReason:invalidatedBlock:
+ _objc_msgSend$initWithReason:invalidatedWithContextBlock:
+ _objc_msgSend$initiatingContext
+ _objc_msgSend$interfaceWithIdentifier:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$launchIdentifiers
+ _objc_msgSend$mainQueue
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$multiplexingType
+ _objc_msgSend$nullEndpointForService:instance:
+ _objc_msgSend$orderedSetWithObject:
+ _objc_msgSend$performAfter:withBlock:
+ _objc_msgSend$performAsyncAndWait:
+ _objc_msgSend$queue
+ _objc_msgSend$queueWithModes:
+ _objc_msgSend$queueWithName:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$queueWithName:serviceQuality:targetQueue:
+ _objc_msgSend$queueWithName:targetQueue:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$serviceClass:
+ _objc_msgSend$setActiveMultilinePrefix:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setInstance:
+ _objc_msgSend$setMultiplexer:
+ _objc_msgSend$setService:
+ _objc_msgSend$setUseDebugDescription:
+ _objc_msgSend$string
+ _objc_msgSend$userInteractiveMultiplexer
+ _objc_opt_respondsToSelector
+ _objc_storeWeak
+ _xpc_dictionary_create_empty
+ _xpc_endpoint_create_bs_named_user
- +[BSServiceConnection _connectionFromIncomingConnection:requiresMessagingAfterHandshake:]
- +[BSServiceConnection _connectionWithEndpoint:clientContextBuilder:]
- +[BSServiceManager sharedInstanceCreatingIfNecessary:]
- +[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]
- +[BSServicesConfiguration _viewServiceConfigWithDomainsDictionary:]
- +[BSXPCServiceConnection _invalidateIncomingXPCConnection:]
- +[BSXPCServiceConnection connectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]
- +[BSXPCServiceConnectionListener XPCServiceListenerWithSubserviceName:]
- +[BSXPCServiceConnectionListener XPCServiceListener]
- +[BSXPCServiceConnectionListener listenerWithServiceName:]
- +[BSXPCServiceConnectionListener listener]
- +[BSXPCServiceConnectionNullContext nullContext]
- +[BSXPCServiceConnectionRootClientEndpointContext uniqueClientContextWithEndpoint:oneshot:nonLaunching:description:]
- -[BSNSXPCTransport _initWithConnection:configurator:assertionProvider:]
- -[BSNSXPCTransport _underlyingServerPeerConnection]
- -[BSService _identifier]
- -[BSServiceConnection _clientContext]
- -[BSServiceConnection _initWithConnection:service:instance:requiresMessagingAfterHandshake:clientContext:]
- -[BSServiceConnection remoteTargetWithLaunchingAssertionAttributes:]
- -[BSServiceConnectionEndpoint _initWithEndpoint:oneshot:isNonLaunching:targetPID:targetDescription:service:instance:]
- -[BSServiceConnectionEndpointInjector setAdditionalAttributes:]
- -[BSServiceConnectionEndpointInjector setDomain:]
- -[BSServiceConnectionEndpointInjector setInheritingEnvironment:]
- -[BSServiceConnectionEndpointInjector setInstance:]
- -[BSServiceConnectionEndpointInjector setService:]
- -[BSServiceConnectionEndpointInjector setTarget:]
- -[BSServiceConnectionListener setDelegate:]
- -[BSServiceConnectionListener setDomain:]
- -[BSServiceConnectionListener setInstance:]
- -[BSServiceConnectionListener setService:]
- -[BSServiceDomain listenerEndpointOneshot]
- -[BSServiceDomain listenerEndpoint]
- -[BSServiceDomain registerListener:]
- -[BSServiceDomainSpecification _initWithIdentifier:machName:start:servicesByIdentifier:derivedServiceRestrictions:enableIfFeatureFlags:disableIfFeatureFlags:]
- -[BSServiceDomainSpecification _xpcSubserviceName]
- -[BSServiceManager _callOutLock_noteEndpointsChangedForServices:]
- -[BSServiceManager newConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]
- -[BSServiceManager registerMonitor:]
- -[BSServiceManager service:didLoseInheritances:]
- -[BSServiceManager service:didReceiveInheritances:]
- -[BSXPCServiceConnection _asyncToConnectionQueueIfEverActivated:]
- -[BSXPCServiceConnection _clientInvalidateExplicitly:]
- -[BSXPCServiceConnection _invalidateChildConnection:]
- -[BSXPCServiceConnection _lock_invalidate]
- -[BSXPCServiceConnection _parentDisconnectedWithInterrupt:]
- -[BSXPCServiceConnection _stateDump]
- -[BSXPCServiceConnectionEventHandler connectionHandleNoMoreChildren:]
- -[BSXPCServiceConnectionEventHandler setContext:]
- -[BSXPCServiceConnectionEventHandler setTargetDispatchingQueue:]
- -[BSXPCServiceConnectionEventHandler setTargetQueue:]
- -[BSXPCServiceConnectionListener _initWithServiceName:isXPCService:]
- -[BSXPCServiceConnectionListener _invalidateChildConnection:]
- -[BSXPCServiceConnectionListener isNonLaunching]
- -[BSXPCServiceConnectionListener setEndpointDescription:]
- -[BSXPCServiceConnectionListener setServiceQuality:]
- -[BSXPCServiceConnectionNullContext isClient]
- -[BSXPCServiceConnectionRootClientEndpointContext .cxx_destruct]
- -[BSXPCServiceConnectionRootClientEndpointContext isClient]
- -[BSXPCServiceConnectionRootClientEndpointContext isNonLaunching]
- -[NSXPCConnection(BSServiceConnection) externalMessageSessionController]
- -[_BSNSXPCInvalidCallbackTracking .cxx_destruct]
- -[_BSNSXPCInvalidCallbackTracking clearPendingInvalidation]
- -[_BSNSXPCInvalidCallbackTracking isInvalidationStillPending]
- -[_BSServiceConnectionConfiguration interface]
- -[_BSServiceConnectionConfiguration setTargetDispatchingQueue:]
- -[_BSServiceDispatchingQueueImpl .cxx_destruct]
- -[_BSServiceDispatchingQueueImpl assertBarrierOnQueue]
- -[_BSServiceDispatchingQueueImpl backingQueueIfExists]
- -[_BSServiceDispatchingQueueImpl initWithQueue:]
- -[_BSServiceDispatchingQueueImpl performAsync:]
- -[_BSServiceDispatchingQueueImpl performAsync:withHandoff:]
- -[_BSServiceOutgoingEndpoint .cxx_destruct]
- -[_BSServiceOutgoingEndpoint copyWithZone:]
- -[_BSServiceOutgoingEndpoint description]
- -[_BSServiceOutgoingEndpoint hash]
- -[_BSServiceOutgoingEndpoint isEqual:]
- _.str.160
- _BSDispatchQueueAssertBarrier
- _OBJC_CLASS_$_BSXPCServiceConnectionNullContext
- _OBJC_CLASS_$_BSXPCServiceConnectionRootClientEndpointContext
- _OBJC_CLASS_$__BSNSXPCInvalidCallbackTracking
- _OBJC_CLASS_$__BSServiceDispatchingQueueImpl
- _OBJC_CLASS_$__BSServiceOutgoingEndpoint
- _OBJC_IVAR_$_BSNSXPCTransport._configured_invalidCallbackTracking
- _OBJC_IVAR_$_BSNSXPCTransport._targetQueue
- _OBJC_IVAR_$_BSServiceConnectionEndpoint._endpoint
- _OBJC_IVAR_$_BSServiceConnectionEndpoint._nonLaunching
- _OBJC_IVAR_$_BSServiceConnectionEndpoint._oneshot
- _OBJC_IVAR_$_BSServiceConnectionEndpoint._targetDescription
- _OBJC_IVAR_$_BSServiceConnectionEndpoint._targetPID
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._additionalAttributes
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._assertion
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._domain
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._inheritingEnvironment
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._instance
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._invalidated
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._manager
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._service
- _OBJC_IVAR_$_BSServiceConnectionEndpointInjector._target
- _OBJC_IVAR_$_BSServiceConnectionEndpointMonitor._manager
- _OBJC_IVAR_$_BSServiceConnectionListener._lock_delegate
- _OBJC_IVAR_$_BSServiceConnectionListener._manager
- _OBJC_IVAR_$_BSServiceDomain._listenerEndpointDescription
- _OBJC_IVAR_$_BSServiceManager._callOutLock
- _OBJC_IVAR_$_BSServiceManager._callOutLock_serviceIdentifierToEndpointsToEnvironments
- _OBJC_IVAR_$_BSServiceManager._lock_endpointToInheritances
- _OBJC_IVAR_$_BSServiceManager._lock_endpointToOutgoingRootConnections
- _OBJC_IVAR_$_BSServiceManager._lock_inheritanceToEndpoint
- _OBJC_IVAR_$_BSServiceManager._lock_serviceIdentifierToEndpoints
- _OBJC_IVAR_$_BSServiceManager._lock_serviceIdentifierToMonitors
- _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._context
- _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._serviceQuality
- _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._targetDispatchingQueue
- _OBJC_IVAR_$_BSXPCServiceConnectionEventHandler._targetQueue
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._config_eDesc
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._config_qos
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._lock_debugDesc
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._lock_nonLaunching
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._lock_queue
- _OBJC_IVAR_$_BSXPCServiceConnectionListener._serviceName
- _OBJC_IVAR_$_BSXPCServiceConnectionRootClientEndpointContext._endpoint
- _OBJC_IVAR_$_BSXPCServiceConnectionRootClientEndpointContext._nonLaunching
- _OBJC_IVAR_$_BSXPCServiceConnectionRootClientEndpointContext._oneshot
- _OBJC_IVAR_$__BSNSXPCInvalidCallbackTracking._lock
- _OBJC_IVAR_$__BSNSXPCInvalidCallbackTracking._lock_handler
- _OBJC_IVAR_$__BSServiceConnectionConfiguration._targetDispatchingQueue
- _OBJC_IVAR_$__BSServiceDispatchingQueueImpl._queue
- _OBJC_IVAR_$__BSServiceOutgoingEndpoint._eDesc
- _OBJC_IVAR_$__BSServiceOutgoingEndpoint._endpoint
- _OBJC_IVAR_$__BSServiceOutgoingEndpoint._invalidationGeneration
- _OBJC_IVAR_$__BSServiceOutgoingEndpoint._oneshot
- _OBJC_IVAR_$__BSServiceOutgoingEndpoint._targetPID
- _OBJC_METACLASS_$_BSXPCServiceConnectionNullContext
- _OBJC_METACLASS_$_BSXPCServiceConnectionRootClientEndpointContext
- _OBJC_METACLASS_$__BSNSXPCInvalidCallbackTracking
- _OBJC_METACLASS_$__BSServiceDispatchingQueueImpl
- _OBJC_METACLASS_$__BSServiceOutgoingEndpoint
- __OBJC_$_CATEGORY_NSXPCConnection_$_BSServiceConnection
- __OBJC_$_INSTANCE_METHODS_BSXPCServiceConnectionNullContext
- __OBJC_$_INSTANCE_METHODS_BSXPCServiceConnectionRootClientEndpointContext
- __OBJC_$_INSTANCE_METHODS_NSXPCConnection(BSServiceConnection|forViewServicesOnly)
- __OBJC_$_INSTANCE_METHODS__BSNSXPCInvalidCallbackTracking
- __OBJC_$_INSTANCE_METHODS__BSServiceDispatchingQueueImpl
- __OBJC_$_INSTANCE_METHODS__BSServiceOutgoingEndpoint
- __OBJC_$_INSTANCE_VARIABLES_BSXPCServiceConnectionRootClientEndpointContext
- __OBJC_$_INSTANCE_VARIABLES__BSNSXPCInvalidCallbackTracking
- __OBJC_$_INSTANCE_VARIABLES__BSServiceDispatchingQueueImpl
- __OBJC_$_INSTANCE_VARIABLES__BSServiceOutgoingEndpoint
- __OBJC_$_PROP_LIST_BSServiceListener
- __OBJC_$_PROP_LIST_BSServiceManager
- __OBJC_$_PROP_LIST_NSXPCConnection_$_BSServiceConnection
- __OBJC_$_PROP_LIST__BSServiceDispatchingQueueImpl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionConfiguring_DispatchingQueue
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionInternalConfiguring
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionConfiguring_DispatchingQueue
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionInternalConfiguring
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceDispatchingQueue
- __OBJC_$_PROTOCOL_REFS_BSServiceConnectionConfiguring_DispatchingQueue
- __OBJC_$_PROTOCOL_REFS_BSServiceDispatchingQueue
- __OBJC_CATEGORY_PROTOCOLS_$_NSXPCConnection_$_BSServiceConnection
- __OBJC_CLASS_PROTOCOLS_$_BSServiceManager
- __OBJC_CLASS_PROTOCOLS_$__BSServiceDispatchingQueueImpl
- __OBJC_CLASS_PROTOCOLS_$__BSServiceOutgoingEndpoint
- __OBJC_CLASS_RO_$_BSXPCServiceConnectionNullContext
- __OBJC_CLASS_RO_$_BSXPCServiceConnectionRootClientEndpointContext
- __OBJC_CLASS_RO_$__BSNSXPCInvalidCallbackTracking
- __OBJC_CLASS_RO_$__BSServiceDispatchingQueueImpl
- __OBJC_CLASS_RO_$__BSServiceOutgoingEndpoint
- __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionConfiguring_DispatchingQueue
- __OBJC_LABEL_PROTOCOL_$_BSServiceDispatchingQueue
- __OBJC_METACLASS_RO_$_BSXPCServiceConnectionNullContext
- __OBJC_METACLASS_RO_$_BSXPCServiceConnectionRootClientEndpointContext
- __OBJC_METACLASS_RO_$__BSNSXPCInvalidCallbackTracking
- __OBJC_METACLASS_RO_$__BSServiceDispatchingQueueImpl
- __OBJC_METACLASS_RO_$__BSServiceOutgoingEndpoint
- __OBJC_PROTOCOL_$_BSServiceConnectionConfiguring_DispatchingQueue
- __OBJC_PROTOCOL_$_BSServiceDispatchingQueue
- ___158-[BSServiceDomainSpecification _initWithIdentifier:machName:start:servicesByIdentifier:derivedServiceRestrictions:enableIfFeatureFlags:disableIfFeatureFlags:]_block_invoke
- ___31-[BSServiceConnection activate]_block_invoke.172
- ___31-[BSServiceConnection activate]_block_invoke.176
- ___31-[BSServiceConnection activate]_block_invoke.180
- ___31-[BSServiceConnection activate]_block_invoke.181
- ___31-[BSServiceConnection activate]_block_invoke.182
- ___31-[BSServiceConnection activate]_block_invoke_3
- ___31-[BSServiceConnection activate]_block_invoke_4
- ___36-[BSNSXPCTransport setErrorHandler:]_block_invoke_2
- ___36-[BSServiceManager debugDescription]_block_invoke_10
- ___36-[BSServiceManager debugDescription]_block_invoke_9
- ___36-[BSServiceManager registerMonitor:]_block_invoke
- ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.105
- ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.113
- ___42-[BSServiceDomain _initWithSpecification:]_block_invoke.117
- ___42-[BSServiceDomain _initWithSpecification:]_block_invoke_2.109
- ___42-[BSXPCServiceConnection _lock_invalidate]_block_invoke
- ___43-[BSService _registerListener:forInstance:]_block_invoke
- ___43-[BSServiceConnection configureConnection:]_block_invoke
- ___51-[BSServiceManager service:didReceiveInheritances:]_block_invoke
- ___52-[BSServiceManager _initWithBootstrapConfiguration:]_block_invoke
- ___52-[BSServiceManager _initWithBootstrapConfiguration:]_block_invoke.35
- ___53-[BSXPCServiceConnection _invalidateChildConnection:]_block_invoke
- ___54-[BSServiceManager extendAutomaticBootstrapCompletion]_block_invoke.97
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.177
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.182
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.190
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.194
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke.195
- ___55-[BSXPCServiceConnection _lock_activateNowOrWhenReady:]_block_invoke_2.196
- ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke.48
- ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke.50
- ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke_2.51
- ___55-[BSXPCServiceConnectionMessage _actuallySendWithMode:]_block_invoke_3
- ___56+[BSServicesConfiguration _bootstrapConfigWithEnv:info:]_block_invoke
- ___56-[BSServiceDomainSpecification loadRBSLaunchIdentifiers]_block_invoke
- ___59+[BSXPCServiceConnection _invalidateIncomingXPCConnection:]_block_invoke
- ___59+[BSXPCServiceConnection _invalidateIncomingXPCConnection:]_block_invoke_2
- ___59-[BSXPCServiceConnection _parentDisconnectedWithInterrupt:]_block_invoke
- ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.28
- ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.31
- ___63-[BSXPCServiceConnectionEventHandler connection:handleMessage:]_block_invoke.32
- ___65-[BSServiceManager _callOutLock_noteEndpointsChangedForServices:]_block_invoke
- ___69-[BSXPCServiceConnectionEventHandler connectionHandleNoMoreChildren:]_block_invoke
- ___71-[BSXPCServiceConnection _connection_handleActivationMessage:fromPeer:]_block_invoke
- ___78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke
- ___78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.103
- ___78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.14
- ___78+[BSServicesConfiguration _configurationFromPlist:isViewService:postfixBlock:]_block_invoke.83
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke.204
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_2.205
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_3
- ___96-[BSServiceManager _lock_rootConnectionWithEndpoint:oneshot:nonLaunching:targetPID:description:]_block_invoke_4
- _____handleEvent_block_invoke.214
- ___block_descriptor_32_e32_v16?0"BSXPCServiceConnection"8l
- ___block_descriptor_32_e67_q24?0"_BSServiceOutgoingEndpoint"8"_BSServiceOutgoingEndpoint"16l
- ___block_descriptor_40_ea8_32bs_e32_v16?0"BSXPCServiceConnection"8ls32l8
- ___block_descriptor_40_ea8_32bs_e50_v16?0"<BSServiceConnectionInternalConfiguring>"8ls32l8
- ___block_descriptor_40_ea8_32s_e36_16?0"_BSServiceOutgoingEndpoint"8ls32l8
- ___block_descriptor_40_ea8_32s_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls32l8
- ___block_descriptor_48_ea8_32s40bs_e32_v16?0"BSXPCServiceConnection"8ls32l8s40l8
- ___block_descriptor_48_ea8_32s40bs_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls40l8s32l8
- ___block_descriptor_48_ea8_32s40bs_e66_v24?0"BSXPCServiceConnection"8"BSXPCServiceConnectionMessage"16ls40l8s32l8
- ___block_descriptor_48_ea8_32s40s_e42_v32?0"NSString"8"RBSMachEndpoint"16^B24ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e44_v24?0"BSXPCServiceConnection"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e59_v24?0"BSXPCServiceConnection"8"BSXPCServiceConnection"16ls32l8s40l8
- ___block_descriptor_56_ea8_32s40s48w_e27_v16?0"BSSimpleAssertion"8ls32l8w48l8s40l8
- ___block_descriptor_64_ea8_32s40bs48bs56w_e33_v16?0"NSObject<OS_xpc_object>"8lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48bs_e44_v16?0"BSXPCServiceConnectionEventHandler"8ls32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48bs_e44_v24?0"BSXPCServiceConnection"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_73_ea8_32s40s48bs_e39_v32?0"NSString"8"NSDictionary"16^B24ls48l8s32l8s40l8
- ___block_literal_global.115
- ___block_literal_global.137
- ___block_literal_global.162
- ___block_literal_global.165
- ___block_literal_global.176
- ___block_literal_global.185
- ___block_literal_global.198
- ___block_literal_global.208
- ___block_literal_global.220
- ___block_literal_global.258
- ___block_literal_global.262
- ___block_literal_global.38
- ___block_literal_global.45
- ___block_literal_global.74
- ___block_literal_global.99
- __initWithServiceName:isXPCService:.__uniqueCounter
- _getRBSHereditaryGrantClass
- _getRBSHereditaryGrantClass.softClass
- _objc_msgSend$_configureConnection:
- _objc_msgSend$_invalidateChildConnection:
- _objc_msgSend$backingQueueIfExists
- _objc_msgSend$connectionWithEndpoint:
- _objc_msgSend$connectionWithEndpoint:clientContextBuilder:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$extractNSXPCConnectionWithConfigurator:
- _objc_msgSend$isNullEndpoint
- _objc_msgSend$performAsync:withHandoff:
- _objc_msgSend$setEndpointDescription:
- _objc_msgSend$setServiceQuality:
- _objc_msgSend$stringWithString:
- _objc_msgSend$targetDescription
- _objc_msgSend$utility
- _objc_retain_x10
- _xpc_copy
- _xpc_dictionary_create
CStrings:
+ "\t"
+ " +"
+ " + %lu attrs"
+ " + 1 attr"
+ " [%@]"
+ " inherited from '%@'"
+ " on %@"
+ "!_lock_invalidated"
+ "%@ is not available on subclass %@"
+ "%@: _currentConnection is nil in activation handler : context=%@ : name=%@ : t=%@ : tls=%@"
+ "%@: _currentConnection is nil in interrupt handler : context=%@ : name=%@ : t=%@ : tls=%@"
+ "%@: _currentConnection is nil in invalidation handler : context=%@ : name=%@ : t=%@ : tls=%@"
+ "%@: dropping activation handler because _currentConnection is unexpectedly nil (client bug) : context=%@ : name=%@"
+ "%@: dropping interrupt handler because _currentConnection is unexpectedly nil (client bug) : context=%@ : name=%@"
+ "%@: dropping invalidation handler because _currentConnection is unexpectedly nil (client bug) : context=%@ name=%@"
+ "%@:%@"
+ "%@{%@:%@}"
+ "%@{%@}"
+ "%{public}@ Cancelling incoming connection because the root has already been invalidated"
+ "%{public}@ Client invalidation signaled. (type=%i)"
+ "%{public}@ Dropping child activate event (for invalidation message) because we have already been invalidated."
+ "%{public}@ Failed to wrap incoming connection - cancelling"
+ "%{public}@ Invalidating. (message=%i)"
+ "%{public}@ Queue is misconfigured. The user-interactive demuxer will hand-off to a queue that is not user-interactive. queue=%{public}@ demuxer=%{public}@"
+ "%{public}@ Queue is user-interactive on a default demuxer. If an incoming message is sent from a user-interactive context then this may lead to a priority drop in the demuxer. queue=%{public}@ demuxer=%{public}@"
+ "%{public}@ Queue may be misconfigured. The user-interactive demuxer will hand-off to a queue that may not be user-interactive (please switch to using `BSServiceQueue` directly). queue=%{public}@ demuxer=%{public}@"
+ "%{public}@ Trailing client invalidation explicitly signaled. (type=%i)"
+ "%{public}@ [callout] connectionHandleNoMoreChildren: withGeneration=%u"
+ "%{public}@ dropping message received after invalidation callback : message=%@"
+ "(unknown - %d)"
+ ","
+ "-[BSServiceConnection activate]_block_invoke_2"
+ "-init is not allowed on BSXPCServiceConnectionEndpoint"
+ "<%@: p=<%@:%p> ch=%lu c=%i a=%i w=%i e=%i ri=%i ci=%i cie=%i i=%i eh=%p>"
+ "<%@:%p name=%@>"
+ "<BSNSXPCConnectionEvent: onQueue=%@ error=%@>"
+ "<not-initialized>"
+ "<unknown>"
+ "@\"<BSInvalidatable>\"40@?0@\"RBSTarget\"8@\"NSArray\"16@\"NSString\"24@\"NSString\"32"
+ "@\"<BSNSXPCConnectionEventObserver>\""
+ "@\"<BSNSXPCSending>\""
+ "@\"BSRBSService\""
+ "@\"BSService\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceDomain\""
+ "@\"BSServiceInitiatingConnectionMultiplexer\""
+ "@\"BSServiceMainRunLoopQueue\""
+ "@\"BSServiceQueue\""
+ "@\"BSXPCServiceConnectionEndpoint\""
+ "@\"BSXPCServiceConnectionEventObservers\""
+ "@\"NSMapTable\""
+ "@\"NSMutableOrderedSet\""
+ "@\"NSValue\"32@0:8r*16@\"NSString\"24"
+ "@\"NSXPCConnection\""
+ "@\"_BSNSXPCCallbackTracking\""
+ "@16@?0@\"BSServiceConnectionEndpoint\"8"
+ "@16@?0@\"BSXPCServiceConnectionEndpoint\"8"
+ "@32@0:8r*16@24"
+ "@44@0:8@16I24@28@36"
+ "Activated outgoing root connection %{public}@ to %d"
+ "B40@0:8o^v16r*24@\"NSString\"32"
+ "B40@0:8o^v16r*24@32"
+ "BSCancellable"
+ "BSDebugDescriptionProviding"
+ "BSNSXPCConnectionHaltEvent"
+ "BSNSXPCConnectionInternalConfiguring"
+ "BSNSXPCConnectionViewServiceConfiguring"
+ "BSNSXPCMessageSession"
+ "BSNSXPCSending"
+ "BSRBSService"
+ "BSRBSService.m"
+ "BSServiceCompoundQueue"
+ "BSServiceConnectionCommonConfiguring"
+ "BSServiceConnectionConfiguring_MessageBatching"
+ "BSServiceConnectionContext_DEPRECATED"
+ "BSServiceConnectionEndpoint: Unable to decode endpoint from %@ : endpoint=%@ oneshot=%@ nonLaunching=%{bool}i (%@) service=%@ instance=%@"
+ "BSServiceConnectionEndpointInjectorConfiguration"
+ "BSServiceConnectionInitiatingOptions"
+ "BSServiceConnectionListenerConfiguration"
+ "BSServiceDispatchQueue"
+ "BSServiceDispatchQueueReference"
+ "BSServiceInitiatingConnection"
+ "BSServiceInitiatingConnectionConfiguring"
+ "BSServiceInitiatingConnectionLegacyFrontBoardConfiguring"
+ "BSServiceInitiatingConnectionMultiplexer"
+ "BSServiceInitiatingConnectionMultiplexer.m"
+ "BSServiceListenerConnection"
+ "BSServiceListenerConnectionConfiguring"
+ "BSServiceListenerConnectionLegacyFrontBoardConfiguring"
+ "BSServiceListenerConnectionRevocationEvent"
+ "BSServiceMainRunLoopQueue"
+ "BSServiceQueue"
+ "BSServiceQueue.m"
+ "BSServiceReplyFallbackQueue"
+ "BSServiceSetIsTesting isn't allowed outside unit tests"
+ "BSServiceTesting.m"
+ "BSServicesConfigurationRegistration"
+ "BSXPC(%@%@)"
+ "BSXPC(%@%@)-as(%@)"
+ "BSXPC(%@%@)-from(%d)"
+ "BSXPC(%@%@)-from(%d)-as(%@)"
+ "BSXPC(%@%@)-from(%d:%@)"
+ "BSXPC(%@%@)-from(%d:%@)-as(%@)"
+ "BSXPCServiceConnectionConfiguring"
+ "BSXPCServiceConnectionEndpoint"
+ "BSXPCServiceConnectionEndpoint.m"
+ "BSXPCServiceConnectionEventObservers"
+ "BSXPCServiceConnectionRootClientContext"
+ "BoardServices"
+ "Cannot have a queue of target queue set if specifying a queue : service=%@"
+ "Cannot have a serviceQuality if specifying a queue : service=%@"
+ "Cannot have a target queue set if specifying a queue : service=%@"
+ "Class getRBSAttributeClass(void)_block_invoke"
+ "Default"
+ "Error on outgoing root connection %{public}@: %{public}@"
+ "FBSSerialQueue"
+ "Multiplexing"
+ "Multiplexing of domain %@ must be NSString : %@"
+ "Must have a connection replyQueue that understands how to schedule replies : %@"
+ "RBSAttribute"
+ "T@\"<BSXPCDecoding>\",R,N"
+ "T@\"BSAuditToken\",R,D,N"
+ "T@\"BSServiceDispatchQueue\",R,N,V_dispatchQueue"
+ "T@\"BSServiceInitiatingConnectionMultiplexer\",R,N"
+ "T@\"BSServiceQueue\",R,N,V_targetQueue"
+ "T@\"BSServiceSpecification\",R,D,N"
+ "T@\"BSServicesConfiguration\",R,N,V_configuration"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSSet\",R,C,N,V_launchIdentifiers"
+ "T@\"NSString\",R,C,D,N"
+ "TB,R,N,GisExplicitInitiatorInvalidation"
+ "TB,R,N,GisKnownToBeOnQueue"
+ "TB,R,N,GisKnownToBeOnQueue,V_onQueue"
+ "TB,R,N,GisLocalCancel"
+ "TB,R,N,GisNonLaunching"
+ "TB,R,N,GisPermanent"
+ "TB,R,N,GisRevoked"
+ "TB,R,N,GisValid"
+ "TQ,R,N,V_multiplexingType"
+ "UnboundedManualBootstrap"
+ "UserInitiated"
+ "UserInteractive"
+ "VerifyDemuxingQueues"
+ "[%u]"
+ "[BSServiceDomain-%{public}@] Activating incoming root connection %{public}@"
+ "[BSServiceDomain-%{public}@] Error on incoming root connection %{public}@: %{public}@"
+ "[BSServiceDomain-%{public}@] Failed to wrap incoming child connection %{public}@"
+ "[BSServiceDomain-%{public}@] Incoming root connection is %{public}@"
+ "[BSServiceDomain-%{public}@] Unknown service \"%{public}@\" for incoming child connection %{public}@ on %{public}@. Invalidating the connection."
+ "[_bs_assert_object isKindOfClass:BSRBSServiceClass]"
+ "[modes count] > 0"
+ "^{__CFRunLoopSource=}"
+ "_BSNSXPCCallbackTracking"
+ "_BSNSXPCCallbackTracking must invalidate before dealloc"
+ "_BSNSXPCConnectionEvent"
+ "_BSNSXPCTransport"
+ "_assertSharedInstanceNotCreated"
+ "_assertSharedInstancesNotCreated"
+ "_bootstrapConfigOfService:withEnv:info:"
+ "_callbackTracking"
+ "_calloutContext"
+ "_clientInvalidateWithType:"
+ "_code"
+ "_config:"
+ "_configOfService:fromPlist:isViewService:postfixBlock:"
+ "_configuration"
+ "_configure:"
+ "_description"
+ "_dfMuxer"
+ "_dispatchQueue"
+ "_extractNSXPCConnectionWithConfigurator:assertionProvider:"
+ "_handleParentDisconnectWithMessage:outRevocations:"
+ "_initWithConfiguration:"
+ "_initWithConnection:configurator:assertionProvider:outWrappedConnection:"
+ "_initWithEndpoint:service:instance:"
+ "_initWithModes:"
+ "_initWithRBSService:service:"
+ "_initWithRBSService:uiMuxer:dfMuxer:bootstrapConfiguration:"
+ "_injector:"
+ "_invalidate"
+ "_isAnonymous"
+ "_isAssociated"
+ "_launchIdentifiers"
+ "_listenerWithManager:configuration:handler:"
+ "_listenerWithManager:legacyConfigurator:"
+ "_lock_additionalAttributes"
+ "_lock_assertionGenerator"
+ "_lock_cancelEnqueued"
+ "_lock_cancelProcessed"
+ "_lock_childrenGeneration"
+ "_lock_connection != nil"
+ "_lock_connectionReference"
+ "_lock_connectionReference != nil"
+ "_lock_connectionReference == nil"
+ "_lock_domain"
+ "_lock_endpoints"
+ "_lock_eventObservers"
+ "_lock_explicitlyRevoked"
+ "_lock_inheritingEnvironment"
+ "_lock_instance"
+ "_lock_machNameToLaunchIdentifiers"
+ "_lock_manager"
+ "_lock_newRootConnectionWithEndpoint:"
+ "_lock_observer"
+ "_lock_revocations"
+ "_lock_service"
+ "_lock_target"
+ "_main_callingOut"
+ "_modes"
+ "_multiplexer"
+ "_multiplexingType"
+ "_newEmptyTestInstance"
+ "_newEmptyTestInstanceAsUserInteractive:"
+ "_noteChildConnectionDidInvalidate:"
+ "_onQueue"
+ "_performAsync:withHandoff:"
+ "_queue cannot be nil"
+ "_queue must be set"
+ "_queueOfTargetQueue"
+ "_queueWithDispatchQueue:"
+ "_queueWithReplyQueue:serviceQueue:"
+ "_queue_blocks"
+ "_queue_keepAliveForBlocks"
+ "_registration"
+ "_sendingQueue"
+ "_serviceQueue"
+ "_setSendingQueue:"
+ "_sharedTestInstance"
+ "_source"
+ "_state"
+ "_uiMuxer"
+ "_underlying"
+ "_underlyingEndpoint"
+ "_userInteractive"
+ "_wrapWithNSXPCConnectionUsingAssertionProvider:configurator:"
+ "_xpcEndpoint"
+ "_xpcReplyQueue"
+ "_xpcReplyQueue_performReply:"
+ "_xpcSubserviceName"
+ "abandon"
+ "accessed _sharedTestInstance outside of tests"
+ "addEndpoint:"
+ "addEventObserver:"
+ "addObserverWithReason:forRevocation:"
+ "additionalAttributes"
+ "appendFormat:"
+ "appendPointer:withName:"
+ "appendQueue:withName:"
+ "asked to register a nil listener for instance %@ of service %@ of domain %@"
+ "assertOnQueue"
+ "assertion"
+ "attempt to create a redundant outgoing connection for endpoint %@ : existing=%@"
+ "attempt to create an outgoing connection after invalidation"
+ "attempt to set delegate after configuration has been sealed"
+ "attempt to set domain after configuration has been sealed"
+ "attempt to set instance after configuration has been sealed"
+ "attempt to set service after configuration has been sealed"
+ "attribute"
+ "b2"
+ "bs_compactMap:"
+ "builderWithClass:"
+ "callingOut"
+ "cancelling is only supported on server peer connections"
+ "cannot call observer with event %@ because connection has deallocated : %@"
+ "cannot create outgoing root connection from an endpoint that is no longer valid (%{public}@)"
+ "cannot send a reply via sendNotification:"
+ "captureConnection"
+ "clientInvalidation must be a concrete type"
+ "clientManagers"
+ "clients"
+ "com.apple.BoardServices.invalid-service"
+ "commonModesQueue"
+ "config"
+ "config->_connection"
+ "config->_instance"
+ "config->_service"
+ "configuration"
+ "configuration of BSServiceDomain %{public}@ did not specify its Multiplexing type"
+ "configurationWithDomain:service:"
+ "configurationWithDomain:service:instance:"
+ "connection:didHaltWithEvent:"
+ "connection:revokedWithEvent:"
+ "connectionHandleNoMoreChildren:withGeneration:"
+ "consumeRevocations:"
+ "contextBuilder"
+ "created outgoing root connection %{public}@"
+ "dealloced without invalidating"
+ "debugDescriptionWithMultilinePrefix:"
+ "decodeStruct:withObjCType:forKey:"
+ "decodeValueWithObjCType:forKey:"
+ "defaultMultiplexer"
+ "destroying session for domain %{public}@"
+ "dfMuxer"
+ "dispatchQueue"
+ "domain=%{public}@ service=%{public}@ : no listener at %{public}@"
+ "domainIdentifier"
+ "dynamic domains may not specify a mach name : %@"
+ "encodeContext:"
+ "encodeContext: called outside of options builder"
+ "encodeStruct:withObjCType:forKey:"
+ "endpointForMachName:targetUserIdentifier:service:instance:"
+ "enqueued"
+ "explanation"
+ "explicitInitiatorInvalidation"
+ "extractNSXPCConnectionWithViewServiceConfigurator:"
+ "failed to acquire injector with error=%{public}@ : description='%{public}@'"
+ "failed to create BSNSXPCTransport for %@"
+ "failed to create NSXPCConnection with %@"
+ "failed to create outgoing root connection for endpoint=%{public}@"
+ "failed to create source"
+ "failed to extract BSXPCServiceConnection from %@"
+ "failed to find domain '%@' : manager=%@"
+ "failed to find service '%@' in domain '%@' : manager=%@"
+ "failed to get an xpcEndpoint for the service listener %@"
+ "failure in %@ of <%@:%p> (%@:%i)"
+ "found existing rootConnection %{public}@ by endpoint (%{public}@)"
+ "how could we have revocation observers if we're not done adding the child? : self=%@ child=%@"
+ "incompatible clientMessagingExpectation for this connection : interface=%@"
+ "incomplete lookup information : domain='%@' service'%@' instance='%@'"
+ "init is not allowed on %@"
+ "initWithConfigurator:"
+ "initWithEndpoint:"
+ "initWithEndpoint:options:"
+ "initWithReason:invalidatedBlock:"
+ "initWithReason:invalidatedWithContextBlock:"
+ "initWithXPCEndpoint:oneshot:nonLaunching:targetPID:targetDescription:"
+ "initializing automatic domain %{public}@"
+ "initializing domain %{public}@"
+ "initializing view-service domain %{public}@"
+ "initiatingContext"
+ "injecting %@"
+ "interface must be specified if you specified a target : service=%@"
+ "interface's identifier doesn't match our service : service=%@ interface=%@"
+ "interfaceWithIdentifier:configurator:"
+ "invalid targetPID %i"
+ "invalidating connection %{public}@ to instance %{public}@ of service %{public}@ of domain %{public}@ because pending has been disabled"
+ "invalidating connection %{public}@ to instance %{public}@ of service %{public}@ of domain %{public}@ because the listener has gone away"
+ "invalidating connection %{public}@ to instance %{public}@ of service %{public}@ of domain %{public}@ because there is no listener to handle it"
+ "invalidating connection to instance %@ of service %@ of domain %@ because there is no handler for it : %@"
+ "invalidating domain %{public}@"
+ "isExplicitInitiatorInvalidation"
+ "isKnownToBeOnQueue"
+ "isLocalCancel"
+ "isMainThread"
+ "isPermanent"
+ "isRevoked"
+ "isRevokedPeer"
+ "isValid"
+ "knownToBeOnQueue"
+ "launchIdentifiers"
+ "listenerForSpecification:"
+ "listenerWithConfiguration:handler:"
+ "localCancel"
+ "lp"
+ "mainDispatchQueue"
+ "mainQueue"
+ "manager"
+ "manually activating session for domain %{public}@"
+ "manually bootstrapping domain %{public}@"
+ "mapTableWithKeyOptions:valueOptions:"
+ "missing registration"
+ "mode"
+ "modes"
+ "multiplexer"
+ "multiplexingType"
+ "must call before invalidation"
+ "must configure a manager"
+ "must configure an assertion generator"
+ "newConnectionWithEndpoint:"
+ "no endpoint found for domain='%@' service='%@' instance='%@'"
+ "observe-none:"
+ "observe-revoked:"
+ "observer"
+ "oneshot"
+ "only viable on server connections"
+ "orderedSetWithObject:"
+ "other"
+ "outRevocations"
+ "pending connection %{public}@ to instance %{public}@ of service %{public}@ of domain %{public}@ because there is no listener to handle it"
+ "performAfter:withBlock:"
+ "performAsyncAndWait:"
+ "permanent"
+ "q24@?0@\"BSXPCServiceConnectionEndpoint\"8@\"BSXPCServiceConnectionEndpoint\"16"
+ "queue must be set"
+ "queueWithDispatchQueue:"
+ "queueWithDispatchQueue:targetQueue:"
+ "queueWithMainRunLoopModes:"
+ "queueWithModes:"
+ "queueWithName:"
+ "queueWithName:serviceQuality:"
+ "queueWithName:serviceQuality:targetQueue:"
+ "queueWithName:targetQueue:"
+ "raw message handlers aren't supported on this connection : service=%@"
+ "reason"
+ "registerListener:forInstance:"
+ "registration"
+ "removeAllObjects"
+ "revoked"
+ "sendError:isOnQueue:"
+ "sendingQueue"
+ "serviceClass:"
+ "serviceQueue"
+ "serviceQueue already specifies a replyQueue"
+ "setActivationHandler: called outside of configurator"
+ "setActiveMultilinePrefix:"
+ "setAssertionGenerator:"
+ "setBatchingHandler: called outside of configurator"
+ "setConnection:"
+ "setEventObserver:"
+ "setInterface: called outside of configurator"
+ "setInterfaceTarget: called outside of configurator"
+ "setInterruptionHandler: called outside of configurator"
+ "setInvalidationHandler: called outside of configurator"
+ "setManager:"
+ "setMultiplexer:"
+ "setMultiplexer: called outside of options builder"
+ "setName: called outside of configurator"
+ "setQueue:"
+ "setQueue: called outside of configurator"
+ "setSendingQueue:"
+ "setServiceQuality: called outside of configurator"
+ "setTargetQueue: called outside of configurator"
+ "setUseDebugDescription:"
+ "setUserInfo: called outside of configurator"
+ "sharedInstance"
+ "sharedInstanceIfCreated"
+ "some form of interface handler must be specified before activation : service=%@"
+ "source"
+ "string"
+ "target must be specified if the local interface is not empty : interface=%@"
+ "targetPID"
+ "the underlying queue must always know if its user-interactive priority : %@"
+ "threading violation: expected the main thread"
+ "uiMuxer"
+ "uniqueClientContextWithEndpoint:"
+ "unrecognized Multiplexing value of domain %@ : %@"
+ "unsupported configuration : inheritingEnvironment='%@' endpoints=%@"
+ "user-initiated"
+ "user-interactive"
+ "userInteractiveMultiplexer"
+ "v12@?0B8"
+ "v16@?0@\"<BSServiceConnectionInitiatingOptions>\"8"
+ "v16@?0@\"<BSServiceConnectionListenerConfiguring>\"8"
+ "v16@?0@\"<BSSimpleAssertionInvalidationContext>\"8"
+ "v16@?0@\"BSServiceConnectionEndpointInjectorConfiguration\"8"
+ "v20@?0@\"BSXPCServiceConnection\"8I16"
+ "v24@0:8@\"<BSNSXPCConnectionEventObserver>\"16"
+ "v24@0:8@\"<BSNSXPCSending>\"16"
+ "v24@0:8@\"BSServiceConnectionEndpoint\"16"
+ "v24@0:8@\"BSServiceDispatchQueue\"16"
+ "v24@0:8@\"BSServiceInitiatingConnectionMultiplexer\"16"
+ "v24@0:8@\"BSServiceListenerConnection\"16"
+ "v24@0:8@\"BSServiceQueue\"16"
+ "v24@0:8@?<v@?@\"<BSXPCEncoding>\">16"
+ "v24@0:8@?<v@?@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\">16"
+ "v24@0:8@?<v@?@\"BSServiceListenerConnection<BSServiceConnectionContext>\">16"
+ "v24@?0@\"BSServiceConnectionListener\"8@\"BSServiceListenerConnection\"16"
+ "v32@0:8d16@?24"
+ "v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24"
+ "v40@0:8rn^v16r*24@\"NSString\"32"
+ "v40@0:8rn^v16r*24@32"
+ "valid"
+ "validateDynamicConfiguration:withDebugInfo:"
+ "void BSServiceSetIsTesting(void)"
+ "xpcEndpoint"
+ "you must configure an invalidation handler : service=%@"
- " (%@)"
- " + inherited from %i<%@> to %@"
- " to %@"
- "%@ -> failed to acquire on %@ : %{public}@"
- "%@: _currentConnection is nil in activation handler : context=%@ : eventHandler=%@ : name=%@ : t=%@ : tls=%@"
- "%@: _currentConnection is nil in interrupt handler : context=%@ : eventHandler=%@ : name=%@ : t=%@ : tls=%@"
- "%@: _currentConnection is nil in invalidation handler : context=%@ : eventHandler=%@ : name=%@ : t=%@ : tls=%@"
- "%@: dropping activation handler because _currentConnection is unexpectedly nil (client bug) : context=%@ : eventHandler=%@ : name=%@"
- "%@: dropping interrupt handler because _currentConnection is unexpectedly nil (client bug) : context=%@ : eventHandler=%@ : name=%@"
- "%@: dropping invalidation handler because _currentConnection is unexpectedly nil (client bug) : context=%@ : eventHandler=%@ : name=%@"
- "%{public}@ Client invalidation signaled. (explicit=%{bool}i)"
- "%{public}@ Failed to wrap incoming connection - invalidating"
- "%{public}@ Invalidating incoming connection because the root has already been invalidated"
- "%{public}@ Invalidating."
- "%{public}@ Trailing client invalidation explicitly signaled."
- "%{public}@ [callout] connectionHandleNoMoreChildren:"
- "-[BSServiceConnection activate]_block_invoke_4"
- ":"
- "<%@: p=<%@:%p> ch=%lu c=%i a=%i w=%i e=%i ri=%i ci=%i cie=%i i=%i>"
- "<anonymous>"
- "@\"<BSServiceDispatchingQueue>\""
- "@\"BSServiceInterface\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"_BSNSXPCInvalidCallbackTracking\""
- "@16@?0@\"_BSServiceOutgoingEndpoint\"8"
- "Activated root connection to %{public}@:%{public}d: %{public}@"
- "BSCnx:"
- "BSServiceConnection+NSXPCConnection.m"
- "BSServiceConnectionConfiguring_DispatchingQueue"
- "BSServiceConnectionEndpoint: Unable to decode endpoint from %@ : endpoint=%@ oneshot=%@ (%@) service=%@ instance=%@"
- "BSServiceConnectionTransport"
- "BSServiceDispatchingQueue"
- "BSXPCCnx:%@"
- "BSXPCRootIn:%@"
- "BSXPCRootOut:%@"
- "BSXPCServiceConnectionNullContext"
- "BSXPCServiceConnectionRootClientEndpointContext"
- "Cannot have a target queue set if using a target dispatching queue."
- "Error on outgoing connection %{public}@: %{public}@"
- "Must have a connection reply queue to send a message with a reply."
- "Must have a connection target queue to send a message with a reply."
- "NL:"
- "NSUUID"
- "Root connections may not specify a <BSServiceDispatchingQueue>."
- "TB,R,N,GisNonLaunching,V_nonLaunching"
- "XPCServiceListenerWithSubserviceName:"
- "[BSServiceDomain-%{public}@] Activating incoming root connection for %{public}@"
- "[BSServiceDomain-%{public}@] Error on connection from %{public}@: %{public}@"
- "[BSServiceDomain-%{public}@] Incoming connection from %{public}@"
- "[BSServiceDomain-%{public}@] Unknown service \"%{public}@\" for incoming connection. Invalidating the connection."
- "[_bs_assert_object isKindOfClass:BSServiceDomainClass]"
- "[_bs_assert_object isKindOfClass:BSServiceManagerClass]"
- "[_bs_assert_object isKindOfClass:BSServiceQualityClass]"
- "[_bs_assert_object isKindOfClass:NSUUIDClass]"
- "^{os_unfair_lock_s=I}"
- "_BSNSXPCInvalidCallbackTracking"
- "_BSServiceDispatchingQueueImpl"
- "_BSServiceOutgoingEndpoint"
- "_additionalAttributes"
- "_assertion"
- "_bootstrapConfigWithEnv:info:"
- "_config_eDesc"
- "_config_qos"
- "_configurationFromPlist:isViewService:postfixBlock:"
- "_configured_invalidCallbackTracking"
- "_inheritingEnvironment"
- "_initWithConnection:service:instance:requiresMessagingAfterHandshake:clientContext:"
- "_initWithEndpoint:oneshot:isNonLaunching:targetPID:targetDescription:service:instance:"
- "_initWithManager:config:"
- "_initWithManager:configurator:"
- "_initWithManager:service:"
- "_invalidateChildConnection:"
- "_invalidationGeneration"
- "_listenerEndpointDescription"
- "_lock_debugDesc"
- "_lock_nonLaunching"
- "_lock_queue"
- "_manager"
- "_parentDisconnectedWithInterrupt:"
- "_registerListener:forInstance:"
- "_serviceName"
- "_targetDispatchingQueue"
- "_targetDispatchingQueue cannot be nil"
- "asked for non-launching status before sealing the listener configuration"
- "asked to register a nil listener of domain %@"
- "backingQueueIfExists"
- "cannot query RBSLaunchIdentifiers if BoardServices infrastructure has not initialized"
- "client:"
- "connectionHandleNoMoreChildren:"
- "connectionWithEndpoint:oneshot:nonLaunching:targetPID:description:"
- "created rootConnection with endpoint=%@"
- "destroying session for domain %@"
- "dispatchingQueue"
- "domain=%{public}@ service=%{public}@ : no listener at %@"
- "dynamic domains may not specificy a mach name : %@"
- "encodeInt:forKey:"
- "failed to activate listener for instance %@ of service %@ in domain %@ because the domain was not initialized"
- "failed to activate listener for instance %@ of service %@ in domain %@ because the service was not initialized"
- "failed to create rootConnection for endpoint=%@"
- "failed to fetch endpoint for %@"
- "failed to get an endpoint for the service listener %@"
- "failed to wrap raw connection to domain %@ : %@"
- "found existing rootConnection by endpoint (%@)"
- "host:"
- "if we don't have an endpoint then we can only be the null endpoint which shouldn't have a description %@"
- "incompatible clientMessagingExpectation for this connection"
- "initWithLock:clientContext:"
- "initializing automatic domain %@"
- "initializing domain %@"
- "initializing view-service domain %@"
- "injecting \"%@\"-\"%@\""
- "injecting \"%@\"-\"%@\"-\"%@\""
- "injecting inherited from \"%@\" to %@"
- "interface must be specified if you specified a target"
- "interface's identifier doesn't match our service"
- "invalidating connection to instance %@ of service %@ of domain %@ because pending has been disabled : %@"
- "invalidating connection to instance %@ of service %@ of domain %@ because the listener has gone away : %@"
- "invalidating connection to instance %@ of service %@ of domain %@ because there is no delegate to handle it : %@"
- "invalidating connection to instance %@ of service %@ of domain %@ because there is no listener to handle it : %@"
- "invalidating domain %@"
- "listenerWithServiceName:"
- "manually activating session for domain %@"
- "manually bootstrapping domain %@"
- "no endpoint found for domain=\"%@\" service=\"%@\" instance=\"%@\""
- "pending connection to instance %@ of service %@ of domain %@ because there is no listener to handle it : %@"
- "performAsync:withHandoff:"
- "q24@?0@\"_BSServiceOutgoingEndpoint\"8@\"_BSServiceOutgoingEndpoint\"16"
- "raw message handlers aren't supported on this connection"
- "registerListener:"
- "serviceQuality must be specified before activation"
- "setEndpointDescription:"
- "setTargetDispatchingQueue:"
- "some form of interface handler must be specified before activation"
- "stringWithString:"
- "target must be specified if the local interface is not empty"
- "targetDispatchingQueue must be set"
- "testing_domain"
- "unexpected error code: %@"
- "uniqueClientContextWithEndpoint:oneshot:nonLaunching:description:"
- "unsupported configuration : domain=\"%@\" service=\"%@\" inheritingEnvironment=\"%@\""
- "v16@?0@\"<BSServiceConnectionInternalConfiguring>\"8"
- "v24@0:8@\"<BSServiceDispatchingQueue>\"16"
- "v24@0:8@\"BSServiceConnection<BSServiceConnectionHost>\"16"
- "v32@0:8@?<v@?>16@\"NSObject<OS_xpc_object>\"24"
- "you must configure an invalidation handler"

```
