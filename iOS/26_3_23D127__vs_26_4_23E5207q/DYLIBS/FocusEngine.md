## FocusEngine

> `/System/Library/PrivateFrameworks/FocusEngine.framework/FocusEngine`

```diff

-9126.3.6.1.104
-  __TEXT.__text: 0x2f9c8
-  __TEXT.__auth_stubs: 0x7f0
+9126.4.20.1.105
+  __TEXT.__text: 0x31ad8
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x3a48
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x4566
-  __TEXT.__gcc_except_tab: 0x56c
+  __TEXT.__cstring: 0x455f
+  __TEXT.__gcc_except_tab: 0x4ec
   __TEXT.__oslogstring: 0xcd7
   __TEXT.__ustring: 0x35c
-  __TEXT.__unwind_info: 0xd18
+  __TEXT.__unwind_info: 0xda8
   __TEXT.__objc_classname: 0x8c1
   __TEXT.__objc_methname: 0x9e2b
   __TEXT.__objc_methtype: 0x1ce7

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x258
-  __AUTH_CONST.__cfstring: 0x29c0
+  __AUTH_CONST.__cfstring: 0x29a0
   __AUTH_CONST.__objc_const: 0x71d8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/SubFrameworks/UIUtilities.framework/UIUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30FDAB7D-F6FE-34F8-BEE4-175AE16D00C8
-  Functions: 1209
-  Symbols:   4359
-  CStrings:  2485
+  UUID: CE5163FA-8E15-3231-B98E-0754922469D0
+  Functions: 1210
+  Symbols:   4355
+  CStrings:  2483
 
Symbols:
+ __UIFocusRectInset
+ _objc_release_x2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _objc_retain_x9
Functions:
~ __UITreeFirstCommonAncestor : 356 -> 348
~ ___recursePreOrderDepthFirstTraversal : 496 -> 508
~ -[_UIFocusGroup initWithIdentifier:parentGroup:coordinateSpace:] : 444 -> 440
~ -[_UIFocusGroup _deepCopyWithNewIdentifierToGroupMap:] : 532 -> 564
~ -[_UIFocusGroup _updateWithEnvironment:] : 172 -> 176
~ -[_UIFocusGroup primaryItem] : 56 -> 64
~ -[_UIFocusGroup _validatePrimaryItemIfNecessary] : 592 -> 616
~ -[_UIFocusGroup _validatePrimaryRectIfNeccessary] : 412 -> 436
~ -[_UIFocusGroup description] : 160 -> 172
~ -[_UIFocusGroup debugDescription] : 196 -> 212
~ -[_UIFocusGroupHistory init] : 176 -> 184
~ -[_UIFocusGroupHistory setLastFocusedItem:forGroupIdentifier:] : 268 -> 276
~ __UIFocusItemSafeCast : 92 -> 96
~ __UIFocusEnvironmentParentEnvironment : 384 -> 400
~ __UIFocusEnvironmentRootAncestorEnvironment : 264 -> 280
~ __UIFocusEnvironmentIsAncestorOfEnvironment : 252 -> 248
~ __UIFocusEnvironmentEnumerateAncestorEnvironments : 248 -> 252
~ __UIFocusEnvironmentsHaveCommonHierarchy : 124 -> 128
~ __UIFocusEnvironmentShouldUpdateFocus : 244 -> 248
~ __UIFocusEnvironmentInheritedFocusMovementStyle : 324 -> 332
~ ____UIFocusEnvironmentInheritedFocusMovementStyle_block_invoke : 140 -> 148
~ __UIFocusEnvironmentIsEligibleForFocusInteraction : 188 -> 196
~ __UIFocusEnvironmentIsEligibleForFocusOcclusion : 220 -> 228
~ __UIFocusEnvironmentPreferredFocusMapContainer : 388 -> 392
~ ____UIFocusEnvironmentPreferredFocusMapContainer_block_invoke : 232 -> 244
~ __UIFocusEnvironmentContainerFrameInCoordinateSpace : 236 -> 244
~ __UIFocusEnvironmentRotaryFocusMovementAxis : 180 -> 184
~ __UIFocusEnvironmentPrefersFocusContainment : 124 -> 132
~ __UIFocusEnvironmentResolvedRotaryFocusMovementAxis : 688 -> 700
~ ____UIFocusEnvironmentResolvedRotaryFocusMovementAxis_block_invoke : 136 -> 144
~ __UIFocusEnvironmentPreferredFocusEnvironments : 128 -> 132
~ __UIFocusEnvironmentEffectivePreferredFocusEnvironments : 380 -> 400
~ __UIFocusEnvironmentAllowsFocusToLeaveViaHeading : 88 -> 92
~ -[_UIFocusUpdateRequest init] : 108 -> 112
~ -[_UIFocusUpdateRequest initWithEnvironment:] : 228 -> 232
~ -[_UIFocusUpdateRequest initWithFocusSystem:environment:] : 328 -> 332
~ -[_UIFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:] : 524 -> 536
~ -[_UIFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment] : 304 -> 308
~ ___78-[_UIFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment]_block_invoke : 160 -> 172
~ -[_UIFocusUpdateRequest canMergeWithRequest:] : 328 -> 352
~ -[_UIFocusUpdateRequest requestByMergingWithRequest:] : 556 -> 564
~ -[_UIFocusUpdateRequest focusSystem] : 208 -> 216
~ -[_UIFocusUpdateRequest cacheCurrentFocusSystem] : 84 -> 88
~ -[_UIFocusUpdateRequest isValidInFocusSystem:] : 232 -> 244
~ -[_UIFocusEnvironmentPreferenceCacheNode initWithEnvironment:] : 148 -> 144
~ -[_UIFocusEnvironmentPreferenceCacheNode _reevaluateResolution] : 456 -> 472
~ -[_UIFocusEnvironmentPreferenceCacheNode _resolve:explicitly:] : 360 -> 348
~ -[_UIFocusEnvironmentPreferenceCacheNode setChildNodes:] : 444 -> 448
~ -[_UIFocusEnvironmentPreferenceCacheNode description] : 312 -> 324
~ -[_UIFocusEnvironmentPreferenceCacheNode debugDescription] : 296 -> 308
~ __UIFocusRegionSearchContextAddChildItemsInEnvironmentContainer : 520 -> 548
~ __UIFocusRegionSearchContextSearchForFocusRegionsInEnvironment : 760 -> 796
~ -[_UIFocusRegion initWithFrame:coordinateSpace:] : 244 -> 240
~ -[_UIFocusRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 328 -> 336
~ -[_UIFocusRegion _descriptionBuilder] : 332 -> 356
~ -[_UIFocusRegion description] : 76 -> 84
~ -[_UIFocusRegion isEqual:] : 244 -> 232
~ -[_UIFocusRegion _effectiveBoundariesBlockingFocusMovementRequest:] : 116 -> 120
~ -[_UIFocusGuideImpl initWithDelegate:] : 240 -> 244
~ -[_UIFocusGuideImpl preferredFocusEnvironments] : 252 -> 260
~ -[_UIFocusGuideImpl setPreferredFocusEnvironments:] : 132 -> 156
~ -[_UIFocusGuideImpl _isEligibleForFocusInteraction] : 124 -> 132
~ -[_UIFocusGuideImpl _preferredFocusRegionCoordinateSpace] : 100 -> 112
~ -[_UIFocusGuideImpl _searchForFocusRegionsInContext:] : 356 -> 368
~ -[_UIFocusGuideImpl focusGuideRegion:preferredFocusEnvironmentsForMovementRequest:] : 180 -> 192
~ -[_UIFocusGuideImpl focusGuideRegion:willParticipateAsDestinationRegionInFocusUpdate:] : 100 -> 112
~ -[_UIFocusGuideImpl description] : 176 -> 184
~ -[_UIFocusContainerGuideImpl _isEligibleForFocusInteraction] : 76 -> 80
~ -[_UIFocusContainerGuideImpl _searchForFocusRegionsInContext:] : 492 -> 536
~ -[_UIFocusContainerGuideImpl fallbackItemProvider] : 16 -> 8
~ -[_UIFocusContainerGuideImpl setFallbackItemProvider:] : 12 -> 8
~ -[_UIFocusContainerGuideImpl .cxx_destruct] : 20 -> 12
~ -[_UIDebugLogReport messageCount] : 56 -> 60
~ -[_UIDebugLogReport addMessageWithFormat:] : 192 -> 196
~ -[_UIDebugLogReport addMessage:] : 284 -> 304
~ -[_UIDebugLogReport addLineBreak] : 112 -> 116
~ -[_UIDebugLogReport fallbackMessagePrefixHandler] : 76 -> 72
~ ___49-[_UIDebugLogReport fallbackMessagePrefixHandler]_block_invoke : 28 -> 76
~ -[_UIDebugLogReport pushMessagePrefix:] : 184 -> 200
~ -[_UIDebugLogReport pushMessagePrefixHandler:] : 204 -> 220
~ -[_UIDebugLogReport popMessagePrefix] : 64 -> 68
~ -[_UIDebugLogReport clearAllMessagePrefixes] : 64 -> 68
~ -[_UIDebugLogReport _messagePrefixAtIndentLevel:] : 308 -> 332
~ -[_UIDebugLogReport incrementIndentLevelAndPushMessagePrefix:] : 88 -> 92
~ -[_UIDebugLogReport setStatements:] : 12 -> 64
~ -[_UIDebugLogReport setPrefixStack:] : 12 -> 64
~ -[_UIDebugLogReportFormatter _componentsFromReport:] : 292 -> 296
~ ___52-[_UIDebugLogReportFormatter _componentsFromReport:]_block_invoke : 632 -> 664
~ ___52-[_UIDebugLogReportFormatter _componentsFromReport:]_block_invoke_2 : 156 -> 168
~ -[_UIDebugLogReportFormatter stringFromReport:] : 88 -> 96
~ +[_UIDebugIssue issueWithDescription:] : 184 -> 188
~ +[_UIDebugIssue issueWithFormat:] : 220 -> 228
~ -[_UIDebugIssue addIssue:] : 176 -> 184
~ -[_UIDebugIssueReport addIssue:] : 176 -> 184
~ -[_UIDebugIssueReportFormatter defaultIssuePrefix] : 80 -> 92
~ -[_UIDebugIssueReportFormatter _componentsFromReport:] : 604 -> 628
~ ___54-[_UIDebugIssueReportFormatter _componentsFromReport:]_block_invoke : 396 -> 428
~ -[_UIDebugIssueReportFormatter stringFromReport:] : 88 -> 96
~ -[_UIFocusMovementInfo description] : 152 -> 164
~ -[_UIFocusMovementInfo encodeWithXPCDictionary:] : 380 -> 384
~ -[_UIFocusMovementInfo encodeWithCoder:] : 368 -> 372
~ -[_UIDebugReportFormatter stringFromReportComponents:] : 664 -> 700
~ -[_UIFocusEnvironmentPreferenceEnumerationContext init] : 108 -> 112
~ -[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:] : 652 -> 668
~ ___92-[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]_block_invoke : 348 -> 376
~ -[_UIFocusEnvironmentPreferenceEnumerationContext isLeafPreference] : 60 -> 64
~ -[_UIFocusEnvironmentPreferenceEnumerationContext isPreferredByItself] : 56 -> 60
~ -[_UIFocusEnvironmentPreferenceEnumerationContext preferringEnvironment] : 100 -> 104
~ -[_UIFocusEnvironmentPreferenceEnumerationContext preferredEnvironments] : 68 -> 76
~ -[_UIFocusEnvironmentPreferenceEnumerationContext _resolvePreferredFocusEnvironments] : 748 -> 776
~ -[_UIFocusEnvironmentPreferenceEnumerationContext _inferPreferencesForEnvironment:] : 360 -> 368
~ -[_UIFocusEnvironmentPreferenceEnumerationContext _isAllowedToPreferEnvironment:] : 480 -> 492
~ -[_UIFocusEnvironmentPreferenceEnumerationContext pushEnvironment:] : 516 -> 564
~ -[_UIFocusEnvironmentPreferenceEnumerationContext popEnvironment] : 244 -> 256
~ -[_UIFocusEnvironmentPreferenceEnumerationContext _startLogging] : 508 -> 528
~ -[_UIFocusEnvironmentPreferenceEnumerationContext _reportInferredPreferredFocusEnvironment:] : 312 -> 336
~ -[_UIFocusEnvironmentPreferenceEnumerationContext setDebugStack:] : 12 -> 64
~ -[_UIFocusEnvironmentPreferenceEnumerator enumeratePreferencesForEnvironment:usingBlock:] : 376 -> 384
~ __enumeratePreferredFocusEnvironments : 976 -> 896
~ -[_UIFocusEnvironmentPreferenceEnumerator setDebugLog:] : 12 -> 64
~ ___96-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:]_block_invoke : 240 -> 256
~ ___96-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:]_block_invoke_2 : 72 -> 76
~ ___96-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:]_block_invoke_3 : 896 -> 864
~ -[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusEnvironmentForEnvironment:] : 736 -> 748
~ ___87-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusEnvironmentForEnvironment:]_block_invoke : 188 -> 208
~ -[_UIDeepestPreferredEnvironmentSearch _overridingPreferredFocusEnvironmentForPreferredEnvironment:visitedFocusEnvironments:] : 604 -> 600
~ ___125-[_UIDeepestPreferredEnvironmentSearch _overridingPreferredFocusEnvironmentForPreferredEnvironment:visitedFocusEnvironments:]_block_invoke : 216 -> 228
~ -[_UIDeepestPreferredEnvironmentSearch _reportStartingSearch] : 112 -> 120
~ -[_UIDeepestPreferredEnvironmentSearch _reportFoundFocusableItem:inContext:] : 120 -> 128
~ -[_UIDeepestPreferredEnvironmentSearch _reportFinishedEvaluatingAllPreferencesForEnvironmentInContext:result:] : 508 -> 544
~ ___110-[_UIDeepestPreferredEnvironmentSearch _reportFinishedEvaluatingAllPreferencesForEnvironmentInContext:result:]_block_invoke : 108 -> 112
~ -[_UIDeepestPreferredEnvironmentSearch _reportDidFinishEnumeratingPreferencesWithDeepestPreferredFocusableItem:] : 308 -> 336
~ -[_UIDeepestPreferredEnvironmentSearch _reportDidFindOverridingPreferredFocusEnvironment:source:] : 400 -> 424
~ -[_UIDeepestPreferredEnvironmentSearch _reportDidFindLockedFocusEnvironment:] : 288 -> 312
~ -[_UIDeepestPreferredEnvironmentSearch setDebugLog:] : 12 -> 64
~ -[_UIFocusItemDummy preferredFocusEnvironments] : 116 -> 120
~ -[_UIFocusMovementRequest init] : 108 -> 112
~ -[_UIFocusMovementRequest initWithFocusSystem:] : 192 -> 196
~ -[_UIFocusMovementRequest _requestByRedirectingRequestToFocusSystem:] : 112 -> 120
~ -[_UIFocusMovementRequest focusedItemInfo] : 140 -> 156
~ -[_UIFocusMovementRequest movementInfo] : 128 -> 136
~ -[_UIFocusMovementRequest searchInfo] : 88 -> 100
~ -[_UIFocusMovementRequest fallbackRequest] : 124 -> 132
~ -[_UIFocusMovementRequest setInputDeviceInfo:] : 12 -> 64
~ -[_UIFocusMovementRequest setFocusedItemInfo:] : 12 -> 64
~ -[_UIFocusMovementRequest setMovementInfo:] : 12 -> 64
~ -[_UIFocusMovementRequest setSearchInfo:] : 12 -> 64
~ -[_UIFocusMap init] : 108 -> 112
~ -[_UIFocusMap initWithFocusSystem:rootEnvironment:] : 276 -> 280
~ -[_UIFocusMap initWithFocusSystem:rootEnvironment:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:] : 272 -> 280
~ -[_UIFocusMap initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:] : 528 -> 544
~ -[_UIFocusMap _defaultMapSnapshotter] : 184 -> 188
~ -[_UIFocusMap _inferredDefaultFocusItemInEnvironment:] : 1768 -> 1828
~ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:] : 1064 -> 1148
~ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:] : 1284 -> 1324
~ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:inRegions:withSnapshot:] : 176 -> 184
~ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:] : 208 -> 212
~ -[_UIFocusMap _nextFocusedItemForNonLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:] : 3492 -> 3472
~ -[_UIFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:] : 1736 -> 1824
~ ___103-[_UIFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]_block_invoke : 96 -> 100
~ -[_UIFocusMap _allRegionsInContainer:intersectingRegion:] : 356 -> 376
~ -[_UIFocusMap _closestFocusableItemToPoint:inRect:itemFilter:distanceMeasuringUnitPoint:] : 1028 -> 1048
~ -[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:] : 556 -> 592
~ ___76-[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]_block_invoke : 76 -> 80
~ -[_UIFocusMap verifyFocusabilityForItem:] : 628 -> 668
~ -[_UIFocusMap _beginTrackingSearches] : 124 -> 128
~ -[_UIFocusMap _stopTrackingSearches] : 152 -> 164
~ -[_UIFocusMap _trackExternalSnapshot:] : 132 -> 140
~ -[_UIFocusMap diagnoseFocusabilityForItem:report:] : 1232 -> 1288
~ -[_UIFocusMapSearchInfo snapshots] : 72 -> 76
~ -[_UIFocusMapSearchInfo destinationRegions] : 72 -> 76
~ -[_UIFocusMapSearchInfo addSnapshot:] : 132 -> 144
~ -[_UIFocusMapSearchInfo addDestinationRegion:] : 104 -> 108
~ -[_UIFocusMapSearchInfo setLinearSortedFocusItems:] : 12 -> 64
~ -[_UIFocusMapSearchInfo setFocusGroupMap:] : 12 -> 64
~ -[_UIFocusMapSearchInfo setMutableSnapshots:] : 12 -> 64
~ -[_UIFocusMapSearchInfo setMutableDestinationRegions:] : 12 -> 64
~ -[_UIFocusMapSearchInfo setSearchInfo:] : 12 -> 64
~ -[UIFocusUpdateContext init] : 136 -> 140
~ -[UIFocusUpdateContext _initWithFocusUpdateRequest:] : 404 -> 428
~ -[UIFocusUpdateContext _initWithFocusMovementRequest:nextFocusedItem:] : 348 -> 364
~ -[UIFocusUpdateContext _initWithContext:] : 356 -> 392
~ -[UIFocusUpdateContext _cacheFocusBehavior] : 112 -> 124
~ -[UIFocusUpdateContext _isValidInFocusSystem:] : 132 -> 136
~ -[UIFocusUpdateContext _validate] : 1072 -> 1104
~ ___33-[UIFocusUpdateContext _validate]_block_invoke_2 : 684 -> 712
~ -[UIFocusUpdateContext previouslyFocusedItem] : 76 -> 84
~ -[UIFocusUpdateContext nextFocusedItem] : 76 -> 84
~ -[UIFocusUpdateContext _destinationItemInfo] : 56 -> 64
~ -[UIFocusUpdateContext linearSortedFocusItems] : 76 -> 84
~ -[UIFocusUpdateContext _updateDestinationItemIfNeeded] : 380 -> 412
~ -[UIFocusUpdateContext _commonAncestorEnvironment] : 160 -> 172
~ -[UIFocusUpdateContext focusHeading] : 56 -> 60
~ -[UIFocusUpdateContext _focusVelocity] : 104 -> 108
~ -[UIFocusUpdateContext _isInitialMovement] : 56 -> 60
~ -[UIFocusUpdateContext _setFocusedGuideImpl:] : 128 -> 132
~ -[UIFocusUpdateContext _focusedGuide] : 76 -> 80
~ -[UIFocusUpdateContext _willUpdateFocusFromFocusedItem:] : 140 -> 152
~ -[UIFocusUpdateContext _didUpdateFocus] : 288 -> 300
~ -[UIFocusUpdateContext _restoreRestrictedFocusMovementWithMovement:] : 12 -> 64
~ -[UIFocusUpdateContext _focusGroupMap] : 196 -> 220
~ -[UIFocusUpdateContext _previouslyFocusedGroupIdentifier] : 148 -> 168
~ -[UIFocusUpdateContext _nextFocusedGroupIdentifier] : 148 -> 168
~ -[UIFocusUpdateContext _groupFilter] : 56 -> 60
~ -[UIFocusUpdateContext description] : 488 -> 528
~ -[UIFocusUpdateContext _setFocusGroupMap:] : 12 -> 64
~ -[UIFocusUpdateContext _setCommonEnvironmentScrollableContainer:] : 12 -> 64
~ -[UIFocusUpdateContext _setPreferredFocusReport:] : 12 -> 64
~ -[UIFocusUpdateContext _setValidationReport:] : 12 -> 64
~ -[_UIFocusMovementPerformer performFocusMovement:] : 708 -> 728
~ -[_UIFocusMovementPerformer __findFocusCandidateInEnvironment:container:forRequest:minimumSearchArea:isLoadingScrollableContainer:] : 468 -> 496
~ -[_UIFocusMovementPerformer _findFocusCandidateByExhaustivelySearchingEnvironment:scrollableContainer:forRequest:] : 680 -> 712
~ __UIFocusShiftAndExpandRectAlongFocusMovement : 500 -> 524
~ -[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:] : 468 -> 480
~ ___98-[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke : 288 -> 272
~ ___98-[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke_2 : 480 -> 508
~ -[_UIFocusMovementPerformer _bestCandidateForNonLinearFocusMovement:] : 1012 -> 1092
~ -[_UIFocusMovementPerformer _bestCandidateForLinearFocusMovement:] : 312 -> 352
~ -[_UIFocusMovementPerformer contextForFocusMovement:] : 140 -> 156
~ -[_UIFocusMovementPerformer _environmentContainersToCheckForRequest:] : 692 -> 760
~ -[_UIFocusMovementPerformer _dummyFocusItemForFocusMovement:searchArea:parent:] : 472 -> 480
~ -[_UIFocusMovementPerformer _nextLinearCandidateLoadingScrollableContentForRequest:] : 1824 -> 1940
~ -[_UIFocusMovementPerformer _isMovementValidForFocusSequences:] : 268 -> 272
~ ___63-[_UIFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke : 208 -> 224
~ ___63-[_UIFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke_2 : 264 -> 284
~ -[_UIFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:shouldLoadScrollableContainer:] : 388 -> 424
~ -[_UIFocusMapSnapshot init] : 108 -> 112
~ -[_UIFocusMapSnapshot _initWithSnapshotter:mapArea:searchArea:] : 800 -> 844
~ -[_UIFocusMapSnapshot regions] : 484 -> 476
~ -[_UIFocusMapSnapshot originalRegions] : 400 -> 420
~ -[_UIFocusMapSnapshot regionsForOriginalRegion:] : 444 -> 456
~ -[_UIFocusMapSnapshot _trackSubregion:forRegion:] : 356 -> 368
~ -[_UIFocusMapSnapshot originalRegionForRegion:] : 252 -> 260
~ -[_UIFocusMapSnapshot _trackOccludingRegion:forRegion:] : 188 -> 196
~ -[_UIFocusMapSnapshot occludingRegionsForRegion:] : 236 -> 248
~ -[_UIFocusMapSnapshot consumeRegionInformationForRegions:fromSnapshot:] : 388 -> 412
~ -[_UIFocusMapSnapshot _cachedNextFocusedItemForRegion:withFocusMovementRequest:inMap:] : 296 -> 324
~ -[_UIFocusMapSnapshot snapshotFrameForRegion:] : 308 -> 316
~ -[_UIFocusMapSnapshot markContainerAsProvidingDynamicContent] : 104 -> 112
~ -[_UIFocusMapSnapshot _capture] : 536 -> 556
~ -[_UIFocusMapSnapshot coordinateSpace] : 76 -> 84
~ -[_UIFocusMapSnapshot addRegion:] : 876 -> 920
~ -[_UIFocusMapSnapshot addRegions:] : 332 -> 336
~ -[_UIFocusMapSnapshot addRegionsInContainer:] : 3408 -> 3420
~ ___45-[_UIFocusMapSnapshot addRegionsInContainer:]_block_invoke : 172 -> 176
~ -[_UIFocusMapSnapshot addRegionsInContainers:] : 332 -> 336
~ -[_UIFocusMapSnapshot setSearchInfo:] : 12 -> 64
~ -[_UIFocusMapSnapshot setMovementInfo:] : 12 -> 64
~ -[_UIFocusRegionSearchContextState initWithRegionContainer:focusSystem:clippingRect:] : 192 -> 184
~ +[_UIFocusRegionSearchContextState stateWithRegionContainer:focusSystem:clippingRect:] : 160 -> 156
~ _____UIFocusMapRecurseSearchForFocusSystemInEligibleContainer_block_invoke : 324 -> 328
~ -[_UIFocusDebuggerStringOutput initWithString:] : 200 -> 204
~ -[_UIFocusDebuggerStringOutput description] : 24 -> 72
~ +[UIFocusDebugger help] : 420 -> 424
~ ___23+[UIFocusDebugger help]_block_invoke : 208 -> 204
~ +[UIFocusDebugger status] : 424 -> 440
~ +[UIFocusDebugger _verboseStatus] : 388 -> 400
~ +[UIFocusDebugger _statusForFocusSystem:includeDeferralTarget:] : 684 -> 724
~ +[UIFocusDebugger checkFocusabilityForItem:] : 860 -> 912
~ +[UIFocusDebugger simulateFocusUpdateRequestFromEnvironment:] : 1440 -> 1548
~ +[UIFocusDebugger _ancestryForEnvironment:] : 424 -> 432
~ ___43+[UIFocusDebugger _ancestryForEnvironment:]_block_invoke : 196 -> 212
~ +[UIFocusDebugger focusGroupsForEnvironment:] : 656 -> 684
~ ___45+[UIFocusDebugger focusGroupsForEnvironment:]_block_invoke : 164 -> 176
~ +[UIFocusDebugger preferredFocusEnvironmentsForEnvironment:] : 472 -> 488
~ ___60+[UIFocusDebugger preferredFocusEnvironmentsForEnvironment:]_block_invoke : 348 -> 372
~ -[_UIFocusEnvironmentPreferenceCache init] : 112 -> 116
~ -[_UIFocusEnvironmentPreferenceCache preferredEnvironmentsForEnvironment:isFinal:] : 340 -> 368
~ -[_UIFocusEnvironmentPreferenceCache setResolvedPreference:forEnvironment:] : 232 -> 240
~ -[_UIFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:] : 596 -> 636
~ ___78-[_UIFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]_block_invoke : 188 -> 200
~ -[_UIFocusEnvironmentPreferenceCache deepestPrimaryPreferredEnvironmentForEnvironment:] : 240 -> 268
~ -[UIFocusMovementAction initWithFocusMovementInfo:] : 112 -> 116
~ -[UIFocusMovementAction initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:focusedFrameInSceneCoordinateSpace:] : 324 -> 328
~ -[UIFocusMovementAction focusMovementInfo] : 80 -> 88
~ -[UIFocusMovementAction inputDeviceInfo] : 80 -> 88
~ -[UIFocusMovementAction shouldPerformHapticFeedback] : 84 -> 92
~ -[UIFocusMovementAction focusedFrame] : 116 -> 124
~ +[_UIFocusRegionEvaluator subregionFromRegion:withSnapshotFrame:inSnapshot:] : 364 -> 376
~ +[_UIFocusRegionEvaluator frameForRegion:inCoordinateSpace:] : 372 -> 380
~ +[_UIFocusRegionEvaluator _visibleSubregionsWhenRegion:occludedByRegion:inSnapshot:] : 1876 -> 1904
~ +[_UIFocusRegionEvaluator regionsByEvaluatingOcclusionsForRegions:inSnapshot:] : 316 -> 328
~ +[_UIFocusRegionEvaluator regionsByOccludingRegions:beneathRegions:inSnapshot:] : 400 -> 408
~ -[_UIFocusUpdateReport init] : 108 -> 112
~ -[_UIFocusUpdateReport initWithFocusSystem:] : 192 -> 196
~ -[_UIFocusUpdateReport shouldLog] : 268 -> 280
~ -[_UIFocusUpdateReport setContext:] : 12 -> 64
~ -[_UIFocusUpdateReportFormatter _componentsFromReport:] : 248 -> 260
~ -[_UIFocusUpdateReportFormatter stringFromReport:] : 204 -> 216
~ -[_UIFocusUpdateReportFormatter _headerForReport:] : 592 -> 640
~ -[_UIFocusUpdateReportFormatter _bodyForReport:] : 660 -> 696
~ -[_UIFocusUpdateThrottle initWithUpdateHandler:] : 212 -> 216
~ -[_UIFocusUpdateThrottle scheduleProgrammaticFocusUpdate] : 408 -> 416
~ -[_UIFocusUpdateThrottle didCreateProgrammaticFocusUpdateContext:] : 308 -> 316
~ __UIFocusItemIsFocused : 216 -> 232
~ __UIFocusItemIsFocusedOrFocusable : 232 -> 244
~ ___UIFocusItemIsFocusedOrFocusableInFocusSystem : 428 -> 444
~ __UIFocusItemIsFocusedOrFocusableInFocusSystem : 316 -> 328
~ __UIFocusItemIsFocusableInFocusSystem : 316 -> 328
~ __UIFocusItemCanBecomeFocused : 264 -> 272
~ __UIFocusItemIsFocusableInFocusSystemWithSearchInfo : 360 -> 368
~ __UIFocusItemIsTransparentFocusItem : 80 -> 84
~ __UIParentCoordinateSpaceForFocusItem : 352 -> 400
~ __UIFocusItemDeferralModeForItem : 80 -> 84
~ __UIFocusItemFocusSpeedBumpEdges : 80 -> 84
~ -[_UIFocusMapRect intersectsRegion:inSnapshot:] : 232 -> 244
~ -[_UIFocusMapRect intersectionWithRegion:inSnapshot:] : 400 -> 408
~ -[_UIFocusMapRect description] : 200 -> 208
~ -[_UIFocusPromiseRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 156 -> 172
~ -[_UIFocusPromiseRegion isEqual:] : 220 -> 200
~ -[_UIFocusPromiseRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:] : 668 -> 708
~ -[_UIFocusPromiseRegion _focusableBoundaries] : 52 -> 60
~ -[_UIFocusPromiseRegion _descriptionBuilder] : 128 -> 132
~ -[_UIFocusInputDeviceInfo encodeWithXPCDictionary:] : 108 -> 112
~ -[_UIFocusInputDeviceInfo encodeWithCoder:] : 96 -> 100
~ __UIFocusUserDefaults : 84 -> 100
~ __UIFocusPreferencesOnce : 84 -> 100
~ ____UIFocusPreferencesOnce_block_invoke : 84 -> 92
~ __UIFocusInternalPreferencesRevisionInit_block_invoke : 228 -> 248
~ _notificationHandler : 180 -> 188
~ __UIFocusInternalPreferenceSync : 120 -> 124
~ _SplitBracesAndComma : 732 -> 736
+ __UIFocusRectInset
~ -[NSCoder(UIFocusGeometryKeyedCoding) encodeCGRect:forKey:] : 148 -> 152
~ -[NSCoder(UIFocusGeometryKeyedCoding) decodeCGRectForKey:] : 472 -> 476
~ __UIFocusItemCompare : 772 -> 792
~ __UIFocusGetNextItemFromList : 396 -> 404
~ __UIFocusGroupCompare : 1624 -> 1708
~ __UIFocusGroupIdentifierForInstance : 240 -> 256
~ __UIFocusGroupUnresolvedIdentifierForEnvironment : 636 -> 660
~ __UIFocusGroupPriorityForItem : 152 -> 156
~ -[_UIFocusMapSnapshotter init] : 108 -> 112
~ -[_UIFocusMapSnapshotter initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:] : 492 -> 488
~ -[_UIFocusMapSnapshotter captureSnapshot] : 252 -> 256
~ -[_UIFocusMapSnapshotter setFocusedRegion:] : 12 -> 64
~ -[_UIFocusMapSnapshotter setSearchInfo:] : 12 -> 64
~ -[_UIFocusMapSnapshotter setMovementInfo:] : 12 -> 64
~ -[_UIFocusRegionContainerProxy initWithOwningEnvironment:itemContainer:] : 76 -> 80
~ -[_UIFocusRegionContainerProxy initWithEnvironmentContainer:] : 220 -> 216
~ -[_UIFocusRegionContainerProxy hash] : 56 -> 60
~ -[_UIFocusRegionContainerProxy description] : 372 -> 404
~ -[_UIFocusRegionContainerProxy preferredFocusEnvironments] : 76 -> 84
~ -[_UIFocusRegionContainerProxy shouldUpdateFocusInContext:] : 116 -> 120
~ -[_UIFocusRegionContainerProxy _didUpdateFocusInContext:] : 128 -> 136
~ -[_UIFocusRegionContainerProxy setNeedsFocusUpdate] : 104 -> 112
~ -[_UIFocusRegionContainerProxy updateFocusIfNeeded] : 64 -> 68
~ -[_UIFocusRegionContainerProxy parentFocusEnvironment] : 116 -> 128
~ -[_UIFocusRegionContainerProxy _clippingRectInCoordinateSpace:] : 160 -> 164
~ -[_UIFocusRegionContainerProxy _isEligibleForFocusInteraction] : 56 -> 60
~ -[_UIFocusRegionContainerProxy _isEligibleForFocusOcclusion] : 60 -> 64
~ -[_UIFocusRegionContainerProxy _preferredFocusRegionCoordinateSpace] : 144 -> 152
~ -[_UIFocusRegionContainerProxy _searchForFocusRegionsInContext:] : 188 -> 192
~ -[_UIFocusRegionContainerProxy setEnvironmentContainer:] : 12 -> 64
~ __UIFocusRegionContainerFromEnvironmentAndContainer : 192 -> 212
~ -[_UIFocusContainerGuideFallbackItemsContainer initWithParentEnvironment:childItems:] : 304 -> 312
~ -[_UIFocusContainerGuideFallbackItemsContainer coordinateSpace] : 100 -> 112
~ -[_UIFocusContainerGuideFallbackItemsContainer setNeedsFocusUpdate] : 92 -> 96
~ -[_UIFocusContainerGuideFallbackItemsContainer updateFocusIfNeeded] : 76 -> 80
~ -[_UIFocusGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 244 -> 256
~ -[_UIFocusGuideRegion isEqual:] : 340 -> 328
~ -[_UIFocusGuideRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:] : 532 -> 552
~ -[_UIFocusGuideRegion _focusedItemForLinearSorting:inMap:withSnapshot:] : 220 -> 224
~ -[_UIFocusGuideRegion _willParticipateAsDestinationRegionInFocusUpdate:] : 160 -> 168
~ -[_UIFocusGuideRegion _delegatePreferredFocusEnvironmentsForMovementRequest:] : 152 -> 172
~ -[_UIFocusLinearMovementCache nextItemForRequest:] : 264 -> 284
~ -[_UIFocusLinearMovementCache updateCacheWithContext:] : 344 -> 376
~ -[_UIFocusLinearMovementCache _updateParentEnvironmentIfNecessary] : 352 -> 356
~ -[_UIFocusLinearMovementCache environmentDidAppear:] : 600 -> 624
~ _logger : 84 -> 100
~ -[_UIHostedFocusSystemDelegateProxy respondsToSelector:] : 132 -> 140
~ -[_UIHostedFocusSystemDelegateProxy methodSignatureForSelector:] : 180 -> 196
~ -[_UIHostedFocusSystemDelegateProxy forwardingTargetForSelector:] : 144 -> 152
~ -[_UIHostedFocusSystemDelegateProxy _focusSystem:containsChildOfHostEnvironment:] : 104 -> 100
~ -[_UIHostedFocusSystemDelegateProxy _focusSystem:focusItemsInRect:] : 152 -> 156
~ -[_UIFocusTreeLock init] : 340 -> 344
~ -[_UIFocusTreeLock lockEnvironmentTree:] : 376 -> 384
~ -[_UIFocusTreeLock unlockEnvironmentTree:] : 420 -> 436
~ -[_UIFocusTreeLock isEnvironmentLocked:] : 432 -> 440
~ -[_UIFocusTreeLock _validateLockedEnvironments] : 264 -> 268
~ -[_UIFocusTreeLock description] : 120 -> 128
~ -[_UIFocusTreeLockItem initWithEnvironment:finalUnlockHandler:] : 496 -> 492
~ ___63-[_UIFocusTreeLockItem initWithEnvironment:finalUnlockHandler:]_block_invoke : 248 -> 252
~ -[_UIFocusTreeLockItem lock] : 248 -> 256
~ -[_UIFocusTreeLockItem unlock] : 452 -> 464
~ -[_UIFocusTreeLockItem _cleanup:] : 464 -> 488
~ -[_UIFocusTreeLockItem validate] : 472 -> 484
~ -[_UIFocusTreeLockItem description] : 448 -> 460
~ -[_UIFocusItemInfo copyWithZone:] : 4 -> 40
~ -[_UIFocusItemInfo ancestorEnvironmentScrollableContainers] : 104 -> 116
~ -[_UIFocusItemInfo inheritedFocusMovementStyle] : 108 -> 116
~ -[_UIFocusItemInfo focusTouchSensitivityStyle] : 112 -> 116
~ -[_UIFocusItemInfo rotaryFocusMovementAxis] : 88 -> 92
~ -[_UIFocusItemInfo isFocusMovementFlippedHorizontally] : 244 -> 248
~ ___54-[_UIFocusItemInfo isFocusMovementFlippedHorizontally]_block_invoke : 120 -> 128
~ -[_UIFocusItemInfo focusedRegion] : 96 -> 108
~ -[_UIFocusItemInfo _createFocusedRegion] : 1208 -> 1308
~ -[_UIFocusItemInfo focusedRectInCoordinateSpace:] : 164 -> 168
~ -[_UIFocusItemInfo description] : 136 -> 140
~ -[_UIFocusItemInfo shortDescription] : 324 -> 340
~ -[_UIFocusLinearMovementSequence initWithItems:loops:restrictEnteringSequence:] : 224 -> 228
~ -[_UIFocusSpeedBumpRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 104 -> 108
~ -[_UIFocusSpeedBumpRegion _boundariesBlockingFocusMovementRequest:] : 112 -> 116
~ -[_UIFocusItemRegion initWithFrame:coordinateSpace:item:focusSystem:] : 656 -> 664
~ -[_UIFocusItemRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 164 -> 168
~ -[_UIFocusItemRegion _descriptionBuilder] : 312 -> 328
~ -[_UIFocusItemRegion isEqual:] : 300 -> 280
~ -[_UIFocusItemRegion _canBeOccludedByRegionsAbove] : 76 -> 80
~ -[_UIFocusItemRegion _defaultFocusItem] : 80 -> 84
~ -[_UIFocusItemRegion _focusableBoundaries] : 112 -> 116
~ __UIFocusNearestAncestorEnvironmentScrollableContainer : 544 -> 568
~ __UIFocusItemContainerIsScrollableContainer : 88 -> 92
~ __UIFocusAncestorEnvironmentScrollableContainers : 188 -> 196
~ __UIFocusItemContainerAddChildItemsInContextWithOptions : 2008 -> 2128
~ __UIFocusItemContainerSupportsInvalidatingFocusCache : 88 -> 92
~ __UIFocusItemScrollableContainerCanScrollX : 112 -> 116
~ __UIFocusItemScrollableContainerCanScrollY : 112 -> 116
~ __UIFocusItemScrollableContainerContentBounds : 148 -> 152
~ __UIFocusItemScrollableContainerPrimaryAxis : 212 -> 216
~ __UIFocusEngineCommonEnvironmentScrollableContainerForItems : 336 -> 348
~ ____UIFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke : 212 -> 216
~ ____UIFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke_2 : 80 -> 88
~ __UIFocusEngineScrollableContainerCanScroll : 112 -> 116
~ __UIFocusEngineFirstScrollableContainerTupleThatScrollsForItem : 312 -> 324
~ -[_UIFocusEnvironmentContainerTuple initWithOwningEnvironment:itemContainer:] : 428 -> 436
~ +[_UIFocusEnvironmentContainerTuple tupleWithOwningEnvironment:itemContainer:] : 112 -> 108
~ +[_UIFocusEnvironmentContainerTuple tupleWithRequiredContainerFromEnvironment:] : 112 -> 124
~ -[_UIFocusEnvironmentContainerTuple isEqualToEnvironmentContainerTuple:] : 632 -> 668
~ -[_UIFocusEnvironmentContainerTuple hash] : 96 -> 104
~ -[_UIFocusEnvironmentContainerTuple description] : 132 -> 140
~ -[_UIFocusEnvironmentScrollableContainerTuple initWithOwningEnvironment:scrollableContainer:] : 416 -> 424
~ +[_UIFocusEnvironmentScrollableContainerTuple tupleWithOwningEnvironment:scrollableContainer:] : 112 -> 108
~ -[_UIFocusEnvironmentScrollableContainerTuple isEqual:] : 844 -> 900
~ -[_UIFocusEnvironmentScrollableContainerTuple hash] : 96 -> 104
~ -[_UIFocusEnvironmentScrollableContainerTuple description] : 132 -> 140
~ -[UIFocusSystem init] : 108 -> 112
~ -[UIFocusSystem initWithFocusBehavior:enabled:] : 256 -> 240
~ -[UIFocusSystem _setEnabled:] : 1008 -> 1076
~ -[UIFocusSystem _enableWithoutFocusRestoration] : 116 -> 120
~ -[UIFocusSystem focusedItem] : 148 -> 152
~ -[UIFocusSystem _focusedItemOrDeferralTarget] : 92 -> 100
~ -[UIFocusSystem _focusItemForValidation] : 104 -> 120
~ -[UIFocusSystem _hasValidItemForCurrentDeferralState] : 96 -> 104
~ -[UIFocusSystem _focusGroupHistory] : 84 -> 92
~ -[UIFocusSystem _prefersDeferralForFocusUpdateInContext:] : 368 -> 388
~ -[UIFocusSystem _configureFocusDeferralIfNecessaryForContext:report:] : 688 -> 732
~ -[UIFocusSystem _performDeferredFocusUpdateIfAvailable] : 380 -> 396
~ -[UIFocusSystem _tickHasSeenFocusedItemTimer:] : 564 -> 584
~ -[UIFocusSystem _resetFocusDeferral] : 388 -> 408
~ -[UIFocusSystem _setDeferredFocusUpdateTarget:] : 148 -> 156
~ -[UIFocusSystem _effectiveFocusDeferralBehavior] : 108 -> 116
~ -[UIFocusSystem _setOverrideFocusDeferralBehavior:] : 160 -> 172
~ +[UIFocusSystem _allFocusSystems] : 80 -> 96
~ -[UIFocusSystem _focusMapContainer] : 152 -> 156
~ -[UIFocusSystem focusItemContainer] : 116 -> 120
~ -[UIFocusSystem _clippingRectInCoordinateSpace:] : 160 -> 164
~ -[UIFocusSystem preferredFocusEnvironments] : 196 -> 220
~ +[UIFocusSystem environment:containsEnvironment:] : 260 -> 264
~ -[UIFocusSystem requestFocusUpdateToEnvironment:] : 196 -> 208
~ -[UIFocusSystem _requestFocusUpdate:] : 1372 -> 1396
~ -[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:] : 1216 -> 1248
~ ___69-[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:]_block_invoke : 368 -> 372
~ -[UIFocusSystem _focusEnvironmentDidBecomeVisible:] : 148 -> 152
~ -[UIFocusSystem _focusEnvironmentDidAppear:] : 816 -> 852
~ -[UIFocusSystem _validatedAppearingFocusEnvironmentRequest] : 604 -> 632
~ -[UIFocusSystem _validatedPendingFocusUpdateRequest] : 480 -> 484
~ -[UIFocusSystem _topEnvironment] : 184 -> 188
~ -[UIFocusSystem _isEnvironmentEligibleForFocusUpdate:fallbackToEnvironment:debugReport:] : 544 -> 564
~ -[UIFocusSystem _updateWantsTreeLocking] : 176 -> 180
~ -[UIFocusSystem _isEnvironmentLocked:] : 104 -> 108
~ -[UIFocusSystem _lockEnvironment:] : 104 -> 108
~ -[UIFocusSystem _unlockEnvironment:] : 116 -> 120
~ -[UIFocusSystem updateFocusIfNeeded] : 2096 -> 2224
~ -[UIFocusSystem _updateFocusWithContext:report:] : 1200 -> 1272
~ -[UIFocusSystem _notifyEnvironment:didUpdateFocusInContext:] : 172 -> 176
~ ___60-[UIFocusSystem _sendWillUpdateFocusNotificationsInContext:]_block_invoke : 96 -> 104
~ -[UIFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:] : 600 -> 624
~ -[UIFocusSystem _disappearingFocusEnvironment] : 8 -> 56
~ -[UIFocusSystem _updateFocusImmediatelyWithContext:] : 292 -> 308
~ -[UIFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:] : 688 -> 720
~ -[UIFocusSystem _contextForUpdateToEnvironment:allowsOverridingPreferedFocusEnvironments:allowsDeferral:] : 176 -> 180
~ -[UIFocusSystem _performFocusMovement:] : 88 -> 92
~ -[UIFocusSystem _closestFocusableItemToPoint:inEnvironment:constrainedToRect:distanceMeasuringUnitPoint:itemFilter:] : 416 -> 432
~ -[UIFocusSystem invalidateFocusItemContainer:] : 96 -> 100
~ -[UIFocusSystem _deepestPreferredFocusableItemCacheForCurrentUpdate] : 132 -> 144
~ -[UIFocusSystem _buildFocusItemAncestorCacheIfNecessary] : 232 -> 244
~ -[UIFocusSystem _focusedItemIsContainedInEnvironment:includeSelf:] : 320 -> 324
~ -[UIFocusSystem _reevaluateLockedEnvironments] : 272 -> 276
~ -[UIFocusSystem _deepestPreferredFocusEnvironment] : 172 -> 184
~ -[UIFocusSystem _shouldReverseLayoutDirectionForEnvironment:] : 108 -> 112
~ -[UIFocusSystem _shouldReverseLinearWrappingForEnvironment:] : 108 -> 112
~ -[UIFocusSystem _uiktest_updateFocusToItem:] : 72 -> 76
~ -[UIFocusSystem _uiktest_disableFocusDeferral] : 116 -> 120
~ -[UIFocusSystem setDelegate:] : 856 -> 860
~ -[UIFocusSystem _shouldRestoreFocusInContext:] : 236 -> 248
~ -[UIFocusSystem _didFinishUpdatingFocusInContext:] : 252 -> 276
~ -[UIFocusSystem _isScrollingScrollableContainer:targetContentOffset:] : 124 -> 128
~ -[UIFocusSystem _handleFailedFocusMovementRequest:withPerformer:] : 108 -> 112
~ -[UIFocusSystem setBehavior:] : 108 -> 120
~ -[UIFocusSystem _updateFocusUpdateThrottle] : 372 -> 380
~ -[UIFocusSystem description] : 588 -> 604
~ -[UIFocusSystem setPendingFocusMovementAction:] : 12 -> 64
~ -[UIFocusSystem _setFocusMovementCache:] : 12 -> 64
~ ____UIFocusSystemRegister_block_invoke : 68 -> 72
~ -[_UIFocusGroupMap initWithItems:standInItemsMap:coordinateSpace:] : 448 -> 464
~ -[_UIFocusGroupMap copyWithZone:] : 488 -> 552
~ -[_UIFocusGroupMap _indexItems:] : 484 -> 512
~ -[_UIFocusGroupMap _indexEnvironment:] : 764 -> 804
~ -[_UIFocusGroupMap focusGroups] : 112 -> 120
~ ___addChildFocusGroupsRecursively : 288 -> 292
~ -[_UIFocusGroupMap focusItems] : 380 -> 396
~ -[_UIFocusGroupMap focusGroupForItem:] : 180 -> 188
~ -[_UIFocusGroupMap description] : 148 -> 160
~ -[_UIDynamicFocusGroupMap init] : 120 -> 124
~ -[_UIDynamicFocusGroupMap focusGroupIdentifierForItem:] : 136 -> 148
~ __UIHostedFocusSystemsForHostEnvironment : 208 -> 220
~ -[_UIHostedFocusSystem _initWithHostEnvironment:] : 584 -> 612
~ -[_UIHostedFocusSystem delegate] : 76 -> 80
~ -[_UIHostedFocusSystem setDelegate:] : 180 -> 188
~ -[_UIHostedFocusSystem containsChildOfHostEnvironment:] : 212 -> 224
~ -[_UIHostedFocusSystem behavior] : 148 -> 164
~ -[_UIHostedFocusSystem _hostFocusSystem] : 140 -> 144
~ -[_UIHostedFocusSystem _focusSystemIsValid] : 112 -> 116
~ -[_UIHostedFocusSystem setDelegateProxy:] : 20 -> 80
~ -[_UIHostedFocusSystemItemContainer coordinateSpace] : 116 -> 132
~ -[_UIHostedFocusSystemItemContainer focusItemsInRect:] : 188 -> 204
~ ____UIHostedFocusSystemRegister_block_invoke : 72 -> 76
~ -[_UIFocusPromiseItem initWithParentEnvironment:frame:fullfillmentHandler:] : 456 -> 464
~ -[_UIFocusPromiseItem description] : 236 -> 252
~ -[_UIFocusPromiseItem fulfilledItem] : 132 -> 148
~ -[_UIFocusPromiseItem setNeedsFocusUpdate] : 92 -> 96
~ -[_UIFocusPromiseItem updateFocusIfNeeded] : 76 -> 80
~ -[_UIFocusPromiseItem focusItemsInRect:] : 164 -> 172
~ -[_UIFocusPromiseItem coordinateSpace] : 100 -> 112
~ -[_UIFocusContainerGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:] : 168 -> 180
~ -[_UIFocusContainerGuideRegion isEqual:] : 316 -> 296
~ -[_UIFocusContainerGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:] : 540 -> 568
~ -[_UIFocusContainerGuideRegion setFallbackRootRegionContainer:] : 20 -> 80
~ -[_UIFocusContainerGuideRegion setContentFocusRegionContainer:] : 20 -> 80
~ -[_UIFocusSearchInfo shouldIncludeFocusItem:] : 128 -> 136
CStrings:
- "result"

```
