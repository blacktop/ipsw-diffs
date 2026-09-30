## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`

```diff

-668.5.29.0.0
-  __TEXT.__text: 0x71458
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x6b64
-  __TEXT.__const: 0x444
+726.0.0.0.0
+  __TEXT.__text: 0x805f0
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0x7bac
+  __TEXT.__const: 0x424
   __TEXT.__dlopen_cstrs: 0x18e
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__cstring: 0xa247
-  __TEXT.__oslogstring: 0x1efa
+  __TEXT.__gcc_except_tab: 0x410
+  __TEXT.__cstring: 0xb030
+  __TEXT.__oslogstring: 0x206a
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1a48
-  __TEXT.__objc_classname: 0x1754
-  __TEXT.__objc_methname: 0xbc51
-  __TEXT.__objc_methtype: 0x1c90
-  __TEXT.__objc_stubs: 0x62e0
-  __DATA_CONST.__got: 0x698
-  __DATA_CONST.__const: 0x1498
-  __DATA_CONST.__objc_classlist: 0x4b0
-  __DATA_CONST.__objc_protolist: 0x150
+  __TEXT.__unwind_info: 0x1eb8
+  __TEXT.__objc_classname: 0x1af9
+  __TEXT.__objc_methname: 0xd026
+  __TEXT.__objc_methtype: 0x1fd7
+  __TEXT.__objc_stubs: 0x6a80
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__const: 0x1758
+  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a0
+  __DATA_CONST.__objc_selrefs: 0x2af8
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x348
+  __DATA_CONST.__objc_superrefs: 0x3b8
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH_CONST.__const: 0x11e8
-  __AUTH_CONST.__cfstring: 0x8ea0
-  __AUTH_CONST.__objc_const: 0xdf08
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__const: 0x1428
+  __AUTH_CONST.__cfstring: 0x9800
+  __AUTH_CONST.__objc_const: 0x102b8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x1e00
-  __DATA.__objc_ivar: 0x6b0
-  __DATA.__data: 0xfd0
-  __DATA.__bss: 0x548
-  __DATA_DIRTY.__objc_data: 0x10e0
+  __AUTH.__objc_data: 0x23a0
+  __DATA.__objc_ivar: 0x7b0
+  __DATA.__data: 0x10f0
+  __DATA.__bss: 0x558
+  __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08994F1D-25F8-3436-BB45-08B971D424BE
-  Functions: 2748
-  Symbols:   8592
-  CStrings:  5272
+  UUID: 5678780F-6830-3A68-9760-846BDC061063
+  Functions: 3117
+  Symbols:   9732
+  CStrings:  5700
 
Symbols:
+ +[BKSHIDEventBaseAttributes _classForAttributeType:]
+ +[BKSHIDEventBaseAttributes _eventAttributeType]
+ +[BKSHIDEventBaseAttributes deserializeFromBytes:byteCount:]
+ +[BKSHIDEventCollectionDescriptor descriptorWithPage:usage:]
+ +[BKSHIDEventDeferringChangeBasis constraintBasis]
+ +[BKSHIDEventDeferringChangeBasis new]
+ +[BKSHIDEventDeferringChangeBasis ruleOriginatorBasis]
+ +[BKSHIDEventDeferringChangeBasis supportsSecureCoding]
+ +[BKSHIDEventDeferringConstraint build:]
+ +[BKSHIDEventDeferringConstraint new]
+ +[BKSHIDEventDeferringConstraint simpleConstraint]
+ +[BKSHIDEventDeferringConstraint supportsSecureCoding]
+ +[BKSHIDEventDeferringConstraintAssertion build:]
+ +[BKSHIDEventDeferringConstraintAssertion new]
+ +[BKSHIDEventDeferringConstraintAssertion supportsSecureCoding]
+ +[BKSHIDEventDeferringModality activeInputModality]
+ +[BKSHIDEventDeferringModality build:]
+ +[BKSHIDEventDeferringModality new]
+ +[BKSHIDEventDeferringModality protobufSchema]
+ +[BKSHIDEventDeferringModality supportsSecureCoding]
+ +[BKSHIDEventDeferringModalityAssertion build:]
+ +[BKSHIDEventDeferringModalityAssertion new]
+ +[BKSHIDEventDeferringModalityAssertion supportsSecureCoding]
+ +[BKSHIDEventDeferringRule ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:seed:pid:]
+ +[BKSHIDEventDeferringSelectionChangeRequest build:]
+ +[BKSHIDEventDeferringSelectionChangeRequest new]
+ +[BKSHIDEventDeferringSelectionChangeRequest supportsSecureCoding]
+ +[BKSHIDEventDeferringSelectionPathIdentifier everySelectionPath]
+ +[BKSHIDEventDeferringSelectionPathIdentifier genericGesture]
+ +[BKSHIDEventDeferringSelectionPathIdentifier primary]
+ +[BKSHIDEventDeferringSelectionPathIdentifier protobufSchema]
+ +[BKSHIDEventDeferringSelectionPathIdentifier supportsSecureCoding]
+ +[BKSHIDEventDeferringSelectionPathSymbol protobufSchema]
+ +[BKSHIDEventDeferringSelectionPathSymbol supportsSecureCoding]
+ +[BKSHIDEventDeferringSelectionTarget build:]
+ +[BKSHIDEventDeferringSelectionTarget new]
+ +[BKSHIDEventDeferringSelectionTarget supportsSecureCoding]
+ +[BKSHIDEventDeferringTarget build:]
+ +[BKSHIDEventDeferringToken tokenForIdentifierOfCGSWindow:]
+ +[BKSHIDEventDigitizerAttributes _eventAttributeType]
+ +[BKSHIDEventDispatchingTarget targetForDeferringEnvironment:selectionPath:]
+ +[BKSHIDEventDispatchingTarget targetForPID:environment:selectionPath:]
+ +[BKSHIDEventKeyboardAttributes _eventAttributeType]
+ +[BKSHIDEventPointerAttributes _eventAttributeType]
+ +[BKSHIDEventProximityAttributes _eventAttributeType]
+ +[BKSHIDEventRedirectAttributes _eventAttributeType]
+ +[BKSHIDEventSimpleProvenance _withInternalKey:buildMessage:]
+ +[BKSHIDEventSimpleProvenance build:]
+ +[BKSHIDEventSimpleProvenance new]
+ +[BKSHIDEventSimpleProvenance protobufSchema]
+ +[BKSHIDEventSimpleProvenance supportsSecureCoding]
+ +[BKSHIDEventSmartCoverAttributes _eventAttributeType]
+ +[BKSHIDEventUnitTestableProvenance invalid]
+ +[BKSHIDEventUnitTestableProvenance validWithTimestamp:]
+ +[BKSHIDEventUnitTestableProvenance valid]
+ +[BKSHIDServiceConnectionFactory sharedInstance]
+ +[BKSTouchHitTestFilterParameters build:]
+ +[BKSTouchHitTestFilterParameters new]
+ +[BKSTouchHitTestFilterParameters protobufSchema]
+ +[BKSTouchHitTestFilterParameters supportsSecureCoding]
+ +[_BKSHIDCGSConnectionIDEventDeferringToken protobufSchema]
+ +[_BKSHIDCGSConnectionIDEventDeferringToken supportsSecureCoding]
+ +[_BKSHIDCGSWindowIDEventDeferringToken protobufSchema]
+ +[_BKSHIDCGSWindowIDEventDeferringToken supportsSecureCoding]
+ +[_BKSHIDEventAuthenticationKey eventAuthenticationKey]
+ -[BKSHIDEventBaseAttributes changeBasis]
+ -[BKSHIDEventBaseAttributes provenance]
+ -[BKSHIDEventBaseAttributes serializedData]
+ -[BKSHIDEventBaseAttributes setProvenance:]
+ -[BKSHIDEventCollectionDescriptor init]
+ -[BKSHIDEventDeferringChangeBasis .cxx_destruct]
+ -[BKSHIDEventDeferringChangeBasis _initWithIdentifier:provenance:]
+ -[BKSHIDEventDeferringChangeBasis encodeWithCoder:]
+ -[BKSHIDEventDeferringChangeBasis eventProvenance]
+ -[BKSHIDEventDeferringChangeBasis initWithCoder:]
+ -[BKSHIDEventDeferringChangeBasis initWithEventProvenance:]
+ -[BKSHIDEventDeferringChangeBasis init]
+ -[BKSHIDEventDeferringConstraint .cxx_destruct]
+ -[BKSHIDEventDeferringConstraint _initWithCopyOf:]
+ -[BKSHIDEventDeferringConstraint _init]
+ -[BKSHIDEventDeferringConstraint appendDescriptionToStream:]
+ -[BKSHIDEventDeferringConstraint copyWithZone:]
+ -[BKSHIDEventDeferringConstraint description]
+ -[BKSHIDEventDeferringConstraint encodeWithCoder:]
+ -[BKSHIDEventDeferringConstraint hash]
+ -[BKSHIDEventDeferringConstraint identifier]
+ -[BKSHIDEventDeferringConstraint initWithCoder:]
+ -[BKSHIDEventDeferringConstraint init]
+ -[BKSHIDEventDeferringConstraint isEqual:]
+ -[BKSHIDEventDeferringConstraint mutableCopyWithZone:]
+ -[BKSHIDEventDeferringConstraintAssertion .cxx_destruct]
+ -[BKSHIDEventDeferringConstraintAssertion _initWithCopyOf:]
+ -[BKSHIDEventDeferringConstraintAssertion _init]
+ -[BKSHIDEventDeferringConstraintAssertion appendDescriptionToStream:]
+ -[BKSHIDEventDeferringConstraintAssertion basis]
+ -[BKSHIDEventDeferringConstraintAssertion constraint]
+ -[BKSHIDEventDeferringConstraintAssertion copyWithZone:]
+ -[BKSHIDEventDeferringConstraintAssertion description]
+ -[BKSHIDEventDeferringConstraintAssertion encodeWithCoder:]
+ -[BKSHIDEventDeferringConstraintAssertion hash]
+ -[BKSHIDEventDeferringConstraintAssertion initWithCoder:]
+ -[BKSHIDEventDeferringConstraintAssertion init]
+ -[BKSHIDEventDeferringConstraintAssertion isEqual:]
+ -[BKSHIDEventDeferringConstraintAssertion mutableCopyWithZone:]
+ -[BKSHIDEventDeferringConstraintAssertion pathIdentifier]
+ -[BKSHIDEventDeferringConstraintAssertion selectionTarget]
+ -[BKSHIDEventDeferringConstraintAssertion timestamp]
+ -[BKSHIDEventDeferringModality .cxx_destruct]
+ -[BKSHIDEventDeferringModality _initWithCopyOf:]
+ -[BKSHIDEventDeferringModality _init]
+ -[BKSHIDEventDeferringModality appendDescriptionToStream:]
+ -[BKSHIDEventDeferringModality copyWithZone:]
+ -[BKSHIDEventDeferringModality description]
+ -[BKSHIDEventDeferringModality encodeWithCoder:]
+ -[BKSHIDEventDeferringModality hash]
+ -[BKSHIDEventDeferringModality identifier]
+ -[BKSHIDEventDeferringModality initForProtobufDecoding]
+ -[BKSHIDEventDeferringModality initWithCoder:]
+ -[BKSHIDEventDeferringModality init]
+ -[BKSHIDEventDeferringModality isEqual:]
+ -[BKSHIDEventDeferringModality mutableCopyWithZone:]
+ -[BKSHIDEventDeferringModalityAssertion .cxx_destruct]
+ -[BKSHIDEventDeferringModalityAssertion _initWithCopyOf:]
+ -[BKSHIDEventDeferringModalityAssertion _init]
+ -[BKSHIDEventDeferringModalityAssertion appendDescriptionToStream:]
+ -[BKSHIDEventDeferringModalityAssertion basis]
+ -[BKSHIDEventDeferringModalityAssertion copyWithZone:]
+ -[BKSHIDEventDeferringModalityAssertion description]
+ -[BKSHIDEventDeferringModalityAssertion encodeWithCoder:]
+ -[BKSHIDEventDeferringModalityAssertion hash]
+ -[BKSHIDEventDeferringModalityAssertion initWithCoder:]
+ -[BKSHIDEventDeferringModalityAssertion init]
+ -[BKSHIDEventDeferringModalityAssertion isEqual:]
+ -[BKSHIDEventDeferringModalityAssertion modality]
+ -[BKSHIDEventDeferringModalityAssertion mutableCopyWithZone:]
+ -[BKSHIDEventDeferringModalityAssertion pathIdentifier]
+ -[BKSHIDEventDeferringModalityAssertion selectionTarget]
+ -[BKSHIDEventDeferringModalityAssertion timestamp]
+ -[BKSHIDEventDeferringRule _initWithPredicate:restrictedToEventDescriptors:target:reason:identity:]
+ -[BKSHIDEventDeferringRule eventDescriptorIsRestricted:]
+ -[BKSHIDEventDeferringRule restrictedToEventDescriptors]
+ -[BKSHIDEventDeferringSelectionChangeRequest .cxx_destruct]
+ -[BKSHIDEventDeferringSelectionChangeRequest _initWithCopyOf:]
+ -[BKSHIDEventDeferringSelectionChangeRequest _init]
+ -[BKSHIDEventDeferringSelectionChangeRequest appendDescriptionToStream:]
+ -[BKSHIDEventDeferringSelectionChangeRequest basis]
+ -[BKSHIDEventDeferringSelectionChangeRequest copyWithZone:]
+ -[BKSHIDEventDeferringSelectionChangeRequest description]
+ -[BKSHIDEventDeferringSelectionChangeRequest encodeWithCoder:]
+ -[BKSHIDEventDeferringSelectionChangeRequest hash]
+ -[BKSHIDEventDeferringSelectionChangeRequest ignoreModalities]
+ -[BKSHIDEventDeferringSelectionChangeRequest initWithCoder:]
+ -[BKSHIDEventDeferringSelectionChangeRequest init]
+ -[BKSHIDEventDeferringSelectionChangeRequest isEqual:]
+ -[BKSHIDEventDeferringSelectionChangeRequest mutableCopyWithZone:]
+ -[BKSHIDEventDeferringSelectionChangeRequest pathIdentifier]
+ -[BKSHIDEventDeferringSelectionChangeRequest selectionTarget]
+ -[BKSHIDEventDeferringSelectionChangeRequest timestamp]
+ -[BKSHIDEventDeferringSelectionPathIdentifier .cxx_destruct]
+ -[BKSHIDEventDeferringSelectionPathIdentifier _substituteSingeltonForIdentifierString:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier appendDescriptionToStream:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier copyWithZone:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier description]
+ -[BKSHIDEventDeferringSelectionPathIdentifier didFinishProtobufDecodingWithError:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier encodeWithCoder:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier hash]
+ -[BKSHIDEventDeferringSelectionPathIdentifier identifier]
+ -[BKSHIDEventDeferringSelectionPathIdentifier initWithCoder:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier initWithIdentifier:]
+ -[BKSHIDEventDeferringSelectionPathIdentifier isEqual:]
+ -[BKSHIDEventDeferringSelectionPathSymbol .cxx_destruct]
+ -[BKSHIDEventDeferringSelectionPathSymbol copyWithZone:]
+ -[BKSHIDEventDeferringSelectionPathSymbol copy]
+ -[BKSHIDEventDeferringSelectionPathSymbol description]
+ -[BKSHIDEventDeferringSelectionPathSymbol didFinishProtobufDecodingWithError:]
+ -[BKSHIDEventDeferringSelectionPathSymbol encodeWithCoder:]
+ -[BKSHIDEventDeferringSelectionPathSymbol hash]
+ -[BKSHIDEventDeferringSelectionPathSymbol initWithCoder:]
+ -[BKSHIDEventDeferringSelectionPathSymbol init]
+ -[BKSHIDEventDeferringSelectionPathSymbol isEqual:]
+ -[BKSHIDEventDeferringSelectionTarget .cxx_destruct]
+ -[BKSHIDEventDeferringSelectionTarget _initWithCopyOf:]
+ -[BKSHIDEventDeferringSelectionTarget _init]
+ -[BKSHIDEventDeferringSelectionTarget appendDescriptionToStream:]
+ -[BKSHIDEventDeferringSelectionTarget copyWithZone:]
+ -[BKSHIDEventDeferringSelectionTarget description]
+ -[BKSHIDEventDeferringSelectionTarget display]
+ -[BKSHIDEventDeferringSelectionTarget encodeWithCoder:]
+ -[BKSHIDEventDeferringSelectionTarget environment]
+ -[BKSHIDEventDeferringSelectionTarget hash]
+ -[BKSHIDEventDeferringSelectionTarget initWithCoder:]
+ -[BKSHIDEventDeferringSelectionTarget init]
+ -[BKSHIDEventDeferringSelectionTarget isEqual:]
+ -[BKSHIDEventDeferringSelectionTarget mutableCopyWithZone:]
+ -[BKSHIDEventDeferringSelectionTarget target]
+ -[BKSHIDEventDeferringToken _identifierOfCGSWindow]
+ -[BKSHIDEventDeferringToken _isIdentifierOfCGSWindow]
+ -[BKSHIDEventDeliveryChain containsEndOfChain]
+ -[BKSHIDEventDeliveryChain containsSubset]
+ -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:]
+ -[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:]
+ -[BKSHIDEventDeliveryChain modalities]
+ -[BKSHIDEventDeliveryChain selectionPath]
+ -[BKSHIDEventDeliveryChain setContainsEndOfChain:]
+ -[BKSHIDEventDeliveryChain subsetForPID:]
+ -[BKSHIDEventDeliveryChainObserver chainIdentity]
+ -[BKSHIDEventDeliveryManager _executeDescriptionFetch:result:]
+ -[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:]
+ -[BKSHIDEventDeliveryManager _lock_noteServerInterruption]
+ -[BKSHIDEventDeliveryManager _lock_pendQuery:]
+ -[BKSHIDEventDeliveryManager appendDescriptionToStream:]
+ -[BKSHIDEventDeliveryManager assertSelectionPath:target:hasModality:basis:]
+ -[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:]
+ -[BKSHIDEventDeliveryManager changeSelectionPath:target:basis:ignoreModalities:]
+ -[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleIdentity:result:]
+ -[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleWithSeed:pid:result:]
+ -[BKSHIDEventDeliveryManager debugDescription]
+ -[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:]
+ -[BKSHIDEventDeliveryManager deliveryChainsDescription:]
+ -[BKSHIDEventDeliveryManager deliveryGraphDescription:]
+ -[BKSHIDEventDeliveryManager resolutionDescriptionForEventDescriptor:sender:result:]
+ -[BKSHIDEventDeliveryManager resolutionDescriptionForKeyCommand:sender:result:]
+ -[BKSHIDEventDeliveryPolicy _initWithPolicyObservation:]
+ -[BKSHIDEventDeliveryPolicy appendDescriptionToStream:]
+ -[BKSHIDEventDeliveryPolicy deferringPolicyStatus]
+ -[BKSHIDEventDeliveryPolicy description]
+ -[BKSHIDEventDeliveryPolicy finalStringTokenInChain]
+ -[BKSHIDEventDeliveryPolicy hash]
+ -[BKSHIDEventDeliveryPolicy isEqual:]
+ -[BKSHIDEventDeliveryPolicyObserver _lock_buildCurrentPolicy]
+ -[BKSHIDEventDeliveryPolicyObserver _lock_effectivePolicyObservation]
+ -[BKSHIDEventDeliveryPolicyObserver _lock_updatePolicyWithBlock:]
+ -[BKSHIDEventDeliveryPolicyObserver _notifyAsyncObservers:didUpdatePolicy:]
+ -[BKSHIDEventDeliveryPolicyObserver _replacePolicySpecificationObject:withObject:replaceIvarBlock:]
+ -[BKSHIDEventDeliveryPolicyObserver asyncObserverCalloutQueue]
+ -[BKSHIDEventDeliveryPolicyObserver currentPolicy]
+ -[BKSHIDEventDeliveryPolicyObserver finalStringTokenInChain]
+ -[BKSHIDEventDeliveryPolicyObserver selectionPathIdentifier]
+ -[BKSHIDEventDeliveryPolicyObserver setSelectionPathIdentifier:]
+ -[BKSHIDEventDeliveryRuleChangeTransaction constraintAssertions]
+ -[BKSHIDEventDeliveryRuleChangeTransaction modalityAssertions]
+ -[BKSHIDEventDeliveryRuleChangeTransaction selectionRequests]
+ -[BKSHIDEventDeliveryRuleChangeTransaction setConstraintAssertions:]
+ -[BKSHIDEventDeliveryRuleChangeTransaction setModalityAssertions:]
+ -[BKSHIDEventDeliveryRuleChangeTransaction setSelectionRequests:]
+ -[BKSHIDEventDigitizerPathAttributes changeBasis]
+ -[BKSHIDEventDigitizerPathAttributes provenance]
+ -[BKSHIDEventDigitizerPathAttributes setProvenance:]
+ -[BKSHIDEventDispatchingTarget _initWithEnvironment:token:selectionPath:pid:]
+ -[BKSHIDEventDispatchingTarget selectionPathIdentifier]
+ -[BKSHIDEventObserver _initWithConnectionFactory:]
+ -[BKSHIDEventObserver _lock_flushInitialStateToServer]
+ -[BKSHIDEventObserver hasReceivedLatestDeferringObservationsFromServer]
+ -[BKSHIDEventPolicyObservation appendDescriptionToStream:]
+ -[BKSHIDEventPolicyObservation isFinalStringToken]
+ -[BKSHIDEventPolicyObservation selectionPath]
+ -[BKSHIDEventSimpleProvenance .cxx_destruct]
+ -[BKSHIDEventSimpleProvenance _calculateSignatureWithHMACContext:]
+ -[BKSHIDEventSimpleProvenance _initWithCopyOf:]
+ -[BKSHIDEventSimpleProvenance _init]
+ -[BKSHIDEventSimpleProvenance _verifySignatureWithInternalKey:]
+ -[BKSHIDEventSimpleProvenance appendDescriptionToStream:]
+ -[BKSHIDEventSimpleProvenance copyWithZone:]
+ -[BKSHIDEventSimpleProvenance description]
+ -[BKSHIDEventSimpleProvenance encodeWithCoder:]
+ -[BKSHIDEventSimpleProvenance eventType]
+ -[BKSHIDEventSimpleProvenance hash]
+ -[BKSHIDEventSimpleProvenance initForProtobufDecoding]
+ -[BKSHIDEventSimpleProvenance initWithCoder:]
+ -[BKSHIDEventSimpleProvenance init]
+ -[BKSHIDEventSimpleProvenance isEqual:]
+ -[BKSHIDEventSimpleProvenance mutableCopyWithZone:]
+ -[BKSHIDEventSimpleProvenance signature]
+ -[BKSHIDEventSimpleProvenance timestamp]
+ -[BKSHIDEventSimpleProvenance versionedPID]
+ -[BKSHIDEventSimpleProvenanceOriginator .cxx_destruct]
+ -[BKSHIDEventSimpleProvenanceOriginator buildProvenance:]
+ -[BKSHIDEventSimpleProvenanceOriginator verifyAuthentic:]
+ -[BKSHIDEventUnitTestableProvenance eventType]
+ -[BKSHIDEventUnitTestableProvenance isAuthentic]
+ -[BKSHIDEventUnitTestableProvenance timestamp]
+ -[BKSHIDEventUnitTestableProvenance versionedPID]
+ -[BKSHIDServiceConnectionFactory clientConnectionForServiceWithName:]
+ -[BKSHIDServiceConnectionFactory clientConnectionForServiceWithName:isNonLaunching:]
+ -[BKSHIDServiceConnectionFactory clientConnectionForServiceWithName:multiplexer:]
+ -[BKSHIDServiceConnectionFactory clientConnectionForServiceWithName:multiplexer:isNonLaunching:]
+ -[BKSHitTestRegion appendDescriptionToStream:]
+ -[BKSHitTestRegion hitTestRegionLocationForPoint:]
+ -[BKSHitTestRegion isEmpty]
+ -[BKSMousePointerService _activateServerConnection:]
+ -[BKSMutableHIDEventDeferringConstraint copyWithZone:]
+ -[BKSMutableHIDEventDeferringConstraint setIdentifier:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion copyWithZone:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setBasis:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setConstraint:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setPathIdentifier:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setSelectionTarget:]
+ -[BKSMutableHIDEventDeferringConstraintAssertion setTimestamp:]
+ -[BKSMutableHIDEventDeferringModality copyWithZone:]
+ -[BKSMutableHIDEventDeferringModality setIdentifier:]
+ -[BKSMutableHIDEventDeferringModalityAssertion copyWithZone:]
+ -[BKSMutableHIDEventDeferringModalityAssertion setBasis:]
+ -[BKSMutableHIDEventDeferringModalityAssertion setModality:]
+ -[BKSMutableHIDEventDeferringModalityAssertion setPathIdentifier:]
+ -[BKSMutableHIDEventDeferringModalityAssertion setSelectionTarget:]
+ -[BKSMutableHIDEventDeferringModalityAssertion setTimestamp:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest copyWithZone:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest setBasis:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest setIgnoreModalities:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest setPathIdentifier:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest setSelectionTarget:]
+ -[BKSMutableHIDEventDeferringSelectionChangeRequest setTimestamp:]
+ -[BKSMutableHIDEventDeferringSelectionTarget copyWithZone:]
+ -[BKSMutableHIDEventDeferringSelectionTarget setDisplay:]
+ -[BKSMutableHIDEventDeferringSelectionTarget setEnvironment:]
+ -[BKSMutableHIDEventDeferringSelectionTarget setTarget:]
+ -[BKSMutableHIDEventPolicyObservation copyWithZone:]
+ -[BKSMutableHIDEventPolicyObservation setFinalStringToken:]
+ -[BKSMutableHIDEventPolicyObservation setSelectionPath:]
+ -[BKSMutableHIDEventSimpleProvenance copyWithZone:]
+ -[BKSMutableHIDEventSimpleProvenance setEventType:]
+ -[BKSMutableHIDEventSimpleProvenance setSignature:]
+ -[BKSMutableHIDEventSimpleProvenance setTimestamp:]
+ -[BKSMutableHIDEventSimpleProvenance setVersionedPID:]
+ -[BKSMutableTouchHitTestFilterParameters copyWithZone:]
+ -[BKSMutableTouchHitTestFilterParameters setContextIDs:]
+ -[BKSMutableTouchHitTestFilterParameters setSenderDescriptors:]
+ -[BKSTouchEventService _updateServerHitTestFilterParameters]
+ -[BKSTouchEventService excludeEventsFromSenders:fromHitTestingToContextIDs:]
+ -[BKSTouchHitTestFilterParameters .cxx_destruct]
+ -[BKSTouchHitTestFilterParameters _initWithCopyOf:]
+ -[BKSTouchHitTestFilterParameters _init]
+ -[BKSTouchHitTestFilterParameters appendDescriptionToStream:]
+ -[BKSTouchHitTestFilterParameters contextIDs]
+ -[BKSTouchHitTestFilterParameters copyWithZone:]
+ -[BKSTouchHitTestFilterParameters description]
+ -[BKSTouchHitTestFilterParameters encodeWithCoder:]
+ -[BKSTouchHitTestFilterParameters hash]
+ -[BKSTouchHitTestFilterParameters initForProtobufDecoding]
+ -[BKSTouchHitTestFilterParameters initWithCoder:]
+ -[BKSTouchHitTestFilterParameters init]
+ -[BKSTouchHitTestFilterParameters isEqual:]
+ -[BKSTouchHitTestFilterParameters mutableCopyWithZone:]
+ -[BKSTouchHitTestFilterParameters senderDescriptors]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken _identifierOfCGSConnection]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken _initWithCGSConnectionID:]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken _isIdentifierOfCGSConnection]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken appendDescriptionToFormatter:]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken description]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken encodeWithCoder:]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken hash]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken initForProtobufDecoding]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken initWithCoder:]
+ -[_BKSHIDCGSConnectionIDEventDeferringToken isEqual:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken _identifierOfCGSWindow]
+ -[_BKSHIDCGSWindowIDEventDeferringToken _initWithCGSWindowID:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken _isIdentifierOfCGSWindow]
+ -[_BKSHIDCGSWindowIDEventDeferringToken appendDescriptionToFormatter:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken description]
+ -[_BKSHIDCGSWindowIDEventDeferringToken encodeWithCoder:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken hash]
+ -[_BKSHIDCGSWindowIDEventDeferringToken initForProtobufDecoding]
+ -[_BKSHIDCGSWindowIDEventDeferringToken initWithCoder:]
+ -[_BKSHIDCGSWindowIDEventDeferringToken isEqual:]
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1208
+ GCC_except_table1231
+ GCC_except_table1252
+ GCC_except_table1385
+ GCC_except_table1389
+ GCC_except_table1399
+ GCC_except_table1522
+ GCC_except_table1638
+ GCC_except_table1766
+ GCC_except_table1889
+ GCC_except_table1898
+ GCC_except_table2031
+ GCC_except_table2139
+ GCC_except_table2141
+ GCC_except_table2171
+ GCC_except_table2350
+ GCC_except_table2515
+ GCC_except_table2522
+ GCC_except_table2787
+ GCC_except_table2802
+ GCC_except_table2962
+ _BKSDisplayServicesSetCalibrationPhaseWithEventType
+ _BKSDisplayServicesSetReachabilityBounds
+ _BKSHIDServicesExcludeCAContextsFromHitTestingForZoomSenders.sPreviousAssertion
+ _BSContinuousMachTimeNow
+ _CGRectContainsPoint
+ _CGRectIsEmpty
+ _NSStringFromBKSHitTestRegionLocation
+ _OBJC_CLASS_$_BKSHIDEventCollectionDescriptor
+ _OBJC_CLASS_$_BKSHIDEventDeferringChangeBasis
+ _OBJC_CLASS_$_BKSHIDEventDeferringConstraint
+ _OBJC_CLASS_$_BKSHIDEventDeferringConstraintAssertion
+ _OBJC_CLASS_$_BKSHIDEventDeferringModality
+ _OBJC_CLASS_$_BKSHIDEventDeferringModalityAssertion
+ _OBJC_CLASS_$_BKSHIDEventDeferringSelectionChangeRequest
+ _OBJC_CLASS_$_BKSHIDEventDeferringSelectionPathIdentifier
+ _OBJC_CLASS_$_BKSHIDEventDeferringSelectionPathSymbol
+ _OBJC_CLASS_$_BKSHIDEventDeferringSelectionTarget
+ _OBJC_CLASS_$_BKSHIDEventDeliveryPolicy
+ _OBJC_CLASS_$_BKSHIDEventSimpleProvenance
+ _OBJC_CLASS_$_BKSHIDEventSimpleProvenanceOriginator
+ _OBJC_CLASS_$_BKSHIDEventUnitTestableProvenance
+ _OBJC_CLASS_$_BKSHIDServiceConnectionFactory
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringConstraint
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringConstraintAssertion
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringModality
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringModalityAssertion
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringSelectionChangeRequest
+ _OBJC_CLASS_$_BKSMutableHIDEventDeferringSelectionTarget
+ _OBJC_CLASS_$_BKSMutableHIDEventSimpleProvenance
+ _OBJC_CLASS_$_BKSMutableTouchHitTestFilterParameters
+ _OBJC_CLASS_$_BKSTouchHitTestFilterParameters
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_BSServiceInitiatingConnection
+ _OBJC_CLASS_$_BSServiceInitiatingConnectionMultiplexer
+ _OBJC_CLASS_$__BKSHIDCGSConnectionIDEventDeferringToken
+ _OBJC_CLASS_$__BKSHIDCGSWindowIDEventDeferringToken
+ _OBJC_IVAR_$_BKSHIDEventBaseAttributes._simpleProvenance
+ _OBJC_IVAR_$_BKSHIDEventDeferringChangeBasis._eventProvenance
+ _OBJC_IVAR_$_BKSHIDEventDeferringChangeBasis._identifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraint._identifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._basis
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._constraint
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._pathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._selectionTarget
+ _OBJC_IVAR_$_BKSHIDEventDeferringConstraintAssertion._timestamp
+ _OBJC_IVAR_$_BKSHIDEventDeferringModality._identifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringModalityAssertion._basis
+ _OBJC_IVAR_$_BKSHIDEventDeferringModalityAssertion._modality
+ _OBJC_IVAR_$_BKSHIDEventDeferringModalityAssertion._pathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringModalityAssertion._selectionTarget
+ _OBJC_IVAR_$_BKSHIDEventDeferringModalityAssertion._timestamp
+ _OBJC_IVAR_$_BKSHIDEventDeferringRule._restrictedToEventDescriptors
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionChangeRequest._basis
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionChangeRequest._ignoreModalities
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionChangeRequest._pathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionChangeRequest._selectionTarget
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionChangeRequest._timestamp
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionPathIdentifier._identifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionPathSymbol._identifier
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionTarget._display
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionTarget._environment
+ _OBJC_IVAR_$_BKSHIDEventDeferringSelectionTarget._target
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._containsEndOfChain
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._containsSubset
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._modalities
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChain._selectionPath
+ _OBJC_IVAR_$_BKSHIDEventDeliveryChainObserver._chainIdentity
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._asyncResultQueue
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_constraintAssertSeed
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_constraintAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_lastSentConstraintAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_lastSentModalityAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_modalityAssertSeed
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_modalityAsserts
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_pendingQueriesToBeExecutedInsideLockOnceActivationHappens
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_remoteTargetSafeToMessage
+ _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_selectionRequests
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicy._deferringPolicyStatus
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicy._finalStringTokenInChain
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicyObserver._asyncObserverCalloutQueue
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicyObserver._lock_currentPolicy
+ _OBJC_IVAR_$_BKSHIDEventDeliveryPolicyObserver._lock_selectionPathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventDeliveryRuleChangeTransaction._constraintAssertions
+ _OBJC_IVAR_$_BKSHIDEventDeliveryRuleChangeTransaction._modalityAssertions
+ _OBJC_IVAR_$_BKSHIDEventDeliveryRuleChangeTransaction._selectionRequests
+ _OBJC_IVAR_$_BKSHIDEventDigitizerPathAttributes._simpleProvenance
+ _OBJC_IVAR_$_BKSHIDEventDispatchingTarget._selectionPathIdentifier
+ _OBJC_IVAR_$_BKSHIDEventObserver._isNonLaunchingServer
+ _OBJC_IVAR_$_BKSHIDEventObserver._lock_hasReceivedLatestDeferringObservationsFromServer
+ _OBJC_IVAR_$_BKSHIDEventObserver._lock_waitingOnServerHandshake
+ _OBJC_IVAR_$_BKSHIDEventPolicyObservation._finalStringToken
+ _OBJC_IVAR_$_BKSHIDEventPolicyObservation._selectionPath
+ _OBJC_IVAR_$_BKSHIDEventSimpleProvenance._eventType
+ _OBJC_IVAR_$_BKSHIDEventSimpleProvenance._signature
+ _OBJC_IVAR_$_BKSHIDEventSimpleProvenance._timestamp
+ _OBJC_IVAR_$_BKSHIDEventSimpleProvenance._versionedPID
+ _OBJC_IVAR_$_BKSHIDEventSimpleProvenanceOriginator._key
+ _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._authentic
+ _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._eventType
+ _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._timetamp
+ _OBJC_IVAR_$_BKSHIDEventUnitTestableProvenance._versionedPID
+ _OBJC_IVAR_$_BKSProximitySensorService._bsServiceDispatchQueue
+ _OBJC_IVAR_$_BKSTouchDeliveryObservationService._bsServiceDispatchQueue
+ _OBJC_IVAR_$_BKSTouchEventService._hitTestFilterParameters
+ _OBJC_IVAR_$_BKSTouchHitTestFilterParameters._contextIDs
+ _OBJC_IVAR_$_BKSTouchHitTestFilterParameters._senderDescriptors
+ _OBJC_IVAR_$__BKSHIDCGSConnectionIDEventDeferringToken._CGSConnectionID
+ _OBJC_IVAR_$__BKSHIDCGSWindowIDEventDeferringToken._CGSWindowID
+ _OBJC_METACLASS_$_BKSHIDEventCollectionDescriptor
+ _OBJC_METACLASS_$_BKSHIDEventDeferringChangeBasis
+ _OBJC_METACLASS_$_BKSHIDEventDeferringConstraint
+ _OBJC_METACLASS_$_BKSHIDEventDeferringConstraintAssertion
+ _OBJC_METACLASS_$_BKSHIDEventDeferringModality
+ _OBJC_METACLASS_$_BKSHIDEventDeferringModalityAssertion
+ _OBJC_METACLASS_$_BKSHIDEventDeferringSelectionChangeRequest
+ _OBJC_METACLASS_$_BKSHIDEventDeferringSelectionPathIdentifier
+ _OBJC_METACLASS_$_BKSHIDEventDeferringSelectionPathSymbol
+ _OBJC_METACLASS_$_BKSHIDEventDeferringSelectionTarget
+ _OBJC_METACLASS_$_BKSHIDEventDeliveryPolicy
+ _OBJC_METACLASS_$_BKSHIDEventSimpleProvenance
+ _OBJC_METACLASS_$_BKSHIDEventSimpleProvenanceOriginator
+ _OBJC_METACLASS_$_BKSHIDEventUnitTestableProvenance
+ _OBJC_METACLASS_$_BKSHIDServiceConnectionFactory
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringConstraint
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringConstraintAssertion
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringModality
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringModalityAssertion
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringSelectionChangeRequest
+ _OBJC_METACLASS_$_BKSMutableHIDEventDeferringSelectionTarget
+ _OBJC_METACLASS_$_BKSMutableHIDEventSimpleProvenance
+ _OBJC_METACLASS_$_BKSMutableTouchHitTestFilterParameters
+ _OBJC_METACLASS_$_BKSTouchHitTestFilterParameters
+ _OBJC_METACLASS_$__BKSHIDCGSConnectionIDEventDeferringToken
+ _OBJC_METACLASS_$__BKSHIDCGSWindowIDEventDeferringToken
+ _QuartzCoreLibrary.11878
+ _QuartzCoreLibraryCore.frameworkLibrary.11893
+ _QuartzCoreLibraryCore.frameworkLibrary.8152
+ _QuartzCoreLibraryCore.frameworkLibrary.8961
+ __BKSDisplaySetReachabilityBounds
+ __OBJC_$_CLASS_METHODS_BKSHIDEventCollectionDescriptor
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringChangeBasis
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringConstraint
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringModality
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringModalityAssertion
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_CLASS_METHODS_BKSHIDEventDeferringSelectionTarget
+ __OBJC_$_CLASS_METHODS_BKSHIDEventSimpleProvenance
+ __OBJC_$_CLASS_METHODS_BKSHIDEventUnitTestableProvenance
+ __OBJC_$_CLASS_METHODS_BKSTouchHitTestFilterParameters
+ __OBJC_$_CLASS_METHODS__BKSHIDCGSConnectionIDEventDeferringToken
+ __OBJC_$_CLASS_METHODS__BKSHIDCGSWindowIDEventDeferringToken
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringChangeBasis
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringConstraint
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringModality
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringModalityAssertion
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventDeferringSelectionTarget
+ __OBJC_$_CLASS_PROP_LIST_BKSHIDEventSimpleProvenance
+ __OBJC_$_CLASS_PROP_LIST_BKSMutableHIDEventSimpleProvenance
+ __OBJC_$_CLASS_PROP_LIST_BKSTouchHitTestFilterParameters
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventCollectionDescriptor
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringChangeBasis
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringConstraint
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringModality
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringModalityAssertion
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeferringSelectionTarget
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventDeliveryPolicy
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventSimpleProvenance
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventSimpleProvenanceOriginator
+ __OBJC_$_INSTANCE_METHODS_BKSHIDEventUnitTestableProvenance
+ __OBJC_$_INSTANCE_METHODS_BKSHIDServiceConnectionFactory
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringConstraint
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringConstraintAssertion
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringModality
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringModalityAssertion
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventDeferringSelectionTarget
+ __OBJC_$_INSTANCE_METHODS_BKSMutableHIDEventSimpleProvenance
+ __OBJC_$_INSTANCE_METHODS_BKSMutableTouchHitTestFilterParameters
+ __OBJC_$_INSTANCE_METHODS_BKSTouchHitTestFilterParameters
+ __OBJC_$_INSTANCE_METHODS__BKSHIDCGSConnectionIDEventDeferringToken
+ __OBJC_$_INSTANCE_METHODS__BKSHIDCGSWindowIDEventDeferringToken
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringChangeBasis
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringConstraint
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringModality
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringModalityAssertion
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeferringSelectionTarget
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventDeliveryPolicy
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventSimpleProvenance
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventSimpleProvenanceOriginator
+ __OBJC_$_INSTANCE_VARIABLES_BKSHIDEventUnitTestableProvenance
+ __OBJC_$_INSTANCE_VARIABLES_BKSTouchHitTestFilterParameters
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDCGSConnectionIDEventDeferringToken
+ __OBJC_$_INSTANCE_VARIABLES__BKSHIDCGSWindowIDEventDeferringToken
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringChangeBasis
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringConstraint
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringModality
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringModalityAssertion
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_PROP_LIST_BKSHIDEventDeferringSelectionTarget
+ __OBJC_$_PROP_LIST_BKSHIDEventDeliveryPolicy
+ __OBJC_$_PROP_LIST_BKSHIDEventProvenance
+ __OBJC_$_PROP_LIST_BKSHIDEventSimpleProvenance
+ __OBJC_$_PROP_LIST_BKSHIDEventUnitTestableProvenance
+ __OBJC_$_PROP_LIST_BKSHIDServiceConnectionFactory
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringConstraint
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringConstraintAssertion
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringModality
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringModalityAssertion
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringSelectionChangeRequest
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventDeferringSelectionTarget
+ __OBJC_$_PROP_LIST_BKSMutableHIDEventSimpleProvenance
+ __OBJC_$_PROP_LIST_BKSMutableTouchHitTestFilterParameters
+ __OBJC_$_PROP_LIST_BKSTouchHitTestFilterParameters
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDEventProvenance
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSHIDServiceConnectionFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDEventProvenance
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSHIDServiceConnectionFactory
+ __OBJC_$_PROTOCOL_REFS_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_$_PROTOCOL_REFS_BKSHIDEventProvenance
+ __OBJC_$_PROTOCOL_REFS_BKSHIDServiceConnectionFactory
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringChangeBasis
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringConstraint
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringModality
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringModalityAssertion
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeferringSelectionTarget
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventDeliveryPolicy
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventSimpleProvenance
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDEventUnitTestableProvenance
+ __OBJC_CLASS_PROTOCOLS_$_BKSHIDServiceConnectionFactory
+ __OBJC_CLASS_PROTOCOLS_$_BKSMutableHIDEventSimpleProvenance
+ __OBJC_CLASS_PROTOCOLS_$_BKSTouchHitTestFilterParameters
+ __OBJC_CLASS_RO_$_BKSHIDEventCollectionDescriptor
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringChangeBasis
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringConstraint
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringModality
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringModalityAssertion
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_CLASS_RO_$_BKSHIDEventDeferringSelectionTarget
+ __OBJC_CLASS_RO_$_BKSHIDEventDeliveryPolicy
+ __OBJC_CLASS_RO_$_BKSHIDEventSimpleProvenance
+ __OBJC_CLASS_RO_$_BKSHIDEventSimpleProvenanceOriginator
+ __OBJC_CLASS_RO_$_BKSHIDEventUnitTestableProvenance
+ __OBJC_CLASS_RO_$_BKSHIDServiceConnectionFactory
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringConstraint
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringConstraintAssertion
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringModality
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringModalityAssertion
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringSelectionChangeRequest
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventDeferringSelectionTarget
+ __OBJC_CLASS_RO_$_BKSMutableHIDEventSimpleProvenance
+ __OBJC_CLASS_RO_$_BKSMutableTouchHitTestFilterParameters
+ __OBJC_CLASS_RO_$_BKSTouchHitTestFilterParameters
+ __OBJC_CLASS_RO_$__BKSHIDCGSConnectionIDEventDeferringToken
+ __OBJC_CLASS_RO_$__BKSHIDCGSWindowIDEventDeferringToken
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDEventProvenance
+ __OBJC_LABEL_PROTOCOL_$_BKSHIDServiceConnectionFactory
+ __OBJC_METACLASS_RO_$_BKSHIDEventCollectionDescriptor
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringChangeBasis
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringConstraint
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringConstraintAssertion
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringModality
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringModalityAssertion
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringSelectionChangeRequest
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringSelectionPathIdentifier
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeferringSelectionTarget
+ __OBJC_METACLASS_RO_$_BKSHIDEventDeliveryPolicy
+ __OBJC_METACLASS_RO_$_BKSHIDEventSimpleProvenance
+ __OBJC_METACLASS_RO_$_BKSHIDEventSimpleProvenanceOriginator
+ __OBJC_METACLASS_RO_$_BKSHIDEventUnitTestableProvenance
+ __OBJC_METACLASS_RO_$_BKSHIDServiceConnectionFactory
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringConstraint
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringConstraintAssertion
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringModality
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringModalityAssertion
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringSelectionChangeRequest
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventDeferringSelectionTarget
+ __OBJC_METACLASS_RO_$_BKSMutableHIDEventSimpleProvenance
+ __OBJC_METACLASS_RO_$_BKSMutableTouchHitTestFilterParameters
+ __OBJC_METACLASS_RO_$_BKSTouchHitTestFilterParameters
+ __OBJC_METACLASS_RO_$__BKSHIDCGSConnectionIDEventDeferringToken
+ __OBJC_METACLASS_RO_$__BKSHIDCGSWindowIDEventDeferringToken
+ __OBJC_PROTOCOL_$_BKSHIDEventDeferringSelectionPathSymbol
+ __OBJC_PROTOCOL_$_BKSHIDEventProvenance
+ __OBJC_PROTOCOL_$_BKSHIDServiceConnectionFactory
+ ___108-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:]_block_invoke
+ ___28-[BKSTouchEventService init]_block_invoke_2
+ ___41-[BKSHIDEventDeliveryChain subsetForPID:]_block_invoke
+ ___41-[BKSTouchEventService _connectToService]_block_invoke.189
+ ___41-[BKSTouchEventService _connectToService]_block_invoke.191
+ ___45+[BKSHIDEventSimpleProvenance protobufSchema]_block_invoke
+ ___46+[BKSHIDEventDeferringModality protobufSchema]_block_invoke
+ ___46-[BKSHitTestRegion appendDescriptionToStream:]_block_invoke
+ ___48+[BKSHIDServiceConnectionFactory sharedInstance]_block_invoke
+ ___49+[BKSTouchHitTestFilterParameters protobufSchema]_block_invoke
+ ___50+[BKSHIDEventDeferringChangeBasis constraintBasis]_block_invoke
+ ___50+[BKSHIDEventDeferringConstraint simpleConstraint]_block_invoke
+ ___50+[BKSHIDEventDeferringConstraint simpleConstraint]_block_invoke_2
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.106
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke.107
+ ___50-[BKSHIDEventObserver _initWithConnectionFactory:]_block_invoke_2
+ ___51+[BKSHIDEventDeferringModality activeInputModality]_block_invoke
+ ___51+[BKSHIDEventDeferringModality activeInputModality]_block_invoke_2
+ ___52-[BKSMousePointerService _activateServerConnection:]_block_invoke
+ ___52-[BKSMousePointerService _activateServerConnection:]_block_invoke.140
+ ___52-[BKSMousePointerService _activateServerConnection:]_block_invoke_2
+ ___54+[BKSHIDEventDeferringChangeBasis ruleOriginatorBasis]_block_invoke
+ ___54+[BKSHIDEventDeferringSelectionPathIdentifier primary]_block_invoke
+ ___55+[_BKSHIDCGSWindowIDEventDeferringToken protobufSchema]_block_invoke
+ ___55+[_BKSHIDCGSWindowIDEventDeferringToken protobufSchema]_block_invoke_2
+ ___55-[BKSHIDEventDeliveryManager deliveryGraphDescription:]_block_invoke
+ ___55-[BKSHIDEventDeliveryPolicy appendDescriptionToStream:]_block_invoke
+ ___56-[BKSHIDEventDeliveryManager appendDescriptionToStream:]_block_invoke
+ ___56-[BKSHIDEventDeliveryManager deliveryChainsDescription:]_block_invoke
+ ___57+[BKSHIDEventDeferringSelectionPathSymbol protobufSchema]_block_invoke
+ ___57+[BKSHIDEventDeferringSelectionPathSymbol protobufSchema]_block_invoke_2
+ ___57-[BKSHIDEventSimpleProvenanceOriginator buildProvenance:]_block_invoke
+ ___59+[_BKSHIDCGSConnectionIDEventDeferringToken protobufSchema]_block_invoke
+ ___59+[_BKSHIDCGSConnectionIDEventDeferringToken protobufSchema]_block_invoke_2
+ ___60-[BKSProximitySensorService _connectToRemoteServiceIfNeeded]_block_invoke.62
+ ___61+[BKSHIDEventDeferringSelectionPathIdentifier genericGesture]_block_invoke
+ ___61+[BKSHIDEventDeferringSelectionPathIdentifier protobufSchema]_block_invoke
+ ___61+[BKSHIDEventDeferringSelectionPathIdentifier protobufSchema]_block_invoke_2
+ ___62-[BKSHIDEventDeliveryManager _executeDescriptionFetch:result:]_block_invoke
+ ___62-[BKSHIDEventDeliveryManager _executeDescriptionFetch:result:]_block_invoke_2
+ ___64-[BKSHIDEventDeliveryPolicyObserver deferringResolutionsChanged]_block_invoke.83
+ ___64-[BKSHIDEventDeliveryPolicyObserver setSelectionPathIdentifier:]_block_invoke
+ ___65+[BKSHIDEventDeferringSelectionPathIdentifier everySelectionPath]_block_invoke
+ ___68-[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:]_block_invoke
+ ___68-[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:]_block_invoke.103
+ ___68-[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:]_block_invoke.104
+ ___68-[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:]_block_invoke_2
+ ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:hasModality:basis:]_block_invoke
+ ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:hasModality:basis:]_block_invoke_2
+ ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:]_block_invoke
+ ___75-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:]_block_invoke_2
+ ___75-[BKSHIDEventDeliveryPolicyObserver _notifyAsyncObservers:didUpdatePolicy:]_block_invoke
+ ___76-[BKSTouchEventService excludeEventsFromSenders:fromHitTestingToContextIDs:]_block_invoke
+ ___79-[BKSHIDEventDeliveryManager resolutionDescriptionForKeyCommand:sender:result:]_block_invoke
+ ___80-[BKSHIDEventDeliveryManager changeSelectionPath:target:basis:ignoreModalities:]_block_invoke
+ ___83-[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleIdentity:result:]_block_invoke
+ ___84-[BKSHIDEventDeliveryManager resolutionDescriptionForEventDescriptor:sender:result:]_block_invoke
+ ___96-[BKSHIDServiceConnectionFactory clientConnectionForServiceWithName:multiplexer:isNonLaunching:]_block_invoke
+ ___99-[BKSHIDEventDeliveryPolicyObserver _replacePolicySpecificationObject:withObject:replaceIvarBlock:]_block_invoke
+ ___BKSHIDServicesExcludeCAContextsFromHitTestingForZoomSenders_block_invoke
+ ___BKSHIDServicesExcludeCAContextsFromHitTestingForZoomSenders_block_invoke_2
+ ___Block_byref_object_copy_.9945
+ ___Block_byref_object_dispose_.9946
+ ___QuartzCoreLibraryCore_block_invoke.11894
+ ___QuartzCoreLibraryCore_block_invoke.8153
+ ___QuartzCoreLibraryCore_block_invoke.8962
+ ___block_descriptor_32_e45_v16?0"BKSMutableHIDEventDeferringModality"8l
+ ___block_descriptor_32_e47_v16?0"BKSMutableHIDEventDeferringConstraint"8l
+ ___block_descriptor_32_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_40_e8_32bs_e44_v16?0"BKSMutableHIDEventSimpleProvenance"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_v16?0"BKSHIDEventDeliveryPolicyObserver"8ls32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8ls32l8
+ ___block_descriptor_40_e8_32s_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e63_"NSString"16?0"<BKSHIDEventDeliveryManagerServerInterface>"8ls32l8
+ ___block_descriptor_40_e8_32s_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_40_e8_32w_e67_v16?0"BSServiceInitiatingConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e48_v16?0"BKSMutableTouchHitTestFilterParameters"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e63_"NSString"16?0"<BKSHIDEventDeliveryManagerServerInterface>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e52_v16?0"<BSServiceInitiatingConnectionConfiguring>"8ls32l8w40l8
+ ___block_descriptor_52_e8_32r40r_e36_B16?0"BKSHIDEventDeferringTarget"8lr32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e65_v24?0"<BKSHIDEventDeliveryManagerServerInterface>"8"NSError"16ls40l8s32l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e56_v16?0"BKSMutableHIDEventDeferringConstraintAssertion"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e63_"NSString"16?0"<BKSHIDEventDeliveryManagerServerInterface>"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e59_v16?0"BKSMutableHIDEventDeferringSelectionChangeRequest"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e54_v16?0"BKSMutableHIDEventDeferringModalityAssertion"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10007
+ ___block_literal_global.10188
+ ___block_literal_global.102
+ ___block_literal_global.10428
+ ___block_literal_global.1064
+ ___block_literal_global.10680
+ ___block_literal_global.109
+ ___block_literal_global.113
+ ___block_literal_global.11479
+ ___block_literal_global.11663
+ ___block_literal_global.11869
+ ___block_literal_global.1189
+ ___block_literal_global.11962
+ ___block_literal_global.12
+ ___block_literal_global.12091
+ ___block_literal_global.12603
+ ___block_literal_global.12836
+ ___block_literal_global.13106
+ ___block_literal_global.13207
+ ___block_literal_global.13312
+ ___block_literal_global.13445
+ ___block_literal_global.136.5332
+ ___block_literal_global.13729
+ ___block_literal_global.139
+ ___block_literal_global.13945
+ ___block_literal_global.142
+ ___block_literal_global.14501
+ ___block_literal_global.150
+ ___block_literal_global.1541
+ ___block_literal_global.16.8069
+ ___block_literal_global.169
+ ___block_literal_global.1717
+ ___block_literal_global.18.9144
+ ___block_literal_global.1846
+ ___block_literal_global.187
+ ___block_literal_global.193
+ ___block_literal_global.2.12833
+ ___block_literal_global.218
+ ___block_literal_global.22.10169
+ ___block_literal_global.2232
+ ___block_literal_global.2386
+ ___block_literal_global.24
+ ___block_literal_global.246
+ ___block_literal_global.25.8078
+ ___block_literal_global.2520
+ ___block_literal_global.2678
+ ___block_literal_global.2811
+ ___block_literal_global.3.1191
+ ___block_literal_global.3.13948
+ ___block_literal_global.3082
+ ___block_literal_global.31.8084
+ ___block_literal_global.310
+ ___block_literal_global.320
+ ___block_literal_global.3237
+ ___block_literal_global.357
+ ___block_literal_global.3904
+ ___block_literal_global.4078
+ ___block_literal_global.409
+ ___block_literal_global.426
+ ___block_literal_global.438
+ ___block_literal_global.4512
+ ___block_literal_global.4589
+ ___block_literal_global.4804
+ ___block_literal_global.4974
+ ___block_literal_global.503
+ ___block_literal_global.5179
+ ___block_literal_global.5409
+ ___block_literal_global.553
+ ___block_literal_global.5530
+ ___block_literal_global.5727
+ ___block_literal_global.6024
+ ___block_literal_global.6264
+ ___block_literal_global.64
+ ___block_literal_global.64.3905
+ ___block_literal_global.6409
+ ___block_literal_global.659
+ ___block_literal_global.6748
+ ___block_literal_global.6762
+ ___block_literal_global.677
+ ___block_literal_global.695
+ ___block_literal_global.75.9973
+ ___block_literal_global.7724
+ ___block_literal_global.7902
+ ___block_literal_global.7904
+ ___block_literal_global.7985
+ ___block_literal_global.80
+ ___block_literal_global.8058
+ ___block_literal_global.8390
+ ___block_literal_global.85
+ ___block_literal_global.8690
+ ___block_literal_global.90
+ ___block_literal_global.9157
+ ___block_literal_global.92
+ ___block_literal_global.93
+ ___block_literal_global.9352
+ ___block_literal_global.957
+ ___block_literal_global.9682
+ ___block_literal_global.9822
+ ___getCADisplayClass_block_invoke.8960
+ _activeInputModality.modality
+ _activeInputModality.onceToken
+ _audit_stringQuartzCore.11897
+ _audit_stringQuartzCore.8168
+ _audit_stringQuartzCore.8977
+ _constraintBasis.basis
+ _constraintBasis.onceToken
+ _everySelectionPath.onceToken
+ _everySelectionPath.symbol
+ _genericGesture.genericGesture
+ _genericGesture.onceToken
+ _getCADisplayClass.8958
+ _getCADisplayClass.softClass.8959
+ _objc_msgSend$_activateServerConnection:
+ _objc_msgSend$_classForAttributeType:
+ _objc_msgSend$_eventAttributeType
+ _objc_msgSend$_executeDescriptionFetch:result:
+ _objc_msgSend$_identifierOfCGSWindow
+ _objc_msgSend$_initWithCGSWindowID:
+ _objc_msgSend$_initWithConnectionFactory:
+ _objc_msgSend$_initWithConnectionFactory:forTesting:
+ _objc_msgSend$_initWithEnvironment:token:selectionPath:pid:
+ _objc_msgSend$_initWithPolicyObservation:
+ _objc_msgSend$_initWithPredicate:restrictedToEventDescriptors:target:reason:identity:
+ _objc_msgSend$_lock_buildCurrentPolicy
+ _objc_msgSend$_lock_effectivePolicyObservation
+ _objc_msgSend$_lock_flushInitialStateToServer
+ _objc_msgSend$_lock_noteServerInterruption
+ _objc_msgSend$_lock_pendQuery:
+ _objc_msgSend$_lock_updatePolicyWithBlock:
+ _objc_msgSend$_notifyAsyncObservers:didUpdatePolicy:
+ _objc_msgSend$_replacePolicySpecificationObject:withObject:replaceIvarBlock:
+ _objc_msgSend$_substituteSingeltonForIdentifierString:
+ _objc_msgSend$_updateServerHitTestFilterParameters
+ _objc_msgSend$_verifySignatureWithInternalKey:
+ _objc_msgSend$_withInternalKey:buildMessage:
+ _objc_msgSend$appendUInt64:withName:
+ _objc_msgSend$bs_filter:
+ _objc_msgSend$chainIdentity
+ _objc_msgSend$clientConnectionForServiceWithName:isNonLaunching:
+ _objc_msgSend$clientConnectionForServiceWithName:multiplexer:
+ _objc_msgSend$configure:
+ _objc_msgSend$connectionDescriptionForDeferringRuleIdentity:result:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$defaultMultiplexer
+ _objc_msgSend$deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:
+ _objc_msgSend$deferringPolicyStatus
+ _objc_msgSend$deliveryChainsDescription
+ _objc_msgSend$deliveryPolicyObserver:policyDidChange:
+ _objc_msgSend$deserializeFromBytes:byteCount:
+ _objc_msgSend$everySelectionPath
+ _objc_msgSend$excludeEventsFromSenders:fromHitTestingToContextIDs:
+ _objc_msgSend$finalStringTokenInChain
+ _objc_msgSend$genericGesture
+ _objc_msgSend$hasReceivedLatestDeferringObservationsFromServer
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$initWithEventProvenance:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:
+ _objc_msgSend$isFinalStringToken
+ _objc_msgSend$isNonLaunching
+ _objc_msgSend$primary
+ _objc_msgSend$provenance
+ _objc_msgSend$queue
+ _objc_msgSend$queueWithName:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$replaceBytesInRange:withBytes:length:
+ _objc_msgSend$ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:seed:pid:
+ _objc_msgSend$ruleOriginatorBasis
+ _objc_msgSend$selectionPath
+ _objc_msgSend$selectionPathIdentifier
+ _objc_msgSend$setActivationHandler:
+ _objc_msgSend$setBasis:
+ _objc_msgSend$setClientMessagingExpectation:
+ _objc_msgSend$setConstraint:
+ _objc_msgSend$setConstraintAssertions:
+ _objc_msgSend$setContextIDs:
+ _objc_msgSend$setHitTestFilterParameters:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setIgnoreModalities:
+ _objc_msgSend$setModality:
+ _objc_msgSend$setModalityAssertions:
+ _objc_msgSend$setMultiplexer:
+ _objc_msgSend$setPathIdentifier:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setSelectionRequests:
+ _objc_msgSend$setSelectionTarget:
+ _objc_msgSend$setSenderID:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$target
+ _objc_msgSend$userInteractiveMultiplexer
+ _primary.onceToken
+ _primary.primary
+ _protobufSchema.onceToken.100
+ _protobufSchema.onceToken.13097
+ _protobufSchema.onceToken.13443
+ _protobufSchema.onceToken.137
+ _protobufSchema.onceToken.13726
+ _protobufSchema.onceToken.1538
+ _protobufSchema.onceToken.2510
+ _protobufSchema.onceToken.2808
+ _protobufSchema.onceToken.308
+ _protobufSchema.onceToken.318
+ _protobufSchema.onceToken.4075
+ _protobufSchema.onceToken.436
+ _protobufSchema.onceToken.5177
+ _protobufSchema.onceToken.551
+ _protobufSchema.onceToken.6262
+ _protobufSchema.onceToken.6407
+ _protobufSchema.onceToken.657
+ _protobufSchema.onceToken.675
+ _protobufSchema.onceToken.693
+ _protobufSchema.onceToken.8387
+ _protobufSchema.onceToken.91
+ _protobufSchema.onceToken.9349
+ _protobufSchema.onceToken.9819
+ _protobufSchema.schema.13098
+ _protobufSchema.schema.13444
+ _protobufSchema.schema.136
+ _protobufSchema.schema.13727
+ _protobufSchema.schema.1539
+ _protobufSchema.schema.2511
+ _protobufSchema.schema.2809
+ _protobufSchema.schema.307
+ _protobufSchema.schema.317
+ _protobufSchema.schema.4076
+ _protobufSchema.schema.435
+ _protobufSchema.schema.5178
+ _protobufSchema.schema.550
+ _protobufSchema.schema.6263
+ _protobufSchema.schema.6408
+ _protobufSchema.schema.656
+ _protobufSchema.schema.674
+ _protobufSchema.schema.692
+ _protobufSchema.schema.8388
+ _protobufSchema.schema.90
+ _protobufSchema.schema.9350
+ _protobufSchema.schema.9820
+ _protobufSchema.schema.99
+ _ruleOriginatorBasis.basis
+ _ruleOriginatorBasis.onceToken
+ _sharedInstance.__shared.13208
+ _sharedInstance.__sharedInstance.11511
+ _sharedInstance.controller.6763
+ _sharedInstance.onceToken.10006
+ _sharedInstance.onceToken.11510
+ _sharedInstance.onceToken.13206
+ _sharedInstance.onceToken.13578
+ _sharedInstance.onceToken.186
+ _sharedInstance.onceToken.4511
+ _sharedInstance.onceToken.5408
+ _sharedInstance.onceToken.6747
+ _sharedInstance.onceToken.6761
+ _sharedInstance.onceToken.7901
+ _sharedInstance.onceToken.956
+ _sharedInstance.service.13579
+ _sharedInstance.service.188
+ _sharedInstance.service.5410
+ _sharedInstance.service.958
+ _simpleConstraint.constraint
+ _simpleConstraint.onceToken
- +[BKSHIDServiceConnection clientConnectionForServiceWithName:]
- +[_BKSHIDCGSConnectIDEventDeferringToken protobufSchema]
- +[_BKSHIDCGSConnectIDEventDeferringToken supportsSecureCoding]
- -[BKSHIDEventDeferringRule _initWithPredicate:target:reason:identity:]
- -[BKSHIDEventDeliveryManager _coreSetUpWithServiceConnection:]
- -[BKSHIDEventDeliveryManager _initForTestingWithService:]
- -[BKSHIDEventDeliveryManager _initWithRemoteConnection]
- -[BKSHIDEventDeliveryManager _reconnectAfterServerInterruption]
- -[BKSHIDEventDeliveryManager appendDescriptionToFormatter:]
- -[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleIdentity:]
- -[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleWithSeed:pid:]
- -[BKSHIDEventDeliveryManager deliveryGraphDescription]
- -[BKSHIDEventDeliveryManager requestActiveUIResponderForDeferringPredicate:withReason:]
- -[BKSHIDEventDeliveryManager resolutionDescriptionForEventDescriptor:sender:]
- -[BKSHIDEventDeliveryManager resolutionDescriptionForKeyCommand:sender:]
- -[BKSHIDEventDeliveryManager selectDeferringPredicate:withReason:]
- -[BKSHIDEventDeliveryPolicyObserver _lock_policyStatus]
- -[BKSHIDEventDeliveryPolicyObserver _lock_updateStateWithBlock:]
- -[BKSHIDEventDeliveryRuleChangeTransaction activeUIResponders]
- -[BKSHIDEventDeliveryRuleChangeTransaction setActiveUIResponders:]
- -[BKSHIDEventDispatchingTarget _initWithEnvironment:token:pid:]
- -[BKSHIDEventObserver _init]
- -[BKSHIDEventPolicyObservation appendDescriptionToFormatter:]
- -[BKSHitTestRegion appendDescriptionToFormatter:]
- -[BKSMousePointerService _activateServerConnection]
- -[_BKSHIDCGSConnectIDEventDeferringToken _identifierOfCGSConnection]
- -[_BKSHIDCGSConnectIDEventDeferringToken _initWithCGSConnectionID:]
- -[_BKSHIDCGSConnectIDEventDeferringToken _isIdentifierOfCGSConnection]
- -[_BKSHIDCGSConnectIDEventDeferringToken appendDescriptionToFormatter:]
- -[_BKSHIDCGSConnectIDEventDeferringToken description]
- -[_BKSHIDCGSConnectIDEventDeferringToken encodeWithCoder:]
- -[_BKSHIDCGSConnectIDEventDeferringToken hash]
- -[_BKSHIDCGSConnectIDEventDeferringToken initForProtobufDecoding]
- -[_BKSHIDCGSConnectIDEventDeferringToken initWithCoder:]
- -[_BKSHIDCGSConnectIDEventDeferringToken isEqual:]
- GCC_except_table1019
- GCC_except_table1135
- GCC_except_table1139
- GCC_except_table1149
- GCC_except_table1329
- GCC_except_table1452
- GCC_except_table1566
- GCC_except_table1575
- GCC_except_table1703
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table1843
- GCC_except_table2022
- GCC_except_table2149
- GCC_except_table2156
- GCC_except_table2417
- GCC_except_table2429
- GCC_except_table2590
- GCC_except_table865
- GCC_except_table866
- GCC_except_table976
- GCC_except_table998
- _BKSHIDEventGetKeyCommandResolutionDescription
- _BKSHIDEventGetResolutionDescription
- _BKSHIDServicesGetDeviceBacklightArchitectureVersion
- _BSDispatchQueueCreate
- _BSDispatchQueueCreateSerialWithQoS
- _IOHIDEventGetTypeString
- _OBJC_CLASS_$_BKSHIDServiceConnection
- _OBJC_CLASS_$_BSDispatchQueueAttributes
- _OBJC_CLASS_$__BKSHIDCGSConnectIDEventDeferringToken
- _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_activeUIResponderPredicates
- _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_activeUIResponderSeed
- _OBJC_IVAR_$_BKSHIDEventDeliveryManager._lock_lastSentActiveUIResponderPredicates
- _OBJC_IVAR_$_BKSHIDEventDeliveryPolicyObserver._lock_policyStatus
- _OBJC_IVAR_$_BKSHIDEventDeliveryRuleChangeTransaction._activeUIResponders
- _OBJC_IVAR_$_BKSHIDEventObserver._calloutQueue
- _OBJC_IVAR_$_BKSTouchEventService._requestQueue
- _OBJC_IVAR_$__BKSHIDCGSConnectIDEventDeferringToken._CGSConnectionID
- _OBJC_METACLASS_$_BKSHIDServiceConnection
- _OBJC_METACLASS_$__BKSHIDCGSConnectIDEventDeferringToken
- _QuartzCoreLibrary.9861
- _QuartzCoreLibraryCore.frameworkLibrary.6380
- _QuartzCoreLibraryCore.frameworkLibrary.7150
- _QuartzCoreLibraryCore.frameworkLibrary.9881
- __BKSDisplayGetBlankingRemovesPower
- __BKSDisplaySetBlankingRemovesPower
- __BKSHIDExcludeCAContextsFromHitTestingForZoomSenders
- __BKSHIDGetDeviceBacklightArchitectureVersion
- __OBJC_$_CLASS_METHODS_BKSHIDServiceConnection
- __OBJC_$_CLASS_METHODS__BKSHIDCGSConnectIDEventDeferringToken
- __OBJC_$_INSTANCE_METHODS__BKSHIDCGSConnectIDEventDeferringToken
- __OBJC_$_INSTANCE_VARIABLES__BKSHIDCGSConnectIDEventDeferringToken
- __OBJC_CLASS_RO_$_BKSHIDServiceConnection
- __OBJC_CLASS_RO_$__BKSHIDCGSConnectIDEventDeferringToken
- __OBJC_METACLASS_RO_$_BKSHIDServiceConnection
- __OBJC_METACLASS_RO_$__BKSHIDCGSConnectIDEventDeferringToken
- ___28-[BKSHIDEventObserver _init]_block_invoke
- ___28-[BKSHIDEventObserver _init]_block_invoke_2
- ___28-[BKSHIDEventObserver _init]_block_invoke_3
- ___28-[BKSHitTestRegion isEqual:]_block_invoke
- ___28-[BKSHitTestRegion isEqual:]_block_invoke_2
- ___41-[BKSTouchEventService _connectToService]_block_invoke.170
- ___41-[BKSTouchEventService _connectToService]_block_invoke.172
- ___51-[BKSMousePointerService _activateServerConnection]_block_invoke
- ___51-[BKSMousePointerService _activateServerConnection]_block_invoke.139
- ___51-[BKSMousePointerService _activateServerConnection]_block_invoke_2
- ___55-[BKSHIDEventDeliveryManager _initWithRemoteConnection]_block_invoke
- ___55-[BKSHIDEventDeliveryManager _initWithRemoteConnection]_block_invoke_2
- ___55-[BKSHIDEventDeliveryManager _initWithRemoteConnection]_block_invoke_3
- ___56+[_BKSHIDCGSConnectIDEventDeferringToken protobufSchema]_block_invoke
- ___56+[_BKSHIDCGSConnectIDEventDeferringToken protobufSchema]_block_invoke_2
- ___59-[BKSHIDEventDeliveryManager appendDescriptionToFormatter:]_block_invoke
- ___60-[BKSProximitySensorService _connectToRemoteServiceIfNeeded]_block_invoke.58
- ___79-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:toTarget:withReason:]_block_invoke
- ___87-[BKSHIDEventDeliveryManager requestActiveUIResponderForDeferringPredicate:withReason:]_block_invoke
- ___Block_byref_object_copy_.8104
- ___Block_byref_object_dispose_.8105
- ___QuartzCoreLibraryCore_block_invoke.6381
- ___QuartzCoreLibraryCore_block_invoke.7151
- ___QuartzCoreLibraryCore_block_invoke.9882
- ___block_descriptor_40_e8_32s_e29_v16?0"BSServiceConnection"8ls32l8
- ___block_descriptor_40_e8_32s_e36_{CGRect={CGPoint=dd}{CGSize=dd}}8?0ls32l8
- ___block_descriptor_48_e8_32s40w_e29_v16?0"BSServiceConnection"8lw40l8s32l8
- ___block_literal_global.100.7820
- ___block_literal_global.10079
- ___block_literal_global.104
- ___block_literal_global.10553
- ___block_literal_global.10788
- ___block_literal_global.11065
- ___block_literal_global.11165
- ___block_literal_global.11270
- ___block_literal_global.11404
- ___block_literal_global.11672
- ___block_literal_global.118
- ___block_literal_global.11889
- ___block_literal_global.12468
- ___block_literal_global.1274
- ___block_literal_global.133
- ___block_literal_global.141
- ___block_literal_global.1459
- ___block_literal_global.151
- ___block_literal_global.1587
- ___block_literal_global.16.6299
- ___block_literal_global.165
- ___block_literal_global.170
- ___block_literal_global.18.7333
- ___block_literal_global.180
- ___block_literal_global.183
- ___block_literal_global.1973
- ___block_literal_global.2.10785
- ___block_literal_global.2117
- ___block_literal_global.22.8323
- ___block_literal_global.2245
- ___block_literal_global.23
- ___block_literal_global.2391
- ___block_literal_global.242
- ___block_literal_global.2503
- ___block_literal_global.2707
- ___block_literal_global.273
- ___block_literal_global.283
- ___block_literal_global.2885
- ___block_literal_global.31.6312
- ___block_literal_global.3216
- ___block_literal_global.3293
- ___block_literal_global.3509
- ___block_literal_global.353
- ___block_literal_global.3678
- ___block_literal_global.3865
- ___block_literal_global.404
- ___block_literal_global.4098
- ___block_literal_global.412
- ___block_literal_global.428
- ___block_literal_global.4319
- ___block_literal_global.4609
- ___block_literal_global.4808
- ___block_literal_global.5143
- ___block_literal_global.5157
- ___block_literal_global.518
- ___block_literal_global.521
- ___block_literal_global.53
- ___block_literal_global.6054
- ___block_literal_global.6135
- ___block_literal_global.62.2708
- ___block_literal_global.6216
- ___block_literal_global.624
- ___block_literal_global.6288
- ___block_literal_global.642
- ___block_literal_global.660
- ___block_literal_global.6607
- ___block_literal_global.6880
- ___block_literal_global.7346
- ___block_literal_global.7528
- ___block_literal_global.7845
- ___block_literal_global.7984
- ___block_literal_global.8160
- ___block_literal_global.8342
- ___block_literal_global.8576
- ___block_literal_global.8826
- ___block_literal_global.9471
- ___block_literal_global.9645
- ___block_literal_global.975
- ___block_literal_global.9852
- ___block_literal_global.9950
- ___getCADisplayClass_block_invoke.7149
- _audit_stringQuartzCore.6392
- _audit_stringQuartzCore.7166
- _audit_stringQuartzCore.9885
- _dispatch_queue_create
- _getCADisplayClass.7147
- _getCADisplayClass.softClass.7148
- _objc_msgSend$_coreSetUpWithServiceConnection:
- _objc_msgSend$_initWithEnvironment:token:pid:
- _objc_msgSend$_initWithPredicate:target:reason:identity:
- _objc_msgSend$_initWithRemoteConnection
- _objc_msgSend$_lock_policyStatus
- _objc_msgSend$_lock_updateStateWithBlock:
- _objc_msgSend$_reconnectAfterServerInterruption
- _objc_msgSend$appendCGRect:
- _objc_msgSend$appendCGRect:counterpart:
- _objc_msgSend$exclusiveTouchNormalizedSubRect
- _objc_msgSend$new
- _objc_msgSend$rect
- _objc_msgSend$resolutionDescriptionForEventDescriptor:sender:
- _objc_msgSend$resolutionDescriptionForKeyCommand:sender:
- _objc_msgSend$ruleForDeferringEventsMatchingPredicate:toTarget:withReason:seed:pid:
- _objc_msgSend$selectDeferringTargetForPredicate:
- _objc_msgSend$serial
- _objc_msgSend$setActiveUIResponders:
- _protobufSchema.onceToken.11055
- _protobufSchema.onceToken.11402
- _protobufSchema.onceToken.116
- _protobufSchema.onceToken.11669
- _protobufSchema.onceToken.1271
- _protobufSchema.onceToken.2235
- _protobufSchema.onceToken.2501
- _protobufSchema.onceToken.271
- _protobufSchema.onceToken.281
- _protobufSchema.onceToken.2882
- _protobufSchema.onceToken.3863
- _protobufSchema.onceToken.402
- _protobufSchema.onceToken.4806
- _protobufSchema.onceToken.516
- _protobufSchema.onceToken.622
- _protobufSchema.onceToken.640
- _protobufSchema.onceToken.658
- _protobufSchema.onceToken.6604
- _protobufSchema.onceToken.7525
- _protobufSchema.onceToken.7981
- _protobufSchema.schema.11056
- _protobufSchema.schema.11403
- _protobufSchema.schema.115
- _protobufSchema.schema.11670
- _protobufSchema.schema.1272
- _protobufSchema.schema.2236
- _protobufSchema.schema.2502
- _protobufSchema.schema.270
- _protobufSchema.schema.280
- _protobufSchema.schema.2883
- _protobufSchema.schema.3864
- _protobufSchema.schema.401
- _protobufSchema.schema.4807
- _protobufSchema.schema.515
- _protobufSchema.schema.621
- _protobufSchema.schema.639
- _protobufSchema.schema.657
- _protobufSchema.schema.6605
- _protobufSchema.schema.7526
- _protobufSchema.schema.7982
- _sharedInstance.__shared.11166
- _sharedInstance.controller.5158
- _sharedInstance.onceToken.11164
- _sharedInstance.onceToken.11520
- _sharedInstance.onceToken.182
- _sharedInstance.onceToken.3215
- _sharedInstance.onceToken.4097
- _sharedInstance.onceToken.5142
- _sharedInstance.onceToken.5156
- _sharedInstance.onceToken.8159
- _sharedInstance.onceToken.9493
- _sharedInstance.onceToken.974
- _sharedInstance.service.11521
- _sharedInstance.service.184
- _sharedInstance.service.4099
- _sharedInstance.service.976
CStrings:
+ "#20@0:8C16"
+ "%d"
+ "%li-constraint"
+ "%li-modality"
+ "&"
+ "+[BKSHIDEventDeferringConstraint new]"
+ "+[BKSHIDEventDeferringConstraintAssertion new]"
+ "+[BKSHIDEventDeferringModality new]"
+ "+[BKSHIDEventDeferringModalityAssertion new]"
+ "+[BKSHIDEventDeferringSelectionChangeRequest new]"
+ "+[BKSHIDEventDeferringSelectionTarget new]"
+ "+[BKSHIDEventSimpleProvenance new]"
+ "+[BKSTouchHitTestFilterParameters new]"
+ "-[BKSHIDEventDeferringConstraint init]"
+ "-[BKSHIDEventDeferringConstraintAssertion init]"
+ "-[BKSHIDEventDeferringModality init]"
+ "-[BKSHIDEventDeferringModalityAssertion init]"
+ "-[BKSHIDEventDeferringSelectionChangeRequest init]"
+ "-[BKSHIDEventDeferringSelectionTarget init]"
+ "-[BKSHIDEventSimpleProvenance init]"
+ "-[BKSTouchHitTestFilterParameters init]"
+ "@\"<BKSHIDEventDeferringSelectionPathSymbol>\""
+ "@\"<BKSHIDEventDeliveryManagerServerInterface>\""
+ "@\"<BKSHIDEventProvenance>\""
+ "@\"BKSHIDEventDeferringChangeBasis\""
+ "@\"BKSHIDEventDeferringConstraint\""
+ "@\"BKSHIDEventDeferringModality\""
+ "@\"BKSHIDEventDeferringSelectionPathIdentifier\""
+ "@\"BKSHIDEventDeferringSelectionTarget\""
+ "@\"BKSHIDEventDeliveryPolicy\""
+ "@\"BKSHIDEventSimpleProvenance\""
+ "@\"BSServiceDispatchQueue\""
+ "@\"BSServiceInitiatingConnection\""
+ "@\"BSServiceInitiatingConnection\"24@0:8@\"NSString\"16"
+ "@\"BSServiceInitiatingConnection\"32@0:8@\"NSString\"16@\"BSServiceInitiatingConnectionMultiplexer\"24"
+ "@\"BSServiceInitiatingConnection\"32@0:8@\"NSString\"16^B24"
+ "@\"NSString\"16@?0@\"<BKSHIDEventDeliveryManagerServerInterface>\"8"
+ "@32@0:8@16^B24"
+ "@32@0:8r*16q24"
+ "@36@0:8i16@20@28"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16@24@32@40I48i52"
+ "@64@0:8@16@24@32@40@48B56B60"
+ "AX maybe"
+ "B16@?0@\"BKSHIDEventDeferringTarget\"8"
+ "BKSHIDEventAttributes.m"
+ "BKSHIDEventCollectionDescriptor"
+ "BKSHIDEventDeferringChangeBasis"
+ "BKSHIDEventDeferringChangeBasis.m"
+ "BKSHIDEventDeferringConstraint"
+ "BKSHIDEventDeferringConstraint cannot be subclassed"
+ "BKSHIDEventDeferringConstraint.m"
+ "BKSHIDEventDeferringConstraintAssertion"
+ "BKSHIDEventDeferringConstraintAssertion cannot be subclassed"
+ "BKSHIDEventDeferringConstraintAssertion.m"
+ "BKSHIDEventDeferringModality"
+ "BKSHIDEventDeferringModality cannot be subclassed"
+ "BKSHIDEventDeferringModality.m"
+ "BKSHIDEventDeferringModalityAssertion"
+ "BKSHIDEventDeferringModalityAssertion cannot be subclassed"
+ "BKSHIDEventDeferringModalityAssertion.m"
+ "BKSHIDEventDeferringSelectionChangeRequest"
+ "BKSHIDEventDeferringSelectionChangeRequest cannot be subclassed"
+ "BKSHIDEventDeferringSelectionChangeRequest.m"
+ "BKSHIDEventDeferringSelectionPathIdentifier"
+ "BKSHIDEventDeferringSelectionPathSymbol"
+ "BKSHIDEventDeferringSelectionTarget"
+ "BKSHIDEventDeferringSelectionTarget.m"
+ "BKSHIDEventDeliveryManager - connection activation"
+ "BKSHIDEventDeliveryManager - connection interruption"
+ "BKSHIDEventDeliveryPolicy"
+ "BKSHIDEventDeliveryPolicyObserver <%p> - async callout"
+ "BKSHIDEventDeliverySelectionTarget cannot be subclassed"
+ "BKSHIDEventObserver - connection activation"
+ "BKSHIDEventObserver - connection interruption"
+ "BKSHIDEventProvenance"
+ "BKSHIDEventSimpleProvenance"
+ "BKSHIDEventSimpleProvenance cannot be subclassed"
+ "BKSHIDEventSimpleProvenance.m"
+ "BKSHIDEventSimpleProvenanceOriginator"
+ "BKSHIDEventUnitTestableProvenance"
+ "BKSHIDServiceConnectionFactory"
+ "BKSHIDServiceConnectionFactory.m"
+ "BKSMutableHIDEventDeferringConstraint"
+ "BKSMutableHIDEventDeferringConstraintAssertion"
+ "BKSMutableHIDEventDeferringModality"
+ "BKSMutableHIDEventDeferringModalityAssertion"
+ "BKSMutableHIDEventDeferringSelectionChangeRequest"
+ "BKSMutableHIDEventDeferringSelectionTarget"
+ "BKSMutableHIDEventSimpleProvenance"
+ "BKSMutableTouchHitTestFilterParameters"
+ "BKSTouchHitTestFilterParameters"
+ "BKSTouchHitTestFilterParameters cannot be subclassed"
+ "BKSTouchHitTestFilterParameters.m"
+ "BKSenderDescriptorsToFilter"
+ "CGSWindowID"
+ "T@\"<BKSHIDEventDeferringSelectionPathSymbol>\",&,D,N"
+ "T@\"<BKSHIDEventDeferringSelectionPathSymbol>\",R,N"
+ "T@\"<BKSHIDEventProvenance>\",&,N"
+ "T@\"<BKSHIDEventProvenance>\",R,N,V_eventProvenance"
+ "T@\"BKSEventDeferringChainIdentity\",R,N"
+ "T@\"BKSHIDEventDeferringChangeBasis\",&,D,N"
+ "T@\"BKSHIDEventDeferringChangeBasis\",R,N"
+ "T@\"BKSHIDEventDeferringConstraint\",&,D,N"
+ "T@\"BKSHIDEventDeferringConstraint\",R,N"
+ "T@\"BKSHIDEventDeferringModality\",&,D,N"
+ "T@\"BKSHIDEventDeferringModality\",R,N"
+ "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",&,D,N"
+ "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",C,N"
+ "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,C,N,V_selectionPathIdentifier"
+ "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,N"
+ "T@\"BKSHIDEventDeferringSelectionPathIdentifier\",R,N,V_selectionPath"
+ "T@\"BKSHIDEventDeferringSelectionTarget\",&,D,N"
+ "T@\"BKSHIDEventDeferringSelectionTarget\",R,N"
+ "T@\"BKSHIDEventDeferringTarget\",&,D,N"
+ "T@\"BKSHIDEventDeferringTarget\",R,N"
+ "T@\"BKSHIDEventDeliveryPolicy\",R,N"
+ "T@\"BSServiceInitiatingConnection\",&,N,V_connection"
+ "T@\"NSArray\",C,N,V_constraintAssertions"
+ "T@\"NSArray\",C,N,V_modalityAssertions"
+ "T@\"NSArray\",C,N,V_selectionRequests"
+ "T@\"NSData\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N"
+ "T@\"NSSet\",R,C,N,V_modalities"
+ "T@\"NSSet\",R,C,N,V_restrictedToEventDescriptors"
+ "T@\"NSString\",R,C,N,V_identifier"
+ "TB,D,N,GisFinalStringToken"
+ "TB,N,V_containsEndOfChain"
+ "TB,R,N,GisEmpty"
+ "TB,R,N,GisFinalStringToken,V_finalStringToken"
+ "TB,R,N,V_containsSubset"
+ "TQ,R,N,V_timetamp"
+ "Td,R,N"
+ "Tq,R,N,V_deferringPolicyStatus"
+ "UNKNOWN"
+ "Unable to get a connection to the hid event observer server! No observation will be allowed!!!"
+ "[contextIDs count] > 0"
+ "[senders count] > 0"
+ "[target target]"
+ "_BKSHIDCGSConnectionIDEventDeferringToken"
+ "_BKSHIDCGSWindowIDEventDeferringToken"
+ "_CGSWindowID"
+ "_activateServerConnection:"
+ "_asyncObserverCalloutQueue"
+ "_asyncResultQueue"
+ "_authentic"
+ "_basis"
+ "_bsServiceDispatchQueue"
+ "_chainIdentity"
+ "_classForAttributeType:"
+ "_constraint"
+ "_constraintAssertions"
+ "_containsEndOfChain"
+ "_containsSubset"
+ "_contextIDs"
+ "_deferringPolicyStatus"
+ "_eventAttributeType"
+ "_eventProvenance"
+ "_executeDescriptionFetch:result:"
+ "_finalStringToken"
+ "_finalStringTokenInChain"
+ "_hitTestFilterParameters"
+ "_identifierOfCGSWindow"
+ "_ignoreModalities"
+ "_initWithCGSWindowID:"
+ "_initWithConnectionFactory:"
+ "_initWithConnectionFactory:forTesting:"
+ "_initWithEnvironment:token:selectionPath:pid:"
+ "_initWithIdentifier:provenance:"
+ "_initWithPolicyObservation:"
+ "_initWithPredicate:restrictedToEventDescriptors:target:reason:identity:"
+ "_isIdentifierOfCGSWindow"
+ "_isNonLaunchingServer"
+ "_lock_buildCurrentPolicy"
+ "_lock_constraintAssertSeed"
+ "_lock_constraintAsserts"
+ "_lock_currentPolicy"
+ "_lock_effectivePolicyObservation"
+ "_lock_flushInitialStateToServer"
+ "_lock_hasReceivedLatestDeferringObservationsFromServer"
+ "_lock_lastSentConstraintAsserts"
+ "_lock_lastSentModalityAsserts"
+ "_lock_modalityAssertSeed"
+ "_lock_modalityAsserts"
+ "_lock_noteServerInterruption"
+ "_lock_pendQuery:"
+ "_lock_pendingQueriesToBeExecutedInsideLockOnceActivationHappens"
+ "_lock_remoteTargetSafeToMessage"
+ "_lock_selectionPathIdentifier"
+ "_lock_selectionRequests"
+ "_lock_updatePolicyWithBlock:"
+ "_lock_waitingOnServerHandshake"
+ "_modalities"
+ "_modality"
+ "_modalityAssertions"
+ "_notifyAsyncObservers:didUpdatePolicy:"
+ "_pathIdentifier"
+ "_replacePolicySpecificationObject:withObject:replaceIvarBlock:"
+ "_restrictedToEventDescriptors"
+ "_selectionPath"
+ "_selectionPathIdentifier"
+ "_selectionRequests"
+ "_selectionTarget"
+ "_simpleProvenance"
+ "_substituteSingeltonForIdentifierString:"
+ "_timetamp"
+ "_updateServerHitTestFilterParameters"
+ "aborting flush, not connected to server"
+ "activeInput"
+ "activeInputModality"
+ "appendUInt64:withName:"
+ "assertSelectionPath:target:hasModality:basis:"
+ "assertSelectionPath:target:imposesConstraint:"
+ "assertions"
+ "asyncObserverCalloutQueue"
+ "attributes data corrupt (length overrun)"
+ "attributes data too small"
+ "backboardd-attr-cache-17000309"
+ "backboarddSelfData"
+ "basis"
+ "bs_filter:"
+ "buildProvenance:"
+ "cannot directly allocate BKSHIDEventDeferringConstraint"
+ "cannot directly allocate BKSHIDEventDeferringConstraintAssertion"
+ "cannot directly allocate BKSHIDEventDeferringModality"
+ "cannot directly allocate BKSHIDEventDeferringModalityAssertion"
+ "cannot directly allocate BKSHIDEventDeferringSelectionChangeRequest"
+ "cannot directly allocate BKSHIDEventDeliverySelectionTarget"
+ "cannot directly allocate BKSHIDEventSimpleProvenance"
+ "cannot directly allocate BKSTouchHitTestFilterParameters"
+ "cannot subclass BKSHIDEventDeferringChangeBasis"
+ "chainIdentity"
+ "changeBasis"
+ "changeSelectionPath:target:basis:ignoreModalities:"
+ "clientConnectionForServiceWithName:isNonLaunching:"
+ "clientConnectionForServiceWithName:multiplexer:"
+ "clientConnectionForServiceWithName:multiplexer:isNonLaunching:"
+ "com.apple.backboard.hid.delivery-manager.asyncResult"
+ "com.apple.backboard.hid.delivery.selectionPathHold"
+ "configure:"
+ "connectionDescriptionForDeferringRuleIdentity:result:"
+ "connectionDescriptionForDeferringRuleWithSeed:pid:result:"
+ "connectionFactory"
+ "constraint"
+ "constraintAssertions"
+ "constraintBasis"
+ "constraints"
+ "containsEndOfChain"
+ "containsSubset"
+ "currentPolicy"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "defaultMultiplexer"
+ "deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:"
+ "deferringPolicyStatus"
+ "deliveryChainsDescription"
+ "deliveryChainsDescription:"
+ "deliveryGraphDescription:"
+ "deliveryPolicyObserver:policyDidChange:"
+ "deserializeFromBytes:byteCount:"
+ "empty"
+ "event"
+ "eventDescriptorIsRestricted:"
+ "eventDescriptors"
+ "eventProvenance"
+ "everyPath"
+ "everySelectionPath"
+ "excludeEventsFromSenders:fromHitTestingToContextIDs:"
+ "exclusive"
+ "exclusiveDenormalized"
+ "exclusiveNormalized"
+ "finalStringToken"
+ "finalStringTokenInChain"
+ "genericGesture"
+ "hasReceivedLatestDeferringObservationsFromServer"
+ "hitTestRegionLocationForPoint:"
+ "hostOverride"
+ "ignoreModalities"
+ "initWithEndpoint:options:"
+ "initWithEventProvenance:"
+ "initWithIdentifier:"
+ "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:"
+ "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:containsSubset:containsEndOfChain:"
+ "insideExclusive"
+ "insideNonExclusive"
+ "isAuthentic"
+ "isEmpty"
+ "isFinalStringToken"
+ "isNonLaunching"
+ "modalities"
+ "modality"
+ "modalityAssertions"
+ "multiplexer"
+ "must be a valid path or symbol"
+ "outside"
+ "path != ((void *)0)"
+ "pathIdentifier"
+ "primary"
+ "provenance"
+ "q32@0:8{CGPoint=dd}16"
+ "queueWithName:"
+ "queueWithName:serviceQuality:"
+ "replaceBytesInRange:withBytes:length:"
+ "requested attributes from %{public}@, but decoded %{public}@"
+ "resolutionDescriptionForEventDescriptor:sender:result:"
+ "resolutionDescriptionForKeyCommand:sender:result:"
+ "restrictedToEventDescriptors"
+ "ruleForDeferringEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:seed:pid:"
+ "ruleOriginatorBasis"
+ "selectionPath"
+ "selectionPath != ((void *)0)"
+ "selectionPathIdentifier"
+ "selectionRequests"
+ "selectionTarget"
+ "serializedData"
+ "serviceName"
+ "setActivationHandler:"
+ "setBasis:"
+ "setClientMessagingExpectation:"
+ "setConstraint:"
+ "setConstraintAssertions:"
+ "setContainsEndOfChain:"
+ "setContextIDs:"
+ "setFinalStringToken:"
+ "setHitTestFilterParameters:"
+ "setIdentifier:"
+ "setIgnoreModalities:"
+ "setModality:"
+ "setModalityAssertions:"
+ "setMultiplexer:"
+ "setPathIdentifier:"
+ "setProvenance doesn't know what to do with %@"
+ "setProvenance:"
+ "setSelectionPath:"
+ "setSelectionPathIdentifier:"
+ "setSelectionRequests:"
+ "setSelectionTarget:"
+ "setSignature:"
+ "setTarget:"
+ "signature"
+ "simple"
+ "simpleConstraint"
+ "simpleProvenance"
+ "subsetForPID:"
+ "targetForDeferringEnvironment:selectionPath:"
+ "targetForPID:environment:selectionPath:"
+ "tokenForIdentifierOfCGSWindow:"
+ "unrecognized serializable basis identifier : %@"
+ "unsupported type for attribute decode:%d"
+ "userInteractiveMultiplexer"
+ "v16@?0@\"<BSServiceConnectionInitiatingOptions>\"8"
+ "v16@?0@\"<BSServiceInitiatingConnectionConfiguring>\"8"
+ "v16@?0@\"BKSHIDEventDeliveryPolicyObserver\"8"
+ "v16@?0@\"BKSMutableHIDEventDeferringConstraint\"8"
+ "v16@?0@\"BKSMutableHIDEventDeferringConstraintAssertion\"8"
+ "v16@?0@\"BKSMutableHIDEventDeferringModality\"8"
+ "v16@?0@\"BKSMutableHIDEventDeferringModalityAssertion\"8"
+ "v16@?0@\"BKSMutableHIDEventDeferringSelectionChangeRequest\"8"
+ "v16@?0@\"BKSMutableHIDEventSimpleProvenance\"8"
+ "v16@?0@\"BKSMutableTouchHitTestFilterParameters\"8"
+ "v16@?0@\"BSServiceInitiatingConnection<BSServiceConnectionContext>\"8"
+ "v24@0:8@\"NSArray<__BKSTouchHitTestFilterParameters__>\"16"
+ "v24@?0@\"<BKSHIDEventDeliveryManagerServerInterface>\"8@\"NSError\"16"
+ "v32@0:8@?16@?24"
+ "v32@0:8I16i20@?24"
+ "v44@0:8@16@24@32B40"
+ "validWithTimestamp:"
+ "verifyAuthentic:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
- "%li-activeUIResponder: %@"
- "@36@0:8@16@24i32"
- "BKSHIDServiceConnection"
- "Error encoding contextIDs: %{public}@"
- "Error sending contextIDs: 0x%x"
- "T@\"BSServiceConnection\",&,N,V_connection"
- "T@\"NSArray\",C,N,V_activeUIResponders"
- "Vv24@0:8@\"BKSHIDEventDeferringPredicate\"16"
- "_BKSHIDCGSConnectIDEventDeferringToken"
- "_activeUIResponders"
- "_coreSetUpWithServiceConnection:"
- "_initForTestingWithService:"
- "_initWithEnvironment:token:pid:"
- "_initWithPredicate:target:reason:identity:"
- "_initWithRemoteConnection"
- "_lock_activeUIResponderPredicates"
- "_lock_activeUIResponderSeed"
- "_lock_lastSentActiveUIResponderPredicates"
- "_lock_policyStatus"
- "_lock_updateStateWithBlock:"
- "_reconnectAfterServerInterruption"
- "_requestQueue"
- "activeUIResponderPredicates"
- "activeUIResponders"
- "appendCGRect:"
- "appendCGRect:counterpart:"
- "backboardd-attr-cache-17000013"
- "com.apple.backboard.hid.delivery.activeUIResponder"
- "connectionDescriptionForDeferringRuleWithSeed:pid:"
- "hitTestRegion"
- "predicate must have a valid token"
- "requestActiveUIResponderForDeferringPredicate:withReason:"
- "resolutionDescriptionForEventDescriptor:sender:"
- "resolutionDescriptionForKeyCommand:sender:"
- "selectDeferringPredicate:withReason:"
- "selectDeferringTargetForPredicate:"
- "serial"
- "serviceConnection"
- "setActiveUIResponders:"
- "unsupported type for attribute decode:%d -- %{public}s event"
- "wow! we've got duplicate activeUIResponder keys!!! new=%@ existing=%@ : predicate=%@"
- "{CGRect={CGPoint=dd}{CGSize=dd}}8@?0"

```
