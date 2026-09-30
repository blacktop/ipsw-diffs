## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-668.5.29.0.0
-  __TEXT.__text: 0x20328
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x189c
-  __TEXT.__const: 0xec
-  __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x2379
-  __TEXT.__oslogstring: 0x1afd
-  __TEXT.__ustring: 0x5c
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__objc_classname: 0x725
-  __TEXT.__objc_methname: 0x4052
-  __TEXT.__objc_methtype: 0x15c6
-  __TEXT.__objc_stubs: 0x2ca0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xe10
-  __DATA_CONST.__objc_classlist: 0x148
-  __DATA_CONST.__objc_protolist: 0xc0
+726.0.0.0.0
+  __TEXT.__text: 0x2b08c
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x1ce0
+  __TEXT.__const: 0x1f4
+  __TEXT.__cstring: 0x2c95
+  __TEXT.__constg_swiftt: 0x114
+  __TEXT.__swift5_typeref: 0x7c
+  __TEXT.__swift5_reflstr: 0x4b
+  __TEXT.__swift5_fieldmd: 0xac
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__oslogstring: 0x2502
+  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__objc_classname: 0x922
+  __TEXT.__objc_methname: 0x4ceb
+  __TEXT.__objc_methtype: 0x18cf
+  __TEXT.__objc_stubs: 0x34a0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0x10c8
+  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_selrefs: 0x11a0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x290
-  __AUTH_CONST.__auth_got: 0x520
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0x4788
+  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__const: 0x5c8
+  __AUTH_CONST.__cfstring: 0x26a0
+  __AUTH_CONST.__objc_const: 0x5188
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x354
-  __DATA.__data: 0x900
-  __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_data: 0xa50
+  __AUTH.__objc_data: 0x360
+  __AUTH.__data: 0x148
+  __DATA.__objc_ivar: 0x39c
+  __DATA.__data: 0xc38
+  __DATA.__bss: 0xc8
+  __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F00DC94-C786-3285-A6A8-2559671C8E53
-  Functions: 614
-  Symbols:   2651
-  CStrings:  1745
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: C1A36180-C90E-34D7-8964-938A3DBF77D8
+  Functions: 767
+  Symbols:   3096
+  CStrings:  2010
 
