## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-735.5.1.0.0
-  __TEXT.__text: 0x2cb98
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x1ce0
-  __TEXT.__const: 0x204
-  __TEXT.__constg_swiftt: 0x114
-  __TEXT.__swift5_typeref: 0x7c
-  __TEXT.__swift5_reflstr: 0x4b
-  __TEXT.__swift5_fieldmd: 0xac
-  __TEXT.__cstring: 0x2be0
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__oslogstring: 0x2502
-  __TEXT.__unwind_info: 0x960
-  __TEXT.__objc_classname: 0x9ef
-  __TEXT.__objc_methname: 0x4d78
-  __TEXT.__objc_methtype: 0x18d0
-  __TEXT.__objc_stubs: 0x34c0
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x10a8
-  __DATA_CONST.__objc_classlist: 0x178
-  __DATA_CONST.__objc_protolist: 0xf8
+860.0.1.0.0
+  __TEXT.__text: 0x3a3c4
+  __TEXT.__objc_methlist: 0x2048
+  __TEXT.__const: 0x68c
+  __TEXT.__constg_swiftt: 0x1b0
+  __TEXT.__swift5_typeref: 0x225
+  __TEXT.__swift5_reflstr: 0x12c
+  __TEXT.__swift5_fieldmd: 0x1b0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__cstring: 0x2f6a
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__gcc_except_tab: 0x3d0
+  __TEXT.__oslogstring: 0x31c7
+  __TEXT.__unwind_info: 0xb78
+  __TEXT.__eh_frame: 0x158
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x12b8
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a0
+  __DATA_CONST.__objc_selrefs: 0x1320
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x290
-  __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH_CONST.__const: 0x5c8
-  __AUTH_CONST.__cfstring: 0x2700
-  __AUTH_CONST.__objc_const: 0x5208
+  __DATA_CONST.__got: 0x3d8
+  __AUTH_CONST.__const: 0xa18
+  __AUTH_CONST.__cfstring: 0x2a20
+  __AUTH_CONST.__objc_const: 0x5cb8
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2c0
+  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH.__objc_data: 0x450
   __AUTH.__data: 0x148
-  __DATA.__objc_ivar: 0x3ac
-  __DATA.__data: 0xbd0
-  __DATA.__bss: 0xc0
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA.__objc_ivar: 0x420
+  __DATA.__data: 0xca0
+  __DATA.__bss: 0x460
+  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__data: 0x118
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 2F5536CD-1A2F-342A-819D-46168A182D95
-  Functions: 772
-  Symbols:   3091
-  CStrings:  2015
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: D56FCFD6-33E7-3BB3-AAA0-7E67B2DE385A
+  Functions: 1016
+  Symbols:   3594
+  CStrings:  994
 
