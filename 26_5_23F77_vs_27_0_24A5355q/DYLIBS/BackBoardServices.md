## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

```diff

-735.5.1.0.0
-  __TEXT.__text: 0x85b48
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x7c04
-  __TEXT.__const: 0x44c
+860.0.1.0.0
+  __TEXT.__text: 0x87258
+  __TEXT.__objc_methlist: 0x88ac
+  __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0x18e
-  __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__cstring: 0xb0bf
-  __TEXT.__oslogstring: 0x20a9
+  __TEXT.__gcc_except_tab: 0x5d8
+  __TEXT.__cstring: 0xb6ad
+  __TEXT.__oslogstring: 0x260a
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x2000
-  __TEXT.__objc_classname: 0x1af9
-  __TEXT.__objc_methname: 0xd0f7
-  __TEXT.__objc_methtype: 0x1fd7
-  __TEXT.__objc_stubs: 0x6a80
-  __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x1770
-  __DATA_CONST.__objc_classlist: 0x570
-  __DATA_CONST.__objc_protolist: 0x168
+  __TEXT.__unwind_info: 0x2248
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x18f8
+  __DATA_CONST.__objc_classlist: 0x5c0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b20
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x2ef8
+  __DATA_CONST.__objc_protorefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH_CONST.__const: 0x1428
-  __AUTH_CONST.__cfstring: 0x9860
-  __AUTH_CONST.__objc_const: 0x10378
+  __DATA_CONST.__got: 0x7a8
+  __AUTH_CONST.__const: 0x15a8
+  __AUTH_CONST.__cfstring: 0xa0a0
+  __AUTH_CONST.__objc_const: 0x11a08
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x23a0
-  __DATA.__objc_ivar: 0x7bc
-  __DATA.__data: 0x10f0
-  __DATA.__bss: 0x548
-  __DATA_DIRTY.__objc_data: 0x12c0
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH.__objc_data: 0x2378
+  __DATA.__objc_ivar: 0x8cc
+  __DATA.__data: 0x14b0
+  __DATA.__bss: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x1608
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DFD2C823-08AC-3031-A182-19CCCAE6530D
-  Functions: 3127
-  Symbols:   9745
-  CStrings:  5719
+  UUID: 4EA9A99E-537F-38A9-806E-4C4E19D4FE70
+  Functions: 3377
+  Symbols:   10614
+  CStrings:  3208
 
Symbols:
+ +[BKSDisplayService sharedInstance]
+ +[BKSDisplayTraits _classesRequiredToDecode]
+ +[BKSDisplayTraits build:]
+ +[BKSDisplayTraits new]
+ +[BKSDisplayTraits protobufSchema]
+ +[BKSDisplayTraits supportsSecureCoding]
+ +[BKSHIDEventDeferringConstraint protobufSchema]
+ +[BKSHIDEventDeferringConstraintAssertion _withTimestamp:build:]
+ +[BKSHIDEventDeferringGrantAssertion build:]
+ +[BKSHIDEventDeferringGrantAssertion new]
+ +[BKSHIDEventDeferringGrantAssertion supportsSecureCoding]
+ +[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:priority:seed:pid:]
+ +[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:toTarget:withReason:priority:seed:pid:]
+ +[BKSHIDEventDeferringToken tokenForIdentifierOfCAContext:andCGSWindow:]
+ +[BKSHIDEventDeferringToken uniqueTokenWithLabel:]
+ +[BKSHIDEventSimpleProvenance supportsBSXPCSecureCoding]
+ +[BKSHIDEventUnitTestableProvenance supportsBSXPCSecureCoding]
+ +[BKSHIDUISensorCharacteristics supportsBSXPCSecureCoding]
+ +[BKSHIDUISensorMode supportsBSXPCSecureCoding]
+ +[BKSHIDUISensorService acquireTransactionForReason:]
+ +[BKSHIDUISensorService serviceForDisplayUUID:]
+ +[BKSHitTestTargetIdentifier supportsSecureCoding]
+ +[BKSSecureModeViolation supportsSecureCoding]
+ +[BKSTouchDeliveryBackgroundObserver supportsBSXPCSecureCoding]
+ +[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken protobufSchema]
+ +[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken supportsSecureCoding]
+ +[_BKSHIDUISensorOverseer sharedInstance]
+ +[_BKSHIDUniqueEventDeferringToken protobufSchema]
+ +[_BKSHIDUniqueEventDeferringToken supportsSecureCoding]
+ -[BKSBackgroundTouchDeliveryUpdate .cxx_destruct]
+ -[BKSBackgroundTouchDeliveryUpdate appendDescriptionToStream:]
+ -[BKSBackgroundTouchDeliveryUpdate copyWithZone:]
+ -[BKSBackgroundTouchDeliveryUpdate hash]
+ -[BKSBackgroundTouchDeliveryUpdate hostingContextsChain]
+ -[BKSBackgroundTouchDeliveryUpdate isEqual:]
+ -[BKSBackgroundTouchDeliveryUpdate pid]
+ -[BKSBackgroundTouchDeliveryUpdate setHostingContextsChain:]
+ -[BKSBackgroundTouchDeliveryUpdate setPid:]
+ -[BKSBackgroundTouchDeliveryUpdate setTargetID:]
+ -[BKSBackgroundTouchDeliveryUpdate setTimestamp:]
+ -[BKSBackgroundTouchDeliveryUpdate setTouchIdentifier:]
+ -[BKSBackgroundTouchDeliveryUpdate targetID]
+ -[BKSBackgroundTouchDeliveryUpdate timestamp]
+ -[BKSBackgroundTouchDeliveryUpdate touchIdentifier]
+ -[BKSDisplayService traitsForDisplayUUID:]
+ -[BKSDisplayTraits _initWithCopyOf:]
+ -[BKSDisplayTraits _init]
+ -[BKSDisplayTraits appendDescriptionToFormatter:]
+ -[BKSDisplayTraits copyWithZone:]
+ -[BKSDisplayTraits description]
+ -[BKSDisplayTraits encodeWithCoder:]
+ -[BKSDisplayTraits hash]
+ -[BKSDisplayTraits initForProtobufDecoding]
+ -[BKSDisplayTraits initWithCoder:]
+ -[BKSDisplayTraits init]
+ -[BKSDisplayTraits isEqual:]
+ -[BKSDisplayTraits mutableCopyWithZone:]
+ -[BKSDisplayTraits surfaceType]
+ -[BKSHIDEventAuthenticationMessage targetWindowID]
+ -[BKSHIDEventDeferringConstraint initForProtobufDecoding]
+ -[BKSHIDEventDeferringConstraintAssertion reason]
+ -[BKSHIDEventDeferringGrantAssertion .cxx_destruct]
+ -[BKSHIDEventDeferringGrantAssertion appendDescriptionToStream:]
+ -[BKSHIDEventDeferringGrantAssertion copyWithZone:]
+ -[BKSHIDEventDeferringGrantAssertion description]
+ -[BKSHIDEventDeferringGrantAssertion encodeWithCoder:]
+ -[BKSHIDEventDeferringGrantAssertion granteeTarget]
+ -[BKSHIDEventDeferringGrantAssertion grantorTarget]
+ -[BKSHIDEventDeferringGrantAssertion hash]
+ -[BKSHIDEventDeferringGrantAssertion initWithCoder:]
+ -[BKSHIDEventDeferringGrantAssertion init]
+ -[BKSHIDEventDeferringGrantAssertion isEqual:]
+ -[BKSHIDEventDeferringGrantAssertion pathIdentifier]
+ -[BKSHIDEventDeferringGrantAssertion reason]
+ -[BKSHIDEventDeferringGrantAssertion setGranteeTarget:]
+ -[BKSHIDEventDeferringGrantAssertion setGrantorTarget:]
+ -[BKSHIDEventDeferringGrantAssertion setPathIdentifier:]
+ -[BKSHIDEventDeferringGrantAssertion setReason:]
+ -[BKSHIDEventDeferringGrantAssertion timestamp]
+ -[BKSHIDEventDeferringRule _initWithPredicate:restrictedToEventDescriptors:target:reason:priority:identity:]
+ -[BKSHIDEventDeferringRule priority]
+ -[BKSHIDEventDeferringTarget initWithPID:token:]
+ -[BKSHIDEventDeferringTarget initWithToken:]
+ -[BKSHIDEventDeferringTarget mutableCopy]
+ -[BKSHIDEventDeferringToken _isIdentifierOfCAContextAndCGSWindow]
+ -[BKSHIDEventDeferringToken _isUnique]
+ -[BKSHIDEventDeferringToken _label]
+ -[BKSHIDEventDeferringToken appendDescriptionToStream:]
+ -[BKSHIDEventDeferringToken pithyDescription]
+ -[BKSHIDEventDeliveryChain constraints]
+ -[BKSHIDEventDeliveryChain finalStringTargetIndex]
+ -[BKSHIDEventDeliveryChain generation]
+ -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:containsSubset:containsEndOfChain:finalStringTargetIndex:generation:]
+ -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:generation:]
+ -[BKSHIDEventDeliveryManager assertSelectionPath:target:grantsSelectionToTarget:reason:]
+ -[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:reason:]
+ -[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:priority:restrictedToEventDescriptors:toTarget:withReason:]
+ -[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:priority:toTarget:withReason:]
+ -[BKSHIDEventDeliveryPolicy generation]
+ -[BKSHIDEventDeliveryRuleChangeTransaction grantAssertions]
+ -[BKSHIDEventDeliveryRuleChangeTransaction setGrantAssertions:]
+ -[BKSHIDEventObserver _lock_postObservingStateToServerIncludingNegative:]
+ -[BKSHIDEventObserver _lock_shouldObserveDeferringChanges]
+ -[BKSHIDEventObserver _observationsFromChains:]
+ -[BKSHIDEventObserver didUpdateDeferringChains:withReply:]
+ -[BKSHIDEventPolicyObservation generation]
+ -[BKSHIDEventSenderDescriptor _initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:inverted:]
+ -[BKSHIDEventSenderDescriptor invertedDescriptor]
+ -[BKSHIDEventSenderDescriptor isInverted]
+ -[BKSHIDEventSimpleProvenance encodeWithBSXPCCoder:]
+ -[BKSHIDEventSimpleProvenance encodeWithXPCDictionary:]
+ -[BKSHIDEventSimpleProvenance initWithBSXPCCoder:]
+ -[BKSHIDEventSimpleProvenance initWithXPCDictionary:]
+ -[BKSHIDEventUnitTestableProvenance encodeWithBSXPCCoder:]
+ -[BKSHIDEventUnitTestableProvenance encodeWithXPCDictionary:]
+ -[BKSHIDEventUnitTestableProvenance initWithBSXPCCoder:]
+ -[BKSHIDEventUnitTestableProvenance initWithXPCDictionary:]
+ -[BKSHIDKeyboardDevice _initWithProperties:service:]
+ -[BKSHIDKeyboardDevice _serverLayout]
+ -[BKSHIDTouchRoutingPolicy _initWithSettings:]
+ -[BKSHIDTouchRoutingPolicy copyWithZone:]
+ -[BKSHIDTouchRoutingPolicy hash]
+ -[BKSHIDTouchRoutingPolicy isEqual:]
+ -[BKSHIDTouchRoutingPolicy restrictHitTestToTheseContextIDs]
+ -[BKSHIDTouchRoutingPolicy restrictHitTestToTheseTargets]
+ -[BKSHIDTouchRoutingPolicy restrictedHitTestsAllowEmbeddedTargets]
+ -[BKSHIDTouchRoutingPolicy setRestrictHitTestToTheseContextIDs:]
+ -[BKSHIDTouchRoutingPolicy setRestrictHitTestToTheseTargets:]
+ -[BKSHIDTouchRoutingPolicy setRestrictedHitTestsAllowEmbeddedTargets:]
+ -[BKSHIDTouchRoutingPolicy setTargetsToAlwaysSendTouches:]
+ -[BKSHIDTouchRoutingPolicy setTargetsToExcludeFromHitTesting:]
+ -[BKSHIDTouchRoutingPolicy targetsToAlwaysSendTouches]
+ -[BKSHIDTouchRoutingPolicy targetsToExcludeFromHitTesting]
+ -[BKSHIDUISensorCharacteristics encodeWithBSXPCCoder:]
+ -[BKSHIDUISensorCharacteristics initWithBSXPCCoder:]
+ -[BKSHIDUISensorMode encodeWithBSXPCCoder:]
+ -[BKSHIDUISensorMode initWithBSXPCCoder:]
+ -[BKSHIDUISensorService acquireTransactionForReason:]
+ -[BKSHIDUISensorService recalibrateProximitySensor]
+ -[BKSHIDUISensorService requestEstimatedProximityEventWithTimeout:]
+ -[BKSHIDUISensorService requestProximityDetectionMode:]
+ -[BKSHIDUISensorService requestProximityStatusEventForReason:]
+ -[BKSHitTestTargetIdentifier _initWithContextID:]
+ -[BKSHitTestTargetIdentifier contextID]
+ -[BKSHitTestTargetIdentifier copyWithZone:]
+ -[BKSHitTestTargetIdentifier description]
+ -[BKSHitTestTargetIdentifier encodeWithCoder:]
+ -[BKSHitTestTargetIdentifier hash]
+ -[BKSHitTestTargetIdentifier initWithCoder:]
+ -[BKSHitTestTargetIdentifier initWithContextID:]
+ -[BKSHitTestTargetIdentifier isEqual:]
+ -[BKSMousePointerService setDesignatedMainDisplayUUID:]
+ -[BKSMutableDisplayTraits copyWithZone:]
+ -[BKSMutableDisplayTraits setSurfaceType:]
+ -[BKSMutableHIDEventAuthenticationMessage setTargetWindowID:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setReason:]
+ -[BKSMutableHIDEventPolicyObservation setGeneration:]
+ -[BKSMutableHIDEventSenderDescriptor setInverted:]
+ -[BKSMutableTouchHitTestFilterParameters setHitTestStimulus:]
+ -[BKSSecureModeViolation displayUUID]
+ -[BKSSecureModeViolation encodeWithCoder:]
+ -[BKSSecureModeViolation hash]
+ -[BKSSecureModeViolation initWithCoder:]
+ -[BKSSecureModeViolation isEqual:]
+ -[BKSSecureModeViolation setDisplayUUID:]
+ -[BKSSecureRenderingService .cxx_destruct]
+ -[BKSSecureRenderingService _server]
+ -[BKSSecureRenderingService activateSecureRenderingControlForDisplayUUID:]
+ -[BKSSecureRenderingService delegate]
+ -[BKSSecureRenderingService init]
+ -[BKSSecureRenderingService isSecureRenderingEnabledForDisplayUUID:]
+ -[BKSSecureRenderingService secureRenderingViolationsOccurred:]
+ -[BKSSecureRenderingService setDelegate:]
+ -[BKSSecureRenderingService setSecureRenderingEnabled:forDisplayUUID:]
+ -[BKSTouchDeliveryBackgroundObserver .cxx_destruct]
+ -[BKSTouchDeliveryBackgroundObserver contexts]
+ -[BKSTouchDeliveryBackgroundObserver description]
+ -[BKSTouchDeliveryBackgroundObserver encodeWithBSXPCCoder:]
+ -[BKSTouchDeliveryBackgroundObserver initWithBSXPCCoder:]
+ -[BKSTouchDeliveryBackgroundObserver setContexts:]
+ -[BKSTouchDeliveryBackgroundObserver setTimestamp:]
+ -[BKSTouchDeliveryBackgroundObserver setToken:]
+ -[BKSTouchDeliveryBackgroundObserver timestamp]
+ -[BKSTouchDeliveryBackgroundObserver token]
+ -[BKSTouchDeliveryObservationService _configureConnection]
+ -[BKSTouchDeliveryObservationService _connectionForTouchDeliveryService]
+ -[BKSTouchDeliveryObservationService _queue_handlePendingObservers:]
+ -[BKSTouchDeliveryObservationService initWithConnection:]
+ -[BKSTouchDeliveryUpdate hash]
+ -[BKSTouchDeliveryUpdate setTargetID:]
+ -[BKSTouchDeliveryUpdate targetID]
+ -[BKSTouchDetachment .cxx_destruct]
+ -[BKSTouchDetachment addTouchIdentifiers:]
+ -[BKSTouchDetachment appendDescriptionToFormatter:]
+ -[BKSTouchDetachment description]
+ -[BKSTouchDetachment routingPolicy]
+ -[BKSTouchDetachment setRoutingPolicy:]
+ -[BKSTouchDetachment setTouchOffset:]
+ -[BKSTouchDetachment touchIdentifiers]
+ -[BKSTouchDetachment touchOffset]
+ -[BKSTouchDetachment userIdentifier]
+ -[BKSTouchEventService _initConnectionWithConnectionFactory:]
+ -[BKSTouchEventService _initWithConnectionFactory:]
+ -[BKSTouchEventService _lock_flushStateToServer]
+ -[BKSTouchEventService _lock_repostAllRegistrations]
+ -[BKSTouchEventService _lock_updateServerHitTestCategoryContextIDs]
+ -[BKSTouchEventService _lock_updateServerHitTestFilterParameters]
+ -[BKSTouchEventService _updateTouchDetachmentOffset:userIdentifier:]
+ -[BKSTouchEventService _updateTouchDetachmentRoutingPolicy:userIdentifier:]
+ -[BKSTouchEventService detachTouchIdentifiers:userIdentifier:]
+ -[BKSTouchEventService detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:]
+ -[BKSTouchEventService detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:initialTouchOffset:]
+ -[BKSTouchEventService excludeEventsFromStimulus:fromHitTestingToContextIDs:]
+ -[BKSTouchHitTestFilterParameters hitTestStimulus]
+ -[BKSTouchStream .cxx_destruct]
+ -[BKSTouchStream _configureServerConnectionWithFactory:]
+ -[BKSTouchStream _lock_flushInitialStateToServer]
+ -[BKSTouchStream initWithContextID:displayUUID:identifier:policy:connectionFactory:]
+ -[_BKSCloneMirroringModeRequest destinationDisplayUUID]
+ -[_BKSCloneMirroringModeRequest setDestinationDisplayUUID:]
+ -[_BKSCloneMirroringModeRequest setSourceDisplayUUID:]
+ -[_BKSCloneMirroringModeRequest sourceDisplayUUID]
+ -[_BKSHIDCAContextEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken _identifierOfCAContext]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken _identifierOfCGSWindow]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken _initWithCAContextID:andCGSWindowID:]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken _isIdentifierOfCAContextAndCGSWindow]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken description]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken encodeWithCoder:]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken hash]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken initForProtobufDecoding]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken initWithCoder:]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken init]
+ -[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken isEqual:]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDStringIdentifierEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDStringIdentifierEventDeferringToken pithyDescription]
+ -[_BKSHIDUISensorDisplayAssociatedService .cxx_destruct]
+ -[_BKSHIDUISensorDisplayAssociatedService _lock_reevaluateExistence]
+ -[_BKSHIDUISensorDisplayAssociatedService acquireTransactionForReason:]
+ -[_BKSHIDUISensorDisplayAssociatedService appendDescriptionToStream:]
+ -[_BKSHIDUISensorDisplayAssociatedService dealloc]
+ -[_BKSHIDUISensorDisplayAssociatedService proximityDidUnoccludeAfterWake]
+ -[_BKSHIDUISensorDisplayAssociatedService recalibrateProximitySensor]
+ -[_BKSHIDUISensorDisplayAssociatedService requestEstimatedProximityEventWithTimeout:]
+ -[_BKSHIDUISensorDisplayAssociatedService requestProximityDetectionMode:]
+ -[_BKSHIDUISensorDisplayAssociatedService requestProximityStatusEventForReason:]
+ -[_BKSHIDUISensorDisplayAssociatedService requestUISensorMode:]
+ -[_BKSHIDUISensorDisplayAssociatedService sensorCharacteristics]
+ -[_BKSHIDUISensorDisplayAssociatedService suppressUISensorChangesForReason:]
+ -[_BKSHIDUISensorOverseer .cxx_destruct]
+ -[_BKSHIDUISensorOverseer _dataLock_prevailingModeDidChange:forDisplayUUID:]
+ -[_BKSHIDUISensorOverseer _dataLock_pushModesToServer]
+ -[_BKSHIDUISensorOverseer _server]
+ -[_BKSHIDUISensorOverseer _systemShellDidReconnect]
+ -[_BKSHIDUISensorOverseer acquireTransactionForReason:]
+ -[_BKSHIDUISensorOverseer initWithServiceConnection:]
+ -[_BKSHIDUISensorOverseer init]
+ -[_BKSHIDUISensorServiceReference .cxx_destruct]
+ -[_BKSHIDUISensorServiceReference acquireTransactionForReason:]
+ -[_BKSHIDUISensorServiceReference dealloc]
+ -[_BKSHIDUISensorServiceReference proximityDidUnoccludeAfterWake]
+ -[_BKSHIDUISensorServiceReference recalibrateProximitySensor]
+ -[_BKSHIDUISensorServiceReference requestEstimatedProximityEventWithTimeout:]
+ -[_BKSHIDUISensorServiceReference requestProximityDetectionMode:]
+ -[_BKSHIDUISensorServiceReference requestProximityStatusEventForReason:]
+ -[_BKSHIDUISensorServiceReference requestUISensorMode:]
+ -[_BKSHIDUISensorServiceReference sensorCharacteristics]
+ -[_BKSHIDUISensorServiceReference suppressUISensorChangesForReason:]
+ -[_BKSHIDUniqueEventDeferringToken .cxx_destruct]
+ -[_BKSHIDUniqueEventDeferringToken _initWithLabel:]
+ -[_BKSHIDUniqueEventDeferringToken _isUnique]
+ -[_BKSHIDUniqueEventDeferringToken _label]
+ -[_BKSHIDUniqueEventDeferringToken appendDescriptionToStream:]
+ -[_BKSHIDUniqueEventDeferringToken description]
+ -[_BKSHIDUniqueEventDeferringToken encodeWithCoder:]
+ -[_BKSHIDUniqueEventDeferringToken hash]
+ -[_BKSHIDUniqueEventDeferringToken initForProtobufDecoding]
+ -[_BKSHIDUniqueEventDeferringToken initWithCoder:]
+ -[_BKSHIDUniqueEventDeferringToken init]
+ -[_BKSHIDUniqueEventDeferringToken isEqual:]
+ GCC_except_table118
+ GCC_except_table1181
+ GCC_except_table1192
+ GCC_except_table1194
+ GCC_except_table1195
+ GCC_except_table1311
+ GCC_except_table1335
+ GCC_except_table1358
+ GCC_except_table1532
+ GCC_except_table1537
+ GCC_except_table1547
+ GCC_except_table1685
+ GCC_except_table1794
+ GCC_except_table1927
+ GCC_except_table2055
+ GCC_except_table2064
+ GCC_except_table2193
+ GCC_except_table2305
+ GCC_except_table2307
+ GCC_except_table2348
+ GCC_except_table2552
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table2727
+ GCC_except_table2734
+ GCC_except_table3046
+ GCC_except_table3072
+ GCC_except_table3234
+ GCC_except_table3268
+ GCC_except_table3269
+ OBJC_IVAR_$_BKSHIDEventAuthenticationMessage._targetWindowID
+ OBJC_IVAR_$_BKSHIDEventSenderDescriptor._inverted
+ _BKLogSecureRendering
+ _BKLogSecureRendering.__logObj
+ _BKLogSecureRendering.onceToken
+ _BKLogTouchStream
+ _BKLogTouchStream.__logObj
+ _BKLogTouchStream.onceToken
+ _BKSDisplayServicesGetDisplayTraits
+ _BKSDisplayServicesSetCloneMirroringModeForSourceDisplayToDestinationDisplay
+ _BKSDisplayServicesSetCloneMirroringModeForSourceDisplayToDestinationDisplay.destinationDisplayToModeCache
+ _BKSDisplayServicesSetMirroringOnlyDisplayCloningSource
+ _BKSHIDEventClientConnectionBundleIdentifierKey
+ _BKSHIDEventClientConnectionLastPathComponentKey
+ _BKSHIDEventClientConnectionPidKey
+ _BKSHIDEventDeferringPithyDescription
+ _BKSHIDEventRegisterEventCallbackOnQueue
+ _BKSHIDEventServiceKeyRouteEventsIgnoringSystemShellPolicy
+ _BKSHIDServicesSetDisplayInterfaceOrientation
+ _BKSHIDTouchStreamBSServiceName
+ _BKSHIDUISensorServiceName
+ _BKSSecureRenderingServiceName
+ _BSEqualDictionaries
+ _BSExecutablePathForPID
+ _IOHIDEventSystemClientScheduleWithDispatchQueue
+ _NSRequestConcreteImplementation
+ _NSStringFromBKSHIDEventDeferringRulePriority
+ _NSStringFromBKSHitTestStimulus
+ _OBJC_CLASS_$_BKSBackgroundTouchDeliveryUpdate
+ _OBJC_CLASS_$_BKSDisplayService
+ _OBJC_CLASS_$_BKSDisplayTraits
+ _OBJC_CLASS_$_BKSHIDEventDeferringGrantAssertion
+ _OBJC_CLASS_$_BKSHitTestTargetIdentifier
+ _OBJC_CLASS_$_BKSMutableDisplayTraits
+ _OBJC_CLASS_$_BKSSecureRenderingService
+ _OBJC_CLASS_$_BKSTouchDeliveryBackgroundObserver
+ _OBJC_CLASS_$_BKSTouchDetachment
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ _OBJC_CLASS_$__BKSHIDUISensorDisplayAssociatedService
+ _OBJC_CLASS_$__BKSHIDUISensorOverseer
+ _OBJC_CLASS_$__BKSHIDUISensorServiceReference
+ _OBJC_CLASS_$__BKSHIDUniqueEventDeferringToken
+ _OBJC_IVAR_$_BKSBackgroundTouchDeliveryUpdate._hostingContextsChain
+ _OBJC_IVAR_$_BKSBackgroundTouchDeliveryUpdate._pid
+ _OBJC_IVAR_$_BKSBackgroundTouchDeliveryUpdate._targetID
+ _OBJC_IVAR_$_BKSBackgroundTouchDeliveryUpdate._timestamp
+ _OBJC_IVAR_$_BKSBackgroundTouchDeliveryUpdate._touchIdentifier
+ _OBJC_IVAR_$_BKSDisplayTraits._surfaceType
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._reason
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._granteeTarget
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._grantorTarget
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._immutable
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._pathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._reason
+ _OBJC_IVAR_$_BKSHIDEventDeferringGrantAssertion._timestamp
+ _OBJC_IVAR_$_BKSHIDEventDeferringRule._priority
+ _OBJC_IVAR_$_BKSHIDEventDeferringRule._sortPriority
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._constraints
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._finalStringTargetIndex
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._generation
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_grantAssertSeed
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_grantAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_lastSentGrantAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicy._generation
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicyObserver._lock_debugLabel
+ _OBJC_IVAR_$_BKSHIDEventDeliveryRuleChangeTransaction._grantAssertions
+ _OBJC_IVAR_$_BKSHIDEventObserver._lock_observerToLastSeenDeferringObservations
+ _OBJC_IVAR_$_BKSHIDEventPolicyObservation._generation
+ _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._timestamp
+ _OBJC_IVAR_$_BKSHIDKeyboardDevice._senderID
+ _OBJC_IVAR_$_BKSHIDKeyboardDevice._service
+ _OBJC_IVAR_$_BKSHIDKeyboardService._lock_pendingLayoutUpdatesBySenderID
+ _OBJC_IVAR_$_BKSHitTestTargetIdentifier._contextID
+ _OBJC_IVAR_$_BKSSecureModeViolation._displayUUID
+ _OBJC_IVAR_$_BKSSecureRenderingService._connection
+ _OBJC_IVAR_$_BKSSecureRenderingService._delegate
+ _OBJC_IVAR_$_BKSSecureRenderingService._delegateQueue
+ _OBJC_IVAR_$_BKSSecureRenderingService._lock
+ _OBJC_IVAR_$_BKSSecureRenderingService._lock_registeredDisplayUUIDs
+ _OBJC_IVAR_$_BKSTouchDeliveryBackgroundObserver._contexts
+ _OBJC_IVAR_$_BKSTouchDeliveryBackgroundObserver._timestamp
+ _OBJC_IVAR_$_BKSTouchDeliveryBackgroundObserver._token
+ _OBJC_IVAR_$_BKSTouchDeliveryObservationService._remoteTarget
+ _OBJC_IVAR_$_BKSTouchDeliveryUpdate._targetID
+ _OBJC_IVAR_$_BKSTouchDetachment._mutableTouchIdentifiers
+ _OBJC_IVAR_$_BKSTouchDetachment._routingPolicy
+ _OBJC_IVAR_$_BKSTouchDetachment._service
+ _OBJC_IVAR_$_BKSTouchDetachment._touchOffset
+ _OBJC_IVAR_$_BKSTouchDetachment._userIdentifier
+ _OBJC_IVAR_$_BKSTouchEventService._isNonLaunchingServer
+ _OBJC_IVAR_$_BKSTouchEventService._lock
+ _OBJC_IVAR_$_BKSTouchEventService._lock_registrationsByContextID
+ _OBJC_IVAR_$_BKSTouchEventService._lock_waitingOnServerHandshake
+ _OBJC_IVAR_$_BKSTouchHitTestFilterParameters._hitTestStimulus
+ _OBJC_IVAR_$_BKSTouchStream._connection
+ _OBJC_IVAR_$_BKSTouchStream._contextID
+ _OBJC_IVAR_$_BKSTouchStream._displayUUID
+ _OBJC_IVAR_$_BKSTouchStream._identifier
+ _OBJC_IVAR_$_BKSTouchStream._invalidSignal
+ _OBJC_IVAR_$_BKSTouchStream._lock
+ _OBJC_IVAR_$_BKSTouchStream._lock_pendingAmbiguityRecommendation
+ _OBJC_IVAR_$_BKSTouchStream._lock_pendingEventDispatchMode
+ _OBJC_IVAR_$_BKSTouchStream._lock_pendingLastTouchTimestamp
+ _OBJC_IVAR_$_BKSTouchStream._lock_waitingOnServerHandshake
+ _OBJC_IVAR_$_BKSTouchStream._shouldSendAmbiguityRecommendations
+ _OBJC_IVAR_$__BKSCloneMirroringModeRequest._destinationDisplayUUID
+ _OBJC_IVAR_$__BKSCloneMirroringModeRequest._sourceDisplayUUID
+ _OBJC_IVAR_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken._CAContextID
+ _OBJC_IVAR_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken._CGSWindowID
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._displayUUID
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._lock
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._lock_characteristics
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._lock_externalReferenceCount
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._lock_prevailingMode
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._modeAssertion
+ _OBJC_IVAR_$__BKSHIDUISensorDisplayAssociatedService._overseer
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._connectionLock
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._connectionLock_connection
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._dataLock
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._dataLock_currentDisplayUUIDToSensorModes
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._dataLock_displayUUIDToSensorService
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._dataLock_sentDisplayUUIDToSensorModes
+ _OBJC_IVAR_$__BKSHIDUISensorOverseer._transactionAssertion
+ _OBJC_IVAR_$__BKSHIDUISensorServiceReference._service
+ _OBJC_IVAR_$__BKSHIDUniqueEventDeferringToken._label
+ _OBJC_IVAR_$__BKSHIDUniqueEventDeferringToken._uniqueValue
+ _OBJC_METACLASS_$_BKSBackgroundTouchDeliveryUpdate
+ _OBJC_METACLASS_$_BKSDisplayService
+ _OBJC_METACLASS_$_BKSDisplayTraits
+ _OBJC_METACLASS_$_BKSHIDEventDeferringGrantAssertion
+ _OBJC_METACLASS_$_BKSHitTestTargetIdentifier
+ _OBJC_METACLASS_$_BKSMutableDisplayTraits
+ _OBJC_METACLASS_$_BKSSecureRenderingService
+ _OBJC_METACLASS_$_BKSTouchDeliveryBackgroundObserver
+ _OBJC_METACLASS_$_BKSTouchDetachment
+ _OBJC_METACLASS_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ _OBJC_METACLASS_$__BKSHIDUISensorDisplayAssociatedService
+ _OBJC_METACLASS_$__BKSHIDUISensorOverseer
+ _OBJC_METACLASS_$__BKSHIDUISensorServiceReference
+ _OBJC_METACLASS_$__BKSHIDUniqueEventDeferringToken
+ _QuartzCoreLibrary.12780
+ _QuartzCoreLibraryCore.frameworkLibrary.12800
+ _QuartzCoreLibraryCore.frameworkLibrary.8807
+ _QuartzCoreLibraryCore.frameworkLibrary.9621
+ __BKSContextIDsFromTargetIdentifiers
+ __BKSDisplayGetDisplayTraits
+ __BKSDisplayRemoveCloneMirroringModeForSourceDisplayToDestinationDisplay
+ __BKSDisplaySetCloneMirroringModeForSourceDisplayToDestinationDisplay
+ __BKSDisplaySetMirroringOnlyDisplayCloningSource
+ __BKSHIDEventDeferringTargetClassIsCompatible
+ __BKSHIDSetDisplayInterfaceOrientation
+ __BKSHitTestTargetIdentifiersFromContextIDs
+ __BKSVerifyIsArrayOfTargetIdentifiers
+ __OBJC_$_CLASS_METHODS_BKSDisplayService
+ __OBJC_$_CLASS_METHODS_BKSDisplayTraits
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringGrantAssertion
+ __OBJC_$_CLASS_METHODS_BKSHitTestTargetIdentifier
+ __OBJC_$_CLASS_METHODS_BKSSecureModeViolation
+ __OBJC_$_CLASS_METHODS_BKSTouchDeliveryBackgroundObserver
+ __OBJC_$_CLASS_METHODS__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ __OBJC_$_CLASS_METHODS__BKSHIDUniqueEventDeferringToken
+ __OBJC_$_CLASS_PROP_LIST_BKSDisplayTraits
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringGrantAssertion
+ __OBJC_$_CLASS_PROP_LIST_BKSHitTestTargetIdentifier
+ __OBJC_$_CLASS_PROP_LIST_BKSSecureModeViolation
+ __OBJC_$_INSTANCE_METHODS_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_$_INSTANCE_METHODS_BKSDisplayService
+ __OBJC_$_INSTANCE_METHODS_BKSDisplayTraits
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringGrantAssertion
+ __OBJC_$_INSTANCE_METHODS_BKSHitTestTargetIdentifier
+ __OBJC_$_INSTANCE_METHODS_BKSMutableDisplayTraits
+ __OBJC_$_INSTANCE_METHODS_BKSSecureRenderingService
+ __OBJC_$_INSTANCE_METHODS_BKSTouchDeliveryBackgroundObserver
+ __OBJC_$_INSTANCE_METHODS_BKSTouchDetachment
+ __OBJC_$_INSTANCE_METHODS__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ __OBJC_$_INSTANCE_METHODS__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_$_INSTANCE_METHODS__BKSHIDUISensorOverseer
+ __OBJC_$_INSTANCE_METHODS__BKSHIDUISensorServiceReference
+ __OBJC_$_INSTANCE_METHODS__BKSHIDUniqueEventDeferringToken
+ __OBJC_$_INSTANCE_VARIABLES_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_$_INSTANCE_VARIABLES_BKSDisplayTraits
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringGrantAssertion
+ __OBJC_$_INSTANCE_VARIABLES_BKSHitTestTargetIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_BKSSecureRenderingService
+ __OBJC_$_INSTANCE_VARIABLES_BKSTouchDeliveryBackgroundObserver
+ __OBJC_$_INSTANCE_VARIABLES_BKSTouchDetachment
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDUISensorOverseer
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDUISensorServiceReference
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDUniqueEventDeferringToken
+ __OBJC_$_PROP_LIST_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_$_PROP_LIST_BKSDisplayTraits
+ __OBJC_$_PROP_LIST_BKSDisplayTraitsProviding
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringGrantAssertion
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_$_PROP_LIST_BKSHIDUISensorSystemShellServicing
+ __OBJC_$_PROP_LIST_BKSHitTestTargetIdentifier
+ __OBJC_$_PROP_LIST_BKSMutableDisplayTraits
+ __OBJC_$_PROP_LIST_BKSSecureRenderingService
+ __OBJC_$_PROP_LIST_BKSTouchDeliveryBackgroundObserver
+ __OBJC_$_PROP_LIST_BKSTouchDetachment
+ __OBJC_$_PROP_LIST__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_$_PROP_LIST__BKSHIDUISensorServiceReference
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSDisplayTraitsProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDTouchStreamServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDUISensorInternalServicing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDUISensorServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDUISensorServicing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDUISensorSystemShellServicing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSSecureRenderingClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSSecureRenderingServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSDisplayTraitsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDTouchStreamServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDUISensorInternalServicing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDUISensorServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDUISensorServicing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDUISensorSystemShellServicing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSSecureRenderingClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSSecureRenderingServerInterface
+ __OBJC_$_PROTOCOL_REFS_BKSDisplayTraitsProviding
+ __OBJC_$_PROTOCOL_REFS_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_$_PROTOCOL_REFS_BKSHIDTouchStreamServerInterface
+ __OBJC_$_PROTOCOL_REFS_BKSHIDUISensorClientInterface
+ __OBJC_$_PROTOCOL_REFS_BKSHIDUISensorInternalServicing
+ __OBJC_$_PROTOCOL_REFS_BKSHIDUISensorServerInterface
+ __OBJC_$_PROTOCOL_REFS_BKSHIDUISensorServicing
+ __OBJC_$_PROTOCOL_REFS_BKSHIDUISensorSystemShellServicing
+ __OBJC_$_PROTOCOL_REFS_BKSSecureRenderingClientInterface
+ __OBJC_$_PROTOCOL_REFS_BKSSecureRenderingServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_CLASS_PROTOCOLS_$_BKSDisplayTraits
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringGrantAssertion
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDUISensorService
+ __OBJC_CLASS_PROTOCOLS_$_BKSHitTestTargetIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_BKSSecureRenderingService
+ __OBJC_CLASS_PROTOCOLS_$_BKSTouchDeliveryBackgroundObserver
+ __OBJC_CLASS_PROTOCOLS_$_BKSTouchDetachment
+ __OBJC_CLASS_PROTOCOLS_$__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_CLASS_PROTOCOLS_$__BKSHIDUISensorServiceReference
+ __OBJC_CLASS_RO_$_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_CLASS_RO_$_BKSDisplayService
+ __OBJC_CLASS_RO_$_BKSDisplayTraits
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringGrantAssertion
+ __OBJC_CLASS_RO_$_BKSHitTestTargetIdentifier
+ __OBJC_CLASS_RO_$_BKSMutableDisplayTraits
+ __OBJC_CLASS_RO_$_BKSSecureRenderingService
+ __OBJC_CLASS_RO_$_BKSTouchDeliveryBackgroundObserver
+ __OBJC_CLASS_RO_$_BKSTouchDetachment
+ __OBJC_CLASS_RO_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ __OBJC_CLASS_RO_$__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_CLASS_RO_$__BKSHIDUISensorOverseer
+ __OBJC_CLASS_RO_$__BKSHIDUISensorServiceReference
+ __OBJC_CLASS_RO_$__BKSHIDUniqueEventDeferringToken
+ __OBJC_LABEL_PROTOCOL_$_BKSDisplayTraitsProviding
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDTouchStreamServerInterface
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDUISensorClientInterface
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDUISensorInternalServicing
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDUISensorServerInterface
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDUISensorServicing
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDUISensorSystemShellServicing
+ __OBJC_LABEL_PROTOCOL_$_BKSSecureRenderingClientInterface
+ __OBJC_LABEL_PROTOCOL_$_BKSSecureRenderingServerInterface
+ __OBJC_METACLASS_RO_$_BKSBackgroundTouchDeliveryUpdate
+ __OBJC_METACLASS_RO_$_BKSDisplayService
+ __OBJC_METACLASS_RO_$_BKSDisplayTraits
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringGrantAssertion
+ __OBJC_METACLASS_RO_$_BKSHitTestTargetIdentifier
+ __OBJC_METACLASS_RO_$_BKSMutableDisplayTraits
+ __OBJC_METACLASS_RO_$_BKSSecureRenderingService
+ __OBJC_METACLASS_RO_$_BKSTouchDeliveryBackgroundObserver
+ __OBJC_METACLASS_RO_$_BKSTouchDetachment
+ __OBJC_METACLASS_RO_$__BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken
+ __OBJC_METACLASS_RO_$__BKSHIDUISensorDisplayAssociatedService
+ __OBJC_METACLASS_RO_$__BKSHIDUISensorOverseer
+ __OBJC_METACLASS_RO_$__BKSHIDUISensorServiceReference
+ __OBJC_METACLASS_RO_$__BKSHIDUniqueEventDeferringToken
+ __OBJC_PROTOCOL_$_BKSDisplayTraitsProviding
+ __OBJC_PROTOCOL_$_BKSHIDEventDeferringGrantAssertionBuilder
+ __OBJC_PROTOCOL_$_BKSHIDTouchStreamServerInterface
+ __OBJC_PROTOCOL_$_BKSHIDUISensorClientInterface
+ __OBJC_PROTOCOL_$_BKSHIDUISensorInternalServicing
+ __OBJC_PROTOCOL_$_BKSHIDUISensorServerInterface
+ __OBJC_PROTOCOL_$_BKSHIDUISensorServicing
+ __OBJC_PROTOCOL_$_BKSHIDUISensorSystemShellServicing
+ __OBJC_PROTOCOL_$_BKSSecureRenderingClientInterface
+ __OBJC_PROTOCOL_$_BKSSecureRenderingServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BKSHIDTouchStreamServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BKSHIDUISensorClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BKSHIDUISensorServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BKSSecureRenderingClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BKSSecureRenderingServerInterface
+ ___117-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:priority:restrictedToEventDescriptors:toTarget:withReason:]_block_invoke
+ ___34+[BKSDisplayTraits protobufSchema]_block_invoke
+ ___35+[BKSDisplayService sharedInstance]_block_invoke
+ ___41+[_BKSHIDUISensorOverseer sharedInstance]_block_invoke
+ ___47-[BKSHIDEventObserver _observationsFromChains:]_block_invoke
+ ___48+[BKSHIDEventDeferringConstraint protobufSchema]_block_invoke
+ ___50+[_BKSHIDUniqueEventDeferringToken protobufSchema]_block_invoke
+ ___50+[_BKSHIDUniqueEventDeferringToken protobufSchema]_block_invoke_2
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.101
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.102
+ ___50-[_BKSHIDUISensorDisplayAssociatedService dealloc]_block_invoke
+ ___51-[BKSTouchDetachment appendDescriptionToFormatter:]_block_invoke
+ ___51-[BKSTouchEventService _initWithConnectionFactory:]_block_invoke
+ ___51-[BKSTouchEventService _initWithConnectionFactory:]_block_invoke_2
+ ___52-[BKSMousePointerService _activateServerConnection:]_block_invoke.139
+ ___52-[BKSTouchEventService _lock_repostAllRegistrations]_block_invoke
+ ___52-[BKSTouchEventService _lock_repostAllRegistrations]_block_invoke_2
+ ___53-[_BKSHIDUISensorOverseer initWithServiceConnection:]_block_invoke
+ ___54-[BKSSecureRenderingService _activateServerConnection]_block_invoke
+ ___54-[BKSSecureRenderingService _activateServerConnection]_block_invoke.62
+ ___54-[BKSSecureRenderingService _activateServerConnection]_block_invoke.7
+ ___54-[BKSSecureRenderingService _activateServerConnection]_block_invoke_2
+ ___56-[BKSTouchStream _configureServerConnectionWithFactory:]_block_invoke
+ ___56-[BKSTouchStream _configureServerConnectionWithFactory:]_block_invoke.53
+ ___56-[BKSTouchStream _configureServerConnectionWithFactory:]_block_invoke_2
+ ___57-[BKSSystemShellService _checkInWaitingForDataMigration:]_block_invoke.102
+ ___58-[BKSHIDEventObserver didUpdateDeferringChains:withReply:]_block_invoke
+ ___58-[BKSHIDEventObserver didUpdateDeferringChains:withReply:]_block_invoke_2
+ ___58-[BKSTouchDeliveryObservationService _configureConnection]_block_invoke
+ ___58-[BKSTouchDeliveryObservationService _configureConnection]_block_invoke.119
+ ___58-[BKSTouchDeliveryObservationService _configureConnection]_block_invoke.120
+ ___58-[BKSTouchDeliveryObservationService _configureConnection]_block_invoke.124
+ ___58-[BKSTouchDeliveryObservationService _configureConnection]_block_invoke_2
+ ___61-[BKSTouchEventService _initConnectionWithConnectionFactory:]_block_invoke
+ ___61-[BKSTouchEventService _initConnectionWithConnectionFactory:]_block_invoke.287
+ ___61-[BKSTouchEventService _initConnectionWithConnectionFactory:]_block_invoke.289
+ ___61-[BKSTouchEventService _initConnectionWithConnectionFactory:]_block_invoke.291
+ ___62-[BKSBackgroundTouchDeliveryUpdate appendDescriptionToStream:]_block_invoke
+ ___62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.149
+ ___62-[_BKSHIDStringIdentifierEventDeferringToken pithyDescription]_block_invoke
+ ___62-[_BKSHIDUniqueEventDeferringToken appendDescriptionToStream:]_block_invoke
+ ___63-[BKSEventDeferringChainIdentity appendDescriptionToFormatter:]_block_invoke
+ ___64-[BKSHIDEventDeferringGrantAssertion appendDescriptionToStream:]_block_invoke
+ ___64-[BKSHIDEventDeliveryPolicyObserver deferringResolutionsChanged]_block_invoke.101
+ ___65-[BKSHIDEventDeferringSelectionTarget appendDescriptionToStream:]_block_invoke
+ ___65-[BKSMutableHIDEventKeyCommandsDispatchingPredicate setDisplays:]_block_invoke.122
+ ___68-[BKSTouchDeliveryObservationService _queue_handlePendingObservers:]_block_invoke
+ ___69+[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken protobufSchema]_block_invoke
+ ___69+[_BKSHIDCAContextIDAndCGSWindowIDEventDeferringToken protobufSchema]_block_invoke_2
+ ___69-[BKSHIDEventDeferringConstraintAssertion appendDescriptionToStream:]_block_invoke
+ ___69-[_BKSHIDUISensorDisplayAssociatedService appendDescriptionToStream:]_block_invoke
+ ___71-[BKSTouchDeliveryObservationService _processTouchEventDeliveryUpdate:]_block_invoke.128
+ ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.114
+ ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.124
+ ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.125
+ ___73-[_BKSHIDUISensorDisplayAssociatedService _initWithDisplayUUID:overseer:]_block_invoke
+ ___73-[_BKSHIDUISensorDisplayAssociatedService requestProximityDetectionMode:]_block_invoke
+ ___73-[_BKSHIDUISensorOverseer _connectionLock_connectToRemoteServiceIfNeeded]_block_invoke
+ ___73-[_BKSHIDUISensorOverseer _connectionLock_connectToRemoteServiceIfNeeded]_block_invoke.73
+ ___73-[_BKSHIDUISensorOverseer _connectionLock_connectToRemoteServiceIfNeeded]_block_invoke.77
+ ___77-[BKSTouchEventService excludeEventsFromStimulus:fromHitTestingToContextIDs:]_block_invoke
+ ___82-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:reason:]_block_invoke
+ ___82-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:reason:]_block_invoke_2
+ ___88-[BKSHIDEventDeliveryManager assertSelectionPath:target:grantsSelectionToTarget:reason:]_block_invoke
+ ___88-[BKSHIDEventDeliveryManager assertSelectionPath:target:grantsSelectionToTarget:reason:]_block_invoke_2
+ ___BKLogSecureRendering_block_invoke
+ ___BKLogTouchStream_block_invoke
+ ___BKSDisplayServicesAcquireDisplayDisabledAssertion_block_invoke.62
+ ___BKSDisplayServicesArchiveWithOptionsAndCompletion_block_invoke.152
+ ___BKSDisplayServicesSetCloneMirroringModeForSourceDisplayToDestinationDisplay_block_invoke
+ ___Block_byref_object_copy_.10672
+ ___Block_byref_object_copy_.5601
+ ___Block_byref_object_dispose_.10673
+ ___Block_byref_object_dispose_.5602
+ ___QuartzCoreLibraryCore_block_invoke.12801
+ ___QuartzCoreLibraryCore_block_invoke.8808
+ ___QuartzCoreLibraryCore_block_invoke.9622
+ ___block_descriptor_109_e8_32s40s48s56s64r_e45_v16?0"BKSMutableHIDEventPolicyObservation"8ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_32_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8l
+ ___block_descriptor_32_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_44_e8_32r_e36_B16?0"BKSHIDEventDeferringTarget"8lr32l8
+ ___block_descriptor_48_e8_32s40s_e43_v16?0"BKSHIDEventDeliveryPolicyObserver"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e27_v16?0"BSSimpleAssertion"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e29_v16?0"BSServiceConnection"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e48_v16?0"BKSMutableTouchHitTestFilterParameters"8ls32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e27_v16?0"BSSimpleAssertion"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e47_v32?0"NSNumber"8"BKSHIDKeyboardDevice"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e53_v16?0"<BKSHIDEventDeferringGrantAssertionBuilder>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e56_v16?0"BKSMutableHIDEventDeferringConstraintAssertion"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10020
+ ___block_literal_global.101
+ ___block_literal_global.10354
+ ___block_literal_global.104
+ ___block_literal_global.104.10329
+ ___block_literal_global.104.5109
+ ___block_literal_global.10499
+ ___block_literal_global.10721
+ ___block_literal_global.1082
+ ___block_literal_global.109.14081
+ ___block_literal_global.10906
+ ___block_literal_global.11147
+ ___block_literal_global.11400
+ ___block_literal_global.1163
+ ___block_literal_global.11727
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.12383
+ ___block_literal_global.125
+ ___block_literal_global.12565
+ ___block_literal_global.127
+ ___block_literal_global.1272
+ ___block_literal_global.12771
+ ___block_literal_global.12868
+ ___block_literal_global.129
+ ___block_literal_global.12997
+ ___block_literal_global.135
+ ___block_literal_global.13556
+ ___block_literal_global.13796
+ ___block_literal_global.138
+ ___block_literal_global.138.5662
+ ___block_literal_global.14094
+ ___block_literal_global.141
+ ___block_literal_global.141.13440
+ ___block_literal_global.1416
+ ___block_literal_global.14192
+ ___block_literal_global.14425
+ ___block_literal_global.145
+ ___block_literal_global.14565
+ ___block_literal_global.149
+ ___block_literal_global.14929
+ ___block_literal_global.15145
+ ___block_literal_global.152
+ ___block_literal_global.15721
+ ___block_literal_global.16.8717
+ ___block_literal_global.161
+ ___block_literal_global.166
+ ___block_literal_global.1688
+ ___block_literal_global.170
+ ___block_literal_global.177
+ ___block_literal_global.18.9805
+ ___block_literal_global.1863
+ ___block_literal_global.191
+ ___block_literal_global.2.13793
+ ___block_literal_global.209
+ ___block_literal_global.2145
+ ___block_literal_global.22.10887
+ ___block_literal_global.227
+ ___block_literal_global.233
+ ___block_literal_global.25.1409
+ ___block_literal_global.25.8726
+ ___block_literal_global.2590
+ ___block_literal_global.2749
+ ___block_literal_global.2880
+ ___block_literal_global.3.1418
+ ___block_literal_global.3.15148
+ ___block_literal_global.3039
+ ___block_literal_global.307
+ ___block_literal_global.31.8732
+ ___block_literal_global.3188
+ ___block_literal_global.3454
+ ___block_literal_global.351
+ ___block_literal_global.361
+ ___block_literal_global.3628
+ ___block_literal_global.402
+ ___block_literal_global.457
+ ___block_literal_global.4585
+ ___block_literal_global.471
+ ___block_literal_global.4767
+ ___block_literal_global.479
+ ___block_literal_global.505
+ ___block_literal_global.5129
+ ___block_literal_global.5207
+ ___block_literal_global.5326
+ ___block_literal_global.5426
+ ___block_literal_global.55
+ ___block_literal_global.5599
+ ___block_literal_global.58.14092
+ ___block_literal_global.58.8757
+ ___block_literal_global.5849
+ ___block_literal_global.594
+ ___block_literal_global.6070
+ ___block_literal_global.6194
+ ___block_literal_global.6422
+ ___block_literal_global.65.14090
+ ___block_literal_global.66
+ ___block_literal_global.6743
+ ___block_literal_global.683
+ ___block_literal_global.70
+ ___block_literal_global.70.5832
+ ___block_literal_global.700
+ ___block_literal_global.7001
+ ___block_literal_global.7152
+ ___block_literal_global.718
+ ___block_literal_global.736
+ ___block_literal_global.74
+ ___block_literal_global.7482
+ ___block_literal_global.7496
+ ___block_literal_global.76
+ ___block_literal_global.79
+ ___block_literal_global.79.7141
+ ___block_literal_global.8365
+ ___block_literal_global.84
+ ___block_literal_global.8545
+ ___block_literal_global.8547
+ ___block_literal_global.8635
+ ___block_literal_global.8706
+ ___block_literal_global.9034
+ ___block_literal_global.9354
+ ___block_literal_global.9818
+ ___getCADisplayClass_block_invoke.9620
+ _audit_stringQuartzCore.12804
+ _audit_stringQuartzCore.8823
+ _audit_stringQuartzCore.9637
+ _didUpdateDeferringChains:withReply:.descriptionStyle
+ _didUpdateDeferringChains:withReply:.onceToken
+ _getCADisplayClass.9618
+ _getCADisplayClass.softClass.9619
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_configureConnection
+ _objc_msgSend$_configureServerConnectionWithFactory:
+ _objc_msgSend$_connectionForTouchDeliveryService
+ _objc_msgSend$_initConnectionWithConnectionFactory:
+ _objc_msgSend$_initWithCAContextID:andCGSWindowID:
+ _objc_msgSend$_initWithContextID:
+ _objc_msgSend$_initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:inverted:
+ _objc_msgSend$_initWithLabel:
+ _objc_msgSend$_initWithPredicate:restrictedToEventDescriptors:target:reason:priority:identity:
+ _objc_msgSend$_initWithProperties:service:
+ _objc_msgSend$_initWithSettings:
+ _objc_msgSend$_isString
+ _objc_msgSend$_lock_flushStateToServer
+ _objc_msgSend$_lock_postObservingStateToServerIncludingNegative:
+ _objc_msgSend$_lock_repostAllRegistrations
+ _objc_msgSend$_lock_shouldObserveDeferringChanges
+ _objc_msgSend$_lock_updateServerHitTestCategoryContextIDs
+ _objc_msgSend$_lock_updateServerHitTestFilterParameters
+ _objc_msgSend$_observationsFromChains:
+ _objc_msgSend$_queue_handlePendingObservers:
+ _objc_msgSend$_serverLayout
+ _objc_msgSend$_updateTouchDetachmentOffset:userIdentifier:
+ _objc_msgSend$_updateTouchDetachmentRoutingPolicy:userIdentifier:
+ _objc_msgSend$_withTimestamp:build:
+ _objc_msgSend$acquireTransactionForReason:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addTouchAuthenticationSpecifications:forReason:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$assertBarrierOnQueue
+ _objc_msgSend$assertSelectionPath:target:imposesConstraint:reason:
+ _objc_msgSend$compatibilityDisplay
+ _objc_msgSend$containsEndOfChain
+ _objc_msgSend$decodeCollectionOfClass:containingClass:forKey:
+ _objc_msgSend$decodeUInt64ForKey:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$deferEventsMatchingPredicate:priority:restrictedToEventDescriptors:toTarget:withReason:
+ _objc_msgSend$deferringPath
+ _objc_msgSend$detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:
+ _objc_msgSend$detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:initialTouchOffset:
+ _objc_msgSend$detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:initialTouchOffset:error:
+ _objc_msgSend$enableSecureRenderingControlForDisplayUUID:
+ _objc_msgSend$encodeUInt64:forKey:
+ _objc_msgSend$finalStringTargetIndex
+ _objc_msgSend$generation
+ _objc_msgSend$hasBeenSignalled
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithConnection:
+ _objc_msgSend$initWithContextID:
+ _objc_msgSend$initWithContextID:displayUUID:identifier:policy:connectionFactory:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:containsSubset:containsEndOfChain:finalStringTargetIndex:generation:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:generation:
+ _objc_msgSend$initWithPID:token:
+ _objc_msgSend$initWithReason:invalidatedBlock:
+ _objc_msgSend$initWithServiceConnection:
+ _objc_msgSend$intValue
+ _objc_msgSend$isSecureRenderingEnabledForDisplayUUID:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$mutableCopyWithZone:
+ _objc_msgSend$newTouchStreamForContextID:displayUUID:identifier:shouldSendAmbiguityRecommendations:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$proximityDidUnoccludeAfterWake
+ _objc_msgSend$proximityDidUnoccludeScreenAfterWakeForDisplayUUID:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$recalibrateProximitySensor
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$requestEstimatedProximityEventWithTimeout:
+ _objc_msgSend$requestEstimatedProximityEventWithTimeout:displayUUID:
+ _objc_msgSend$requestProximityDetectionMode:
+ _objc_msgSend$requestProximityStatusEventForReason:
+ _objc_msgSend$requestProximityStatusEventForReason:displayUUID:
+ _objc_msgSend$requestUISensorModes:
+ _objc_msgSend$resetProximityCalibrationForDisplayUUID:
+ _objc_msgSend$restrictHitTestToTheseTargets
+ _objc_msgSend$restrictedHitTestsAllowEmbeddedTargets
+ _objc_msgSend$routingPolicy
+ _objc_msgSend$ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:priority:seed:pid:
+ _objc_msgSend$secureRenderingService:receivedSecureRenderingViolations:
+ _objc_msgSend$sensorCharacteristics
+ _objc_msgSend$sensorCharacteristicsForDisplayUUID:
+ _objc_msgSend$serviceForDisplayUUID:
+ _objc_msgSend$setDesignatedMainDisplayUUID:
+ _objc_msgSend$setDestinationDisplayUUID:
+ _objc_msgSend$setDetachedTouchOffset:userIdentifier:
+ _objc_msgSend$setDetachedTouchRoutingPolicy:userIdentifier:
+ _objc_msgSend$setFinalStringToken:
+ _objc_msgSend$setGeneration:
+ _objc_msgSend$setGrantAssertions:
+ _objc_msgSend$setGranteeTarget:
+ _objc_msgSend$setGrantorTarget:
+ _objc_msgSend$setHitTestStimulus:
+ _objc_msgSend$setLayout:
+ _objc_msgSend$setMaximumValueLengthBeforeTruncation:
+ _objc_msgSend$setObservesDeferringChanges:
+ _objc_msgSend$setPolicyStatus:
+ _objc_msgSend$setRestrictHitTestToTheseTargets:
+ _objc_msgSend$setRestrictedHitTestsAllowEmbeddedTargets:
+ _objc_msgSend$setSecureRenderingEnabled:forDisplayUUID:
+ _objc_msgSend$setSelectionPath:
+ _objc_msgSend$setSourceDisplayUUID:
+ _objc_msgSend$setString:
+ _objc_msgSend$setTargetsToAlwaysSendTouches:
+ _objc_msgSend$setTargetsToExcludeFromHitTesting:
+ _objc_msgSend$setValueTruncation:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$targetID
+ _objc_msgSend$targetsToAlwaysSendTouches
+ _objc_msgSend$targetsToExcludeFromHitTesting
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$touchOffset
+ _objc_msgSend$updateDispatchMode:ambiguityRecommendation:timestamp:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
+ _protobufSchema.onceToken.10017
+ _protobufSchema.onceToken.10496
+ _protobufSchema.onceToken.127
+ _protobufSchema.onceToken.14078
+ _protobufSchema.onceToken.14563
+ _protobufSchema.onceToken.148
+ _protobufSchema.onceToken.14926
+ _protobufSchema.onceToken.1685
+ _protobufSchema.onceToken.169
+ _protobufSchema.onceToken.207
+ _protobufSchema.onceToken.225
+ _protobufSchema.onceToken.2870
+ _protobufSchema.onceToken.3186
+ _protobufSchema.onceToken.349
+ _protobufSchema.onceToken.359
+ _protobufSchema.onceToken.4765
+ _protobufSchema.onceToken.477
+ _protobufSchema.onceToken.56
+ _protobufSchema.onceToken.5847
+ _protobufSchema.onceToken.592
+ _protobufSchema.onceToken.698
+ _protobufSchema.onceToken.6999
+ _protobufSchema.onceToken.7150
+ _protobufSchema.onceToken.716
+ _protobufSchema.onceToken.734
+ _protobufSchema.onceToken.90
+ _protobufSchema.onceToken.9031
+ _protobufSchema.schema.10018
+ _protobufSchema.schema.10497
+ _protobufSchema.schema.126
+ _protobufSchema.schema.14079
+ _protobufSchema.schema.14564
+ _protobufSchema.schema.147
+ _protobufSchema.schema.14927
+ _protobufSchema.schema.168
+ _protobufSchema.schema.1686
+ _protobufSchema.schema.206
+ _protobufSchema.schema.224
+ _protobufSchema.schema.2871
+ _protobufSchema.schema.3187
+ _protobufSchema.schema.348
+ _protobufSchema.schema.358
+ _protobufSchema.schema.476
+ _protobufSchema.schema.4766
+ _protobufSchema.schema.55
+ _protobufSchema.schema.5848
+ _protobufSchema.schema.591
+ _protobufSchema.schema.697
+ _protobufSchema.schema.7000
+ _protobufSchema.schema.715
+ _protobufSchema.schema.7151
+ _protobufSchema.schema.733
+ _protobufSchema.schema.89
+ _protobufSchema.schema.9032
+ _sUniqueTokenCounter
+ _sUniqueTokenLock
+ _sharedInstance.__instance.5130
+ _sharedInstance.__shared.14193
+ _sharedInstance.__sharedInstance.12414
+ _sharedInstance.controller.7497
+ _sharedInstance.onceToken.10720
+ _sharedInstance.onceToken.1081
+ _sharedInstance.onceToken.1162
+ _sharedInstance.onceToken.12413
+ _sharedInstance.onceToken.14191
+ _sharedInstance.onceToken.14761
+ _sharedInstance.onceToken.2941
+ _sharedInstance.onceToken.5128
+ _sharedInstance.onceToken.6069
+ _sharedInstance.onceToken.7481
+ _sharedInstance.onceToken.7495
+ _sharedInstance.onceToken.8544
+ _sharedInstance.overseer
+ _sharedInstance.service.1164
+ _sharedInstance.service.14762
+ _sharedInstance.service.6071
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_uint64
- +[BKSHIDEventDeferringChainObserverPredicate build:]
- +[BKSHIDEventDeferringChainObserverPredicate new]
- +[BKSHIDEventDeferringChainObserverPredicate supportsSecureCoding]
- +[BKSSimplerAssertion assertionWithDescription:invalidationBlock:]
- +[BKSSimplerAssertion new]
- -[BKSExternalDefaults lockdownDefaults]
- -[BKSHIDEventDeferringChainObserverPredicate .cxx_destruct]
- -[BKSHIDEventDeferringChainObserverPredicate _initWithCopyOf:]
- -[BKSHIDEventDeferringChainObserverPredicate _init]
- -[BKSHIDEventDeferringChainObserverPredicate copyWithZone:]
- -[BKSHIDEventDeferringChainObserverPredicate display]
- -[BKSHIDEventDeferringChainObserverPredicate encodeWithCoder:]
- -[BKSHIDEventDeferringChainObserverPredicate environment]
- -[BKSHIDEventDeferringChainObserverPredicate hash]
- -[BKSHIDEventDeferringChainObserverPredicate initWithCoder:]
- -[BKSHIDEventDeferringChainObserverPredicate init]
- -[BKSHIDEventDeferringChainObserverPredicate isEqual:]
- -[BKSHIDEventDeferringChainObserverPredicate mutableCopyWithZone:]
- -[BKSHIDEventDeferringConstraintAssertion basis]
- -[BKSHIDEventDeferringTarget _initWithPID:token:]
- -[BKSHIDEventDeferringToken appendDescriptionToFormatter:]
- -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:]
- -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:]
- -[BKSHIDEventObserver _lock_disableObservation]
- -[BKSHIDEventObserver _lock_enableObservation]
- -[BKSHIDEventObserver _lock_flushInitialStateToServer]
- -[BKSHIDEventObserver didUpdateDeferringChains:]
- -[BKSHIDEventObserver didUpdateDeferringObservations:]
- -[BKSHIDEventSenderDescriptor _initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:]
- -[BKSHIDKeyboardDevice _initWithProperties:]
- -[BKSHIDUISensorService .cxx_destruct]
- -[BKSHIDUISensorService _lock_pushCurrentModeToServer]
- -[BKSHIDUISensorService init]
- -[BKSLockdownDefaults _bindAndRegisterDefaults]
- -[BKSLockdownDefaults init]
- -[BKSMutableHIDEventDeferringChainObserverPredicate copyWithZone:]
- -[BKSMutableHIDEventDeferringChainObserverPredicate setDisplay:]
- -[BKSMutableHIDEventDeferringChainObserverPredicate setEnvironment:]
- -[BKSMutableHIDEventDeferringConstraintAssertion setBasis:]
- -[BKSSimplerAssertion .cxx_destruct]
- -[BKSSimplerAssertion dealloc]
- -[BKSSimplerAssertion description]
- -[BKSSimplerAssertion init]
- -[BKSSimplerAssertion invalidate]
- -[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]
- -[BKSTouchDeliveryUpdate contextID]
- -[BKSTouchDeliveryUpdate setContextID:]
- -[BKSTouchEventService _connectToService]
- -[BKSTouchEventService _repostAllRegistrations]
- -[BKSTouchEventService init]
- -[BKSTouchStream reference]
- -[BKSTouchStream setReference:]
- -[_BKSCloneMirroringModeRequest displayUUID]
- -[_BKSCloneMirroringModeRequest setDisplayUUID:]
- -[_BKSHIDCAContextEventDeferringToken appendDescriptionToFormatter:]
- -[_BKSHIDCGSConnectionIDEventDeferringToken appendDescriptionToFormatter:]
- -[_BKSHIDCGSWindowIDEventDeferringToken appendDescriptionToFormatter:]
- -[_BKSHIDStringIdentifierEventDeferringToken appendDescriptionToFormatter:]
- GCC_except_table1095
- GCC_except_table1096
- GCC_except_table1208
- GCC_except_table1231
- GCC_except_table1252
- GCC_except_table1385
- GCC_except_table1389
- GCC_except_table1399
- GCC_except_table1527
- GCC_except_table1643
- GCC_except_table1771
- GCC_except_table1894
- GCC_except_table1903
- GCC_except_table2036
- GCC_except_table2146
- GCC_except_table2148
- GCC_except_table2178
- GCC_except_table2357
- GCC_except_table2523
- GCC_except_table2530
- GCC_except_table2795
- GCC_except_table2810
- GCC_except_table2970
- _BKSDisplayServicesSetMainDisplayCloneMirroringModeForDestinationDisplay.displayToModeCache
- _OBJC_CLASS_$_BKSHIDEventDeferringChainObserverPredicate
- _OBJC_CLASS_$_BKSLockdownDefaults
- _OBJC_CLASS_$_BKSMutableHIDEventDeferringChainObserverPredicate
- _OBJC_CLASS_$_BKSSimplerAssertion
- _OBJC_IVAR_$_BKSExternalDefaults._lazy_lockdownDefaults
- _OBJC_IVAR_$_BKSHIDEventDeferringChainObserverPredicate._display
- _OBJC_IVAR_$_BKSHIDEventDeferringChainObserverPredicate._environment
- _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._basis
- _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._timetamp
- _OBJC_IVAR_$_BKSHIDUISensorService._lock
- _OBJC_IVAR_$_BKSHIDUISensorService._lock_prevailingMode
- _OBJC_IVAR_$_BKSHIDUISensorService._modeAssertion
- _OBJC_IVAR_$_BKSHIDUISensorService._suppressionAssertion
- _OBJC_IVAR_$_BKSSimplerAssertion._identifier
- _OBJC_IVAR_$_BKSSimplerAssertion._invalid
- _OBJC_IVAR_$_BKSSimplerAssertion._invalidationBlock
- _OBJC_IVAR_$_BKSTouchDeliveryUpdate._contextID
- _OBJC_IVAR_$_BKSTouchEventService._connectionLock
- _OBJC_IVAR_$_BKSTouchEventService._registrationLock
- _OBJC_IVAR_$_BKSTouchEventService._registrationLock_registrationsByContextID
- _OBJC_IVAR_$_BKSTouchStream._reference
- _OBJC_IVAR_$__BKSCloneMirroringModeRequest._displayUUID
- _OBJC_METACLASS_$_BKSHIDEventDeferringChainObserverPredicate
- _OBJC_METACLASS_$_BKSLockdownDefaults
- _OBJC_METACLASS_$_BKSMutableHIDEventDeferringChainObserverPredicate
- _OBJC_METACLASS_$_BKSSimplerAssertion
- _QuartzCoreLibrary.11926
- _QuartzCoreLibraryCore.frameworkLibrary.11941
- _QuartzCoreLibraryCore.frameworkLibrary.8180
- _QuartzCoreLibraryCore.frameworkLibrary.8993
- __BKSDisplayDisplayIsTethered
- __BKSDisplayRemoveCloneMirroringModeForDestinationDisplay
- __BKSDisplaySetCloneMirroringModeForDestinationDisplay
- __BKSDisplaySetTetheredOrientationNotificationsDisabled
- __BKSDisplayTetherPrefsNeedImmediateUpdate
- __BKSDisplayUpdateMirroredDisplayOrientationWithInterfaceOrientation
- __BKSDisplayUpdateTetheredDisplayOrientationIfNecessaryWithInterfaceOrientation
- __BKSHIDDigitizerTouchDetach
- __BKSHIDDigitizerTouchSetOffset
- __BKSHIDDigitizerTouchSetRoutingPolicy
- __BKSHIDGetUISensorCharacteristics
- __BKSHIDNotifyOnNextUserEvent
- __BKSHIDProximityDidUnoccludeAfterScreenWake
- __BKSHIDRequestEstimatedProximityEvents
- __BKSHIDRequestProximityStatusEvent
- __BKSHIDRequestUISensorMode
- __BKSHIDResetProximityCalibration
- __BKSHIDResetUserEventTimer
- __BKSHIDSafeToResetIdleTimer
- __BKSHIDSetDeviceInterfaceOrientation
- __BKSHIDTouchStreamCreate
- __BKSHIDTouchStreamInvalidate
- __BKSHIDTouchStreamSetEventDispatchMode
- __BKSVerifyIsArrayOfNumbers
- __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_$_CLASS_METHODS_BKSSimplerAssertion
- __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_$_INSTANCE_METHODS_BKSLockdownDefaults
- __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringChainObserverPredicate
- __OBJC_$_INSTANCE_METHODS_BKSSimplerAssertion
- __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_$_INSTANCE_VARIABLES_BKSHIDUISensorService
- __OBJC_$_INSTANCE_VARIABLES_BKSSimplerAssertion
- __OBJC_$_PROP_LIST_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_$_PROP_LIST_BKSLockdownDefaults
- __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringChainObserverPredicate
- __OBJC_$_PROP_LIST_BKSSimplerAssertion
- __OBJC_$_PROP_LIST_BKSTouchStream
- __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_CLASS_PROTOCOLS_$_BKSSimplerAssertion
- __OBJC_CLASS_PROTOCOLS_$_BKSTouchDeliveryObservationService
- __OBJC_CLASS_RO_$_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_CLASS_RO_$_BKSLockdownDefaults
- __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringChainObserverPredicate
- __OBJC_CLASS_RO_$_BKSSimplerAssertion
- __OBJC_METACLASS_RO_$_BKSHIDEventDeferringChainObserverPredicate
- __OBJC_METACLASS_RO_$_BKSLockdownDefaults
- __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringChainObserverPredicate
- __OBJC_METACLASS_RO_$_BKSSimplerAssertion
- ___28-[BKSTouchEventService init]_block_invoke
- ___28-[BKSTouchEventService init]_block_invoke_2
- ___29-[BKSHIDUISensorService init]_block_invoke
- ___29-[BKSHIDUISensorService init]_block_invoke_2
- ___39+[BKSHIDUISensorService sharedInstance]_block_invoke
- ___39-[BKSExternalDefaults lockdownDefaults]_block_invoke
- ___41-[BKSTouchEventService _connectToService]_block_invoke
- ___41-[BKSTouchEventService _connectToService]_block_invoke.189
- ___41-[BKSTouchEventService _connectToService]_block_invoke.191
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke_2
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke_3
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke_4
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke_5
- ___45-[BKSDisplayRenderOverlayDescriptor isEqual:]_block_invoke_6
- ___46-[BKSHIDUISensorService sensorCharacteristics]_block_invoke
- ___47-[BKSTouchEventService _repostAllRegistrations]_block_invoke
- ___47-[BKSTouchEventService _repostAllRegistrations]_block_invoke_2
- ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.106
- ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.107
- ___52-[BKSMousePointerService _activateServerConnection:]_block_invoke.140
- ___57-[BKSSystemShellService _checkInWaitingForDataMigration:]_block_invoke.94
- ___62-[BKSMutableHIDEventDiscreteDispatchingPredicate setDisplays:]_block_invoke.150
- ___64-[BKSHIDEventDeliveryPolicyObserver deferringResolutionsChanged]_block_invoke.83
- ___65-[BKSMutableHIDEventKeyCommandsDispatchingPredicate setDisplays:]_block_invoke.123
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke.71
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke.72
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke_2
- ___68-[BKSTouchDeliveryObservationService _connectToTouchDeliveryService]_block_invoke_3
- ___71-[BKSTouchDeliveryObservationService _processTouchEventDeliveryUpdate:]_block_invoke.84
- ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.110
- ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.120
- ___72-[BKSSystemShellService _activateServerConnectionWithIdleSleepInterval:]_block_invoke.121
- ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:]_block_invoke
- ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:]_block_invoke_2
- ___BKSDisplayServicesAcquireDisplayDisabledAssertion_block_invoke.65
- ___BKSDisplayServicesArchiveWithOptionsAndCompletion_block_invoke.148
- ___BKSDisplayServicesSetMainDisplayCloneMirroringModeForDestinationDisplay_block_invoke
- ___BKSHIDServicesRequestProximityDetectionMode_block_invoke
- ___Block_byref_object_copy_.9985
- ___Block_byref_object_dispose_.9986
- ___QuartzCoreLibraryCore_block_invoke.11942
- ___QuartzCoreLibraryCore_block_invoke.8181
- ___QuartzCoreLibraryCore_block_invoke.8994
- ___block_descriptor_40_e8_32s_e27_v16?0"BSSimpleAssertion"8ls32l8
- ___block_descriptor_40_e8_32s_e5_8?0ls32l8
- ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
- ___block_descriptor_48_e8_32s40s_e47_v32?0"NSNumber"8"BKSHIDKeyboardDevice"16^B24ls32l8s40l8
- ___block_descriptor_52_e8_32r40r_e36_B16?0"BKSHIDEventDeferringTarget"8lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e56_v16?0"BKSMutableHIDEventDeferringConstraintAssertion"8ls32l8s40l8s48l8
- ___block_literal_global.100
- ___block_literal_global.10047
- ___block_literal_global.10228
- ___block_literal_global.10469
- ___block_literal_global.105
- ___block_literal_global.106
- ___block_literal_global.1064
- ___block_literal_global.10719
- ___block_literal_global.11530
- ___block_literal_global.117
- ___block_literal_global.11712
- ___block_literal_global.1189
- ___block_literal_global.11917
- ___block_literal_global.12010
- ___block_literal_global.12139
- ___block_literal_global.12654
- ___block_literal_global.12886
- ___block_literal_global.13171
- ___block_literal_global.13271
- ___block_literal_global.13376
- ___block_literal_global.13509
- ___block_literal_global.136
- ___block_literal_global.136.5332
- ___block_literal_global.137
- ___block_literal_global.13793
- ___block_literal_global.139
- ___block_literal_global.14009
- ___block_literal_global.14598
- ___block_literal_global.146
- ___block_literal_global.153
- ___block_literal_global.1541
- ___block_literal_global.16.8097
- ___block_literal_global.162
- ___block_literal_global.167
- ___block_literal_global.1717
- ___block_literal_global.174
- ___block_literal_global.18.9177
- ___block_literal_global.1846
- ___block_literal_global.186
- ___block_literal_global.187
- ___block_literal_global.193
- ___block_literal_global.2.12883
- ___block_literal_global.219
- ___block_literal_global.22.10209
- ___block_literal_global.2232
- ___block_literal_global.2386
- ___block_literal_global.24
- ___block_literal_global.246
- ___block_literal_global.25.8106
- ___block_literal_global.2520
- ___block_literal_global.2678
- ___block_literal_global.2811
- ___block_literal_global.3.1191
- ___block_literal_global.3.14012
- ___block_literal_global.3082
- ___block_literal_global.31.8112
- ___block_literal_global.310
- ___block_literal_global.320
- ___block_literal_global.3237
- ___block_literal_global.357
- ___block_literal_global.3904
- ___block_literal_global.4078
- ___block_literal_global.409
- ___block_literal_global.426
- ___block_literal_global.438
- ___block_literal_global.4512
- ___block_literal_global.4589
- ___block_literal_global.4804
- ___block_literal_global.4974
- ___block_literal_global.503
- ___block_literal_global.5179
- ___block_literal_global.5409
- ___block_literal_global.553
- ___block_literal_global.5530
- ___block_literal_global.56
- ___block_literal_global.5756
- ___block_literal_global.6052
- ___block_literal_global.62
- ___block_literal_global.6293
- ___block_literal_global.64.3905
- ___block_literal_global.6438
- ___block_literal_global.659
- ___block_literal_global.677
- ___block_literal_global.6777
- ___block_literal_global.6791
- ___block_literal_global.695
- ___block_literal_global.75
- ___block_literal_global.75.10013
- ___block_literal_global.7752
- ___block_literal_global.7930
- ___block_literal_global.7932
- ___block_literal_global.8
- ___block_literal_global.80
- ___block_literal_global.8013
- ___block_literal_global.8086
- ___block_literal_global.81
- ___block_literal_global.83
- ___block_literal_global.8418
- ___block_literal_global.85
- ___block_literal_global.8721
- ___block_literal_global.90
- ___block_literal_global.9190
- ___block_literal_global.93
- ___block_literal_global.9386
- ___block_literal_global.957
- ___block_literal_global.97
- ___block_literal_global.9722
- ___block_literal_global.9862
- ___getCADisplayClass_block_invoke.8992
- _audit_stringQuartzCore.11945
- _audit_stringQuartzCore.8196
- _audit_stringQuartzCore.9009
- _getCADisplayClass.8990
- _getCADisplayClass.softClass.8991
- _lockdownDefaults.__once
- _objc_msgSend$_connectToService
- _objc_msgSend$_connectToTouchDeliveryService
- _objc_msgSend$_initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:
- _objc_msgSend$_initWithPID:token:
- _objc_msgSend$_initWithProperties:
- _objc_msgSend$_lock_disableObservation
- _objc_msgSend$_lock_enableObservation
- _objc_msgSend$_lock_pushCurrentModeToServer
- _objc_msgSend$_repostAllRegistrations
- _objc_msgSend$_string
- _objc_msgSend$appendBool:counterpart:
- _objc_msgSend$appendObject:counterpart:
- _objc_msgSend$assertionWithDescription:invalidationBlock:
- _objc_msgSend$contextIDsToAlwaysSendTouches
- _objc_msgSend$contextIDsToExcludeFromHitTesting
- _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:
- _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:
- _objc_msgSend$reference
- _objc_msgSend$setContextIDsToAlwaysSendTouches:
- _objc_msgSend$setContextIDsToExcludeFromHitTesting:
- _objc_msgSend$setDisplayUUID:
- _objc_msgSend$setObservesDeferringChainIdentities:
- _objc_msgSend$setObservesDeferringResolutions:
- _objc_msgSend$setWithCapacity:
- _protobufSchema.onceToken.13162
- _protobufSchema.onceToken.13507
- _protobufSchema.onceToken.137
- _protobufSchema.onceToken.13790
- _protobufSchema.onceToken.1538
- _protobufSchema.onceToken.184
- _protobufSchema.onceToken.2510
- _protobufSchema.onceToken.2808
- _protobufSchema.onceToken.308
- _protobufSchema.onceToken.318
- _protobufSchema.onceToken.4075
- _protobufSchema.onceToken.436
- _protobufSchema.onceToken.5177
- _protobufSchema.onceToken.54
- _protobufSchema.onceToken.551
- _protobufSchema.onceToken.6291
- _protobufSchema.onceToken.6436
- _protobufSchema.onceToken.657
- _protobufSchema.onceToken.675
- _protobufSchema.onceToken.693
- _protobufSchema.onceToken.79
- _protobufSchema.onceToken.8415
- _protobufSchema.onceToken.91
- _protobufSchema.onceToken.9383
- _protobufSchema.onceToken.9859
- _protobufSchema.schema.13163
- _protobufSchema.schema.13508
- _protobufSchema.schema.136
- _protobufSchema.schema.13791
- _protobufSchema.schema.1539
- _protobufSchema.schema.183
- _protobufSchema.schema.2511
- _protobufSchema.schema.2809
- _protobufSchema.schema.307
- _protobufSchema.schema.317
- _protobufSchema.schema.4076
- _protobufSchema.schema.435
- _protobufSchema.schema.5178
- _protobufSchema.schema.53
- _protobufSchema.schema.550
- _protobufSchema.schema.6292
- _protobufSchema.schema.6437
- _protobufSchema.schema.656
- _protobufSchema.schema.674
- _protobufSchema.schema.692
- _protobufSchema.schema.78
- _protobufSchema.schema.8416
- _protobufSchema.schema.90
- _protobufSchema.schema.9384
- _protobufSchema.schema.9860
- _sensorCharacteristics.onceToken
- _sensorCharacteristics.sCharacteristics
- _sharedInstance.__shared.13272
- _sharedInstance.__sharedInstance.11562
- _sharedInstance.controller.6792
- _sharedInstance.onceToken.10046
- _sharedInstance.onceToken.11561
- _sharedInstance.onceToken.13270
- _sharedInstance.onceToken.13642
- _sharedInstance.onceToken.186
- _sharedInstance.onceToken.4511
- _sharedInstance.onceToken.5408
- _sharedInstance.onceToken.6776
- _sharedInstance.onceToken.6790
- _sharedInstance.onceToken.7929
- _sharedInstance.onceToken.956
- _sharedInstance.service.13643
- _sharedInstance.service.188
- _sharedInstance.service.5410
- _sharedInstance.service.958
CStrings:
+ "%@-%p"
+ "%@->%@:%@"
+ "%X"
+ "%li-grant"
+ "%x-%d"
+ "'"
+ "(stimulus & (BKSHitTestStimulusFinger | BKSHitTestStimulusPencil | BKSHitTestStimulusMousePointer)) != 0"
+ "+[BKSDisplayTraits new]"
+ "+[BKSHIDEventDeferringGrantAssertion new]"
+ "-[BKSDisplayTraits init]"
+ "-[BKSHIDEventDeferringGrantAssertion init]"
+ "-init is not allowed on _BKSHIDUniqueEventEventDeferringToken"
+ "/"
+ "1"
+ "<%@: %p; token=%llu; timestamp=%f; contexts=%@>"
+ "<%X>"
+ "<invalid:%llX>"
+ "A"
+ "BKHIDUISensorService"
+ "BKSDisplayServicesSetCloningSourceDisplayUUID changed to %{public}@"
+ "BKSDisplayTraits cannot be subclassed"
+ "BKSDisplayTraits.m"
+ "BKSHIDEventDeferringGrantAssertion builder used outside of +build: closure"
+ "BKSHIDEventDeferringGrantAssertion cannot be subclassed"
+ "BKSHIDEventDeferringGrantAssertion.m"
+ "BKSHIDPithy"
+ "BKSHIDServicesNotifyOnNextUserEvent"
+ "BKSHIDServicesProximityDetectionModeIsValid(proxMode)"
+ "BKSHIDServicesResetUserEventTimer"
+ "BKSHIDServicesSafeToResetIdleTimer"
+ "BKSHIDUISensorMode transaction"
+ "BKSLogMouseInterpolationDetails"
+ "BKSSecureRenderingService: cannot get connection for service"
+ "BKSSecureRenderingService: cannot get endpoint for mach service"
+ "BKSSystemShellDidReconnect-21000319"
+ "BKSTouchEventService interruption -- attempting to reconnect"
+ "BKSTouchStream - connection activation"
+ "BKSTouchStream.m"
+ "BKSecureRendering"
+ "BKTouchStream"
+ "BQ"
+ "BSSTouchEventService - connection activation"
+ "Failed to detach additional touches: %{public}@"
+ "Failed to detach touches: %{public}@"
+ "Failed to update offset for userIdentifier %d - waiting to connect"
+ "Failed to update routing policy for userIdentifier %d - waiting to connect"
+ "Not connected to server - returning identity transform for display:%{public}@ context:%X layer:%llX"
+ "Not connected to server, cannot add detached touches!!"
+ "Not connected to server, cannot detach touches!!"
+ "PhoneMute"
+ "RouteEventsIgnoringSystemShellPolicy"
+ "SecureRendering"
+ "TouchDelivery120Hz"
+ "TouchStream"
+ "Unable to get a connection to the touch event server! No services will be allowed!!!"
+ "Unable to get a connection to the touch stream server! No stream will be allowed!!!"
+ "Unknown(%ld)"
+ "WARNING: BKSTouchEventService invalidated!!"
+ "WARNING: BKSTouchStream invalidated!  No more touches will be delivered!!"
+ "[BKSHIDEventObserver] %p %{public}@ setToken:%{public}@"
+ "[BKSHIDEventObserver] - connection activation"
+ "[BKSHIDEventObserver] - connection interruption"
+ "[BKSHIDEventObserver] Unable to get a connection to the hid event observer server! No observation will be allowed!!!"
+ "[BKSHIDEventObserver] invalidated - backboardd must have unloaded, exiting…"
+ "[BKSHIDEventObserver] policy-per %{public}@"
+ "[BKSHIDEventObserver] policyDidChange: %p -> <%{public}@: %p> now:%{public}@"
+ "[BKSHIDEventObserver] set observing:%{BOOL}u"
+ "[matchDisplays count] > 0"
+ "_BKSHIDUISensorDisplayAssociatedService.m"
+ "_BKSHIDUISensorOverseer.m"
+ "_constraints"
+ "_finalStringTargetIndex"
+ "_generation"
+ "_hitTestStimulus"
+ "_inverted"
+ "_label"
+ "_surfaceType"
+ "_targetWindowID"
+ "_uniqueValue"
+ "add reference:(%{public}@): %p"
+ "authentic"
+ "backboardd must be exiting"
+ "backboardd-attr-cache-21000319"
+ "cannot connect to server, exiting"
+ "cannot directly allocate BKSDisplayTraits"
+ "cannot directly allocate BKSHIDEventDeferringGrantAssertion"
+ "characteristics"
+ "com.apple."
+ "com.apple.backboardservices.secureRenderingService"
+ "com.apple.frontboard.systemappservices/"
+ "connection activation"
+ "contexts"
+ "desc"
+ "destinationDisplayUUID"
+ "dunno"
+ "env"
+ "error decoding characteristics:%{public}@"
+ "error decoding mode:%{public}@"
+ "error encoding mode:%{public}@"
+ "externalReferenceCount"
+ "fb/"
+ "finalStringTargetIndex"
+ "finger"
+ "generation"
+ "grantAssertions"
+ "granteeTarget"
+ "grantorTarget"
+ "grants"
+ "high"
+ "hitTestStimulus"
+ "hostingContextsChain"
+ "id<BSInvalidatable>  _Nonnull BKSDisplayServicesSetCloneMirroringModeForSourceDisplayToDestinationDisplay(NSString * _Nullable __strong, NSString *__strong _Nonnull, BKSDisplayServicesCloneMirroringMode)"
+ "inverted"
+ "label"
+ "lastPathComponent"
+ "logMouseInterpolationDetails"
+ "low"
+ "modeAssertion"
+ "mousePointer"
+ "newRoutingPolicy"
+ "normal"
+ "observerPolicyDidChange: %p -> <%{public}@: %p> now:%{public}@"
+ "overseer: add %{public}@"
+ "overseer: remove %{public}@"
+ "policy observer %{public}@ added"
+ "policy observer %{public}@ gone"
+ "prevailing client request(%{public}@): %{public}@"
+ "prevailing client request(%{public}@): %{public}@ all modes:%{public}@"
+ "prevailing client request(%{public}@): none!"
+ "prevailingMode"
+ "priority"
+ "protobuf"
+ "proxMode != BKSHIDServicesProximityDetectionModeNone"
+ "reactivating connection to server"
+ "reconnecting after service interruption and shell reconnection"
+ "remove reference:(%{public}@): %p"
+ "request is now %{public}@"
+ "restrictHitTestToTheseTargets"
+ "restrictedHitTestsAllowEmbeddedTargets"
+ "routingPolicy"
+ "still waiting on handshake??"
+ "surfaceType"
+ "t"
+ "targetID"
+ "targetWindowID"
+ "targetsToAlwaysSendTouches"
+ "targetsToExcludeFromHitTesting"
+ "this process is invoking %{public}s, which is a no-op"
+ "touchIdentifiers"
+ "uniqueValue"
+ "unsupported restrictHitTestToTheseTargets structure %@"
+ "unsupported targetsToAlwaysSendTouches structure %@"
+ "unsupported targetsToExcludeFromHitTesting structure %@"
+ "uq"
+ "v16@?0@\"<BKSHIDEventDeferringGrantAssertionBuilder>\"8"
+ "v16@?0@\"BKSMutableHIDEventPolicyObservation\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
+ "will update observations for %d observers"
+ "window"
- "#16@0:8"
- "#20@0:8C16"
- "%@:%@"
- "%s failed to create touch stream:%d"
- "&"
- "+[BKSHIDEventDeferringChainObserverPredicate new]"
- "-[BKSHIDEventDeferringChainObserverPredicate init]"
- "-[BKSTouchStream initWithContextID:displayUUID:identifier:policy:]"
- ".cxx_destruct"
- "2OK50OGmkXM1ospsh766WQ"
- "2Q"
- "@"
- "@\"<BKSAccelerometerDelegate>\""
- "@\"<BKSAlternateSystemAppDelegate>\""
- "@\"<BKSHIDEventDeferringSelectionPathSymbol>\""
- "@\"<BKSHIDEventDeliveryChainObserving>\""
- "@\"<BKSHIDEventDeliveryManagerServerInterface>\""
- "@\"<BKSHIDEventProvenance>\""
- "@\"<BKSMousePointerDeviceObserver>\""
- "@\"<BKSMousePointerPreferencesObserver>\""
- "@\"<BSInvalidatable>\""
- "@\"BKSDisplayProgressIndicatorProperties\""
- "@\"BKSDisplayProgressIndicatorProperties\"16@0:8"
- "@\"BKSDisplayRenderOverlayDescriptor\""
- "@\"BKSDisplayRenderOverlayDescriptor\"16@0:8"
- "@\"BKSEventDeferringChainIdentity\""
- "@\"BKSHIDEventAuthenticationMessage\""
- "@\"BKSHIDEventDeferringChangeBasis\""
- "@\"BKSHIDEventDeferringConstraint\""
- "@\"BKSHIDEventDeferringEnvironment\""
- "@\"BKSHIDEventDeferringEnvironment\"16@0:8"
- "@\"BKSHIDEventDeferringModality\""
- "@\"BKSHIDEventDeferringPredicate\""
- "@\"BKSHIDEventDeferringSelectionPathIdentifier\""
- "@\"BKSHIDEventDeferringSelectionTarget\""
- "@\"BKSHIDEventDeferringTarget\""
- "@\"BKSHIDEventDeferringToken\""
- "@\"BKSHIDEventDeferringToken\"16@0:8"
- "@\"BKSHIDEventDeliveryChainObserver\""
- "@\"BKSHIDEventDeliveryPolicy\""
- "@\"BKSHIDEventDescriptor\""
- "@\"BKSHIDEventDiscreteDispatchingPredicate\""
- "@\"BKSHIDEventDispatchingTarget\""
- "@\"BKSHIDEventDisplay\""
- "@\"BKSHIDEventDisplay\"16@0:8"
- "@\"BKSHIDEventHitTestLayerInformation\""
- "@\"BKSHIDEventKeyCommand\""
- "@\"BKSHIDEventKeyCommandsDispatchingPredicate\""
- "@\"BKSHIDEventObserver\""
- "@\"BKSHIDEventSenderDescriptor\""
- "@\"BKSHIDEventSimpleProvenance\""
- "@\"BKSHIDKeyboardDevice\""
- "@\"BKSHIDKeyboardDeviceProperties\""
- "@\"BKSHIDUISensorMode\""
- "@\"BKSIAPDefaults\""
- "@\"BKSKeyboardDefaults\""
- "@\"BKSLockdownDefaults\""
- "@\"BKSMousePointerDevicePreferences\"16@0:8"
- "@\"BKSMousePointerDevicePreferences\"24@0:8@\"BKSMousePointerDevice\"16"
- "@\"BKSMousePointerGlobalContextOptions\""
- "@\"BKSPersistentConnectionDefaults\""
- "@\"BKSProximityDetectionMaskChangeEvent\"24@0:8@\"NSNumber\"16"
- "@\"BKSSceneHostSettings\""
- "@\"BKSSpringBoardDefaults\""
- "@\"BKSTouchEventService\""
- "@\"BKSWindowServerHitTestSecurityAnalysis\""
- "@\"BSCompoundAssertion\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSMutableIntegerMap\""
- "@\"BSMutableSettings\""
- "@\"BSOrderedDictionary\""
- "@\"BSProtobufSchema\"16@0:8"
- "@\"BSServiceConnection\""
- "@\"BSServiceDispatchQueue\""
- "@\"BSServiceInitiatingConnection\""
- "@\"BSServiceInitiatingConnection\"24@0:8@\"NSString\"16"
- "@\"BSServiceInitiatingConnection\"32@0:8@\"NSString\"16@\"BSServiceInitiatingConnectionMultiplexer\"24"
- "@\"BSServiceInitiatingConnection\"32@0:8@\"NSString\"16^B24"
- "@\"CADisplay\""
- "@\"CADisplay\"16@0:8"
- "@\"CAFenceHandle\""
- "@\"FBSSystemService\""
- "@\"NSArray\""
- "@\"NSArray<__BKSHIDKeyboardDeviceProperties__>\"24@0:8@\"NSNumber\"16"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSLock\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSSet<__BKSHIDEventPolicyObservation__>\"24@0:8@\"NSNumber\"16"
- "@\"NSSet<__BKSMousePointerDevice__>\"24@0:8@\"NSNumber\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSString\"24@0:8@\"_BKSHIDEventDeferringRuleIdentity\"16"
- "@\"NSString\"32@0:8@\"BKSHIDEventDescriptor\"16@\"BKSHIDEventSenderDescriptor\"24"
- "@\"NSString\"32@0:8@\"BKSHIDEventKeyCommand\"16@\"BKSHIDEventSenderDescriptor\"24"
- "@\"NSThread\""
- "@\"NSValue\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"_BKSCATransform3DContainer\"40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32"
- "@\"_BKSHIDEventAuthenticationKey\""
- "@\"_BKSHIDEventDeferringRuleIdentity\""
- "@\"_BKSTouchDeliveryPolicyConcreteServerInterface\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8I16I20"
- "@24@0:8I16i20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__IOHIDEvent=}16"
- "@24@0:8o^@16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@28@0:8I16I20I24"
- "@28@0:8I16S20S24"
- "@28@0:8I16d20"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@32@0:8@16q24"
- "@32@0:8^{__IOHIDEvent=}16^{__GSKeyboard=}24"
- "@32@0:8q16q24"
- "@32@0:8r*16q24"
- "@36@0:8@16I24@28"
- "@36@0:8i16@20@28"
- "@36@0:8{CGPoint=dd}16I32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16q24q32"
- "@40@0:8@?16@?24@?32"
- "@40@0:8I16@20C28@32"
- "@40@0:8^{__IOHIDEvent=}16^{__GSKeyboard=}24^q32"
- "@40@0:8q16{CGPoint=dd}24"
- "@44@0:8@16@24@32i40"
- "@44@0:8@16@24I32d36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32I40i44"
- "@48@0:8@16d24@32@?40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8q16@24B32I36I40Q44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40I48i52"
- "@64@0:8@16@24@32@40@48B56B60"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "@8@?0"
- "@?"
- "@?16@0:8"
- "@?<B@?>16@0:8"
- "Aq"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{__IOHIDEvent=}16"
- "B28@0:8@16I24"
- "B32@0:8@16^@24"
- "B32@0:8@16^i24"
- "B32@0:8I16I20^{__IOHIDEvent=}24"
- "B32@0:8^{__IOHIDEvent=}16^{__GSKeyboard=}24"
- "B32@0:8q16q24"
- "BKDitherEnabled"
- "BKIgnoreTetherPrefs"
- "BKSAbstractDefaults"
- "BKSAccelerometer"
- "BKSAlternateSystemApp"
- "BKSAlternateSystemAppClientProtocol"
- "BKSAlternateSystemAppServerProtocol"
- "BKSAnimationFenceHandle"
- "BKSBacklightFeatures"
- "BKSButtonHapticsController"
- "BKSButtonHapticsDefinition"
- "BKSContextRelativePoint"
- "BKSDefaults"
- "BKSDisplayArrangementItem"
- "BKSDisplayInterstitialRenderOverlayDismissAction"
- "BKSDisplayProgressIndicatorProperties"
- "BKSDisplayRenderOverlay"
- "BKSDisplayRenderOverlayDescribing"
- "BKSDisplayRenderOverlayDescriptor"
- "BKSDisplayRenderOverlayDismissAction"
- "BKSEventDeferringChainIdentity"
- "BKSEventFocusManager"
- "BKSExternalDefaults"
- "BKSHIDAuthenticatedKeyCommandSpecification"
- "BKSHIDEventAuthenticationMessage"
- "BKSHIDEventAuthenticationOriginator"
- "BKSHIDEventBaseAttributeSubsetProviding"
- "BKSHIDEventBaseAttributes"
- "BKSHIDEventBiometricDescriptor"
- "BKSHIDEventCollectionDescriptor"
- "BKSHIDEventDeferringChainObserverPredicate"
- "BKSHIDEventDeferringChainObserverPredicate cannot be subclassed"
- "BKSHIDEventDeferringChainObserverPredicate.m"
- "BKSHIDEventDeferringChangeBasis"
- "BKSHIDEventDeferringConstraint"
- "BKSHIDEventDeferringConstraintAssertion"
- "BKSHIDEventDeferringEnvironment"
- "BKSHIDEventDeferringModality"
- "BKSHIDEventDeferringModalityAssertion"
- "BKSHIDEventDeferringObserving"
- "BKSHIDEventDeferringPredicate"
- "BKSHIDEventDeferringResolution"
- "BKSHIDEventDeferringRule"
- "BKSHIDEventDeferringSelectionChangeRequest"
- "BKSHIDEventDeferringSelectionPathIdentifier"
- "BKSHIDEventDeferringSelectionPathSymbol"
- "BKSHIDEventDeferringSelectionTarget"
- "BKSHIDEventDeferringTarget"
- "BKSHIDEventDeferringToken"
- "BKSHIDEventDeliveryChain"
- "BKSHIDEventDeliveryChainObserver"
- "BKSHIDEventDeliveryManager"
- "BKSHIDEventDeliveryManagerClientInterface"
- "BKSHIDEventDeliveryManagerServerInterface"
- "BKSHIDEventDeliveryPolicy"
- "BKSHIDEventDeliveryPolicyObserver"
- "BKSHIDEventDeliveryRuleChangeTransaction"
- "BKSHIDEventDeliveryRuleWrapper"
- "BKSHIDEventDescriptor"
- "BKSHIDEventDigitizerAttributes"
- "BKSHIDEventDigitizerPathAttributes"
- "BKSHIDEventDiscreteDispatchingPredicate"
- "BKSHIDEventDiscreteDispatchingRoot"
- "BKSHIDEventDiscreteDispatchingRule"
- "BKSHIDEventDispatchingTarget"
- "BKSHIDEventDisplay"
- "BKSHIDEventGenericGestureDescriptor"
- "BKSHIDEventHitTestClientContext"
- "BKSHIDEventHitTestLayerInformation"
- "BKSHIDEventKeyCommand"
- "BKSHIDEventKeyCommandDescriptor"
- "BKSHIDEventKeyCommandDispatchingRoot"
- "BKSHIDEventKeyCommandsDispatchingPredicate"
- "BKSHIDEventKeyCommandsDispatchingRule"
- "BKSHIDEventKeyCommandsRegistration"
- "BKSHIDEventKeyboardAttributes"
- "BKSHIDEventKeyboardDescriptor"
- "BKSHIDEventObserver"
- "BKSHIDEventObserver - connection activation"
- "BKSHIDEventObserver - connection interruption"
- "BKSHIDEventObserver invalidated - backboardd must have unloaded, exiting…"
- "BKSHIDEventObserverClientInterface"
- "BKSHIDEventObserverServerInterface"
- "BKSHIDEventPointerAttributes"
- "BKSHIDEventPolicyObservation"
- "BKSHIDEventProvenance"
- "BKSHIDEventProximityAttributes"
- "BKSHIDEventRedirectAttributes"
- "BKSHIDEventSenderDescriptor"
- "BKSHIDEventSenderSpecificDescriptor"
- "BKSHIDEventSimpleProvenance"
- "BKSHIDEventSimpleProvenanceOriginator"
- "BKSHIDEventSmartCoverAttributes"
- "BKSHIDEventUnitTestableProvenance"
- "BKSHIDEventUsagePairDescriptor"
- "BKSHIDEventVendorDefinedDescriptor"
- "BKSHIDHapticFeedbackRequest"
- "BKSHIDKeyboardDevice"
- "BKSHIDKeyboardDeviceProperties"
- "BKSHIDKeyboardDevicePropertiesProviding"
- "BKSHIDKeyboardService"
- "BKSHIDServiceConnectionFactory"
- "BKSHIDTouchRoutingPolicy"
- "BKSHIDUISensorCharacteristics"
- "BKSHIDUISensorMode"
- "BKSHIDUISensorMode suppress mode changes"
- "BKSHIDUISensorService"
- "BKSHitTestRegion"
- "BKSIAPDefaults"
- "BKSInsecureDrawingAction"
- "BKSKeyboardDefaults"
- "BKSKeyboardServiceClientToServerIPC"
- "BKSKeyboardServiceServerToClientIPC"
- "BKSLocalDefaults"
- "BKSLockdownDefaults"
- "BKSMousePointerDevice"
- "BKSMousePointerDeviceObserverInfo"
- "BKSMousePointerDevicePreferences"
- "BKSMousePointerEventGlobalRoute"
- "BKSMousePointerGlobalContextOptions"
- "BKSMousePointerPerDisplayInfo"
- "BKSMousePointerPreferencesObserverInfo"
- "BKSMousePointerService"
- "BKSMousePointerServiceClientToServerInterface"
- "BKSMousePointerServiceServerToClientInterface"
- "BKSMousePointerServiceSessionSpecification"
- "BKSMousePointerSuppressionAssertionDescriptor"
- "BKSMutableEventDeferringChainIdentity"
- "BKSMutableHIDEventAuthenticationMessage"
- "BKSMutableHIDEventDeferringChainObserverPredicate"
- "BKSMutableHIDEventDeferringConstraint"
- "BKSMutableHIDEventDeferringConstraintAssertion"
- "BKSMutableHIDEventDeferringModality"
- "BKSMutableHIDEventDeferringModalityAssertion"
- "BKSMutableHIDEventDeferringPredicate"
- "BKSMutableHIDEventDeferringResolution"
- "BKSMutableHIDEventDeferringSelectionChangeRequest"
- "BKSMutableHIDEventDeferringSelectionTarget"
- "BKSMutableHIDEventDeferringTarget"
- "BKSMutableHIDEventDiscreteDispatchingPredicate"
- "BKSMutableHIDEventHitTestLayerInformation"
- "BKSMutableHIDEventKeyCommandsDispatchingPredicate"
- "BKSMutableHIDEventKeyCommandsRegistration"
- "BKSMutableHIDEventPolicyObservation"
- "BKSMutableHIDEventSenderDescriptor"
- "BKSMutableHIDEventSimpleProvenance"
- "BKSMutableHIDHapticFeedbackRequest"
- "BKSMutableHIDKeyboardDeviceProperties"
- "BKSMutableHIDUISensorCharacteristics"
- "BKSMutableHIDUISensorMode"
- "BKSMutableMousePointerEventGlobalRoute"
- "BKSMutableMousePointerGlobalContextOptions"
- "BKSMutableProximityEvent"
- "BKSMutableTouchAuthenticationSpecification"
- "BKSMutableTouchHitTestFilterParameters"
- "BKSMutableWindowServerHitTestSecurityAnalysis"
- "BKSPersistentConnectionDefaults"
- "BKSProximityDetectionMaskChangeEvent"
- "BKSProximitySensorClient_IPC"
- "BKSProximitySensorServer_IPC"
- "BKSProximitySensorService"
- "BKSRestartAction"
- "BKSSceneHostRegistration"
- "BKSSceneHostSettings"
- "BKSSecureModeViolation"
- "BKSSimplerAssertion"
- "BKSSimplerAssertion.m"
- "BKSSpringBoardDefaults"
- "BKSSystemGesturesTouchStreamPolicy"
- "BKSSystemService"
- "BKSSystemShellClientInterface"
- "BKSSystemShellControlClientInterface"
- "BKSSystemShellControlServerInterface"
- "BKSSystemShellControlService"
- "BKSSystemShellDataMigrationCheckInClientInterface"
- "BKSSystemShellDataMigrationCheckInServerInterface"
- "BKSSystemShellServerInterface"
- "BKSSystemShellService"
- "BKSSystemShellServiceConfiguration"
- "BKSTouchAnnotation"
- "BKSTouchAnnotationController"
- "BKSTouchAuthenticationSpecification"
- "BKSTouchDeliveryObservationService"
- "BKSTouchDeliveryObservationService_IPC"
- "BKSTouchDeliveryObserving_IPC"
- "BKSTouchDeliveryPolicyAssertion"
- "BKSTouchDeliveryPolicyServerInterface"
- "BKSTouchDeliveryUpdate"
- "BKSTouchEventClient_IPC"
- "BKSTouchEventServer_IPC"
- "BKSTouchEventService"
- "BKSTouchHitTestFilterParameters"
- "BKSTouchStream"
- "BKSTouchStreamPolicy"
- "BKSWatchdogServerWrapper"
- "BKSWindowServerHitTestSecurityAnalysis"
- "BOOL BKSHIDEventDigitizerDetachTouches(NSArray<NSNumber *> *__strong _Nonnull, uint32_t, BKSHIDTouchRoutingPolicy *__strong _Nonnull, CGPoint)"
- "BSDescriptionProviding"
- "BSDescriptionStreamable"
- "BSDescriptionStreaming"
- "BSInvalidatable"
- "BSProtobufSerializable"
- "BSSettings"
- "BSXPCCoding"
- "BSXPCSecureCoding"
- "C"
- "C16@0:8"
- "CAPort"
- "CATransform3DValue"
- "Client code must invalidate <%@:%p> (%@) before dealloc"
- "DASClientToServiceProtocol"
- "EnableTetheredDisplayPortMode"
- "Error detaching touches: 0x%X"
- "Error encoding policy: %{public}@"
- "Error encoding policy: %{public}@ for touches with userIdentifier:%X"
- "Error setting touch routing policy:0x%X for touches with userIdentifier:%X"
- "I16@0:8"
- "Mach IPC error getting UI sensor characteristics: 0x%x"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCConnectionWithEndpoint:configurator:"
- "Q16@0:8"
- "Resetting user event timer to %{public}@ with duration %gs"
- "S"
- "S16@0:8"
- "SimulateRedGreenPhoneButton"
- "T#,R"
- "T@\"<BKSAccelerometerDelegate>\",W,N,V_delegate"
- "T@\"<BKSAlternateSystemAppDelegate>\",W,N,V_delegate"
- "T@\"<BKSHIDEventDeferringSelectionPathSymbol>\",&,D,N"
- "T@\"<BKSHIDEventDeferringSelectionPathSymbol>\",R,N"
- "T@\"<BKSHIDEventDeliveryChainObserving>\",&,N,V_observingClient"
- "T@\"<BKSHIDEventProvenance>\",&,N"
- "T@\"<BKSHIDEventProvenance>\",R,N,V_eventProvenance"
- "T@\"<BKSMousePointerDeviceObserver>\",&,N,V_observer"
- "T@\"<BKSMousePointerPreferencesObserver>\",W,N,V_observer"
- "T@\"BKSDisplayProgressIndicatorProperties\",&,N,V_progressIndicatorProperties"
- "T@\"BKSDisplayProgressIndicatorProperties\",R,N"
- "T@\"BKSDisplayRenderOverlayDescriptor\",R,N"
- "T@\"BKSDisplayRenderOverlayDescriptor\",R,N,G_descriptor,V_descriptor"
- "T@\"BKSEventDeferringChainIdentity\",&,N,V_requestedChainIdentity"
- "T@\"BKSEventDeferringChainIdentity\",R,N"
- "T@\"BKSEventDeferringChainIdentity\",R,N,V_identity"
- "T@\"BKSHIDEventAuthenticationMessage\",&,N,V_authenticationMessage"
- "T@\"BKSHIDEventDeferringChangeBasis\",&,D,N"
- "T@\"BKSHIDEventDeferringChangeBasis\",R,N"
- "T@\"BKSHIDEventDeferringConstraint\",&,D,N"
- "T@\"BKSHIDEventDeferringConstraint\",R,N"
- "T@\"BKSHIDEventDeferringEnvironment\",&,D,N"
- "T@\"BKSHIDEventDeferringEnvironment\",&,N,V_environment"
- "T@\"BKSHIDEventDeferringEnvironment\",C,D,N"
- "T@\"BKSHIDEventDeferringEnvironment\",C,N"
- "T@\"BKSHIDEventDeferringEnvironment\",R,C,N,V_deferringEnvironment"
- "T@\"BKSHIDEventDeferringEnvironment\",R,C,N,V_environment"
- "T@\"BKSHIDEventDeferringEnvironment\",R,N"
- "T@\"BKSHIDEventDeferringModality\",&,D,N"
- "T@\"BKSHIDEventDeferringModality\",R,N"
- "T@\"BKSHIDEventDeferringPredicate\",R,C,N,V_predicate"
- "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",&,D,N"
- "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",C,N"
- "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,C,N,V_selectionPathIdentifier"
- "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,N"
- "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,N,V_selectionPath"
- "T@\"BKSHIDEventDeferringSelectionTarget\",&,D,N"
- "T@\"BKSHIDEventDeferringSelectionTarget\",R,N"
- "T@\"BKSHIDEventDeferringTarget\",&,D,N"
- "T@\"BKSHIDEventDeferringTarget\",R,C,N,V_target"
- "T@\"BKSHIDEventDeferringTarget\",R,N"
- "T@\"BKSHIDEventDeferringToken\",&,D,N"
- "T@\"BKSHIDEventDeferringToken\",&,N,V_token"
- "T@\"BKSHIDEventDeferringToken\",C,D,N"
- "T@\"BKSHIDEventDeferringToken\",C,N"
- "T@\"BKSHIDEventDeferringToken\",R,C,N,V_deferringToken"
- "T@\"BKSHIDEventDeferringToken\",R,C,N,V_token"
- "T@\"BKSHIDEventDeferringToken\",R,N"
- "T@\"BKSHIDEventDeliveryChainObserver\",&,N,V_observerInterface"
- "T@\"BKSHIDEventDeliveryPolicy\",R,N"
- "T@\"BKSHIDEventDescriptor\",&,N,V_sourceDescriptor"
- "T@\"BKSHIDEventDiscreteDispatchingPredicate\",R,C,N,V_predicate"
- "T@\"BKSHIDEventDispatchingTarget\",&,D,N"
- "T@\"BKSHIDEventDispatchingTarget\",R,C,N,V_target"
- "T@\"BKSHIDEventDispatchingTarget\",R,N,V_dispatchingTarget"
- "T@\"BKSHIDEventDisplay\",&,D,N"
- "T@\"BKSHIDEventDisplay\",&,N,V_display"
- "T@\"BKSHIDEventDisplay\",C,D,N"
- "T@\"BKSHIDEventDisplay\",C,N"
- "T@\"BKSHIDEventDisplay\",R,C,N,V_display"
- "T@\"BKSHIDEventDisplay\",R,N"
- "T@\"BKSHIDEventDisplay\",R,N,V_associatedDisplay"
- "T@\"BKSHIDEventDisplay\",R,N,V_compatibilityDisplay"
- "T@\"BKSHIDEventHitTestLayerInformation\",&,D,N"
- "T@\"BKSHIDEventHitTestLayerInformation\",R,N,V_hitTestInformationFromEndEvent"
- "T@\"BKSHIDEventHitTestLayerInformation\",R,N,V_hitTestInformationFromStartEvent"
- "T@\"BKSHIDEventKeyCommand\",&,N,V_keyCommand"
- "T@\"BKSHIDEventKeyCommandsDispatchingPredicate\",R,C,N,V_predicate"
- "T@\"BKSHIDEventKeyCommandsDispatchingRule\",R,C,N"
- "T@\"BKSHIDEventSenderDescriptor\",R,C,N,V_senderDescriptor"
- "T@\"BKSHIDUISensorCharacteristics\",R,N"
- "T@\"BKSIAPDefaults\",R,&,N"
- "T@\"BKSKeyboardDefaults\",R,&,N"
- "T@\"BKSLockdownDefaults\",R,&,N"
- "T@\"BKSMousePointerDevicePreferences\",C"
- "T@\"BKSMousePointerGlobalContextOptions\",&,D,N"
- "T@\"BKSMousePointerGlobalContextOptions\",R,N"
- "T@\"BKSPersistentConnectionDefaults\",R,&,N"
- "T@\"BKSSpringBoardDefaults\",R,&,N"
- "T@\"BKSWindowServerHitTestSecurityAnalysis\",&,N,V_hitTestSecurityAnalysis"
- "T@\"BKSWindowServerHitTestSecurityAnalysis\",&,N,V_securityAnalysis"
- "T@\"BSCompoundAssertion\",&,N,V_globalEventsAssertion"
- "T@\"BSCompoundAssertion\",&,N,V_pointerSuppressionAssertion"
- "T@\"BSMutableIntegerMap\",&,N,V_touchIdentifierToObserverLists"
- "T@\"BSMutableSettings\",&,N,V_settings"
- "T@\"BSServiceInitiatingConnection\",&,N,V_connection"
- "T@\"BSServiceInterface\",R,C,N"
- "T@\"BSServiceQuality\",R,C,N"
- "T@\"BSSettings\",R,N,G_BSSettings,V_settings"
- "T@\"CADisplay\",R,&,N"
- "T@\"CADisplay\",R,N,V_display"
- "T@\"NSArray\",&,D,N"
- "T@\"NSArray\",&,N,V_pathAttributes"
- "T@\"NSArray\",C,D,N"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",C,N,V_bufferingPredicates"
- "T@\"NSArray\",C,N,V_constraintAssertions"
- "T@\"NSArray\",C,N,V_contextIds"
- "T@\"NSArray\",C,N,V_deferringRules"
- "T@\"NSArray\",C,N,V_discreteDispatchingRules"
- "T@\"NSArray\",C,N,V_hitTestContexts"
- "T@\"NSArray\",C,N,V_keyCommandDispatchingRules"
- "T@\"NSArray\",C,N,V_keyCommandsRegistrations"
- "T@\"NSArray\",C,N,V_modalityAssertions"
- "T@\"NSArray\",C,N,V_selectionRequests"
- "T@\"NSArray\",D,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_deferringPath"
- "T@\"NSArray\",R,C,N,V_targets"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_policies"
- "T@\"NSArray\",W,D,N"
- "T@\"NSData\",&,D,N"
- "T@\"NSData\",C,D,N"
- "T@\"NSData\",R,C,D,N"
- "T@\"NSData\",R,C,N"
- "T@\"NSData\",R,N"
- "T@\"NSDictionary\",&,D,N"
- "T@\"NSDictionary\",C,N,V_layerNamesByContext"
- "T@\"NSDictionary\",R,N"
- "T@\"NSHashTable\",&,N,V_generalObservers"
- "T@\"NSMapTable\",&,N,V_observersToTouchIdentifiers"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSNumber\",&,N,V_processId"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_stateChangeSemaphore"
- "T@\"NSObject<OS_xpc_object>\",&,N"
- "T@\"NSSet\",&,N,V_previouslyRoutedContextIDs"
- "T@\"NSSet\",&,N,V_visibleDevices"
- "T@\"NSSet\",C,D,N"
- "T@\"NSSet\",R,C,D,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,C,N,V_descriptors"
- "T@\"NSSet\",R,C,N,V_displays"
- "T@\"NSSet\",R,C,N,V_keyCommands"
- "T@\"NSSet\",R,C,N,V_modalities"
- "T@\"NSSet\",R,C,N,V_multitouchHostStateKeys"
- "T@\"NSSet\",R,C,N,V_proximityHostStateKeys"
- "T@\"NSSet\",R,C,N,V_restrictedToEventDescriptors"
- "T@\"NSSet\",R,C,N,V_senderDescriptors"
- "T@\"NSSet\",R,D,N"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",&,N,V_commandModifiedInput"
- "T@\"NSString\",&,N,V_shiftModifiedInput"
- "T@\"NSString\",&,N,V_unmodifiedInput"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N,V_bundleId"
- "T@\"NSString\",C,N,V_displayUUID"
- "T@\"NSString\",C,N,V_manufacturerName"
- "T@\"NSString\",C,N,V_preferenceKey"
- "T@\"NSString\",C,N,V_productName"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",C,N,V_uniqueIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,D,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_displayUUID"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_processDescription"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSString\",R,C,N,V_relativeDisplayUUID"
- "T@\"NSString\",R,D,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_input"
- "T@\"NSString\",W,D,N"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"_BKSHIDEventDeferringRuleIdentity\",R,C,N,V_identity"
- "T@\"_BKSTouchDeliveryPolicyConcreteServerInterface\",&,N,V_server"
- "T@,R,C,N,V_payload"
- "T@?,C,N"
- "T@?,C,N,V_errorHandler"
- "TB,D,N"
- "TB,D,N,GisALSEnabled"
- "TB,D,N,GisAuthenticated"
- "TB,D,N,GisDigitizerSignpostsEnabled"
- "TB,D,N,GisDitheringEnabled"
- "TB,D,N,GisEventBufferingEnabled"
- "TB,D,N,GisFinalStringToken"
- "TB,D,N,GisSqueezeForSystemShortcutEnabled"
- "TB,D,N,GisSteveNoteOverscanEnabled"
- "TB,D,N,GisSteveNoteRotationEnabled"
- "TB,N"
- "TB,N,GisInterstitial,S_setInterstitial:,V_interstitial"
- "TB,N,GshouldAvoidHitTesting"
- "TB,N,V_allowWirelessExtendedDisplay"
- "TB,N,V_backgroundStatisticsValid"
- "TB,N,V_containsEndOfChain"
- "TB,N,V_disableExtendedDisplayByDefault"
- "TB,N,V_disableFeatures"
- "TB,N,V_disableStudyLogALSLogging"
- "TB,N,V_disableStudyLogAccelerometerLogging"
- "TB,N,V_disableStudyLogGyroLogging"
- "TB,N,V_enableNaturalScrolling"
- "TB,N,V_enableTapToClick"
- "TB,N,V_enableTwoFingerSecondaryClick"
- "TB,N,V_hasVirtualMouseButtons"
- "TB,N,V_isDetached"
- "TB,N,V_lockBacklight"
- "TB,N,V_orientationEventsEnabled"
- "TB,N,V_passiveOrientationEvents"
- "TB,N,V_representsHomeButton"
- "TB,N,V_shouldSendAmbiguityRecommendations"
- "TB,N,V_stateChangeWaiter"
- "TB,N,V_supportsDragLock"
- "TB,N,V_supportsLightClick"
- "TB,N,V_supportsSystemHaptics"
- "TB,N,V_systemGestureStateChange"
- "TB,N,V_systemGesturesPossible"
- "TB,R"
- "TB,R,D,N"
- "TB,R,N"
- "TB,R,N,GisAuthenticated,V_authenticated"
- "TB,R,N,GisEmpty"
- "TB,R,N,GisFinalStringToken,V_finalStringToken"
- "TB,R,N,GisInterstitial"
- "TB,R,N,GisRestrictedToSystemShell"
- "TB,R,N,GisUsable"
- "TB,R,N,V_containsSubset"
- "TB,R,N,V_isBuffer"
- "TB,R,N,V_registrantEntitled"
- "TC,D,N"
- "TC,N,V_locus"
- "TC,N,V_pointerEdgeMask"
- "TC,N,V_touchStreamIdentifier"
- "TC,R,D,N"
- "TC,R,N"
- "TI,D,N"
- "TI,N,V_GSModifierState"
- "TI,N,V_contextID"
- "TI,N,V_touchIdentifier"
- "TI,N,V_userIdentifier"
- "TI,R,D,N"
- "TI,R,N"
- "TI,R,N,V_biometricEventType"
- "TI,R,N,V_childContextId"
- "TI,R,N,V_contextID"
- "TI,R,N,V_contextId"
- "TI,R,N,V_edge"
- "TI,R,N,V_eventType"
- "TI,R,N,V_genericGestureType"
- "TI,R,N,V_hidEventType"
- "TI,R,N,V_hostContextId"
- "TI,R,N,V_primaryPage"
- "TI,R,N,V_primaryUsage"
- "TI,R,N,V_secureName"
- "TI,R,N,V_seed"
- "TI,R,N,V_slotID"
- "TI,R,N,V_targetContextID"
- "TI,R,N,V_targetSlotID"
- "TI,R,N,V_touchIdentifier"
- "TI,R,V_page"
- "TI,R,V_usage"
- "TI,V_reference"
- "TQ,D,N"
- "TQ,N,V_contentsMask"
- "TQ,N,V_context"
- "TQ,N,V_mode"
- "TQ,N,V_suppressionOptions"
- "TQ,R"
- "TQ,R,D,N"
- "TQ,R,N"
- "TQ,R,N,V_authenticationMessageContext"
- "TQ,R,N,V_context"
- "TQ,R,N,V_hitTestInformationMask"
- "TQ,R,N,V_originIdentifier"
- "TQ,R,N,V_predicateEventTypeMask"
- "TQ,R,N,V_senderID"
- "TQ,R,N,V_timestamp"
- "TQ,R,N,V_timetamp"
- "TQ,R,V_senderID"
- "TS,D,N"
- "TS,N,V_options"
- "TS,N,V_teleportState"
- "Td,D,N"
- "Td,N"
- "Td,N,V_initialTouchTimestamp"
- "Td,N,V_maximumPositionZ"
- "Td,N,V_updateInterval"
- "Td,R,N"
- "Td,R,N,V_initialTouchTimestamp"
- "Td,R,N,V_longPressTimeout"
- "Td,R,N,V_offset"
- "Tf,D,N"
- "Tf,N,V_fixedBrightnessLevelWhileDisabled"
- "Tf,N,V_fixedBrightnessNitsWhileDisabled"
- "Tf,N,V_maximumForce"
- "Tf,N,V_pointerAccelerationFactor"
- "Tf,N,V_scrollAccelerationFactor"
- "Tf,N,V_xThreshold"
- "Tf,N,V_yThreshold"
- "Tf,N,V_zGradient"
- "Tf,N,V_zThreshold"
- "Tf,R,N"
- "Tf,R,N,V_backgroundStatisticsFailingContrast"
- "Tf,R,N,V_backgroundStatisticsForeground"
- "Tf,R,N,V_backgroundStatisticsPassingContrast"
- "Ti,D,N"
- "Ti,N,V_pid"
- "Ti,N,V_proximityDetectionMode"
- "Ti,N,V_smartCoverState"
- "Ti,N,V_source"
- "Ti,N,V_wakeAnimationStyle"
- "Ti,R,N"
- "Ti,R,N,V_pid"
- "Touches not found:%{public}@"
- "Tq,D,N"
- "Tq,N"
- "Tq,N,V_activeModifiers"
- "Tq,N,V_buttonConfigurationForHardwareButtonMice"
- "Tq,N,V_buttonConfigurationForVirtualButtonMice"
- "Tq,N,V_clickHapticStrength"
- "Tq,N,V_contextMove"
- "Tq,N,V_contextType"
- "Tq,N,V_doubleTapDragMode"
- "Tq,N,V_fingerDownCount"
- "Tq,N,V_hitTestContextCategory"
- "Tq,N,V_interfaceOrientation"
- "Tq,N,V_pathIndex"
- "Tq,N,V_sceneTouchBehavior"
- "Tq,N,V_state"
- "Tq,N,V_type"
- "Tq,N,V_usagePage"
- "Tq,R,D,N"
- "Tq,R,N"
- "Tq,R,N,GisLongPressEnabled"
- "Tq,R,N,V_deferringPolicyStatus"
- "Tq,R,N,V_finalSampleEvent"
- "Tq,R,N,V_hardwareType"
- "Tq,R,N,V_identifier"
- "Tq,R,N,V_initialSampleEvent"
- "Tq,R,N,V_keyCode"
- "Tq,R,N,V_modifierFlags"
- "Tq,R,N,V_secureNameStatus"
- "Tq,R,N,V_style"
- "Tq,R,N,V_touchBehavior"
- "Tq,R,N,V_versionedPID"
- "T{?=SSSS},D,N"
- "T{?=SSSS},R,N"
- "T{CATransform3D=dddddddddddddddd},D,N"
- "T{CATransform3D=dddddddddddddddd},N,V_transform"
- "T{CATransform3D=dddddddddddddddd},R,N"
- "T{CGPoint=dd},N,V_acceleratedRelativePosition"
- "T{CGPoint=dd},N,V_hitTestLocation"
- "T{CGPoint=dd},N,V_preciseLocation"
- "T{CGPoint=dd},N,V_unacceleratedRelativePosition"
- "T{CGPoint=dd},R,N,V_point"
- "T{CGPoint=dd},R,N,V_position"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_exclusiveTouchNormalizedSubRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,G_exclusiveTouchNormalizedSubRectInReferenceSpace,V_exclusiveTouchNormalizedSubRectInReferenceSpace"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rect"
- "T{CGSize=dd},N,V_digitizerSurfaceSize"
- "UTF8String"
- "UUID"
- "Unable to get a connection to the hid event observer server! No observation will be allowed!!!"
- "Vv16@0:8"
- "Vv24@0:8@\"BKSHIDEventDeliveryRuleChangeTransaction\"16"
- "Vv24@0:8@\"BKSMousePointerDevicePreferences\"16"
- "Vv24@0:8@\"BKSProximityDetectionMaskChangeEvent\"16"
- "Vv24@0:8@\"NSArray<__BKSHIDEventDeliveryChain__>\"16"
- "Vv24@0:8@\"NSNumber\"16"
- "Vv24@0:8@\"NSSet<__BKSHIDEventPolicyObservation__>\"16"
- "Vv24@0:8@\"NSSet<__BKSMousePointerDevice__>\"16"
- "Vv24@0:8@\"NSValue\"16"
- "Vv24@0:8@16"
- "Vv28@0:8@16I24"
- "Vv32@0:8@\"BKSMousePointerDevicePreferences\"16@\"BKSMousePointerDevice\"24"
- "Vv32@0:8@\"BKSSceneHostSettings\"16@\"NSNumber\"24"
- "Vv32@0:8@\"NSArray<__BKSHIDKeyboardDeviceProperties__>\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSArray<__BKSTouchDeliveryUpdate__>\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSNumber\"16@\"NSNumber\"24"
- "Vv32@0:8@\"NSSet<__BKSMousePointerEventGlobalRoute__>\"16@\"NSString\"24"
- "Vv32@0:8@\"NSString\"16@\"NSNumber\"24"
- "Vv32@0:8@\"NSUUID\"16@\"NSString\"24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"NSValue\"16@\"NSString\"24@\"BSAnimationSettings\"32"
- "Vv40@0:8@16@24@32"
- "Vv48@0:8@\"BKSContextRelativePoint\"16@\"NSSet<__BKSHIDEventHitTestClientContext__>\"24@\"NSString\"32@?<v@?@\"NSArray<__BKSHIDEventHitTestClientContext__>\"@\"NSArray<__NSValue__>\"@\"NSError\">40"
- "Vv48@0:8@\"BKSContextRelativePoint\"16@\"NSString\"24@\"BSAnimationSettings\"32@\"NSNumber\"40"
- "Vv48@0:8@16@24@32@40"
- "Vv48@0:8@16@24@32@?40"
- "Vv56@0:8@\"BKSContextRelativePoint\"16@\"BKSContextRelativePoint\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48"
- "Vv56@0:8@\"NSUUID\"16@\"NSString\"24@\"BKSContextRelativePoint\"32@\"NSString\"40@\"NSNumber\"48"
- "Vv56@0:8@16@24@32@40@48"
- "^{_NSZone=}16@0:8"
- "^{__CFBoolean=}"
- "^{__CFRunLoop=}"
- "^{__CFRunLoopSource=}"
- "_BKChainObserverContainer"
- "_BKSCATransform3DContainer"
- "_BKSCancelTouchesTouchDeliveryPolicy"
- "_BKSCloneMirroringModeRequest"
- "_BKSCombinedTouchDeliveryPolicy"
- "_BKSHIDCAContextEventDeferringToken"
- "_BKSHIDCGSConnectionIDEventDeferringToken"
- "_BKSHIDCGSWindowIDEventDeferringToken"
- "_BKSHIDEventAuthenticationKey"
- "_BKSHIDEventDeferringRuleIdentity"
- "_BKSHIDKeyboardDeviceClientProxy"
- "_BKSHIDStringIdentifierEventDeferringToken"
- "_BKSLocallyOwnedTouchAuthenticationAssertion"
- "_BKSShareTouchesTouchDeliveryPolicy"
- "_BKSTouchDeliveryPolicyConcreteServerInterface"
- "_BKSTouchDeliveryPolicyConcreteServerReference"
- "_BKSWatchdogGetIsAlive:isAlive:timeout:"
- "_BSSettings"
- "_accelerometerEventsRunLoop"
- "_accelerometerEventsSource"
- "_activateServerConnection"
- "_activateServerConnection:"
- "_activateServerConnectionWithIdleSleepInterval:"
- "_allowWirelessExtendedDisplay"
- "_appendDescriptionOfKeyCommandCollection:toStream:"
- "_appendDescriptionToFormatterCore:"
- "_appendKeyWithoutModifiersToDescriptionTarget:keyCodeString:"
- "_appendPropertiesCommon:"
- "_assertionEndpoint"
- "_asyncObserverCalloutQueue"
- "_asyncResultQueue"
- "_attachedDevices"
- "_authentic"
- "_backgroundStatisticsValid"
- "_basis"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_biometricEventType"
- "_bsServiceDispatchQueue"
- "_bufferingPredicates"
- "_bundleId"
- "_caFence"
- "_calloutQueue"
- "_chainIdentity"
- "_checkIn"
- "_checkInStatus"
- "_checkInWaitingForDataMigration:"
- "_checkOut"
- "_childContextId"
- "_classForAttributeType:"
- "_classesRequiredToDecode"
- "_commandModifiedInput"
- "_comparisonScore"
- "_configurationFinished"
- "_connectToRemoteServiceIfNeeded"
- "_connectToService"
- "_connectToTouchDeliveryService"
- "_connection"
- "_connectionLock"
- "_connectionQueue"
- "_constraint"
- "_constraintAssertions"
- "_contentsMask"
- "_contextIDsForAXZoom"
- "_contextId"
- "_contextIds"
- "_dataProtobufEncoded"
- "_deferringEnvironment"
- "_deferringPolicyStatus"
- "_deferringRules"
- "_deferringToken"
- "_delegate"
- "_descriptionForKeyCommandCollection:"
- "_descriptor"
- "_descriptors"
- "_detectionMask"
- "_device"
- "_deviceConnectionObservers"
- "_disableExtendedDisplayByDefault"
- "_disableStudyLogALSLogging"
- "_disableStudyLogAccelerometerLogging"
- "_disableStudyLogGyroLogging"
- "_discreteDispatchingRules"
- "_dispatchingTarget"
- "_displayUUID"
- "_displayUUIDToPerDisplayInfo"
- "_edge"
- "_errorHandler"
- "_eventAttributeType"
- "_eventProvenance"
- "_exclusiveTouchNormalizedSubRectInReferenceSpace"
- "_executeDescriptionFetch:result:"
- "_fbsSystemService"
- "_finalStringToken"
- "_finalStringTokenInChain"
- "_fixMissingButtonConfigurations"
- "_forTesting"
- "_fuzzyDescriptors"
- "_generalObservers"
- "_genericGestureType"
- "_globalEventsAssertion"
- "_handleInterruptedConnection"
- "_handleInvalidatedConnection"
- "_hidEventType"
- "_hitTestFilterParameters"
- "_hmacContext"
- "_hmacInitialized"
- "_hostContextId"
- "_identifierDescription"
- "_identifierOfCAContext"
- "_identifierOfCGSConnection"
- "_identifierOfCGSWindow"
- "_idleSleepInterval"
- "_ignoreModalities"
- "_implicitFlushQueue"
- "_init"
- "_initCopyFrom:"
- "_initWithBSSettings:"
- "_initWithCAFenceHandle:"
- "_initWithCGSConnectionID:"
- "_initWithCGSWindowID:"
- "_initWithConnection:"
- "_initWithConnectionFactory:"
- "_initWithConnectionFactory:forTesting:"
- "_initWithCopyOf:"
- "_initWithDisplay:environment:versionedPID:pid:token:dispatchingTarget:"
- "_initWithDomain:"
- "_initWithEnvironment:display:token:"
- "_initWithEnvironment:token:keyCommands:"
- "_initWithEnvironment:token:selectionPath:pid:"
- "_initWithEventType:"
- "_initWithHardwareIdentifier:"
- "_initWithHardwareType:associatedDisplay:authenticated:primaryPage:primaryUsage:senderID:"
- "_initWithIdentifier:"
- "_initWithIdentifier:invalidationBlock:"
- "_initWithIdentifier:provenance:"
- "_initWithInput:keyCode:modifierFlags:"
- "_initWithName:displayUUID:"
- "_initWithObserver:"
- "_initWithPID:token:"
- "_initWithPage:usage:eventType:"
- "_initWithPidToContextInfoDictionary:"
- "_initWithPolicyObservation:"
- "_initWithPredicate:restrictedToEventDescriptors:target:reason:identity:"
- "_initWithPredicate:target:"
- "_initWithPredicate:targets:"
- "_initWithProperties:"
- "_initWithRect:exclusiveTouchNormalizedSubRect:"
- "_initWithSenderDescriptors:"
- "_initWithSourceDescriptors:descriptors:"
- "_initWithString:"
- "_initWithStyle:position:"
- "_input"
- "_interfaceOrientation"
- "_interstitial"
- "_invalid"
- "_invalidationBlock"
- "_isBuffer"
- "_isBuiltinDisplay"
- "_isDetached"
- "_isIdentifierOfCAContext"
- "_isIdentifierOfCGSConnection"
- "_isIdentifierOfCGSWindow"
- "_isKeyboardFocusEnvironment"
- "_isModifierKeyWithPage:usage:"
- "_isNonLaunchingServer"
- "_isNullDisplay"
- "_isObservingDeviceConnection"
- "_isObservingPreferences"
- "_isString"
- "_isSystemEnvironment"
- "_isWildcard"
- "_key"
- "_keyCode"
- "_keyCommand"
- "_keyCommandDispatchingRules"
- "_keyCommandsRegistrations"
- "_keyData"
- "_keyLastAccessTime"
- "_layerNamesByContext"
- "_lazy_iapDefaults"
- "_lazy_keyboardDefaults"
- "_lazy_lockdownDefaults"
- "_lazy_persistentConnectionDefaults"
- "_lazy_springBoardDefaults"
- "_lifetimeAssertion"
- "_listener"
- "_lock"
- "_lockBacklight"
- "_lock_allChainObserverPredicates"
- "_lock_appendDescriptionToStream:"
- "_lock_assertions"
- "_lock_bufferingPredicates"
- "_lock_bufferingSeed"
- "_lock_buildCurrentPolicy"
- "_lock_chainObserverContainers"
- "_lock_constraintAssertSeed"
- "_lock_constraintAsserts"
- "_lock_currentPolicy"
- "_lock_currentlyObserving"
- "_lock_deferringAssertionsToObservers"
- "_lock_deferringObservations"
- "_lock_deferringRules"
- "_lock_deferringSeed"
- "_lock_description"
- "_lock_disableObservation"
- "_lock_discreteDispatchingRoots"
- "_lock_discreteDispatchingSeed"
- "_lock_display"
- "_lock_effectivePolicyObservation"
- "_lock_enableObservation"
- "_lock_environment"
- "_lock_flushIfNeeded"
- "_lock_flushInitialStateToServer"
- "_lock_hasReceivedLatestDeferringObservationsFromServer"
- "_lock_identityToChainMatches"
- "_lock_implicitFlush"
- "_lock_implicitPreventFlushingAssertion"
- "_lock_keyCommandsDispatchingRoots"
- "_lock_keyCommandsDispatchingSeed"
- "_lock_keyCommandsRegistrationSeed"
- "_lock_keyCommandsRegistrations"
- "_lock_lastSentBufferingPredicates"
- "_lock_lastSentConstraintAsserts"
- "_lock_lastSentDeferringRules"
- "_lock_lastSentDiscreteDispatchingRoots"
- "_lock_lastSentKeyCommandsDispatchingRoots"
- "_lock_lastSentKeyCommandsRegistrations"
- "_lock_lastSentModalityAsserts"
- "_lock_lastSentSetOfKeyCommandsRegistrations"
- "_lock_modalityAssertSeed"
- "_lock_modalityAsserts"
- "_lock_needsFlush"
- "_lock_noteServerInterruption"
- "_lock_observations"
- "_lock_observers"
- "_lock_observingDetectionMaskChanges"
- "_lock_pendQuery:"
- "_lock_pendingQueriesToBeExecutedInsideLockOnceActivationHappens"
- "_lock_prevailingMode"
- "_lock_preventFlushingReasons"
- "_lock_preventFlushingSeed"
- "_lock_properties"
- "_lock_pushCurrentModeToServer"
- "_lock_remoteTargetSafeToMessage"
- "_lock_resetChainObserverPredicates"
- "_lock_selectionPathIdentifier"
- "_lock_selectionRequests"
- "_lock_senderIDToDevice"
- "_lock_stateDescription"
- "_lock_token"
- "_lock_transactionAssertionWithReason:"
- "_lock_updatePolicyWithBlock:"
- "_lock_waitingOnServerHandshake"
- "_locked_infoForDisplayUUID:createIfNeeded:"
- "_locked_pointingDevicesDidChange:"
- "_locked_reactivateConnection"
- "_locked_sendCurrentAssertionParameters:forDisplayUUID:"
- "_locked_serverTarget"
- "_locked_setMousePointerDeviceObservationEnabled:"
- "_locked_setMousePointerPreferencesObservationEnabled:"
- "_locked_updateEventRoutesFromContext:forDisplayUUID:"
- "_locked_updateObserver:withPointingDevices:"
- "_locked_updateServerWithPointerDeviceObservationState"
- "_locked_updateServerWithPreferencesObservationState"
- "_modality"
- "_modalityAssertions"
- "_mode"
- "_modeAssertion"
- "_modifierFlags"
- "_name"
- "_notifyAsyncObservers:didUpdatePolicy:"
- "_observer"
- "_observerAssertion"
- "_observerInterface"
- "_observers"
- "_observersToTouchIdentifiers"
- "_observingAssertion"
- "_observingClient"
- "_offset"
- "_orientationCheckToken"
- "_orientationDidChange"
- "_orientationEventsEnabled"
- "_orientationEventsThread"
- "_orientationNotificationsToken"
- "_orientationPort"
- "_overlayDescriptor"
- "_page:usage:matchesHIDEvent:"
- "_passiveOrientationEvents"
- "_pathIdentifier"
- "_payload"
- "_pinOnButtonDown"
- "_point"
- "_pointerSuppressionAssertion"
- "_policies"
- "_policyStatus"
- "_position"
- "_predicate"
- "_predicateEventTypeMask"
- "_preferencesObservers"
- "_prevailingMode:"
- "_previouslyRoutedContextIDs"
- "_processDescription"
- "_processId"
- "_processTouchEventDeliveryUpdate:"
- "_progressIndicatorProperties"
- "_properties"
- "_protobufDecodedFromData:"
- "_proxiesAssertion"
- "_queue"
- "_queue_addObserver:forTouchIdentifier:"
- "_queue_changeState:"
- "_queue_ensureConnection"
- "_queue_invalidate"
- "_queue_observersForTouchIdentifier:"
- "_queue_removeObserver:forTouchIdentifier:"
- "_queue_removeObserversForTouchIdentifier:"
- "_reference"
- "_registerForOrientationNotifications"
- "_registrationLock"
- "_registrationLock_registrationsByContextID"
- "_relativeDisplayUUID"
- "_replacePolicySpecificationObject:withObject:replaceIvarBlock:"
- "_replaceProperties:"
- "_repostAllRegistrations"
- "_representsHomeButton"
- "_requestedChainIdentity"
- "_restrictedToEventDescriptors"
- "_sanitizedInputForDescription"
- "_sceneHostSettings"
- "_seed"
- "_selectionPathIdentifier"
- "_selectionRequests"
- "_selectionTarget"
- "_server"
- "_serverWasRestarted"
- "_service"
- "_serviceConnection"
- "_setCheckInStatus:"
- "_setInterstitial:"
- "_setMultitouchSettingKey:enabled:"
- "_settingKeysAllowed:"
- "_settings"
- "_shiftModifiedInput"
- "_shouldMatchKeyCommandsForEvent:gsKeyboard:"
- "_shouldSendAmbiguityRecommendations"
- "_state"
- "_stateChangeSemaphore"
- "_stateChangeWaiter"
- "_store"
- "_string"
- "_stringRepresentation"
- "_style"
- "_substituteSingeltonForIdentifierString:"
- "_suppressMouseEvents"
- "_suppressionAssertion"
- "_suppressionOptions"
- "_syncServiceFlushState"
- "_target"
- "_targets"
- "_text"
- "_timetamp"
- "_touchBehavior"
- "_touchClientQueue"
- "_touchIdentifierToObserverLists"
- "_uniqueIdentifier"
- "_unlocked_serverTarget"
- "_unmodifiedInput"
- "_updateCCHmacContext:"
- "_updateInterval"
- "_updateOrientationServer"
- "_updateServerHitTestCategoryContextIDs"
- "_updateServerHitTestFilterParameters"
- "_usagePage"
- "_verifySignatureWithInternalKey:"
- "_visibleDevices"
- "_waitForDataMigration"
- "_waitForState:"
- "_watchdogPingBlock"
- "_withInternalKey:buildMessage:"
- "_xThreshold"
- "_yThreshold"
- "_zThreshold"
- "acceleratedRelativePositionX"
- "acceleratedRelativePositionY"
- "accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:"
- "accelerometer:didChangeDeviceOrientation:"
- "accelerometerEventsEnabled"
- "accessMachPort:"
- "acquireButtonDownPointerRepositionAssertionForReason:contextRelativePointerPosition:onDisplay:restrictingToPID:"
- "acquireButtonDownPointerRepositionAssertionWithUniqueIdentifier:forReason:contextRelativePointerPosition:onDisplay:restrictingToPID:"
- "acquireForReason:"
- "acquireForReason:withContext:"
- "actionWithOptions:"
- "activate"
- "activeInputModality"
- "addAuthenticationSpecifications:forReason:"
- "addChainObserver:"
- "addDeferringObserver:"
- "addFence:"
- "addField:"
- "addField:forTag:"
- "addKeyboardObserver:"
- "addObject:"
- "addObserver:"
- "addObserver:forReason:"
- "addObserver:forTouchIdentifier:"
- "addObservingClient:forChainObserver:"
- "addPointerDeviceObserver:"
- "addPointerPreferencesObserver:"
- "addRepeatingField:containsClass:"
- "addTouchAuthenticationSpecifications:forReason:"
- "addValue:"
- "allKeys"
- "allObjects"
- "allValues"
- "alloc"
- "allocWithZone:"
- "alternateSystemApp:didExitWithStatus:"
- "alternateSystemApp:didFailToLaunchWithError:"
- "alternateSystemApp:didTerminateWithSignal:"
- "alternateSystemAppDidLaunch:"
- "alternateSystemAppWithBundleID:didExitWithContext:"
- "alternateSystemAppWithBundleID:failedToOpenWithResult:"
- "alternateSystemAppWithBundleIDDidOpen:"
- "alternateSystemAppWithBundleIDDidTerminate:"
- "alwaysOnGesturesEnabled"
- "anyBuiltinTouchscreenDigitizer"
- "anyDigitizer"
- "appendArraySection:withName:multilinePrefix:skipIfEmpty:"
- "appendArraySection:withName:skipIfEmpty:objectTransformer:"
- "appendBodySectionWithName:block:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCGFloat:"
- "appendCGFloat:counterpart:"
- "appendCGPoint:counterpart:"
- "appendCollection:withName:itemBlock:"
- "appendCustomFormatForValue:withCustomFormatForName:"
- "appendCustomFormatWithName:block:"
- "appendDescriptionToFormatter:"
- "appendDescriptionToStream:"
- "appendDescriptionToStream:fromProxy:"
- "appendDescriptorArray:toDescriptionStream:"
- "appendDictionary:withName:itemBlock:"
- "appendDictionarySection:withName:multilinePrefix:skipIfEmpty:"
- "appendDouble:"
- "appendDouble:withName:decimalPrecision:"
- "appendFloat:withName:"
- "appendFormat:"
- "appendInt64:withName:"
- "appendInt:withName:"
- "appendInteger:"
- "appendInteger:counterpart:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPoint:withName:"
- "appendPointer:withName:"
- "appendProem:block:"
- "appendRect:withName:"
- "appendRightArrow"
- "appendSize:withName:"
- "appendString:"
- "appendString:counterpart:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUInt64:withName:"
- "appendUInt64:withName:format:"
- "appendUnsignedInt:withName:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:counterpart:"
- "appendUnsignedInteger:withName:"
- "appendUnsignedInteger:withName:format:"
- "appendVersionedPID:withName:"
- "applyAssertionParametersOnDisplay:withOptionsMask:"
- "applyDefinitions:"
- "array"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assertSelectionPath:target:hasModality:basis:"
- "assertSelectionPath:target:imposesConstraint:"
- "assertionEndpoint"
- "assertionWithDescription:invalidationBlock:"
- "assertionWithIdentifier:stateDidChangeHandler:"
- "asyncObserverCalloutQueue"
- "authenticateMessage:"
- "autorelease"
- "avoidHitTesting"
- "backboardd must be going down, exiting"
- "backboardd must be going down, ignoring"
- "backboardd-attr-cache-21000099"
- "backgroundStatisticsRegion"
- "backgroundStatisticsValid"
- "baseAttributesFromProvider:"
- "block != ((void *)0)"
- "blockSystemAppForAlternateSystemApp"
- "boolForSetting:"
- "boolValue"
- "bs_CGPointValue"
- "bs_CGRectValue"
- "bs_addObject:toCollectionClass:forKey:"
- "bs_bytesForMIG"
- "bs_containsObjectPassingTest:"
- "bs_dataWithVMAllocatedBytes:length:"
- "bs_dictionaryByPartitioning:"
- "bs_filter:"
- "bs_flatten"
- "bs_jobLabel"
- "bs_lengthForMIG"
- "bs_map:"
- "bs_reduce:block:"
- "bs_removeObject:fromCollectionForKey:"
- "bs_secureDataFromObject:"
- "bs_secureDecodedFromData:withAdditionalClasses:"
- "bs_secureEncoded"
- "bs_valueWithCGPoint:"
- "bs_valueWithCGRect:"
- "bufferEventsMatchingPredicate:withReason:"
- "build"
- "build:"
- "buildMessage:"
- "buildModeForReason:builder:"
- "buildProvenance:"
- "buildSchemaForClass:builder:"
- "buildSpecification:"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "builtinDisplay"
- "bundleId"
- "bundleIdentifier"
- "buttonConfigurationForHardwareButtonMice"
- "buttonConfigurationForVirtualButtonMice"
- "bytes"
- "calloutQueue"
- "canOpenApplication:reason:"
- "canReceiveEvents"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "cannot directly allocate BKSHIDEventDeferringChainObserverPredicate"
- "caseInsensitiveCompare:"
- "chainIdentity"
- "changeBasis"
- "changeSelectionPath:target:basis:ignoreModalities:"
- "checkInAfterDataMigrationUsingCompletionBlock:"
- "checkInBypassingDataMigrationUsingCompletionBlock:"
- "childContextId"
- "class"
- "classForCoder"
- "cleanupClientPort:"
- "clickHapticStrength"
- "clientConnectionForServiceWithName:"
- "clientConnectionForServiceWithName:isNonLaunching:"
- "clientConnectionForServiceWithName:multiplexer:"
- "clientConnectionForServiceWithName:multiplexer:isNonLaunching:"
- "clientInformation"
- "collectionLineBreakNoneStyle"
- "collectiveWatchdogPingBlock"
- "com.apple.mobile.demo"
- "commandModifiedInput"
- "compare:"
- "componentsJoinedByString:"
- "configure:"
- "configureConnection:"
- "conformsToProtocol:"
- "connectionDescriptionForDeferringRuleIdentity:"
- "connectionDescriptionForDeferringRuleIdentity:result:"
- "connectionDescriptionForDeferringRuleWithSeed:pid:result:"
- "connectionWithEndpoint:"
- "connectionWithEndpoint:clientContextBuilder:"
- "constraintBasis"
- "containsDescriptor:"
- "containsObject:"
- "containsValueForKey:"
- "contextIDsToAlwaysSendTouches"
- "contextIDsToExcludeFromHitTesting"
- "contextId"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "coverGestureEnabled"
- "createClientPort"
- "createXPCRepresentation"
- "currentDeviceOrientation"
- "currentHandler"
- "currentMode"
- "currentPolicy"
- "currentThread"
- "d"
- "d16@0:8"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dealloc"
- "debugDescription"
- "debugStyle"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeCGPointForKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClass:fromData:error:"
- "decodeObjectOfClasses:forKey:"
- "decodePayload:"
- "decodeStringForKey:"
- "decodeXPCObjectOfType:forKey:"
- "decoding characteristics failed: %{public}@"
- "defaultCStringEncoding"
- "defaultFocusPredicate"
- "defaultMultiplexer"
- "defaultPreferencesForHardwareType:"
- "defaultSystemPredicate"
- "deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:"
- "deferEventsMatchingPredicate:toTarget:withReason:"
- "deferringObservations"
- "deferringPath"
- "deferringPolicyStatus"
- "deferringResolutionsChanged"
- "definitionForHomeButton"
- "delegate"
- "deliveryChainsDescription"
- "deliveryChainsDescription:"
- "deliveryGraphDescription"
- "deliveryGraphDescription:"
- "deliveryPolicyObserver:policyDidChange:"
- "describes:"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionForRootObject:"
- "descriptionForRootObject:withStyle:"
- "descriptionWithMultilinePrefix:"
- "descriptorByAddingSenderIDToMatchCriteria:"
- "descriptorForAnyGenericGestureType"
- "descriptorForHIDEvent:"
- "descriptorForHIDEventType:page:usage:"
- "descriptorWithBiometricEventType:"
- "descriptorWithEventType:"
- "descriptorWithGenericGestureType:"
- "descriptorWithName:display:"
- "descriptorWithPage:usage:"
- "deserializeFromBytes:byteCount:"
- "dictionaryWithObjects:forKeys:count:"
- "didBlockSystemAppForAlternateSystemApp"
- "didFinishProtobufDecodingWithError:"
- "didUnblockSystemAppForAlternateSystemApp"
- "didUpdateDeferringChains:"
- "didUpdateDeferringObservations:"
- "diffFromSettings:toSettings:"
- "digitizerSurfaceHeight"
- "digitizerSurfaceSize"
- "digitizerSurfaceWidth"
- "dismiss"
- "dismissActions"
- "dismissWithAnimation:"
- "dispatchDiscreteEventsForReason:withRules:"
- "dispatchKeyCommandsForReason:withRule:"
- "displayWithHardwareIdentifier:"
- "ditheringEnabled"
- "doesNotRecognizeSelector:"
- "doubleTapDragMode"
- "doubleValue"
- "dumpAllWithCompletion:"
- "empty"
- "enableNaturalScrolling"
- "enableTapToClick"
- "enableTwoFingerSecondaryClick"
- "encodeBool:forKey:"
- "encodeCGPoint:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:error:"
- "encodeObject:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "encodeWithXPCDictionary:"
- "encodeXPCObject:forKey:"
- "endpoint"
- "endpointForMachName:service:instance:"
- "endpointForServiceName:oneshot:service:instance:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateKeysWithBlock:"
- "enumerateWithBlock:"
- "environmentWithIdentifier:"
- "error"
- "error encoding BKSHIDUISensorMode: %{public}@ : %{public}@"
- "errorHandler"
- "errorWithDomain:code:userInfo:"
- "eventDescriptorIsRestricted:"
- "eventProvenance"
- "everySelectionPath"
- "exceptionWithName:reason:userInfo:"
- "excludeEventsFromSenders:fromHitTestingToContextIDs:"
- "exclusiveTouchNormalizedSubRect"
- "exclusiveTouchNormalizedSubRectInReferenceSpace"
- "existingOverlayForDisplay:"
- "externalDefaults"
- "f16@0:8"
- "failWithError:"
- "fallbackXPCEncodableClass"
- "fenceName"
- "finalStringTokenInChain"
- "firstObject"
- "floatValue"
- "flush"
- "focusTargetForPID:"
- "freeze"
- "generalObservers"
- "getHitTestContextsAtPoint:withAdditionalContexts:onDisplay:withCompletion:"
- "globalDevicePreferences"
- "globalEventsAssertion"
- "globalPointerPosition"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleFromXPCRepresentation:"
- "hasDebugStyle"
- "hasReceivedLatestDeferringObservationsFromServer"
- "hasSuccinctStyle"
- "hasVirtualMouseButtons"
- "hash"
- "hashTableWithOptions:"
- "hidEventType"
- "hitTestLocationX"
- "hitTestLocationY"
- "hitTestRegionLocationForPoint:"
- "hostContextId"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8I16*20I28"
- "iapDefaults"
- "id<BSInvalidatable>  _Nonnull BKSDisplayServicesSetMainDisplayCloneMirroringModeForDestinationDisplay(NSString *__strong _Nonnull, BKSDisplayServicesCloneMirroringMode)"
- "identity"
- "idleSleepInterval"
- "ignoreTetheringPreferences"
- "info"
- "infoDictionary"
- "init"
- "initForProtobufDecoding"
- "initFromPropertyList:"
- "initProtobufTranslatorForObject:"
- "initWithBSXPCCoder:"
- "initWithBiometricEventType:"
- "initWithBundleId:"
- "initWithCalloutQueue:"
- "initWithCapacity:"
- "initWithChildContextId:hostContextId:"
- "initWithCoder:"
- "initWithConfigurator:"
- "initWithContextID:displayUUID:identifier:policy:"
- "initWithContextId:initialTouchTimestamp:"
- "initWithDescriptor:"
- "initWithDescriptor:senderID:"
- "initWithDevice:lifetimeAssertion:"
- "initWithDisplay:environment:"
- "initWithDisplayUUID:relativeToDisplayUUID:alongEdge:atOffset:"
- "initWithEndpoint:options:"
- "initWithEventProvenance:"
- "initWithEventType:"
- "initWithGenericGestureType:"
- "initWithIdentifier:"
- "initWithIdentifier:forReason:invalidationBlock:"
- "initWithIdentifier:touchBehavior:"
- "initWithIdentity:compatibilityDisplay:path:"
- "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:"
- "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:"
- "initWithInfo:responder:"
- "initWithInfo:timeout:forResponseOnQueue:withHandler:"
- "initWithMachServiceName:options:"
- "initWithName:display:"
- "initWithObjects:"
- "initWithPidToContextIdsDictionary:"
- "initWithPoint:contextID:"
- "initWithPolicies:"
- "initWithProcessId:contextIds:"
- "initWithReason:"
- "initWithReason:seed:payload:"
- "initWithReason:seed:rule:"
- "initWithReason:seed:rules:"
- "initWithRect:"
- "initWithRect:exclusiveTouchSubRect:"
- "initWithSecureModeViolations:"
- "initWithSeed:pid:"
- "initWithSenderDescriptor:"
- "initWithString:"
- "initWithXPCDictionary:"
- "inspectChangesWithBlock:"
- "inspectChangesWithOldPolicy:newPolicy:usingBlock:"
- "integerValue"
- "interface"
- "interfaceWithIdentifier:"
- "interfaceWithProtocol:"
- "intersectsSet:"
- "invalidate"
- "invalidateButtonDownPointerRepositionAssertionWithUniqueIdentifier:onDisplay:"
- "ipc_addPolicy:"
- "isActive"
- "isAuthentic"
- "isAuthenticated"
- "isBuffer"
- "isEffectivelyEqualToMode:"
- "isEmpty"
- "isEqual"
- "isEqual:"
- "isEqualExceptIdentifierAndReasons:"
- "isEqualToArray:"
- "isEqualToString:"
- "isFinalStringToken"
- "isInterstitial"
- "isKindOfClass:"
- "isLongPressEnabled"
- "isMemberOfClass:"
- "isModifierOnlyCommand"
- "isNonLaunching"
- "isProxy"
- "isRestrictedToSystemShell"
- "isRoutableKeyCommand"
- "isSignal"
- "isTextualKeyCommand"
- "isUsable"
- "keyCommandForEvent:gsKeyboard:"
- "keyCommandForEvent:gsKeyboard:activeModifiers:"
- "keyCommandWithInput:modifierFlags:"
- "keyCommandWithKeyCode:modifierFlags:"
- "keyDescriptionForSetting:"
- "keyboardDefaults"
- "keyboardDeviceForSenderID:"
- "keyboardDeviceLayoutsDidChange:"
- "keyboardDevicesDidConnect:"
- "keyboardDevicesDidDisconnect:"
- "keyboardFocusEnvironment"
- "keyboardFocusTarget"
- "keyboardFocusTargetWithDeferringToken:"
- "lastObject"
- "length"
- "localDefaults"
- "lock"
- "lockdownDefaults"
- "longPressEnabled"
- "lowercaseString"
- "mainBundle"
- "mainDisplay"
- "makeObjectsPerformSelector:withObject:"
- "manufacturerName"
- "matchSharingTouchesPolicy:orCancelTouchesPolicy:orCombinedPolicy:"
- "matchesDescriptor:failureReason:"
- "matchesHIDEvent:"
- "maximumBackgroundColor"
- "migrateDefaultsIfNecessary"
- "migrateIfNeeded"
- "minimumBackgroundColor"
- "minusSet:"
- "modifiedResolution:"
- "modifyBody:"
- "mostRecentFirstCompare:"
- "mousePointerDevicesDidChange:"
- "mousePointerDevicesDidConnect:"
- "mousePointerDevicesDidDisconnect:"
- "mousePointerGlobalDevicePreferencesDidChange:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nameAllWithCompletion:"
- "nameAndDumpAllWithCompletion:"
- "new"
- "newFenceFromDefaultServer"
- "newFenceHandleForCAFenceHandle:"
- "newFenceHandleForContext:"
- "normalizedGlobalPointerPosition"
- "nullDisplay"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "observeTouchEventDeliveryDidOccur:response:"
- "observer:deliveryChainDidUpdate:"
- "observerDeliveryPolicyDidChange:"
- "observerInterface"
- "observerPolicyDidChange: %p -> <%{public}@: %p>"
- "observersToTouchIdentifiers"
- "observingClient"
- "openAlternateSystemAppWithBundleID:"
- "openApplication:options:clientPort:withResult:"
- "openApplication:options:withResult:"
- "openURL:application:options:clientPort:withResult:"
- "orderedContext"
- "orientationEventsEnabled"
- "overlayStyle:block:"
- "passiveOrientationEvents"
- "performSelector:"
- "performSelector:onThread:withObject:waitUntilDone:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:inModes:"
- "performSelector:withObject:withObject:"
- "persistentConnectionDefaults"
- "pidForApplication:"
- "pointScale"
- "pointerAccelerationFactor"
- "pointerGlobalDevicePreferencesDidChange:"
- "pointerState"
- "pointerSuppressionAssertion"
- "pointerSuppressionAssertionOnDisplay:forReason:withOptionsMask:"
- "pointingDevicesDidChange:"
- "policies"
- "policyByCombiningPolicies:"
- "policyByMappingContainedPoliciesWithBlock:"
- "policyCancelingTouchesDeliveredToContextId:withInitialTouchTimestamp:"
- "policyExcludingPolicy:"
- "policyExcludingPolicyIdenticalTo:"
- "policyIncludingPolicy:"
- "policyRequiringSharingOfTouchesDeliveredToChildContextId:withHostContextId:"
- "postTouchAnnotations:"
- "preciseLocationX"
- "preciseLocationY"
- "predicateEventTypeMask"
- "preferenceKey"
- "preferences"
- "preferencesForDevice:"
- "preferredScale"
- "present"
- "prevailing client request: %{public}@"
- "prevailing client request: %{public}@ all modes:%{public}@"
- "prevailing client request: none!"
- "previouslyRoutedContextIDs"
- "processDescription"
- "processIds"
- "processInfo"
- "productName"
- "progressIndicatorWithStyle:position:"
- "propertyListEncoded"
- "protobufSchema"
- "protocolForProtocol:"
- "proximityDetectionMaskDidChange:"
- "proximityDidUnoccludeAfterWake"
- "proximitySensorDetectionMaskDidChange:"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8{CGPoint=dd}16"
- "queue"
- "queueWithName:"
- "queueWithName:serviceQuality:"
- "raise:format:"
- "rect"
- "reducePolicyToObjectWithBlock:"
- "reference"
- "registerKeyCommands:"
- "registerSceneHostSettings:forCAContextID:"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remoteTarget"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeValue:"
- "replaceBytesInRange:withBytes:length:"
- "requestGlobalMouseEventsForDisplay:targetContextID:"
- "requestGlobalMouseEventsForDisplay:targetContextID:options:"
- "requestUISensorMode:"
- "requestedChainIdentity"
- "requiresFuzzyMatching"
- "resolutionDescriptionForEventDescriptor:sender:result:"
- "resolutionDescriptionForEventDescriptor:senderDescriptor:"
- "resolutionDescriptionForKeyCommand:sender:result:"
- "resolutionDescriptionForKeyCommand:senderDescriptor:"
- "respondsToSelector:"
- "restartWithOptions:"
- "restrictedToEventDescriptors"
- "restrictedToSystemShell"
- "resume"
- "retain"
- "retainCount"
- "ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:seed:pid:"
- "ruleForDeferringEventsMatchingPredicate:toTarget:withReason:seed:pid:"
- "ruleForDispatchingDiscreteEventsMatchingPredicate:toTarget:"
- "ruleForDispatchingKeyCommandsMatchingPredicate:toTargets:"
- "ruleOriginatorBasis"
- "scrollAccelerationFactor"
- "securityAnalysisFromCAHitTestDictionary:errorString:"
- "senderDescriptor"
- "sensorCharacteristics"
- "serializedData"
- "server"
- "serviceQuality"
- "set"
- "setAcceleratedRelativePosition:"
- "setAcceleratedRelativePositionX:"
- "setAcceleratedRelativePositionY:"
- "setAccelerometerEventsEnabled:"
- "setAcceptableConcreteSubclasses:"
- "setActivationHandler:"
- "setActiveModifiers:"
- "setAllowWirelessExtendedDisplay:"
- "setAlwaysOnGesturesEnabled:"
- "setAssertionEndpoint:"
- "setAssociatedDisplay:"
- "setAuthenticated:"
- "setAuthenticationMessage:"
- "setAuthenticationMessageContext:"
- "setAvoidHitTesting:"
- "setBackgroundAverage:"
- "setBackgroundAverageContrastThreshold:"
- "setBackgroundStandardDeviation:"
- "setBackgroundStatisticsFailingContrast:"
- "setBackgroundStatisticsForeground:"
- "setBackgroundStatisticsPassingContrast:"
- "setBackgroundStatisticsRegion:"
- "setBackgroundStatisticsValid:"
- "setBasis:"
- "setBufferingPredicates:"
- "setBundleId:"
- "setButtonConfigurationForHardwareButtonMice:"
- "setButtonConfigurationForVirtualButtonMice:"
- "setByAddingObject:"
- "setCalloutQueue:"
- "setCapsLockKeyHasLanguageSwitchLabel:"
- "setChangeSource:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClickHapticAssetType:"
- "setClickHapticStrength:"
- "setClient:"
- "setClientInformation:"
- "setClientMessagingExpectation:"
- "setCollectionLineBreak:"
- "setCollectiveWatchdogPingBlock:"
- "setCommandModifiedInput:"
- "setConnectedKeyboards:withReply:"
- "setConnection:"
- "setConstraint:"
- "setConstraintAssertions:"
- "setContainsEndOfChain:"
- "setContentsMask:"
- "setContext:"
- "setContextID:"
- "setContextIDs:"
- "setContextIDs:forHitTestContextCategory:"
- "setContextIDsToAlwaysSendTouches:"
- "setContextIDsToExcludeFromHitTesting:"
- "setContextIds:"
- "setContextMove:"
- "setContextRelativePointerPosition:onDisplay:withAnimationParameters:restrictingToPID:"
- "setContextRelativePointerPosition:withInitialVelocity:onDisplay:withDecelerationRate:restrictingToPID:"
- "setContextType:"
- "setCountryCode:"
- "setCoverGestureEnabled:"
- "setCumulativeContentsTransform:"
- "setCumulativeLayerTransform:"
- "setCumulativeOpacity:"
- "setCumulativeTransform:"
- "setDeferringEnvironment:"
- "setDeferringRules:"
- "setDeferringToken:"
- "setDelegate:"
- "setDescriptors:"
- "setDestinationAuditToken:"
- "setDetectedOcclusion:"
- "setDetectionMask:"
- "setDeviceType:"
- "setDigitizerEnabled:"
- "setDigitizerSurfaceHeight:"
- "setDigitizerSurfaceSize:"
- "setDigitizerSurfaceWidth:"
- "setDisableExtendedDisplayByDefault:"
- "setDisableFeatures:"
- "setDisableStudyLogALSLogging:"
- "setDisableStudyLogAccelerometerLogging:"
- "setDisableStudyLogGyroLogging:"
- "setDiscreteDispatchingRules:"
- "setDispatchingTarget:"
- "setDisplay:"
- "setDisplayState:"
- "setDisplayUUID:"
- "setDisplays:"
- "setDoubleTapDragMode:"
- "setEnableNaturalScrolling:"
- "setEnableTapToClick:"
- "setEnableTwoFingerSecondaryClick:"
- "setEnvironment:"
- "setErrorHandler:"
- "setEstimatedProximityMode:"
- "setEventDispatchMode:ambiguityRecommendation:lastTouchTimestamp:"
- "setEventDispatchMode:lastTouchTimestamp:"
- "setEventType:"
- "setExclusiveTouchNormalizedSubRect:"
- "setExclusivityIdentifier:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFinalSampleEvent:"
- "setFinalStringToken:"
- "setFingerDownCount:"
- "setFixedBrightnessLevelWhileDisabled:"
- "setFixedBrightnessNitsWhileDisabled:"
- "setFlag:forSetting:"
- "setForegroundApplicationOnMainDisplay:pid:"
- "setGSModifierState:"
- "setGeneralObservers:"
- "setGlobalDevicePreferences:"
- "setGlobalEventsAssertion:"
- "setGlobalPointerEventRoutes:forDisplay:"
- "setGlobalPointerPosition:"
- "setGlobeKeyLabelHasGlobeSymbol:"
- "setHardwareType:"
- "setHasDiscreteProximitySensor:"
- "setHasInsecureFilter:"
- "setHasVirtualMouseButtons:"
- "setHitTestContextCategory:"
- "setHitTestContexts:"
- "setHitTestFilterParameters:"
- "setHitTestInformationFromEndEvent:"
- "setHitTestInformationFromStartEvent:"
- "setHitTestInformationMask:"
- "setHitTestLocation:"
- "setHitTestLocationX:"
- "setHitTestLocationY:"
- "setHitTestSecurityAnalysis:"
- "setIdentifier:"
- "setIdleSleepInterval:"
- "setIgnoreModalities:"
- "setIndependentWatchdogEnabled:"
- "setInitialSampleEvent:"
- "setInitialTouchTimestamp:"
- "setInterface:"
- "setInterfaceOrientation:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsDetached:"
- "setKeyCommand:"
- "setKeyCommandDispatchingRules:"
- "setKeyCommands:"
- "setKeyCommandsRegistrations:"
- "setLanguage:"
- "setLayerNamesByContext:"
- "setLayout:"
- "setLockBacklight:"
- "setLocus:"
- "setLog:"
- "setLongPressTimeout:"
- "setManufacturerName:"
- "setMaximumBackgroundColor:"
- "setMaximumForce:"
- "setMaximumLongPressTimeInterval:"
- "setMaximumMultiplePressTimeInterval:"
- "setMaximumPositionZ:"
- "setMaximumPressCount:"
- "setMaximumTapCount:"
- "setMinimumBackgroundColor:"
- "setMinimumLongPressTimeInterval:"
- "setMinimumMultiplePressTimeInterval:"
- "setModality:"
- "setModalityAssertions:"
- "setMode:"
- "setModifierKeyRemapping:"
- "setMousePointerDeviceObservationEnabled:"
- "setMousePointerPreferenceObservationEnabled:"
- "setMultiplexer:"
- "setMultitouchHostStateKeys:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObject:forSetting:"
- "setObserver:"
- "setObserverInterface:"
- "setObserversToTouchIdentifiers:"
- "setObservesAllTouches:"
- "setObservesDeferringChainIdentities:"
- "setObservesDeferringResolutions:"
- "setObservesProximitySensorDetectionMaskChanges:"
- "setObservesTouch:withIdentifier:"
- "setObservingClient:"
- "setObservingUsableKeyboardConnections:"
- "setOcclusionMask:"
- "setOcclusionPercentage:"
- "setOcclusionType:"
- "setOldModifierKeyRemapping:"
- "setOptions:"
- "setOrientationEventsEnabled:"
- "setOriginIdentifier:"
- "setParentsHaveInsecureLayerProperties:"
- "setPassiveOrientationEvents:"
- "setPathAttributes:"
- "setPathIdentifier:"
- "setPathIndex:"
- "setPattern:"
- "setPid:"
- "setPinOnButtonDown:"
- "setPlatformInputModeConfiguration:"
- "setPocketTouchesExpected:"
- "setPointerAccelerationFactor:"
- "setPointerEdgeMask:"
- "setPointerPosition:onDisplay:withAnimationParameters:"
- "setPointerState:"
- "setPointerSuppressionAssertion:"
- "setPolicyStatus:"
- "setPostEventWithCurrentDetectionMask:"
- "setPowerSourceID:"
- "setPreciseLocation:"
- "setPreciseLocationX:"
- "setPreciseLocationY:"
- "setPreferenceKey:"
- "setPreferences:"
- "setPreferences:forDevice:"
- "setPreviouslyRoutedContextIDs:"
- "setPrimaryPage:primaryUsage:"
- "setProcessDescription:"
- "setProcessId:"
- "setProductName:"
- "setProgressIndicatorProperties:"
- "setProvenance:"
- "setProximityDetectionMode:"
- "setProximityHostStateKeys:"
- "setQueue:"
- "setReason:"
- "setReference:"
- "setRegistrantEntitled:"
- "setRemoteObjectInterface:"
- "setRepresentsHomeButton:"
- "setRequestedChainIdentity:"
- "setSceneHostSettings:forContextID:"
- "setSceneTouchBehavior:"
- "setScrollAccelerationFactor:"
- "setSecureName:"
- "setSecureNameStatus:"
- "setSecurityAnalysis:"
- "setSelectionPath:"
- "setSelectionPathIdentifier:"
- "setSelectionRequests:"
- "setSelectionTarget:"
- "setSenderDescriptors:"
- "setSenderID:"
- "setServer:"
- "setServiceQuality:"
- "setSettings:"
- "setShiftModifiedInput:"
- "setShouldSendAmbiguityRecommendations:"
- "setSignature:"
- "setSlotID:"
- "setSmartCoverState:"
- "setSource:"
- "setSourceDescriptor:"
- "setStandardType:"
- "setState:"
- "setStateChangeSemaphore:"
- "setStateChangeWaiter:"
- "setSubinterfaceID:"
- "setSuggestedSystemApertureGracePeriodForScreenOff:"
- "setSupportsDragLock:"
- "setSupportsLightClick:"
- "setSupportsSystemHaptics:"
- "setSuppressAllEvents:"
- "setSuppressionOptions:"
- "setSystemAppControlsFocusOnMainDisplay:"
- "setSystemGestureStateChange:"
- "setSystemGesturesPossible:"
- "setTapToWakeEnabled:"
- "setTarget:"
- "setTargetContextID:"
- "setTargetQueue:"
- "setTargetSlotID:"
- "setTeleportState:"
- "setText:"
- "setTimestamp:"
- "setToken:"
- "setTouchIdentifier:"
- "setTouchIdentifierToObserverLists:"
- "setTouchStreamIdentifier:"
- "setTransform:"
- "setTransport:"
- "setType:"
- "setUnacceleratedRelativePosition:"
- "setUnacceleratedRelativePositionX:"
- "setUnacceleratedRelativePositionY:"
- "setUniqueIdentifier:"
- "setUnmodifiedInput:"
- "setUpdateInterval:"
- "setUsagePage:"
- "setUserIdentifier:"
- "setValidMask:"
- "setValue:forKey:"
- "setVersionedPID:"
- "setVisibleDevices:"
- "setWaitForDataMigration:"
- "setWakeAnimationStyle:"
- "setWakeOnLongPressEnabled:"
- "setWakeOnLongTapThroughEnabled:"
- "setWakeOnSwipeEnabled:"
- "setWakeOnSwipeThroughEnabled:"
- "setWakeOnTapThroughEnabled:"
- "setWatchdogMonitoringEnabled:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setXThreshold:"
- "setYThreshold:"
- "setZGradient:"
- "setZThreshold:"
- "settings"
- "sharedInstance"
- "shiftModifiedInput"
- "shouldSendAmbiguityRecommendations"
- "signal"
- "simpleConstraint"
- "simulatePhoneButton"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "specificationWithKeyCommand:context:"
- "specifiesDescriptor:"
- "springBoardDefaults"
- "start"
- "stateChangeSemaphore"
- "stateChangeWaiter"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "stringWithCString:encoding:"
- "stringWithCharacters:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "stylusOpaqueTouchDigitizer"
- "submitRuleChanges:"
- "subsetForPID:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "succinctStyle"
- "superclass"
- "supportsBSXPCSecureCoding"
- "supportsDragLock"
- "supportsLightClick"
- "supportsReadyToReceiveEventServiceProperty"
- "supportsSecureCoding"
- "supportsSystemHaptics"
- "suppressPointerEventsForReason:"
- "suppressUISensorChangesForReason:"
- "suppressionOptions"
- "synchronize"
- "systemApplicationBundleIdentifier"
- "systemEnvironment"
- "systemTarget"
- "systemTargetWithDeferringToken:"
- "tag"
- "tapToWakeEnabled"
- "targetForDeferringEnvironment:"
- "targetForDeferringEnvironment:deferringToken:"
- "targetForDeferringEnvironment:selectionPath:"
- "targetForPID:environment:"
- "targetForPID:environment:selectionPath:"
- "terminate"
- "terminateAlternateSystemAppWithBundleID:"
- "terminateApplication:forReason:andReport:withDescription:"
- "terminateShellWithJobLabel:"
- "terminateSystemShellWithJobLabel:"
- "tetheredDisplayPortMode"
- "tokenForIdentifierOfCAContext:"
- "tokenForIdentifierOfCGSConnection:"
- "tokenForIdentifierOfCGSWindow:"
- "tokenForString:"
- "touchDetachedForIdentifier:context:pid:"
- "touchIdentifierToObserverLists"
- "touchUpOccuredForIdentifier:detached:context:pid:"
- "transactionAssertionWithReason:"
- "transform"
- "transform3DForDisplayUUID:layerID:contextID:"
- "transformForDisplayUUID:layerID:contextID:"
- "type"
- "unacceleratedRelativePositionX"
- "unacceleratedRelativePositionY"
- "unblockSystemAppForAlternateSystemApp"
- "uniqueId"
- "unlock"
- "unmodifiedInput"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsupported contextIDsToAlwaysSendTouches structure %@"
- "unsupported contextIDsToExcludeFromHitTesting structure %@"
- "updateFromDefinition:withChangeInspectorBlock:"
- "updateInterval"
- "updateSettings:"
- "uppercaseString"
- "usable"
- "usagePage"
- "userInitiated"
- "userInteractive"
- "userInteractiveMultiplexer"
- "v144@0:8{CATransform3D=dddddddddddddddd}16"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"<BSDescriptionFormatting>\"16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"BKSTouchDeliveryPolicy\"16"
- "v24@0:8@\"BSAnimationSettings\"16"
- "v24@0:8@\"BSDescriptionStream\"16"
- "v24@0:8@\"NSArray<__BKSEventDeferringChainIdentity__>\"16"
- "v24@0:8@\"NSArray<__BKSTouchHitTestFilterParameters__>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<B@?>16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8I16I20"
- "v24@0:8Q16"
- "v24@0:8^{?=[96I]}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8{?=SSSS}16"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8C16d20"
- "v32@0:8@\"NSArray<__NSNumber__>\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"RBSProcessExitContext\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8C16C20d24"
- "v32@0:8I16i20@?24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8@16@24@?32"
- "v40@0:8@16i24B28@32"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24@32i40"
- "v44@0:8@16@24I32@?36"
- "v48@0:8@16@24@32@?40"
- "v48@0:8{CGPoint=dd}16@32@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@16@24@32I40@?44"
- "v52@0:8@16@24@32d40i48"
- "validWithTimestamp:"
- "validateMessage:"
- "validateProvenance:"
- "valueForKey:"
- "valueForKey:defaultValueProvider:"
- "valueWithBytes:objCType:"
- "valueWithCATransform3D:"
- "verifyAuthentic:"
- "visibleDevices"
- "void BKSHIDServicesRequestProximityStatusEvent(NSString *__strong _Nonnull)"
- "waitForDataMigration"
- "wakeOnLongPressEnabled"
- "wakeOnLongPressThroughEnabled"
- "wakeOnSwipeEnabled"
- "wakeOnSwipeThroughEnabled"
- "wakeOnTapThroughEnabled"
- "weakObjectsHashTable"
- "weakToStrongObjectsMapTable"
- "weakToWeakObjectsMapTable"
- "weightedDeferringRuleCompare:"
- "whitespaceCharacterSet"
- "wildcard"
- "xThreshold"
- "yThreshold"
- "zThreshold"
- "zone"
- "{?=\"ctx\"[96I]}"
- "{?=SSSS}16@0:8"
- "{CATransform3D=\"m11\"d\"m12\"d\"m13\"d\"m14\"d\"m21\"d\"m22\"d\"m23\"d\"m24\"d\"m31\"d\"m32\"d\"m33\"d\"m34\"d\"m41\"d\"m42\"d\"m43\"d\"m44\"d}"
- "{CATransform3D=dddddddddddddddd}16@0:8"
- "{CATransform3D=dddddddddddddddd}36@0:8@16Q24I32"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{atomic_flag=\"_Value\"AB}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