Symbols:
+ -[BKEventDeferringEnvironmentGraph _changeSelectionPath:toNode:requestingPID:basis:ignoreModality:]
+ -[BKEventDeferringEnvironmentGraph _chooseSubnodeOfNode:forSelectionPath:appendToPath:]
+ -[BKEventDeferringEnvironmentGraph _forEachSelectionPath:block:]
+ -[BKEventDeferringEnvironmentGraph _updateConstraintMap]
+ -[BKEventDeferringEnvironmentGraph _updateModalityMap]
+ -[BKEventDeferringEnvironmentGraph allSelectionPathIdentifiers]
+ -[BKEventDeferringEnvironmentGraph constraintsForNode:pathIdentifier:]
+ -[BKEventDeferringEnvironmentGraph modalitiesForNode:pathIdentifier:]
+ -[BKEventDeferringEnvironmentGraph topLevelInEachProcess]
+ -[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]
+ -[BKEventDeferringGraph deferringPathForPID:environment:display:dispatchTarget:returnModalities:]
+ -[BKEventDeferringNode appendDescriptionToStream:]
+ -[BKEventDeferringNode connectSubnode:]
+ -[BKEventDeferringNode copyWithZone:]
+ -[BKEventDeferringNode copy]
+ -[BKEventDeferringNode pid]
+ -[BKEventDeferringNode rule]
+ -[BKEventDeferringNode subnodes]
+ -[BKEventDeferringNode succinctDescription]
+ -[BKEventDeferringSelectionPathContainer .cxx_destruct]
+ -[BKEventDeferringSelectionPathContainer _keyForNode:]
+ -[BKEventDeferringSelectionPathContainer _removeNode:]
+ -[BKEventDeferringSelectionPathContainer constraintsForNode:]
+ -[BKEventDeferringSelectionPathContainer containsNode:]
+ -[BKEventDeferringSelectionPathContainer copyWithZone:]
+ -[BKEventDeferringSelectionPathContainer copy]
+ -[BKEventDeferringSelectionPathContainer description]
+ -[BKEventDeferringSelectionPathContainer initWithPathIdentifier:]
+ -[BKEventDeferringSelectionPathContainer modalitiesForNode:]
+ -[BKEventDeliveryChain appendDescriptionToStream:]
+ -[BKEventDeliveryChain deferringPath]
+ -[BKEventDeliveryChain dispatchTarget]
+ -[BKEventDeliveryChain environmentGraph]
+ -[BKEventDeliveryChain resolutionPathForEventDescriptor:]
+ -[BKEventDeliveryChain senderDescriptor]
+ -[BKHIDDomainIncomingServiceConnection .cxx_destruct]
+ -[BKHIDDomainIncomingServiceConnection _lock_markAsHandled]
+ -[BKHIDDomainIncomingServiceConnection acceptConnection]
+ -[BKHIDDomainIncomingServiceConnection appendDescriptionToStream:]
+ -[BKHIDDomainIncomingServiceConnection connection:revokedWithEvent:]
+ -[BKHIDDomainIncomingServiceConnection connection]
+ -[BKHIDDomainIncomingServiceConnection dealloc]
+ -[BKHIDDomainIncomingServiceConnection delegate]
+ -[BKHIDDomainIncomingServiceConnection description]
+ -[BKHIDDomainIncomingServiceConnection handler]
+ -[BKHIDDomainIncomingServiceConnection initWithConnection:log:]
+ -[BKHIDDomainIncomingServiceConnection isRevoked]
+ -[BKHIDDomainIncomingServiceConnection log]
+ -[BKHIDDomainIncomingServiceConnection rejectConnection]
+ -[BKHIDDomainIncomingServiceConnection setDelegate:]
+ -[BKHIDDomainIncomingServiceConnection setHandler:]
+ -[BKHIDDomainServiceServer acceptIncomingServiceConnection:]
+ -[BKHIDDomainServiceServer initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:]
+ -[BKHIDDomainServiceServer rejectIncomingServiceConnection:]
+ -[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:eventDescriptor:getTargetOrder:]
+ -[BKHIDEventDeliveryManager _lock_verifyProvenance:]
+ -[BKHIDEventDeliveryManager _publishedChainFromDeliveryChain:]
+ -[BKHIDEventDeliveryManager deliveryChainsDescription]
+ -[BKHIDEventDeliveryManager deliveryChainsForDeferringTarget:display:environment:event:]
+ -[BKHIDEventDeliveryManager observerService]
+ -[BKHIDEventDeliveryManager requestSelectionChanges:forClientWithPID:]
+ -[BKHIDEventDeliveryManager setConstraintAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryManager setModalityAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryManager simpleProvenanceOriginator]
+ -[BKHIDEventDeliveryManagerServer _deliveryManagerForEstablishedConnection:]
+ -[BKHIDEventDeliveryManagerServer _performDescriptionRetrieval:forConnection:]
+ -[BKHIDEventDeliveryManagerServer acceptIncomingServiceConnection:mappedObject:]
+ -[BKHIDEventDeliveryManagerServer activate]
+ -[BKHIDEventDeliveryManagerServer connectionDidTerminate:]
+ -[BKHIDEventDeliveryManagerServer deliveryChainsDescription]
+ -[BKHIDEventDeliveryManagerServer handleIncomingServiceConnection:]
+ -[BKHIDEventDeliveryManagerServer incomingConnectionHandler]
+ -[BKHIDEventDeliveryManagerServer initWithDeliveryManagerProvider:ruleChangeAuthority:]
+ -[BKHIDEventDeliveryManagerServer initWithIncomingServiceConnectionHandler:ruleChangeAuthority:]
+ -[BKHIDEventDeliveryManagerServer rejectIncomingServiceConnection:]
+ -[BKHIDEventDeliveryManagerServer ruleChangeAuthority]
+ -[BKHIDEventDeliveryObserverServer .cxx_destruct]
+ -[BKHIDEventDeliveryObserverServer _deliveryObserverServiceForEstablishedConnection:]
+ -[BKHIDEventDeliveryObserverServer acceptIncomingServiceConnection:mappedObject:]
+ -[BKHIDEventDeliveryObserverServer activate]
+ -[BKHIDEventDeliveryObserverServer connectionDidTerminate:]
+ -[BKHIDEventDeliveryObserverServer domainServiceServer]
+ -[BKHIDEventDeliveryObserverServer handleIncomingServiceConnection:]
+ -[BKHIDEventDeliveryObserverServer incomingConnectionHandler]
+ -[BKHIDEventDeliveryObserverServer initWithDeliveryObserverServiceProvider:]
+ -[BKHIDEventDeliveryObserverServer initWithIncomingServiceConnectionHandler:]
+ -[BKHIDEventDeliveryObserverServer rejectIncomingServiceConnection:]
+ -[BKHIDEventDeliveryObserverServer setObservesDeferringChainIdentities:]
+ -[BKHIDEventDeliveryObserverServer setObservesDeferringResolutions:]
+ -[BKHIDEventDeliveryObserverService connection:setObservesDeferringChainIdentities:entitled:]
+ -[BKHIDEventDeliveryObserverService connection:setObservesDeferringResolutions:]
+ -[BKHIDEventDeliveryObserverService connectionDidTerminate:]
+ -[BKHIDEventDeliveryObserverService initWithDomainServiceServer:]
+ -[BKHIDEventSenderCache sync]
+ -[BKHIDIncomingServiceConnection .cxx_destruct]
+ -[BKHIDIncomingServiceConnection acceptConnectionWithMappedObject:]
+ -[BKHIDIncomingServiceConnection appendDescriptionToStream:]
+ -[BKHIDIncomingServiceConnection auditToken]
+ -[BKHIDIncomingServiceConnection dealloc]
+ -[BKHIDIncomingServiceConnection delegate]
+ -[BKHIDIncomingServiceConnection description]
+ -[BKHIDIncomingServiceConnection domainIncomingServiceConnection]
+ -[BKHIDIncomingServiceConnection handler]
+ -[BKHIDIncomingServiceConnection incomingServiceConnectionDidRevoke:]
+ -[BKHIDIncomingServiceConnection initWithIncomingServiceConnection:debugMappedObjectName:]
+ -[BKHIDIncomingServiceConnection rejectConnection]
+ -[BKHIDIncomingServiceConnection setDelegate:]
+ -[BKHIDIncomingServiceConnection setHandler:]
+ -[BKIOHIDServiceMatcher _expectDeallocation]
+ -[BKIOHIDServiceMatcher initWithMatchingDictionary:serviceClass:dataProvider:]
+ -[_BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler handleIncomingDeliveryManagerConnection:]
+ -[_BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler initWithDeliveryManagerProvider:]
+ -[_BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler handleIncomingDeliveryObserverConnection:]
+ GCC_except_table214
+ GCC_except_table318
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table339
+ GCC_except_table342
+ GCC_except_table39
+ GCC_except_table570
+ GCC_except_table618
+ _BKHitTestContextFilteringEntitlement
+ _OBJC_CLASS_$_BKEventDeferringSelectionPathContainer
+ _OBJC_CLASS_$_BKHIDDomainIncomingServiceConnection
+ _OBJC_CLASS_$_BKHIDEventDeliveryObserverServer
+ _OBJC_CLASS_$_BKHIDIncomingServiceConnection
+ _OBJC_CLASS_$_BKSHIDEventAuthenticationMessage
+ _OBJC_CLASS_$_BKSHIDEventDeferringChangeBasis
+ _OBJC_CLASS_$_BKSHIDEventDeferringConstraint
+ _OBJC_CLASS_$_BKSHIDEventDeferringModality
+ _OBJC_CLASS_$_BKSHIDEventDeferringRule
+ _OBJC_CLASS_$_BKSHIDEventDeferringSelectionPathIdentifier
+ _OBJC_CLASS_$_BKSHIDEventSimpleProvenance
+ _OBJC_CLASS_$_BKSHIDEventSimpleProvenanceOriginator
+ _OBJC_CLASS_$_BSAtomicSignal
+ _OBJC_CLASS_$_BSServiceConnectionListenerConfiguration
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ _OBJC_CLASS_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ _OBJC_CLASS_$__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._constraintAssertionsByClientPID
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._modalityAssertionsByClientPID
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._nodeByDeferringTarget
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._selectionPathContainerByIdentifier
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._constraintAssertionsByNode
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._includedIdentities
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._modalityAssertionsByNode
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._pathIdentifier
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._subnodeSelectionHistoryByNodeIdentity
+ _OBJC_IVAR_$_BKEventDeliveryChain._environmentGraph
+ _OBJC_IVAR_$_BKEventDeliveryChain._modalities
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._connection
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._lock
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._lock_delegate
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._lock_eventObserver
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._lock_handler
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._lock_wasHandled
+ _OBJC_IVAR_$_BKHIDDomainIncomingServiceConnection._log
+ _OBJC_IVAR_$_BKHIDDomainServiceServer._incomingConnectionHandler
+ _OBJC_IVAR_$_BKHIDDomainServiceServer._invalidSignal
+ _OBJC_IVAR_$_BKHIDDomainServiceServer._lock_activeConnectionsByPID
+ _OBJC_IVAR_$_BKHIDEventDeliveryManager._previousProvenanceTimestamp
+ _OBJC_IVAR_$_BKHIDEventDeliveryManager._simpleProvenanceOriginator
+ _OBJC_IVAR_$_BKHIDEventDeliveryManagerServer._incomingServiceConnectionHandler
+ _OBJC_IVAR_$_BKHIDEventDeliveryObserverServer._incomingServiceConnectionHandler
+ _OBJC_IVAR_$_BKHIDEventDeliveryObserverServer._lock
+ _OBJC_IVAR_$_BKHIDEventDeliveryObserverServer._server
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._debugMappedObjectName
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._domainIncomingServiceConnection
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._lock
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._lock_delegate
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._lock_handler
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._lock_wasHandled
+ _OBJC_IVAR_$_BKHIDIncomingServiceConnection._log
+ _OBJC_IVAR_$__BKEventObserverConnectionRecord._entitledToObserveFullDeliveryChain
+ _OBJC_IVAR_$__BKEventObserverConnectionRecord._observerService
+ _OBJC_IVAR_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler._deliveryManagerProvider
+ _OBJC_IVAR_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler._deliveryObserverServiceProvider
+ _OBJC_METACLASS_$_BKEventDeferringSelectionPathContainer
+ _OBJC_METACLASS_$_BKHIDDomainIncomingServiceConnection
+ _OBJC_METACLASS_$_BKHIDEventDeliveryObserverServer
+ _OBJC_METACLASS_$_BKHIDIncomingServiceConnection
+ _OBJC_METACLASS_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ _OBJC_METACLASS_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ _OBJC_METACLASS_$__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA_BKEventGraphDescriptionAccumulator
+ __DATA__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ __DATA__TtC27BackBoardHIDEventFoundationP33_924A0A2DAF65EBFF9E2C8DDA409C596A10_GraphNode
+ __INSTANCE_METHODS_BKEventGraphDescriptionAccumulator
+ __INSTANCE_METHODS__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ __IVARS_BKEventGraphDescriptionAccumulator
+ __IVARS__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ __IVARS__TtC27BackBoardHIDEventFoundationP33_924A0A2DAF65EBFF9E2C8DDA409C596A10_GraphNode
+ __METACLASS_DATA_BKEventGraphDescriptionAccumulator
+ __METACLASS_DATA__TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper
+ __METACLASS_DATA__TtC27BackBoardHIDEventFoundationP33_924A0A2DAF65EBFF9E2C8DDA409C596A10_GraphNode
+ __OBJC_$_INSTANCE_METHODS_BKEventDeferringEnvironmentGraph(SwiftStuff)
+ __OBJC_$_INSTANCE_METHODS_BKEventDeferringGraph(SwiftStuff)
+ __OBJC_$_INSTANCE_METHODS_BKEventDeferringSelectionPathContainer
+ __OBJC_$_INSTANCE_METHODS_BKHIDDomainIncomingServiceConnection
+ __OBJC_$_INSTANCE_METHODS_BKHIDEventDeliveryObserverServer
+ __OBJC_$_INSTANCE_METHODS_BKHIDIncomingServiceConnection
+ __OBJC_$_INSTANCE_METHODS__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_$_INSTANCE_METHODS__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_$_INSTANCE_VARIABLES_BKEventDeferringSelectionPathContainer
+ __OBJC_$_INSTANCE_VARIABLES_BKHIDDomainIncomingServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_BKHIDEventDeliveryObserverServer
+ __OBJC_$_INSTANCE_VARIABLES_BKHIDIncomingServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_$_INSTANCE_VARIABLES__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_$_PROP_LIST_BKHIDDomainIncomingServiceConnection
+ __OBJC_$_PROP_LIST_BKHIDEventDeliveryObserverServer
+ __OBJC_$_PROP_LIST_BKHIDIncomingServiceConnection
+ __OBJC_$_PROP_LIST__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_$_PROP_LIST__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDDomainIncomingServiceConnectionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDEventDeliveryManagerIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDEventDeliveryObserverIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BSServiceListenerConnectionEventObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__BKHIDIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKHIDDomainIncomingServiceConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKHIDEventDeliveryManagerIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKHIDEventDeliveryObserverIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceListenerConnectionEventObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES__BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES__BKHIDIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_REFS_BKHIDDomainIncomingServiceConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_REFS_BKHIDEventDeliveryManagerIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_REFS_BKHIDEventDeliveryObserverIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_REFS_BSDescriptionStreaming
+ __OBJC_$_PROTOCOL_REFS_BSServiceListenerConnectionEventObserver
+ __OBJC_$_PROTOCOL_REFS__BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_$_PROTOCOL_REFS__BKHIDIncomingServiceConnectionHandler
+ __OBJC_CLASS_PROTOCOLS_$_BKEventDeferringSelectionPathContainer
+ __OBJC_CLASS_PROTOCOLS_$_BKHIDDomainIncomingServiceConnection
+ __OBJC_CLASS_PROTOCOLS_$_BKHIDEventDeliveryObserverServer
+ __OBJC_CLASS_PROTOCOLS_$_BKHIDIncomingServiceConnection
+ __OBJC_CLASS_PROTOCOLS_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_CLASS_PROTOCOLS_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_CLASS_RO_$_BKEventDeferringSelectionPathContainer
+ __OBJC_CLASS_RO_$_BKHIDDomainIncomingServiceConnection
+ __OBJC_CLASS_RO_$_BKHIDEventDeliveryObserverServer
+ __OBJC_CLASS_RO_$_BKHIDIncomingServiceConnection
+ __OBJC_CLASS_RO_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_CLASS_RO_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_LABEL_PROTOCOL_$_BKHIDDomainIncomingServiceConnectionDelegate
+ __OBJC_LABEL_PROTOCOL_$_BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_LABEL_PROTOCOL_$_BKHIDEventDeliveryManagerIncomingServiceConnectionHandler
+ __OBJC_LABEL_PROTOCOL_$_BKHIDEventDeliveryObserverIncomingServiceConnectionHandler
+ __OBJC_LABEL_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_LABEL_PROTOCOL_$_BSServiceListenerConnectionEventObserver
+ __OBJC_LABEL_PROTOCOL_$__BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_LABEL_PROTOCOL_$__BKHIDIncomingServiceConnectionHandler
+ __OBJC_METACLASS_RO_$_BKEventDeferringSelectionPathContainer
+ __OBJC_METACLASS_RO_$_BKHIDDomainIncomingServiceConnection
+ __OBJC_METACLASS_RO_$_BKHIDEventDeliveryObserverServer
+ __OBJC_METACLASS_RO_$_BKHIDIncomingServiceConnection
+ __OBJC_METACLASS_RO_$__BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler
+ __OBJC_METACLASS_RO_$__BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler
+ __OBJC_PROTOCOL_$_BKHIDDomainIncomingServiceConnectionDelegate
+ __OBJC_PROTOCOL_$_BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_PROTOCOL_$_BKHIDEventDeliveryManagerIncomingServiceConnectionHandler
+ __OBJC_PROTOCOL_$_BKHIDEventDeliveryObserverIncomingServiceConnectionHandler
+ __OBJC_PROTOCOL_$_BSDescriptionStreaming
+ __OBJC_PROTOCOL_$_BSServiceListenerConnectionEventObserver
+ __OBJC_PROTOCOL_$__BKHIDDomainIncomingServiceConnectionHandler
+ __OBJC_PROTOCOL_$__BKHIDIncomingServiceConnectionHandler
+ ___132-[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:eventDescriptor:getTargetOrder:]_block_invoke
+ ___132-[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:eventDescriptor:getTargetOrder:]_block_invoke_2
+ ___155-[BKHIDDomainServiceServer initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:]_block_invoke
+ ___29-[BKHIDEventSenderCache sync]_block_invoke
+ ___50-[BKEventDeferringNode appendDescriptionToStream:]_block_invoke
+ ___50-[BKEventDeliveryChain appendDescriptionToStream:]_block_invoke
+ ___52-[BKEventDeferringEnvironmentGraph setRules:forPID:]_block_invoke.10
+ ___54-[BKEventDeferringEnvironmentGraph _updateModalityMap]_block_invoke
+ ___54-[BKEventDeferringEnvironmentGraph _updateModalityMap]_block_invoke_2
+ ___54-[BKEventDeferringEnvironmentGraph _updateModalityMap]_block_invoke_3
+ ___54-[BKHIDDomainServiceServer _handleIncomingConnection:]_block_invoke
+ ___54-[BKHIDDomainServiceServer _handleIncomingConnection:]_block_invoke_2
+ ___56-[BKEventDeferringEnvironmentGraph _updateConstraintMap]_block_invoke
+ ___56-[BKEventDeferringEnvironmentGraph _updateConstraintMap]_block_invoke_2
+ ___56-[BKEventDeferringEnvironmentGraph _updateConstraintMap]_block_invoke_3
+ ___57-[BKEventDeliveryChain resolutionPathForEventDescriptor:]_block_invoke
+ ___57-[BKEventDeliveryChain resolutionPathForEventDescriptor:]_block_invoke_2
+ ___60-[BKEventDeferringSelectionPathContainer modalitiesForNode:]_block_invoke
+ ___60-[BKHIDDomainServiceServer acceptIncomingServiceConnection:]_block_invoke
+ ___60-[BKHIDEventDeliveryManagerServer deliveryChainsDescription]_block_invoke
+ ___60-[BKHIDIncomingServiceConnection appendDescriptionToStream:]_block_invoke
+ ___61-[BKEventDeferringSelectionPathContainer constraintsForNode:]_block_invoke
+ ___64-[BKEventDeferringGraph setModalityAssertions:forClientWithPID:]_block_invoke
+ ___65-[BKEventDeferringGraph requestSelectionChange:forClientWithPID:]_block_invoke
+ ___65-[BKHIDEventDeliveryManager _lock_deliveryGraphDescriptionTarget]_block_invoke
+ ___66-[BKEventDeferringGraph setConstraintAssertions:forClientWithPID:]_block_invoke
+ ___66-[BKHIDDomainIncomingServiceConnection appendDescriptionToStream:]_block_invoke
+ ___67-[BKEventDeferringEnvironmentGraph _removeNodesWithIdentities:pid:]_block_invoke
+ ___68-[BKHIDEventDeliveryManager setModalityAssertions:forClientWithPID:]_block_invoke
+ ___69-[BKEventDeferringEnvironmentGraph _updateTopLevelNodesInEachProcess]_block_invoke
+ ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke
+ ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke_2
+ ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke_3
+ ___70-[BKHIDEventDeliveryManager requestSelectionChanges:forClientWithPID:]_block_invoke
+ ___70-[BKHIDEventDeliveryManager setConstraintAssertions:forClientWithPID:]_block_invoke
+ ___73-[BKHIDEventDeliveryObserverService _locked_postChainsToObservingClients]_block_invoke
+ ___74-[BKHIDEventDeliveryManager _lock_setModalityAssertions:forClientWithPID:]_block_invoke
+ ___74-[BKHIDEventDeliveryManager _lock_setModalityAssertions:forClientWithPID:]_block_invoke_2
+ ___75-[BKEventDeferringEnvironmentGraph setModalityAssertions:forClientWithPID:]_block_invoke
+ ___75-[BKEventDeferringEnvironmentGraph setModalityAssertions:forClientWithPID:]_block_invoke_2
+ ___76-[BKHIDEventDeliveryManager _lock_requestSelectionChanges:forClientWithPID:]_block_invoke
+ ___76-[BKHIDEventDeliveryManager _lock_setConstraintAssertions:forClientWithPID:]_block_invoke
+ ___77-[BKEventDeferringEnvironmentGraph setConstraintAssertions:forClientWithPID:]_block_invoke
+ ___79-[BKHIDEventDeliveryManager _lock_destinationsForKeyCommand:sender:transcript:]_block_invoke.193
+ ___81-[BKEventDeferringEnvironmentGraph _selectDeferringPathForRequest:requestingPID:]_block_invoke
+ ___block_descriptor_32_e47_B16?0"BKSHIDEventDeferringModalityAssertion"8l
+ ___block_descriptor_32_e49_B16?0"BKSHIDEventDeferringConstraintAssertion"8l
+ ___block_descriptor_32_e52_B16?0"BKSHIDEventDeferringSelectionChangeRequest"8l
+ ___block_descriptor_32_e77_"BKSHIDEventDeferringModality"16?0"BKSHIDEventDeferringModalityAssertion"8l
+ ___block_descriptor_32_e81_"BKSHIDEventDeferringConstraint"16?0"BKSHIDEventDeferringConstraintAssertion"8l
+ ___block_descriptor_36_e34_16?0"BKSHIDEventDeliveryChain"8l
+ ___block_descriptor_36_e54_v24?0"BKEventDeferringEnvironmentGraph"8"NSArray"16l
+ ___block_descriptor_40_e8_32s_e100_v32?0"BKSHIDEventDeferringSelectionPathIdentifier"8"BKEventDeferringSelectionPathContainer"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e28_16?0"BKSHIDEventDisplay"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_B32?0"BKEventDeferringNode"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e47_"<NSCopying>"16?0"<_BKSelectionTargetable>"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_B16?0"BKSHIDEventDeferringModalityAssertion"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v32?0"NSNumber"8"BKEventDeferringNode"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e62_v32?0"BKEventDeferringSelectionPathContainer"8"NSSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_40_e8_32w_e37_v16?0"BSServiceListenerConnection"8lw32l8
+ ___block_descriptor_44_e8_32s_e47_16?0"BKSHIDEventDeferringModalityAssertion"8ls32l8
+ ___block_descriptor_44_e8_32s_e54_v24?0"BKEventDeferringEnvironmentGraph"8"NSArray"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e56_v32?0"BKSEventDeferringChainIdentity"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e62_v32?0"BKEventDeferringSelectionPathContainer"8"NSSet"16^B24ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8s40l8s48l8
+ ___block_descriptor_61_e8_32s40s48s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s_e45_v16?0"BKSMutableHIDEventPolicyObservation"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.117
+ ___block_literal_global.120
+ ___block_literal_global.123
+ ___block_literal_global.1490
+ ___block_literal_global.1667
+ ___block_literal_global.206
+ ___block_literal_global.2084
+ ___block_literal_global.221
+ ___block_literal_global.237
+ ___block_literal_global.24.2566
+ ___block_literal_global.240
+ ___block_literal_global.2593
+ ___block_literal_global.2932
+ ___block_literal_global.3025
+ ___block_literal_global.3219
+ ___block_literal_global.33.2556
+ ___block_literal_global.3323
+ ___block_literal_global.357
+ ___block_literal_global.6.3028
+ ___block_literal_global.717
+ ___block_literal_global.80
+ ___block_literal_global.91
+ ___block_literal_global.91.3223
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy24_8
+ ___swift_memcpy33_8
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_BackBoardHIDEventFoundation
+ __swift_stdlib_reportUnimplementedInitializer
+ _bzero
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_expectDeallocation
+ _objc_msgSend$_isString
+ _objc_msgSend$_keyForNode:
+ _objc_msgSend$_removeNode:
+ _objc_msgSend$_servicesForIOHIDServiceRefs:
+ _objc_msgSend$acceptConnection
+ _objc_msgSend$acceptConnectionWithMappedObject:
+ _objc_msgSend$acceptIncomingServiceConnection:
+ _objc_msgSend$acceptIncomingServiceConnection:mappedObject:
+ _objc_msgSend$activeInputModality
+ _objc_msgSend$addEventObserver:
+ _objc_msgSend$addSibling:
+ _objc_msgSend$addSubnode:
+ _objc_msgSend$auditToken
+ _objc_msgSend$basis
+ _objc_msgSend$bs_array
+ _objc_msgSend$configurationWithDomain:service:
+ _objc_msgSend$configure:
+ _objc_msgSend$connection:setObservesDeferringChainIdentities:entitled:
+ _objc_msgSend$connection:setObservesDeferringResolutions:
+ _objc_msgSend$connectionDidTerminate:
+ _objc_msgSend$connectionWillBegin:
+ _objc_msgSend$constraint
+ _objc_msgSend$constraintAssertions
+ _objc_msgSend$constraintBasis
+ _objc_msgSend$deliveryChainsDescription
+ _objc_msgSend$deliveryManagerForAuditToken:
+ _objc_msgSend$deliveryObserverServiceForAuditToken:
+ _objc_msgSend$describeDeliveryChain:identifier:
+ _objc_msgSend$describeDeliveryChains:identifier:
+ _objc_msgSend$domainIncomingServiceConnection
+ _objc_msgSend$domainServiceServer
+ _objc_msgSend$eventDescriptorIsRestricted:
+ _objc_msgSend$eventProvenance
+ _objc_msgSend$everySelectionPath
+ _objc_msgSend$graphDescriptionWithLabel:
+ _objc_msgSend$handleIncomingDeliveryManagerConnection:
+ _objc_msgSend$handleIncomingDeliveryObserverConnection:
+ _objc_msgSend$handleIncomingServiceConnection:
+ _objc_msgSend$hasBeenSignalled
+ _objc_msgSend$hasSuccinctStyle
+ _objc_msgSend$ignoreModalities
+ _objc_msgSend$incomingServiceConnectionDidRevoke:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithConnection:log:
+ _objc_msgSend$initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:
+ _objc_msgSend$initWithDomainServiceServer:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:
+ _objc_msgSend$initWithIncomingServiceConnection:debugMappedObjectName:
+ _objc_msgSend$initWithIncomingServiceConnectionHandler:
+ _objc_msgSend$initWithIncomingServiceConnectionHandler:ruleChangeAuthority:
+ _objc_msgSend$initWithMatchingDictionary:serviceClass:dataProvider:
+ _objc_msgSend$initWithObjects:count:
+ _objc_msgSend$isRevoked
+ _objc_msgSend$listenerWithConfiguration:handler:
+ _objc_msgSend$log
+ _objc_msgSend$modality
+ _objc_msgSend$modalityAssertions
+ _objc_msgSend$pathIdentifier
+ _objc_msgSend$performAsyncAndWait:
+ _objc_msgSend$popSection:
+ _objc_msgSend$primary
+ _objc_msgSend$pushSection
+ _objc_msgSend$queue
+ _objc_msgSend$queueWithName:
+ _objc_msgSend$rejectConnection
+ _objc_msgSend$rejectIncomingServiceConnection:
+ _objc_msgSend$requestSelectionChanges:forClientWithPID:
+ _objc_msgSend$ruleOriginatorBasis
+ _objc_msgSend$selectionPath
+ _objc_msgSend$selectionPathIdentifier
+ _objc_msgSend$selectionRequests
+ _objc_msgSend$selectionTarget
+ _objc_msgSend$setBasis:
+ _objc_msgSend$setConstraintAssertions:forClientWithPID:
+ _objc_msgSend$setFinalStringToken:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$setModalityAssertions:forClientWithPID:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setSelectionPath:
+ _objc_msgSend$signal
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$subsetForPID:
+ _objc_msgSend$succinctStyle
+ _objc_msgSend$timestamp
+ _objc_msgSend$validateMessage:
+ _objc_msgSend$verifyAuthentic:
+ _objc_opt_self
+ _objc_retain_x5
+ _sharedInstance.onceToken.2931
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_native
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_retain_n
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic SS
+ _symbolic Say_____G 27BackBoardHIDEventFoundation10_GraphNode33_924A0A2DAF65EBFF9E2C8DDA409C596ALLC
+ _symbolic Sb
+ _symbolic ShySiG
+ _symbolic Si
+ _symbolic So8NSObjectC
+ _symbolic _____ 27BackBoardHIDEventFoundation10_GraphNode33_924A0A2DAF65EBFF9E2C8DDA409C596ALLC
+ _symbolic _____ 27BackBoardHIDEventFoundation22UnicodeArtTreeRendererV
+ _symbolic _____ 27BackBoardHIDEventFoundation22_BKGraphSectionWrapperC
+ _symbolic _____ 27BackBoardHIDEventFoundation23UnicodeArtTreePrimitive33_77387F2FE86C381C58D563EE66E0135DLLV
+ _symbolic _____Sg 27BackBoardHIDEventFoundation10_GraphNode33_924A0A2DAF65EBFF9E2C8DDA409C596ALLC
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____ySo24BKSHIDEventDeferringRuleCG s11_SetStorageC
+ _type_layout_string 27BackBoardHIDEventFoundation22UnicodeArtTreeRendererV
+ _type_layout_string 27BackBoardHIDEventFoundation23UnicodeArtTreePrimitive33_77387F2FE86C381C58D563EE66E0135DLLV
- -[BKEventDeferringEnvironmentGraph _chooseSubnodeOfNode:appendToPath:]
- -[BKEventDeferringEnvironmentGraph _logNodes:toGraphDescription:]
- -[BKEventDeferringEnvironmentGraph _policyNodeFromCollection:]
- -[BKEventDeferringEnvironmentGraph _reevaluateActiveUIResponderNodesForPID:]
- -[BKEventDeferringEnvironmentGraph setActiveUIResponderTokens:forPID:]
- -[BKEventDeferringGraph deferringPathForPID:environment:display:dispatchTarget:]
- -[BKEventDeferringGraph setActiveUIResponderPredicates:forPID:]
- -[BKEventDeferringNode appendDescriptionToFormatter:]
- -[BKEventDeferringNode appendGraphDescription:]
- -[BKEventDeliveryChain appendDescriptionToFormatter:]
- -[BKEventDeliveryChain resolutionPath]
- -[BKEventGraphDescriptionAccumulator .cxx_destruct]
- -[BKEventGraphDescriptionAccumulator _nodeWithSupernode:format:args:]
- -[BKEventGraphDescriptionAccumulator _recursiveAppendNode:toDescription:]
- -[BKEventGraphDescriptionAccumulator init]
- -[BKEventGraphDescriptionAccumulator popSection:]
- -[BKEventGraphDescriptionAccumulator pushSection]
- -[BKGraphDescription .cxx_destruct]
- -[BKGraphDescription _themeForItemIndex:]
- -[BKGraphDescription appendNode:]
- -[BKGraphDescription appendSubnodesWithCount:block:]
- -[BKGraphDescription initWithTopLevelCount:target:]
- -[BKHIDDomainServiceServer _removeConnection:process:]
- -[BKHIDDomainServiceServer initWithDelegate:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:]
- -[BKHIDDomainServiceServer listener:didReceiveConnection:withContext:]
- -[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:getTargetOrder:]
- -[BKHIDEventDeliveryManager _recursiveAppendNodes:index:toGraphDescription:]
- -[BKHIDEventDeliveryManager forceSelectDeferringTarget:forEnvironment:forClientWithPID:]
- -[BKHIDEventDeliveryManager selectDeferringPredicate:forClientWithPID:]
- -[BKHIDEventDeliveryManager setActiveUIResponders:forClientWithPID:]
- -[BKHIDEventDeliveryManagerServer _performDescriptionRetrieval:forAuditToken:]
- -[BKHIDEventDeliveryManagerServer connectionDidTerminate:process:]
- -[BKHIDEventDeliveryManagerServer initWithDeliveryManager:ruleChangeAuthority:]
- -[BKHIDEventDeliveryManagerServer selectDeferringTargetForPredicate:]
- -[BKHIDEventDeliveryObserverService connectionDidTerminate:process:]
- -[BKHIDEventDeliveryObserverService init]
- -[BKHIDEventDeliveryObserverService setObservesDeferringChainIdentities:]
- -[BKHIDEventDeliveryObserverService setObservesDeferringResolutions:]
- -[BKOSLogTranscriptTarget writePrefix:label:args:]
- -[BKStringTranscriptTarget writePrefix:label:args:]
- -[_BKGraphStructureNode .cxx_destruct]
- -[_BKGraphStructureNode init]
- GCC_except_table169
- GCC_except_table265
- GCC_except_table277
- GCC_except_table280
- GCC_except_table286
- GCC_except_table289
- GCC_except_table505
- GCC_except_table553
- _CFStringAppend
- _CFStringAppendFormat
- _CFStringAppendFormatAndArguments
- _OBJC_CLASS_$_BKGraphDescription
- _OBJC_CLASS_$_BSServiceQuality
- _OBJC_CLASS_$__BKGraphStructureNode
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._pidToActiveUIResponderNodes
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._pidToActiveUIResponderTokens
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._selectedNodeIdentities
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._tokenToNode
- _OBJC_IVAR_$_BKEventDeferringNode._isActiveUIResponder
- _OBJC_IVAR_$_BKEventGraphDescriptionAccumulator._current
- _OBJC_IVAR_$_BKEventGraphDescriptionAccumulator._topLevel
- _OBJC_IVAR_$_BKGraphDescription._itemCountStack
- _OBJC_IVAR_$_BKGraphDescription._itemRemainingStack
- _OBJC_IVAR_$_BKGraphDescription._stackIndexesHighlighted
- _OBJC_IVAR_$_BKGraphDescription._target
- _OBJC_IVAR_$_BKHIDDomainServiceServer._invalid
- _OBJC_IVAR_$_BKHIDDomainServiceServer._lock_connectionsByPID
- _OBJC_IVAR_$_BKHIDEventDeliveryManager._deferringRulesByPID
- _OBJC_IVAR_$_BKHIDEventDeliveryManagerServer._deliveryManager
- _OBJC_IVAR_$_BKHIDEventDeliveryManagerServer._observerPIDs
- _OBJC_IVAR_$_BKHIDEventDeliveryManagerServer._resolutionsByPID
- _OBJC_IVAR_$__BKGraphStructureNode._label
- _OBJC_IVAR_$__BKGraphStructureNode._subnodes
- _OBJC_IVAR_$__BKGraphStructureNode._supernode
- _OBJC_METACLASS_$_BKGraphDescription
- _OBJC_METACLASS_$__BKGraphStructureNode
- __BKHighlightedTheme.dictionary
- __BKHighlightedTheme.onceToken
- __BKNormalTheme.dictionary
- __BKNormalTheme.onceToken
- __OBJC_$_INSTANCE_METHODS_BKEventDeferringEnvironmentGraph
- __OBJC_$_INSTANCE_METHODS_BKEventDeferringGraph
- __OBJC_$_INSTANCE_METHODS_BKEventGraphDescriptionAccumulator
- __OBJC_$_INSTANCE_METHODS_BKGraphDescription
- __OBJC_$_INSTANCE_METHODS__BKGraphStructureNode
- __OBJC_$_INSTANCE_VARIABLES_BKEventGraphDescriptionAccumulator
- __OBJC_$_INSTANCE_VARIABLES_BKGraphDescription
- __OBJC_$_INSTANCE_VARIABLES__BKGraphStructureNode
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionListenerDelegate
- __OBJC_$_PROTOCOL_REFS_BSServiceConnectionListenerDelegate
- __OBJC_CLASS_RO_$_BKEventGraphDescriptionAccumulator
- __OBJC_CLASS_RO_$_BKGraphDescription
- __OBJC_CLASS_RO_$__BKGraphStructureNode
- __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionListenerDelegate
- __OBJC_METACLASS_RO_$_BKEventGraphDescriptionAccumulator
- __OBJC_METACLASS_RO_$_BKGraphDescription
- __OBJC_METACLASS_RO_$__BKGraphStructureNode
- __OBJC_PROTOCOL_$_BSServiceConnectionListenerDelegate
- ___116-[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:getTargetOrder:]_block_invoke
- ___122-[BKHIDDomainServiceServer initWithDelegate:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:]_block_invoke
- ___38-[BKEventDeliveryChain resolutionPath]_block_invoke
- ___38-[BKEventDeliveryChain resolutionPath]_block_invoke_2
- ___45-[BKEventDeferringGraph processDidTerminate:]_block_invoke
- ___47-[BKEventDeferringNode appendGraphDescription:]_block_invoke
- ___51-[BKHIDDomainServiceServer _addConnection:process:]_block_invoke
- ___53-[BKHIDEventDeliveryManager deliveryGraphDescription]_block_invoke
- ___59-[BKEventDeferringEnvironmentGraph appendGraphDescription:]_block_invoke
- ___59-[BKEventDeferringEnvironmentGraph appendGraphDescription:]_block_invoke_2
- ___62-[BKEventDeferringEnvironmentGraph _updateNodeTopLevelStatus:]_block_invoke
- ___63-[BKEventDeferringGraph setActiveUIResponderPredicates:forPID:]_block_invoke
- ___63-[BKEventDeferringGraph setActiveUIResponderPredicates:forPID:]_block_invoke_2
- ___63-[BKEventDeferringGraph setActiveUIResponderPredicates:forPID:]_block_invoke_3
- ___65-[BKEventDeferringEnvironmentGraph _logNodes:toGraphDescription:]_block_invoke
- ___70-[BKHIDDomainServiceServer listener:didReceiveConnection:withContext:]_block_invoke
- ___70-[BKHIDDomainServiceServer listener:didReceiveConnection:withContext:]_block_invoke.18
- ___70-[BKHIDDomainServiceServer listener:didReceiveConnection:withContext:]_block_invoke_2
- ___73-[BKEventGraphDescriptionAccumulator _recursiveAppendNode:toDescription:]_block_invoke
- ___76-[BKEventDeferringEnvironmentGraph _reevaluateActiveUIResponderNodesForPID:]_block_invoke
- ___76-[BKHIDEventDeliveryManager _recursiveAppendNodes:index:toGraphDescription:]_block_invoke
- ___77-[BKHIDEventDeliveryManager _lock_selectDeferringPredicate:forClientWithPID:]_block_invoke
- ___79-[BKHIDEventDeliveryManager _lock_destinationsForKeyCommand:sender:transcript:]_block_invoke.166
- ___86-[BKHIDEventDeliveryManager _lock_resolveEventDescriptor:senderDescriptor:transcript:]_block_invoke
- ___86-[BKHIDEventDeliveryManager _lock_resolveEventDescriptor:senderDescriptor:transcript:]_block_invoke_2
- ____BKHighlightedTheme_block_invoke
- ____BKNormalTheme_block_invoke
- ___block_descriptor_32_e39_16?0"BKSHIDEventDeferringPredicate"8l
- ___block_descriptor_32_e52_"<NSCopying>"16?0"BKSHIDEventDeferringPredicate"8l
- ___block_descriptor_36_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24l
- ___block_descriptor_40_e8_32s_e35_16?0"BKSHIDEventDeferringToken"8ls32l8
- ___block_descriptor_48_e8_32s40s_e29_v16?0"BSServiceConnection"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e39_v32?0"NSNumber"8"NSOrderedSet"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s_e45_v16?0"BKSMutableHIDEventPolicyObservation"8ls32l8s40l8s48l8
- ___block_literal_global.1226
- ___block_literal_global.1387
- ___block_literal_global.1637
- ___block_literal_global.174
- ___block_literal_global.1766
- ___block_literal_global.178
- ___block_literal_global.195
- ___block_literal_global.211
- ___block_literal_global.2134
- ___block_literal_global.214
- ___block_literal_global.2215
- ___block_literal_global.24.2187
- ___block_literal_global.2556
- ___block_literal_global.2721
- ___block_literal_global.278
- ___block_literal_global.2846
- ___block_literal_global.29
- ___block_literal_global.33.2177
- ___block_literal_global.38
- ___block_literal_global.44
- ___block_literal_global.507
- ___block_literal_global.55
- _objc_msgSend$activeUIResponders
- _objc_msgSend$configureConnection:
- _objc_msgSend$connectionDidBegin:process:
- _objc_msgSend$connectionDidTerminate:process:
- _objc_msgSend$containsIndex:
- _objc_msgSend$initWithDelegate:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:
- _objc_msgSend$initWithIdentity:compatibilityDisplay:path:
- _objc_msgSend$initWithServer:
- _objc_msgSend$listenerWithConfigurator:
- _objc_msgSend$new
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$remoteProcess
- _objc_msgSend$removeLastObject
- _objc_msgSend$selectDeferringPredicate:forClientWithPID:
- _objc_msgSend$setActiveUIResponders:forClientWithPID:
- _objc_msgSend$setDomain:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setService:
- _objc_msgSend$setServiceQuality:
- _objc_msgSend$setTargetQueue:
- _objc_msgSend$userInitiated
- _objc_msgSend$writePrefix:label:args:
- _sharedInstance.onceToken.2555
CStrings:
+ "\nDeferring rules:\n"
+ "2"
+ "<nil>"
+ "<root>"
+ "@\"<BKHIDDomainIncomingServiceConnectionDelegate>\""
+ "@\"<BKHIDDomainIncomingServiceConnectionHandler>\""
+ "@\"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>\""
+ "@\"<BKHIDEventDeliveryManagerProvider>\""
+ "@\"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>\""
+ "@\"<BKHIDEventDeliveryObserverServiceProvider>\""
+ "@\"<BKHIDIncomingServiceConnectionDelegate>\""
+ "@\"<BSInvalidatable>\""
+ "@\"<NSCopying>\"16@?0@\"<_BKSelectionTargetable>\"8"
+ "@\"<_BKHIDDomainIncomingServiceConnectionHandler>\""
+ "@\"<_BKHIDIncomingServiceConnectionHandler>\""
+ "@\"BKEventDeferringEnvironmentGraph\""
+ "@\"BKHIDDomainIncomingServiceConnection\""
+ "@\"BKHIDEventDeliveryObserverService\""
+ "@\"BKSHIDEventDeferringConstraint\"16@?0@\"BKSHIDEventDeferringConstraintAssertion\"8"
+ "@\"BKSHIDEventDeferringModality\"16@?0@\"BKSHIDEventDeferringModalityAssertion\"8"
+ "@\"BKSHIDEventDeferringSelectionPathIdentifier\""
+ "@\"BKSHIDEventSimpleProvenanceOriginator\""
+ "@\"BSAtomicSignal\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceListenerConnection\""
+ "@16@?0@\"BKSHIDEventDeferringModalityAssertion\"8"
+ "@16@?0@\"BKSHIDEventDeliveryChain\"8"
+ "@16@?0@\"BKSHIDEventDisplay\"8"
+ "@28@0:8@16B24"
+ "@32@0:8[44@]16@24"
+ "@40@0:8@16#24@32"
+ "@48@0:8@16@24@32^{__IOHIDEvent=}40"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "B16@?0@\"BKSHIDEventDeferringConstraintAssertion\"8"
+ "B16@?0@\"BKSHIDEventDeferringModalityAssertion\"8"
+ "B16@?0@\"BKSHIDEventDeferringSelectionChangeRequest\"8"
+ "B32@?0@\"BKEventDeferringNode\"8Q16^B24"
+ "BKEventDeferringEnvironmentGraph.m"
+ "BKEventDeferringNode.m"
+ "BKEventDeferringSelectionPathContainer"
+ "BKHIDDomainIncomingServiceConnection"
+ "BKHIDDomainIncomingServiceConnection.m"
+ "BKHIDDomainIncomingServiceConnectionDelegate"
+ "BKHIDDomainIncomingServiceConnectionHandler"
+ "BKHIDDomainServiceServer.m"
+ "BKHIDEventDeliveryManagerIncomingServiceConnectionHandler"
+ "BKHIDEventDeliveryManagerServer.m"
+ "BKHIDEventDeliveryObserverIncomingServiceConnectionHandler"
+ "BKHIDEventDeliveryObserverServer"
+ "BKHIDEventDeliveryObserverServer.m"
+ "BKHIDEventDeliveryObserverService.m"
+ "BKHIDIncomingServiceConnection"
+ "BKHIDIncomingServiceConnection.m"
+ "BSDescriptionStreaming"
+ "BSServiceListenerConnectionEventObserver"
+ "BackBoardHIDEventFoundation._BKGraphSectionWrapper"
+ "CHOOSE %{public}@ @ %{public}@"
+ "CHOOSE %{public}@ done"
+ "CHOOSE %{public}@ subnode:%{public}@"
+ "Client code must accept/reject the connection <%@:%p> before dealloc"
+ "Incoming connection revoked: %{public}@  - not notifying delegate %p because this incoming connection was already handled"
+ "Incoming connection revoked: %{public}@  - notifying delegate %p"
+ "SwiftStuff"
+ "T@\"<BKHIDDomainIncomingServiceConnectionDelegate>\",N"
+ "T@\"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>\",R,N"
+ "T@\"<BKHIDEventDeliveryManagerServerRuleChangeAuthority>\",R,N"
+ "T@\"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>\",R,N"
+ "T@\"<BKHIDIncomingServiceConnectionDelegate>\",N"
+ "T@\"<_BKHIDDomainIncomingServiceConnectionHandler>\",N"
+ "T@\"<_BKHIDIncomingServiceConnectionHandler>\",N"
+ "T@\"BKHIDDomainIncomingServiceConnection\",R,N,V_domainIncomingServiceConnection"
+ "T@\"BKHIDDomainServiceServer\",R,N"
+ "T@\"BKHIDEventDeliveryObserverService\",&,N,V_resolutionObserver"
+ "T@\"BKHIDEventDeliveryObserverService\",R,N"
+ "T@\"BKSHIDEventSimpleProvenanceOriginator\",R,N,V_simpleProvenanceOriginator"
+ "T@\"BSAuditToken\",R,N"
+ "T@\"BSServiceListenerConnection\",R,N,V_connection"
+ "T@\"NSObject<OS_os_log>\",R,N,V_log"
+ "TB,R,N,GisRevoked"
+ "Unable to find delivery chains for target: %{public}@, chainId: %{public}@"
+ "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting because target is not reachable due to constraints -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting because we can't switch from activeInput to not-activeInput -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting hostOverride: not hosted by pid(%d) -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting: parent not in selection path -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath:%{public}@ requestingPID:(%d) toNode:%{public}@"
+ "[%{public}@ %p] setConstraintAssertions:forPID(%d): %{public}@"
+ "[%{public}@ %p] setModalityAssertions:forPID(%d): %{public}@"
+ "[%{public}@ %p] setRules:forPID(%d): %{public}@"
+ "[44@\"NSArray\"]"
+ "_BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler"
+ "_BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler"
+ "_BKHIDDomainIncomingServiceConnectionHandler"
+ "_BKHIDIncomingServiceConnectionHandler"
+ "_TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper"
+ "_TtC27BackBoardHIDEventFoundationP33_924A0A2DAF65EBFF9E2C8DDA409C596A10_GraphNode"
+ "_changeSelectionPath:toNode:requestingPID:basis:ignoreModality:"
+ "_connection"
+ "_constraintAssertionsByClientPID"
+ "_constraintAssertionsByNode"
+ "_debugMappedObjectName"
+ "_deliveryManagerForEstablishedConnection:"
+ "_deliveryManagerProvider"
+ "_deliveryObserverServiceForEstablishedConnection:"
+ "_deliveryObserverServiceProvider"
+ "_domainIncomingServiceConnection"
+ "_entitledToObserveFullDeliveryChain"
+ "_environmentGraph"
+ "_includedIdentities"
+ "_incomingConnectionHandler"
+ "_incomingServiceConnectionHandler"
+ "_invalidSignal"
+ "_isString"
+ "_keyForNode:"
+ "_lock_activeConnectionsByPID"
+ "_lock_delegate"
+ "_lock_eventObserver"
+ "_lock_handler"
+ "_lock_submitRuleChanges:validatedContentsMask:connection:"
+ "_lock_wasHandled"
+ "_modalities"
+ "_modalityAssertionsByClientPID"
+ "_modalityAssertionsByNode"
+ "_nodeByDeferringTarget"
+ "_observerService"
+ "_pathIdentifier"
+ "_performDescriptionRetrieval:forConnection:"
+ "_previousProvenanceTimestamp"
+ "_removeNode:"
+ "_selectDeferringPathForRequest:requestingPID:"
+ "_selectionPathContainerByIdentifier"
+ "_servicesForIOHIDServiceRefs:"
+ "_simpleProvenanceOriginator"
+ "_subnodeSelectionHistoryByNodeIdentity"
+ "acceptConnection"
+ "acceptConnectionWithMappedObject:"
+ "acceptIncomingServiceConnection:"
+ "acceptIncomingServiceConnection:mappedObject:"
+ "activating connection (%{public}@) - %{public}@"
+ "activeInputModality"
+ "addEventObserver:"
+ "addSibling:"
+ "addSubnode:"
+ "appendDescriptionToStream:"
+ "auditToken"
+ "authority"
+ "basis"
+ "basis decaying pid:%d (%{public}@)"
+ "bs_array"
+ "can't disconnect the root"
+ "can't set delegate for connection: %{public}@, already handled"
+ "can't set handler for connection: %{public}@, already handled"
+ "com.apple.backboardd.hitTestFilterBySender"
+ "configurationWithDomain:service:"
+ "configure:"
+ "connection:revokedWithEvent:"
+ "connection:setObservesDeferringChainIdentities:entitled:"
+ "connection:setObservesDeferringResolutions:"
+ "connectionDidTerminate:"
+ "connectionWillBegin:"
+ "constraint"
+ "constraintAssertions"
+ "constraintBasis"
+ "constraints"
+ "constraints(%{public}@) now %{public}@"
+ "current"
+ "delivery manager"
+ "delivery observer service"
+ "deliveryChainsDescription"
+ "deliveryChainsForDeferringTarget:display:environment:event:"
+ "deliveryManagerForAuditToken:"
+ "deliveryManagerProvider"
+ "deliveryObserverServiceForAuditToken:"
+ "deliveryObserverServiceProvider"
+ "describeDeliveryChain:identifier:"
+ "describeDeliveryChains:identifier:"
+ "disconnectFromGraph"
+ "domainIncomingServiceConnection"
+ "domainServiceServer"
+ "dropping request from pid:%d (%{public}@)"
+ "event != ((void*)0)"
+ "eventDescriptorIsRestricted:"
+ "eventProvenance"
+ "everySelectionPath"
+ "failed to find delivery manager for established connection: %@"
+ "failed to find delivery observer service for established connection: %@"
+ "failed to provide %@ while activating incoming connection: %@"
+ "failed to provide delivery manager for auditToken: %@"
+ "failed to provide delivery manager for incoming connection: %@"
+ "failed to provide delivery observer service for auditToken: %@"
+ "failed to provide delivery observer service for incoming connection: %@"
+ "graphDescriptionWithLabel:"
+ "handleIncomingDeliveryManagerConnection:"
+ "handleIncomingDeliveryObserverConnection:"
+ "handleIncomingServiceConnection:"
+ "handled"
+ "handler"
+ "hasBeenSignalled"
+ "hasSuccinctStyle"
+ "ignoreModalities"
+ "ignoring call to acceptConnection: %{public}@, already handled"
+ "ignoring call to acceptConnection: %{public}@, no handler"
+ "ignoring call to rejectConnection: %{public}@, already handled"
+ "ignoring call to rejectConnection: %{public}@, no handler"
+ "incomingConnection"
+ "incomingConnectionHandler"
+ "incomingServiceConnectionDidRevoke:"
+ "incomingServiceConnectionHandler"
+ "indexOfObjectPassingTest:"
+ "init()"
+ "initWithConnection:log:"
+ "initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:"
+ "initWithDeliveryManagerProvider:"
+ "initWithDeliveryManagerProvider:ruleChangeAuthority:"
+ "initWithDeliveryObserverServiceProvider:"
+ "initWithDomainServiceServer:"
+ "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:"
+ "initWithIncomingServiceConnection:debugMappedObjectName:"
+ "initWithIncomingServiceConnectionHandler:"
+ "initWithIncomingServiceConnectionHandler:ruleChangeAuthority:"
+ "initWithMatchingDictionary:serviceClass:dataProvider:"
+ "initWithObjects:count:"
+ "invalidating connection (%{public}@) - %{public}@"
+ "isRevoked"
+ "label"
+ "listenerWithConfiguration:handler:"
+ "log"
+ "logCategory"
+ "missing constraint assertions from pid:%d"
+ "missing modality assertions from pid:%d"
+ "missing record"
+ "missing selection requests from pid:%d"
+ "modalities"
+ "modality"
+ "modalityAssertions"
+ "no delivery manager provider"
+ "no delivery observer service"
+ "no delivery observer service provider"
+ "observerService"
+ "pathIdentifier"
+ "performAsyncAndWait:"
+ "predicate != ((void*)0)"
+ "previous"
+ "primary"
+ "priority"
+ "pushSection"
+ "queue"
+ "queueWithName:"
+ "rejectConnection"
+ "rejectIncomingServiceConnection:"
+ "remotePID"
+ "requestSelectionChanges: missing basis: %{public}@"
+ "requestSelectionChanges: missing deferring target: %{public}@"
+ "requestSelectionChanges: missing selection path: %{public}@"
+ "requestSelectionChanges: missing selection target: %{public}@"
+ "requestSelectionChanges:forClientWithPID:"
+ "revoked"
+ "ruleChangeAuthority"
+ "ruleOriginatorBasis"
+ "selected"
+ "selection history %{public}@ (add %{public}@): %{public}@"
+ "selection history %{public}@ (remove %{public}@): %{public}@"
+ "selection request deferring target is nil: %{public}@"
+ "selection request deferring target token is nil: %{public}@"
+ "selection request target not found: %{public}@"
+ "selection request token is not accessible by the requesting process(%{public}@): %{public}@"
+ "selectionPath"
+ "selectionPathIdentifier"
+ "selectionRequests"
+ "selectionTarget"
+ "senders != ((void*)0)"
+ "server"
+ "service"
+ "setBasis:"
+ "setConstraintAssertions: missing deferring target: %{public}@"
+ "setConstraintAssertions: missing selection path: %{public}@"
+ "setConstraintAssertions: missing selection target: %{public}@"
+ "setConstraintAssertions:forClientWithPID:"
+ "setFinalStringToken:"
+ "setHandler:"
+ "setModalityAssertions: missing basis: %{public}@"
+ "setModalityAssertions: missing deferring target: %{public}@"
+ "setModalityAssertions: missing selection path: %{public}@"
+ "setModalityAssertions: missing selection target: %{public}@"
+ "setModalityAssertions:forClientWithPID:"
+ "setQueue:"
+ "setSelectionPath:"
+ "signal"
+ "simpleProvenanceOriginator"
+ "subarrayWithRange:"
+ "subnodes"
+ "subsetForPID:"
+ "succinctStyle"
+ "supernode"
+ "sync"
+ "target != ((void*)0)"
+ "targetNode != ((void*)0)"
+ "timestamp"
+ "topLevel"
+ "v16@?0@\"<BSServiceListenerConnectionConfiguring>\"8"
+ "v16@?0@\"BKEventDeferringSelectionPathContainer\"8"
+ "v16@?0@\"BSServiceListenerConnection\"8"
+ "v16@?0@\"BSServiceListenerConnection<BSServiceConnectionContext>\"8"
+ "v24@0:8@\"BKHIDDomainIncomingServiceConnection\"16"
+ "v24@0:8@\"BKHIDIncomingServiceConnection\"16"
+ "v24@0:8@\"BSDescriptionStream\"16"
+ "v24@0:8@\"BSServiceListenerConnection\"16"
+ "v24@?0@\"BKEventDeferringEnvironmentGraph\"8@\"NSArray\"16"
+ "v32@0:8@\"BKHIDIncomingServiceConnection\"16@24"
+ "v32@0:8@\"BSServiceListenerConnection\"16@\"<BSServiceListenerConnectionRevocationEvent>\"24"
+ "v32@?0@\"BKEventDeferringSelectionPathContainer\"8@\"NSSet\"16^B24"
+ "v32@?0@\"BKSHIDEventDeferringSelectionPathIdentifier\"8@\"BKEventDeferringSelectionPathContainer\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"BKEventDeferringNode\"16^B24"
+ "v36@0:8@16@24B32"
+ "validateMessage:"
+ "verifyAuthentic:"
+ "verifyProvenance: corrupt provenance"
+ "verifyProvenance: event too old (expected %llu > %llu)"
+ "verifyProvenance: unfamiliar class %{public}@"
- "\x02% "
- "\x03% "
- "\t"
- "\f%"
- "\x0f%\x01%\xcf%\x01%"
- "\x14%"
- "\x17%\x01%\xcf%\x01%"
- "\x1c%"
- " "
- "  "
- "#%\x01%\xcf%\x01%"
- "%@ <%@>"
- "%{public}@%{public}@"
- "'%public@' tried to observe deferring chains. That's illegal."
- "(%@)"
- "<pid: %d; token: %@>"
- "<token: %@>"
- "@\"<BKHIDEventDeliveryResolutionObserver>\""
- "@\"<BKTranscriptTarget>\""
- "@\"<NSCopying>\"16@?0@\"BKSHIDEventDeferringPredicate\"8"
- "@\"NSMutableIndexSet\""
- "@\"_BKGraphStructureNode\""
- "@16@?0@\"BKSHIDEventDeferringPredicate\"8"
- "@16@?0@\"BKSHIDEventDeferringToken\"8"
- "@32@0:8[43@]16@24"
- "BKEventGraphTranscript.m"
- "BKGraphDescription"
- "BSServiceConnectionListenerDelegate"
- "T@\"<BKHIDEventDeliveryResolutionObserver>\",&,N,V_resolutionObserver"
- "Vv24@0:8@\"BKSHIDEventDeferringPredicate\"16"
- "[43@\"NSArray\"]"
- "_BKGraphStructureNode"
- "_current"
- "_deferringRulesByPID"
- "_isActiveUIResponder"
- "_itemCountStack"
- "_itemRemainingStack"
- "_label"
- "_lock_connectionsByPID"
- "_observerPIDs"
- "_pidToActiveUIResponderNodes"
- "_pidToActiveUIResponderTokens"
- "_resolutionsByPID"
- "_selectedNodeIdentities"
- "_stackIndexesHighlighted"
- "_supernode"
- "_target"
- "_tokenToNode"
- "_topLevel"
- "activeUIResponders"
- "bottom"
- "configureConnection:"
- "connectionDidBegin:process:"
- "connectionDidTerminate:process:"
- "containsIndex:"
- "dropline"
- "forceSelectDeferringTarget:forEnvironment:forClientWithPID:"
- "indent"
- "initWithDelegate:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:"
- "initWithDeliveryManager:ruleChangeAuthority:"
- "initWithIdentity:compatibilityDisplay:path:"
- "interrupted connection %{public}@"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "new"
- "no node for active UI responder token %{public}@ (yet?)"
- "numberWithInteger:"
- "path"
- "pid:%d remote target: %{public}@"
- "predicate != ((void *)0)"
- "remoteProcess"
- "removeLastObject"
- "selectDeferringPathForToken:%{public}@"
- "selectDeferringPredicate:forClientWithPID:"
- "selectDeferringTargetForPredicate:"
- "selected nodes now: %{public}@"
- "selection target not found: %{public}@"
- "senders != ((void *)0)"
- "setActiveUIResponderTokens:%{public}@ forPID:%d"
- "setActiveUIResponders:forClientWithPID:"
- "setDomain:"
- "setInterruptionHandler:"
- "setService:"
- "setServiceQuality:"
- "setTargetQueue:"
- "single"
- "top"
- "userInitiated"
- "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
- "v16@?0@\"<BSServiceConnectionListenerConfiguring>\"8"
- "v16@?0@\"BSServiceConnection\"8"
- "v32@0:8@\"BSServiceConnection\"16@\"BSProcessHandle\"24"
- "v32@?0@\"NSNumber\"8@\"NSOrderedSet\"16^B24"
- "v36@0:8@16@24i32"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24*32"
- "v40@0:8@16@24*32"
- "writePrefix:label:args:"

```