Symbols:
+ +[BKDisplayOrientationController sharedInstance]
+ +[BKHIDPrimaryEventProcessor primaryProcessorWithCreationContext:configuration:]
+ +[BKTargetIDWrapper wrapperWithTargetID:]
+ -[BKDisplayOrientationController .cxx_destruct]
+ -[BKDisplayOrientationController _removeObserverEntry:]
+ -[BKDisplayOrientationController addObserver:]
+ -[BKDisplayOrientationController addObserver:priority:]
+ -[BKDisplayOrientationController init]
+ -[BKDisplayOrientationController interfaceOrientationForDisplayUUID:]
+ -[BKDisplayOrientationController setInterfaceOrientation:forDisplayUUID:]
+ -[BKEventDeferringEnvironmentGraph _changeSelectionPath:toNode:requestingPID:basis:ignoreModality:reason:]
+ -[BKEventDeferringEnvironmentGraph _choosePredicateNodeFromSet:forSelectionPath:]
+ -[BKEventDeferringEnvironmentGraph _chooseRuleNodeOfPredicateNode:forSelectionPath:appendToPath:]
+ -[BKEventDeferringEnvironmentGraph _collectDeadPredicateNodes]
+ -[BKEventDeferringEnvironmentGraph _effectiveDestinationForNode:]
+ -[BKEventDeferringEnvironmentGraph _grantAuthorizesSelectionForPID:toNode:onSelectionPath:]
+ -[BKEventDeferringEnvironmentGraph _nodeForDeferringTarget:]
+ -[BKEventDeferringEnvironmentGraph _removeNodeAndDescendantsFromSelectionPath:selectionPath:]
+ -[BKEventDeferringEnvironmentGraph _targetIsEffectivelySelected:selectionPath:pathIdentifier:visited:]
+ -[BKEventDeferringEnvironmentGraph _topLevelRuleNodesForPID:]
+ -[BKEventDeferringEnvironmentGraph allNodesWithoutSupernodes]
+ -[BKEventDeferringEnvironmentGraph appendDescriptionToStream:]
+ -[BKEventDeferringEnvironmentGraph constraintsForDeferringTarget:pathIdentifier:]
+ -[BKEventDeferringEnvironmentGraph deferringPathForPID:dispatchTarget:returnModalities:returnConstraints:]
+ -[BKEventDeferringEnvironmentGraph deferringTargetIsSelected:pathIdentifier:]
+ -[BKEventDeferringEnvironmentGraph description]
+ -[BKEventDeferringEnvironmentGraph modalitiesForDeferringTarget:pathIdentifier:]
+ -[BKEventDeferringEnvironmentGraph setConstraintAssertions:forClientWithPID:]
+ -[BKEventDeferringEnvironmentGraph setGrantAssertions:forGrantorPID:]
+ -[BKEventDeferringEnvironmentGraph setModalityAssertions:forClientWithPID:]
+ -[BKEventDeferringEnvironmentGraph topLevelPredicateNodesByPID]
+ -[BKEventDeferringGraph _identitySetsGroupedByEqualGraphContents]
+ -[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:forPID:block:]
+ -[BKEventDeferringGraph deliveryChainForPID:sender:environment:display:dispatchTarget:]
+ -[BKEventDeferringPredicateNode .cxx_destruct]
+ -[BKEventDeferringPredicateNode appendDescriptionToStream:]
+ -[BKEventDeferringPredicateNode connectSubnode:]
+ -[BKEventDeferringPredicateNode description]
+ -[BKEventDeferringPredicateNode subnodes]
+ -[BKEventDeferringPredicateNode target]
+ -[BKEventDeferringRuleNode .cxx_destruct]
+ -[BKEventDeferringRuleNode _disconnectSubnode:]
+ -[BKEventDeferringRuleNode appendDescriptionToStream:]
+ -[BKEventDeferringRuleNode copyWithZone:]
+ -[BKEventDeferringRuleNode copy]
+ -[BKEventDeferringRuleNode description]
+ -[BKEventDeferringRuleNode destinationTarget]
+ -[BKEventDeferringRuleNode disconnectFromGraph]
+ -[BKEventDeferringRuleNode hasAncestorNode:]
+ -[BKEventDeferringRuleNode hash]
+ -[BKEventDeferringRuleNode isEqual:]
+ -[BKEventDeferringRuleNode pid]
+ -[BKEventDeferringRuleNode rule]
+ -[BKEventDeferringRuleNode sourceTarget]
+ -[BKEventDeferringRuleNode subnodes]
+ -[BKEventDeferringSelectionPathContainer _addTarget:parentTarget:]
+ -[BKEventDeferringSelectionPathContainer _addTarget:parentTarget:recordInHistory:]
+ -[BKEventDeferringSelectionPathContainer _keyForTarget:]
+ -[BKEventDeferringSelectionPathContainer appendDescriptionToStream:]
+ -[BKEventDeferringSelectionPathContainer constraintsForTarget:supertarget:]
+ -[BKEventDeferringSelectionPathContainer hash]
+ -[BKEventDeferringSelectionPathContainer isEqual:]
+ -[BKEventDeferringSelectionPathContainer latestConstrainedSiblingTargetForTarget:siblingTargets:]
+ -[BKEventDeferringSelectionPathContainer modalitiesForTarget:]
+ -[BKEventDeferringSelectionPathContainer previouslySelectedSubtargetsForTarget:]
+ -[BKEventDeferringSelectionPathContainer removeTargetWithoutAlteringHistory:]
+ -[BKEventDeferringSelectionPathContainer setConstraintAssertionsByTarget:bySourcePID:]
+ -[BKEventDeferringSelectionPathContainer setModalityAssertionsByTarget:]
+ -[BKEventDeferringSelectionPathContainer succinctDescription]
+ -[BKEventDeferringSelectionPathContainer targetsWithConstraintsFromAssertions:]
+ -[BKEventDeliveryChain identity]
+ -[BKHIDClientConnection lastPathComponent]
+ -[BKHIDClientConnection succinctDescriptionOfRemoteProcess]
+ -[BKHIDClientConnectionManager succinctDescriptionForPID:]
+ -[BKHIDEventDeliveryManager _deferringTargetsForChainPath:]
+ -[BKHIDEventDeliveryManager _lock_setConstraintAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryManager _lock_setGrantAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryManager _lock_setModalityAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryManager setGrantAssertions:forClientWithPID:]
+ -[BKHIDEventDeliveryObserverServer setObservesDeferringChanges:]
+ -[BKHIDEventDeliveryObserverService _lock_postChainsToObservingClient:]
+ -[BKHIDEventDeliveryObserverService connection:setObservesDeferringChanges:]
+ -[BKHIDEventProcessorCreationContext deliveryManagerProvider]
+ -[BKHIDEventProcessorCreationContext deliveryObservationManager]
+ -[BKHIDEventProcessorCreationContext displayRenderSpace]
+ -[BKHIDEventProcessorCreationContext keyboardHIDEventProcessorClass]
+ -[BKHIDEventProcessorCreationContext orientationProvider]
+ -[BKHIDEventProcessorCreationContext sensorCoordinator]
+ -[BKHIDEventProcessorCreationContext setDeliveryManagerProvider:]
+ -[BKHIDEventProcessorCreationContext setDisplayRenderSpace:]
+ -[BKHIDEventProcessorCreationContext setKeyboardHIDEventProcessorClass:]
+ -[BKHIDEventProcessorCreationContext setOrientationProvider:]
+ -[BKHIDEventProcessorCreationContext setSensorCoordinator:]
+ -[BKHIDEventProcessorCreationContext setSmartCoverHIDEventProcessorClass:]
+ -[BKHIDEventProcessorCreationContext setTouchDeliveryObservationManager:]
+ -[BKHIDEventProcessorCreationContext setTouchPadManager:]
+ -[BKHIDEventProcessorCreationContext smartCoverHIDEventProcessorClass]
+ -[BKHIDEventProcessorCreationContext touchDeliveryObservationManager]
+ -[BKHIDEventProcessorCreationContext touchPadManager]
+ -[BKIOHIDService hasSiblingFIDOInterface]
+ -[BKPortraitOnlyOrientationProvider .cxx_destruct]
+ -[BKPortraitOnlyOrientationProvider addOrientationObserver:]
+ -[BKPortraitOnlyOrientationProvider currentRawDeviceOrientation]
+ -[BKPortraitOnlyOrientationProvider currentUserInterfaceOrientation]
+ -[BKPortraitOnlyOrientationProvider dealloc]
+ -[BKPortraitOnlyOrientationProvider displaySupportsRotation:]
+ -[BKPortraitOnlyOrientationProvider effectiveDeviceOrientation]
+ -[BKPortraitOnlyOrientationProvider init]
+ -[BKPortraitOnlyOrientationProvider lastEffectiveInterfaceOrientation]
+ -[BKSHitTestTargetIdentifier(BKTargetIDWrapper) initWithTargetID:]
+ -[BKSHitTestTargetIdentifier(BKTargetIDWrapper) targetID]
+ -[_BKDisplayOrientationObserverAssertion .cxx_destruct]
+ -[_BKDisplayOrientationObserverAssertion initWithController:entry:]
+ -[_BKDisplayOrientationObserverAssertion invalidate]
+ -[_BKDisplayOrientationObserverEntry .cxx_destruct]
+ -[_BKDisplayOrientationObserverEntry observer]
+ -[_BKDisplayOrientationObserverEntry priority]
+ -[_BKDisplayOrientationObserverEntry setObserver:]
+ -[_BKDisplayOrientationObserverEntry setPriority:]
+ GCC_except_table205
+ GCC_except_table240
+ GCC_except_table286
+ GCC_except_table340
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table597
+ GCC_except_table600
+ GCC_except_table631
+ GCC_except_table679
+ GCC_except_table740
+ GCC_except_table752
+ GCC_except_table783
+ OBJC_IVAR_$__BKDisplayOrientationObserverAssertion._controller
+ OBJC_IVAR_$__BKDisplayOrientationObserverAssertion._entry
+ _BKDisplayTraitsEntitlement
+ _BKEventDeferringRuleNodeMatchConnected
+ _BKEventDeferringRuleNodeMatchPartiallyConnected
+ _BKEventDeferringRuleNodeMatchProcessMismatch
+ _BKProcessDescriptionForPID
+ _BKSDisplayUUIDMainKey
+ _BKSHIDEventClientConnectionBundleIdentifierKey
+ _BKSHIDEventClientConnectionLastPathComponentKey
+ _BKSHIDEventClientConnectionPidKey
+ _BKTargetIdentifierIsEqual
+ _CACurrentMediaTime
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectRelease
+ _IOObjectRetain
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryGetParentEntry
+ _IORegistryEntryIDMatching
+ _IOServiceGetMatchingService
+ _NSStringFromBKIOHIDServiceStatus
+ _NSStringFromBKOrientationChangeSource
+ _NSStringFromBKTargetIdentifier
+ _OBJC_CLASS_$_BKDisplayOrientationController
+ _OBJC_CLASS_$_BKEventDeferringPredicateNode
+ _OBJC_CLASS_$_BKEventDeferringRuleNode
+ _OBJC_CLASS_$_BKPortraitOnlyOrientationProvider
+ _OBJC_CLASS_$_BKSHIDEventDeferringTarget
+ _OBJC_CLASS_$_BKSHitTestTargetIdentifier
+ _OBJC_CLASS_$_BKTargetIDWrapper
+ _OBJC_CLASS_$_BSCompoundAssertion
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$__BKDisplayOrientationObserverAssertion
+ _OBJC_CLASS_$__BKDisplayOrientationObserverEntry
+ _OBJC_IVAR_$_BKDisplayOrientationController._lock
+ _OBJC_IVAR_$_BKDisplayOrientationController._observers
+ _OBJC_IVAR_$_BKDisplayOrientationController._orientationByDisplayUUID
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._generation
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._grantAssertionsByGrantorPID
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._graphIdentity
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._predicateNodesByTarget
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._ruleNodesByDestinationTarget
+ _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._topLevelPredicateNodesByPID
+ _OBJC_IVAR_$_BKEventDeferringGraph._pidToConstraints
+ _OBJC_IVAR_$_BKEventDeferringGraph._pidToGrants
+ _OBJC_IVAR_$_BKEventDeferringGraph._pidToModalities
+ _OBJC_IVAR_$_BKEventDeferringPredicateNode._pid
+ _OBJC_IVAR_$_BKEventDeferringPredicateNode._subnodes
+ _OBJC_IVAR_$_BKEventDeferringPredicateNode._target
+ _OBJC_IVAR_$_BKEventDeferringRuleNode._pid
+ _OBJC_IVAR_$_BKEventDeferringRuleNode._rule
+ _OBJC_IVAR_$_BKEventDeferringRuleNode._subnodes
+ _OBJC_IVAR_$_BKEventDeferringRuleNode._supernodes
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._constraintAssertionsBySourcePID
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._constraintAssertionsByTarget
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._modalityAssertionsByTarget
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._selectedDestinations
+ _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._subtargetSelectionHistoryByTarget
+ _OBJC_IVAR_$_BKEventDeliveryChain._constraints
+ _OBJC_IVAR_$_BKEventDeliveryChain._generation
+ _OBJC_IVAR_$_BKHIDClientConnection._lastPathComponent
+ _OBJC_IVAR_$_BKHIDEventDeliveryObserverService._lock_chainPublicationSeed
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._deliveryManagerProvider
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._deliveryObservationManager
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._displayRenderSpace
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._keyboardHIDEventProcessorClass
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._orientationProvider
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._sensorCoordinator
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._smartCoverHIDEventProcessorClass
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._touchDeliveryObservationManager
+ _OBJC_IVAR_$_BKHIDEventProcessorCreationContext._touchPadManager
+ _OBJC_IVAR_$_BKPortraitOnlyOrientationProvider._observers
+ _OBJC_IVAR_$__BKDisplayOrientationObserverEntry._observer
+ _OBJC_IVAR_$__BKDisplayOrientationObserverEntry._priority
+ _OBJC_METACLASS_$_BKDisplayOrientationController
+ _OBJC_METACLASS_$_BKEventDeferringPredicateNode
+ _OBJC_METACLASS_$_BKEventDeferringRuleNode
+ _OBJC_METACLASS_$_BKPortraitOnlyOrientationProvider
+ _OBJC_METACLASS_$_BKSHitTestTargetIdentifier
+ _OBJC_METACLASS_$_BKTargetIDWrapper
+ _OBJC_METACLASS_$__BKDisplayOrientationObserverAssertion
+ _OBJC_METACLASS_$__BKDisplayOrientationObserverEntry
+ __BKEnumerateSenderDescriptorsForRebuild
+ __BKGrantMatchesPath
+ __BKHIDGetLastUserEventTime
+ __OBJC_$_CATEGORY_BKSHitTestTargetIdentifier_$_BKTargetIDWrapper
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_BKSHitTestTargetIdentifier_$_BKTargetIDWrapper
+ __OBJC_$_CLASS_METHODS_BKDisplayOrientationController
+ __OBJC_$_CLASS_METHODS_BKHIDPrimaryEventProcessor
+ __OBJC_$_CLASS_METHODS_BKTargetIDWrapper
+ __OBJC_$_INSTANCE_METHODS_BKDisplayOrientationController
+ __OBJC_$_INSTANCE_METHODS_BKEventDeferringPredicateNode
+ __OBJC_$_INSTANCE_METHODS_BKEventDeferringRuleNode
+ __OBJC_$_INSTANCE_METHODS_BKPortraitOnlyOrientationProvider
+ __OBJC_$_INSTANCE_METHODS__BKDisplayOrientationObserverAssertion
+ __OBJC_$_INSTANCE_METHODS__BKDisplayOrientationObserverEntry
+ __OBJC_$_INSTANCE_VARIABLES_BKDisplayOrientationController
+ __OBJC_$_INSTANCE_VARIABLES_BKEventDeferringPredicateNode
+ __OBJC_$_INSTANCE_VARIABLES_BKEventDeferringRuleNode
+ __OBJC_$_INSTANCE_VARIABLES_BKPortraitOnlyOrientationProvider
+ __OBJC_$_INSTANCE_VARIABLES__BKDisplayOrientationObserverAssertion
+ __OBJC_$_INSTANCE_VARIABLES__BKDisplayOrientationObserverEntry
+ __OBJC_$_PROP_LIST_BKEventDeferringPredicateNode
+ __OBJC_$_PROP_LIST_BKEventDeferringRuleNode
+ __OBJC_$_PROP_LIST_BKEventDeferringSelectionPathContainer
+ __OBJC_$_PROP_LIST_BKHIDEventDeliveryManagerProviding
+ __OBJC_$_PROP_LIST_BKOrientationProvider
+ __OBJC_$_PROP_LIST_BKPortraitOnlyOrientationProvider
+ __OBJC_$_PROP_LIST_BKSHitTestTargetIdentifier_$_BKTargetIDWrapper
+ __OBJC_$_PROP_LIST__BKDisplayOrientationObserverAssertion
+ __OBJC_$_PROP_LIST__BKDisplayOrientationObserverEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKHIDEventDeliveryManagerProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKOrientationProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKHIDEventDeliveryManagerProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKOrientationProvider
+ __OBJC_$_PROTOCOL_REFS_BKHIDEventDeliveryManagerProviding
+ __OBJC_$_PROTOCOL_REFS_BKOrientationProvider
+ __OBJC_CLASS_PROTOCOLS_$_BKEventDeferringPredicateNode
+ __OBJC_CLASS_PROTOCOLS_$_BKEventDeferringRuleNode
+ __OBJC_CLASS_PROTOCOLS_$_BKPortraitOnlyOrientationProvider
+ __OBJC_CLASS_PROTOCOLS_$__BKDisplayOrientationObserverAssertion
+ __OBJC_CLASS_RO_$_BKDisplayOrientationController
+ __OBJC_CLASS_RO_$_BKEventDeferringPredicateNode
+ __OBJC_CLASS_RO_$_BKEventDeferringRuleNode
+ __OBJC_CLASS_RO_$_BKPortraitOnlyOrientationProvider
+ __OBJC_CLASS_RO_$_BKTargetIDWrapper
+ __OBJC_CLASS_RO_$__BKDisplayOrientationObserverAssertion
+ __OBJC_CLASS_RO_$__BKDisplayOrientationObserverEntry
+ __OBJC_LABEL_PROTOCOL_$_BKHIDEventDeliveryManagerProviding
+ __OBJC_LABEL_PROTOCOL_$_BKOrientationProvider
+ __OBJC_METACLASS_RO_$_BKDisplayOrientationController
+ __OBJC_METACLASS_RO_$_BKEventDeferringPredicateNode
+ __OBJC_METACLASS_RO_$_BKEventDeferringRuleNode
+ __OBJC_METACLASS_RO_$_BKPortraitOnlyOrientationProvider
+ __OBJC_METACLASS_RO_$_BKTargetIDWrapper
+ __OBJC_METACLASS_RO_$__BKDisplayOrientationObserverAssertion
+ __OBJC_METACLASS_RO_$__BKDisplayOrientationObserverEntry
+ __OBJC_PROTOCOL_$_BKHIDEventDeliveryManagerProviding
+ __OBJC_PROTOCOL_$_BKOrientationProvider
+ ___106-[BKEventDeferringEnvironmentGraph _changeSelectionPath:toNode:requestingPID:basis:ignoreModality:reason:]_block_invoke
+ ___114-[BKEventDeferringEnvironmentGraph _nodeToRestoreAfterRemovingConstraint:siblingNodes:parentTarget:selectionPath:]_block_invoke
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke_2
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke_3
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke_4
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke_5
+ ___42-[BKEventDeferringGraph logRulesToTarget:]_block_invoke_6
+ ___43-[BKEventDeferringRuleNode connectSubnode:]_block_invoke
+ ___48+[BKDisplayOrientationController sharedInstance]_block_invoke
+ ___48-[BKEventDeferringPredicateNode connectSubnode:]_block_invoke
+ ___50-[BKEventDeferringEnvironmentGraph _addNodes:pid:]_block_invoke
+ ___52-[BKEventDeferringEnvironmentGraph setRules:forPID:]_block_invoke.48
+ ___52-[BKEventDeferringGraph _setRules:forPID:toDisplay:]_block_invoke.92
+ ___52-[BKEventDeferringGraph _setRules:forPID:toDisplay:]_block_invoke_4
+ ___53-[BKHIDEventDeliveryManager initWithObserverService:]_block_invoke_4
+ ___54-[BKEventDeferringEnvironmentGraph _updateModalityMap]_block_invoke_4
+ ___54-[BKEventDeferringRuleNode appendDescriptionToStream:]_block_invoke
+ ___55-[BKDisplayOrientationController addObserver:priority:]_block_invoke
+ ___56-[BKEventDeferringEnvironmentGraph _updateConstraintMap]_block_invoke_4
+ ___59-[BKEventDeferringPredicateNode appendDescriptionToStream:]_block_invoke
+ ___60-[BKHIDEventDeliveryManager _lock_rebuildRootDeliveryPaths:]_block_invoke_2
+ ___61-[BKEventDeferringEnvironmentGraph allNodesWithoutSupernodes]_block_invoke
+ ___62-[BKEventDeferringEnvironmentGraph _collectDeadPredicateNodes]_block_invoke
+ ___62-[BKEventDeferringEnvironmentGraph _updateNodeTopLevelStatus:]_block_invoke
+ ___62-[BKEventDeferringEnvironmentGraph appendDescriptionToStream:]_block_invoke
+ ___62-[BKEventDeferringSelectionPathContainer modalitiesForTarget:]_block_invoke
+ ___63-[BKEventDeferringEnvironmentGraph _updateDeferringTargetCache]_block_invoke
+ ___63-[BKEventDeferringEnvironmentGraph _updateDeferringTargetCache]_block_invoke_2
+ ___65-[BKEventDeferringGraph _identitySetsGroupedByEqualGraphContents]_block_invoke
+ ___65-[BKEventDeferringGraph _identitySetsGroupedByEqualGraphContents]_block_invoke_2
+ ___65-[BKEventDeferringSelectionPathContainer removeAllTargetsExcept:]_block_invoke
+ ___65-[BKHIDEventDeliveryManager setGrantAssertions:forClientWithPID:]_block_invoke
+ ___67-[BKEventDeferringGraph _dispatchGrantsToEnvironmentGraphs:forPID:]_block_invoke
+ ___68-[BKEventDeferringEnvironmentGraph _pathIdentifierForSelectionPath:]_block_invoke
+ ___68-[BKEventDeferringSelectionPathContainer appendDescriptionToStream:]_block_invoke
+ ___68-[BKHIDEventDeliveryObserverService _lock_chainsForObservingClient:]_block_invoke
+ ___70-[BKHIDEventDeliveryManager _lock_rebuildKeyCommandRootDeliveryPaths:]_block_invoke
+ ___70-[BKHIDEventDeliveryManager _lock_rebuildKeyCommandRootDeliveryPaths:]_block_invoke_2
+ ___71-[BKEventDeferringGraph _identityToTargetableDictionaryForTargetables:]_block_invoke
+ ___71-[BKEventDeferringGraph _identityToTargetableDictionaryForTargetables:]_block_invoke_2
+ ___71-[BKHIDEventDeliveryManager _lock_setGrantAssertions:forClientWithPID:]_block_invoke
+ ___71-[BKHIDEventDeliveryManager _lock_setKeyCommandRoots:forClientWithPID:]_block_invoke_2
+ ___71-[BKHIDEventDeliveryObserverService _lock_postChainsToObservingClient:]_block_invoke
+ ___75-[BKEventDeferringSelectionPathContainer constraintsForTarget:supertarget:]_block_invoke
+ ___75-[BKEventDeferringSelectionPathContainer constraintsForTarget:supertarget:]_block_invoke_2
+ ___76-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:forPID:block:]_block_invoke
+ ___78-[BKEventDeferringEnvironmentGraph _revalidateSelectionAfterRuleChangeForPID:]_block_invoke
+ ___78-[BKEventDeferringEnvironmentGraph _revalidateSelectionAfterRuleChangeForPID:]_block_invoke_2
+ ___78-[BKEventDeferringEnvironmentGraph _revalidateSelectionAfterRuleChangeForPID:]_block_invoke_3
+ ___78-[BKEventDeferringEnvironmentGraph _revalidateSelectionAfterRuleChangeForPID:]_block_invoke_4
+ ___79-[BKEventDeferringSelectionPathContainer targetsWithConstraintsFromAssertions:]_block_invoke
+ ___79-[BKHIDEventDeliveryManager _lock_destinationsForKeyCommand:sender:transcript:]_block_invoke.257
+ ___81-[BKEventDeferringEnvironmentGraph _selectDeferringPathForRequest:requestingPID:]_block_invoke.99
+ ___90-[BKIOHIDServicePersistentPropertyController setPersistentProperties:forSenderDescriptor:]_block_invoke.61
+ ___94-[BKEventDeferringEnvironmentGraph _applyConstraintDrivenSelectionForPID:previousConstraints:]_block_invoke
+ ___94-[BKEventDeferringEnvironmentGraph _applyConstraintDrivenSelectionForPID:previousConstraints:]_block_invoke.71
+ ___94-[BKEventDeferringEnvironmentGraph _applyConstraintDrivenSelectionForPID:previousConstraints:]_block_invoke.76
+ ___94-[BKEventDeferringEnvironmentGraph _applyConstraintDrivenSelectionForPID:previousConstraints:]_block_invoke_2
+ ___Block_byref_object_copy_.2827
+ ___Block_byref_object_copy_.3639
+ ___Block_byref_object_dispose_.2828
+ ___Block_byref_object_dispose_.3640
+ ___block_descriptor_32_e100_v32?0"BKSHIDEventDeferringSelectionPathIdentifier"8"BKEventDeferringSelectionPathContainer"16^B24l
+ ___block_descriptor_32_e34_16?0"BKEventDeferringRuleNode"8l
+ ___block_descriptor_32_e62_v32?0"BKEventDeferringSelectionPathContainer"8"NSSet"16^B24l
+ ___block_descriptor_32_e63_q24?0"BKEventDeferringRuleNode"8"BKEventDeferringRuleNode"16l
+ ___block_descriptor_32_e73_q24?0"BKEventDeferringPredicateNode"8"BKEventDeferringPredicateNode"16l
+ ___block_descriptor_32_e74_v32?0"BKSHIDEventDeferringTarget"8"BKEventDeferringPredicateNode"16^B24l
+ ___block_descriptor_32_e83_q24?0"_BKDisplayOrientationObserverEntry"8"_BKDisplayOrientationObserverEntry"16l
+ ___block_descriptor_36_e34_16?0"BKEventDeferringRuleNode"8l
+ ___block_descriptor_36_e44_B16?0"BKSHIDEventDeferringGrantAssertion"8l
+ ___block_descriptor_40_e8_32bs_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e34_16?0"BKEventDeferringRuleNode"8ls32l8
+ ___block_descriptor_40_e8_32s_e41_B32?0"BKEventDeferringRuleNode"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSNumber"8"NSMutableOrderedSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"BKEventDeferringSelectionPathContainer"8ls32l8
+ ___block_descriptor_40_e8_32s_e74_v32?0"BKSHIDEventDeferringTarget"8"BKEventDeferringPredicateNode"16^B24ls32l8
+ ___block_descriptor_44_e8_32r_e54_v24?0"BKEventDeferringEnvironmentGraph"8"NSArray"16lr32l8
+ ___block_descriptor_44_e8_32s_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e37_v16?0"BKSHIDEventSenderDescriptor"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e100_v32?0"BKSHIDEventDeferringSelectionPathIdentifier"8"BKEventDeferringSelectionPathContainer"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e34_v32?0"NSString"8"NSNumber"1624ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_v32?0"BKSHIDEventDeferringTarget"8"NSSet"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e64_v32?0"BKSHIDEventDeferringTarget"8"NSMutableOrderedSet"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e70_v24?0"BKSHIDEventSenderDescriptor"8"BKSHIDEventDispatchingTarget"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e81_"BKSHIDEventDeferringConstraint"16?0"BKSHIDEventDeferringConstraintAssertion"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40r_e56_v32?0"BKSEventDeferringChainIdentity"8"NSArray"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e100_v32?0"BKSHIDEventDeferringSelectionPathIdentifier"8"BKEventDeferringSelectionPathContainer"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48r_e48_v16?0"BKEventDeferringSelectionPathContainer"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_literal_global.121
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.170
+ ___block_literal_global.171
+ ___block_literal_global.172
+ ___block_literal_global.1730
+ ___block_literal_global.174
+ ___block_literal_global.178
+ ___block_literal_global.179
+ ___block_literal_global.180
+ ___block_literal_global.185
+ ___block_literal_global.190
+ ___block_literal_global.1967
+ ___block_literal_global.201
+ ___block_literal_global.2384
+ ___block_literal_global.283
+ ___block_literal_global.2899
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.3218
+ ___block_literal_global.3331
+ ___block_literal_global.3493
+ ___block_literal_global.364
+ ___block_literal_global.3683
+ ___block_literal_global.3821
+ ___block_literal_global.425
+ ___block_literal_global.44
+ ___block_literal_global.47
+ ___block_literal_global.47.2892
+ ___block_literal_global.50
+ ___block_literal_global.53
+ ___block_literal_global.56
+ ___block_literal_global.59
+ ___block_literal_global.59.3497
+ ___block_literal_global.62
+ ___block_literal_global.64
+ ___block_literal_global.65
+ ___block_literal_global.66
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.74
+ ___block_literal_global.75
+ ___block_literal_global.77
+ ___block_literal_global.78
+ ___block_literal_global.811
+ ___block_literal_global.83
+ ___chkstk_darwin
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy45_8
+ ___swift_memcpy4_4
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ __lastEventTime
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_BackBoardHIDEventFoundation
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_BackBoardHIDEventFoundation
+ __swift_stdlib_malloc_size
+ _associated conformance 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentOSHAASQ
+ _associated conformance 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentOSLAASQ
+ _associated conformance So18BKTargetIdentifieraSH27BackBoardHIDEventFoundationSQ
+ _get_enum_tag_for_layout_string 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV5LabelO
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _malloc_size
+ _memcpy
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_addTarget:parentTarget:
+ _objc_msgSend$_addTarget:parentTarget:recordInHistory:
+ _objc_msgSend$_isUnique
+ _objc_msgSend$_keyForTarget:
+ _objc_msgSend$_removeObserverEntry:
+ _objc_msgSend$acquireForReason:withContext:
+ _objc_msgSend$addObserver:priority:
+ _objc_msgSend$allObjects
+ _objc_msgSend$anyObject
+ _objc_msgSend$appendBodySectionWithName:block:
+ _objc_msgSend$assertionWithIdentifier:
+ _objc_msgSend$collectionLineBreakEachItemStyle
+ _objc_msgSend$connection:setObservesDeferringChanges:
+ _objc_msgSend$contextID
+ _objc_msgSend$defaultCollectionLineBreakStyle
+ _objc_msgSend$didRespondBlockForConnection:
+ _objc_msgSend$didUpdateDeferringChains:withReply:
+ _objc_msgSend$dispatcherForEvent:sender:
+ _objc_msgSend$displayOrientationController:interfaceOrientationDidChange:forDisplayUUID:
+ _objc_msgSend$grantAssertions
+ _objc_msgSend$granteeTarget
+ _objc_msgSend$grantorTarget
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithContextID:
+ _objc_msgSend$initWithController:entry:
+ _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:generation:
+ _objc_msgSend$initWithPID:token:
+ _objc_msgSend$initWithTargetID:
+ _objc_msgSend$isBuiltIn
+ _objc_msgSend$isInverted
+ _objc_msgSend$legend
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$observer
+ _objc_msgSend$orderedSet
+ _objc_msgSend$pithyDescription
+ _objc_msgSend$priority
+ _objc_msgSend$removeObjectIdenticalTo:
+ _objc_msgSend$responsePendingForConnection:
+ _objc_msgSend$setGrantAssertions:forClientWithPID:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$succinctDescriptionForPID:
+ _objc_msgSend$succinctDescriptionOfRemoteProcess
+ _objc_release_x2
+ _objc_release_x3
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x7
+ _sharedInstance.instance
+ _sharedInstance.onceToken.3217
+ _sharedInstance.onceToken.3330
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_cvw_enumFn_getEnumTag
+ _swift_getForeignTypeMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x26
+ _swift_retain_x8
+ _swift_weakAssign
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic $sSY
+ _symbolic SDySo43BKSHIDEventDeferringSelectionPathIdentifierCShy_____GG 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentO
+ _symbolic SaySSG
+ _symbolic SaySo24BKEventDeferringRuleNodeCG
+ _symbolic Say_____G 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV
+ _symbolic So26BKSHIDEventDeferringTargetC
+ _symbolic _____ 27BackBoardHIDEventFoundation15GraphPrimitivesV
+ _symbolic _____ 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV
+ _symbolic _____ 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV5LabelO
+ _symbolic _____ 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentO
+ _symbolic _____ So18BKTargetIdentifiera
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg s5Int32V
+ _symbolic _____SgXw 27BackBoardHIDEventFoundation10_GraphNode33_924A0A2DAF65EBFF9E2C8DDA409C596ALLC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo43BKSHIDEventDeferringSelectionPathIdentifierCShy_____GG s18_DictionaryStorageC 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentO
+ _symbolic _____y_____G s11_SetStorageC 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 27BackBoardHIDEventFoundation15GraphPrimitivesV0H4NodeV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 27BackBoardHIDEventFoundation15GraphPrimitivesV8OrnamentO
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic yp3key_yp5valuet
+ _symbolic yp3key_yp5valuetSg
+ _symbolic ypSg
+ _type_layout_string 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV
+ _type_layout_string 27BackBoardHIDEventFoundation15GraphPrimitivesV0E4NodeV5LabelO
+ _type_layout_string So18BKTargetIdentifiera
- -[BKEventDeferringEnvironmentGraph _changeSelectionPath:toNode:requestingPID:basis:ignoreModality:]
- -[BKEventDeferringEnvironmentGraph appendDescriptionToFormatter:]
- -[BKEventDeferringEnvironmentGraph constraintsForNode:pathIdentifier:]
- -[BKEventDeferringEnvironmentGraph modalitiesForNode:pathIdentifier:]
- -[BKEventDeferringEnvironmentGraph topLevelInEachProcess]
- -[BKEventDeferringGraph _dictionaryWithGraphToIdentityMapping]
- -[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]
- -[BKEventDeferringGraph deferringPathForPID:environment:display:dispatchTarget:returnModalities:]
- -[BKEventDeferringNode .cxx_destruct]
- -[BKEventDeferringNode _disconnectSubnode:]
- -[BKEventDeferringNode appendDescriptionToStream:]
- -[BKEventDeferringNode connectSubnode:]
- -[BKEventDeferringNode copyWithZone:]
- -[BKEventDeferringNode copy]
- -[BKEventDeferringNode description]
- -[BKEventDeferringNode disconnectFromGraph]
- -[BKEventDeferringNode hasAncestorNode:]
- -[BKEventDeferringNode hash]
- -[BKEventDeferringNode isEqual:]
- -[BKEventDeferringNode pid]
- -[BKEventDeferringNode rule]
- -[BKEventDeferringNode subnodes]
- -[BKEventDeferringNode succinctDescription]
- -[BKEventDeferringSelectionPathContainer _keyForNode:]
- -[BKEventDeferringSelectionPathContainer _removeNode:]
- -[BKEventDeferringSelectionPathContainer constraintsForNode:]
- -[BKEventDeferringSelectionPathContainer containsNode:]
- -[BKEventDeferringSelectionPathContainer modalitiesForNode:]
- -[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:eventDescriptor:getTargetOrder:]
- -[BKHIDEventDeliveryObserverServer setObservesDeferringChainIdentities:]
- -[BKHIDEventDeliveryObserverServer setObservesDeferringResolutions:]
- -[BKHIDEventDeliveryObserverService _locked_postChainsToObservingClients]
- -[BKHIDEventDeliveryObserverService connection:setObservesDeferringChainIdentities:entitled:]
- -[BKHIDEventDeliveryObserverService connection:setObservesDeferringResolutions:]
- -[BKHIDPrimaryEventProcessor initWithSubProcessors:defaultProcessor:]
- -[BKThreeLevelForest addLeaf:toBranch:trunk:]
- GCC_except_table185
- GCC_except_table218
- GCC_except_table322
- GCC_except_table334
- GCC_except_table337
- GCC_except_table343
- GCC_except_table346
- GCC_except_table575
- GCC_except_table623
- _BKEventDeferringNodeMatchConnected
- _BKEventDeferringNodeMatchPartiallyConnected
- _BKEventDeferringNodeMatchProcessMismatch
- _BKLoggingSubsystem
- _BKTouchStreamsEntitlement
- _OBJC_CLASS_$_BKEventDeferringNode
- _OBJC_CLASS_$_BKSHIDEventPolicyObservation
- _OBJC_CLASS_$_BKSMutableHIDEventDeferringTarget
- _OBJC_CLASS_$_NSMutableIndexSet
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._environment
- _OBJC_IVAR_$_BKEventDeferringEnvironmentGraph._topLevelInEachProcess
- _OBJC_IVAR_$_BKEventDeferringNode._pid
- _OBJC_IVAR_$_BKEventDeferringNode._rule
- _OBJC_IVAR_$_BKEventDeferringNode._subnodes
- _OBJC_IVAR_$_BKEventDeferringNode._supernodes
- _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._constraintAssertionsByNode
- _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._includedIdentities
- _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._modalityAssertionsByNode
- _OBJC_IVAR_$_BKEventDeferringSelectionPathContainer._subnodeSelectionHistoryByNodeIdentity
- _OBJC_IVAR_$_BKHIDEventDeliveryObserverService._lock_identityToPIDToObservations
- _OBJC_IVAR_$__BKEventObserverConnectionRecord._observingChainIdentities
- _OBJC_IVAR_$__BKEventObserverConnectionRecord._observingLocalPolicy
- _OBJC_METACLASS_$_BKEventDeferringNode
- __BKHIDSetUserEventNotifier
- __BKHIDSetUserEventNotifier.onceToken
- __OBJC_$_INSTANCE_METHODS_BKEventDeferringNode
- __OBJC_$_INSTANCE_VARIABLES_BKEventDeferringNode
- __OBJC_$_PROP_LIST_BKEventDeferringNode
- __OBJC_CLASS_PROTOCOLS_$_BKEventDeferringNode
- __OBJC_CLASS_RO_$_BKEventDeferringNode
- __OBJC_METACLASS_RO_$_BKEventDeferringNode
- ___132-[BKHIDEventDeliveryManager _lock_resolveDeferringChainForPID:display:environment:dispatchingTarget:eventDescriptor:getTargetOrder:]_block_invoke_2
- ___39-[BKEventDeferringNode connectSubnode:]_block_invoke
- ___42-[BKEventDeferringGraph logGraphToTarget:]_block_invoke
- ___43-[BKThreeLevelForest enumerateTrunk:block:]_block_invoke
- ___50-[BKEventDeferringNode appendDescriptionToStream:]_block_invoke
- ___52-[BKEventDeferringEnvironmentGraph setRules:forPID:]_block_invoke.10
- ___52-[BKEventDeferringEnvironmentGraph setRules:forPID:]_block_invoke_2
- ___58-[BKThreeLevelForest dictionaryContainingBranchesToLeaves]_block_invoke
- ___58-[BKThreeLevelForest dictionaryContainingBranchesToLeaves]_block_invoke_2
- ___60-[BKEventDeferringSelectionPathContainer modalitiesForNode:]_block_invoke
- ___61-[BKEventDeferringSelectionPathContainer constraintsForNode:]_block_invoke
- ___62-[BKEventDeferringGraph _dictionaryWithGraphToIdentityMapping]_block_invoke
- ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke
- ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke_2
- ___69-[BKEventDeferringGraph _mapSelectionTargetablesByEnvironment:block:]_block_invoke_3
- ___73-[BKHIDEventDeliveryObserverService _locked_postChainsToObservingClients]_block_invoke
- ___77-[BKEventDeferringEnvironmentGraph setConstraintAssertions:forClientWithPID:]_block_invoke
- ___79-[BKHIDEventDeliveryManager _lock_destinationsForKeyCommand:sender:transcript:]_block_invoke.203
- ___79-[BKHIDEventDeliveryObserverService deliveryChainDidUpdate:forIdentity:reason:]_block_invoke
- ___79-[BKHIDEventDeliveryObserverService deliveryChainDidUpdate:forIdentity:reason:]_block_invoke_2
- ___79-[BKHIDEventDeliveryObserverService deliveryChainDidUpdate:forIdentity:reason:]_block_invoke_3
- ___79-[BKHIDEventDeliveryObserverService deliveryChainDidUpdate:forIdentity:reason:]_block_invoke_4
- ___83-[BKEventDeferringGraph logConnectionDescriptionForDeferringRuleIdentity:toTarget:]_block_invoke
- ___90-[BKIOHIDServicePersistentPropertyController setPersistentProperties:forSenderDescriptor:]_block_invoke.19
- ____BKHIDSetUserEventNotifier_block_invoke
- ___block_descriptor_32_e30_16?0"BKEventDeferringNode"8l
- ___block_descriptor_32_e55_q24?0"BKEventDeferringNode"8"BKEventDeferringNode"16l
- ___block_descriptor_36_e30_16?0"BKEventDeferringNode"8l
- ___block_descriptor_40_e8_32bs_e29_v32?08"NSMutableSet"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e29_v32?08"NSMutableSet"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e32_v32?0"NSNumber"8"NSSet"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e36_v32?08"NSMutableDictionary"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e37_B32?0"BKEventDeferringNode"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e47_v32?0"NSNumber"8"BKEventDeferringNode"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8
- ___block_descriptor_40_e8_32s_e51_v24?0"NSNumber"8"BKSHIDEventPolicyObservation"16ls32l8
- ___block_descriptor_40_e8_32s_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8
- ___block_descriptor_40_e8_32s_e81_v32?0"BKSEventDeferringChainIdentity"8"BKEventDeferringEnvironmentGraph"16^B24ls32l8
- ___block_descriptor_44_e8_32s_e56_v32?0"BKSEventDeferringChainIdentity"8"NSArray"16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e56_v32?0"BKSEventDeferringChainIdentity"8"NSArray"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e12_v24?0Q8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e58_v32?0"BKEventDeferringEnvironmentGraph"8"NSArray"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e62_v32?0"BKEventDeferringSelectionPathContainer"8"NSSet"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e58_v32?0"BKEventDeferringEnvironmentGraph"8"NSArray"16^B24ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s_e45_v16?0"BKSMutableHIDEventPolicyObservation"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.12
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.1496
- ___block_literal_global.15
- ___block_literal_global.1671
- ___block_literal_global.18
- ___block_literal_global.2088
- ___block_literal_global.21
- ___block_literal_global.216
- ___block_literal_global.22
- ___block_literal_global.231
- ___block_literal_global.24
- ___block_literal_global.24.2570
- ___block_literal_global.247
- ___block_literal_global.250
- ___block_literal_global.2597
- ___block_literal_global.27
- ___block_literal_global.2936
- ___block_literal_global.3
- ___block_literal_global.30
- ___block_literal_global.3029
- ___block_literal_global.3223
- ___block_literal_global.33
- ___block_literal_global.33.2560
- ___block_literal_global.3327
- ___block_literal_global.36
- ___block_literal_global.360
- ___block_literal_global.5
- ___block_literal_global.6
- ___block_literal_global.6.3032
- ___block_literal_global.725
- ___block_literal_global.80
- ___block_literal_global.9
- ___block_literal_global.91
- ___block_literal_global.91.3227
- __userEventNotifier
- _objc_msgSend$_isString
- _objc_msgSend$_keyForNode:
- _objc_msgSend$_removeNode:
- _objc_msgSend$addIndex:
- _objc_msgSend$bs_flatten
- _objc_msgSend$compatibilityDisplay
- _objc_msgSend$connection:setObservesDeferringChainIdentities:entitled:
- _objc_msgSend$connection:setObservesDeferringResolutions:
- _objc_msgSend$connectionForPID:
- _objc_msgSend$deferringPath
- _objc_msgSend$didUpdateDeferringChains:
- _objc_msgSend$didUpdateDeferringObservations:
- _objc_msgSend$dispatcherForEvent:
- _objc_msgSend$enumerateIndexesUsingBlock:
- _objc_msgSend$initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:
- _objc_msgSend$initWithSubProcessors:defaultProcessor:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$selectionPath
- _objc_msgSend$setFinalStringToken:
- _objc_msgSend$setPolicyStatus:
- _objc_msgSend$setSelectionPath:
- _objc_msgSend$succinctStyle
- _objc_msgSend$userEventOccurredOnDisplay:
- _sharedInstance.onceToken.2935
- _swift_isUniquelyReferenced_native
- _swift_retain
- _swift_retain_n
- _symbolic _____Sg 27BackBoardHIDEventFoundation10_GraphNode33_924A0A2DAF65EBFF9E2C8DDA409C596ALLC
CStrings:
+ "\r"
+ "  sibling=%{public}@ constraints=%{public}@"
+ " -- (no deferring rules)"
+ "%@.%d"
+ "%X"
+ "%d"
+ "--> CHOOSE INPUT %{public}@ from rule %{public}@"
+ "<--electric eye-->"
+ "<missing target, file a radar>"
+ "<nil response from describeDeliveryChains:>\n"
+ "@16@?0@\"BKEventDeferringRuleNode\"8"
+ "B16@?0@\"BKSHIDEventDeferringGrantAssertion\"8"
+ "B32@?0@\"BKEventDeferringRuleNode\"8Q16^B24"
+ "BKHIDEventDeliveryManager - Graph"
+ "BKPortraitOnlyOrientationObservers"
+ "CHOOSE %{public}@ NEXTDOWN"
+ "CHOOSE PREV %{public}@ targetTarget:%{public}@ targetNode:%{public}@ siblings:%{public}@"
+ "CHOOSE PREV history returned:%{public}@"
+ "CHOOSE PREV no selected subnode underneath %{public}@ from rule %{public}@"
+ "CHOOSE PREV querying history for parent:%{public}@ path:%{public}@"
+ "CHOOSE checking constraints for %{public}@ supertarget:%{public}@ -> %{public}@"
+ "CoreMotion"
+ "IOService"
+ "IOUSBHostDevice"
+ "[%{public}@ %p] _nodeIsReachableFromSupernode(%{public}@):%{public}@ NO because sibling %{public}@ has constraint"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) -> SELECT -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) -> substituting unique token %{public}@ with subnode %{public}@"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) reason:%{public}@  -> %{public}@ generation: %ld -- %{public}@"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) reason:%{public}@ requestingPID:(%d) toNode:%{public}@"
+ "[%{public}@ %p] changeSelectionPath(%{public}@) walking up from node:%{public}@ supernodes:%{public}@ parentNode:%{public}@"
+ "[%{public}@ %p] constraints removed for pid(%d), restoring %lu targets from history"
+ "[%{public}@ %p] extantConstraint: skipping destination-constrained selection of %{public}@ because top-level sibling %{public}@ is already selected"
+ "[%{public}@ %p] extantConstraint: skipping selection of %{public}@ because top-level sibling %{public}@ is already selected"
+ "[%{public}@ %p] grant authorized: pid(%d) -> %{public}@ via grantee %{public}@ grantor %{public}@"
+ "[%{public}@ %p] restore: found in history: %{public}@ -> %{public}@"
+ "[%{public}@ %p] restore: no alternatives for %{public}@"
+ "[%{public}@ %p] restore: no history found, falling back to rule sort: %{public}@"
+ "[%{public}@ %p] restore: no parent target found"
+ "[%{public}@ %p] restore: no suitable target found for %{public}@"
+ "[%{public}@ %p] restore: querying history for parent:%{public}@ -> %{public}@"
+ "[%{public}@ %p] restore: selecting from history: %{public}@"
+ "[%{public}@ %p] restore: skipping choiceNode that leads to constrained target: %{public}@"
+ "[%{public}@ %p] restore: skipping sibling in different predicate group: %{public}@"
+ "[%{public}@ %p] restore: substituting unique token choiceNode with content: %{public}@"
+ "[%{public}@ %p] selected (%{public}@)"
+ "[%{public}@ %p] selection request deferring target is nil: %{public}@"
+ "[%{public}@ %p] selection request deferring target token is nil: %{public}@"
+ "[%{public}@ %p] selection request target not found: %{public}@"
+ "[%{public}@ %p] selection request token is not accessible by the requesting process(%{public}@): %{public}@"
+ "[%{public}@ %p] setConstraintAssertions:forPID(%d) generation: %ld: %{public}@"
+ "[%{public}@ %p] setGrantAssertions:forGrantorPID(%d) generation: %ld: %{public}@"
+ "[%{public}@ %p] setModalityAssertions:forPID(%d) generation: %ld: %{public}@"
+ "[%{public}@ %p] setRules:forPID(%d) generation: %ld: %{public}@"
+ "[%{public}@] connection invalidated: (%{public}@)"
+ "_addNodes: created predicate node %{public}@"
+ "_collectDeadPredicateNodes: destroying predicate node %{public}@"
+ "_matchSubnode: trying to match subnode predicate token:%{public}@ to supernode target token:%{public}@ equal:%{BOOL}u"
+ "asserts"
+ "automation"
+ "com.apple.BackBoard"
+ "com.apple.backboardd.displayTraits"
+ "constraint %{public}@ must be from pid %{public}@"
+ "constraints %{public}@ (%{public}@) now %{public}@"
+ "deferring rules"
+ "extantConstraint"
+ "grantAssertionsByGrantorPID"
+ "grants"
+ "latestConstrainedSiblingTargetForTarget: returning %{public}@"
+ "latestConstrainedSiblingTargetForTarget: targetTarget=%{public}@ siblings=%{public}@ map=%{public}@"
+ "missing grant assertions from pid:%d"
+ "observing"
+ "q24@?0@\"BKEventDeferringPredicateNode\"8@\"BKEventDeferringPredicateNode\"16"
+ "q24@?0@\"BKEventDeferringRuleNode\"8@\"BKEventDeferringRuleNode\"16"
+ "q24@?0@\"_BKDisplayOrientationObserverEntry\"8@\"_BKDisplayOrientationObserverEntry\"16"
+ "rejecting hostOverride: not hosted by pid(%d)"
+ "rejecting: no ancestor in same process is in selection path"
+ "rejecting: target is not reachable due to constraints"
+ "rejecting: we can't switch from activeInput to not-activeInput"
+ "removedConstraint"
+ "ruleSort"
+ "selectedDestinations"
+ "selectedSubstituted"
+ "selection add(%{public}@ (offspring of %{public}@)) WITHOUT recording in history"
+ "selection add(%{public}@ (offspring of %{public}@)) destinations: %{public}@ DID"
+ "selection history %{public}@ (gc): %{public}@"
+ "selection history QUERY ALL path:%{public}@ target:%{public}@ key:%{public}@ -> %{public}@"
+ "selection history RECORD path:%{public}@ parent:%{public}@ key:%{public}@ target:%{public}@"
+ "selection remove(%{public}@) destinations now: %{public}@"
+ "selectionChange"
+ "selectionPathContainerByIdentifier"
+ "setGrantAssertions: grantor target not owned by submitting pid(%d): %{public}@"
+ "setGrantAssertions: missing grantee target: %{public}@"
+ "setGrantAssertions: missing grantee token: %{public}@"
+ "setGrantAssertions: missing grantor target: %{public}@"
+ "setGrantAssertions: missing grantor token: %{public}@"
+ "setGrantAssertions: missing selection path: %{public}@"
+ "setKeyCommandRoots"
+ "setModalityAssertions"
+ "success"
+ "topLevelPredicateNodesByPID"
+ "unspecified"
+ "v16@?0@\"NSError\"8"
+ "v32@?0@\"BKSHIDEventDeferringTarget\"8@\"BKEventDeferringPredicateNode\"16^B24"
+ "v32@?0@\"BKSHIDEventDeferringTarget\"8@\"NSMutableOrderedSet\"16^B24"
+ "v32@?0@\"BKSHIDEventDeferringTarget\"8@\"NSSet\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"NSMutableOrderedSet\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16@24"
+ "⬆"
+ "⭐"
+ "🔒"
+ "🔹"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<BKHIDBufferedEventProcessor>\""
- "@\"<BKHIDDisplayChangeObserving>\""
- "@\"<BKHIDDomainIncomingServiceConnectionDelegate>\""
- "@\"<BKHIDDomainIncomingServiceConnectionHandler>\""
- "@\"<BKHIDDomainServiceDelegate>\""
- "@\"<BKHIDEventBufferingHIDSystem>\""
- "@\"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>\""
- "@\"<BKHIDEventDeliveryManagerProvider>\""
- "@\"<BKHIDEventDeliveryManagerServerRuleChangeAuthority>\""
- "@\"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>\""
- "@\"<BKHIDEventDeliveryObserverServiceProvider>\""
- "@\"<BKHIDEventDispatcher>\""
- "@\"<BKHIDEventDispatcherProviding>\""
- "@\"<BKHIDEventProcessor>\""
- "@\"<BKHIDEventProcessor><BKHIDBufferedEventProcessor>\""
- "@\"<BKHIDEventProcessorRegistering>\""
- "@\"<BKHIDEventSenderInfo>\""
- "@\"<BKHIDIncomingServiceConnectionDelegate>\""
- "@\"<BKHIDSystemDelegate>\""
- "@\"<BKHIDSystemInterfacing>\""
- "@\"<BKIOHIDServiceDisappearanceObserver>\""
- "@\"<BKIOHIDServiceMatchObserver>\""
- "@\"<BKIOHIDServiceMatcherDataProviding>\""
- "@\"<BSInvalidatable>\""
- "@\"<_BKHIDDomainIncomingServiceConnectionHandler>\""
- "@\"<_BKHIDIncomingServiceConnectionHandler>\""
- "@\"BKEventDeferringEnvironmentGraph\""
- "@\"BKEventDeferringGraph\""
- "@\"BKHIDClientConnectionManager\"16@0:8"
- "@\"BKHIDDomainIncomingServiceConnection\""
- "@\"BKHIDDomainServiceServer\""
- "@\"BKHIDEventDeliveryManager\""
- "@\"BKHIDEventDeliveryManager\"16@0:8"
- "@\"BKHIDEventDeliveryObserverService\""
- "@\"BKHIDEventDeliverySequence\""
- "@\"BKHIDEventSenderCache\""
- "@\"BKHIDEventSenderCache\"16@0:8"
- "@\"BKIOHIDService\""
- "@\"BKIOHIDServiceMatcher\""
- "@\"BKIOHIDServicePersistentPropertyController\""
- "@\"BKSEventDeferringChainIdentity\""
- "@\"BKSHIDEventAuthenticationOriginator\""
- "@\"BKSHIDEventDeferringEnvironment\""
- "@\"BKSHIDEventDeferringRule\""
- "@\"BKSHIDEventDeferringSelectionPathIdentifier\""
- "@\"BKSHIDEventDispatchingTarget\""
- "@\"BKSHIDEventDisplay\""
- "@\"BKSHIDEventKeyCommand\""
- "@\"BKSHIDEventKeyCommandsDispatchingRule\""
- "@\"BKSHIDEventSenderDescriptor\""
- "@\"BKSHIDEventSenderDescriptor\"16@0:8"
- "@\"BKSHIDEventSenderDescriptor\"20@0:8I16"
- "@\"BKSHIDEventSimpleProvenanceOriginator\""
- "@\"BKSLocalDefaults\""
- "@\"BKThreeLevelForest\""
- "@\"BSAtomicSignal\""
- "@\"BSContinuousMachTimer\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSMutableIntegerMap\""
- "@\"BSServiceConnectionListener\""
- "@\"BSServiceDispatchQueue\""
- "@\"BSServiceInterface\""
- "@\"BSServiceListenerConnection\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"NSDictionary\"16"
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableOrderedSet\""
- "@\"NSMutableSet\""
- "@\"NSMutableString\""
- "@\"NSObject<OS_dispatch_mach>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSSet\""
- "@\"NSSet<__BKSHIDEventPolicyObservation__>\"24@0:8@\"NSNumber\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSString\"24@0:8@\"_BKSHIDEventDeferringRuleIdentity\"16"
- "@\"NSString\"32@0:8@\"BKSHIDEventDescriptor\"16@\"BKSHIDEventSenderDescriptor\"24"
- "@\"NSString\"32@0:8@\"BKSHIDEventKeyCommand\"16@\"BKSHIDEventSenderDescriptor\"24"
- "@16@0:8"
- "@16@?0@\"BKEventDeferringNode\"8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"BKHIDEventProcessorCreationContext\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__IOHIDEventSystem=}16"
- "@24@0:8^{__IOHIDEventSystemConnection=}16"
- "@24@0:8^{__IOHIDService=}16"
- "@28@0:8@16B24"
- "@28@0:8Q16B24"
- "@28@0:8i16@20"
- "@32@0:8#16@24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8[44@]16@24"
- "@32@0:8^{__IOHIDEvent=}16@24"
- "@36@0:8i16i20B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16#24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32^{__IOHIDEvent=}40"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8^{__IOHIDEvent=}16@24@32@40@48"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@?24@0:8@16"
- "AB"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"BKSHIDEventSenderDescriptor\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8S16S20"
- "B32@0:8@16@24"
- "B32@?0@\"BKEventDeferringNode\"8Q16^B24"
- "BKBufferedEventEntry"
- "BKEventDeferringEnvironmentGraph"
- "BKEventDeferringGraph"
- "BKEventDeferringNode"
- "BKEventDeferringNode.m"
- "BKEventDeferringSelectionPathContainer"
- "BKEventDeliveryChain"
- "BKEventGraphDescriptionAccumulator"
- "BKHIDAccessibilitySender"
- "BKHIDBufferedEventProcessor"
- "BKHIDClientConnection"
- "BKHIDClientConnectionManager"
- "BKHIDDefaultEventProcessor"
- "BKHIDDomainIncomingServiceConnection"
- "BKHIDDomainIncomingServiceConnectionDelegate"
- "BKHIDDomainIncomingServiceConnectionHandler"
- "BKHIDDomainServiceDelegate"
- "BKHIDDomainServiceServer"
- "BKHIDEventBuffer"
- "BKHIDEventBufferingHIDSystem"
- "BKHIDEventDeliveryClient"
- "BKHIDEventDeliveryManager"
- "BKHIDEventDeliveryManagerIncomingServiceConnectionHandler"
- "BKHIDEventDeliveryManagerServer"
- "BKHIDEventDeliveryObserverIncomingServiceConnectionHandler"
- "BKHIDEventDeliveryObserverServer"
- "BKHIDEventDeliveryObserverService"
- "BKHIDEventDeliveryResolutionObserver"
- "BKHIDEventDeliverySequence"
- "BKHIDEventProcessor"
- "BKHIDEventProcessorCreationContext"
- "BKHIDEventProcessorRegistering"
- "BKHIDEventProcessorRegistry"
- "BKHIDEventRecognizer"
- "BKHIDEventRecognizerEngine"
- "BKHIDEventReevaluateBufferingContext"
- "BKHIDEventSenderCache"
- "BKHIDEventSenderInfo"
- "BKHIDEventSequenceRecognizer"
- "BKHIDIncomingServiceConnection"
- "BKHIDNullEventProcessor"
- "BKHIDPrimaryEventProcessor"
- "BKHIDSystem"
- "BKHIDSystemInterfacing"
- "BKHIDUnknownSender"
- "BKHIDUserEventNotifying.m"
- "BKIOHIDService"
- "BKIOHIDServiceDisappearanceObserver"
- "BKIOHIDServiceMatchObserver"
- "BKIOHIDServiceMatcher"
- "BKIOHIDServiceMatcherDataProviding"
- "BKIOHIDServicePersistentPropertyController"
- "BKIOHIDServicePersistentPropertyHandling"
- "BKIOHIDServiceSimplePersistentPropertySupport"
- "BKOSLogTranscriptTarget"
- "BKSHIDEventDeliveryManagerClientInterface"
- "BKSHIDEventDeliveryManagerServerInterface"
- "BKSHIDEventObserverClientInterface"
- "BKSHIDEventObserverServerInterface"
- "BKStringTranscriptTarget"
- "BKThreeLevelForest"
- "BKTranscriptTarget"
- "BSDescriptionProviding"
- "BSDescriptionStreamable"
- "BSDescriptionStreaming"
- "BSInvalidatable"
- "BSServiceListenerConnectionEventObserver"
- "HIDSystemChannel"
- "I"
- "I16@0:8"
- "IOHIDServicesMatching:"
- "NSCopying"
- "NSObject"
- "Q"
- "Q16@0:8"
- "SwiftStuff"
- "T#,R"
- "T@\"<BKHIDBufferedEventProcessor>\",R,V_processor"
- "T@\"<BKHIDDisplayChangeObserving>\",&,N,V_mainDisplayObserver"
- "T@\"<BKHIDDomainIncomingServiceConnectionDelegate>\",N"
- "T@\"<BKHIDEventBufferingHIDSystem>\",&,N,V_bufferingDispatcher"
- "T@\"<BKHIDEventDeliveryManagerIncomingServiceConnectionHandler>\",R,N"
- "T@\"<BKHIDEventDeliveryManagerServerRuleChangeAuthority>\",R,N"
- "T@\"<BKHIDEventDeliveryObserverIncomingServiceConnectionHandler>\",R,N"
- "T@\"<BKHIDEventDispatcher>\",&,N,V_eventDispatcher"
- "T@\"<BKHIDEventDispatcher>\",R,V_dispatcher"
- "T@\"<BKHIDEventDispatcherProviding>\",&,N,V_dispatcherProvider"
- "T@\"<BKHIDEventProcessor><BKHIDBufferedEventProcessor>\",R,N,V_eventProcessor"
- "T@\"<BKHIDEventProcessorRegistering>\",&,N,V_eventProcessorRegistry"
- "T@\"<BKHIDEventSenderInfo>\",&,N,V_sender"
- "T@\"<BKHIDIncomingServiceConnectionDelegate>\",N"
- "T@\"<BKHIDSystemDelegate>\",W,V_delegate"
- "T@\"<BKHIDSystemInterfacing>\",&,N,V_systemInterface"
- "T@\"<BKIOHIDServiceMatcherDataProviding>\",&,N,V_serviceMatcherDataProvider"
- "T@\"<_BKHIDDomainIncomingServiceConnectionHandler>\",N"
- "T@\"<_BKHIDIncomingServiceConnectionHandler>\",N"
- "T@\"BKHIDClientConnectionManager\",R"
- "T@\"BKHIDDomainIncomingServiceConnection\",R,N,V_domainIncomingServiceConnection"
- "T@\"BKHIDDomainServiceServer\",R,N"
- "T@\"BKHIDEventDeliveryManager\",R"
- "T@\"BKHIDEventDeliveryManager\",R,V_deliveryManager"
- "T@\"BKHIDEventDeliveryObserverService\",&,N,V_resolutionObserver"
- "T@\"BKHIDEventDeliveryObserverService\",R,N"
- "T@\"BKHIDEventDeliverySequence\",&,N,V_sequence"
- "T@\"BKHIDEventSenderCache\",R"
- "T@\"BKHIDEventSenderCache\",R,V_senderCache"
- "T@\"BKSHIDEventAuthenticationOriginator\",R,N,V_authenticationOriginator"
- "T@\"BKSHIDEventDispatchingTarget\",R,C,N,V_dispatchTarget"
- "T@\"BKSHIDEventDisplay\",&,N,V_mainDisplay"
- "T@\"BKSHIDEventKeyCommand\",R,V_keyCommand"
- "T@\"BKSHIDEventSenderDescriptor\",C,N,V_senderDescriptor"
- "T@\"BKSHIDEventSenderDescriptor\",R,C,N"
- "T@\"BKSHIDEventSimpleProvenanceOriginator\",R,N,V_simpleProvenanceOriginator"
- "T@\"BSAuditToken\",R,N"
- "T@\"BSServiceListenerConnection\",R,N,V_connection"
- "T@\"NSArray\",R,N,V_descriptors"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableArray\",&,N,V_blocks"
- "T@\"NSMutableArray\",&,N,V_recognizers"
- "T@\"NSObject<OS_dispatch_mach>\",&,GHIDSystemChannel,V_HIDSystemChannel"
- "T@\"NSObject<OS_os_log>\",R,N,V_log"
- "T@\"NSSet\",&,N,V_bufferingPIDs"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_displayUUID"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleID"
- "T@\"NSString\",R,C,N,V_clientEntitlement"
- "T@\"NSString\",R,N"
- "T@,&,N,V_additionalContext"
- "T@,R,V_firstAdditionalContext"
- "TB,GisFullyInitialized,V_fullyInitialized"
- "TB,N,GisAuthenticated,V_authenticated"
- "TB,N,GisBuiltIn,V_builtIn"
- "TB,N,V_allBufferingClientsTerminated"
- "TB,N,V_shouldConsumeEvents"
- "TB,R,N"
- "TB,R,N,GisAuthenticated"
- "TB,R,N,GisBuiltIn"
- "TB,R,N,GisRevoked"
- "TI,N,V_primaryUsage"
- "TI,N,V_primaryUsagePage"
- "TI,R,N"
- "TI,R,N,V_task"
- "TQ,N,V_senderID"
- "TQ,R"
- "TQ,R,N"
- "T^{__IOHIDService=},N,V_IOHIDService"
- "Ti,N,V_eventSource"
- "Ti,R,N"
- "Ti,R,N,V_pid"
- "Tq,N,V_serviceStatus"
- "Tq,R,N,V_versionedPID"
- "UTF8String"
- "Vv16@0:8"
- "Vv24@0:8@\"BKSHIDEventDeliveryRuleChangeTransaction\"16"
- "Vv24@0:8@\"NSArray<__BKSHIDEventDeliveryChain__>\"16"
- "Vv24@0:8@\"NSSet<__BKSHIDEventPolicyObservation__>\"16"
- "Vv24@0:8@16"
- "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting because target is not reachable due to constraints -- %{public}@"
- "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting because we can't switch from activeInput to not-activeInput -- %{public}@"
- "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting hostOverride: not hosted by pid(%d) -- %{public}@"
- "[%{public}@ %p] changeSelectionPath:%{public}@ rejecting: parent not in selection path -- %{public}@"
- "[%{public}@ %p] changeSelectionPath:%{public}@ requestingPID:(%d) toNode:%{public}@"
- "[%{public}@ %p] setConstraintAssertions:forPID(%d): %{public}@"
- "[%{public}@ %p] setModalityAssertions:forPID(%d): %{public}@"
- "[%{public}@ %p] setRules:forPID(%d): %{public}@"
- "[44@\"NSArray\"]"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}"
- "^{__IOHIDEvent=}"
- "^{__IOHIDEvent=}16@0:8"
- "^{__IOHIDEvent=}32@0:8I16^{__IOHIDEvent=}20I28"
- "^{__IOHIDEventSystem=}"
- "^{__IOHIDEventSystemClient=}"
- "^{__IOHIDEventSystemConnection=}"
- "^{__IOHIDEventSystemConnection=}16@0:8"
- "^{__IOHIDEventSystemConnection=}20@0:8I16"
- "^{__IOHIDEventSystemConnection=}24@0:8@16"
- "^{__IOHIDNotification=}"
- "^{__IOHIDService=}"
- "^{__IOHIDService=}16@0:8"
- "_BKEventObserverConnectionRecord"
- "_BKHIDDeliveryManagerDeprecatedIncomingConnectionHandler"
- "_BKHIDDeliveryObserverDeprecatedIncomingConnectionHandler"
- "_BKHIDDomainClientRecord"
- "_BKHIDDomainIncomingServiceConnectionHandler"
- "_BKHIDEventDeliveryRoot"
- "_BKHIDIncomingServiceConnectionHandler"
- "_BKHIDKeyCommandDeliveryRoot"
- "_BKIOHIDServiceDisappearanceObserverInfo"
- "_HIDEventSystem"
- "_HIDEventSystemClient"
- "_HIDSystemChannel"
- "_IOHIDService"
- "_TtC27BackBoardHIDEventFoundation22_BKGraphSectionWrapper"
- "_TtC27BackBoardHIDEventFoundationP33_924A0A2DAF65EBFF9E2C8DDA409C596A10_GraphNode"
- "_additionalContext"
- "_allBufferedEventProcessors"
- "_allBufferingClientsTerminated"
- "_allNodes"
- "_allObserverResolutions"
- "_alreadySeenDeliveryChains"
- "_asyncScheduleWithHIDEventQuue:"
- "_authenticated"
- "_authenticationOriginator"
- "_beginHandlingEvents"
- "_blocks"
- "_buffer"
- "_bufferTimer"
- "_bufferedSubProcessors"
- "_bufferingDispatchRules"
- "_bufferingDispatcher"
- "_bufferingPIDs"
- "_bufferingPredicatesByPID"
- "_buffersByDispatchTarget"
- "_buffersWithIncompleteSequences"
- "_builtIn"
- "_bundleID"
- "_chainsStateCapture"
- "_changeSelectionPath:toNode:requestingPID:basis:ignoreModality:"
- "_clientEntitlement"
- "_clientsByPID"
- "_connection"
- "_connectionListener"
- "_constraintAssertionsByClientPID"
- "_constraintAssertionsByNode"
- "_currentBuffers"
- "_currentResolutions"
- "_dataProvider"
- "_debugMappedObjectName"
- "_defaultBufferedEventProcessor"
- "_defaultProcessor"
- "_defaultsKey"
- "_defaultsLock"
- "_defaultsLock_defaults"
- "_deferringGraph"
- "_deferringPath"
- "_deferringRules"
- "_deferringRulesStateCapture"
- "_delegate"
- "_deliveryChainByIdentity"
- "_deliveryManager"
- "_deliveryManagerForEstablishedConnection:"
- "_deliveryManagerProvider"
- "_deliveryObserverServiceForEstablishedConnection:"
- "_deliveryObserverServiceProvider"
- "_deliveryRoots"
- "_deliveryRootsEventTypeMask"
- "_descriptionForKeyCommandCollection:"
- "_descriptorIndex"
- "_descriptors"
- "_destinationCacheBySender"
- "_disappearanceObservers"
- "_dispatchRootsStateCapture"
- "_dispatchTarget"
- "_dispatcher"
- "_dispatcherProvider"
- "_dispatchingEventTypeMask"
- "_dispatchingRule"
- "_dispatchingRules"
- "_displayUUID"
- "_domainIncomingServiceConnection"
- "_entitledToObserveFullDeliveryChain"
- "_entitlement"
- "_environment"
- "_environmentGraph"
- "_eventDispatcher"
- "_eventProcessor"
- "_eventProcessorRegistry"
- "_eventProcessorsByClassName"
- "_eventProcessorsForEventType:"
- "_eventSource"
- "_expectDeallocation"
- "_fireTimeoutForPID:bufferingPredicates:client:"
- "_firstAdditionalContext"
- "_firstEvent"
- "_fullyInitialized"
- "_graphStateCapture"
- "_gsEventQueue"
- "_handlersLock"
- "_handlersLock_handlers"
- "_hidConnectionToBKConnection"
- "_hidEventSystem"
- "_identifier"
- "_identity"
- "_identityToGraph"
- "_includedIdentities"
- "_incomingConnectionHandler"
- "_initForTestingWithSenderID:setUpInitialProperties:"
- "_interface"
- "_invalid"
- "_invalidSignal"
- "_isBuiltinDisplay"
- "_isNullDisplay"
- "_isString"
- "_keyCommand"
- "_keyCommandDeliveryRoots"
- "_keyCommandsRegistrations"
- "_keyForNode:"
- "_lock"
- "_lock_activeConnectionsByPID"
- "_lock_asyncNotifyServicesAdded:"
- "_lock_connection"
- "_lock_deferringChainObserverConnections"
- "_lock_delegate"
- "_lock_eventObserver"
- "_lock_handler"
- "_lock_identityToChain"
- "_lock_identityToPIDToObservations"
- "_lock_observationsByPID"
- "_lock_submitRuleChanges:validatedContentsMask:connection:"
- "_lock_wasHandled"
- "_log"
- "_mainDisplay"
- "_mainDisplayObserver"
- "_matcher"
- "_matchingDictionary"
- "_modalities"
- "_modalityAssertionsByClientPID"
- "_modalityAssertionsByNode"
- "_nodeByDeferringTarget"
- "_nodeByIdentity"
- "_observeSynchronously"
- "_observer"
- "_observerQueue"
- "_observerResolutions"
- "_observerService"
- "_observingChainIdentities"
- "_observingLocalPolicy"
- "_pathIdentifier"
- "_performDescriptionRetrieval:forConnection:"
- "_persistentPropertyController"
- "_pid"
- "_pidToClientConnectionMapping"
- "_pidToRules"
- "_previousProvenanceTimestamp"
- "_primaryUsage"
- "_primaryUsagePage"
- "_processDescription"
- "_processor"
- "_queue"
- "_rawEvent"
- "_recognizers"
- "_removeNode:"
- "_repostedToBuffers"
- "_resolutionObserver"
- "_resolutionPaths"
- "_resolutionsWithIncompleteSequences"
- "_responsePending"
- "_rule"
- "_ruleChangeAuthority"
- "_selectDeferringPathForRequest:requestingPID:"
- "_selectionPathContainerByIdentifier"
- "_sender"
- "_senderCache"
- "_senderDescriptor"
- "_senderDescriptorForKeyboardEvents"
- "_senderDisplays"
- "_senderID"
- "_senderIDToSenderInfo"
- "_senderInfo"
- "_sequence"
- "_server"
- "_serviceClass"
- "_serviceMatcherDataProvider"
- "_serviceName"
- "_serviceStatus"
- "_serviceTarget"
- "_serviceWasRemoved"
- "_servicesForIOHIDServiceRefs:"
- "_setUpInitialProperties"
- "_shouldConsumeEvents"
- "_simpleProvenanceOriginator"
- "_startObserving:queue:sync:"
- "_startedMatching"
- "_string"
- "_stringRepresentation"
- "_strongSelf"
- "_subProcessors"
- "_subnodeSelectionHistoryByNodeIdentity"
- "_subnodes"
- "_supernodes"
- "_systemInterface"
- "_task"
- "_taskPortToClientConnectionMapping"
- "_terminating"
- "_test_deliveryRootForIdentifier:"
- "_test_peekAllEvents"
- "_test_peekAllIOHIDEvents"
- "_topLevelInEachProcess"
- "_trunkToBranchDictionary"
- "_userInfo"
- "_versionedPID"
- "_versionedPIDToClientConnectionMapping"
- "_workQueueAccessLock"
- "_workQueue_disappearanceObservers"
- "_workQueue_do_not_touch_directly"
- "_workQueue_removalNotification"
- "_workQueue_startIOServiceRemovalNotifications"
- "_workQueue_stopIOServiceRemovalNotifications"
- "_workQueue_willTerminateNotification"
- "acceptConnection"
- "acceptConnectionWithMappedObject:"
- "acceptIncomingServiceConnection:"
- "acceptIncomingServiceConnection:mappedObject:"
- "accessibilityHIDServices"
- "activate"
- "activeInputModality"
- "addDisappearanceObserver:queue:"
- "addEntriesFromDictionary:"
- "addEventObserver:"
- "addEventProcessor:"
- "addIndex:"
- "addObject:"
- "addObjectsFromArray:"
- "addRecognizer:recognitionBlock:"
- "addSenderInfo:"
- "addSenderInfo:forSenderID:"
- "addSibling:"
- "addSubnode:"
- "additionalContext"
- "allKeys"
- "allPersistentPropertiesForServicesMatchingDescriptor:"
- "allValues"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCollection:withName:itemBlock:"
- "appendCustomFormatWithName:block:"
- "appendDescriptionToFormatter:"
- "appendDescriptionToStream:"
- "appendEvent:sender:sequence:additionalContext:"
- "appendFormat:"
- "appendInteger:withName:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPointer:withName:"
- "appendProem:block:"
- "appendRightArrow"
- "appendString:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendUnsignedInteger:withName:format:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "associatedDisplay"
- "asyncSetProperties:"
- "asyncSetProperty:forKey:"
- "asyncSetProperty:forKey:andDelayForSeconds:"
- "auditToken"
- "authenticationOriginator"
- "autorelease"
- "blocks"
- "boolValue"
- "bs_addObject:toCollectionClass:forKey:"
- "bs_array"
- "bs_compactMap:"
- "bs_containsObjectPassingTest:"
- "bs_dictionaryByPartitioning:"
- "bs_filter:"
- "bs_flatten"
- "bs_map:"
- "bs_removeObject:fromCollectionForKey:"
- "bs_reverse"
- "buffer:drainEvent:withContext:sender:sequence:toResolution:"
- "bufferDidDrain:"
- "bufferDidEndDraining:"
- "bufferDidFinishDraining:"
- "bufferWillBeginDraining:"
- "bufferingDidAddNewBuffers:"
- "bufferingDispatcher"
- "bufferingPredicates"
- "build"
- "build:"
- "builderWithObject:"
- "builtinDisplay"
- "bundleIDForPID:"
- "can't disconnect the root"
- "claimsToConformToUsagePage:usage:"
- "class"
- "classForCoder"
- "clientConnectionManager"
- "clientEntitlement"
- "clientForDestination:"
- "clientForTaskPort:"
- "code"
- "com.apple.backboardd.touchStreams"
- "compatibilityDisplay"
- "componentsJoinedByString:"
- "configurationWithDomain:service:"
- "configure:"
- "conformsToBKHIDBufferedEventProcessor"
- "conformsToProtocol:"
- "connection:revokedWithEvent:"
- "connection:setObservesDeferringChainIdentities:entitled:"
- "connection:setObservesDeferringResolutions:"
- "connectionDescriptionForDeferringRuleIdentity:"
- "connectionDidTerminate:"
- "connectionForPID:"
- "connectionWillBegin:"
- "connectionWithConnection:"
- "constraint"
- "constraintAssertions"
- "constraintBasis"
- "constraints(%{public}@) now %{public}@"
- "containsObject:"
- "contentsMask"
- "copy"
- "copyClientForDestination:"
- "copyClientForTaskPort:"
- "copyConnection"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "current"
- "currentBuffersPerDispatchTarget"
- "currentConnection"
- "currentContext"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "deferringEnvironment"
- "deferringPath"
- "deferringRules"
- "deferringToken"
- "delegate"
- "deliveryChainDidUpdate:forIdentity:reason:"
- "deliveryChainsDescription"
- "deliveryChainsForDeferringTarget:display:environment:event:"
- "deliveryGraphDescription"
- "deliveryManagerForAuditToken:"
- "deliveryObserverServiceForAuditToken:"
- "describeDeliveryChain:identifier:"
- "describeDeliveryChains:identifier:"
- "describes:"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionForRootObject:"
- "descriptionForRootObject:withStyle:"
- "descriptionOfResolutionPathForEventDescriptor:senderDescriptor:"
- "descriptionOfResolutionPathForKeyCommand:senderDescriptor:"
- "descriptionWithMultilinePrefix:"
- "descriptorForHIDEvent:"
- "descriptors"
- "destinationsForEvent:fromSender:"
- "destinationsForEvent:sender:"
- "destinationsForKeyCommand:sender:"
- "destinationsStartingFromPID:deferringPredicate:"
- "dictionary"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithObjects:forKeys:count:"
- "didInitializeRegistryWithContext:"
- "didRespondBlockForConnection:"
- "didUpdateDeferringChains:"
- "didUpdateDeferringObservations:"
- "digitizerServicePersistentPropertyController"
- "disconnectFromGraph"
- "discreteDispatchingRules"
- "dispatcher"
- "dispatcherForEvent:"
- "dispatcherProvider"
- "dispatchingTarget"
- "displayWithHardwareIdentifier:"
- "domain"
- "domainIncomingServiceConnection"
- "drainAllEvents"
- "enumerateIndexesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateUserInfoWithBlock:"
- "enumerateWithBlock:"
- "environment"
- "event"
- "eventDescriptorIsRestricted:"
- "eventDispatcher"
- "eventProcessorOfClass:"
- "eventProcessorRegistry"
- "eventProvenance"
- "everySelectionPath"
- "existingServices"
- "fileURLWithPath:isDirectory:"
- "firstAdditionalContext"
- "firstObject"
- "fullyInitialized"
- "graphDescriptionWithLabel:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleIncomingDeliveryManagerConnection:"
- "handleIncomingDeliveryObserverConnection:"
- "handleIncomingServiceConnection:"
- "handler"
- "handlesPersistentPropertiesForSenderDescriptor:"
- "hardwareType"
- "hasBeenSignalled"
- "hasEntitlement:"
- "hasEvents"
- "hasPrefix:"
- "hasSuccinctStyle"
- "hash"
- "hidEventType"
- "hidSystem:receivedUpdatedDeviceOrientation:"
- "i16@0:8"
- "i24@0:8@16"
- "ignoreModalities"
- "incomingConnectionHandler"
- "incomingServiceConnectionDidRevoke:"
- "indexOfObject:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "indexOfObjectPassingTest:"
- "init"
- "initForSimulatorWithDisplayUUID:"
- "initFromPropertyList:"
- "initWithCapacity:"
- "initWithClientEntitlement:defaults:defaultsKey:"
- "initWithConnection:"
- "initWithConnection:log:"
- "initWithContext:"
- "initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:"
- "initWithDeliveryManagerProvider:"
- "initWithDeliveryManagerProvider:ruleChangeAuthority:"
- "initWithDeliveryObserverServiceProvider:"
- "initWithDispatchTarget:"
- "initWithDisplay:environment:"
- "initWithDomainServiceServer:"
- "initWithHIDEventSystem:"
- "initWithHIDServiceRef:"
- "initWithIdentifier:"
- "initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:"
- "initWithIncomingServiceConnection:debugMappedObjectName:"
- "initWithIncomingServiceConnectionHandler:"
- "initWithIncomingServiceConnectionHandler:ruleChangeAuthority:"
- "initWithMatchingDictionary:dataProvider:"
- "initWithMatchingDictionary:serviceClass:dataProvider:"
- "initWithOSLog:"
- "initWithObjects:"
- "initWithObjects:count:"
- "initWithObserverService:"
- "initWithProcessor:dispatcher:senderInfo:additionalContext:keyCommand:deliveryManager:resolutions:buffers:"
- "initWithQueue:"
- "initWithSenderDescriptor:dataProvider:"
- "initWithSenderDescriptor:matcherDataProvider:persistentPropertyController:"
- "initWithSenderID:"
- "initWithServer:"
- "initWithSubProcessors:defaultProcessor:"
- "initWithUsagePage:usage:builtIn:dataProvider:"
- "injectGSEvent:"
- "injectHIDEvent:"
- "insertObject:atIndex:"
- "instancesRespondToSelector:"
- "intValue"
- "integerValue"
- "interfaceWithIdentifier:"
- "intersectsSet:"
- "invalidate"
- "invalidated connection %{public}@"
- "isAuthenticated"
- "isBuiltIn"
- "isEqual:"
- "isEqualToString:"
- "isFullyInitialized"
- "isInvalid"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPencilDigitizer"
- "isProxy"
- "isRevoked"
- "isRoutableKeyCommand"
- "isVirtualService"
- "keyCommand"
- "keyCommandDispatchingRules"
- "keyCommands"
- "keyCommandsRegistrations"
- "keyboardFocusEnvironment"
- "label"
- "lastObject"
- "length"
- "listenerWithConfiguration:handler:"
- "localDefaults"
- "mainDisplay"
- "mainDisplayObserver"
- "matcher:servicesDidMatch:"
- "matchesDescriptor:failureReason:"
- "matchesHIDEvent:"
- "minusOrderedSet:"
- "minusSet:"
- "modality"
- "modalityAssertions"
- "mutableCopy"
- "node"
- "nullDisplay"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observerService"
- "options"
- "pathIdentifier"
- "performAsyncAndWait:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permittedRuleChangeMaskForAuditToken:"
- "persistentPropertiesForKeys:forSenderDescriptor:"
- "pidForBundleID:"
- "popSection:"
- "postEvent:position:additionalContext:"
- "postEvent:position:additionalContext:fromBuffer:toResolution:"
- "postEvent:toDestination:"
- "postEvent:withContext:toResolution:fromSequence:"
- "predicate"
- "predicateEventTypeMask"
- "primary"
- "primaryPage"
- "priority"
- "processDescription"
- "processDidTerminate:"
- "processEvent:sender:dispatcher:"
- "processEvent:shouldConsume:"
- "processEvent:withContext:buffer:sequence:sender:dispatcher:resolution:"
- "processor"
- "propertyForKey:"
- "propertyListEncoded"
- "propertyOfClass:forKey:"
- "protocolForProtocol:"
- "pushSection"
- "q"
- "q16@0:8"
- "q20@0:8i16"
- "q24@?0@\"BKEventDeferringNode\"8@\"BKEventDeferringNode\"16"
- "q32@0:8@\"NSDictionary\"16@\"BKSHIDEventSenderDescriptor\"24"
- "q32@0:8@16@24"
- "q32@0:8^{__IOHIDEvent=}16^B24"
- "q40@0:8N^^{__IOHIDEvent}16@\"<BKHIDEventSenderInfo>\"24@\"<BKHIDEventDispatcher>\"32"
- "q40@0:8N^^{__IOHIDEvent}16@24@32"
- "q72@0:8N^^{__IOHIDEvent}16@24@\"BKHIDEventBuffer\"32@\"BKHIDEventDeliverySequence\"40@\"<BKHIDEventSenderInfo>\"48@\"<BKHIDEventDispatcher>\"56@\"BKSHIDEventDeferringResolution\"64"
- "q72@0:8N^^{__IOHIDEvent}16@24@32@40@48@56@64"
- "queue"
- "queueWithName:"
- "reason"
- "recognizerForEventDescriptor:"
- "recognizerForEventDescriptors:"
- "recognizers"
- "reevaluateBufferingWithContext:"
- "registerHandler:"
- "registerIOHIDServicesCallback:matchingDictionary:target:refCon:"
- "rejectConnection"
- "rejectIncomingServiceConnection:"
- "release"
- "remoteTarget"
- "remoteTargetForServiceConnection:"
- "remoteToken"
- "removeAllObjects"
- "removeDisappearanceObserver:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObjectsInArray:"
- "removeRecognizer:"
- "removeSenderInfo:"
- "repostFirstEventToBufferedTargets:"
- "requestBufferReevaluationWithContext:"
- "requestSelectionChanges:forClientWithPID:"
- "resolutionDescriptionForEventDescriptor:senderDescriptor:"
- "resolutionDescriptionForKeyCommand:senderDescriptor:"
- "resolutionObserver"
- "resolutions"
- "respondsToSelector:"
- "responsePendingForConnection:"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "revoked"
- "rule"
- "ruleChangeAuthority"
- "ruleOriginatorBasis"
- "rules"
- "sameLine:"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "seed"
- "selection request deferring target is nil: %{public}@"
- "selection request deferring target token is nil: %{public}@"
- "selection request target not found: %{public}@"
- "selection request token is not accessible by the requesting process(%{public}@): %{public}@"
- "selectionPath"
- "selectionPathIdentifier"
- "selectionRequests"
- "selectionTarget"
- "self"
- "sendEvent:toClientTaskPort:"
- "sendEvent:toDestination:"
- "senderCache"
- "senderDescriptor"
- "senderDescriptorForEventType:"
- "senderDescriptors"
- "senderInfoForSenderID:"
- "sequence"
- "sequenceForFirstEvent:sender:processor:dispatcher:additionalContext:"
- "sequenceForKeyCommand:sender:processor:dispatcher:additionalContext:"
- "serviceDidDisappear:"
- "serviceMatcherDataProvider"
- "set"
- "setAdditionalContext:"
- "setAllBufferingClientsTerminated:"
- "setAssociatedDisplay:"
- "setAuthenticated:"
- "setBasis:"
- "setBlocks:"
- "setBufferingDispatcher:"
- "setBufferingPIDs:"
- "setBuiltIn:"
- "setClient:"
- "setConstraintAssertions:forClientWithPID:"
- "setDeferringRules:forClientWithPID:"
- "setDelegate:"
- "setDispatcherProvider:"
- "setDispatchingRoots:forClientWithPID:"
- "setDispatchingTarget:"
- "setDisplay:"
- "setDisplayChangedHandler:"
- "setDisplayUUID:"
- "setElementValue:forUsagePage:usage:"
- "setEnvironment:"
- "setEvent:"
- "setEventBufferingPredicates:forClientWithPID:"
- "setEventDispatcher:"
- "setEventProcessorRegistry:"
- "setEventSource:"
- "setFinalStringToken:"
- "setFullyInitialized:"
- "setHIDSystemChannel:"
- "setHandler:"
- "setHardwareType:"
- "setIOHIDService:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInvalidationHandler:"
- "setKeyCommandRoots:forClientWithPID:"
- "setKeyCommands:"
- "setKeyCommandsRegistrations:forClientWithPID:"
- "setMainDisplay:"
- "setMainDisplayObserver:"
- "setMaximumValueLengthBeforeTruncation:"
- "setModalityAssertions:forClientWithPID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObservesDeferringChainIdentities:"
- "setObservesDeferringResolutions:"
- "setPersistentProperties:forSenderDescriptor:"
- "setPersistentProperties:forServicesMatchingDescriptor:"
- "setPid:"
- "setPolicyStatus:"
- "setPrimaryPage:primaryUsage:"
- "setPrimaryUsage:"
- "setPrimaryUsagePage:"
- "setProcessDescription:"
- "setProperties:"
- "setProperty:forKey:"
- "setQueue:"
- "setRecognizers:"
- "setResolutionObserver:"
- "setSelectionPath:"
- "setSender:"
- "setSenderDescriptor:"
- "setSenderID:"
- "setSequence:"
- "setServer:"
- "setServiceMatcherDataProvider:"
- "setServiceStatus:"
- "setShouldConsumeEvents:"
- "setSystemInterface:"
- "setSystemProperty:forKey:"
- "setToken:"
- "setUserInfo:"
- "setUserInfo:forConnection:"
- "setValue:forKey:"
- "setValueTruncation:"
- "setWithArray:"
- "setWithObject:"
- "sharedInstance"
- "sharedInstances"
- "shouldConsumeEvents"
- "signal"
- "simpleProvenanceOriginator"
- "sortedArrayUsingSelector:"
- "source"
- "specifiesDescriptor:"
- "startEventProcessor:mainDisplayObserver:deliveryManager:dispatcherProvider:"
- "startEventRouting"
- "startHIDSystem"
- "startObserving:queue:"
- "startObservingSynchronously:"
- "startServerWithChannel:"
- "stringByAppendingPathComponent:"
- "stringByReplacingCharactersInRange:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "submitRuleChanges:"
- "subnodes"
- "subsetForPID:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "succinctStyle"
- "superclass"
- "supernode"
- "sync"
- "systemEventOfType:matchingEvent:options:"
- "systemInterface"
- "systemPropertyForKey:"
- "target"
- "task"
- "timestamp"
- "topLevel"
- "touchSensitiveButtonServicePersistentPropertyController"
- "unionSet:"
- "uniqueProductIdentifier"
- "unknownSenderInfo"
- "unregisterIOHIDServicesCallback:matchingDictionary:target:refCon:"
- "unsignedLongLongValue"
- "userEventNotifier must not be nil"
- "userEventOccurredOnDisplay:"
- "userInfo"
- "userInfoForConnection:"
- "v16@0:8"
- "v16@?0@\"BKSMutableHIDEventPolicyObservation\"8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"<BKHIDEventProcessor>\"16"
- "v24@0:8@\"<BSDescriptionFormatting>\"16"
- "v24@0:8@\"BKHIDDomainIncomingServiceConnection\"16"
- "v24@0:8@\"BKHIDEventBuffer\"16"
- "v24@0:8@\"BKHIDEventProcessorCreationContext\"16"
- "v24@0:8@\"BKHIDEventReevaluateBufferingContext\"16"
- "v24@0:8@\"BKHIDIncomingServiceConnection\"16"
- "v24@0:8@\"BKIOHIDService\"16"
- "v24@0:8@\"BSDescriptionStream\"16"
- "v24@0:8@\"BSServiceListenerConnection\"16"
- "v24@0:8@\"NSArray<__BKSEventDeferringChainIdentity__>\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{__GSEvent=}16"
- "v24@0:8^{__IOHIDEvent=}16"
- "v24@0:8^{__IOHIDService=}16"
- "v24@0:8q16"
- "v24@?0@\"NSNumber\"8@\"BKSHIDEventPolicyObservation\"16"
- "v24@?0Q8^B16"
- "v28@0:8@16i24"
- "v28@0:8I16I20I24"
- "v28@0:8^{__IOHIDEvent=}16I24"
- "v32@0:8@\"BKHIDIncomingServiceConnection\"16@24"
- "v32@0:8@\"BKIOHIDServiceMatcher\"16@\"NSArray\"24"
- "v32@0:8@\"BSServiceListenerConnection\"16@\"<BSServiceListenerConnectionRevocationEvent>\"24"
- "v32@0:8@16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8^{__IOHIDEvent=}16@24"
- "v32@?0@\"BKEventDeferringEnvironmentGraph\"8@\"NSArray\"16^B24"
- "v32@?0@\"NSNumber\"8@\"BKEventDeferringNode\"16^B24"
- "v32@?0@\"NSNumber\"8@\"NSSet\"16^B24"
- "v32@?0@8@\"NSMutableDictionary\"16^B24"
- "v32@?0@8@\"NSMutableSet\"16^B24"
- "v36@0:8@16@24B32"
- "v36@0:8i16@20@28"
- "v40@0:8@\"BKSHIDEventDeliveryChain\"16@\"BKSEventDeferringChainIdentity\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8^{__IOHIDEvent=}16q24@32"
- "v48@0:8@16@24@32@40"
- "v48@0:8^?16@\"NSDictionary\"24^v32^v40"
- "v48@0:8^?16@24^v32^v40"
- "v48@0:8^{__IOHIDEvent=}16@24@\"BKSHIDEventDeferringResolution\"32@\"BKHIDEventDeliverySequence\"40"
- "v48@0:8^{__IOHIDEvent=}16@24@32@40"
- "v56@0:8^{__IOHIDEvent=}16q24@32@40@48"
- "v64@0:8@\"BKHIDEventBuffer\"16^{__IOHIDEvent=}24@32@\"<BKHIDEventSenderInfo>\"40@\"BKHIDEventDeliverySequence\"48@\"BKSHIDEventDeferringResolution\"56"
- "v64@0:8@16^{__IOHIDEvent=}24@32@40@48@56"
- "validateMessage:"
- "valueForKey:defaultValueProvider:"
- "verifyAuthentic:"
- "versionedPID"
- "versionedPIDForPID:"
- "void _BKHIDSetUserEventNotifier(__strong id<BKHIDUserEventNotifying> _Nonnull)"
- "weightedDeferringRuleCompare:"
- "wildcard"
- "writeString:"
- "zone"
- "{atomic_flag=\"_Value\"AB}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
