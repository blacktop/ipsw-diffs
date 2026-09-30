## FocusEngine

> `/System/Library/PrivateFrameworks/FocusEngine.framework/Versions/A/FocusEngine`

```diff

-8306.1.401.0.0
-  __TEXT.__text: 0x32284
+8444.1.402.0.0
+  __TEXT.__text: 0x321a8
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x3458
+  __TEXT.__objc_methlist: 0x398c
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0x3d18
   __TEXT.__ustring: 0x374
-  __TEXT.__gcc_except_tab: 0x6b8
+  __TEXT.__gcc_except_tab: 0x6ac
   __TEXT.__oslogstring: 0x1277
   __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0xe18
+  __TEXT.__unwind_info: 0xe10
   __TEXT.__objc_classname: 0x895
   __TEXT.__objc_methname: 0xa682
   __TEXT.__objc_methtype: 0x19e7

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e68
+  __DATA_CONST.__objc_selrefs: 0x1f08
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x318
   __AUTH_CONST.__cfstring: 0x2a40
-  __AUTH_CONST.__objc_const: 0x7a48
+  __AUTH_CONST.__objc_const: 0x70d0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1590

   __DATA.__data: 0x6c8
   __DATA.__FEkit_ip: 0x20
   __DATA.__FE_ipl: 0x0
-  __DATA.__bss: 0xb0
   __DATA.__common: 0x38
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A35C39F3-854B-3DB7-9B3B-BB78CCACDF6B
-  Functions: 1246
+  UUID: E25E02B0-26F4-37EC-A21E-6F22903470C1
+  Functions: 1244
   Symbols:   3306
   CStrings:  2576
 
Functions:
~ +[_FEDebugLogMessage messageWithStyle:string:] : 292 -> 288
- sub_22fa6f620
~ -[_FEFocusStateObserver notifyObserversIfNecessary] : 304 -> 300
~ -[_FEFocusStateObserver descriptionBuilder] : 200 -> 192
~ -[_FEFocusSystem focusedItem] : 180 -> 168
~ -[_FEFocusSystem _prefersDeferralForFocusUpdateInContext:] : 372 -> 368
- sub_22fa711dc
~ -[_FEFocusSystem _tickHasSeenFocusedItemTimer:] : 580 -> 564
~ -[_FEFocusSystem _startDeferringFocusIfSupported] : 236 -> 232
~ -[_FEFocusSystem _setDeferredFocusUpdateTarget:] : 160 -> 148
~ -[_FEFocusSystem _focusItemContainer] : 128 -> 116
~ -[_FEFocusSystem _requestFocusUpdate:] : 1492 -> 1488
~ -[_FEFocusSystem _focusEnvironmentDidAppear:] : 816 -> 812
~ -[_FEFocusSystem _isEnvironmentEligibleForFocusUpdate:fallbackToEnvironment:debugReport:] : 540 -> 544
~ -[_FEFocusSystem updateFocusIfNeeded] : 2040 -> 2044
~ -[_FEFocusSystem _updateFocusWithContext:report:] : 1356 -> 1352
~ ___105-[_FEFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]_block_invoke : 104 -> 108
~ -[_FEFocusSystem _reevaluateLockedEnvironments] : 380 -> 376
~ -[_FEFocusSystem _deepestPreferredFocusEnvironment] : 176 -> 172
~ -[_FEFocusSystem setDelegate:] : 868 -> 856
~ -[_FEFocusSystem _updateFocusUpdateThrottle] : 376 -> 372
~ -[_FEFocusSystem description] : 580 -> 572
~ __FEFocusGroupCompare : 1632 -> 1624
~ __FEFocusGroupUnresolvedIdentifierForEnvironment : 644 -> 636
~ __FEFocusNearestAncestorEnvironmentScrollableContainer : 528 -> 544
~ __FEFocusItemContainerAddChildItemsInContextWithOptions : 2016 -> 2008
~ -[_FEFocusEnvironmentScrollableContainerTuple isEqual:] : 840 -> 844
~ __FEGetFocusCastingVisualization : 216 -> 212
~ -[_FEFocusItemRegion initWithFrame:coordinateSpace:item:focusSystem:] : 644 -> 656
~ -[_FEFocusItemRegion _defaultFocusItem] : 68 -> 80
~ -[_FEFocusItemRegion _focusableBoundaries] : 76 -> 80
~ __FEFocusEnvironmentIsAncestorOfEnvironment : 260 -> 252
~ __FEFocusEnvironmentEnumerateAncestorEnvironments : 228 -> 248
~ __FEFocusEnvironmentResolvedRotaryFocusMovementAxis : 708 -> 688
~ -[_FEFocusMapSnapshotter captureSnapshot] : 248 -> 252
~ -[_FEFocusEnvironmentPreferenceEnumerationContext pushEnvironment:] : 512 -> 516
~ -[_FEFocusEnvironmentPreferenceEnumerationContext popEnvironment] : 248 -> 244
~ -[_FEFocusEnvironmentPreferenceEnumerator _shouldInferDefaultPreferenceForEnvironmentInContext:] : 136 -> 140
~ -[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:] : 1160 -> 1168
~ ___96-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:]_block_invoke_3 : 892 -> 896
~ ___125-[_UIDeepestPreferredEnvironmentSearch _overridingPreferredFocusEnvironmentForPreferredEnvironment:visitedFocusEnvironments:]_block_invoke : 208 -> 216
~ -[_UIDeepestPreferredEnvironmentSearch _reportFinishedEvaluatingAllPreferencesForEnvironmentInContext:result:] : 504 -> 508
~ -[_FEFocusUpdateThrottle teardown] : 248 -> 236
~ -[_FEFocusUpdateThrottle scheduleProgrammaticFocusUpdate] : 480 -> 476
~ -[_FEFocusUpdateThrottle _performScheduledUpdate] : 104 -> 100
~ -[_FEFocusMapSnapshot addRegionsInContainer:] : 3012 -> 3020
~ _____UIFocusMapRecurseSearchForFocusSystemInEligibleContainer_block_invoke : 316 -> 324
~ -[_FEFocusGroup _validatePrimaryRectIfNeccessary] : 432 -> 412
~ __FEFocusRegionSearchContextSearchForFocusRegionsInEnvironment : 696 -> 740
~ ___recursePreOrderDepthFirstTraversal : 516 -> 496
~ -[_FEFocusMap _inferredDefaultFocusItemInEnvironment:] : 1760 -> 1744
~ __FEFocusMapDistanceToRegionBoundary : 828 -> 824
~ -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:] : 1068 -> 1064
~ -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:] : 1292 -> 1284
~ -[_FEFocusMap _nextFocusedItemForNonLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:] : 3576 -> 3492
~ -[_FEFocusMap _closestFocusableItemToPoint:inRect:excludingItems:distanceMeasuringUnitPoint:] : 1020 -> 1016
~ -[_FEFocusMap _beginTrackingSearches] : 120 -> 124
~ -[_FEFocusMap _stopTrackingSearches] : 148 -> 152
~ -[_FEFocusMap _beginTrackingDefaultItemSearchInfoIfNecessary] : 76 -> 88
~ -[_FEFocusMap _beginTrackingFocusMovementSearchInfoIfNecessary] : 76 -> 88
~ -[_FEFocusMap diagnoseFocusabilityForItem:report:] : 1216 -> 1232
~ -[_FEFocusGroupMap focusItems] : 376 -> 380
~ -[_FEFocusUpdateRequest canMergeWithRequest:] : 332 -> 328
~ -[_FEFocusUpdateRequest requestByMergingWithRequest:] : 544 -> 548
~ -[_FEFocusMovementHint interactionTransform] : 444 -> 412
~ -[_FEFocusUpdateContext _validate] : 1076 -> 1072
~ -[_FEFocusUpdateContext _setSourceItemInfo:] : 76 -> 80
~ -[_FEFocusUpdateContext _setInitialDestinationEnvironment:] : 132 -> 120
~ -[_FEFocusUpdateContext _updateDestinationItemIfNeeded] : 400 -> 380
~ -[_FEFocusUpdateContext _setFocusedGuide:] : 152 -> 140
~ -[_FEFocusRegionDebugDrawingConfiguration initWithRegion:baseHue:patternAlpha:dashedStroke:] : 204 -> 200
~ -[_FEFocusMovementInfo _isLinearMovement] : 52 -> 56
~ -[_FEFocusMovementPerformer performFocusMovement:] : 700 -> 708
~ ___98-[_FEFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke : 256 -> 288
~ -[_FEFocusMovementPerformer _bestCandidateForLinearFocusMovement:] : 348 -> 336
~ -[_FEFocusMovementPerformer _nextLinearCandidateLoadingScrollableContentForRequest:] : 1864 -> 1884
~ __FEFocusRectCompare : 396 -> 388
~ -[_FETreeLock init] : 344 -> 340
~ -[_FETreeLock lockEnvironmentTree:] : 380 -> 376
~ -[_FETreeLock isEnvironmentLocked:] : 428 -> 432
~ __FEGetFocusTreeLockVerboseLogging : 216 -> 212
~ -[_FETreeLockItem description] : 412 -> 416
~ -[_FEFocusItemFrameReporter _reportFocusFrameForCurrentlyFocusedItem] : 124 -> 112
~ -[_FEFocusItemFrameReporter _scheduleRepeatingFrameUpdate] : 324 -> 320
~ -[_FEFocusItemFrameReporter _rect:differsFromRect:lowerThreshold:upperThreshold:] : 260 -> 264

```
