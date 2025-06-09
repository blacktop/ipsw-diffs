## FocusEngine

> `/System/Library/PrivateFrameworks/FocusEngine.framework/FocusEngine`

```diff

-8506.1.101.0.0
-  __TEXT.__text: 0x3216c
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x398c
-  __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x3d18
-  __TEXT.__ustring: 0x374
-  __TEXT.__gcc_except_tab: 0x5f0
-  __TEXT.__oslogstring: 0x1277
-  __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__unwind_info: 0xe00
-  __TEXT.__objc_classname: 0x895
-  __TEXT.__objc_methname: 0xa682
-  __TEXT.__objc_methtype: 0x19e7
-  __TEXT.__objc_stubs: 0x6780
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__objc_classlist: 0x228
+9071.1.107.0.0
+  __TEXT.__text: 0x2f970
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x3a38
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x4556
+  __TEXT.__gcc_except_tab: 0x56c
+  __TEXT.__oslogstring: 0xcd7
+  __TEXT.__ustring: 0x35c
+  __TEXT.__unwind_info: 0xd10
+  __TEXT.__objc_classname: 0x8c1
+  __TEXT.__objc_methname: 0x9e20
+  __TEXT.__objc_methtype: 0x1ce7
+  __TEXT.__objc_stubs: 0x60c0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f08
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x2a40
-  __AUTH_CONST.__objc_const: 0x70d0
+  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0x258
+  __AUTH_CONST.__cfstring: 0x29a0
+  __AUTH_CONST.__objc_const: 0x71d8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__data: 0x6c8
-  __DATA.__FEkit_ip: 0x20
-  __DATA.__FE_ipl: 0x0
-  __DATA.__common: 0x38
-  __DATA.__bss: 0xb0
+  __AUTH.__objc_data: 0x1450
+  __DATA.__objc_ivar: 0x480
+  __DATA.__UIFocuskit_ip: 0x20
+  __DATA.__data: 0x840
+  __DATA.__UIFocus_ipl: 0x0
+  __DATA.__bss: 0x58
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/SubFrameworks/UIUtilities.framework/UIUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CD7119A-7840-3641-8C12-B9307468D4E4
-  Functions: 1244
-  Symbols:   4540
-  CStrings:  2576
+  UUID: E5163631-759B-376E-9E91-DB947045467C
+  Functions: 1208
+  Symbols:   4356
+  CStrings:  2482
 
Symbols:
+ +[UIFocusDebugger _ancestryForEnvironment:]
+ +[UIFocusDebugger _statusForFocusSystem:includeDeferralTarget:]
+ +[UIFocusDebugger _verboseStatus]
+ +[UIFocusDebugger checkFocusGroupTreeForEnvironment:]
+ +[UIFocusDebugger checkFocusabilityForItem:]
+ +[UIFocusDebugger focusGroupsForEnvironment:]
+ +[UIFocusDebugger help]
+ +[UIFocusDebugger preferredFocusEnvironmentsForEnvironment:]
+ +[UIFocusDebugger simulateFocusUpdateRequestFromEnvironment:]
+ +[UIFocusDebugger status]
+ +[UIFocusSystem _allFocusSystems]
+ +[UIFocusSystem _focusSystemForEnvironment:]
+ +[UIFocusSystem environment:containsEnvironment:]
+ +[UIFocusSystem focusSystemForEnvironment:]
+ +[UIFocusUpdateContext _defaultValidationReportFormatter]
+ +[_UIDebugIssue issueWithDescription:]
+ +[_UIDebugIssue issueWithFormat:]
+ +[_UIDebugReportFormatter defaultFormatter]
+ +[_UIFocusDebuggerStringOutput outputWithString:]
+ +[_UIFocusEnvironmentContainerTuple tupleWithOwningEnvironment:itemContainer:]
+ +[_UIFocusEnvironmentContainerTuple tupleWithRequiredContainerFromEnvironment:]
+ +[_UIFocusEnvironmentScrollableContainerTuple tupleWithOwningEnvironment:scrollableContainer:]
+ +[_UIFocusGroup nullGroupWithCoordinateSpace:]
+ +[_UIFocusInputDeviceInfo infoWithSenderID:]
+ +[_UIFocusInputDeviceInfo supportsSecureCoding]
+ +[_UIFocusItemInfo infoWithItem:]
+ +[_UIFocusItemInfo infoWithItem:useFallbackAncestorScroller:]
+ +[_UIFocusLinearMovementSequence sequenceWithItems:loops:]
+ +[_UIFocusLinearMovementSequence sequenceWithItems:loops:restrictEnteringSequence:]
+ +[_UIFocusMovementInfo _movementWithHeading:isInitial:fallbackMovementOriginatingFrame:]
+ +[_UIFocusMovementInfo supportsSecureCoding]
+ +[_UIFocusRegionEvaluator __regionsByEvaluatingOcclusionsForBaseRegions:occludingRegions:baseRegionsCanOccludeEachOther:inSnapshot:]
+ +[_UIFocusRegionEvaluator _visibleSubregionsWhenRegion:occludedByRegion:inSnapshot:]
+ +[_UIFocusRegionEvaluator frameForRegion:inCoordinateSpace:]
+ +[_UIFocusRegionEvaluator regionsByEvaluatingOcclusionsForRegions:inSnapshot:]
+ +[_UIFocusRegionEvaluator regionsByOccludingRegions:beneathRegions:inSnapshot:]
+ +[_UIFocusRegionEvaluator subregionFromRegion:withSnapshotFrame:inSnapshot:]
+ +[_UIFocusRegionMovementInfo _movementWithHeading:linearHeading:originatingHeading:isInitial:inputType:]
+ +[_UIFocusRegionSearchContextState stateWithRegionContainer:focusSystem:clippingRect:]
+ +[_UIFocusSearchInfo defaultInfo]
+ +[_UIFocusUpdateRequest requestForRemovingFocusInFocusSystem:]
+ -[NSCoder(UIFocusGeometryKeyedCoding) decodeCGRectForKey:]
+ -[NSCoder(UIFocusGeometryKeyedCoding) encodeCGRect:forKey:]
+ -[NSObject(_UIFocusRegionContainerProxy) _ui_isUIFocusRegionContainerProxy]
+ -[UIFocusMovementAction focusMovementInfo]
+ -[UIFocusMovementAction focusedFrame]
+ -[UIFocusMovementAction initWithFocusMovementInfo:]
+ -[UIFocusMovementAction initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:]
+ -[UIFocusMovementAction initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:focusedFrameInSceneCoordinateSpace:]
+ -[UIFocusMovementAction inputDeviceInfo]
+ -[UIFocusMovementAction shouldPerformHapticFeedback]
+ -[UIFocusMovementHint copyWithZone:]
+ -[UIFocusMovementHint initWithMovementDirection:itemSize:]
+ -[UIFocusMovementHint interactionTransform]
+ -[UIFocusMovementHint movementDirection]
+ -[UIFocusMovementHint perspectiveTransform]
+ -[UIFocusMovementHint rotationAmount]
+ -[UIFocusMovementHint rotation]
+ -[UIFocusMovementHint setRotationAmount:]
+ -[UIFocusMovementHint setTranslationAmount:]
+ -[UIFocusMovementHint translationAmount]
+ -[UIFocusMovementHint translation]
+ -[UIFocusSystem .cxx_destruct]
+ -[UIFocusSystem _buildFocusItemAncestorCacheIfNecessary]
+ -[UIFocusSystem _cancelPendingFocusRestoration]
+ -[UIFocusSystem _clearDeferredFocusUpdateTarget]
+ -[UIFocusSystem _clearFocusItemAncestorCache]
+ -[UIFocusSystem _clippingRectInCoordinateSpace:]
+ -[UIFocusSystem _closestFocusableItemToPoint:inEnvironment:constrainedToRect:distanceMeasuringUnitPoint:itemFilter:]
+ -[UIFocusSystem _configureFocusDeferralIfNecessaryForContext:report:]
+ -[UIFocusSystem _contextForUpdateToEnvironment:]
+ -[UIFocusSystem _contextForUpdateToEnvironment:allowsOverridingPreferedFocusEnvironments:allowsDeferral:]
+ -[UIFocusSystem _debug_isEnvironmentEligibleForFocusUpdate:debugReport:]
+ -[UIFocusSystem _deepestPreferredFocusEnvironment]
+ -[UIFocusSystem _deepestPreferredFocusableItemCacheForCurrentUpdate]
+ -[UIFocusSystem _didFinishUpdatingFocusInContext:]
+ -[UIFocusSystem _disappearingFocusEnvironment]
+ -[UIFocusSystem _dropFocusAndStartDeferring:suppressUpdate:]
+ -[UIFocusSystem _effectiveFocusDeferralBehavior]
+ -[UIFocusSystem _enableWithoutFocusRestoration]
+ -[UIFocusSystem _focusBehaviorDidChange]
+ -[UIFocusSystem _focusCasting]
+ -[UIFocusSystem _focusEnvironmentDidAppear:]
+ -[UIFocusSystem _focusEnvironmentDidBecomeVisible:]
+ -[UIFocusSystem _focusEnvironmentWillBecomeInvisible:]
+ -[UIFocusSystem _focusEnvironmentWillDisappear:]
+ -[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:]
+ -[UIFocusSystem _focusGroupHistory]
+ -[UIFocusSystem _focusItemForValidation]
+ -[UIFocusSystem _focusMapContainer]
+ -[UIFocusSystem _focusMovementCache]
+ -[UIFocusSystem _focusSystemIsValid]
+ -[UIFocusSystem _focusedItemIsContainedInEnvironment:includeSelf:]
+ -[UIFocusSystem _focusedItemOrDeferralTarget]
+ -[UIFocusSystem _handleFailedFocusMovementRequest:withPerformer:]
+ -[UIFocusSystem _handleFocusMovementAction:]
+ -[UIFocusSystem _hasSeenFocusedItemDidExpire]
+ -[UIFocusSystem _hasValidItemForCurrentDeferralState]
+ -[UIFocusSystem _hostFocusSystem]
+ -[UIFocusSystem _isEligibleForFocusInteraction]
+ -[UIFocusSystem _isEligibleForFocusOcclusion]
+ -[UIFocusSystem _isEnabled]
+ -[UIFocusSystem _isEnvironmentEligibleForFocusUpdate:fallbackToEnvironment:debugReport:]
+ -[UIFocusSystem _isEnvironmentLocked:]
+ -[UIFocusSystem _isScrollingScrollableContainer:targetContentOffset:]
+ -[UIFocusSystem _lockEnvironment:]
+ -[UIFocusSystem _movementPerformer]
+ -[UIFocusSystem _notifyEnvironment:didUpdateFocusInContext:]
+ -[UIFocusSystem _overrideFocusDeferralBehavior]
+ -[UIFocusSystem _performDeferredFocusUpdateIfAvailable]
+ -[UIFocusSystem _performFocusMovement:]
+ -[UIFocusSystem _performWithoutFocusUpdates:]
+ -[UIFocusSystem _postsFocusUpdateNotifications]
+ -[UIFocusSystem _prefersDeferralForFocusUpdateInContext:]
+ -[UIFocusSystem _prefersFocusContainment]
+ -[UIFocusSystem _prepareForTeardown]
+ -[UIFocusSystem _previousFocusedItem]
+ -[UIFocusSystem _reevaluateLockedEnvironments]
+ -[UIFocusSystem _requestFocusUpdate:]
+ -[UIFocusSystem _resetFocusDeferral]
+ -[UIFocusSystem _sendDidUpdateFocusNotificationsInContext:]
+ -[UIFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]
+ -[UIFocusSystem _sendWillUpdateFocusNotificationsInContext:]
+ -[UIFocusSystem _setDeferredFocusUpdateTarget:]
+ -[UIFocusSystem _setEnabled:]
+ -[UIFocusSystem _setFocusCasting:]
+ -[UIFocusSystem _setFocusMovementCache:]
+ -[UIFocusSystem _setNeedsFocusRestoration]
+ -[UIFocusSystem _setOverrideFocusDeferralBehavior:]
+ -[UIFocusSystem _shouldRestoreFocusInContext:]
+ -[UIFocusSystem _shouldReverseLayoutDirectionForEnvironment:]
+ -[UIFocusSystem _shouldReverseLinearWrappingForEnvironment:]
+ -[UIFocusSystem _simulatedNonDeferredProgrammaticFocusUpdateToEnvironment:]
+ -[UIFocusSystem _startDeferringFocusIfSupported]
+ -[UIFocusSystem _tickHasSeenFocusedItemTimer:]
+ -[UIFocusSystem _topEnvironment]
+ -[UIFocusSystem _uiktest_disableFocusDeferral]
+ -[UIFocusSystem _uiktest_disableThrottle]
+ -[UIFocusSystem _uiktest_setPreviousFocusedItem:]
+ -[UIFocusSystem _uiktest_updateFocusToItem:]
+ -[UIFocusSystem _unlockEnvironment:]
+ -[UIFocusSystem _updateFocusImmediatelyToEnvironment:]
+ -[UIFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]
+ -[UIFocusSystem _updateFocusImmediatelyWithContext:]
+ -[UIFocusSystem _updateFocusUpdateThrottle]
+ -[UIFocusSystem _updateFocusWithContext:report:]
+ -[UIFocusSystem _updateWantsTreeLocking]
+ -[UIFocusSystem _validatedAppearingFocusEnvironmentRequest]
+ -[UIFocusSystem _validatedPendingFocusUpdateRequest]
+ -[UIFocusSystem behavior]
+ -[UIFocusSystem delegate]
+ -[UIFocusSystem description]
+ -[UIFocusSystem didUpdateFocusInContext:]
+ -[UIFocusSystem focusItemContainer]
+ -[UIFocusSystem focusedItem]
+ -[UIFocusSystem initWithFocusBehavior:]
+ -[UIFocusSystem initWithFocusBehavior:enabled:]
+ -[UIFocusSystem init]
+ -[UIFocusSystem invalidateFocusItemContainer:]
+ -[UIFocusSystem parentFocusEnvironment]
+ -[UIFocusSystem pendingFocusMovementAction]
+ -[UIFocusSystem preferredFocusEnvironments]
+ -[UIFocusSystem requestFocusUpdateToEnvironment:]
+ -[UIFocusSystem setBehavior:]
+ -[UIFocusSystem setDelegate:]
+ -[UIFocusSystem setNeedsFocusUpdate]
+ -[UIFocusSystem setPendingFocusMovementAction:]
+ -[UIFocusSystem setWaitingForFocusMovementAction:]
+ -[UIFocusSystem shouldUpdateFocusInContext:]
+ -[UIFocusSystem treeLock]
+ -[UIFocusSystem updateFocusIfNeeded]
+ -[UIFocusSystem updateThrottle]
+ -[UIFocusSystem waitingForFocusMovementAction]
+ -[UIFocusUpdateContext .cxx_destruct]
+ -[UIFocusUpdateContext _cacheFocusBehavior]
+ -[UIFocusUpdateContext _commonAncestorEnvironment]
+ -[UIFocusUpdateContext _commonEnvironmentScrollableContainer]
+ -[UIFocusUpdateContext _destinationItemInfo]
+ -[UIFocusUpdateContext _destinationViewDistanceOffscreen]
+ -[UIFocusUpdateContext _didUpdateFocus]
+ -[UIFocusUpdateContext _focusGroupMap]
+ -[UIFocusUpdateContext _focusMapSearchInfo]
+ -[UIFocusUpdateContext _focusMovement]
+ -[UIFocusUpdateContext _focusRedirectedByGuide]
+ -[UIFocusUpdateContext _focusVelocity]
+ -[UIFocusUpdateContext _focusedGuideImpl]
+ -[UIFocusUpdateContext _focusedGuide]
+ -[UIFocusUpdateContext _groupFilter]
+ -[UIFocusUpdateContext _initWithContext:]
+ -[UIFocusUpdateContext _initWithFocusMovementRequest:nextFocusedItem:]
+ -[UIFocusUpdateContext _initWithFocusUpdateRequest:]
+ -[UIFocusUpdateContext _initialDestinationEnvironment]
+ -[UIFocusUpdateContext _isDeferredUpdate]
+ -[UIFocusUpdateContext _isFilteredToGroup]
+ -[UIFocusUpdateContext _isInitialMovement]
+ -[UIFocusUpdateContext _isValidInFocusSystem:]
+ -[UIFocusUpdateContext _nextFocusedGroupIdentifier]
+ -[UIFocusUpdateContext _preferredFocusReport]
+ -[UIFocusUpdateContext _previouslyFocusedGroupIdentifier]
+ -[UIFocusUpdateContext _request]
+ -[UIFocusUpdateContext _restoreRestrictedFocusMovementWithMovement:]
+ -[UIFocusUpdateContext _setCommonEnvironmentScrollableContainer:]
+ -[UIFocusUpdateContext _setDeferredUpdate:]
+ -[UIFocusUpdateContext _setDestinationViewDistanceOffscreen:]
+ -[UIFocusUpdateContext _setFocusGroupMap:]
+ -[UIFocusUpdateContext _setFocusMapSearchInfo:]
+ -[UIFocusUpdateContext _setFocusRedirectedByGuide:]
+ -[UIFocusUpdateContext _setFocusedGuideImpl:]
+ -[UIFocusUpdateContext _setInitialDestinationEnvironment:]
+ -[UIFocusUpdateContext _setPreferredFocusReport:]
+ -[UIFocusUpdateContext _setSourceItemInfo:]
+ -[UIFocusUpdateContext _setValidationReport:]
+ -[UIFocusUpdateContext _sourceItemInfo]
+ -[UIFocusUpdateContext _updateDestinationItemIfNeeded]
+ -[UIFocusUpdateContext _updateWithFocusGroupMap:]
+ -[UIFocusUpdateContext _validate]
+ -[UIFocusUpdateContext _validationReport]
+ -[UIFocusUpdateContext _willUpdateFocusFromFocusedItem:]
+ -[UIFocusUpdateContext description]
+ -[UIFocusUpdateContext focusBehavior]
+ -[UIFocusUpdateContext focusHeading]
+ -[UIFocusUpdateContext init]
+ -[UIFocusUpdateContext linearSortedFocusItems]
+ -[UIFocusUpdateContext nextFocusedItem]
+ -[UIFocusUpdateContext previouslyFocusedItem]
+ -[_UIDebugIssue .cxx_destruct]
+ -[_UIDebugIssue _subissueReport]
+ -[_UIDebugIssue addIssue:]
+ -[_UIDebugIssue description]
+ -[_UIDebugIssue init]
+ -[_UIDebugIssue prefix]
+ -[_UIDebugIssue setDescription:]
+ -[_UIDebugIssue setPrefix:]
+ -[_UIDebugIssue subissues]
+ -[_UIDebugIssueReport .cxx_destruct]
+ -[_UIDebugIssueReport addIssue:]
+ -[_UIDebugIssueReport init]
+ -[_UIDebugIssueReport issues]
+ -[_UIDebugIssueReportFormatter .cxx_destruct]
+ -[_UIDebugIssueReportFormatter _componentsFromReport:]
+ -[_UIDebugIssueReportFormatter defaultIssuePrefix]
+ -[_UIDebugIssueReportFormatter footer]
+ -[_UIDebugIssueReportFormatter header]
+ -[_UIDebugIssueReportFormatter init]
+ -[_UIDebugIssueReportFormatter noIssuesDescription]
+ -[_UIDebugIssueReportFormatter setDefaultIssuePrefix:]
+ -[_UIDebugIssueReportFormatter setFooter:]
+ -[_UIDebugIssueReportFormatter setHeader:]
+ -[_UIDebugIssueReportFormatter setNoIssuesDescription:]
+ -[_UIDebugIssueReportFormatter stringFromReport:]
+ -[_UIDebugLogReport .cxx_destruct]
+ -[_UIDebugLogReport _messagePrefixAtIndentLevel:]
+ -[_UIDebugLogReport _prefixStack]
+ -[_UIDebugLogReport _statements]
+ -[_UIDebugLogReport addLineBreak]
+ -[_UIDebugLogReport addMessage:]
+ -[_UIDebugLogReport addMessageWithFormat:]
+ -[_UIDebugLogReport clearAllMessagePrefixes]
+ -[_UIDebugLogReport currentIndentLevel]
+ -[_UIDebugLogReport decrementIndentLevelAndPopMessagePrefix]
+ -[_UIDebugLogReport decrementIndentLevel]
+ -[_UIDebugLogReport fallbackMessagePrefixHandler]
+ -[_UIDebugLogReport incrementIndentLevelAndPushMessagePrefix:]
+ -[_UIDebugLogReport incrementIndentLevel]
+ -[_UIDebugLogReport init]
+ -[_UIDebugLogReport messageCount]
+ -[_UIDebugLogReport popMessagePrefix]
+ -[_UIDebugLogReport pushMessagePrefix:]
+ -[_UIDebugLogReport pushMessagePrefixHandler:]
+ -[_UIDebugLogReport resetIndentLevel]
+ -[_UIDebugLogReport setCurrentIndentLevel:]
+ -[_UIDebugLogReport setFallbackMessagePrefixHandler:]
+ -[_UIDebugLogReport setPrefixStack:]
+ -[_UIDebugLogReport setStatements:]
+ -[_UIDebugLogReportFormatter _componentsFromReport:]
+ -[_UIDebugLogReportFormatter stringFromReport:]
+ -[_UIDebugLogStatement .cxx_destruct]
+ -[_UIDebugLogStatement indentLevel]
+ -[_UIDebugLogStatement init]
+ -[_UIDebugLogStatement prefix]
+ -[_UIDebugLogStatement setIndentLevel:]
+ -[_UIDebugLogStatement setPrefix:]
+ -[_UIDebugLogStatement setText:]
+ -[_UIDebugLogStatement setType:]
+ -[_UIDebugLogStatement text]
+ -[_UIDebugLogStatement type]
+ -[_UIDebugReportComponents .cxx_destruct]
+ -[_UIDebugReportComponents body]
+ -[_UIDebugReportComponents footer]
+ -[_UIDebugReportComponents header]
+ -[_UIDebugReportComponents init]
+ -[_UIDebugReportComponents setBody:]
+ -[_UIDebugReportComponents setFooter:]
+ -[_UIDebugReportComponents setHeader:]
+ -[_UIDebugReportFormatter .cxx_destruct]
+ -[_UIDebugReportFormatter extraBodyIndentLevel]
+ -[_UIDebugReportFormatter indentLevel]
+ -[_UIDebugReportFormatter indentString]
+ -[_UIDebugReportFormatter init]
+ -[_UIDebugReportFormatter setExtraBodyIndentLevel:]
+ -[_UIDebugReportFormatter setIndentLevel:]
+ -[_UIDebugReportFormatter setIndentString:]
+ -[_UIDebugReportFormatter stringFromReportComponents:]
+ -[_UIFocusContainerGuideFallbackItemsContainer .cxx_destruct]
+ -[_UIFocusContainerGuideFallbackItemsContainer childItems]
+ -[_UIFocusContainerGuideFallbackItemsContainer coordinateSpace]
+ -[_UIFocusContainerGuideFallbackItemsContainer didUpdateFocusInContext:]
+ -[_UIFocusContainerGuideFallbackItemsContainer focusItemContainer]
+ -[_UIFocusContainerGuideFallbackItemsContainer focusItemsInRect:]
+ -[_UIFocusContainerGuideFallbackItemsContainer initWithParentEnvironment:childItems:]
+ -[_UIFocusContainerGuideFallbackItemsContainer parentFocusEnvironment]
+ -[_UIFocusContainerGuideFallbackItemsContainer preferredFocusEnvironments]
+ -[_UIFocusContainerGuideFallbackItemsContainer setNeedsFocusUpdate]
+ -[_UIFocusContainerGuideFallbackItemsContainer shouldUpdateFocusInContext:]
+ -[_UIFocusContainerGuideFallbackItemsContainer updateFocusIfNeeded]
+ -[_UIFocusContainerGuideImpl .cxx_destruct]
+ -[_UIFocusContainerGuideImpl _isEligibleForFocusInteraction]
+ -[_UIFocusContainerGuideImpl _searchForFocusRegionsInContext:]
+ -[_UIFocusContainerGuideImpl fallbackItemProvider]
+ -[_UIFocusContainerGuideImpl initWithDelegate:]
+ -[_UIFocusContainerGuideImpl setFallbackItemProvider:]
+ -[_UIFocusContainerGuideRegion .cxx_destruct]
+ -[_UIFocusContainerGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:]
+ -[_UIFocusContainerGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusContainerGuideRegion _focusableBoundaries]
+ -[_UIFocusContainerGuideRegion contentFocusRegionContainer]
+ -[_UIFocusContainerGuideRegion fallbackRootRegionContainer]
+ -[_UIFocusContainerGuideRegion isEqual:]
+ -[_UIFocusContainerGuideRegion setContentFocusRegionContainer:]
+ -[_UIFocusContainerGuideRegion setFallbackRootRegionContainer:]
+ -[_UIFocusDebuggerStringOutput .cxx_destruct]
+ -[_UIFocusDebuggerStringOutput description]
+ -[_UIFocusDebuggerStringOutput initWithString:]
+ -[_UIFocusDebuggerStringOutput init]
+ -[_UIFocusEnvironmentContainerTuple .cxx_destruct]
+ -[_UIFocusEnvironmentContainerTuple description]
+ -[_UIFocusEnvironmentContainerTuple hash]
+ -[_UIFocusEnvironmentContainerTuple initWithOwningEnvironment:itemContainer:]
+ -[_UIFocusEnvironmentContainerTuple isEqual:]
+ -[_UIFocusEnvironmentContainerTuple isEqualToEnvironmentContainerTuple:]
+ -[_UIFocusEnvironmentContainerTuple isScrollableContainer]
+ -[_UIFocusEnvironmentContainerTuple itemContainer]
+ -[_UIFocusEnvironmentContainerTuple owningEnvironment]
+ -[_UIFocusEnvironmentPreferenceCache .cxx_destruct]
+ -[_UIFocusEnvironmentPreferenceCache deepestPrimaryPreferredEnvironmentForEnvironment:]
+ -[_UIFocusEnvironmentPreferenceCache environmentsMap]
+ -[_UIFocusEnvironmentPreferenceCache init]
+ -[_UIFocusEnvironmentPreferenceCache preferredEnvironmentsForEnvironment:isFinal:]
+ -[_UIFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]
+ -[_UIFocusEnvironmentPreferenceCache setResolvedPreference:forEnvironment:]
+ -[_UIFocusEnvironmentPreferenceCacheNode .cxx_destruct]
+ -[_UIFocusEnvironmentPreferenceCacheNode _reevaluateResolution]
+ -[_UIFocusEnvironmentPreferenceCacheNode _resolve:explicitly:]
+ -[_UIFocusEnvironmentPreferenceCacheNode _unresolve]
+ -[_UIFocusEnvironmentPreferenceCacheNode childNodes]
+ -[_UIFocusEnvironmentPreferenceCacheNode debugDescription]
+ -[_UIFocusEnvironmentPreferenceCacheNode description]
+ -[_UIFocusEnvironmentPreferenceCacheNode environment]
+ -[_UIFocusEnvironmentPreferenceCacheNode initWithEnvironment:]
+ -[_UIFocusEnvironmentPreferenceCacheNode isResolved]
+ -[_UIFocusEnvironmentPreferenceCacheNode resolve:]
+ -[_UIFocusEnvironmentPreferenceCacheNode resolvedEnvironment]
+ -[_UIFocusEnvironmentPreferenceCacheNode setChildNodes:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext .cxx_destruct]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _inferPreferencesForEnvironment:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _invalidatePreferredEnvironments]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _isAllowedToPreferEnvironment:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _reportInferredPreferredFocusEnvironment:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _resolvePreferredFocusEnvironments]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _startLogging]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext _stopLogging]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext debugStack]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext delegate]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext environment]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext init]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext isInPreferredSubtree]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext isLeafPreference]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext isPreferredByItself]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext isPrimaryPreference]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext popEnvironment]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext preferredEnvironments]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext preferringEnvironment]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext prefersNothingFocused]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext pushEnvironment:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext setDebugStack:]
+ -[_UIFocusEnvironmentPreferenceEnumerationContext setDelegate:]
+ -[_UIFocusEnvironmentPreferenceEnumerator .cxx_destruct]
+ -[_UIFocusEnvironmentPreferenceEnumerator _shouldInferDefaultPreferenceForEnvironmentInContext:]
+ -[_UIFocusEnvironmentPreferenceEnumerator allowsInferringPreferences]
+ -[_UIFocusEnvironmentPreferenceEnumerator debugLog]
+ -[_UIFocusEnvironmentPreferenceEnumerator didVisitAllPreferencesForEnvironmentHandler]
+ -[_UIFocusEnvironmentPreferenceEnumerator enumeratePreferencesForEnvironment:usingBlock:]
+ -[_UIFocusEnvironmentPreferenceEnumerator enumerationMode]
+ -[_UIFocusEnvironmentPreferenceEnumerator initWithEnumerationMode:]
+ -[_UIFocusEnvironmentPreferenceEnumerator init]
+ -[_UIFocusEnvironmentPreferenceEnumerator setAllowsInferringPreferences:]
+ -[_UIFocusEnvironmentPreferenceEnumerator setDebugLog:]
+ -[_UIFocusEnvironmentPreferenceEnumerator setDidVisitAllPreferencesForEnvironmentHandler:]
+ -[_UIFocusEnvironmentPreferenceEnumerator setShouldInferPreferenceForEnvironmentHandler:]
+ -[_UIFocusEnvironmentPreferenceEnumerator shouldInferPreferenceForEnvironmentHandler]
+ -[_UIFocusEnvironmentScrollableContainerTuple .cxx_destruct]
+ -[_UIFocusEnvironmentScrollableContainerTuple description]
+ -[_UIFocusEnvironmentScrollableContainerTuple hash]
+ -[_UIFocusEnvironmentScrollableContainerTuple initWithOwningEnvironment:scrollableContainer:]
+ -[_UIFocusEnvironmentScrollableContainerTuple isEqual:]
+ -[_UIFocusEnvironmentScrollableContainerTuple owningEnvironment]
+ -[_UIFocusEnvironmentScrollableContainerTuple scrollableContainer]
+ -[_UIFocusGroup .cxx_destruct]
+ -[_UIFocusGroup _deepCopyWithNewIdentifierToGroupMap:]
+ -[_UIFocusGroup _insertChildGroup:]
+ -[_UIFocusGroup _insertItem:]
+ -[_UIFocusGroup _invalidateChildGroupOrder]
+ -[_UIFocusGroup _invalidateItemOrder]
+ -[_UIFocusGroup _invalidatePrimaryItem]
+ -[_UIFocusGroup _invalidatePrimaryRect]
+ -[_UIFocusGroup _updateWithEnvironment:]
+ -[_UIFocusGroup _validateChildGroupOrderIfNecessary]
+ -[_UIFocusGroup _validateItemOrderIfNecessary]
+ -[_UIFocusGroup _validatePrimaryItemIfNecessary]
+ -[_UIFocusGroup _validatePrimaryRectIfNeccessary]
+ -[_UIFocusGroup boundingBox]
+ -[_UIFocusGroup childGroups]
+ -[_UIFocusGroup coordinateSpace]
+ -[_UIFocusGroup debugDescription]
+ -[_UIFocusGroup description]
+ -[_UIFocusGroup hash]
+ -[_UIFocusGroup identifier]
+ -[_UIFocusGroup initWithIdentifier:parentGroup:coordinateSpace:]
+ -[_UIFocusGroup isEqual:]
+ -[_UIFocusGroup isEqualToFocusGroup:]
+ -[_UIFocusGroup items]
+ -[_UIFocusGroup owningEnvironment]
+ -[_UIFocusGroup parentGroup]
+ -[_UIFocusGroup primaryItem]
+ -[_UIFocusGroup primaryRect]
+ -[_UIFocusGroupHistory .cxx_destruct]
+ -[_UIFocusGroupHistory _uiktest_clearHistory]
+ -[_UIFocusGroupHistory init]
+ -[_UIFocusGroupHistory lastFocusedItemForGroupIdentifier:]
+ -[_UIFocusGroupHistory setLastFocusedItem:forGroupIdentifier:]
+ -[_UIFocusGroupMap .cxx_destruct]
+ -[_UIFocusGroupMap _indexEnvironment:]
+ -[_UIFocusGroupMap _indexItems:]
+ -[_UIFocusGroupMap coordinateSpace]
+ -[_UIFocusGroupMap copyWithZone:]
+ -[_UIFocusGroupMap description]
+ -[_UIFocusGroupMap focusGroupForItem:]
+ -[_UIFocusGroupMap focusGroups]
+ -[_UIFocusGroupMap focusItems]
+ -[_UIFocusGroupMap initWithItems:coordinateSpace:]
+ -[_UIFocusGroupMap initWithItems:standInItemsMap:coordinateSpace:]
+ -[_UIFocusGuideImpl .cxx_destruct]
+ -[_UIFocusGuideImpl _automaticallyPreferOwningItem]
+ -[_UIFocusGuideImpl _didSetPreferredFocusedEnvironments]
+ -[_UIFocusGuideImpl _focusPriorityRequired]
+ -[_UIFocusGuideImpl _ignoresSpeedBumpEdges]
+ -[_UIFocusGuideImpl _isEligibleForFocusInteraction]
+ -[_UIFocusGuideImpl _isUnclippable]
+ -[_UIFocusGuideImpl _isUnoccludable]
+ -[_UIFocusGuideImpl _preferredFocusRegionCoordinateSpace]
+ -[_UIFocusGuideImpl _searchForFocusRegionsInContext:]
+ -[_UIFocusGuideImpl _setAutomaticallyPreferOwningItem:]
+ -[_UIFocusGuideImpl _setDidSetPreferredFocusedEnvironments:]
+ -[_UIFocusGuideImpl _setFocusPriorityRequired:]
+ -[_UIFocusGuideImpl _setIgnoresSpeedBumpEdges:]
+ -[_UIFocusGuideImpl _setIsUnclippable:]
+ -[_UIFocusGuideImpl _setIsUnoccludable:]
+ -[_UIFocusGuideImpl _uili_isFocusGuide]
+ -[_UIFocusGuideImpl canBecomeFocused]
+ -[_UIFocusGuideImpl delegate]
+ -[_UIFocusGuideImpl description]
+ -[_UIFocusGuideImpl didUpdateFocusInContext:]
+ -[_UIFocusGuideImpl focusDidUpdateViaGuide]
+ -[_UIFocusGuideImpl focusGuideRegion:preferredFocusEnvironmentsForMovementRequest:]
+ -[_UIFocusGuideImpl focusGuideRegion:willParticipateAsDestinationRegionInFocusUpdate:]
+ -[_UIFocusGuideImpl focusItemContainer]
+ -[_UIFocusGuideImpl focusItemForSorting]
+ -[_UIFocusGuideImpl frame]
+ -[_UIFocusGuideImpl initWithDelegate:]
+ -[_UIFocusGuideImpl init]
+ -[_UIFocusGuideImpl isEnabled]
+ -[_UIFocusGuideImpl owningItem]
+ -[_UIFocusGuideImpl parentFocusEnvironment]
+ -[_UIFocusGuideImpl preferredFocusEnvironments]
+ -[_UIFocusGuideImpl setEnabled:]
+ -[_UIFocusGuideImpl setNeedsFocusUpdate]
+ -[_UIFocusGuideImpl setOwningItem:]
+ -[_UIFocusGuideImpl setPreferredFocusEnvironments:]
+ -[_UIFocusGuideImpl shouldUpdateFocusInContext:]
+ -[_UIFocusGuideImpl updateFocusIfNeeded]
+ -[_UIFocusGuideRegion .cxx_destruct]
+ -[_UIFocusGuideRegion _canBeOccludedByRegionsAbove]
+ -[_UIFocusGuideRegion _canOccludeRegionsBelow]
+ -[_UIFocusGuideRegion _debugAssociatedObject]
+ -[_UIFocusGuideRegion _delegatePreferredFocusEnvironmentsForMovementRequest:]
+ -[_UIFocusGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:]
+ -[_UIFocusGuideRegion _focusPriority]
+ -[_UIFocusGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusGuideRegion _focusableBoundaries]
+ -[_UIFocusGuideRegion _focusedItemForLinearSorting:inMap:withSnapshot:]
+ -[_UIFocusGuideRegion _ignoresSpeedBumpEdges]
+ -[_UIFocusGuideRegion _isEnabledForFocusedRegion:inSnapshot:]
+ -[_UIFocusGuideRegion _isUnclippable]
+ -[_UIFocusGuideRegion _isUnoccludable]
+ -[_UIFocusGuideRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
+ -[_UIFocusGuideRegion _preferredDistanceComparisonType]
+ -[_UIFocusGuideRegion _setFocusPriority:]
+ -[_UIFocusGuideRegion _setIgnoresSpeedBumpEdges:]
+ -[_UIFocusGuideRegion _setIsUnclippable:]
+ -[_UIFocusGuideRegion _setIsUnoccludable:]
+ -[_UIFocusGuideRegion _shouldCropRegionToSearchArea]
+ -[_UIFocusGuideRegion _shouldUseNextFocusedItemForLinearSorting]
+ -[_UIFocusGuideRegion _willParticipateAsDestinationRegionInFocusUpdate:]
+ -[_UIFocusGuideRegion delegate]
+ -[_UIFocusGuideRegion initWithFrame:coordinateSpace:]
+ -[_UIFocusGuideRegion isEqual:]
+ -[_UIFocusGuideRegion owningEnvironment]
+ -[_UIFocusGuideRegion setDelegate:]
+ -[_UIFocusGuideRegion setOwningEnvironment:]
+ -[_UIFocusInputDeviceInfo _initWithSenderID:]
+ -[_UIFocusInputDeviceInfo copyWithZone:]
+ -[_UIFocusInputDeviceInfo encodeWithCoder:]
+ -[_UIFocusInputDeviceInfo encodeWithXPCDictionary:]
+ -[_UIFocusInputDeviceInfo initWithCoder:]
+ -[_UIFocusInputDeviceInfo initWithXPCDictionary:]
+ -[_UIFocusInputDeviceInfo senderID]
+ -[_UIFocusItemDummy .cxx_destruct]
+ -[_UIFocusItemDummy canBecomeFocused]
+ -[_UIFocusItemDummy didUpdateFocusInContext:]
+ -[_UIFocusItemDummy focusItemContainer]
+ -[_UIFocusItemDummy frame]
+ -[_UIFocusItemDummy parentFocusEnvironment]
+ -[_UIFocusItemDummy preferredFocusEnvironments]
+ -[_UIFocusItemDummy setFrame:]
+ -[_UIFocusItemDummy setNeedsFocusUpdate]
+ -[_UIFocusItemDummy setParentFocusEnvironment:]
+ -[_UIFocusItemDummy shouldUpdateFocusInContext:]
+ -[_UIFocusItemDummy updateFocusIfNeeded]
+ -[_UIFocusItemInfo .cxx_destruct]
+ -[_UIFocusItemInfo _createFocusedRegion]
+ -[_UIFocusItemInfo _initWithItem:useFallbackAncestorScroller:]
+ -[_UIFocusItemInfo ancestorEnvironmentScrollableContainers]
+ -[_UIFocusItemInfo copyWithZone:]
+ -[_UIFocusItemInfo description]
+ -[_UIFocusItemInfo focusTouchSensitivityStyle]
+ -[_UIFocusItemInfo focusedRectInCoordinateSpace:]
+ -[_UIFocusItemInfo focusedRegion]
+ -[_UIFocusItemInfo inheritedFocusMovementStyle]
+ -[_UIFocusItemInfo invalidateFocusedRegion]
+ -[_UIFocusItemInfo isFocusMovementFlippedHorizontally]
+ -[_UIFocusItemInfo item]
+ -[_UIFocusItemInfo rotaryFocusMovementAxis]
+ -[_UIFocusItemInfo shortDescription]
+ -[_UIFocusItemInfo useFallbackAncestorScroller]
+ -[_UIFocusItemRegion .cxx_destruct]
+ -[_UIFocusItemRegion _canBeOccludedByRegionsAbove]
+ -[_UIFocusItemRegion _canOccludeRegionsBelow]
+ -[_UIFocusItemRegion _debugAssociatedObject]
+ -[_UIFocusItemRegion _defaultFocusItem]
+ -[_UIFocusItemRegion _descriptionBuilder]
+ -[_UIFocusItemRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusItemRegion _focusableBoundaries]
+ -[_UIFocusItemRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
+ -[_UIFocusItemRegion _preferredDistanceComparisonType]
+ -[_UIFocusItemRegion initWithFrame:coordinateSpace:]
+ -[_UIFocusItemRegion initWithFrame:coordinateSpace:item:focusSystem:]
+ -[_UIFocusItemRegion isEqual:]
+ -[_UIFocusItemRegion item]
+ -[_UIFocusLinearMovementCache .cxx_destruct]
+ -[_UIFocusLinearMovementCache _invalidateOnTimeout]
+ -[_UIFocusLinearMovementCache _invalidate]
+ -[_UIFocusLinearMovementCache _updateParentEnvironmentIfNecessary]
+ -[_UIFocusLinearMovementCache environmentDidAppear:]
+ -[_UIFocusLinearMovementCache environmentWillDisappear:]
+ -[_UIFocusLinearMovementCache focusGroupPriorityDidChange:]
+ -[_UIFocusLinearMovementCache initWithFocusBehavior:]
+ -[_UIFocusLinearMovementCache invalidateFocusItemContainer:]
+ -[_UIFocusLinearMovementCache nextItemForRequest:]
+ -[_UIFocusLinearMovementCache scrollableContainerDidScroll:]
+ -[_UIFocusLinearMovementCache updateCacheWithContext:]
+ -[_UIFocusLinearMovementSequence .cxx_destruct]
+ -[_UIFocusLinearMovementSequence initWithItems:loops:]
+ -[_UIFocusLinearMovementSequence initWithItems:loops:restrictEnteringSequence:]
+ -[_UIFocusLinearMovementSequence init]
+ -[_UIFocusLinearMovementSequence isLooping]
+ -[_UIFocusLinearMovementSequence items]
+ -[_UIFocusLinearMovementSequence restrictsEnteringSequence]
+ -[_UIFocusMap .cxx_destruct]
+ -[_UIFocusMap _allRegionsInContainer:intersectingRegion:]
+ -[_UIFocusMap _beginTrackingDefaultItemSearchInfoIfNecessary]
+ -[_UIFocusMap _beginTrackingFocusMovementSearchInfoIfNecessary]
+ -[_UIFocusMap _beginTrackingSearches]
+ -[_UIFocusMap _closestFocusableItemToPoint:inRect:itemFilter:distanceMeasuringUnitPoint:]
+ -[_UIFocusMap _defaultItemSearchContext]
+ -[_UIFocusMap _defaultMapSnapshotter]
+ -[_UIFocusMap _focusMovementSearchContext]
+ -[_UIFocusMap _inferredDefaultFocusItemInEnvironment:]
+ -[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]
+ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:]
+ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:inRegions:withSnapshot:]
+ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:]
+ -[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
+ -[_UIFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
+ -[_UIFocusMap _nextFocusedItemForNonLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
+ -[_UIFocusMap _stopTrackingSearches]
+ -[_UIFocusMap _trackExternalSnapshot:]
+ -[_UIFocusMap coordinateSpace]
+ -[_UIFocusMap diagnoseFocusabilityForItem:report:]
+ -[_UIFocusMap focusGroupMap]
+ -[_UIFocusMap focusSystem]
+ -[_UIFocusMap initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
+ -[_UIFocusMap initWithFocusSystem:rootEnvironment:]
+ -[_UIFocusMap initWithFocusSystem:rootEnvironment:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
+ -[_UIFocusMap init]
+ -[_UIFocusMap minimumSearchArea]
+ -[_UIFocusMap rootContainer]
+ -[_UIFocusMap searchInfo]
+ -[_UIFocusMap setMinimumSearchArea:]
+ -[_UIFocusMap verifyFocusabilityForItem:]
+ -[_UIFocusMapRect .cxx_destruct]
+ -[_UIFocusMapRect coordinateSpace]
+ -[_UIFocusMapRect description]
+ -[_UIFocusMapRect frame]
+ -[_UIFocusMapRect initWithFrame:coordinateSpace:]
+ -[_UIFocusMapRect intersectionWithRegion:inSnapshot:]
+ -[_UIFocusMapRect intersectsRect:]
+ -[_UIFocusMapRect intersectsRegion:inSnapshot:]
+ -[_UIFocusMapSearchInfo .cxx_destruct]
+ -[_UIFocusMapSearchInfo addDestinationRegion:]
+ -[_UIFocusMapSearchInfo addSnapshot:]
+ -[_UIFocusMapSearchInfo destinationRegions]
+ -[_UIFocusMapSearchInfo didFindFocusBlockingBoundary]
+ -[_UIFocusMapSearchInfo focusGroupMap]
+ -[_UIFocusMapSearchInfo hasOnlyStaticContent]
+ -[_UIFocusMapSearchInfo init]
+ -[_UIFocusMapSearchInfo linearSortedFocusItems]
+ -[_UIFocusMapSearchInfo mutableDestinationRegions]
+ -[_UIFocusMapSearchInfo mutableSnapshots]
+ -[_UIFocusMapSearchInfo searchInfo]
+ -[_UIFocusMapSearchInfo setDidFindFocusBlockingBoundary:]
+ -[_UIFocusMapSearchInfo setFocusGroupMap:]
+ -[_UIFocusMapSearchInfo setLinearSortedFocusItems:]
+ -[_UIFocusMapSearchInfo setMutableDestinationRegions:]
+ -[_UIFocusMapSearchInfo setMutableSnapshots:]
+ -[_UIFocusMapSearchInfo setSearchInfo:]
+ -[_UIFocusMapSearchInfo snapshots]
+ -[_UIFocusMapSnapshot .cxx_destruct]
+ -[_UIFocusMapSnapshot _cachedNextFocusedItemForRegion:withFocusMovementRequest:inMap:]
+ -[_UIFocusMapSnapshot _capture]
+ -[_UIFocusMapSnapshot _initWithSnapshotter:mapArea:searchArea:]
+ -[_UIFocusMapSnapshot _searchArea]
+ -[_UIFocusMapSnapshot _trackOccludingRegion:forRegion:]
+ -[_UIFocusMapSnapshot _trackSubregion:forRegion:]
+ -[_UIFocusMapSnapshot addRegion:]
+ -[_UIFocusMapSnapshot addRegions:]
+ -[_UIFocusMapSnapshot addRegionsInContainer:]
+ -[_UIFocusMapSnapshot addRegionsInContainers:]
+ -[_UIFocusMapSnapshot consumeRegionInformationForRegions:fromSnapshot:]
+ -[_UIFocusMapSnapshot coordinateSpace]
+ -[_UIFocusMapSnapshot dealloc]
+ -[_UIFocusMapSnapshot focusSystem]
+ -[_UIFocusMapSnapshot focusedRegion]
+ -[_UIFocusMapSnapshot hasOnlyStaticContent]
+ -[_UIFocusMapSnapshot init]
+ -[_UIFocusMapSnapshot mapArea]
+ -[_UIFocusMapSnapshot markContainerAsProvidingDynamicContent]
+ -[_UIFocusMapSnapshot movementInfo]
+ -[_UIFocusMapSnapshot occludingRegionsForRegion:]
+ -[_UIFocusMapSnapshot originalRegionForRegion:]
+ -[_UIFocusMapSnapshot originalRegions]
+ -[_UIFocusMapSnapshot regionsContainer]
+ -[_UIFocusMapSnapshot regionsForOriginalRegion:]
+ -[_UIFocusMapSnapshot regions]
+ -[_UIFocusMapSnapshot rootContainer]
+ -[_UIFocusMapSnapshot searchArea]
+ -[_UIFocusMapSnapshot searchInfo]
+ -[_UIFocusMapSnapshot setMovementInfo:]
+ -[_UIFocusMapSnapshot setSearchInfo:]
+ -[_UIFocusMapSnapshot snapshotFrameForRegion:]
+ -[_UIFocusMapSnapshotter .cxx_destruct]
+ -[_UIFocusMapSnapshotter _searchAreaForContainerSearchRect:]
+ -[_UIFocusMapSnapshotter captureSnapshot]
+ -[_UIFocusMapSnapshotter clipToSnapshotRect]
+ -[_UIFocusMapSnapshotter coordinateSpace]
+ -[_UIFocusMapSnapshotter focusSystem]
+ -[_UIFocusMapSnapshotter focusedRegion]
+ -[_UIFocusMapSnapshotter ignoresRootContainerClippingRect]
+ -[_UIFocusMapSnapshotter initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
+ -[_UIFocusMapSnapshotter init]
+ -[_UIFocusMapSnapshotter movementInfo]
+ -[_UIFocusMapSnapshotter regionsContainer]
+ -[_UIFocusMapSnapshotter rootContainer]
+ -[_UIFocusMapSnapshotter searchInfo]
+ -[_UIFocusMapSnapshotter setClipToSnapshotRect:]
+ -[_UIFocusMapSnapshotter setFocusedRegion:]
+ -[_UIFocusMapSnapshotter setIgnoresRootContainerClippingRect:]
+ -[_UIFocusMapSnapshotter setMovementInfo:]
+ -[_UIFocusMapSnapshotter setRegionsContainer:]
+ -[_UIFocusMapSnapshotter setSearchInfo:]
+ -[_UIFocusMapSnapshotter setSnapshotFrame:]
+ -[_UIFocusMapSnapshotter snapshotFrame]
+ -[_UIFocusMovementInfo _fallbackMovementOriginatingFrame]
+ -[_UIFocusMovementInfo _groupFilter]
+ -[_UIFocusMovementInfo _inputType]
+ -[_UIFocusMovementInfo _isInitialMovement]
+ -[_UIFocusMovementInfo _isLinearMovement]
+ -[_UIFocusMovementInfo _isLooping]
+ -[_UIFocusMovementInfo _isVelocityBased]
+ -[_UIFocusMovementInfo _linearHeading]
+ -[_UIFocusMovementInfo _setFallbackMovementOriginatingFrame:]
+ -[_UIFocusMovementInfo _setGroupFilter:]
+ -[_UIFocusMovementInfo _setHeading:]
+ -[_UIFocusMovementInfo _setInputType:]
+ -[_UIFocusMovementInfo _setIsInitialMovement:]
+ -[_UIFocusMovementInfo _setIsVelocityBased:]
+ -[_UIFocusMovementInfo _setLinearHeading:]
+ -[_UIFocusMovementInfo _setLooping:]
+ -[_UIFocusMovementInfo _setShouldLoadScrollableContainer:]
+ -[_UIFocusMovementInfo _setVelocity:]
+ -[_UIFocusMovementInfo _shouldLoadScrollableContainer]
+ -[_UIFocusMovementInfo _velocity]
+ -[_UIFocusMovementInfo copyWithZone:]
+ -[_UIFocusMovementInfo description]
+ -[_UIFocusMovementInfo encodeWithCoder:]
+ -[_UIFocusMovementInfo encodeWithXPCDictionary:]
+ -[_UIFocusMovementInfo heading]
+ -[_UIFocusMovementInfo initWithCoder:]
+ -[_UIFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:]
+ -[_UIFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:inputType:]
+ -[_UIFocusMovementInfo initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:inputType:]
+ -[_UIFocusMovementInfo initWithXPCDictionary:]
+ -[_UIFocusMovementInfo init]
+ -[_UIFocusMovementPerformer .cxx_destruct]
+ -[_UIFocusMovementPerformer __findFocusCandidateInEnvironment:container:forRequest:minimumSearchArea:isLoadingScrollableContainer:]
+ -[_UIFocusMovementPerformer _bestCandidateForLinearFocusMovement:]
+ -[_UIFocusMovementPerformer _bestCandidateForNonLinearFocusMovement:]
+ -[_UIFocusMovementPerformer _dummyFocusItemForFocusMovement:searchArea:parent:]
+ -[_UIFocusMovementPerformer _environmentContainersToCheckForRequest:]
+ -[_UIFocusMovementPerformer _findFocusCandidateByExhaustivelySearchingEnvironment:scrollableContainer:forRequest:]
+ -[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]
+ -[_UIFocusMovementPerformer _findFocusCandidateWithoutLoadingScrollableContentInEnvironment:container:forRequest:minimumSearchArea:]
+ -[_UIFocusMovementPerformer _isMovementValidForFocusSequences:]
+ -[_UIFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:]
+ -[_UIFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:shouldLoadScrollableContainer:]
+ -[_UIFocusMovementPerformer _nextLinearCandidateLoadingScrollableContentForRequest:]
+ -[_UIFocusMovementPerformer contextForFocusMovement:]
+ -[_UIFocusMovementPerformer delegate]
+ -[_UIFocusMovementPerformer performFocusMovement:]
+ -[_UIFocusMovementPerformer setDelegate:]
+ -[_UIFocusMovementRequest .cxx_destruct]
+ -[_UIFocusMovementRequest _requestByRedirectingRequestToFocusSystem:]
+ -[_UIFocusMovementRequest allowsDeferral]
+ -[_UIFocusMovementRequest allowsFocusingCurrentItem]
+ -[_UIFocusMovementRequest allowsOverridingPreferedFocusEnvironments]
+ -[_UIFocusMovementRequest fallbackRequest]
+ -[_UIFocusMovementRequest focusSystem]
+ -[_UIFocusMovementRequest focusedItemInfo]
+ -[_UIFocusMovementRequest initWithFocusSystem:]
+ -[_UIFocusMovementRequest init]
+ -[_UIFocusMovementRequest inputDeviceInfo]
+ -[_UIFocusMovementRequest isMovementRequest]
+ -[_UIFocusMovementRequest movementInfo]
+ -[_UIFocusMovementRequest overridesDeferredFocusUpdate]
+ -[_UIFocusMovementRequest requiresEnvironmentValidation]
+ -[_UIFocusMovementRequest requiresNextFocusedItem]
+ -[_UIFocusMovementRequest searchInfo]
+ -[_UIFocusMovementRequest setFocusedItemInfo:]
+ -[_UIFocusMovementRequest setInputDeviceInfo:]
+ -[_UIFocusMovementRequest setMovementInfo:]
+ -[_UIFocusMovementRequest setOverridesDeferredFocusUpdate:]
+ -[_UIFocusMovementRequest setSearchInfo:]
+ -[_UIFocusMovementRequest setShouldPerformHapticFeedback:]
+ -[_UIFocusMovementRequest shouldPerformHapticFeedback]
+ -[_UIFocusMovementRequest shouldPlayFocusSound]
+ -[_UIFocusMovementRequest shouldScrollIfNecessary]
+ -[_UIFocusNullGroup _updateWithEnvironment:]
+ -[_UIFocusNullGroup boundingBox]
+ -[_UIFocusNullGroup primaryItem]
+ -[_UIFocusPromiseItem .cxx_destruct]
+ -[_UIFocusPromiseItem _isEligibleForFocusInteraction]
+ -[_UIFocusPromiseItem _isLazyFocusItemContainer]
+ -[_UIFocusPromiseItem canBecomeFocused]
+ -[_UIFocusPromiseItem coordinateSpace]
+ -[_UIFocusPromiseItem debugIdentifier]
+ -[_UIFocusPromiseItem description]
+ -[_UIFocusPromiseItem didUpdateFocusInContext:]
+ -[_UIFocusPromiseItem focusItemContainer]
+ -[_UIFocusPromiseItem focusItemsInRect:]
+ -[_UIFocusPromiseItem frame]
+ -[_UIFocusPromiseItem fulfilledItem]
+ -[_UIFocusPromiseItem fulfillmentHandler]
+ -[_UIFocusPromiseItem initWithParentEnvironment:frame:fullfillmentHandler:]
+ -[_UIFocusPromiseItem parentFocusEnvironment]
+ -[_UIFocusPromiseItem preferredFocusEnvironments]
+ -[_UIFocusPromiseItem setDebugIdentifier:]
+ -[_UIFocusPromiseItem setFrame:]
+ -[_UIFocusPromiseItem setFulfillmentHandler:]
+ -[_UIFocusPromiseItem setNeedsFocusUpdate]
+ -[_UIFocusPromiseItem setParentFocusEnvironment:]
+ -[_UIFocusPromiseItem shouldUpdateFocusInContext:]
+ -[_UIFocusPromiseItem updateFocusIfNeeded]
+ -[_UIFocusPromiseRegion .cxx_destruct]
+ -[_UIFocusPromiseRegion _descriptionBuilder]
+ -[_UIFocusPromiseRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusPromiseRegion _focusableBoundaries]
+ -[_UIFocusPromiseRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
+ -[_UIFocusPromiseRegion contentFulfillmentHandler]
+ -[_UIFocusPromiseRegion initWithFrame:coordinateSpace:]
+ -[_UIFocusPromiseRegion initWithFrame:coordinateSpace:identifier:]
+ -[_UIFocusPromiseRegion isEqual:]
+ -[_UIFocusPromiseRegion setContentFulfillmentHandler:]
+ -[_UIFocusRegion .cxx_destruct]
+ -[_UIFocusRegion _boundariesBlockingFocusMovementRequest:]
+ -[_UIFocusRegion _canBeOccludedByRegionsAbove]
+ -[_UIFocusRegion _canOccludeRegionsBelow]
+ -[_UIFocusRegion _debugAssociatedObject]
+ -[_UIFocusRegion _defaultFocusItem]
+ -[_UIFocusRegion _descriptionBuilder]
+ -[_UIFocusRegion _didParticipateAsDestinationRegionInFocusUpdate:]
+ -[_UIFocusRegion _effectiveBoundariesBlockingFocusMovementRequest:]
+ -[_UIFocusRegion _effectiveFocusableBoundariesForHeading:]
+ -[_UIFocusRegion _focusPriority]
+ -[_UIFocusRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusRegion _focusableBoundaries]
+ -[_UIFocusRegion _focusedItemForLinearSorting:inMap:withSnapshot:]
+ -[_UIFocusRegion _ignoresSpeedBumpEdges]
+ -[_UIFocusRegion _isUnclippable]
+ -[_UIFocusRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
+ -[_UIFocusRegion _preferredDistanceComparisonType]
+ -[_UIFocusRegion _shouldCropRegionToSearchArea]
+ -[_UIFocusRegion _shouldUseNextFocusedItemForLinearSorting]
+ -[_UIFocusRegion _willParticipateAsDestinationRegionInFocusUpdate:]
+ -[_UIFocusRegion description]
+ -[_UIFocusRegion hash]
+ -[_UIFocusRegion initWithFrame:coordinateSpace:]
+ -[_UIFocusRegion isEqual:]
+ -[_UIFocusRegion regionCoordinateSpace]
+ -[_UIFocusRegion regionFrame]
+ -[_UIFocusRegionContainerProxy .cxx_destruct]
+ -[_UIFocusRegionContainerProxy _clippingRectInCoordinateSpace:]
+ -[_UIFocusRegionContainerProxy _didUpdateFocusInContext:]
+ -[_UIFocusRegionContainerProxy _focusSystem]
+ -[_UIFocusRegionContainerProxy _isEligibleForFocusInteraction]
+ -[_UIFocusRegionContainerProxy _isEligibleForFocusOcclusion]
+ -[_UIFocusRegionContainerProxy _itemContainer]
+ -[_UIFocusRegionContainerProxy _preferredFocusRegionCoordinateSpace]
+ -[_UIFocusRegionContainerProxy _searchForFocusRegionsInContext:]
+ -[_UIFocusRegionContainerProxy _ui_isUIFocusRegionContainerProxy]
+ -[_UIFocusRegionContainerProxy allowsLazyLoading]
+ -[_UIFocusRegionContainerProxy description]
+ -[_UIFocusRegionContainerProxy didUpdateFocusInContext:]
+ -[_UIFocusRegionContainerProxy environmentContainer]
+ -[_UIFocusRegionContainerProxy focusItemContainer]
+ -[_UIFocusRegionContainerProxy hash]
+ -[_UIFocusRegionContainerProxy initWithEnvironmentContainer:]
+ -[_UIFocusRegionContainerProxy initWithOwningEnvironment:itemContainer:]
+ -[_UIFocusRegionContainerProxy isEqual:]
+ -[_UIFocusRegionContainerProxy owningEnvironment]
+ -[_UIFocusRegionContainerProxy parentFocusEnvironment]
+ -[_UIFocusRegionContainerProxy preferredFocusEnvironments]
+ -[_UIFocusRegionContainerProxy setAllowsLazyLoading:]
+ -[_UIFocusRegionContainerProxy setEnvironmentContainer:]
+ -[_UIFocusRegionContainerProxy setNeedsFocusUpdate]
+ -[_UIFocusRegionContainerProxy setShouldCreateRegionForGuideBehavior:]
+ -[_UIFocusRegionContainerProxy setShouldCreateRegionForOwningItem:]
+ -[_UIFocusRegionContainerProxy shouldCreateRegionForGuideBehavior]
+ -[_UIFocusRegionContainerProxy shouldCreateRegionForOwningItem]
+ -[_UIFocusRegionContainerProxy shouldUpdateFocusInContext:]
+ -[_UIFocusRegionContainerProxy updateFocusIfNeeded]
+ -[_UIFocusRegionMovementInfo originatingHeading]
+ -[_UIFocusRegionMovementInfo setOriginatingHeading:]
+ -[_UIFocusRegionSearchContextState .cxx_destruct]
+ -[_UIFocusRegionSearchContextState clippingRect]
+ -[_UIFocusRegionSearchContextState initWithRegionContainer:focusSystem:clippingRect:]
+ -[_UIFocusRegionSearchContextState regionContainerFocusSystem]
+ -[_UIFocusRegionSearchContextState regionContainer]
+ -[_UIFocusSearchInfo .cxx_destruct]
+ -[_UIFocusSearchInfo evaluator]
+ -[_UIFocusSearchInfo forceFocusToLeaveContainer]
+ -[_UIFocusSearchInfo initWithFocusEvaluator:]
+ -[_UIFocusSearchInfo setEvaluator:]
+ -[_UIFocusSearchInfo setForceFocusToLeaveContainer:]
+ -[_UIFocusSearchInfo setTreatFocusableItemAsLeaf:]
+ -[_UIFocusSearchInfo shouldIncludeFocusItem:]
+ -[_UIFocusSearchInfo treatFocusableItemAsLeaf]
+ -[_UIFocusSpeedBumpRegion _boundariesBlockingFocusMovementRequest:]
+ -[_UIFocusSpeedBumpRegion _canBeOccludedByRegionsAbove]
+ -[_UIFocusSpeedBumpRegion _canOccludeRegionsBelow]
+ -[_UIFocusSpeedBumpRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
+ -[_UIFocusSpeedBumpRegion _shouldCropRegionToSearchArea]
+ -[_UIFocusSpeedBumpRegion initWithFrame:coordinateSpace:]
+ -[_UIFocusSpeedBumpRegion initWithFrame:coordinateSpace:speedBumpEdges:]
+ -[_UIFocusSpeedBumpRegion isEqual:]
+ -[_UIFocusSpeedBumpRegion setSpeedBumpEdges:]
+ -[_UIFocusSpeedBumpRegion speedBumpEdges]
+ -[_UIFocusTreeLock .cxx_destruct]
+ -[_UIFocusTreeLock _validateLockedEnvironments]
+ -[_UIFocusTreeLock description]
+ -[_UIFocusTreeLock init]
+ -[_UIFocusTreeLock isEnvironmentLocked:]
+ -[_UIFocusTreeLock lockEnvironmentTree:]
+ -[_UIFocusTreeLock lockedEnvironments]
+ -[_UIFocusTreeLock unlockEnvironmentTree:]
+ -[_UIFocusTreeLock validationTimer]
+ -[_UIFocusTreeLockItem .cxx_destruct]
+ -[_UIFocusTreeLockItem _cleanup:]
+ -[_UIFocusTreeLockItem dealloc]
+ -[_UIFocusTreeLockItem description]
+ -[_UIFocusTreeLockItem environmentDescription]
+ -[_UIFocusTreeLockItem environment]
+ -[_UIFocusTreeLockItem initWithEnvironment:finalUnlockHandler:]
+ -[_UIFocusTreeLockItem lockCallStackSymbols]
+ -[_UIFocusTreeLockItem lockCount]
+ -[_UIFocusTreeLockItem lockTime]
+ -[_UIFocusTreeLockItem lock]
+ -[_UIFocusTreeLockItem unlockCallStackSymbols]
+ -[_UIFocusTreeLockItem unlock]
+ -[_UIFocusTreeLockItem validate]
+ -[_UIFocusUpdateReport .cxx_destruct]
+ -[_UIFocusUpdateReport context]
+ -[_UIFocusUpdateReport focusSystem]
+ -[_UIFocusUpdateReport initWithFocusSystem:]
+ -[_UIFocusUpdateReport init]
+ -[_UIFocusUpdateReport setContext:]
+ -[_UIFocusUpdateReport shouldLog]
+ -[_UIFocusUpdateReportFormatter _bodyForReport:]
+ -[_UIFocusUpdateReportFormatter _componentsFromReport:]
+ -[_UIFocusUpdateReportFormatter _headerForReport:]
+ -[_UIFocusUpdateReportFormatter stringFromReport:]
+ -[_UIFocusUpdateRequest .cxx_destruct]
+ -[_UIFocusUpdateRequest allowsDeferral]
+ -[_UIFocusUpdateRequest allowsFocusingCurrentItem]
+ -[_UIFocusUpdateRequest allowsOverridingPreferedFocusEnvironments]
+ -[_UIFocusUpdateRequest cacheCurrentFocusSystem]
+ -[_UIFocusUpdateRequest canMergeWithRequest:]
+ -[_UIFocusUpdateRequest copyWithZone:]
+ -[_UIFocusUpdateRequest destinationEnvironment]
+ -[_UIFocusUpdateRequest environment]
+ -[_UIFocusUpdateRequest focusSystem]
+ -[_UIFocusUpdateRequest initWithEnvironment:]
+ -[_UIFocusUpdateRequest initWithFocusSystem:environment:]
+ -[_UIFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:]
+ -[_UIFocusUpdateRequest init]
+ -[_UIFocusUpdateRequest inputDeviceInfo]
+ -[_UIFocusUpdateRequest isFocusRemovalRequest]
+ -[_UIFocusUpdateRequest isMovementRequest]
+ -[_UIFocusUpdateRequest isValidInFocusSystem:]
+ -[_UIFocusUpdateRequest requestByMergingWithRequest:]
+ -[_UIFocusUpdateRequest requestByRedirectingRequestToEnvironment:]
+ -[_UIFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment]
+ -[_UIFocusUpdateRequest requiresEnvironmentValidation]
+ -[_UIFocusUpdateRequest requiresNextFocusedItem]
+ -[_UIFocusUpdateRequest resetsUpdateThrottle]
+ -[_UIFocusUpdateRequest setAllowsDeferral:]
+ -[_UIFocusUpdateRequest setAllowsFocusingCurrentItem:]
+ -[_UIFocusUpdateRequest setAllowsOverridingPreferedFocusEnvironments:]
+ -[_UIFocusUpdateRequest setResetsUpdateThrottle:]
+ -[_UIFocusUpdateRequest setScrollIfNecessary:]
+ -[_UIFocusUpdateRequest setShouldPlayFocusSound:]
+ -[_UIFocusUpdateRequest shouldPerformHapticFeedback]
+ -[_UIFocusUpdateRequest shouldPlayFocusSound]
+ -[_UIFocusUpdateRequest shouldScrollIfNecessary]
+ -[_UIFocusUpdateThrottle .cxx_destruct]
+ -[_UIFocusUpdateThrottle _performScheduledUpdate]
+ -[_UIFocusUpdateThrottle didCreateProgrammaticFocusUpdateContext:]
+ -[_UIFocusUpdateThrottle initWithUpdateHandler:]
+ -[_UIFocusUpdateThrottle reset]
+ -[_UIFocusUpdateThrottle scheduleProgrammaticFocusUpdate]
+ -[_UIFocusUpdateThrottle teardown]
+ -[_UIFocusWeakHelper .cxx_destruct]
+ -[_UIFocusWeakHelper dealloc]
+ -[_UIFocusWeakHelper deallocationBlock]
+ -[_UIFocusWeakHelper initWithDeallocationBlock:]
+ -[_UIFocusWeakHelper invalidate]
+ -[_UIFocusWeakHelper setDeallocationBlock:]
+ -[_UIHostedFocusSystem .cxx_destruct]
+ -[_UIHostedFocusSystem _focusSystemIsValid]
+ -[_UIHostedFocusSystem _hostFocusSystem]
+ -[_UIHostedFocusSystem _initWithHostEnvironment:]
+ -[_UIHostedFocusSystem _isEligibleForFocusInteraction]
+ -[_UIHostedFocusSystem _isEligibleForFocusOcclusion]
+ -[_UIHostedFocusSystem _postsFocusUpdateNotifications]
+ -[_UIHostedFocusSystem _prefersDeferralForFocusUpdateInContext:]
+ -[_UIHostedFocusSystem behavior]
+ -[_UIHostedFocusSystem containsChildOfHostEnvironment:]
+ -[_UIHostedFocusSystem delegateProxy]
+ -[_UIHostedFocusSystem delegate]
+ -[_UIHostedFocusSystem focusItemContainer]
+ -[_UIHostedFocusSystem hostEnvironment]
+ -[_UIHostedFocusSystem itemContainerProxy]
+ -[_UIHostedFocusSystem setDelegate:]
+ -[_UIHostedFocusSystem setDelegateProxy:]
+ -[_UIHostedFocusSystemDelegateProxy .cxx_destruct]
+ -[_UIHostedFocusSystemDelegateProxy _focusSystem:containsChildOfHostEnvironment:]
+ -[_UIHostedFocusSystemDelegateProxy _focusSystem:focusItemsInRect:]
+ -[_UIHostedFocusSystemDelegateProxy delegate]
+ -[_UIHostedFocusSystemDelegateProxy forwardingTargetForSelector:]
+ -[_UIHostedFocusSystemDelegateProxy initWithFocusSystem:delegate:]
+ -[_UIHostedFocusSystemDelegateProxy methodSignatureForSelector:]
+ -[_UIHostedFocusSystemDelegateProxy respondsToSelector:]
+ -[_UIHostedFocusSystemItemContainer .cxx_destruct]
+ -[_UIHostedFocusSystemItemContainer coordinateSpace]
+ -[_UIHostedFocusSystemItemContainer focusItemsInRect:]
+ -[_UIHostedFocusSystemItemContainer focusSystem]
+ -[_UIHostedFocusSystemItemContainer initWithHostedFocusSystem:]
+ -[_UIHostedFocusSystemItemContainer setFocusSystem:]
+ GCC_except_table111
+ _.str.94
+ _.str.97
+ _OBJC_CLASS_$_BSAction
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_UIFocusDebugger
+ _OBJC_CLASS_$_UIFocusMovementAction
+ _OBJC_CLASS_$_UIFocusMovementHint
+ _OBJC_CLASS_$_UIFocusSystem
+ _OBJC_CLASS_$_UIFocusUpdateContext
+ _OBJC_CLASS_$__UIDebugIssue
+ _OBJC_CLASS_$__UIDebugIssueReport
+ _OBJC_CLASS_$__UIDebugIssueReportFormatter
+ _OBJC_CLASS_$__UIDebugLogMessage
+ _OBJC_CLASS_$__UIDebugLogNode
+ _OBJC_CLASS_$__UIDebugLogReport
+ _OBJC_CLASS_$__UIDebugLogReportFormatter
+ _OBJC_CLASS_$__UIDebugLogStack
+ _OBJC_CLASS_$__UIDebugLogStatement
+ _OBJC_CLASS_$__UIDebugReportComponents
+ _OBJC_CLASS_$__UIDebugReportFormatter
+ _OBJC_CLASS_$__UIFocusContainerGuideFallbackItemsContainer
+ _OBJC_CLASS_$__UIFocusContainerGuideImpl
+ _OBJC_CLASS_$__UIFocusContainerGuideRegion
+ _OBJC_CLASS_$__UIFocusDebuggerStringOutput
+ _OBJC_CLASS_$__UIFocusEnvironmentContainerTuple
+ _OBJC_CLASS_$__UIFocusEnvironmentPreferenceCache
+ _OBJC_CLASS_$__UIFocusEnvironmentPreferenceCacheNode
+ _OBJC_CLASS_$__UIFocusEnvironmentPreferenceEnumerationContext
+ _OBJC_CLASS_$__UIFocusEnvironmentPreferenceEnumerator
+ _OBJC_CLASS_$__UIFocusEnvironmentScrollableContainerTuple
+ _OBJC_CLASS_$__UIFocusGroup
+ _OBJC_CLASS_$__UIFocusGroupHistory
+ _OBJC_CLASS_$__UIFocusGroupMap
+ _OBJC_CLASS_$__UIFocusGuideImpl
+ _OBJC_CLASS_$__UIFocusGuideRegion
+ _OBJC_CLASS_$__UIFocusInputDeviceInfo
+ _OBJC_CLASS_$__UIFocusItemDummy
+ _OBJC_CLASS_$__UIFocusItemInfo
+ _OBJC_CLASS_$__UIFocusItemRegion
+ _OBJC_CLASS_$__UIFocusLinearMovementCache
+ _OBJC_CLASS_$__UIFocusLinearMovementSequence
+ _OBJC_CLASS_$__UIFocusMap
+ _OBJC_CLASS_$__UIFocusMapRect
+ _OBJC_CLASS_$__UIFocusMapSearchInfo
+ _OBJC_CLASS_$__UIFocusMapSnapshot
+ _OBJC_CLASS_$__UIFocusMapSnapshotter
+ _OBJC_CLASS_$__UIFocusMovementInfo
+ _OBJC_CLASS_$__UIFocusMovementPerformer
+ _OBJC_CLASS_$__UIFocusMovementRequest
+ _OBJC_CLASS_$__UIFocusNullGroup
+ _OBJC_CLASS_$__UIFocusPromiseItem
+ _OBJC_CLASS_$__UIFocusPromiseRegion
+ _OBJC_CLASS_$__UIFocusRegion
+ _OBJC_CLASS_$__UIFocusRegionContainerProxy
+ _OBJC_CLASS_$__UIFocusRegionEvaluator
+ _OBJC_CLASS_$__UIFocusRegionMovementInfo
+ _OBJC_CLASS_$__UIFocusRegionSearchContextState
+ _OBJC_CLASS_$__UIFocusSearchInfo
+ _OBJC_CLASS_$__UIFocusSpeedBumpRegion
+ _OBJC_CLASS_$__UIFocusTreeLock
+ _OBJC_CLASS_$__UIFocusTreeLockItem
+ _OBJC_CLASS_$__UIFocusUpdateReport
+ _OBJC_CLASS_$__UIFocusUpdateReportFormatter
+ _OBJC_CLASS_$__UIFocusUpdateRequest
+ _OBJC_CLASS_$__UIFocusUpdateThrottle
+ _OBJC_CLASS_$__UIFocusWeakHelper
+ _OBJC_CLASS_$__UIHostedFocusSystem
+ _OBJC_CLASS_$__UIHostedFocusSystemDelegateProxy
+ _OBJC_CLASS_$__UIHostedFocusSystemItemContainer
+ _OBJC_IVAR_$_UIFocusMovementHint._movementDirection
+ _OBJC_IVAR_$_UIFocusMovementHint._rotationAmount
+ _OBJC_IVAR_$_UIFocusMovementHint._translationAmount
+ _OBJC_IVAR_$_UIFocusSystem._appearingFocusEnvironment
+ _OBJC_IVAR_$_UIFocusSystem._behavior
+ _OBJC_IVAR_$_UIFocusSystem._deepestPreferredFocusEnvironment
+ _OBJC_IVAR_$_UIFocusSystem._deepestPreferredFocusableItemCacheForCurrentUpdate
+ _OBJC_IVAR_$_UIFocusSystem._deferredFocusUpdateTarget
+ _OBJC_IVAR_$_UIFocusSystem._delegate
+ _OBJC_IVAR_$_UIFocusSystem._disappearingFocusEnvironment
+ _OBJC_IVAR_$_UIFocusSystem._enabled
+ _OBJC_IVAR_$_UIFocusSystem._flags
+ _OBJC_IVAR_$_UIFocusSystem._focusCasting
+ _OBJC_IVAR_$_UIFocusSystem._focusGroupHistory
+ _OBJC_IVAR_$_UIFocusSystem._focusItemAncestorCache
+ _OBJC_IVAR_$_UIFocusSystem._focusMovementCache
+ _OBJC_IVAR_$_UIFocusSystem._focusedItem
+ _OBJC_IVAR_$_UIFocusSystem._hasSeenFocusedItemDidExpireTimer
+ _OBJC_IVAR_$_UIFocusSystem._movementPerformer
+ _OBJC_IVAR_$_UIFocusSystem._overrideFocusDeferralBehavior
+ _OBJC_IVAR_$_UIFocusSystem._pendingFocusMovementAction
+ _OBJC_IVAR_$_UIFocusSystem._pendingFocusUpdateRequest
+ _OBJC_IVAR_$_UIFocusSystem._previousFocusedItem
+ _OBJC_IVAR_$_UIFocusSystem._treeLock
+ _OBJC_IVAR_$_UIFocusSystem._updateThrottle
+ _OBJC_IVAR_$_UIFocusSystem._waitingForFocusMovementAction
+ _OBJC_IVAR_$_UIFocusUpdateContext._commonAncestorEnvironment
+ _OBJC_IVAR_$_UIFocusUpdateContext._commonEnvironmentScrollableContainer
+ _OBJC_IVAR_$_UIFocusUpdateContext._deferredUpdate
+ _OBJC_IVAR_$_UIFocusUpdateContext._destinationItemInfo
+ _OBJC_IVAR_$_UIFocusUpdateContext._destinationViewDistanceOffscreen
+ _OBJC_IVAR_$_UIFocusUpdateContext._flags
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusBehavior
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusGroupMap
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusMapSearchInfo
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusMovement
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusRedirectedByGuide
+ _OBJC_IVAR_$_UIFocusUpdateContext._focusedGuideImpl
+ _OBJC_IVAR_$_UIFocusUpdateContext._initialDestinationEnvironment
+ _OBJC_IVAR_$_UIFocusUpdateContext._nextFocusedGroupIdentifier
+ _OBJC_IVAR_$_UIFocusUpdateContext._preferredFocusReport
+ _OBJC_IVAR_$_UIFocusUpdateContext._previouslyFocusedGroupIdentifier
+ _OBJC_IVAR_$_UIFocusUpdateContext._request
+ _OBJC_IVAR_$_UIFocusUpdateContext._sourceItemInfo
+ _OBJC_IVAR_$_UIFocusUpdateContext._validationReport
+ _OBJC_IVAR_$__UIDebugIssue._description
+ _OBJC_IVAR_$__UIDebugIssue._prefix
+ _OBJC_IVAR_$__UIDebugIssue._subissueReport
+ _OBJC_IVAR_$__UIDebugIssueReport._mutableIssues
+ _OBJC_IVAR_$__UIDebugLogReport._currentIndentLevel
+ _OBJC_IVAR_$__UIDebugLogReport._fallbackMessagePrefixHandler
+ _OBJC_IVAR_$__UIDebugLogReport._prefixStack
+ _OBJC_IVAR_$__UIDebugLogReport._statements
+ _OBJC_IVAR_$__UIDebugLogStatement._indentLevel
+ _OBJC_IVAR_$__UIDebugLogStatement._prefix
+ _OBJC_IVAR_$__UIDebugLogStatement._text
+ _OBJC_IVAR_$__UIDebugLogStatement._type
+ _OBJC_IVAR_$__UIDebugReportComponents._body
+ _OBJC_IVAR_$__UIDebugReportComponents._footer
+ _OBJC_IVAR_$__UIDebugReportComponents._header
+ _OBJC_IVAR_$__UIDebugReportFormatter._extraBodyIndentLevel
+ _OBJC_IVAR_$__UIDebugReportFormatter._indentLevel
+ _OBJC_IVAR_$__UIDebugReportFormatter._indentString
+ _OBJC_IVAR_$__UIFocusContainerGuideFallbackItemsContainer._childItems
+ _OBJC_IVAR_$__UIFocusContainerGuideFallbackItemsContainer._parentFocusEnvironment
+ _OBJC_IVAR_$__UIFocusContainerGuideImpl._fallbackItemProvider
+ _OBJC_IVAR_$__UIFocusDebuggerStringOutput._outputString
+ _OBJC_IVAR_$__UIFocusEnvironmentContainerTuple._isScrollableContainer
+ _OBJC_IVAR_$__UIFocusEnvironmentContainerTuple._itemContainer
+ _OBJC_IVAR_$__UIFocusEnvironmentContainerTuple._owningEnvironment
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCache._environmentsMap
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCacheNode._childNodes
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCacheNode._environment
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCacheNode._flags
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCacheNode._parentNodes
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceCacheNode._resolvedEnvironment
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._allVisitedEnvironments
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._cachedPreferredEnvironments
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._cachedPrefersNothingFocused
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._debugStack
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._delegate
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._environment
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._focusSystem
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._hasNeverPoppedInPreferredSubtree
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._hasResolvedPreferredFocusEnvironments
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._lastPrimaryPreferredEnvironment
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._preferredEnvironmentsMap
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._preferredSubtree
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._preferredSubtreeEntryPoint
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerationContext._visitedEnvironmentStack
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerator._allowsInferringPreferences
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerator._debugLog
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerator._didVisitAllPreferencesForEnvironmentHandler
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerator._enumerationMode
+ _OBJC_IVAR_$__UIFocusEnvironmentPreferenceEnumerator._shouldInferPreferenceForEnvironmentHandler
+ _OBJC_IVAR_$__UIFocusEnvironmentScrollableContainerTuple._owningEnvironment
+ _OBJC_IVAR_$__UIFocusEnvironmentScrollableContainerTuple._scrollableContainer
+ _OBJC_IVAR_$__UIFocusGroup._boundingBox
+ _OBJC_IVAR_$__UIFocusGroup._childGroups
+ _OBJC_IVAR_$__UIFocusGroup._coordinateSpace
+ _OBJC_IVAR_$__UIFocusGroup._flags
+ _OBJC_IVAR_$__UIFocusGroup._identifier
+ _OBJC_IVAR_$__UIFocusGroup._items
+ _OBJC_IVAR_$__UIFocusGroup._owningEnvironment
+ _OBJC_IVAR_$__UIFocusGroup._parentGroup
+ _OBJC_IVAR_$__UIFocusGroup._primaryItem
+ _OBJC_IVAR_$__UIFocusGroup._primaryRect
+ _OBJC_IVAR_$__UIFocusGroupHistory._groupToItemMap
+ _OBJC_IVAR_$__UIFocusGroupMap._coordinateSpace
+ _OBJC_IVAR_$__UIFocusGroupMap._environmentToGroupMap
+ _OBJC_IVAR_$__UIFocusGroupMap._focusGroups
+ _OBJC_IVAR_$__UIFocusGroupMap._identifierToGroupMap
+ _OBJC_IVAR_$__UIFocusGroupMap._identifierToPrimaryItemMap
+ _OBJC_IVAR_$__UIFocusGroupMap._nullGroup
+ _OBJC_IVAR_$__UIFocusGroupMap._standInItemsMap
+ _OBJC_IVAR_$__UIFocusGuideImpl._delegate
+ _OBJC_IVAR_$__UIFocusGuideImpl._flags
+ _OBJC_IVAR_$__UIFocusGuideImpl._owningItem
+ _OBJC_IVAR_$__UIFocusGuideImpl._preferredFocusEnvironments
+ _OBJC_IVAR_$__UIFocusInputDeviceInfo._senderID
+ _OBJC_IVAR_$__UIFocusItemDummy._frame
+ _OBJC_IVAR_$__UIFocusItemDummy._parentFocusEnvironment
+ _OBJC_IVAR_$__UIFocusItemInfo._ancestorEnvironmentScrollableContainers
+ _OBJC_IVAR_$__UIFocusItemInfo._flags
+ _OBJC_IVAR_$__UIFocusItemInfo._focusMovementFlippedHorizontally
+ _OBJC_IVAR_$__UIFocusItemInfo._focusTouchSensitivityStyle
+ _OBJC_IVAR_$__UIFocusItemInfo._focusedRegion
+ _OBJC_IVAR_$__UIFocusItemInfo._inheritedFocusMovementStyle
+ _OBJC_IVAR_$__UIFocusItemInfo._item
+ _OBJC_IVAR_$__UIFocusItemInfo._rotaryFocusMovementAxis
+ _OBJC_IVAR_$__UIFocusLinearMovementCache._cooldownThreshold
+ _OBJC_IVAR_$__UIFocusLinearMovementCache._flags
+ _OBJC_IVAR_$__UIFocusLinearMovementCache._lastUpdate
+ _OBJC_IVAR_$__UIFocusLinearMovementCache._linearItems
+ _OBJC_IVAR_$__UIFocusLinearMovementCache._parentEnvironments
+ _OBJC_IVAR_$__UIFocusLinearMovementSequence._items
+ _OBJC_IVAR_$__UIFocusLinearMovementSequence._looping
+ _OBJC_IVAR_$__UIFocusLinearMovementSequence._restrictEnteringSequence
+ _OBJC_IVAR_$__UIFocusMap._coordinateSpace
+ _OBJC_IVAR_$__UIFocusMap._defaultItemSearchInfo
+ _OBJC_IVAR_$__UIFocusMap._focusGroupMap
+ _OBJC_IVAR_$__UIFocusMap._focusMovementSearchInfo
+ _OBJC_IVAR_$__UIFocusMap._focusSystem
+ _OBJC_IVAR_$__UIFocusMap._ignoresRootContainerClippingRect
+ _OBJC_IVAR_$__UIFocusMap._minimumSearchArea
+ _OBJC_IVAR_$__UIFocusMap._minimumSearchAreaIsEmpty
+ _OBJC_IVAR_$__UIFocusMap._needsSearchInfo
+ _OBJC_IVAR_$__UIFocusMap._rootContainer
+ _OBJC_IVAR_$__UIFocusMap._rootContainerProxy
+ _OBJC_IVAR_$__UIFocusMap._searchInfo
+ _OBJC_IVAR_$__UIFocusMap._trackingSearchInfo
+ _OBJC_IVAR_$__UIFocusMapRect._coordinateSpace
+ _OBJC_IVAR_$__UIFocusMapRect._frame
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._didFindFocusBlockingBoundary
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._focusGroupMap
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._hasOnlyStaticContent
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._linearSortedFocusItems
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._mutableDestinationRegions
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._mutableSnapshots
+ _OBJC_IVAR_$__UIFocusMapSearchInfo._searchInfo
+ _OBJC_IVAR_$__UIFocusMapSnapshot._eligibleEnvironments
+ _OBJC_IVAR_$__UIFocusMapSnapshot._filteredOriginalRegions
+ _OBJC_IVAR_$__UIFocusMapSnapshot._flags
+ _OBJC_IVAR_$__UIFocusMapSnapshot._focusSystem
+ _OBJC_IVAR_$__UIFocusMapSnapshot._focusedRegion
+ _OBJC_IVAR_$__UIFocusMapSnapshot._ineligibleEnvironments
+ _OBJC_IVAR_$__UIFocusMapSnapshot._mapArea
+ _OBJC_IVAR_$__UIFocusMapSnapshot._movementInfo
+ _OBJC_IVAR_$__UIFocusMapSnapshot._mutableUnoccludedRegions
+ _OBJC_IVAR_$__UIFocusMapSnapshot._regionFrameCache
+ _OBJC_IVAR_$__UIFocusMapSnapshot._regionToFocusItemCache
+ _OBJC_IVAR_$__UIFocusMapSnapshot._regionToOccludingRegionsMap
+ _OBJC_IVAR_$__UIFocusMapSnapshot._regions
+ _OBJC_IVAR_$__UIFocusMapSnapshot._regionsContainer
+ _OBJC_IVAR_$__UIFocusMapSnapshot._rootContainer
+ _OBJC_IVAR_$__UIFocusMapSnapshot._searchArea
+ _OBJC_IVAR_$__UIFocusMapSnapshot._searchInfo
+ _OBJC_IVAR_$__UIFocusMapSnapshot._stateStack
+ _OBJC_IVAR_$__UIFocusMapSnapshot._subregionToRegionMap
+ _OBJC_IVAR_$__UIFocusMapSnapshot._uncachableEnvironments
+ _OBJC_IVAR_$__UIFocusMapSnapshot._visitedRegionContainers
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._clipToSnapshotRect
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._coordinateSpace
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._focusSystem
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._focusedRegion
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._ignoresRootContainerClippingRect
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._movementInfo
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._regionsContainer
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._rootContainer
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._searchInfo
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._snapshotFrame
+ _OBJC_IVAR_$__UIFocusMapSnapshotter._snapshotFrameIsEmpty
+ _OBJC_IVAR_$__UIFocusMovementInfo._fallbackMovementOriginatingFrame
+ _OBJC_IVAR_$__UIFocusMovementInfo._groupFilter
+ _OBJC_IVAR_$__UIFocusMovementInfo._heading
+ _OBJC_IVAR_$__UIFocusMovementInfo._inputType
+ _OBJC_IVAR_$__UIFocusMovementInfo._isInitialMovement
+ _OBJC_IVAR_$__UIFocusMovementInfo._isVelocityBased
+ _OBJC_IVAR_$__UIFocusMovementInfo._linearHeading
+ _OBJC_IVAR_$__UIFocusMovementInfo._looping
+ _OBJC_IVAR_$__UIFocusMovementInfo._shouldLoadScrollableContainer
+ _OBJC_IVAR_$__UIFocusMovementInfo._velocity
+ _OBJC_IVAR_$__UIFocusMovementPerformer._delegate
+ _OBJC_IVAR_$__UIFocusMovementRequest._focusSystem
+ _OBJC_IVAR_$__UIFocusMovementRequest._focusedItemInfo
+ _OBJC_IVAR_$__UIFocusMovementRequest._inputDeviceInfo
+ _OBJC_IVAR_$__UIFocusMovementRequest._movementInfo
+ _OBJC_IVAR_$__UIFocusMovementRequest._overridesDeferredFocusUpdate
+ _OBJC_IVAR_$__UIFocusMovementRequest._searchInfo
+ _OBJC_IVAR_$__UIFocusMovementRequest._shouldPerformHapticFeedback
+ _OBJC_IVAR_$__UIFocusPromiseItem._debugIdentifier
+ _OBJC_IVAR_$__UIFocusPromiseItem._flags
+ _OBJC_IVAR_$__UIFocusPromiseItem._frame
+ _OBJC_IVAR_$__UIFocusPromiseItem._fulfilledItem
+ _OBJC_IVAR_$__UIFocusPromiseItem._fulfillmentHandler
+ _OBJC_IVAR_$__UIFocusPromiseItem._parentFocusEnvironment
+ _OBJC_IVAR_$__UIFocusPromiseRegion._fullfillmentCount
+ _OBJC_IVAR_$__UIFocusRegion._regionCoordinateSpace
+ _OBJC_IVAR_$__UIFocusRegion._regionFrame
+ _OBJC_IVAR_$__UIFocusRegionContainerProxy._allowsLazyLoading
+ _OBJC_IVAR_$__UIFocusRegionContainerProxy._environmentContainer
+ _OBJC_IVAR_$__UIFocusRegionContainerProxy._shouldCreateRegionForGuideBehavior
+ _OBJC_IVAR_$__UIFocusRegionContainerProxy._shouldCreateRegionForOwningItem
+ _OBJC_IVAR_$__UIFocusRegionMovementInfo._originatingHeading
+ _OBJC_IVAR_$__UIFocusRegionSearchContextState._clippingRect
+ _OBJC_IVAR_$__UIFocusRegionSearchContextState._regionContainer
+ _OBJC_IVAR_$__UIFocusRegionSearchContextState._regionContainerFocusSystem
+ _OBJC_IVAR_$__UIFocusSearchInfo._evaluator
+ _OBJC_IVAR_$__UIFocusSearchInfo._forceFocusToLeaveContainer
+ _OBJC_IVAR_$__UIFocusSearchInfo._treatFocusableItemAsLeaf
+ _OBJC_IVAR_$__UIFocusSpeedBumpRegion._speedBumpEdges
+ _OBJC_IVAR_$__UIFocusTreeLock._lockedEnvironments
+ _OBJC_IVAR_$__UIFocusTreeLock._validationTimer
+ _OBJC_IVAR_$__UIFocusTreeLockItem._didCleanup
+ _OBJC_IVAR_$__UIFocusTreeLockItem._didSoftAssert
+ _OBJC_IVAR_$__UIFocusTreeLockItem._environment
+ _OBJC_IVAR_$__UIFocusTreeLockItem._environmentDescription
+ _OBJC_IVAR_$__UIFocusTreeLockItem._finalUnlockHandler
+ _OBJC_IVAR_$__UIFocusTreeLockItem._lockCallStackSymbols
+ _OBJC_IVAR_$__UIFocusTreeLockItem._lockCount
+ _OBJC_IVAR_$__UIFocusTreeLockItem._lockTime
+ _OBJC_IVAR_$__UIFocusTreeLockItem._unlockCallStackSymbols
+ _OBJC_IVAR_$__UIFocusTreeLockItem._unsafeEnvironment
+ _OBJC_IVAR_$__UIFocusUpdateReport._context
+ _OBJC_IVAR_$__UIFocusUpdateReport._focusSystem
+ _OBJC_IVAR_$__UIFocusUpdateRequest._allowsDeferral
+ _OBJC_IVAR_$__UIFocusUpdateRequest._allowsFocusingCurrentItem
+ _OBJC_IVAR_$__UIFocusUpdateRequest._allowsOverridingPreferedFocusEnvironments
+ _OBJC_IVAR_$__UIFocusUpdateRequest._destinationEnvironment
+ _OBJC_IVAR_$__UIFocusUpdateRequest._environment
+ _OBJC_IVAR_$__UIFocusUpdateRequest._focusSystem
+ _OBJC_IVAR_$__UIFocusUpdateRequest._isFocusRemovalRequest
+ _OBJC_IVAR_$__UIFocusUpdateRequest._resetsUpdateThrottle
+ _OBJC_IVAR_$__UIFocusUpdateRequest._scrollIfNecessary
+ _OBJC_IVAR_$__UIFocusUpdateRequest._shouldPlayFocusSound
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._currentTimeout
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._lastUpdate
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._nilUpdateCount
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._updateHandler
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._updateIsScheduled
+ _OBJC_IVAR_$__UIFocusUpdateThrottle._updateTimer
+ _OBJC_IVAR_$__UIFocusWeakHelper._deallocationBlock
+ _OBJC_IVAR_$__UIHostedFocusSystemDelegateProxy._delegate
+ _OBJC_IVAR_$__UIHostedFocusSystemDelegateProxy._focusSystem
+ _OBJC_IVAR_$__UIHostedFocusSystemItemContainer._focusSystem
+ _OBJC_METACLASS_$_BSAction
+ _OBJC_METACLASS_$_UIFocusDebugger
+ _OBJC_METACLASS_$_UIFocusMovementAction
+ _OBJC_METACLASS_$_UIFocusMovementHint
+ _OBJC_METACLASS_$_UIFocusSystem
+ _OBJC_METACLASS_$_UIFocusUpdateContext
+ _OBJC_METACLASS_$__UIDebugIssue
+ _OBJC_METACLASS_$__UIDebugIssueReport
+ _OBJC_METACLASS_$__UIDebugIssueReportFormatter
+ _OBJC_METACLASS_$__UIDebugLogReport
+ _OBJC_METACLASS_$__UIDebugLogReportFormatter
+ _OBJC_METACLASS_$__UIDebugLogStatement
+ _OBJC_METACLASS_$__UIDebugReportComponents
+ _OBJC_METACLASS_$__UIDebugReportFormatter
+ _OBJC_METACLASS_$__UIFocusContainerGuideFallbackItemsContainer
+ _OBJC_METACLASS_$__UIFocusContainerGuideImpl
+ _OBJC_METACLASS_$__UIFocusContainerGuideRegion
+ _OBJC_METACLASS_$__UIFocusDebuggerStringOutput
+ _OBJC_METACLASS_$__UIFocusEnvironmentContainerTuple
+ _OBJC_METACLASS_$__UIFocusEnvironmentPreferenceCache
+ _OBJC_METACLASS_$__UIFocusEnvironmentPreferenceCacheNode
+ _OBJC_METACLASS_$__UIFocusEnvironmentPreferenceEnumerationContext
+ _OBJC_METACLASS_$__UIFocusEnvironmentPreferenceEnumerator
+ _OBJC_METACLASS_$__UIFocusEnvironmentScrollableContainerTuple
+ _OBJC_METACLASS_$__UIFocusGroup
+ _OBJC_METACLASS_$__UIFocusGroupHistory
+ _OBJC_METACLASS_$__UIFocusGroupMap
+ _OBJC_METACLASS_$__UIFocusGuideImpl
+ _OBJC_METACLASS_$__UIFocusGuideRegion
+ _OBJC_METACLASS_$__UIFocusInputDeviceInfo
+ _OBJC_METACLASS_$__UIFocusItemDummy
+ _OBJC_METACLASS_$__UIFocusItemInfo
+ _OBJC_METACLASS_$__UIFocusItemRegion
+ _OBJC_METACLASS_$__UIFocusLinearMovementCache
+ _OBJC_METACLASS_$__UIFocusLinearMovementSequence
+ _OBJC_METACLASS_$__UIFocusMap
+ _OBJC_METACLASS_$__UIFocusMapRect
+ _OBJC_METACLASS_$__UIFocusMapSearchInfo
+ _OBJC_METACLASS_$__UIFocusMapSnapshot
+ _OBJC_METACLASS_$__UIFocusMapSnapshotter
+ _OBJC_METACLASS_$__UIFocusMovementInfo
+ _OBJC_METACLASS_$__UIFocusMovementPerformer
+ _OBJC_METACLASS_$__UIFocusMovementRequest
+ _OBJC_METACLASS_$__UIFocusNullGroup
+ _OBJC_METACLASS_$__UIFocusPromiseItem
+ _OBJC_METACLASS_$__UIFocusPromiseRegion
+ _OBJC_METACLASS_$__UIFocusRegion
+ _OBJC_METACLASS_$__UIFocusRegionContainerProxy
+ _OBJC_METACLASS_$__UIFocusRegionEvaluator
+ _OBJC_METACLASS_$__UIFocusRegionMovementInfo
+ _OBJC_METACLASS_$__UIFocusRegionSearchContextState
+ _OBJC_METACLASS_$__UIFocusSearchInfo
+ _OBJC_METACLASS_$__UIFocusSpeedBumpRegion
+ _OBJC_METACLASS_$__UIFocusTreeLock
+ _OBJC_METACLASS_$__UIFocusTreeLockItem
+ _OBJC_METACLASS_$__UIFocusUpdateReport
+ _OBJC_METACLASS_$__UIFocusUpdateReportFormatter
+ _OBJC_METACLASS_$__UIFocusUpdateRequest
+ _OBJC_METACLASS_$__UIFocusUpdateThrottle
+ _OBJC_METACLASS_$__UIFocusWeakHelper
+ _OBJC_METACLASS_$__UIHostedFocusSystem
+ _OBJC_METACLASS_$__UIHostedFocusSystemDelegateProxy
+ _OBJC_METACLASS_$__UIHostedFocusSystemItemContainer
+ _UIFocusDidUpdateNotification
+ _UIFocusGetSensitivitySetting
+ _UIFocusMovementDidFailNotification
+ _UIFocusSetSensitivitySetting
+ _UIFocusUpdateAnimationCoordinatorKey
+ _UIFocusUpdateContextKey
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_UIFocusGeometryKeyedCoding
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$__UIFocusRegionContainerProxy
+ __OBJC_$_CATEGORY_NSCoder_$_UIFocusGeometryKeyedCoding
+ __OBJC_$_CATEGORY_NSObject_$__UIFocusRegionContainerProxy
+ __OBJC_$_CLASS_METHODS_UIFocusDebugger
+ __OBJC_$_CLASS_METHODS_UIFocusSystem
+ __OBJC_$_CLASS_METHODS_UIFocusUpdateContext
+ __OBJC_$_CLASS_METHODS__UIDebugIssue
+ __OBJC_$_CLASS_METHODS__UIDebugReportFormatter
+ __OBJC_$_CLASS_METHODS__UIFocusDebuggerStringOutput
+ __OBJC_$_CLASS_METHODS__UIFocusEnvironmentContainerTuple
+ __OBJC_$_CLASS_METHODS__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_$_CLASS_METHODS__UIFocusGroup
+ __OBJC_$_CLASS_METHODS__UIFocusInputDeviceInfo
+ __OBJC_$_CLASS_METHODS__UIFocusItemInfo
+ __OBJC_$_CLASS_METHODS__UIFocusLinearMovementSequence
+ __OBJC_$_CLASS_METHODS__UIFocusMovementInfo
+ __OBJC_$_CLASS_METHODS__UIFocusRegionEvaluator
+ __OBJC_$_CLASS_METHODS__UIFocusRegionMovementInfo
+ __OBJC_$_CLASS_METHODS__UIFocusRegionSearchContextState
+ __OBJC_$_CLASS_METHODS__UIFocusSearchInfo
+ __OBJC_$_CLASS_METHODS__UIFocusUpdateRequest
+ __OBJC_$_CLASS_PROP_LIST_UIFocusSystem
+ __OBJC_$_CLASS_PROP_LIST_UIFocusUpdateContext
+ __OBJC_$_INSTANCE_METHODS_UIFocusMovementAction
+ __OBJC_$_INSTANCE_METHODS_UIFocusMovementHint
+ __OBJC_$_INSTANCE_METHODS_UIFocusSystem
+ __OBJC_$_INSTANCE_METHODS_UIFocusUpdateContext
+ __OBJC_$_INSTANCE_METHODS__UIDebugIssue
+ __OBJC_$_INSTANCE_METHODS__UIDebugIssueReport
+ __OBJC_$_INSTANCE_METHODS__UIDebugIssueReportFormatter
+ __OBJC_$_INSTANCE_METHODS__UIDebugLogReport
+ __OBJC_$_INSTANCE_METHODS__UIDebugLogReportFormatter
+ __OBJC_$_INSTANCE_METHODS__UIDebugLogStatement
+ __OBJC_$_INSTANCE_METHODS__UIDebugReportComponents
+ __OBJC_$_INSTANCE_METHODS__UIDebugReportFormatter
+ __OBJC_$_INSTANCE_METHODS__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_$_INSTANCE_METHODS__UIFocusContainerGuideImpl
+ __OBJC_$_INSTANCE_METHODS__UIFocusContainerGuideRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusDebuggerStringOutput
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentContainerTuple
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentPreferenceCache
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentPreferenceCacheNode
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_$_INSTANCE_METHODS__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_$_INSTANCE_METHODS__UIFocusGroup
+ __OBJC_$_INSTANCE_METHODS__UIFocusGroupHistory
+ __OBJC_$_INSTANCE_METHODS__UIFocusGroupMap
+ __OBJC_$_INSTANCE_METHODS__UIFocusGuideImpl
+ __OBJC_$_INSTANCE_METHODS__UIFocusGuideRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusInputDeviceInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusItemDummy
+ __OBJC_$_INSTANCE_METHODS__UIFocusItemInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusItemRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusLinearMovementCache
+ __OBJC_$_INSTANCE_METHODS__UIFocusLinearMovementSequence
+ __OBJC_$_INSTANCE_METHODS__UIFocusMap
+ __OBJC_$_INSTANCE_METHODS__UIFocusMapRect
+ __OBJC_$_INSTANCE_METHODS__UIFocusMapSearchInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusMapSnapshot
+ __OBJC_$_INSTANCE_METHODS__UIFocusMapSnapshotter
+ __OBJC_$_INSTANCE_METHODS__UIFocusMovementInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusMovementPerformer
+ __OBJC_$_INSTANCE_METHODS__UIFocusMovementRequest
+ __OBJC_$_INSTANCE_METHODS__UIFocusNullGroup
+ __OBJC_$_INSTANCE_METHODS__UIFocusPromiseItem
+ __OBJC_$_INSTANCE_METHODS__UIFocusPromiseRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusRegionContainerProxy
+ __OBJC_$_INSTANCE_METHODS__UIFocusRegionMovementInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusRegionSearchContextState
+ __OBJC_$_INSTANCE_METHODS__UIFocusSearchInfo
+ __OBJC_$_INSTANCE_METHODS__UIFocusSpeedBumpRegion
+ __OBJC_$_INSTANCE_METHODS__UIFocusTreeLock
+ __OBJC_$_INSTANCE_METHODS__UIFocusTreeLockItem
+ __OBJC_$_INSTANCE_METHODS__UIFocusUpdateReport
+ __OBJC_$_INSTANCE_METHODS__UIFocusUpdateReportFormatter
+ __OBJC_$_INSTANCE_METHODS__UIFocusUpdateRequest
+ __OBJC_$_INSTANCE_METHODS__UIFocusUpdateThrottle
+ __OBJC_$_INSTANCE_METHODS__UIFocusWeakHelper
+ __OBJC_$_INSTANCE_METHODS__UIHostedFocusSystem
+ __OBJC_$_INSTANCE_METHODS__UIHostedFocusSystemDelegateProxy
+ __OBJC_$_INSTANCE_METHODS__UIHostedFocusSystemItemContainer
+ __OBJC_$_INSTANCE_VARIABLES_UIFocusMovementHint
+ __OBJC_$_INSTANCE_VARIABLES_UIFocusSystem
+ __OBJC_$_INSTANCE_VARIABLES_UIFocusUpdateContext
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugIssue
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugIssueReport
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugIssueReportFormatter
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugLogReport
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugLogStatement
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugReportComponents
+ __OBJC_$_INSTANCE_VARIABLES__UIDebugReportFormatter
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusContainerGuideImpl
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusContainerGuideRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusDebuggerStringOutput
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentContainerTuple
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentPreferenceCache
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentPreferenceCacheNode
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusGroup
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusGroupHistory
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusGroupMap
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusGuideImpl
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusGuideRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusInputDeviceInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusItemDummy
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusItemInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusItemRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusLinearMovementCache
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusLinearMovementSequence
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMap
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMapRect
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMapSearchInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMapSnapshot
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMapSnapshotter
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMovementInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMovementPerformer
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusMovementRequest
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusPromiseItem
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusPromiseRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusRegionContainerProxy
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusRegionMovementInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusRegionSearchContextState
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusSearchInfo
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusSpeedBumpRegion
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusTreeLock
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusTreeLockItem
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusUpdateReport
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusUpdateRequest
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusUpdateThrottle
+ __OBJC_$_INSTANCE_VARIABLES__UIFocusWeakHelper
+ __OBJC_$_INSTANCE_VARIABLES__UIHostedFocusSystem
+ __OBJC_$_INSTANCE_VARIABLES__UIHostedFocusSystemDelegateProxy
+ __OBJC_$_INSTANCE_VARIABLES__UIHostedFocusSystemItemContainer
+ __OBJC_$_PROP_LIST_UIFocusEnvironment
+ __OBJC_$_PROP_LIST_UIFocusItem
+ __OBJC_$_PROP_LIST_UIFocusItemContainer
+ __OBJC_$_PROP_LIST_UIFocusItemScrollableContainer
+ __OBJC_$_PROP_LIST_UIFocusMovementAction
+ __OBJC_$_PROP_LIST_UIFocusMovementHint
+ __OBJC_$_PROP_LIST_UIFocusSystem
+ __OBJC_$_PROP_LIST_UIFocusUpdateContext
+ __OBJC_$_PROP_LIST__UIDebugIssue
+ __OBJC_$_PROP_LIST__UIDebugIssueReport
+ __OBJC_$_PROP_LIST__UIDebugIssueReportFormatter
+ __OBJC_$_PROP_LIST__UIDebugLogReport
+ __OBJC_$_PROP_LIST__UIDebugLogStatement
+ __OBJC_$_PROP_LIST__UIDebugReportComponents
+ __OBJC_$_PROP_LIST__UIDebugReportFormatter
+ __OBJC_$_PROP_LIST__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_$_PROP_LIST__UIFocusContainerGuideImpl
+ __OBJC_$_PROP_LIST__UIFocusContainerGuideRegion
+ __OBJC_$_PROP_LIST__UIFocusDebuggerStringOutput
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentContainerTuple
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentInternal
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPreferenceCache
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPreferenceCacheNode
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPreferenceEnumerationContext.158
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentPrivate
+ __OBJC_$_PROP_LIST__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_$_PROP_LIST__UIFocusGroup
+ __OBJC_$_PROP_LIST__UIFocusGroupMap
+ __OBJC_$_PROP_LIST__UIFocusGuideImpl
+ __OBJC_$_PROP_LIST__UIFocusGuideRegion
+ __OBJC_$_PROP_LIST__UIFocusGuideRegionDelegate
+ __OBJC_$_PROP_LIST__UIFocusInputDeviceInfo
+ __OBJC_$_PROP_LIST__UIFocusItemDummy
+ __OBJC_$_PROP_LIST__UIFocusItemInfo
+ __OBJC_$_PROP_LIST__UIFocusItemRegion
+ __OBJC_$_PROP_LIST__UIFocusLinearMovementSequence
+ __OBJC_$_PROP_LIST__UIFocusMap
+ __OBJC_$_PROP_LIST__UIFocusMapArea
+ __OBJC_$_PROP_LIST__UIFocusMapRect
+ __OBJC_$_PROP_LIST__UIFocusMapSearchInfo
+ __OBJC_$_PROP_LIST__UIFocusMapSnapshot
+ __OBJC_$_PROP_LIST__UIFocusMapSnapshotter
+ __OBJC_$_PROP_LIST__UIFocusMovementInfo
+ __OBJC_$_PROP_LIST__UIFocusMovementPerformer
+ __OBJC_$_PROP_LIST__UIFocusMovementRequest
+ __OBJC_$_PROP_LIST__UIFocusPromiseItem
+ __OBJC_$_PROP_LIST__UIFocusPromiseRegion
+ __OBJC_$_PROP_LIST__UIFocusRegion
+ __OBJC_$_PROP_LIST__UIFocusRegionContainerProxy
+ __OBJC_$_PROP_LIST__UIFocusRegionMovementInfo
+ __OBJC_$_PROP_LIST__UIFocusRegionSearchContext
+ __OBJC_$_PROP_LIST__UIFocusRegionSearchContextState
+ __OBJC_$_PROP_LIST__UIFocusSearchInfo
+ __OBJC_$_PROP_LIST__UIFocusSpeedBumpRegion
+ __OBJC_$_PROP_LIST__UIFocusTreeLock
+ __OBJC_$_PROP_LIST__UIFocusTreeLockItem
+ __OBJC_$_PROP_LIST__UIFocusUpdateReport
+ __OBJC_$_PROP_LIST__UIFocusUpdateRequest
+ __OBJC_$_PROP_LIST__UIFocusUpdateRequesting
+ __OBJC_$_PROP_LIST__UIFocusWeakHelper
+ __OBJC_$_PROP_LIST__UIHostedFocusSystem
+ __OBJC_$_PROP_LIST__UIHostedFocusSystemDelegateProxy
+ __OBJC_$_PROP_LIST__UIHostedFocusSystemItemContainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIFocusItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIFocusEnvironmentInternal
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIFocusEnvironmentPlatformSupport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIFocusEnvironmentPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIFocusGuideRegionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIFocusSystemDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIFocusItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIFocusItemContainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIFocusItemScrollableContainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIDebugIssueReporting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusEnvironmentPreferenceEnumerationContextDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusMapArea
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusMovementPerformerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusRegionContainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusRegionSearchContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIFocusUpdateRequesting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIHostedFocusSystemDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIFocusItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIFocusItemContainer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIFocusItemScrollableContainer
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIDebugIssueReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusEnvironmentInternal
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusEnvironmentPlatformSupport
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusEnvironmentPreferenceEnumerationContextDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusEnvironmentPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusGuideRegionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusMapArea
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusMovementPerformerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusRegionContainer
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusRegionSearchContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusSystemDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIFocusUpdateRequesting
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UIHostedFocusSystemDelegate
+ __OBJC_$_PROTOCOL_REFS_UIFocusDebuggerOutput
+ __OBJC_$_PROTOCOL_REFS_UIFocusEnvironment
+ __OBJC_$_PROTOCOL_REFS_UIFocusItem
+ __OBJC_$_PROTOCOL_REFS_UIFocusItemContainer
+ __OBJC_$_PROTOCOL_REFS_UIFocusItemScrollableContainer
+ __OBJC_$_PROTOCOL_REFS__UIDebugIssueReporting
+ __OBJC_$_PROTOCOL_REFS__UIFocusEnvironmentInternal
+ __OBJC_$_PROTOCOL_REFS__UIFocusEnvironmentPlatformSupport
+ __OBJC_$_PROTOCOL_REFS__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_$_PROTOCOL_REFS__UIFocusEnvironmentPreferenceEnumerationContextDelegate
+ __OBJC_$_PROTOCOL_REFS__UIFocusEnvironmentPrivate
+ __OBJC_$_PROTOCOL_REFS__UIFocusGuideRegionDelegate
+ __OBJC_$_PROTOCOL_REFS__UIFocusMapArea
+ __OBJC_$_PROTOCOL_REFS__UIFocusMovementPerformerDelegate
+ __OBJC_$_PROTOCOL_REFS__UIFocusRegionContainer
+ __OBJC_$_PROTOCOL_REFS__UIFocusRegionSearchContext
+ __OBJC_$_PROTOCOL_REFS__UIFocusSystemDelegate
+ __OBJC_$_PROTOCOL_REFS__UIFocusUpdateRequesting
+ __OBJC_$_PROTOCOL_REFS__UIHostedFocusSystemDelegate
+ __OBJC_CLASS_PROTOCOLS_$_UIFocusMovementHint
+ __OBJC_CLASS_PROTOCOLS_$_UIFocusSystem
+ __OBJC_CLASS_PROTOCOLS_$__UIDebugIssue
+ __OBJC_CLASS_PROTOCOLS_$__UIDebugIssueReport
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusDebuggerStringOutput
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusGroupMap
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusGuideImpl
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusInputDeviceInfo
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusItemDummy
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusItemInfo
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusMapRect
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusMapSnapshot
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusMovementInfo
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusMovementRequest
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusPromiseItem
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusRegionContainerProxy
+ __OBJC_CLASS_PROTOCOLS_$__UIFocusUpdateRequest
+ __OBJC_CLASS_PROTOCOLS_$__UIHostedFocusSystemDelegateProxy
+ __OBJC_CLASS_PROTOCOLS_$__UIHostedFocusSystemItemContainer
+ __OBJC_CLASS_RO_$_UIFocusDebugger
+ __OBJC_CLASS_RO_$_UIFocusMovementAction
+ __OBJC_CLASS_RO_$_UIFocusMovementHint
+ __OBJC_CLASS_RO_$_UIFocusSystem
+ __OBJC_CLASS_RO_$_UIFocusUpdateContext
+ __OBJC_CLASS_RO_$__UIDebugIssue
+ __OBJC_CLASS_RO_$__UIDebugIssueReport
+ __OBJC_CLASS_RO_$__UIDebugIssueReportFormatter
+ __OBJC_CLASS_RO_$__UIDebugLogReport
+ __OBJC_CLASS_RO_$__UIDebugLogReportFormatter
+ __OBJC_CLASS_RO_$__UIDebugLogStatement
+ __OBJC_CLASS_RO_$__UIDebugReportComponents
+ __OBJC_CLASS_RO_$__UIDebugReportFormatter
+ __OBJC_CLASS_RO_$__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_CLASS_RO_$__UIFocusContainerGuideImpl
+ __OBJC_CLASS_RO_$__UIFocusContainerGuideRegion
+ __OBJC_CLASS_RO_$__UIFocusDebuggerStringOutput
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentContainerTuple
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentPreferenceCache
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentPreferenceCacheNode
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_CLASS_RO_$__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_CLASS_RO_$__UIFocusGroup
+ __OBJC_CLASS_RO_$__UIFocusGroupHistory
+ __OBJC_CLASS_RO_$__UIFocusGroupMap
+ __OBJC_CLASS_RO_$__UIFocusGuideImpl
+ __OBJC_CLASS_RO_$__UIFocusGuideRegion
+ __OBJC_CLASS_RO_$__UIFocusInputDeviceInfo
+ __OBJC_CLASS_RO_$__UIFocusItemDummy
+ __OBJC_CLASS_RO_$__UIFocusItemInfo
+ __OBJC_CLASS_RO_$__UIFocusItemRegion
+ __OBJC_CLASS_RO_$__UIFocusLinearMovementCache
+ __OBJC_CLASS_RO_$__UIFocusLinearMovementSequence
+ __OBJC_CLASS_RO_$__UIFocusMap
+ __OBJC_CLASS_RO_$__UIFocusMapRect
+ __OBJC_CLASS_RO_$__UIFocusMapSearchInfo
+ __OBJC_CLASS_RO_$__UIFocusMapSnapshot
+ __OBJC_CLASS_RO_$__UIFocusMapSnapshotter
+ __OBJC_CLASS_RO_$__UIFocusMovementInfo
+ __OBJC_CLASS_RO_$__UIFocusMovementPerformer
+ __OBJC_CLASS_RO_$__UIFocusMovementRequest
+ __OBJC_CLASS_RO_$__UIFocusNullGroup
+ __OBJC_CLASS_RO_$__UIFocusPromiseItem
+ __OBJC_CLASS_RO_$__UIFocusPromiseRegion
+ __OBJC_CLASS_RO_$__UIFocusRegion
+ __OBJC_CLASS_RO_$__UIFocusRegionContainerProxy
+ __OBJC_CLASS_RO_$__UIFocusRegionEvaluator
+ __OBJC_CLASS_RO_$__UIFocusRegionMovementInfo
+ __OBJC_CLASS_RO_$__UIFocusRegionSearchContextState
+ __OBJC_CLASS_RO_$__UIFocusSearchInfo
+ __OBJC_CLASS_RO_$__UIFocusSpeedBumpRegion
+ __OBJC_CLASS_RO_$__UIFocusTreeLock
+ __OBJC_CLASS_RO_$__UIFocusTreeLockItem
+ __OBJC_CLASS_RO_$__UIFocusUpdateReport
+ __OBJC_CLASS_RO_$__UIFocusUpdateReportFormatter
+ __OBJC_CLASS_RO_$__UIFocusUpdateRequest
+ __OBJC_CLASS_RO_$__UIFocusUpdateThrottle
+ __OBJC_CLASS_RO_$__UIFocusWeakHelper
+ __OBJC_CLASS_RO_$__UIHostedFocusSystem
+ __OBJC_CLASS_RO_$__UIHostedFocusSystemDelegateProxy
+ __OBJC_CLASS_RO_$__UIHostedFocusSystemItemContainer
+ __OBJC_LABEL_PROTOCOL_$_UIFocusDebuggerOutput
+ __OBJC_LABEL_PROTOCOL_$_UIFocusEnvironment
+ __OBJC_LABEL_PROTOCOL_$_UIFocusItem
+ __OBJC_LABEL_PROTOCOL_$_UIFocusItemContainer
+ __OBJC_LABEL_PROTOCOL_$_UIFocusItemScrollableContainer
+ __OBJC_LABEL_PROTOCOL_$__UIDebugIssueReporting
+ __OBJC_LABEL_PROTOCOL_$__UIFocusEnvironmentInternal
+ __OBJC_LABEL_PROTOCOL_$__UIFocusEnvironmentPlatformSupport
+ __OBJC_LABEL_PROTOCOL_$__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_LABEL_PROTOCOL_$__UIFocusEnvironmentPreferenceEnumerationContextDelegate
+ __OBJC_LABEL_PROTOCOL_$__UIFocusEnvironmentPrivate
+ __OBJC_LABEL_PROTOCOL_$__UIFocusGuideRegionDelegate
+ __OBJC_LABEL_PROTOCOL_$__UIFocusMapArea
+ __OBJC_LABEL_PROTOCOL_$__UIFocusMovementPerformerDelegate
+ __OBJC_LABEL_PROTOCOL_$__UIFocusRegionContainer
+ __OBJC_LABEL_PROTOCOL_$__UIFocusRegionSearchContext
+ __OBJC_LABEL_PROTOCOL_$__UIFocusSystemDelegate
+ __OBJC_LABEL_PROTOCOL_$__UIFocusUpdateRequesting
+ __OBJC_LABEL_PROTOCOL_$__UIHostedFocusSystemDelegate
+ __OBJC_METACLASS_RO_$_UIFocusDebugger
+ __OBJC_METACLASS_RO_$_UIFocusMovementAction
+ __OBJC_METACLASS_RO_$_UIFocusMovementHint
+ __OBJC_METACLASS_RO_$_UIFocusSystem
+ __OBJC_METACLASS_RO_$_UIFocusUpdateContext
+ __OBJC_METACLASS_RO_$__UIDebugIssue
+ __OBJC_METACLASS_RO_$__UIDebugIssueReport
+ __OBJC_METACLASS_RO_$__UIDebugIssueReportFormatter
+ __OBJC_METACLASS_RO_$__UIDebugLogReport
+ __OBJC_METACLASS_RO_$__UIDebugLogReportFormatter
+ __OBJC_METACLASS_RO_$__UIDebugLogStatement
+ __OBJC_METACLASS_RO_$__UIDebugReportComponents
+ __OBJC_METACLASS_RO_$__UIDebugReportFormatter
+ __OBJC_METACLASS_RO_$__UIFocusContainerGuideFallbackItemsContainer
+ __OBJC_METACLASS_RO_$__UIFocusContainerGuideImpl
+ __OBJC_METACLASS_RO_$__UIFocusContainerGuideRegion
+ __OBJC_METACLASS_RO_$__UIFocusDebuggerStringOutput
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentContainerTuple
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentPreferenceCache
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentPreferenceCacheNode
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentPreferenceEnumerator
+ __OBJC_METACLASS_RO_$__UIFocusEnvironmentScrollableContainerTuple
+ __OBJC_METACLASS_RO_$__UIFocusGroup
+ __OBJC_METACLASS_RO_$__UIFocusGroupHistory
+ __OBJC_METACLASS_RO_$__UIFocusGroupMap
+ __OBJC_METACLASS_RO_$__UIFocusGuideImpl
+ __OBJC_METACLASS_RO_$__UIFocusGuideRegion
+ __OBJC_METACLASS_RO_$__UIFocusInputDeviceInfo
+ __OBJC_METACLASS_RO_$__UIFocusItemDummy
+ __OBJC_METACLASS_RO_$__UIFocusItemInfo
+ __OBJC_METACLASS_RO_$__UIFocusItemRegion
+ __OBJC_METACLASS_RO_$__UIFocusLinearMovementCache
+ __OBJC_METACLASS_RO_$__UIFocusLinearMovementSequence
+ __OBJC_METACLASS_RO_$__UIFocusMap
+ __OBJC_METACLASS_RO_$__UIFocusMapRect
+ __OBJC_METACLASS_RO_$__UIFocusMapSearchInfo
+ __OBJC_METACLASS_RO_$__UIFocusMapSnapshot
+ __OBJC_METACLASS_RO_$__UIFocusMapSnapshotter
+ __OBJC_METACLASS_RO_$__UIFocusMovementInfo
+ __OBJC_METACLASS_RO_$__UIFocusMovementPerformer
+ __OBJC_METACLASS_RO_$__UIFocusMovementRequest
+ __OBJC_METACLASS_RO_$__UIFocusNullGroup
+ __OBJC_METACLASS_RO_$__UIFocusPromiseItem
+ __OBJC_METACLASS_RO_$__UIFocusPromiseRegion
+ __OBJC_METACLASS_RO_$__UIFocusRegion
+ __OBJC_METACLASS_RO_$__UIFocusRegionContainerProxy
+ __OBJC_METACLASS_RO_$__UIFocusRegionEvaluator
+ __OBJC_METACLASS_RO_$__UIFocusRegionMovementInfo
+ __OBJC_METACLASS_RO_$__UIFocusRegionSearchContextState
+ __OBJC_METACLASS_RO_$__UIFocusSearchInfo
+ __OBJC_METACLASS_RO_$__UIFocusSpeedBumpRegion
+ __OBJC_METACLASS_RO_$__UIFocusTreeLock
+ __OBJC_METACLASS_RO_$__UIFocusTreeLockItem
+ __OBJC_METACLASS_RO_$__UIFocusUpdateReport
+ __OBJC_METACLASS_RO_$__UIFocusUpdateReportFormatter
+ __OBJC_METACLASS_RO_$__UIFocusUpdateRequest
+ __OBJC_METACLASS_RO_$__UIFocusUpdateThrottle
+ __OBJC_METACLASS_RO_$__UIFocusWeakHelper
+ __OBJC_METACLASS_RO_$__UIHostedFocusSystem
+ __OBJC_METACLASS_RO_$__UIHostedFocusSystemDelegateProxy
+ __OBJC_METACLASS_RO_$__UIHostedFocusSystemItemContainer
+ __OBJC_PROTOCOL_$_UIFocusDebuggerOutput
+ __OBJC_PROTOCOL_$_UIFocusEnvironment
+ __OBJC_PROTOCOL_$_UIFocusItem
+ __OBJC_PROTOCOL_$_UIFocusItemContainer
+ __OBJC_PROTOCOL_$_UIFocusItemScrollableContainer
+ __OBJC_PROTOCOL_$__UIDebugIssueReporting
+ __OBJC_PROTOCOL_$__UIFocusEnvironmentInternal
+ __OBJC_PROTOCOL_$__UIFocusEnvironmentPlatformSupport
+ __OBJC_PROTOCOL_$__UIFocusEnvironmentPreferenceEnumerationContext
+ __OBJC_PROTOCOL_$__UIFocusEnvironmentPreferenceEnumerationContextDelegate
+ __OBJC_PROTOCOL_$__UIFocusEnvironmentPrivate
+ __OBJC_PROTOCOL_$__UIFocusGuideRegionDelegate
+ __OBJC_PROTOCOL_$__UIFocusMapArea
+ __OBJC_PROTOCOL_$__UIFocusMovementPerformerDelegate
+ __OBJC_PROTOCOL_$__UIFocusRegionContainer
+ __OBJC_PROTOCOL_$__UIFocusRegionSearchContext
+ __OBJC_PROTOCOL_$__UIFocusSystemDelegate
+ __OBJC_PROTOCOL_$__UIFocusUpdateRequesting
+ __OBJC_PROTOCOL_$__UIHostedFocusSystemDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_UIFocusEnvironment
+ __OBJC_PROTOCOL_REFERENCE_$_UIFocusItem
+ __OBJC_PROTOCOL_REFERENCE_$_UIFocusItemScrollableContainer
+ __OBJC_PROTOCOL_REFERENCE_$__UIFocusRegionContainer
+ __UIAXAssignFocusToItem
+ __UIAXAssignFocusToItemWithOptions
+ __UIAXFocusItemIsFocusableInFocusSystemWithSearchInfo
+ __UIFocusAncestorEnvironmentScrollableContainers
+ __UIFocusDistanceBetweenRects
+ __UIFocusEngineCommonEnvironmentScrollableContainerForItems
+ __UIFocusEngineFirstScrollableContainerTupleThatScrollsForItem
+ __UIFocusEngineGestureDidBeginNotification
+ __UIFocusEngineScrollableContainerCanScroll
+ __UIFocusEnvironmentAllowsFocusToLeaveViaHeading
+ __UIFocusEnvironmentContainerFrameInCoordinateSpace
+ __UIFocusEnvironmentEffectivePreferredFocusEnvironments
+ __UIFocusEnvironmentEnumerateAncestorEnvironments
+ __UIFocusEnvironmentFirstCommonAncestor
+ __UIFocusEnvironmentInheritedFocusMovementStyle
+ __UIFocusEnvironmentIsAncestorOfEnvironment
+ __UIFocusEnvironmentIsEligibleForFocusInteraction
+ __UIFocusEnvironmentIsEligibleForFocusOcclusion
+ __UIFocusEnvironmentParentEnvironment
+ __UIFocusEnvironmentPreferredFocusEnvironments
+ __UIFocusEnvironmentPreferredFocusMapContainer
+ __UIFocusEnvironmentPrefersFocusContainment
+ __UIFocusEnvironmentResolvedRotaryFocusMovementAxis
+ __UIFocusEnvironmentRootAncestorEnvironment
+ __UIFocusEnvironmentRotaryFocusMovementAxis
+ __UIFocusEnvironmentShouldUpdateFocus
+ __UIFocusEnvironmentUseLegacyIsFocusedOrContainsFocusLogic
+ __UIFocusEnvironmentsHaveCommonHierarchy
+ __UIFocusGetFocusTreeLockVerboseLogging
+ __UIFocusGetNextItemFromList
+ __UIFocusGroupCompare
+ __UIFocusGroupIdentifierForInstance
+ __UIFocusGroupPriorityForItem
+ __UIFocusGroupUnresolvedIdentifierForEnvironment
+ __UIFocusInternalPreferenceSync
+ __UIFocusInternalPreferenceUpdateBool
+ __UIFocusInternalPreference_FocusEnvironmentUseAncestorScrollableSizeForFallbackRotaryAxis
+ __UIFocusInternalPreference_FocusEnvironmentUseLegacyIsFocusedOrContainsFocusLogic
+ __UIFocusInternalPreference_FocusGroupSeparateNestedEqualRotaryMovementAxis
+ __UIFocusInternalPreference_FocusTreeLockVerboseLogging
+ __UIFocusInternalPreferencesRevisionInit_block_invoke
+ __UIFocusInternalPreferencesRevisionOnce
+ __UIFocusInternalPreferencesRevisionVar
+ __UIFocusItemCanBecomeFocused
+ __UIFocusItemCompare
+ __UIFocusItemContainerAddChildItemsInContextWithOptions
+ __UIFocusItemContainerIsScrollableContainer
+ __UIFocusItemContainerSupportsInvalidatingFocusCache
+ __UIFocusItemDeferralModeForItem
+ __UIFocusItemFocusSpeedBumpEdges
+ __UIFocusItemFrameInCoordinateSpace
+ __UIFocusItemIsFocusableInFocusSystem
+ __UIFocusItemIsFocusableInFocusSystemWithSearchInfo
+ __UIFocusItemIsFocused
+ __UIFocusItemIsFocusedOrFocusable
+ __UIFocusItemIsFocusedOrFocusableInFocusSystem
+ __UIFocusItemIsTransparentFocusItem
+ __UIFocusItemSafeCast
+ __UIFocusItemScrollableContainerCanScrollX
+ __UIFocusItemScrollableContainerCanScrollY
+ __UIFocusItemScrollableContainerContentBounds
+ __UIFocusItemScrollableContainerPrimaryAxis
+ __UIFocusMapDistanceToRegionBoundary
+ __UIFocusNearestAncestorEnvironmentScrollableContainer
+ __UIFocusPreferencesOnce
+ __UIFocusProcessIsBeingDebugged
+ __UIFocusRectCompare
+ __UIFocusRectSmartIntersectsRect
+ __UIFocusRectWithMinimumSize
+ __UIFocusRegionContainerFromEnvironmentAndContainer
+ __UIFocusRegionSearchContextAddChildItemsInEnvironmentContainer
+ __UIFocusRegionSearchContextSearchForFocusRegionsInEnvironment
+ __UIFocusShiftAndExpandRectAlongFocusMovement
+ __UIFocusStringFromCGRect
+ __UIFocusSystemEnabledStateDidChangeNotification
+ __UIFocusUserDefaults
+ __UIHostedFocusSystemsForHostEnvironment
+ __UIStringFromFocusHeading
+ __UIStringFromGroupFilter
+ ___103-[_UIFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]_block_invoke
+ ___104-[UIFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]_block_invoke
+ ___23+[UIFocusDebugger help]_block_invoke
+ ___24-[_UIFocusTreeLock init]_block_invoke
+ ___31-[_UIFocusUpdateThrottle reset]_block_invoke
+ ___33-[UIFocusUpdateContext _validate]_block_invoke
+ ___33-[UIFocusUpdateContext _validate]_block_invoke_2
+ ___34-[_UIFocusUpdateThrottle teardown]_block_invoke
+ ___37-[UIFocusSystem _requestFocusUpdate:]_block_invoke
+ ___40-[_UIFocusTreeLock lockEnvironmentTree:]_block_invoke
+ ___43+[UIFocusDebugger _ancestryForEnvironment:]_block_invoke
+ ___43-[UIFocusSystem _updateFocusUpdateThrottle]_block_invoke
+ ___44-[UIFocusSystem _focusEnvironmentDidAppear:]_block_invoke
+ ___45+[UIFocusDebugger focusGroupsForEnvironment:]_block_invoke
+ ___45+[UIFocusDebugger focusGroupsForEnvironment:]_block_invoke_2
+ ___45-[_UIFocusMapSnapshot addRegionsInContainer:]_block_invoke
+ ___46-[UIFocusSystem _reevaluateLockedEnvironments]_block_invoke
+ ___46-[UIFocusSystem _tickHasSeenFocusedItemTimer:]_block_invoke
+ ___46-[_UIFocusGroup _validateItemOrderIfNecessary]_block_invoke
+ ___48-[_UIFocusUpdateReportFormatter _bodyForReport:]_block_invoke
+ ___49-[_UIDebugLogReport fallbackMessagePrefixHandler]_block_invoke
+ ___52-[_UIDebugLogReportFormatter _componentsFromReport:]_block_invoke
+ ___52-[_UIDebugLogReportFormatter _componentsFromReport:]_block_invoke_2
+ ___52-[_UIFocusGroup _validateChildGroupOrderIfNecessary]_block_invoke
+ ___54-[UIFocusSystem _focusEnvironmentWillBecomeInvisible:]_block_invoke
+ ___54-[_UIDebugIssueReportFormatter _componentsFromReport:]_block_invoke
+ ___54-[_UIFocusItemInfo isFocusMovementFlippedHorizontally]_block_invoke
+ ___54-[_UIFocusMap _inferredDefaultFocusItemInEnvironment:]_block_invoke
+ ___56-[UIFocusSystem _buildFocusItemAncestorCacheIfNecessary]_block_invoke
+ ___57-[_UIFocusUpdateThrottle scheduleProgrammaticFocusUpdate]_block_invoke
+ ___59-[UIFocusSystem _sendDidUpdateFocusNotificationsInContext:]_block_invoke
+ ___60+[UIFocusDebugger preferredFocusEnvironmentsForEnvironment:]_block_invoke
+ ___60-[UIFocusSystem _sendWillUpdateFocusNotificationsInContext:]_block_invoke
+ ___63-[_UIFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke
+ ___63-[_UIFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke_2
+ ___63-[_UIFocusTreeLockItem initWithEnvironment:finalUnlockHandler:]_block_invoke
+ ___69-[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:]_block_invoke
+ ___70-[UIFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]_block_invoke
+ ___70-[UIFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]_block_invoke_2
+ ___76-[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]_block_invoke
+ ___76-[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]_block_invoke_2
+ ___78-[_UIFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]_block_invoke
+ ___78-[_UIFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment]_block_invoke
+ ___82-[_UIFocusEnvironmentPreferenceCache preferredEnvironmentsForEnvironment:isFinal:]_block_invoke
+ ___92-[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]_block_invoke
+ ___93-[_UIFocusContainerGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:]_block_invoke
+ ___98-[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke
+ ___98-[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke_2
+ ____UIFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke
+ ____UIFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke_2
+ ____UIFocusEnvironmentInheritedFocusMovementStyle_block_invoke
+ ____UIFocusEnvironmentIsAncestorOfEnvironment_block_invoke
+ ____UIFocusEnvironmentPreferredFocusMapContainer_block_invoke
+ ____UIFocusEnvironmentResolvedRotaryFocusMovementAxis_block_invoke
+ ____UIFocusItemContainerAddChildItemsInContextWithOptions_block_invoke
+ ____UIFocusPreferencesOnce_block_invoke
+ ____UIFocusSystemRegister_block_invoke
+ ____UIFocusUserDefaults_block_invoke
+ ____UIHostedFocusSystemRegister_block_invoke
+ ____UIStringFromFocusHeading_block_invoke
+ ___block_descriptor_32_e41_q24?0"<UIFocusItem>"8"<UIFocusItem>"16l
+ ___block_descriptor_32_e41_q24?0"_UIFocusGroup"8"_UIFocusGroup"16l
+ ___block_descriptor_32_e48_16?0"_UIFocusEnvironmentPreferenceCacheNode"8l
+ ___block_descriptor_40_e24_B16?0"_UIFocusRegion"8lu32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e34_v24?0"<UIFocusEnvironment>"8^B16lr32l8
+ ___block_descriptor_40_e8_32r_e59_B16?0"<_UIFocusEnvironmentPreferenceEnumerationContext>"8lr32l8
+ ___block_descriptor_40_e8_32s_e30_B32?0"_UIFocusGroup"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e30_v16?0"<UIFocusEnvironment>"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v36?0"_UIFocusGroup"8Q16B24^B28ls32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e58_"<_UIFocusRegionContainer>"16?0"_UIFocusPromiseRegion"8ls32l8
+ ___block_descriptor_40_e8_32s_e60_B32?0"_UIFocusEnvironmentScrollableContainerTuple"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"<UIFocusEnvironment>"8lw32l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"<UIFocusEnvironment>"8^B16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e37_v32?0"_UIDebugLogStatement"8Q16^B24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e37_v32?0"<UIFocusEnvironment>"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e23_B16?0"<UIFocusItem>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e30_16?0"<UIFocusEnvironment>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e30_v16?0"<UIFocusEnvironment>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e40_B24?0"<UIFocusItem>"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e63_v24?0"<_UIFocusEnvironmentPreferenceEnumerationContext>"8^q16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e63_v24?0"<_UIFocusEnvironmentPreferenceEnumerationContext>"8^q16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e37_v32?0"_UIDebugLogStatement"8Q16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r_e47_v32?0"_UIFocusLinearMovementSequence"8Q16^B24ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e63_v24?0"<_UIFocusEnvironmentPreferenceEnumerationContext>"8^q16lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e30_v32?0"_UIDebugIssue"8Q16^B24ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e34_v24?0"<UIFocusEnvironment>"8^B16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56r_e47_v32?0"_UIFocusLinearMovementSequence"8Q16^B24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e63_v24?0"<_UIFocusEnvironmentPreferenceEnumerationContext>"8^q16ls32l8r64l8s40l8r72l8s48l8r80l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64r72r80r88r_e34_v24?0"<UIFocusEnvironment>"8^B16lr64l8s32l8s40l8r72l8r80l8s48l8s56l8r88l8
+ _addRegionsInContainer:.once
+ _dyld_program_sdk_at_least
+ _objc_msgSend$_allRegionsInContainer:intersectingRegion:
+ _objc_msgSend$_allowsFocusToLeaveViaHeading:
+ _objc_msgSend$_automaticallyPreferOwningItem
+ _objc_msgSend$_closestFocusableItemToPoint:inRect:itemFilter:distanceMeasuringUnitPoint:
+ _objc_msgSend$_focusCasting
+ _objc_msgSend$_focusEnvironmentWillDisappear:remainingInHierarchy:
+ _objc_msgSend$_focusGuideBehaviorForFocusMovement:
+ _objc_msgSend$_focusItemGuides
+ _objc_msgSend$_focusPriorityRequired
+ _objc_msgSend$_focusRegionFrameInCoordinateSpace:
+ _objc_msgSend$_focusSystem:containsChildOfHostEnvironment:
+ _objc_msgSend$_focusSystem:focusItemsInRect:
+ _objc_msgSend$_focusedGuideImpl
+ _objc_msgSend$_initWithItem:useFallbackAncestorScroller:
+ _objc_msgSend$_linearFocusMovementSequences
+ _objc_msgSend$_performFocusMovement:
+ _objc_msgSend$_preferredFocusMovementStyle
+ _objc_msgSend$_rotaryFocusMovementAxis
+ _objc_msgSend$_setAutomaticallyPreferOwningItem:
+ _objc_msgSend$_setFocusedGuideImpl:
+ _objc_msgSend$_statusForFocusSystem:includeDeferralTarget:
+ _objc_msgSend$addRegionsInContainers:
+ _objc_msgSend$appendObject:withName:skipIfNil:
+ _objc_msgSend$appendRect:withName:
+ _objc_msgSend$bs_CGRectValue
+ _objc_msgSend$bs_valueWithCGRect:
+ _objc_msgSend$canBecomeFocused
+ _objc_msgSend$childItems
+ _objc_msgSend$containsChildOfHostEnvironment:
+ _objc_msgSend$contentOffset
+ _objc_msgSend$contentSize
+ _objc_msgSend$convertPoint:toCoordinateSpace:
+ _objc_msgSend$debugIdentifier
+ _objc_msgSend$delegateProxy
+ _objc_msgSend$didUpdateFocusFromGuide:
+ _objc_msgSend$fallbackItemProvider
+ _objc_msgSend$fallbackRootRegionContainer
+ _objc_msgSend$focusDidUpdateViaGuide
+ _objc_msgSend$focusGroupIdentifier
+ _objc_msgSend$focusGroupPriority
+ _objc_msgSend$focusGuide:preferredEnvironmentsForHeading:
+ _objc_msgSend$focusItemContainer
+ _objc_msgSend$focusItemDeferralMode
+ _objc_msgSend$focusItemsInRect:
+ _objc_msgSend$focusMovementInfo
+ _objc_msgSend$frameForFocusGuide:
+ _objc_msgSend$fulfilledItem
+ _objc_msgSend$fulfillmentHandler
+ _objc_msgSend$hostEnvironment
+ _objc_msgSend$info
+ _objc_msgSend$infoWithSenderID:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:
+ _objc_msgSend$initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:focusedFrameInSceneCoordinateSpace:
+ _objc_msgSend$initWithFocusSystem:delegate:
+ _objc_msgSend$initWithHostedFocusSystem:
+ _objc_msgSend$initWithParentEnvironment:childItems:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isTransparentFocusItem
+ _objc_msgSend$itemContainerProxy
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectForSetting:
+ _objc_msgSend$originatingHeading
+ _objc_msgSend$owningItem
+ _objc_msgSend$parentFocusEnvironment
+ _objc_msgSend$preferredFocusEnvironments
+ _objc_msgSend$setDelegateProxy:
+ _objc_msgSend$setFallbackRootRegionContainer:
+ _objc_msgSend$setFrame:
+ _objc_msgSend$setFulfillmentHandler:
+ _objc_msgSend$setObject:forSetting:
+ _objc_msgSend$setParentFocusEnvironment:
+ _objc_msgSend$shouldUpdateFocusInContext:
+ _objc_msgSend$visibleSize
- +[_FEDebugIssue issueWithDescription:]
- +[_FEDebugIssue issueWithFormat:]
- +[_FEDebugLogMessage messageWithFormat:]
- +[_FEDebugLogMessage messageWithNewline]
- +[_FEDebugLogMessage messageWithPrefix:string:]
- +[_FEDebugLogMessage messageWithString:]
- +[_FEDebugLogMessage messageWithStyle:string:]
- +[_FEDebugLogNode rootNode]
- +[_FEDebugLogNodeTreeStyle defaultStyle]
- +[_FEDebugLogNodeTreeStyle styleWithNode:lastNode:intermediate:trailing:]
- +[_FEDebugReportFormatter defaultFormatter]
- +[_FEFocusDebugger _ancestryForEnvironment:]
- +[_FEFocusDebugger _legacy_checkFocusabilityForView:]
- +[_FEFocusDebugger _statusForFocusSystem:scene:includeSceneLog:includeDeferralTarget:]
- +[_FEFocusDebugger _verboseStatus]
- +[_FEFocusDebugger checkFocusGroupTreeForEnvironment:]
- +[_FEFocusDebugger checkFocusabilityForItem:]
- +[_FEFocusDebugger focusGroupsForEnvironment:]
- +[_FEFocusDebugger help]
- +[_FEFocusDebugger preferredFocusEnvironmentsForEnvironment:]
- +[_FEFocusDebugger simulateFocusUpdateRequestFromEnvironment:]
- +[_FEFocusDebugger status]
- +[_FEFocusDebuggerStringOutput outputWithString:]
- +[_FEFocusEnvironmentContainerTuple tupleWithOwningEnvironment:itemContainer:]
- +[_FEFocusEnvironmentContainerTuple tupleWithRequiredContainerFromEnvironment:]
- +[_FEFocusEnvironmentScrollableContainerTuple tupleWithOwningEnvironment:scrollableContainer:]
- +[_FEFocusGroup nullGroupWithCoordinateSpace:]
- +[_FEFocusInputDeviceInfo infoWithSenderID:]
- +[_FEFocusInputDeviceInfo supportsSecureCoding]
- +[_FEFocusItemInfo infoWithItem:]
- +[_FEFocusItemInfo infoWithItem:useFallbackAncestorScroller:]
- +[_FEFocusLinearMovementSequence sequenceWithItems:loops:]
- +[_FEFocusLinearMovementSequence sequenceWithItems:loops:restrictEnteringSequence:]
- +[_FEFocusMapSnapshotDebugInfo _summaryImageForDebugInfoArray:forFocusMovementWithInfo:scaleFactor:]
- +[_FEFocusMovementInfo _movementWithHeading:isInitial:]
- +[_FEFocusMovementInfo _movementWithHeading:isInitial:fallbackMovementOriginatingFrame:]
- +[_FEFocusMovementInfo supportsSecureCoding]
- +[_FEFocusRegionDebugDrawingConfiguration containerGuideConfigurationForRegion:]
- +[_FEFocusRegionDebugDrawingConfiguration guideConfigurationForRegion:]
- +[_FEFocusRegionDebugDrawingConfiguration itemConfigurationForRegion:]
- +[_FEFocusRegionDebugDrawingConfiguration promiseConfigurationForRegion:]
- +[_FEFocusRegionDebugQuickLook drawDebugQuickLookImageForRegion:withInfo:inContext:]
- +[_FEFocusRegionEvaluator __regionsByEvaluatingOcclusionsForBaseRegions:occludingRegions:baseRegionsCanOccludeEachOther:inSnapshot:]
- +[_FEFocusRegionEvaluator _visibleSubregionsWhenRegion:occludedByRegion:inSnapshot:]
- +[_FEFocusRegionEvaluator frameForRegion:inCoordinateSpace:]
- +[_FEFocusRegionEvaluator regionsByEvaluatingOcclusionsForRegions:inSnapshot:]
- +[_FEFocusRegionEvaluator regionsByOccludingRegions:beneathRegions:inSnapshot:]
- +[_FEFocusRegionEvaluator subregionFromRegion:withSnapshotFrame:inSnapshot:]
- +[_FEFocusRegionMovementInfo _movementWithHeading:linearHeading:originatingHeading:isInitial:inputType:]
- +[_FEFocusRegionSearchContextState stateWithRegionContainer:focusSystem:clippingRect:]
- +[_FEFocusSearchInfo defaultInfo]
- +[_FEFocusSystem _allFocusSystems]
- +[_FEFocusSystem _focusSystemForEnvironment:]
- +[_FEFocusSystem environment:containsEnvironment:]
- +[_FEFocusSystem focusSystemForEnvironment:]
- +[_FEFocusUpdateContext _defaultValidationReportFormatter]
- +[_FEFocusUpdateRequest requestForRemovingFocusInFocusSystem:]
- -[NSCoder(_FEGeometryKeyedCoding) decodeCGRectForKey:]
- -[NSCoder(_FEGeometryKeyedCoding) encodeCGRect:forKey:]
- -[NSObject(_FEFocusRegionContainerProxy) _ui_isUIFocusRegionContainerProxy]
- -[_FEDebugIssue .cxx_destruct]
- -[_FEDebugIssue _subissueReport]
- -[_FEDebugIssue addIssue:]
- -[_FEDebugIssue description]
- -[_FEDebugIssue init]
- -[_FEDebugIssue prefix]
- -[_FEDebugIssue setDescription:]
- -[_FEDebugIssue setPrefix:]
- -[_FEDebugIssue subissues]
- -[_FEDebugIssueReport .cxx_destruct]
- -[_FEDebugIssueReport addIssue:]
- -[_FEDebugIssueReport init]
- -[_FEDebugIssueReport issues]
- -[_FEDebugIssueReportFormatter .cxx_destruct]
- -[_FEDebugIssueReportFormatter _componentsFromReport:]
- -[_FEDebugIssueReportFormatter defaultIssuePrefix]
- -[_FEDebugIssueReportFormatter footer]
- -[_FEDebugIssueReportFormatter header]
- -[_FEDebugIssueReportFormatter init]
- -[_FEDebugIssueReportFormatter noIssuesDescription]
- -[_FEDebugIssueReportFormatter setDefaultIssuePrefix:]
- -[_FEDebugIssueReportFormatter setFooter:]
- -[_FEDebugIssueReportFormatter setHeader:]
- -[_FEDebugIssueReportFormatter setNoIssuesDescription:]
- -[_FEDebugIssueReportFormatter stringFromReport:]
- -[_FEDebugLogMessage .cxx_destruct]
- -[_FEDebugLogMessage _isNode]
- -[_FEDebugLogMessage _isTransparent]
- -[_FEDebugLogMessage _stringRepresentation]
- -[_FEDebugLogMessage description]
- -[_FEDebugLogMessage initWithString:]
- -[_FEDebugLogNode .cxx_destruct]
- -[_FEDebugLogNode __genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:]
- -[_FEDebugLogNode _appendChildDescription:withPrefix:inheritedTreeStyle:]
- -[_FEDebugLogNode _isNode]
- -[_FEDebugLogNode addMessage:]
- -[_FEDebugLogNode description]
- -[_FEDebugLogNode hasMessages]
- -[_FEDebugLogNode initWithString:]
- -[_FEDebugLogNode setTreeStyle:]
- -[_FEDebugLogNode treeStyle]
- -[_FEDebugLogNodeTreeStyle .cxx_destruct]
- -[_FEDebugLogNodeTreeStyle initWithNode:lastNode:intermediate:trailing:]
- -[_FEDebugLogNodeTreeStyle intermediate]
- -[_FEDebugLogNodeTreeStyle lastNode]
- -[_FEDebugLogNodeTreeStyle node]
- -[_FEDebugLogNodeTreeStyle trailing]
- -[_FEDebugLogReport .cxx_destruct]
- -[_FEDebugLogReport _messagePrefixAtIndentLevel:]
- -[_FEDebugLogReport _prefixStack]
- -[_FEDebugLogReport _statements]
- -[_FEDebugLogReport addLineBreak]
- -[_FEDebugLogReport addMessage:]
- -[_FEDebugLogReport addMessageWithFormat:]
- -[_FEDebugLogReport clearAllMessagePrefixes]
- -[_FEDebugLogReport currentIndentLevel]
- -[_FEDebugLogReport decrementIndentLevelAndPopMessagePrefix]
- -[_FEDebugLogReport decrementIndentLevel]
- -[_FEDebugLogReport fallbackMessagePrefixHandler]
- -[_FEDebugLogReport incrementIndentLevelAndPushMessagePrefix:]
- -[_FEDebugLogReport incrementIndentLevel]
- -[_FEDebugLogReport init]
- -[_FEDebugLogReport messageCount]
- -[_FEDebugLogReport popMessagePrefix]
- -[_FEDebugLogReport pushMessagePrefix:]
- -[_FEDebugLogReport pushMessagePrefixHandler:]
- -[_FEDebugLogReport resetIndentLevel]
- -[_FEDebugLogReport setCurrentIndentLevel:]
- -[_FEDebugLogReport setFallbackMessagePrefixHandler:]
- -[_FEDebugLogReport setPrefixStack:]
- -[_FEDebugLogReport setStatements:]
- -[_FEDebugLogReportFormatter _componentsFromReport:]
- -[_FEDebugLogReportFormatter stringFromReport:]
- -[_FEDebugLogStack .cxx_destruct]
- -[_FEDebugLogStack _topNode]
- -[_FEDebugLogStack addMessage:]
- -[_FEDebugLogStack init]
- -[_FEDebugLogStack performWithPushedNode:block:]
- -[_FEDebugLogStack popNode]
- -[_FEDebugLogStack pushNode:]
- -[_FEDebugLogStack rootNode]
- -[_FEDebugLogStatement .cxx_destruct]
- -[_FEDebugLogStatement indentLevel]
- -[_FEDebugLogStatement init]
- -[_FEDebugLogStatement prefix]
- -[_FEDebugLogStatement setIndentLevel:]
- -[_FEDebugLogStatement setPrefix:]
- -[_FEDebugLogStatement setText:]
- -[_FEDebugLogStatement setType:]
- -[_FEDebugLogStatement text]
- -[_FEDebugLogStatement type]
- -[_FEDebugReportComponents .cxx_destruct]
- -[_FEDebugReportComponents body]
- -[_FEDebugReportComponents footer]
- -[_FEDebugReportComponents header]
- -[_FEDebugReportComponents init]
- -[_FEDebugReportComponents setBody:]
- -[_FEDebugReportComponents setFooter:]
- -[_FEDebugReportComponents setHeader:]
- -[_FEDebugReportFormatter .cxx_destruct]
- -[_FEDebugReportFormatter extraBodyIndentLevel]
- -[_FEDebugReportFormatter indentLevel]
- -[_FEDebugReportFormatter indentString]
- -[_FEDebugReportFormatter init]
- -[_FEDebugReportFormatter setExtraBodyIndentLevel:]
- -[_FEDebugReportFormatter setIndentLevel:]
- -[_FEDebugReportFormatter setIndentString:]
- -[_FEDebugReportFormatter stringFromReportComponents:]
- -[_FEFocusCastingController .cxx_destruct]
- -[_FEFocusCastingController _axisForHeading:]
- -[_FEFocusCastingController _castingFrameForFocusedNormalizedFrame:heading:]
- -[_FEFocusCastingController _castingPointInNormalizedFrame:forHeading:]
- -[_FEFocusCastingController _createFocusMovementIndicator]
- -[_FEFocusCastingController _destroyFocusMovementIndicator]
- -[_FEFocusCastingController _entryPointInNormalizedFrame:forHeading:]
- -[_FEFocusCastingController _focusEffectsControllerForFocusedItem]
- -[_FEFocusCastingController _movementPointInNormalizedFrame:]
- -[_FEFocusCastingController _normalizedCoordinateSpace]
- -[_FEFocusCastingController _positionFocusMovementIndicators]
- -[_FEFocusCastingController _startRememberingEntryPoint]
- -[_FEFocusCastingController _stopRememberingEntryPoint]
- -[_FEFocusCastingController _updateFocusItemFromNormalizedFrame:toNormalizedFrame:withHeading:]
- -[_FEFocusCastingController _updateFocusMovementIndicatorDisplay]
- -[_FEFocusCastingController castingFrameForFocusedItem:heading:inCoordinateSpace:]
- -[_FEFocusCastingController entryPointAxis]
- -[_FEFocusCastingController entryPointMemorizationTimeout]
- -[_FEFocusCastingController focusCastingIndicator]
- -[_FEFocusCastingController focusEffectsController:updateMovementDirection:]
- -[_FEFocusCastingController focusEntryIndicator]
- -[_FEFocusCastingController focusMovementIndicator]
- -[_FEFocusCastingController focusSystem]
- -[_FEFocusCastingController forceUpdateFocusCastingFocusedRect:coordinateSpace:heading:]
- -[_FEFocusCastingController forgetEntryPoint]
- -[_FEFocusCastingController init]
- -[_FEFocusCastingController isRememberingEntryPoint]
- -[_FEFocusCastingController screenEntryPoint]
- -[_FEFocusCastingController setEntryPointAxis:]
- -[_FEFocusCastingController setEntryPointMemorizationTimeout:]
- -[_FEFocusCastingController setFocusCastingIndicator:]
- -[_FEFocusCastingController setFocusEntryIndicator:]
- -[_FEFocusCastingController setFocusMovementIndicator:]
- -[_FEFocusCastingController setFocusSystem:]
- -[_FEFocusCastingController setIsRememberingEntryPoint:]
- -[_FEFocusCastingController setScreenEntryPoint:]
- -[_FEFocusCastingController teardown]
- -[_FEFocusCastingController updateFocusCastingWithContext:]
- -[_FEFocusContainerGuideRegion .cxx_destruct]
- -[_FEFocusContainerGuideRegion _debugDrawingConfigurationWithDebugInfo:]
- -[_FEFocusContainerGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:]
- -[_FEFocusContainerGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusContainerGuideRegion _focusableBoundaries]
- -[_FEFocusContainerGuideRegion contentFocusRegionContainer]
- -[_FEFocusContainerGuideRegion isEqual:]
- -[_FEFocusContainerGuideRegion setContentFocusRegionContainer:]
- -[_FEFocusDebuggerStringOutput .cxx_destruct]
- -[_FEFocusDebuggerStringOutput description]
- -[_FEFocusDebuggerStringOutput initWithString:]
- -[_FEFocusDebuggerStringOutput init]
- -[_FEFocusEnvironmentContainerTuple .cxx_destruct]
- -[_FEFocusEnvironmentContainerTuple description]
- -[_FEFocusEnvironmentContainerTuple hash]
- -[_FEFocusEnvironmentContainerTuple initWithOwningEnvironment:itemContainer:]
- -[_FEFocusEnvironmentContainerTuple isEqual:]
- -[_FEFocusEnvironmentContainerTuple isEqualToEnvironmentContainerTuple:]
- -[_FEFocusEnvironmentContainerTuple isScrollableContainer]
- -[_FEFocusEnvironmentContainerTuple itemContainer]
- -[_FEFocusEnvironmentContainerTuple owningEnvironment]
- -[_FEFocusEnvironmentPreferenceCache .cxx_destruct]
- -[_FEFocusEnvironmentPreferenceCache deepestPrimaryPreferredEnvironmentForEnvironment:]
- -[_FEFocusEnvironmentPreferenceCache environmentsMap]
- -[_FEFocusEnvironmentPreferenceCache init]
- -[_FEFocusEnvironmentPreferenceCache preferredEnvironmentsForEnvironment:isFinal:]
- -[_FEFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]
- -[_FEFocusEnvironmentPreferenceCache setResolvedPreference:forEnvironment:]
- -[_FEFocusEnvironmentPreferenceCacheNode .cxx_destruct]
- -[_FEFocusEnvironmentPreferenceCacheNode _reevaluateResolution]
- -[_FEFocusEnvironmentPreferenceCacheNode _resolve:explicitly:]
- -[_FEFocusEnvironmentPreferenceCacheNode _unresolve]
- -[_FEFocusEnvironmentPreferenceCacheNode childNodes]
- -[_FEFocusEnvironmentPreferenceCacheNode debugDescription]
- -[_FEFocusEnvironmentPreferenceCacheNode description]
- -[_FEFocusEnvironmentPreferenceCacheNode environment]
- -[_FEFocusEnvironmentPreferenceCacheNode initWithEnvironment:]
- -[_FEFocusEnvironmentPreferenceCacheNode isResolved]
- -[_FEFocusEnvironmentPreferenceCacheNode resolve:]
- -[_FEFocusEnvironmentPreferenceCacheNode resolvedEnvironment]
- -[_FEFocusEnvironmentPreferenceCacheNode setChildNodes:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext .cxx_destruct]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _inferPreferencesForEnvironment:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _invalidatePreferredEnvironments]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _isAllowedToPreferEnvironment:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _reportInferredPreferredFocusEnvironment:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _resolvePreferredFocusEnvironments]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _startLogging]
- -[_FEFocusEnvironmentPreferenceEnumerationContext _stopLogging]
- -[_FEFocusEnvironmentPreferenceEnumerationContext debugStack]
- -[_FEFocusEnvironmentPreferenceEnumerationContext delegate]
- -[_FEFocusEnvironmentPreferenceEnumerationContext environment]
- -[_FEFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext init]
- -[_FEFocusEnvironmentPreferenceEnumerationContext isInPreferredSubtree]
- -[_FEFocusEnvironmentPreferenceEnumerationContext isLeafPreference]
- -[_FEFocusEnvironmentPreferenceEnumerationContext isPreferredByItself]
- -[_FEFocusEnvironmentPreferenceEnumerationContext isPrimaryPreference]
- -[_FEFocusEnvironmentPreferenceEnumerationContext popEnvironment]
- -[_FEFocusEnvironmentPreferenceEnumerationContext preferredEnvironments]
- -[_FEFocusEnvironmentPreferenceEnumerationContext preferringEnvironment]
- -[_FEFocusEnvironmentPreferenceEnumerationContext prefersNothingFocused]
- -[_FEFocusEnvironmentPreferenceEnumerationContext pushEnvironment:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext setDebugStack:]
- -[_FEFocusEnvironmentPreferenceEnumerationContext setDelegate:]
- -[_FEFocusEnvironmentPreferenceEnumerator .cxx_destruct]
- -[_FEFocusEnvironmentPreferenceEnumerator _shouldInferDefaultPreferenceForEnvironmentInContext:]
- -[_FEFocusEnvironmentPreferenceEnumerator allowsInferringPreferences]
- -[_FEFocusEnvironmentPreferenceEnumerator debugLog]
- -[_FEFocusEnvironmentPreferenceEnumerator didVisitAllPreferencesForEnvironmentHandler]
- -[_FEFocusEnvironmentPreferenceEnumerator enumeratePreferencesForEnvironment:usingBlock:]
- -[_FEFocusEnvironmentPreferenceEnumerator enumerationMode]
- -[_FEFocusEnvironmentPreferenceEnumerator initWithEnumerationMode:]
- -[_FEFocusEnvironmentPreferenceEnumerator init]
- -[_FEFocusEnvironmentPreferenceEnumerator setAllowsInferringPreferences:]
- -[_FEFocusEnvironmentPreferenceEnumerator setDebugLog:]
- -[_FEFocusEnvironmentPreferenceEnumerator setDidVisitAllPreferencesForEnvironmentHandler:]
- -[_FEFocusEnvironmentPreferenceEnumerator setShouldInferPreferenceForEnvironmentHandler:]
- -[_FEFocusEnvironmentPreferenceEnumerator shouldInferPreferenceForEnvironmentHandler]
- -[_FEFocusEnvironmentScrollableContainerTuple .cxx_destruct]
- -[_FEFocusEnvironmentScrollableContainerTuple description]
- -[_FEFocusEnvironmentScrollableContainerTuple hash]
- -[_FEFocusEnvironmentScrollableContainerTuple initWithOwningEnvironment:scrollableContainer:]
- -[_FEFocusEnvironmentScrollableContainerTuple isEqual:]
- -[_FEFocusEnvironmentScrollableContainerTuple owningEnvironment]
- -[_FEFocusEnvironmentScrollableContainerTuple scrollableContainer]
- -[_FEFocusGroup .cxx_destruct]
- -[_FEFocusGroup _deepCopyWithNewIdentifierToGroupMap:]
- -[_FEFocusGroup _insertChildGroup:]
- -[_FEFocusGroup _insertItem:]
- -[_FEFocusGroup _invalidateChildGroupOrder]
- -[_FEFocusGroup _invalidateItemOrder]
- -[_FEFocusGroup _invalidatePrimaryItem]
- -[_FEFocusGroup _invalidatePrimaryRect]
- -[_FEFocusGroup _updateWithEnvironment:]
- -[_FEFocusGroup _validateChildGroupOrderIfNecessary]
- -[_FEFocusGroup _validateItemOrderIfNecessary]
- -[_FEFocusGroup _validatePrimaryItemIfNecessary]
- -[_FEFocusGroup _validatePrimaryRectIfNeccessary]
- -[_FEFocusGroup boundingBox]
- -[_FEFocusGroup childGroups]
- -[_FEFocusGroup coordinateSpace]
- -[_FEFocusGroup debugDescription]
- -[_FEFocusGroup description]
- -[_FEFocusGroup hash]
- -[_FEFocusGroup identifier]
- -[_FEFocusGroup initWithIdentifier:parentGroup:coordinateSpace:]
- -[_FEFocusGroup isEqual:]
- -[_FEFocusGroup isEqualToFocusGroup:]
- -[_FEFocusGroup items]
- -[_FEFocusGroup owningEnvironment]
- -[_FEFocusGroup parentGroup]
- -[_FEFocusGroup primaryItem]
- -[_FEFocusGroup primaryRect]
- -[_FEFocusGroupHistory .cxx_destruct]
- -[_FEFocusGroupHistory _uiktest_clearHistory]
- -[_FEFocusGroupHistory init]
- -[_FEFocusGroupHistory lastFocusedItemForGroupIdentifier:]
- -[_FEFocusGroupHistory setLastFocusedItem:forGroupIdentifier:]
- -[_FEFocusGroupMap .cxx_destruct]
- -[_FEFocusGroupMap _indexEnvironment:]
- -[_FEFocusGroupMap _indexItems:]
- -[_FEFocusGroupMap coordinateSpace]
- -[_FEFocusGroupMap copyWithZone:]
- -[_FEFocusGroupMap description]
- -[_FEFocusGroupMap focusGroupForItem:]
- -[_FEFocusGroupMap focusGroups]
- -[_FEFocusGroupMap focusItems]
- -[_FEFocusGroupMap initWithItems:coordinateSpace:]
- -[_FEFocusGroupMap initWithItems:standInItemsMap:coordinateSpace:]
- -[_FEFocusGroupMap visualDescription]
- -[_FEFocusGuideRegion .cxx_destruct]
- -[_FEFocusGuideRegion _canBeOccludedByRegionsAbove]
- -[_FEFocusGuideRegion _canOccludeRegionsBelow]
- -[_FEFocusGuideRegion _debugAssociatedObject]
- -[_FEFocusGuideRegion _debugDrawingConfigurationWithDebugInfo:]
- -[_FEFocusGuideRegion _delegatePreferredFocusEnvironmentsForMovementRequest:]
- -[_FEFocusGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:]
- -[_FEFocusGuideRegion _focusPriority]
- -[_FEFocusGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusGuideRegion _focusableBoundaries]
- -[_FEFocusGuideRegion _focusedItemForLinearSorting:inMap:withSnapshot:]
- -[_FEFocusGuideRegion _ignoresSpeedBumpEdges]
- -[_FEFocusGuideRegion _isEnabledForFocusedRegion:inSnapshot:]
- -[_FEFocusGuideRegion _isUnclippable]
- -[_FEFocusGuideRegion _isUnoccludable]
- -[_FEFocusGuideRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
- -[_FEFocusGuideRegion _preferredDistanceComparisonType]
- -[_FEFocusGuideRegion _setFocusPriority:]
- -[_FEFocusGuideRegion _setIgnoresSpeedBumpEdges:]
- -[_FEFocusGuideRegion _setIsUnclippable:]
- -[_FEFocusGuideRegion _setIsUnoccludable:]
- -[_FEFocusGuideRegion _shouldCropRegionToSearchArea]
- -[_FEFocusGuideRegion _shouldUseNextFocusedItemForLinearSorting]
- -[_FEFocusGuideRegion _willParticipateAsDestinationRegionInFocusUpdate:]
- -[_FEFocusGuideRegion delegate]
- -[_FEFocusGuideRegion initWithFrame:coordinateSpace:]
- -[_FEFocusGuideRegion isEqual:]
- -[_FEFocusGuideRegion owningEnvironment]
- -[_FEFocusGuideRegion setDelegate:]
- -[_FEFocusGuideRegion setOwningEnvironment:]
- -[_FEFocusInputDeviceInfo _initWithSenderID:]
- -[_FEFocusInputDeviceInfo copyWithZone:]
- -[_FEFocusInputDeviceInfo encodeWithCoder:]
- -[_FEFocusInputDeviceInfo encodeWithXPCDictionary:]
- -[_FEFocusInputDeviceInfo initWithCoder:]
- -[_FEFocusInputDeviceInfo initWithXPCDictionary:]
- -[_FEFocusInputDeviceInfo senderID]
- -[_FEFocusItemDummy .cxx_destruct]
- -[_FEFocusItemDummy _canBecomeFocused]
- -[_FEFocusItemDummy _focusFrame]
- -[_FEFocusItemDummy _focusItemContainer]
- -[_FEFocusItemDummy _parentFocusEnvironment]
- -[_FEFocusItemDummy _preferredFocusEnvironments]
- -[_FEFocusItemDummy set_focusFrame:]
- -[_FEFocusItemDummy set_parentFocusEnvironment:]
- -[_FEFocusItemFrameReporter .cxx_destruct]
- -[_FEFocusItemFrameReporter _cancelRepeatingFrameUpdate]
- -[_FEFocusItemFrameReporter _focusSystemEnabledStateDidChange:]
- -[_FEFocusItemFrameReporter _globalFrameForFocusedItemInSystem:]
- -[_FEFocusItemFrameReporter _rect:differsFromRect:lowerThreshold:upperThreshold:]
- -[_FEFocusItemFrameReporter _reportFocusFrameForCurrentlyFocusedItem]
- -[_FEFocusItemFrameReporter _reportFocusFrameUpdateForGlobalFrame:]
- -[_FEFocusItemFrameReporter _scheduleRepeatingFrameUpdate]
- -[_FEFocusItemFrameReporter dealloc]
- -[_FEFocusItemFrameReporter focusSystem]
- -[_FEFocusItemFrameReporter initWithFocusSystem:]
- -[_FEFocusItemFrameReporter isEnabled]
- -[_FEFocusItemFrameReporter setEnabled:]
- -[_FEFocusItemInfo .cxx_destruct]
- -[_FEFocusItemInfo _createFocusedRegion]
- -[_FEFocusItemInfo _initWithItem:containingView:useFallbackAncestorScroller:]
- -[_FEFocusItemInfo ancestorEnvironmentScrollableContainers]
- -[_FEFocusItemInfo copyWithZone:]
- -[_FEFocusItemInfo description]
- -[_FEFocusItemInfo focusTouchSensitivityStyle]
- -[_FEFocusItemInfo focusedRectInCoordinateSpace:]
- -[_FEFocusItemInfo focusedRegion]
- -[_FEFocusItemInfo inheritedFocusMovementStyle]
- -[_FEFocusItemInfo invalidateFocusedRegion]
- -[_FEFocusItemInfo isFocusMovementFlippedHorizontally]
- -[_FEFocusItemInfo item]
- -[_FEFocusItemInfo rotaryFocusMovementAxis]
- -[_FEFocusItemInfo shortDescription]
- -[_FEFocusItemInfo useFallbackAncestorScroller]
- -[_FEFocusItemRegion .cxx_destruct]
- -[_FEFocusItemRegion _canBeOccludedByRegionsAbove]
- -[_FEFocusItemRegion _canOccludeRegionsBelow]
- -[_FEFocusItemRegion _debugAssociatedObject]
- -[_FEFocusItemRegion _debugDrawingConfigurationWithDebugInfo:]
- -[_FEFocusItemRegion _defaultFocusItem]
- -[_FEFocusItemRegion _descriptionBuilder]
- -[_FEFocusItemRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusItemRegion _focusableBoundaries]
- -[_FEFocusItemRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
- -[_FEFocusItemRegion _preferredDistanceComparisonType]
- -[_FEFocusItemRegion initWithFrame:coordinateSpace:]
- -[_FEFocusItemRegion initWithFrame:coordinateSpace:item:focusSystem:]
- -[_FEFocusItemRegion isEqual:]
- -[_FEFocusItemRegion item]
- -[_FEFocusLinearMovementCache .cxx_destruct]
- -[_FEFocusLinearMovementCache _invalidateOnTimeout]
- -[_FEFocusLinearMovementCache _invalidate]
- -[_FEFocusLinearMovementCache _updateParentEnvironmentIfNecessary]
- -[_FEFocusLinearMovementCache environmentDidAppear:]
- -[_FEFocusLinearMovementCache environmentWillDisappear:]
- -[_FEFocusLinearMovementCache focusGroupPriorityDidChange:]
- -[_FEFocusLinearMovementCache initWithFocusBehavior:]
- -[_FEFocusLinearMovementCache invalidateFocusItemContainer:]
- -[_FEFocusLinearMovementCache nextItemForRequest:]
- -[_FEFocusLinearMovementCache scrollableContainerDidScroll:]
- -[_FEFocusLinearMovementCache updateCacheWithContext:]
- -[_FEFocusLinearMovementSequence .cxx_destruct]
- -[_FEFocusLinearMovementSequence initWithItems:loops:]
- -[_FEFocusLinearMovementSequence initWithItems:loops:restrictEnteringSequence:]
- -[_FEFocusLinearMovementSequence init]
- -[_FEFocusLinearMovementSequence isLooping]
- -[_FEFocusLinearMovementSequence items]
- -[_FEFocusLinearMovementSequence restrictsEnteringSequence]
- -[_FEFocusMap .cxx_destruct]
- -[_FEFocusMap _allDefaultFocusableRegionsInContainer:intersectingRegion:]
- -[_FEFocusMap _allFocusableItemsInEnvironment:]
- -[_FEFocusMap _beginTrackingDefaultItemSearchInfoIfNecessary]
- -[_FEFocusMap _beginTrackingFocusMovementSearchInfoIfNecessary]
- -[_FEFocusMap _beginTrackingSearches]
- -[_FEFocusMap _closestFocusableItemToPoint:inRect:excludingItems:distanceMeasuringUnitPoint:]
- -[_FEFocusMap _defaultItemSearchContext]
- -[_FEFocusMap _defaultMapSnapshotter]
- -[_FEFocusMap _findAllDefaultFocusableRegionsWithSnapshotter:]
- -[_FEFocusMap _focusMovementSearchContext]
- -[_FEFocusMap _inferredDefaultFocusItemInEnvironment:]
- -[_FEFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]
- -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:]
- -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:inRegions:withSnapshot:]
- -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:]
- -[_FEFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
- -[_FEFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
- -[_FEFocusMap _nextFocusedItemForNonLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]
- -[_FEFocusMap _stopTrackingSearches]
- -[_FEFocusMap _trackExternalSnapshot:]
- -[_FEFocusMap coordinateSpace]
- -[_FEFocusMap diagnoseFocusabilityForItem:report:]
- -[_FEFocusMap focusGroupMap]
- -[_FEFocusMap focusSystem]
- -[_FEFocusMap initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
- -[_FEFocusMap initWithFocusSystem:rootEnvironment:]
- -[_FEFocusMap initWithFocusSystem:rootEnvironment:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
- -[_FEFocusMap init]
- -[_FEFocusMap minimumSearchArea]
- -[_FEFocusMap rootContainer]
- -[_FEFocusMap searchInfo]
- -[_FEFocusMap setMinimumSearchArea:]
- -[_FEFocusMap verifyFocusabilityForItem:]
- -[_FEFocusMapRect .cxx_destruct]
- -[_FEFocusMapRect coordinateSpace]
- -[_FEFocusMapRect description]
- -[_FEFocusMapRect frame]
- -[_FEFocusMapRect initWithFrame:coordinateSpace:]
- -[_FEFocusMapRect intersectionWithRegion:inSnapshot:]
- -[_FEFocusMapRect intersectsRect:]
- -[_FEFocusMapRect intersectsRegion:inSnapshot:]
- -[_FEFocusMapSearchInfo .cxx_destruct]
- -[_FEFocusMapSearchInfo addDestinationRegion:]
- -[_FEFocusMapSearchInfo addSnapshot:]
- -[_FEFocusMapSearchInfo destinationRegions]
- -[_FEFocusMapSearchInfo didFindFocusBlockingBoundary]
- -[_FEFocusMapSearchInfo focusGroupMap]
- -[_FEFocusMapSearchInfo hasOnlyStaticContent]
- -[_FEFocusMapSearchInfo init]
- -[_FEFocusMapSearchInfo linearSortedFocusItems]
- -[_FEFocusMapSearchInfo mutableDestinationRegions]
- -[_FEFocusMapSearchInfo mutableSnapshots]
- -[_FEFocusMapSearchInfo searchInfo]
- -[_FEFocusMapSearchInfo setDidFindFocusBlockingBoundary:]
- -[_FEFocusMapSearchInfo setFocusGroupMap:]
- -[_FEFocusMapSearchInfo setLinearSortedFocusItems:]
- -[_FEFocusMapSearchInfo setMutableDestinationRegions:]
- -[_FEFocusMapSearchInfo setMutableSnapshots:]
- -[_FEFocusMapSearchInfo setSearchInfo:]
- -[_FEFocusMapSearchInfo snapshots]
- -[_FEFocusMapSnapshot .cxx_destruct]
- -[_FEFocusMapSnapshot _cachedNextFocusedItemForRegion:withFocusMovementRequest:inMap:]
- -[_FEFocusMapSnapshot _capture]
- -[_FEFocusMapSnapshot _initWithSnapshotter:mapArea:searchArea:]
- -[_FEFocusMapSnapshot _searchArea]
- -[_FEFocusMapSnapshot _trackOccludingRegion:forRegion:]
- -[_FEFocusMapSnapshot _trackSubregion:forRegion:]
- -[_FEFocusMapSnapshot addRegion:]
- -[_FEFocusMapSnapshot addRegions:]
- -[_FEFocusMapSnapshot addRegionsInContainer:]
- -[_FEFocusMapSnapshot addRegionsInContainers:]
- -[_FEFocusMapSnapshot consumeRegionInformationForRegions:fromSnapshot:]
- -[_FEFocusMapSnapshot coordinateSpace]
- -[_FEFocusMapSnapshot dealloc]
- -[_FEFocusMapSnapshot focusSystem]
- -[_FEFocusMapSnapshot focusedRegion]
- -[_FEFocusMapSnapshot hasOnlyStaticContent]
- -[_FEFocusMapSnapshot init]
- -[_FEFocusMapSnapshot mapArea]
- -[_FEFocusMapSnapshot markContainerAsProvidingDynamicContent]
- -[_FEFocusMapSnapshot movementInfo]
- -[_FEFocusMapSnapshot occludingRegionsForRegion:]
- -[_FEFocusMapSnapshot originalRegionForRegion:]
- -[_FEFocusMapSnapshot originalRegions]
- -[_FEFocusMapSnapshot regionsContainer]
- -[_FEFocusMapSnapshot regionsForOriginalRegion:]
- -[_FEFocusMapSnapshot regions]
- -[_FEFocusMapSnapshot rootContainer]
- -[_FEFocusMapSnapshot searchArea]
- -[_FEFocusMapSnapshot searchInfo]
- -[_FEFocusMapSnapshot setMovementInfo:]
- -[_FEFocusMapSnapshot setSearchInfo:]
- -[_FEFocusMapSnapshot snapshotFrameForRegion:]
- -[_FEFocusMapSnapshot(_FEFocusDebugging) _debugInfoWithFocusMapSearchInfo:]
- -[_FEFocusMapSnapshot(_FEFocusDebugging) _debugInfo]
- -[_FEFocusMapSnapshot(_FEFocusDebugging) debugQuickLookObject]
- -[_FEFocusMapSnapshotDebugInfo .cxx_destruct]
- -[_FEFocusMapSnapshotDebugInfo _drawImage]
- -[_FEFocusMapSnapshotDebugInfo _rectContainingAllFocusRegions]
- -[_FEFocusMapSnapshotDebugInfo focusMapSearchInfo]
- -[_FEFocusMapSnapshotDebugInfo imageAnchorPoint]
- -[_FEFocusMapSnapshotDebugInfo image]
- -[_FEFocusMapSnapshotDebugInfo initWithSnapshot:focusMapSearchInfo:]
- -[_FEFocusMapSnapshotDebugInfo snapshot]
- -[_FEFocusMapSnapshotter .cxx_destruct]
- -[_FEFocusMapSnapshotter _searchAreaForContainerSearchRect:]
- -[_FEFocusMapSnapshotter captureSnapshot]
- -[_FEFocusMapSnapshotter clipToSnapshotRect]
- -[_FEFocusMapSnapshotter coordinateSpace]
- -[_FEFocusMapSnapshotter focusSystem]
- -[_FEFocusMapSnapshotter focusedRegion]
- -[_FEFocusMapSnapshotter ignoresRootContainerClippingRect]
- -[_FEFocusMapSnapshotter initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:]
- -[_FEFocusMapSnapshotter init]
- -[_FEFocusMapSnapshotter movementInfo]
- -[_FEFocusMapSnapshotter regionsContainer]
- -[_FEFocusMapSnapshotter rootContainer]
- -[_FEFocusMapSnapshotter searchInfo]
- -[_FEFocusMapSnapshotter setClipToSnapshotRect:]
- -[_FEFocusMapSnapshotter setFocusedRegion:]
- -[_FEFocusMapSnapshotter setIgnoresRootContainerClippingRect:]
- -[_FEFocusMapSnapshotter setMovementInfo:]
- -[_FEFocusMapSnapshotter setRegionsContainer:]
- -[_FEFocusMapSnapshotter setSearchInfo:]
- -[_FEFocusMapSnapshotter setSnapshotFrame:]
- -[_FEFocusMapSnapshotter snapshotFrame]
- -[_FEFocusMovementHint copyWithZone:]
- -[_FEFocusMovementHint initWithMovementDirection:itemSize:]
- -[_FEFocusMovementHint interactionTransform]
- -[_FEFocusMovementHint movementDirection]
- -[_FEFocusMovementHint perspectiveTransform]
- -[_FEFocusMovementHint rotationAmount]
- -[_FEFocusMovementHint rotation]
- -[_FEFocusMovementHint setRotationAmount:]
- -[_FEFocusMovementHint setTranslationAmount:]
- -[_FEFocusMovementHint translationAmount]
- -[_FEFocusMovementHint translation]
- -[_FEFocusMovementInfo _fallbackMovementOriginatingFrame]
- -[_FEFocusMovementInfo _groupFilter]
- -[_FEFocusMovementInfo _inputType]
- -[_FEFocusMovementInfo _isInitialMovement]
- -[_FEFocusMovementInfo _isLinearMovement]
- -[_FEFocusMovementInfo _isLooping]
- -[_FEFocusMovementInfo _isVelocityBased]
- -[_FEFocusMovementInfo _linearHeading]
- -[_FEFocusMovementInfo _setFallbackMovementOriginatingFrame:]
- -[_FEFocusMovementInfo _setGroupFilter:]
- -[_FEFocusMovementInfo _setHeading:]
- -[_FEFocusMovementInfo _setInputType:]
- -[_FEFocusMovementInfo _setIsInitialMovement:]
- -[_FEFocusMovementInfo _setIsVelocityBased:]
- -[_FEFocusMovementInfo _setLinearHeading:]
- -[_FEFocusMovementInfo _setLooping:]
- -[_FEFocusMovementInfo _setShouldLoadScrollableContainer:]
- -[_FEFocusMovementInfo _setVelocity:]
- -[_FEFocusMovementInfo _shouldLoadScrollableContainer]
- -[_FEFocusMovementInfo _velocity]
- -[_FEFocusMovementInfo copyWithZone:]
- -[_FEFocusMovementInfo description]
- -[_FEFocusMovementInfo encodeWithCoder:]
- -[_FEFocusMovementInfo encodeWithXPCDictionary:]
- -[_FEFocusMovementInfo heading]
- -[_FEFocusMovementInfo initWithCoder:]
- -[_FEFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:]
- -[_FEFocusMovementInfo initWithHeading:linearHeading:isInitial:shouldLoadScrollableContainer:looping:groupFilter:inputType:]
- -[_FEFocusMovementInfo initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:]
- -[_FEFocusMovementInfo initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:inputType:]
- -[_FEFocusMovementInfo initWithXPCDictionary:]
- -[_FEFocusMovementInfo init]
- -[_FEFocusMovementPerformer .cxx_destruct]
- -[_FEFocusMovementPerformer __findFocusCandidateInEnvironment:container:forRequest:minimumSearchArea:isLoadingScrollableContainer:]
- -[_FEFocusMovementPerformer _bestCandidateForLinearFocusMovement:]
- -[_FEFocusMovementPerformer _bestCandidateForNonLinearFocusMovement:]
- -[_FEFocusMovementPerformer _dummyFocusItemForFocusMovement:searchArea:parent:]
- -[_FEFocusMovementPerformer _environmentContainersToCheckForRequest:]
- -[_FEFocusMovementPerformer _findFocusCandidateByExhaustivelySearchingEnvironment:scrollableContainer:forRequest:]
- -[_FEFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]
- -[_FEFocusMovementPerformer _findFocusCandidateWithoutLoadingScrollableContentInEnvironment:container:forRequest:minimumSearchArea:]
- -[_FEFocusMovementPerformer _isMovementValidForFocusSequences:]
- -[_FEFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:]
- -[_FEFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:shouldLoadScrollableContainer:]
- -[_FEFocusMovementPerformer _nextLinearCandidateLoadingScrollableContentForRequest:]
- -[_FEFocusMovementPerformer contextForFocusMovement:]
- -[_FEFocusMovementPerformer delegate]
- -[_FEFocusMovementPerformer performFocusMovement:]
- -[_FEFocusMovementPerformer setDelegate:]
- -[_FEFocusMovementRequest .cxx_destruct]
- -[_FEFocusMovementRequest _requestByRedirectingRequestToFocusSystem:]
- -[_FEFocusMovementRequest allowsDeferral]
- -[_FEFocusMovementRequest allowsFocusingCurrentItem]
- -[_FEFocusMovementRequest allowsOverridingPreferedFocusEnvironments]
- -[_FEFocusMovementRequest fallbackRequest]
- -[_FEFocusMovementRequest focusSystem]
- -[_FEFocusMovementRequest focusedItemInfo]
- -[_FEFocusMovementRequest initWithFocusSystem:]
- -[_FEFocusMovementRequest init]
- -[_FEFocusMovementRequest inputDeviceInfo]
- -[_FEFocusMovementRequest isMovementRequest]
- -[_FEFocusMovementRequest movementInfo]
- -[_FEFocusMovementRequest overridesDeferredFocusUpdate]
- -[_FEFocusMovementRequest requiresEnvironmentValidation]
- -[_FEFocusMovementRequest requiresNextFocusedItem]
- -[_FEFocusMovementRequest searchInfo]
- -[_FEFocusMovementRequest setFocusedItemInfo:]
- -[_FEFocusMovementRequest setInputDeviceInfo:]
- -[_FEFocusMovementRequest setMovementInfo:]
- -[_FEFocusMovementRequest setOverridesDeferredFocusUpdate:]
- -[_FEFocusMovementRequest setSearchInfo:]
- -[_FEFocusMovementRequest setShouldPerformHapticFeedback:]
- -[_FEFocusMovementRequest shouldPerformHapticFeedback]
- -[_FEFocusMovementRequest shouldPlayFocusSound]
- -[_FEFocusMovementRequest shouldScrollIfNecessary]
- -[_FEFocusNullGroup _updateWithEnvironment:]
- -[_FEFocusNullGroup boundingBox]
- -[_FEFocusNullGroup primaryItem]
- -[_FEFocusPromiseRegion .cxx_destruct]
- -[_FEFocusPromiseRegion _debugDrawingConfigurationWithDebugInfo:]
- -[_FEFocusPromiseRegion _descriptionBuilder]
- -[_FEFocusPromiseRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusPromiseRegion _focusableBoundaries]
- -[_FEFocusPromiseRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
- -[_FEFocusPromiseRegion contentFulfillmentHandler]
- -[_FEFocusPromiseRegion initWithFrame:coordinateSpace:]
- -[_FEFocusPromiseRegion initWithFrame:coordinateSpace:identifier:]
- -[_FEFocusPromiseRegion isEqual:]
- -[_FEFocusPromiseRegion setContentFulfillmentHandler:]
- -[_FEFocusRegion .cxx_destruct]
- -[_FEFocusRegion _boundariesBlockingFocusMovementRequest:]
- -[_FEFocusRegion _canBeOccludedByRegionsAbove]
- -[_FEFocusRegion _canOccludeRegionsBelow]
- -[_FEFocusRegion _debugAssociatedObject]
- -[_FEFocusRegion _debugDrawingConfigurationWithDebugInfo:]
- -[_FEFocusRegion _defaultFocusItem]
- -[_FEFocusRegion _descriptionBuilder]
- -[_FEFocusRegion _didParticipateAsDestinationRegionInFocusUpdate:]
- -[_FEFocusRegion _effectiveBoundariesBlockingFocusMovementRequest:]
- -[_FEFocusRegion _effectiveFocusableBoundariesForHeading:]
- -[_FEFocusRegion _focusPriority]
- -[_FEFocusRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusRegion _focusableBoundaries]
- -[_FEFocusRegion _focusedItemForLinearSorting:inMap:withSnapshot:]
- -[_FEFocusRegion _ignoresSpeedBumpEdges]
- -[_FEFocusRegion _isUnclippable]
- -[_FEFocusRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:]
- -[_FEFocusRegion _preferredDistanceComparisonType]
- -[_FEFocusRegion _shouldCropRegionToSearchArea]
- -[_FEFocusRegion _shouldUseNextFocusedItemForLinearSorting]
- -[_FEFocusRegion _willParticipateAsDestinationRegionInFocusUpdate:]
- -[_FEFocusRegion description]
- -[_FEFocusRegion hash]
- -[_FEFocusRegion initWithFrame:coordinateSpace:]
- -[_FEFocusRegion isEqual:]
- -[_FEFocusRegion regionCoordinateSpace]
- -[_FEFocusRegion regionFrame]
- -[_FEFocusRegionContainerProxy .cxx_destruct]
- -[_FEFocusRegionContainerProxy _clippingRectInCoordinateSpace:]
- -[_FEFocusRegionContainerProxy _didUpdateFocusInContext:]
- -[_FEFocusRegionContainerProxy _focusItemContainer]
- -[_FEFocusRegionContainerProxy _focusSystem]
- -[_FEFocusRegionContainerProxy _isEligibleForFocusInteraction]
- -[_FEFocusRegionContainerProxy _isEligibleForFocusOcclusion]
- -[_FEFocusRegionContainerProxy _itemContainer]
- -[_FEFocusRegionContainerProxy _parentFocusEnvironment]
- -[_FEFocusRegionContainerProxy _preferredFocusRegionCoordinateSpace]
- -[_FEFocusRegionContainerProxy _searchForFocusRegionsInContext:]
- -[_FEFocusRegionContainerProxy _shouldUpdateFocusInContext:]
- -[_FEFocusRegionContainerProxy _ui_isUIFocusRegionContainerProxy]
- -[_FEFocusRegionContainerProxy allowsLazyLoading]
- -[_FEFocusRegionContainerProxy description]
- -[_FEFocusRegionContainerProxy environmentContainer]
- -[_FEFocusRegionContainerProxy hash]
- -[_FEFocusRegionContainerProxy initWithEnvironmentContainer:]
- -[_FEFocusRegionContainerProxy initWithOwningEnvironment:itemContainer:]
- -[_FEFocusRegionContainerProxy isEqual:]
- -[_FEFocusRegionContainerProxy owningEnvironment]
- -[_FEFocusRegionContainerProxy preferredFocusEnvironments]
- -[_FEFocusRegionContainerProxy setAllowsLazyLoading:]
- -[_FEFocusRegionContainerProxy setEnvironmentContainer:]
- -[_FEFocusRegionContainerProxy setNeedsFocusUpdate]
- -[_FEFocusRegionContainerProxy setShouldCreateRegionForGuideBehavior:]
- -[_FEFocusRegionContainerProxy setShouldCreateRegionForOwningItem:]
- -[_FEFocusRegionContainerProxy shouldCreateRegionForGuideBehavior]
- -[_FEFocusRegionContainerProxy shouldCreateRegionForOwningItem]
- -[_FEFocusRegionContainerProxy updateFocusIfNeeded]
- -[_FEFocusRegionDebugDrawingConfiguration .cxx_destruct]
- -[_FEFocusRegionDebugDrawingConfiguration associatedObject]
- -[_FEFocusRegionDebugDrawingConfiguration color]
- -[_FEFocusRegionDebugDrawingConfiguration dashedStroke]
- -[_FEFocusRegionDebugDrawingConfiguration initWithRegion:baseHue:patternAlpha:dashedStroke:]
- -[_FEFocusRegionDebugDrawingConfiguration patternAlpha]
- -[_FEFocusRegionDebugDrawingConfiguration pattern]
- -[_FEFocusRegionMovementInfo originatingHeading]
- -[_FEFocusRegionMovementInfo setOriginatingHeading:]
- -[_FEFocusRegionSearchContextState .cxx_destruct]
- -[_FEFocusRegionSearchContextState clippingRect]
- -[_FEFocusRegionSearchContextState initWithRegionContainer:focusSystem:clippingRect:]
- -[_FEFocusRegionSearchContextState regionContainerFocusSystem]
- -[_FEFocusRegionSearchContextState regionContainer]
- -[_FEFocusSearchInfo .cxx_destruct]
- -[_FEFocusSearchInfo evaluator]
- -[_FEFocusSearchInfo forceFocusToLeaveContainer]
- -[_FEFocusSearchInfo initWithFocusEvaluator:]
- -[_FEFocusSearchInfo setEvaluator:]
- -[_FEFocusSearchInfo setForceFocusToLeaveContainer:]
- -[_FEFocusSearchInfo setTreatFocusableItemAsLeaf:]
- -[_FEFocusSearchInfo shouldIncludeFocusItem:]
- -[_FEFocusSearchInfo treatFocusableItemAsLeaf]
- -[_FEFocusSpeedBumpRegion _boundariesBlockingFocusMovementRequest:]
- -[_FEFocusSpeedBumpRegion _canBeOccludedByRegionsAbove]
- -[_FEFocusSpeedBumpRegion _canOccludeRegionsBelow]
- -[_FEFocusSpeedBumpRegion _focusRegionWithAdjustedFrame:coordinateSpace:]
- -[_FEFocusSpeedBumpRegion _shouldCropRegionToSearchArea]
- -[_FEFocusSpeedBumpRegion initWithFrame:coordinateSpace:]
- -[_FEFocusSpeedBumpRegion initWithFrame:coordinateSpace:speedBumpEdges:]
- -[_FEFocusSpeedBumpRegion isEqual:]
- -[_FEFocusSpeedBumpRegion setSpeedBumpEdges:]
- -[_FEFocusSpeedBumpRegion speedBumpEdges]
- -[_FEFocusStateObserver .cxx_destruct]
- -[_FEFocusStateObserver addObserver:]
- -[_FEFocusStateObserver descriptionBuilder]
- -[_FEFocusStateObserver description]
- -[_FEFocusStateObserver init]
- -[_FEFocusStateObserver isActive]
- -[_FEFocusStateObserver notifyObserversIfNecessary]
- -[_FEFocusStateObserver performUpdatesAndNotifyObservers:]
- -[_FEFocusStateObserver removeObserver:]
- -[_FEFocusSystem .cxx_destruct]
- -[_FEFocusSystem _buildFocusItemAncestorCacheIfNecessary]
- -[_FEFocusSystem _cancelPendingFocusRestoration]
- -[_FEFocusSystem _clearDeferredFocusUpdateTarget]
- -[_FEFocusSystem _clearFocusItemAncestorCache]
- -[_FEFocusSystem _clippingRectInCoordinateSpace:]
- -[_FEFocusSystem _configureFocusDeferralIfNecessaryForContext:report:]
- -[_FEFocusSystem _contextForUpdateToEnvironment:]
- -[_FEFocusSystem _contextForUpdateToEnvironment:allowsOverridingPreferedFocusEnvironments:allowsDeferral:]
- -[_FEFocusSystem _debug_isEnvironmentEligibleForFocusUpdate:debugReport:]
- -[_FEFocusSystem _deepestPreferredFocusEnvironment]
- -[_FEFocusSystem _deepestPreferredFocusableItemCacheForCurrentUpdate]
- -[_FEFocusSystem _didFinishUpdatingFocusInContext:]
- -[_FEFocusSystem _didUpdateFocusInContext:]
- -[_FEFocusSystem _disappearingFocusEnvironment]
- -[_FEFocusSystem _dropFocusAndStartDeferring:suppressUpdate:]
- -[_FEFocusSystem _effectiveFocusDeferralBehavior]
- -[_FEFocusSystem _enableWithoutFocusRestoration]
- -[_FEFocusSystem _focusBehaviorDidChange]
- -[_FEFocusSystem _focusCastingController]
- -[_FEFocusSystem _focusEnvironmentDidAppear:]
- -[_FEFocusSystem _focusEnvironmentDidBecomeVisible:]
- -[_FEFocusSystem _focusEnvironmentWillBecomeInvisible:]
- -[_FEFocusSystem _focusEnvironmentWillDisappear:]
- -[_FEFocusSystem _focusGroupHistory]
- -[_FEFocusSystem _focusItemContainer]
- -[_FEFocusSystem _focusItemForValidation]
- -[_FEFocusSystem _focusMapContainer]
- -[_FEFocusSystem _focusMovementCache]
- -[_FEFocusSystem _focusSystemIsValid]
- -[_FEFocusSystem _focusedItemIsContainedInEnvironment:includeSelf:]
- -[_FEFocusSystem _focusedItemOrDeferralTarget]
- -[_FEFocusSystem _handleFailedFocusMovementRequest:withPerformer:]
- -[_FEFocusSystem _handleFocusMovementAction:]
- -[_FEFocusSystem _hasSeenFocusedItemDidExpire]
- -[_FEFocusSystem _hasValidItemForCurrentDeferralState]
- -[_FEFocusSystem _hostFocusSystem]
- -[_FEFocusSystem _isEligibleForFocusInteraction]
- -[_FEFocusSystem _isEligibleForFocusOcclusion]
- -[_FEFocusSystem _isEnabled]
- -[_FEFocusSystem _isEnvironmentEligibleForFocusUpdate:fallbackToEnvironment:debugReport:]
- -[_FEFocusSystem _isEnvironmentLocked:]
- -[_FEFocusSystem _isScrollingScrollableContainer:targetContentOffset:]
- -[_FEFocusSystem _lockEnvironment:]
- -[_FEFocusSystem _movementPerformer]
- -[_FEFocusSystem _notifyEnvironment:didUpdateFocusInContext:]
- -[_FEFocusSystem _overrideFocusDeferralBehavior]
- -[_FEFocusSystem _parentFocusEnvironment]
- -[_FEFocusSystem _performDeferredFocusUpdateIfAvailable]
- -[_FEFocusSystem _performFocusMovement:]
- -[_FEFocusSystem _performWithoutFocusUpdates:]
- -[_FEFocusSystem _postsFocusUpdateNotifications]
- -[_FEFocusSystem _prefersDeferralForFocusUpdateInContext:]
- -[_FEFocusSystem _prefersFocusContainment]
- -[_FEFocusSystem _prepareForTeardown]
- -[_FEFocusSystem _previousFocusedItem]
- -[_FEFocusSystem _reevaluateLockedEnvironments]
- -[_FEFocusSystem _requestFocusUpdate:]
- -[_FEFocusSystem _requiresFocusedItemToBeInHierarchy]
- -[_FEFocusSystem _resetFocusDeferral]
- -[_FEFocusSystem _sendDidUpdateFocusNotificationsInContext:]
- -[_FEFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]
- -[_FEFocusSystem _sendWillUpdateFocusNotificationsInContext:]
- -[_FEFocusSystem _setDeferredFocusUpdateTarget:]
- -[_FEFocusSystem _setEnabled:]
- -[_FEFocusSystem _setFocusCastingController:]
- -[_FEFocusSystem _setFocusMovementCache:]
- -[_FEFocusSystem _setNeedsFocusRestoration]
- -[_FEFocusSystem _setOverrideFocusDeferralBehavior:]
- -[_FEFocusSystem _shouldRestoreFocusInContext:]
- -[_FEFocusSystem _shouldReverseLayoutDirectionForEnvironment:]
- -[_FEFocusSystem _shouldReverseLinearWrappingForEnvironment:]
- -[_FEFocusSystem _shouldUpdateFocusInContext:]
- -[_FEFocusSystem _simulatedNonDeferredProgrammaticFocusUpdateToEnvironment:]
- -[_FEFocusSystem _startDeferringFocusIfSupported]
- -[_FEFocusSystem _tickHasSeenFocusedItemTimer:]
- -[_FEFocusSystem _topEnvironment]
- -[_FEFocusSystem _uiktest_disableFocusDeferral]
- -[_FEFocusSystem _uiktest_disableThrottle]
- -[_FEFocusSystem _uiktest_setPreviousFocusedItem:]
- -[_FEFocusSystem _uiktest_updateFocusToItem:]
- -[_FEFocusSystem _unlockEnvironment:]
- -[_FEFocusSystem _updateFocusImmediatelyToEnvironment:]
- -[_FEFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]
- -[_FEFocusSystem _updateFocusImmediatelyWithContext:]
- -[_FEFocusSystem _updateFocusUpdateThrottle]
- -[_FEFocusSystem _updateFocusWithContext:report:]
- -[_FEFocusSystem _updateWantsTreeLocking]
- -[_FEFocusSystem _validatedAppearingFocusEnvironmentRequest]
- -[_FEFocusSystem _validatedPendingFocusUpdateRequest]
- -[_FEFocusSystem behavior]
- -[_FEFocusSystem delegate]
- -[_FEFocusSystem description]
- -[_FEFocusSystem focusedItem]
- -[_FEFocusSystem initWithFocusBehavior:]
- -[_FEFocusSystem initWithFocusBehavior:enabled:]
- -[_FEFocusSystem init]
- -[_FEFocusSystem invalidateFocusItemContainer:]
- -[_FEFocusSystem pendingFocusMovementAction]
- -[_FEFocusSystem preferredFocusEnvironments]
- -[_FEFocusSystem requestFocusUpdateToEnvironment:]
- -[_FEFocusSystem setBehavior:]
- -[_FEFocusSystem setDelegate:]
- -[_FEFocusSystem setNeedsFocusUpdate]
- -[_FEFocusSystem setPendingFocusMovementAction:]
- -[_FEFocusSystem setWaitingForFocusMovementAction:]
- -[_FEFocusSystem treeLock]
- -[_FEFocusSystem updateFocusIfNeeded]
- -[_FEFocusSystem updateThrottle]
- -[_FEFocusSystem waitingForFocusMovementAction]
- -[_FEFocusUpdateContext .cxx_destruct]
- -[_FEFocusUpdateContext _cacheFocusBehavior]
- -[_FEFocusUpdateContext _commonAncestorEnvironment]
- -[_FEFocusUpdateContext _commonEnvironmentScrollableContainer]
- -[_FEFocusUpdateContext _destinationItemInfo]
- -[_FEFocusUpdateContext _destinationViewDistanceOffscreen]
- -[_FEFocusUpdateContext _didUpdateFocus]
- -[_FEFocusUpdateContext _focusGroupMap]
- -[_FEFocusUpdateContext _focusMapSearchInfo]
- -[_FEFocusUpdateContext _focusMapSnapshotDebugInfoArray]
- -[_FEFocusUpdateContext _focusMovement]
- -[_FEFocusUpdateContext _focusRedirectedByGuide]
- -[_FEFocusUpdateContext _focusVelocity]
- -[_FEFocusUpdateContext _focusedGuide]
- -[_FEFocusUpdateContext _groupFilter]
- -[_FEFocusUpdateContext _initWithContext:]
- -[_FEFocusUpdateContext _initWithFocusMovementRequest:nextFocusedItem:]
- -[_FEFocusUpdateContext _initWithFocusUpdateRequest:]
- -[_FEFocusUpdateContext _initialDestinationEnvironment]
- -[_FEFocusUpdateContext _isDeferredUpdate]
- -[_FEFocusUpdateContext _isFilteredToGroup]
- -[_FEFocusUpdateContext _isValidInFocusSystem:]
- -[_FEFocusUpdateContext _nextFocusedGroupIdentifier]
- -[_FEFocusUpdateContext _preferredFocusReport]
- -[_FEFocusUpdateContext _previouslyFocusedGroupIdentifier]
- -[_FEFocusUpdateContext _publicRegionMapSnapshots]
- -[_FEFocusUpdateContext _regionMapSnapshotsVisualRepresentation]
- -[_FEFocusUpdateContext _regionMapSnapshots]
- -[_FEFocusUpdateContext _request]
- -[_FEFocusUpdateContext _restoreRestrictedFocusMovementWithMovement:]
- -[_FEFocusUpdateContext _setCommonEnvironmentScrollableContainer:]
- -[_FEFocusUpdateContext _setDeferredUpdate:]
- -[_FEFocusUpdateContext _setDestinationViewDistanceOffscreen:]
- -[_FEFocusUpdateContext _setFocusGroupMap:]
- -[_FEFocusUpdateContext _setFocusMapSearchInfo:]
- -[_FEFocusUpdateContext _setFocusRedirectedByGuide:]
- -[_FEFocusUpdateContext _setFocusedGuide:]
- -[_FEFocusUpdateContext _setInitialDestinationEnvironment:]
- -[_FEFocusUpdateContext _setPreferredFocusReport:]
- -[_FEFocusUpdateContext _setRegionMapSnapshots:]
- -[_FEFocusUpdateContext _setSourceItemInfo:]
- -[_FEFocusUpdateContext _setValidationReport:]
- -[_FEFocusUpdateContext _sourceItemInfo]
- -[_FEFocusUpdateContext _updateDestinationItemIfNeeded]
- -[_FEFocusUpdateContext _updateWithFocusGroupMap:]
- -[_FEFocusUpdateContext _validate]
- -[_FEFocusUpdateContext _validationReport]
- -[_FEFocusUpdateContext _willUpdateFocusFromFocusedItem:]
- -[_FEFocusUpdateContext debugQuickLookObject]
- -[_FEFocusUpdateContext description]
- -[_FEFocusUpdateContext focusBehavior]
- -[_FEFocusUpdateContext focusHeading]
- -[_FEFocusUpdateContext init]
- -[_FEFocusUpdateContext nextFocusedItem]
- -[_FEFocusUpdateContext previouslyFocusedItem]
- -[_FEFocusUpdateReport .cxx_destruct]
- -[_FEFocusUpdateReport context]
- -[_FEFocusUpdateReport focusSystem]
- -[_FEFocusUpdateReport initWithFocusSystem:]
- -[_FEFocusUpdateReport init]
- -[_FEFocusUpdateReport setContext:]
- -[_FEFocusUpdateReport shouldLog]
- -[_FEFocusUpdateReportFormatter _bodyForReport:]
- -[_FEFocusUpdateReportFormatter _componentsFromReport:]
- -[_FEFocusUpdateReportFormatter _headerForReport:]
- -[_FEFocusUpdateReportFormatter stringFromReport:]
- -[_FEFocusUpdateRequest .cxx_destruct]
- -[_FEFocusUpdateRequest allowsDeferral]
- -[_FEFocusUpdateRequest allowsFocusingCurrentItem]
- -[_FEFocusUpdateRequest allowsOverridingPreferedFocusEnvironments]
- -[_FEFocusUpdateRequest cacheCurrentFocusSystem]
- -[_FEFocusUpdateRequest canMergeWithRequest:]
- -[_FEFocusUpdateRequest copyWithZone:]
- -[_FEFocusUpdateRequest destinationEnvironment]
- -[_FEFocusUpdateRequest environment]
- -[_FEFocusUpdateRequest focusSystem]
- -[_FEFocusUpdateRequest initWithEnvironment:]
- -[_FEFocusUpdateRequest initWithFocusSystem:environment:]
- -[_FEFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:]
- -[_FEFocusUpdateRequest init]
- -[_FEFocusUpdateRequest inputDeviceInfo]
- -[_FEFocusUpdateRequest isFocusRemovalRequest]
- -[_FEFocusUpdateRequest isMovementRequest]
- -[_FEFocusUpdateRequest isValidInFocusSystem:]
- -[_FEFocusUpdateRequest requestByMergingWithRequest:]
- -[_FEFocusUpdateRequest requestByRedirectingRequestToEnvironment:]
- -[_FEFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment]
- -[_FEFocusUpdateRequest requiresEnvironmentValidation]
- -[_FEFocusUpdateRequest requiresNextFocusedItem]
- -[_FEFocusUpdateRequest resetsUpdateThrottle]
- -[_FEFocusUpdateRequest setAllowsDeferral:]
- -[_FEFocusUpdateRequest setAllowsFocusingCurrentItem:]
- -[_FEFocusUpdateRequest setAllowsOverridingPreferedFocusEnvironments:]
- -[_FEFocusUpdateRequest setResetsUpdateThrottle:]
- -[_FEFocusUpdateRequest setScrollIfNecessary:]
- -[_FEFocusUpdateRequest setShouldPlayFocusSound:]
- -[_FEFocusUpdateRequest shouldPerformHapticFeedback]
- -[_FEFocusUpdateRequest shouldPlayFocusSound]
- -[_FEFocusUpdateRequest shouldScrollIfNecessary]
- -[_FEFocusUpdateThrottle .cxx_destruct]
- -[_FEFocusUpdateThrottle _performScheduledUpdate]
- -[_FEFocusUpdateThrottle didCreateProgrammaticFocusUpdateContext:]
- -[_FEFocusUpdateThrottle initWithUpdateHandler:]
- -[_FEFocusUpdateThrottle reset]
- -[_FEFocusUpdateThrottle scheduleProgrammaticFocusUpdate]
- -[_FEFocusUpdateThrottle teardown]
- -[_FETreeLock .cxx_destruct]
- -[_FETreeLock _validateLockedEnvironments]
- -[_FETreeLock description]
- -[_FETreeLock init]
- -[_FETreeLock isEnvironmentLocked:]
- -[_FETreeLock lockEnvironmentTree:]
- -[_FETreeLock lockedEnvironments]
- -[_FETreeLock unlockEnvironmentTree:]
- -[_FETreeLock validationTimer]
- -[_FETreeLockItem .cxx_destruct]
- -[_FETreeLockItem _cleanup:]
- -[_FETreeLockItem dealloc]
- -[_FETreeLockItem description]
- -[_FETreeLockItem environmentDescription]
- -[_FETreeLockItem environment]
- -[_FETreeLockItem initWithEnvironment:finalUnlockHandler:]
- -[_FETreeLockItem lockCallStackSymbols]
- -[_FETreeLockItem lockCount]
- -[_FETreeLockItem lockTime]
- -[_FETreeLockItem lock]
- -[_FETreeLockItem unlockCallStackSymbols]
- -[_FETreeLockItem unlock]
- -[_FETreeLockItem validate]
- -[_FEWeakHelper .cxx_destruct]
- -[_FEWeakHelper dealloc]
- -[_FEWeakHelper deallocationBlock]
- -[_FEWeakHelper initWithDeallocationBlock:]
- -[_FEWeakHelper invalidate]
- -[_FEWeakHelper setDeallocationBlock:]
- -[__FEDebugLogRootNode _isTransparent]
- -[__FEDebugLogRootNode description]
- GCC_except_table11
- GCC_except_table110
- GCC_except_table130
- GCC_except_table18
- GCC_except_table41
- GCC_except_table49
- GCC_except_table5
- GCC_except_table7
- GCC_except_table88
- _.str
- _.str.100
- _CFNotificationCenterPostNotification
- _OBJC_CLASS_$_FocusEngineDummy
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$__FEDebugIssue
- _OBJC_CLASS_$__FEDebugIssueReport
- _OBJC_CLASS_$__FEDebugIssueReportFormatter
- _OBJC_CLASS_$__FEDebugLogMessage
- _OBJC_CLASS_$__FEDebugLogNode
- _OBJC_CLASS_$__FEDebugLogNodeTreeStyle
- _OBJC_CLASS_$__FEDebugLogReport
- _OBJC_CLASS_$__FEDebugLogReportFormatter
- _OBJC_CLASS_$__FEDebugLogStack
- _OBJC_CLASS_$__FEDebugLogStatement
- _OBJC_CLASS_$__FEDebugReportComponents
- _OBJC_CLASS_$__FEDebugReportFormatter
- _OBJC_CLASS_$__FEFocusCastingController
- _OBJC_CLASS_$__FEFocusContainerGuideRegion
- _OBJC_CLASS_$__FEFocusDebugger
- _OBJC_CLASS_$__FEFocusDebuggerStringOutput
- _OBJC_CLASS_$__FEFocusEnvironmentContainerTuple
- _OBJC_CLASS_$__FEFocusEnvironmentPreferenceCache
- _OBJC_CLASS_$__FEFocusEnvironmentPreferenceCacheNode
- _OBJC_CLASS_$__FEFocusEnvironmentPreferenceEnumerationContext
- _OBJC_CLASS_$__FEFocusEnvironmentPreferenceEnumerator
- _OBJC_CLASS_$__FEFocusEnvironmentScrollableContainerTuple
- _OBJC_CLASS_$__FEFocusGroup
- _OBJC_CLASS_$__FEFocusGroupHistory
- _OBJC_CLASS_$__FEFocusGroupMap
- _OBJC_CLASS_$__FEFocusGuideRegion
- _OBJC_CLASS_$__FEFocusInputDeviceInfo
- _OBJC_CLASS_$__FEFocusItemDummy
- _OBJC_CLASS_$__FEFocusItemFrameReporter
- _OBJC_CLASS_$__FEFocusItemInfo
- _OBJC_CLASS_$__FEFocusItemRegion
- _OBJC_CLASS_$__FEFocusLinearMovementCache
- _OBJC_CLASS_$__FEFocusLinearMovementSequence
- _OBJC_CLASS_$__FEFocusMap
- _OBJC_CLASS_$__FEFocusMapRect
- _OBJC_CLASS_$__FEFocusMapSearchInfo
- _OBJC_CLASS_$__FEFocusMapSnapshot
- _OBJC_CLASS_$__FEFocusMapSnapshotDebugInfo
- _OBJC_CLASS_$__FEFocusMapSnapshotter
- _OBJC_CLASS_$__FEFocusMovementHint
- _OBJC_CLASS_$__FEFocusMovementInfo
- _OBJC_CLASS_$__FEFocusMovementPerformer
- _OBJC_CLASS_$__FEFocusMovementRequest
- _OBJC_CLASS_$__FEFocusNullGroup
- _OBJC_CLASS_$__FEFocusPromiseRegion
- _OBJC_CLASS_$__FEFocusRegion
- _OBJC_CLASS_$__FEFocusRegionContainerProxy
- _OBJC_CLASS_$__FEFocusRegionDebugDrawingConfiguration
- _OBJC_CLASS_$__FEFocusRegionDebugQuickLook
- _OBJC_CLASS_$__FEFocusRegionEvaluator
- _OBJC_CLASS_$__FEFocusRegionMovementInfo
- _OBJC_CLASS_$__FEFocusRegionSearchContextState
- _OBJC_CLASS_$__FEFocusSearchInfo
- _OBJC_CLASS_$__FEFocusSpeedBumpRegion
- _OBJC_CLASS_$__FEFocusStateObserver
- _OBJC_CLASS_$__FEFocusSystem
- _OBJC_CLASS_$__FEFocusUpdateContext
- _OBJC_CLASS_$__FEFocusUpdateReport
- _OBJC_CLASS_$__FEFocusUpdateReportFormatter
- _OBJC_CLASS_$__FEFocusUpdateRequest
- _OBJC_CLASS_$__FEFocusUpdateThrottle
- _OBJC_CLASS_$__FETreeLock
- _OBJC_CLASS_$__FETreeLockItem
- _OBJC_CLASS_$__FEWeakHelper
- _OBJC_CLASS_$___FEDebugLogRootNode
- _OBJC_IVAR_$__FEDebugIssue._description
- _OBJC_IVAR_$__FEDebugIssue._prefix
- _OBJC_IVAR_$__FEDebugIssue._subissueReport
- _OBJC_IVAR_$__FEDebugIssueReport._mutableIssues
- _OBJC_IVAR_$__FEDebugLogMessage._string
- _OBJC_IVAR_$__FEDebugLogNodeTreeStyle._intermediate
- _OBJC_IVAR_$__FEDebugLogNodeTreeStyle._lastNode
- _OBJC_IVAR_$__FEDebugLogNodeTreeStyle._node
- _OBJC_IVAR_$__FEDebugLogNodeTreeStyle._trailing
- _OBJC_IVAR_$__FEDebugLogReport._currentIndentLevel
- _OBJC_IVAR_$__FEDebugLogReport._fallbackMessagePrefixHandler
- _OBJC_IVAR_$__FEDebugLogReport._prefixStack
- _OBJC_IVAR_$__FEDebugLogReport._statements
- _OBJC_IVAR_$__FEDebugLogStack._stack
- _OBJC_IVAR_$__FEDebugLogStatement._indentLevel
- _OBJC_IVAR_$__FEDebugLogStatement._prefix
- _OBJC_IVAR_$__FEDebugLogStatement._text
- _OBJC_IVAR_$__FEDebugLogStatement._type
- _OBJC_IVAR_$__FEDebugReportComponents._body
- _OBJC_IVAR_$__FEDebugReportComponents._footer
- _OBJC_IVAR_$__FEDebugReportComponents._header
- _OBJC_IVAR_$__FEDebugReportFormatter._extraBodyIndentLevel
- _OBJC_IVAR_$__FEDebugReportFormatter._indentLevel
- _OBJC_IVAR_$__FEDebugReportFormatter._indentString
- _OBJC_IVAR_$__FEFocusCastingController._entryPointAxis
- _OBJC_IVAR_$__FEFocusCastingController._entryPointMemorizationTimeout
- _OBJC_IVAR_$__FEFocusCastingController._focusCastingIndicator
- _OBJC_IVAR_$__FEFocusCastingController._focusEntryIndicator
- _OBJC_IVAR_$__FEFocusCastingController._focusMovementIndicator
- _OBJC_IVAR_$__FEFocusCastingController._focusSystem
- _OBJC_IVAR_$__FEFocusCastingController._isRememberingEntryPoint
- _OBJC_IVAR_$__FEFocusCastingController._screenEntryPoint
- _OBJC_IVAR_$__FEFocusContainerGuideRegion._contentFocusRegionContainer
- _OBJC_IVAR_$__FEFocusDebuggerStringOutput._outputString
- _OBJC_IVAR_$__FEFocusEnvironmentContainerTuple._isScrollableContainer
- _OBJC_IVAR_$__FEFocusEnvironmentContainerTuple._itemContainer
- _OBJC_IVAR_$__FEFocusEnvironmentContainerTuple._owningEnvironment
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCache._environmentsMap
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCacheNode._childNodes
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCacheNode._environment
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCacheNode._flags
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCacheNode._parentNodes
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceCacheNode._resolvedEnvironment
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._allVisitedEnvironments
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._cachedPreferredEnvironments
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._cachedPrefersNothingFocused
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._debugStack
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._delegate
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._environment
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._focusSystem
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._hasNeverPoppedInPreferredSubtree
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._hasResolvedPreferredFocusEnvironments
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._lastPrimaryPreferredEnvironment
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._preferredEnvironmentsMap
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._preferredSubtree
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._preferredSubtreeEntryPoint
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerationContext._visitedEnvironmentStack
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerator._allowsInferringPreferences
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerator._debugLog
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerator._didVisitAllPreferencesForEnvironmentHandler
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerator._enumerationMode
- _OBJC_IVAR_$__FEFocusEnvironmentPreferenceEnumerator._shouldInferPreferenceForEnvironmentHandler
- _OBJC_IVAR_$__FEFocusEnvironmentScrollableContainerTuple._owningEnvironment
- _OBJC_IVAR_$__FEFocusEnvironmentScrollableContainerTuple._scrollableContainer
- _OBJC_IVAR_$__FEFocusGroup._boundingBox
- _OBJC_IVAR_$__FEFocusGroup._childGroups
- _OBJC_IVAR_$__FEFocusGroup._coordinateSpace
- _OBJC_IVAR_$__FEFocusGroup._flags
- _OBJC_IVAR_$__FEFocusGroup._identifier
- _OBJC_IVAR_$__FEFocusGroup._items
- _OBJC_IVAR_$__FEFocusGroup._owningEnvironment
- _OBJC_IVAR_$__FEFocusGroup._parentGroup
- _OBJC_IVAR_$__FEFocusGroup._primaryItem
- _OBJC_IVAR_$__FEFocusGroup._primaryRect
- _OBJC_IVAR_$__FEFocusGroupHistory._groupToItemMap
- _OBJC_IVAR_$__FEFocusGroupMap._coordinateSpace
- _OBJC_IVAR_$__FEFocusGroupMap._environmentToGroupMap
- _OBJC_IVAR_$__FEFocusGroupMap._focusGroups
- _OBJC_IVAR_$__FEFocusGroupMap._identifierToGroupMap
- _OBJC_IVAR_$__FEFocusGroupMap._identifierToPrimaryItemMap
- _OBJC_IVAR_$__FEFocusGroupMap._nullGroup
- _OBJC_IVAR_$__FEFocusGroupMap._standInItemsMap
- _OBJC_IVAR_$__FEFocusInputDeviceInfo._senderID
- _OBJC_IVAR_$__FEFocusItemDummy.__focusFrame
- _OBJC_IVAR_$__FEFocusItemDummy.__parentFocusEnvironment
- _OBJC_IVAR_$__FEFocusItemFrameReporter._enabled
- _OBJC_IVAR_$__FEFocusItemFrameReporter._focusSystem
- _OBJC_IVAR_$__FEFocusItemFrameReporter._focusedFrameUpdateTimer
- _OBJC_IVAR_$__FEFocusItemFrameReporter._hasStagedFocusFrameUpdate
- _OBJC_IVAR_$__FEFocusItemInfo._ancestorEnvironmentScrollableContainers
- _OBJC_IVAR_$__FEFocusItemInfo._flags
- _OBJC_IVAR_$__FEFocusItemInfo._focusMovementFlippedHorizontally
- _OBJC_IVAR_$__FEFocusItemInfo._focusTouchSensitivityStyle
- _OBJC_IVAR_$__FEFocusItemInfo._focusedRegion
- _OBJC_IVAR_$__FEFocusItemInfo._inheritedFocusMovementStyle
- _OBJC_IVAR_$__FEFocusItemInfo._item
- _OBJC_IVAR_$__FEFocusItemInfo._rotaryFocusMovementAxis
- _OBJC_IVAR_$__FEFocusLinearMovementCache._cooldownThreshold
- _OBJC_IVAR_$__FEFocusLinearMovementCache._flags
- _OBJC_IVAR_$__FEFocusLinearMovementCache._lastUpdate
- _OBJC_IVAR_$__FEFocusLinearMovementCache._linearItems
- _OBJC_IVAR_$__FEFocusLinearMovementCache._parentEnvironments
- _OBJC_IVAR_$__FEFocusLinearMovementSequence._items
- _OBJC_IVAR_$__FEFocusLinearMovementSequence._looping
- _OBJC_IVAR_$__FEFocusLinearMovementSequence._restrictEnteringSequence
- _OBJC_IVAR_$__FEFocusMap._coordinateSpace
- _OBJC_IVAR_$__FEFocusMap._defaultItemSearchInfo
- _OBJC_IVAR_$__FEFocusMap._focusGroupMap
- _OBJC_IVAR_$__FEFocusMap._focusMovementSearchInfo
- _OBJC_IVAR_$__FEFocusMap._focusSystem
- _OBJC_IVAR_$__FEFocusMap._ignoresRootContainerClippingRect
- _OBJC_IVAR_$__FEFocusMap._minimumSearchArea
- _OBJC_IVAR_$__FEFocusMap._minimumSearchAreaIsEmpty
- _OBJC_IVAR_$__FEFocusMap._needsSearchInfo
- _OBJC_IVAR_$__FEFocusMap._rootContainer
- _OBJC_IVAR_$__FEFocusMap._rootContainerProxy
- _OBJC_IVAR_$__FEFocusMap._searchInfo
- _OBJC_IVAR_$__FEFocusMap._trackingSearchInfo
- _OBJC_IVAR_$__FEFocusMapRect._coordinateSpace
- _OBJC_IVAR_$__FEFocusMapRect._frame
- _OBJC_IVAR_$__FEFocusMapSearchInfo._didFindFocusBlockingBoundary
- _OBJC_IVAR_$__FEFocusMapSearchInfo._focusGroupMap
- _OBJC_IVAR_$__FEFocusMapSearchInfo._hasOnlyStaticContent
- _OBJC_IVAR_$__FEFocusMapSearchInfo._linearSortedFocusItems
- _OBJC_IVAR_$__FEFocusMapSearchInfo._mutableDestinationRegions
- _OBJC_IVAR_$__FEFocusMapSearchInfo._mutableSnapshots
- _OBJC_IVAR_$__FEFocusMapSearchInfo._searchInfo
- _OBJC_IVAR_$__FEFocusMapSnapshot._eligibleEnvironments
- _OBJC_IVAR_$__FEFocusMapSnapshot._filteredOriginalRegions
- _OBJC_IVAR_$__FEFocusMapSnapshot._flags
- _OBJC_IVAR_$__FEFocusMapSnapshot._focusSystem
- _OBJC_IVAR_$__FEFocusMapSnapshot._focusedRegion
- _OBJC_IVAR_$__FEFocusMapSnapshot._ineligibleEnvironments
- _OBJC_IVAR_$__FEFocusMapSnapshot._mapArea
- _OBJC_IVAR_$__FEFocusMapSnapshot._movementInfo
- _OBJC_IVAR_$__FEFocusMapSnapshot._mutableUnoccludedRegions
- _OBJC_IVAR_$__FEFocusMapSnapshot._regionFrameCache
- _OBJC_IVAR_$__FEFocusMapSnapshot._regionToFocusItemCache
- _OBJC_IVAR_$__FEFocusMapSnapshot._regionToOccludingRegionsMap
- _OBJC_IVAR_$__FEFocusMapSnapshot._regions
- _OBJC_IVAR_$__FEFocusMapSnapshot._regionsContainer
- _OBJC_IVAR_$__FEFocusMapSnapshot._rootContainer
- _OBJC_IVAR_$__FEFocusMapSnapshot._searchArea
- _OBJC_IVAR_$__FEFocusMapSnapshot._searchInfo
- _OBJC_IVAR_$__FEFocusMapSnapshot._stateStack
- _OBJC_IVAR_$__FEFocusMapSnapshot._subregionToRegionMap
- _OBJC_IVAR_$__FEFocusMapSnapshot._uncachableEnvironments
- _OBJC_IVAR_$__FEFocusMapSnapshot._visitedRegionContainers
- _OBJC_IVAR_$__FEFocusMapSnapshotDebugInfo._focusMapSearchInfo
- _OBJC_IVAR_$__FEFocusMapSnapshotDebugInfo._image
- _OBJC_IVAR_$__FEFocusMapSnapshotDebugInfo._imageAnchorPoint
- _OBJC_IVAR_$__FEFocusMapSnapshotDebugInfo._snapshot
- _OBJC_IVAR_$__FEFocusMapSnapshotter._clipToSnapshotRect
- _OBJC_IVAR_$__FEFocusMapSnapshotter._coordinateSpace
- _OBJC_IVAR_$__FEFocusMapSnapshotter._focusSystem
- _OBJC_IVAR_$__FEFocusMapSnapshotter._focusedRegion
- _OBJC_IVAR_$__FEFocusMapSnapshotter._ignoresRootContainerClippingRect
- _OBJC_IVAR_$__FEFocusMapSnapshotter._movementInfo
- _OBJC_IVAR_$__FEFocusMapSnapshotter._regionsContainer
- _OBJC_IVAR_$__FEFocusMapSnapshotter._rootContainer
- _OBJC_IVAR_$__FEFocusMapSnapshotter._searchInfo
- _OBJC_IVAR_$__FEFocusMapSnapshotter._snapshotFrame
- _OBJC_IVAR_$__FEFocusMapSnapshotter._snapshotFrameIsEmpty
- _OBJC_IVAR_$__FEFocusMovementHint._movementDirection
- _OBJC_IVAR_$__FEFocusMovementHint._rotationAmount
- _OBJC_IVAR_$__FEFocusMovementHint._translationAmount
- _OBJC_IVAR_$__FEFocusMovementInfo._fallbackMovementOriginatingFrame
- _OBJC_IVAR_$__FEFocusMovementInfo._groupFilter
- _OBJC_IVAR_$__FEFocusMovementInfo._heading
- _OBJC_IVAR_$__FEFocusMovementInfo._inputType
- _OBJC_IVAR_$__FEFocusMovementInfo._isInitialMovement
- _OBJC_IVAR_$__FEFocusMovementInfo._isVelocityBased
- _OBJC_IVAR_$__FEFocusMovementInfo._linearHeading
- _OBJC_IVAR_$__FEFocusMovementInfo._looping
- _OBJC_IVAR_$__FEFocusMovementInfo._shouldLoadScrollableContainer
- _OBJC_IVAR_$__FEFocusMovementInfo._velocity
- _OBJC_IVAR_$__FEFocusMovementPerformer._delegate
- _OBJC_IVAR_$__FEFocusMovementRequest._focusSystem
- _OBJC_IVAR_$__FEFocusMovementRequest._focusedItemInfo
- _OBJC_IVAR_$__FEFocusMovementRequest._inputDeviceInfo
- _OBJC_IVAR_$__FEFocusMovementRequest._movementInfo
- _OBJC_IVAR_$__FEFocusMovementRequest._overridesDeferredFocusUpdate
- _OBJC_IVAR_$__FEFocusMovementRequest._searchInfo
- _OBJC_IVAR_$__FEFocusMovementRequest._shouldPerformHapticFeedback
- _OBJC_IVAR_$__FEFocusPromiseRegion._fullfillmentCount
- _OBJC_IVAR_$__FEFocusRegion._regionCoordinateSpace
- _OBJC_IVAR_$__FEFocusRegion._regionFrame
- _OBJC_IVAR_$__FEFocusRegionContainerProxy._allowsLazyLoading
- _OBJC_IVAR_$__FEFocusRegionContainerProxy._environmentContainer
- _OBJC_IVAR_$__FEFocusRegionContainerProxy._shouldCreateRegionForGuideBehavior
- _OBJC_IVAR_$__FEFocusRegionContainerProxy._shouldCreateRegionForOwningItem
- _OBJC_IVAR_$__FEFocusRegionDebugDrawingConfiguration._associatedObject
- _OBJC_IVAR_$__FEFocusRegionDebugDrawingConfiguration._color
- _OBJC_IVAR_$__FEFocusRegionDebugDrawingConfiguration._dashedStroke
- _OBJC_IVAR_$__FEFocusRegionDebugDrawingConfiguration._pattern
- _OBJC_IVAR_$__FEFocusRegionDebugDrawingConfiguration._patternAlpha
- _OBJC_IVAR_$__FEFocusRegionMovementInfo._originatingHeading
- _OBJC_IVAR_$__FEFocusRegionSearchContextState._clippingRect
- _OBJC_IVAR_$__FEFocusRegionSearchContextState._regionContainer
- _OBJC_IVAR_$__FEFocusRegionSearchContextState._regionContainerFocusSystem
- _OBJC_IVAR_$__FEFocusSearchInfo._evaluator
- _OBJC_IVAR_$__FEFocusSearchInfo._forceFocusToLeaveContainer
- _OBJC_IVAR_$__FEFocusSearchInfo._treatFocusableItemAsLeaf
- _OBJC_IVAR_$__FEFocusSpeedBumpRegion._speedBumpEdges
- _OBJC_IVAR_$__FEFocusStateObserver._flags
- _OBJC_IVAR_$__FEFocusStateObserver._observers
- _OBJC_IVAR_$__FEFocusSystem._appearingFocusEnvironment
- _OBJC_IVAR_$__FEFocusSystem._behavior
- _OBJC_IVAR_$__FEFocusSystem._deepestPreferredFocusEnvironment
- _OBJC_IVAR_$__FEFocusSystem._deepestPreferredFocusableItemCacheForCurrentUpdate
- _OBJC_IVAR_$__FEFocusSystem._deferredFocusUpdateTarget
- _OBJC_IVAR_$__FEFocusSystem._delegate
- _OBJC_IVAR_$__FEFocusSystem._disappearingFocusEnvironment
- _OBJC_IVAR_$__FEFocusSystem._enabled
- _OBJC_IVAR_$__FEFocusSystem._flags
- _OBJC_IVAR_$__FEFocusSystem._focusCastingController
- _OBJC_IVAR_$__FEFocusSystem._focusGroupHistory
- _OBJC_IVAR_$__FEFocusSystem._focusItemAncestorCache
- _OBJC_IVAR_$__FEFocusSystem._focusMovementCache
- _OBJC_IVAR_$__FEFocusSystem._focusedItem
- _OBJC_IVAR_$__FEFocusSystem._hasSeenFocusedItemDidExpireTimer
- _OBJC_IVAR_$__FEFocusSystem._movementPerformer
- _OBJC_IVAR_$__FEFocusSystem._overrideFocusDeferralBehavior
- _OBJC_IVAR_$__FEFocusSystem._pendingFocusMovementAction
- _OBJC_IVAR_$__FEFocusSystem._pendingFocusUpdateRequest
- _OBJC_IVAR_$__FEFocusSystem._previousFocusedItem
- _OBJC_IVAR_$__FEFocusSystem._treeLock
- _OBJC_IVAR_$__FEFocusSystem._updateThrottle
- _OBJC_IVAR_$__FEFocusSystem._waitingForFocusMovementAction
- _OBJC_IVAR_$__FEFocusUpdateContext._commonAncestorEnvironment
- _OBJC_IVAR_$__FEFocusUpdateContext._commonEnvironmentScrollableContainer
- _OBJC_IVAR_$__FEFocusUpdateContext._deferredUpdate
- _OBJC_IVAR_$__FEFocusUpdateContext._destinationItemInfo
- _OBJC_IVAR_$__FEFocusUpdateContext._destinationViewDistanceOffscreen
- _OBJC_IVAR_$__FEFocusUpdateContext._flags
- _OBJC_IVAR_$__FEFocusUpdateContext._focusBehavior
- _OBJC_IVAR_$__FEFocusUpdateContext._focusGroupMap
- _OBJC_IVAR_$__FEFocusUpdateContext._focusMapSearchInfo
- _OBJC_IVAR_$__FEFocusUpdateContext._focusMovement
- _OBJC_IVAR_$__FEFocusUpdateContext._focusRedirectedByGuide
- _OBJC_IVAR_$__FEFocusUpdateContext._focusedGuide
- _OBJC_IVAR_$__FEFocusUpdateContext._initialDestinationEnvironment
- _OBJC_IVAR_$__FEFocusUpdateContext._nextFocusedGroupIdentifier
- _OBJC_IVAR_$__FEFocusUpdateContext._preferredFocusReport
- _OBJC_IVAR_$__FEFocusUpdateContext._previouslyFocusedGroupIdentifier
- _OBJC_IVAR_$__FEFocusUpdateContext._regionMapSnapshots
- _OBJC_IVAR_$__FEFocusUpdateContext._regionMapSnapshotsVisualRepresentation
- _OBJC_IVAR_$__FEFocusUpdateContext._request
- _OBJC_IVAR_$__FEFocusUpdateContext._sourceItemInfo
- _OBJC_IVAR_$__FEFocusUpdateContext._validationReport
- _OBJC_IVAR_$__FEFocusUpdateReport._context
- _OBJC_IVAR_$__FEFocusUpdateReport._focusSystem
- _OBJC_IVAR_$__FEFocusUpdateRequest._allowsDeferral
- _OBJC_IVAR_$__FEFocusUpdateRequest._allowsFocusingCurrentItem
- _OBJC_IVAR_$__FEFocusUpdateRequest._allowsOverridingPreferedFocusEnvironments
- _OBJC_IVAR_$__FEFocusUpdateRequest._destinationEnvironment
- _OBJC_IVAR_$__FEFocusUpdateRequest._environment
- _OBJC_IVAR_$__FEFocusUpdateRequest._focusSystem
- _OBJC_IVAR_$__FEFocusUpdateRequest._isFocusRemovalRequest
- _OBJC_IVAR_$__FEFocusUpdateRequest._resetsUpdateThrottle
- _OBJC_IVAR_$__FEFocusUpdateRequest._scrollIfNecessary
- _OBJC_IVAR_$__FEFocusUpdateRequest._shouldPlayFocusSound
- _OBJC_IVAR_$__FEFocusUpdateThrottle._currentTimeout
- _OBJC_IVAR_$__FEFocusUpdateThrottle._lastUpdate
- _OBJC_IVAR_$__FEFocusUpdateThrottle._nilUpdateCount
- _OBJC_IVAR_$__FEFocusUpdateThrottle._updateHandler
- _OBJC_IVAR_$__FEFocusUpdateThrottle._updateIsScheduled
- _OBJC_IVAR_$__FEFocusUpdateThrottle._updateTimer
- _OBJC_IVAR_$__FETreeLock._lockedEnvironments
- _OBJC_IVAR_$__FETreeLock._validationTimer
- _OBJC_IVAR_$__FETreeLockItem._didCleanup
- _OBJC_IVAR_$__FETreeLockItem._didSoftAssert
- _OBJC_IVAR_$__FETreeLockItem._environment
- _OBJC_IVAR_$__FETreeLockItem._environmentDescription
- _OBJC_IVAR_$__FETreeLockItem._finalUnlockHandler
- _OBJC_IVAR_$__FETreeLockItem._lockCallStackSymbols
- _OBJC_IVAR_$__FETreeLockItem._lockCount
- _OBJC_IVAR_$__FETreeLockItem._lockTime
- _OBJC_IVAR_$__FETreeLockItem._unlockCallStackSymbols
- _OBJC_IVAR_$__FETreeLockItem._unsafeEnvironment
- _OBJC_IVAR_$__FEWeakHelper._deallocationBlock
- _OBJC_METACLASS_$_FocusEngineDummy
- _OBJC_METACLASS_$__FEDebugIssue
- _OBJC_METACLASS_$__FEDebugIssueReport
- _OBJC_METACLASS_$__FEDebugIssueReportFormatter
- _OBJC_METACLASS_$__FEDebugLogMessage
- _OBJC_METACLASS_$__FEDebugLogNode
- _OBJC_METACLASS_$__FEDebugLogNodeTreeStyle
- _OBJC_METACLASS_$__FEDebugLogReport
- _OBJC_METACLASS_$__FEDebugLogReportFormatter
- _OBJC_METACLASS_$__FEDebugLogStack
- _OBJC_METACLASS_$__FEDebugLogStatement
- _OBJC_METACLASS_$__FEDebugReportComponents
- _OBJC_METACLASS_$__FEDebugReportFormatter
- _OBJC_METACLASS_$__FEFocusCastingController
- _OBJC_METACLASS_$__FEFocusContainerGuideRegion
- _OBJC_METACLASS_$__FEFocusDebugger
- _OBJC_METACLASS_$__FEFocusDebuggerStringOutput
- _OBJC_METACLASS_$__FEFocusEnvironmentContainerTuple
- _OBJC_METACLASS_$__FEFocusEnvironmentPreferenceCache
- _OBJC_METACLASS_$__FEFocusEnvironmentPreferenceCacheNode
- _OBJC_METACLASS_$__FEFocusEnvironmentPreferenceEnumerationContext
- _OBJC_METACLASS_$__FEFocusEnvironmentPreferenceEnumerator
- _OBJC_METACLASS_$__FEFocusEnvironmentScrollableContainerTuple
- _OBJC_METACLASS_$__FEFocusGroup
- _OBJC_METACLASS_$__FEFocusGroupHistory
- _OBJC_METACLASS_$__FEFocusGroupMap
- _OBJC_METACLASS_$__FEFocusGuideRegion
- _OBJC_METACLASS_$__FEFocusInputDeviceInfo
- _OBJC_METACLASS_$__FEFocusItemDummy
- _OBJC_METACLASS_$__FEFocusItemFrameReporter
- _OBJC_METACLASS_$__FEFocusItemInfo
- _OBJC_METACLASS_$__FEFocusItemRegion
- _OBJC_METACLASS_$__FEFocusLinearMovementCache
- _OBJC_METACLASS_$__FEFocusLinearMovementSequence
- _OBJC_METACLASS_$__FEFocusMap
- _OBJC_METACLASS_$__FEFocusMapRect
- _OBJC_METACLASS_$__FEFocusMapSearchInfo
- _OBJC_METACLASS_$__FEFocusMapSnapshot
- _OBJC_METACLASS_$__FEFocusMapSnapshotDebugInfo
- _OBJC_METACLASS_$__FEFocusMapSnapshotter
- _OBJC_METACLASS_$__FEFocusMovementHint
- _OBJC_METACLASS_$__FEFocusMovementInfo
- _OBJC_METACLASS_$__FEFocusMovementPerformer
- _OBJC_METACLASS_$__FEFocusMovementRequest
- _OBJC_METACLASS_$__FEFocusNullGroup
- _OBJC_METACLASS_$__FEFocusPromiseRegion
- _OBJC_METACLASS_$__FEFocusRegion
- _OBJC_METACLASS_$__FEFocusRegionContainerProxy
- _OBJC_METACLASS_$__FEFocusRegionDebugDrawingConfiguration
- _OBJC_METACLASS_$__FEFocusRegionDebugQuickLook
- _OBJC_METACLASS_$__FEFocusRegionEvaluator
- _OBJC_METACLASS_$__FEFocusRegionMovementInfo
- _OBJC_METACLASS_$__FEFocusRegionSearchContextState
- _OBJC_METACLASS_$__FEFocusSearchInfo
- _OBJC_METACLASS_$__FEFocusSpeedBumpRegion
- _OBJC_METACLASS_$__FEFocusStateObserver
- _OBJC_METACLASS_$__FEFocusSystem
- _OBJC_METACLASS_$__FEFocusUpdateContext
- _OBJC_METACLASS_$__FEFocusUpdateReport
- _OBJC_METACLASS_$__FEFocusUpdateReportFormatter
- _OBJC_METACLASS_$__FEFocusUpdateRequest
- _OBJC_METACLASS_$__FEFocusUpdateThrottle
- _OBJC_METACLASS_$__FETreeLock
- _OBJC_METACLASS_$__FETreeLockItem
- _OBJC_METACLASS_$__FEWeakHelper
- _OBJC_METACLASS_$___FEDebugLogRootNode
- _UIKitCoreLibraryCore
- _UIKitCoreLibraryCore.frameworkLibrary
- __FEAXAssignFocusToItem
- __FEAXAssignFocusToItemWithOptions
- __FEAXFocusItemIsFocusableInFocusSystemWithSearchInfo
- __FEDistanceBetweenRects
- __FEFocusAncestorEnvironmentScrollableContainers
- __FEFocusCastingPointNone
- __FEFocusClearCachedSensitivitySettingObserver
- __FEFocusDeferralModeForItem
- __FEFocusDidUpdateNotification
- __FEFocusEngineCommonEnvironmentScrollableContainerForItems
- __FEFocusEngineFirstScrollableContainerTupleThatScrollsForItem
- __FEFocusEngineGestureDidBeginNotification
- __FEFocusEngineScrollableContainerCanScroll
- __FEFocusEnvironmentAllowsFocusToLeaveViaHeading
- __FEFocusEnvironmentContainerFrameInCoordinateSpace
- __FEFocusEnvironmentEffectivePreferredFocusEnvironments
- __FEFocusEnvironmentEnumerateAncestorEnvironments
- __FEFocusEnvironmentFirstCommonAncestor
- __FEFocusEnvironmentInheritedFocusMovementStyle
- __FEFocusEnvironmentIsAncestorOfEnvironment
- __FEFocusEnvironmentIsEligibleForFocusInteraction
- __FEFocusEnvironmentIsEligibleForFocusOcclusion
- __FEFocusEnvironmentIsViewOrRespondsToSelector
- __FEFocusEnvironmentIsViewOrViewControllerOrRespondsToSelector
- __FEFocusEnvironmentPreferredFocusEnvironments
- __FEFocusEnvironmentPreferredFocusMapContainer
- __FEFocusEnvironmentPrefersFocusContainment
- __FEFocusEnvironmentResolvedRotaryFocusMovementAxis
- __FEFocusEnvironmentRootAncestorEnvironment
- __FEFocusEnvironmentRotaryFocusMovementAxis
- __FEFocusEnvironmentShouldUpdateFocus
- __FEFocusEnvironmentsHaveCommonHierarchy
- __FEFocusGetNextItemFromList
- __FEFocusGetSensitivitySetting
- __FEFocusGroupCompare
- __FEFocusGroupIdentifierForInstance
- __FEFocusGroupPriorityForItem
- __FEFocusGroupUnresolvedIdentifierForEnvironment
- __FEFocusItemCanBecomeFocused
- __FEFocusItemCompare
- __FEFocusItemContainerAddChildItemsInContextWithOptions
- __FEFocusItemContainerIsScrollableContainer
- __FEFocusItemContainerIsViewOrRespondsToSelector
- __FEFocusItemContainerSupportsInvalidatingFocusCache
- __FEFocusItemFocusSpeedBumpEdges
- __FEFocusItemFrameInCoordinateSpace
- __FEFocusItemIsFocusableInFocusSystem
- __FEFocusItemIsFocusableInFocusSystemWithSearchInfo
- __FEFocusItemIsFocused
- __FEFocusItemIsFocusedOrFocusable
- __FEFocusItemIsFocusedOrFocusableInFocusSystem
- __FEFocusItemIsLegacyTransparentFocusRegionInSearchContext
- __FEFocusItemIsTransparentFocusItem
- __FEFocusItemIsViewOrRespondsToSelector
- __FEFocusItemSafeCast
- __FEFocusItemScrollableContainerCanScrollX
- __FEFocusItemScrollableContainerCanScrollY
- __FEFocusItemScrollableContainerContentBounds
- __FEFocusItemScrollableContainerIsScrollViewOrRespondsToSelector
- __FEFocusItemScrollableContainerPrimaryAxis
- __FEFocusMapDistanceToRegionBoundary
- __FEFocusMovementDidFailNotification
- __FEFocusNearestAncestorEnvironmentScrollableContainer
- __FEFocusRectCompare
- __FEFocusRectWithMinimumSize
- __FEFocusRegionContainerFromEnvironmentAndContainer
- __FEFocusRegionSearchContextAddChildItemsInEnvironmentContainer
- __FEFocusRegionSearchContextSearchForFocusRegionsInEnvironment
- __FEFocusSensitivityCachedSetting
- __FEFocusSetSensitivitySetting
- __FEFocusShiftAndExpandRectAlongFocusMovement
- __FEFocusSystemEnabledStateDidChangeNotification
- __FEFocusUpdateContextKey
- __FEGetFocusCastingVisualization
- __FEGetFocusTreeLockVerboseLogging
- __FEInternalPreferenceSync
- __FEInternalPreferenceUpdateBool
- __FEInternalPreference_FocusCastingVisualization
- __FEInternalPreference_FocusEnvironmentUseAncestorScrollableSizeForFallbackRotaryAxis
- __FEInternalPreference_FocusGroupSeparateNestedEqualRotaryMovementAxis
- __FEInternalPreference_FocusTreeLockVerboseLogging
- __FEInternalPreferencesRevisionInit_block_invoke
- __FEInternalPreferencesRevisionOnce
- __FEInternalPreferencesRevisionVar
- __FEPerformDelayed
- __FEPreferencesOnce
- __FEProcessIsBeingDebugged
- __FERectSmartIntersectsRect
- __FEStringFromCGRect
- __FEStringFromFocusHeading
- __FEStringFromGroupFilter
- __FEUserDefaults
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$__FEGeometryKeyedCoding
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$__FEFocusRegionContainerProxy
- __OBJC_$_CATEGORY_NSCoder_$__FEGeometryKeyedCoding
- __OBJC_$_CATEGORY_NSObject_$__FEFocusRegionContainerProxy
- __OBJC_$_CLASS_METHODS__FEDebugIssue
- __OBJC_$_CLASS_METHODS__FEDebugLogMessage
- __OBJC_$_CLASS_METHODS__FEDebugLogNode
- __OBJC_$_CLASS_METHODS__FEDebugLogNodeTreeStyle
- __OBJC_$_CLASS_METHODS__FEDebugReportFormatter
- __OBJC_$_CLASS_METHODS__FEFocusDebugger
- __OBJC_$_CLASS_METHODS__FEFocusDebuggerStringOutput
- __OBJC_$_CLASS_METHODS__FEFocusEnvironmentContainerTuple
- __OBJC_$_CLASS_METHODS__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_$_CLASS_METHODS__FEFocusGroup
- __OBJC_$_CLASS_METHODS__FEFocusInputDeviceInfo
- __OBJC_$_CLASS_METHODS__FEFocusItemInfo
- __OBJC_$_CLASS_METHODS__FEFocusLinearMovementSequence
- __OBJC_$_CLASS_METHODS__FEFocusMapSnapshotDebugInfo
- __OBJC_$_CLASS_METHODS__FEFocusMovementInfo
- __OBJC_$_CLASS_METHODS__FEFocusRegionDebugDrawingConfiguration
- __OBJC_$_CLASS_METHODS__FEFocusRegionDebugQuickLook
- __OBJC_$_CLASS_METHODS__FEFocusRegionEvaluator
- __OBJC_$_CLASS_METHODS__FEFocusRegionMovementInfo
- __OBJC_$_CLASS_METHODS__FEFocusRegionSearchContextState
- __OBJC_$_CLASS_METHODS__FEFocusSearchInfo
- __OBJC_$_CLASS_METHODS__FEFocusSystem
- __OBJC_$_CLASS_METHODS__FEFocusUpdateContext
- __OBJC_$_CLASS_METHODS__FEFocusUpdateRequest
- __OBJC_$_CLASS_PROP_LIST__FEFocusSystem
- __OBJC_$_CLASS_PROP_LIST__FEFocusUpdateContext
- __OBJC_$_INSTANCE_METHODS__FEDebugIssue
- __OBJC_$_INSTANCE_METHODS__FEDebugIssueReport
- __OBJC_$_INSTANCE_METHODS__FEDebugIssueReportFormatter
- __OBJC_$_INSTANCE_METHODS__FEDebugLogMessage
- __OBJC_$_INSTANCE_METHODS__FEDebugLogNode
- __OBJC_$_INSTANCE_METHODS__FEDebugLogNodeTreeStyle
- __OBJC_$_INSTANCE_METHODS__FEDebugLogReport
- __OBJC_$_INSTANCE_METHODS__FEDebugLogReportFormatter
- __OBJC_$_INSTANCE_METHODS__FEDebugLogStack
- __OBJC_$_INSTANCE_METHODS__FEDebugLogStatement
- __OBJC_$_INSTANCE_METHODS__FEDebugReportComponents
- __OBJC_$_INSTANCE_METHODS__FEDebugReportFormatter
- __OBJC_$_INSTANCE_METHODS__FEFocusCastingController
- __OBJC_$_INSTANCE_METHODS__FEFocusContainerGuideRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusDebuggerStringOutput
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentContainerTuple
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentPreferenceCache
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentPreferenceCacheNode
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_$_INSTANCE_METHODS__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_$_INSTANCE_METHODS__FEFocusGroup
- __OBJC_$_INSTANCE_METHODS__FEFocusGroupHistory
- __OBJC_$_INSTANCE_METHODS__FEFocusGroupMap
- __OBJC_$_INSTANCE_METHODS__FEFocusGuideRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusInputDeviceInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusItemDummy
- __OBJC_$_INSTANCE_METHODS__FEFocusItemFrameReporter
- __OBJC_$_INSTANCE_METHODS__FEFocusItemInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusItemRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusLinearMovementCache
- __OBJC_$_INSTANCE_METHODS__FEFocusLinearMovementSequence
- __OBJC_$_INSTANCE_METHODS__FEFocusMap
- __OBJC_$_INSTANCE_METHODS__FEFocusMapRect
- __OBJC_$_INSTANCE_METHODS__FEFocusMapSearchInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusMapSnapshot(_FEFocusDebugging)
- __OBJC_$_INSTANCE_METHODS__FEFocusMapSnapshotDebugInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusMapSnapshotter
- __OBJC_$_INSTANCE_METHODS__FEFocusMovementHint
- __OBJC_$_INSTANCE_METHODS__FEFocusMovementInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusMovementPerformer
- __OBJC_$_INSTANCE_METHODS__FEFocusMovementRequest
- __OBJC_$_INSTANCE_METHODS__FEFocusNullGroup
- __OBJC_$_INSTANCE_METHODS__FEFocusPromiseRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusRegionContainerProxy
- __OBJC_$_INSTANCE_METHODS__FEFocusRegionDebugDrawingConfiguration
- __OBJC_$_INSTANCE_METHODS__FEFocusRegionMovementInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusRegionSearchContextState
- __OBJC_$_INSTANCE_METHODS__FEFocusSearchInfo
- __OBJC_$_INSTANCE_METHODS__FEFocusSpeedBumpRegion
- __OBJC_$_INSTANCE_METHODS__FEFocusStateObserver
- __OBJC_$_INSTANCE_METHODS__FEFocusSystem
- __OBJC_$_INSTANCE_METHODS__FEFocusUpdateContext
- __OBJC_$_INSTANCE_METHODS__FEFocusUpdateReport
- __OBJC_$_INSTANCE_METHODS__FEFocusUpdateReportFormatter
- __OBJC_$_INSTANCE_METHODS__FEFocusUpdateRequest
- __OBJC_$_INSTANCE_METHODS__FEFocusUpdateThrottle
- __OBJC_$_INSTANCE_METHODS__FETreeLock
- __OBJC_$_INSTANCE_METHODS__FETreeLockItem
- __OBJC_$_INSTANCE_METHODS__FEWeakHelper
- __OBJC_$_INSTANCE_METHODS___FEDebugLogRootNode
- __OBJC_$_INSTANCE_VARIABLES__FEDebugIssue
- __OBJC_$_INSTANCE_VARIABLES__FEDebugIssueReport
- __OBJC_$_INSTANCE_VARIABLES__FEDebugIssueReportFormatter
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogMessage
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogNode
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogNodeTreeStyle
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogReport
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogStack
- __OBJC_$_INSTANCE_VARIABLES__FEDebugLogStatement
- __OBJC_$_INSTANCE_VARIABLES__FEDebugReportComponents
- __OBJC_$_INSTANCE_VARIABLES__FEDebugReportFormatter
- __OBJC_$_INSTANCE_VARIABLES__FEFocusCastingController
- __OBJC_$_INSTANCE_VARIABLES__FEFocusContainerGuideRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusDebuggerStringOutput
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentContainerTuple
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentPreferenceCache
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentPreferenceCacheNode
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_$_INSTANCE_VARIABLES__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_$_INSTANCE_VARIABLES__FEFocusGroup
- __OBJC_$_INSTANCE_VARIABLES__FEFocusGroupHistory
- __OBJC_$_INSTANCE_VARIABLES__FEFocusGroupMap
- __OBJC_$_INSTANCE_VARIABLES__FEFocusGuideRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusInputDeviceInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusItemDummy
- __OBJC_$_INSTANCE_VARIABLES__FEFocusItemFrameReporter
- __OBJC_$_INSTANCE_VARIABLES__FEFocusItemInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusItemRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusLinearMovementCache
- __OBJC_$_INSTANCE_VARIABLES__FEFocusLinearMovementSequence
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMap
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMapRect
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMapSearchInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMapSnapshot
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMapSnapshotDebugInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMapSnapshotter
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMovementHint
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMovementInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMovementPerformer
- __OBJC_$_INSTANCE_VARIABLES__FEFocusMovementRequest
- __OBJC_$_INSTANCE_VARIABLES__FEFocusPromiseRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusRegionContainerProxy
- __OBJC_$_INSTANCE_VARIABLES__FEFocusRegionDebugDrawingConfiguration
- __OBJC_$_INSTANCE_VARIABLES__FEFocusRegionMovementInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusRegionSearchContextState
- __OBJC_$_INSTANCE_VARIABLES__FEFocusSearchInfo
- __OBJC_$_INSTANCE_VARIABLES__FEFocusSpeedBumpRegion
- __OBJC_$_INSTANCE_VARIABLES__FEFocusStateObserver
- __OBJC_$_INSTANCE_VARIABLES__FEFocusSystem
- __OBJC_$_INSTANCE_VARIABLES__FEFocusUpdateContext
- __OBJC_$_INSTANCE_VARIABLES__FEFocusUpdateReport
- __OBJC_$_INSTANCE_VARIABLES__FEFocusUpdateRequest
- __OBJC_$_INSTANCE_VARIABLES__FEFocusUpdateThrottle
- __OBJC_$_INSTANCE_VARIABLES__FETreeLock
- __OBJC_$_INSTANCE_VARIABLES__FETreeLockItem
- __OBJC_$_INSTANCE_VARIABLES__FEWeakHelper
- __OBJC_$_PROP_LIST__FEDebugIssue
- __OBJC_$_PROP_LIST__FEDebugIssueReport
- __OBJC_$_PROP_LIST__FEDebugIssueReportFormatter
- __OBJC_$_PROP_LIST__FEDebugLogNode
- __OBJC_$_PROP_LIST__FEDebugLogNodeTreeStyle
- __OBJC_$_PROP_LIST__FEDebugLogReport
- __OBJC_$_PROP_LIST__FEDebugLogStack
- __OBJC_$_PROP_LIST__FEDebugLogStatement
- __OBJC_$_PROP_LIST__FEDebugReportComponents
- __OBJC_$_PROP_LIST__FEDebugReportFormatter
- __OBJC_$_PROP_LIST__FEFocusCastingController
- __OBJC_$_PROP_LIST__FEFocusContainerGuideRegion
- __OBJC_$_PROP_LIST__FEFocusDebuggerStringOutput
- __OBJC_$_PROP_LIST__FEFocusEnvironment
- __OBJC_$_PROP_LIST__FEFocusEnvironmentContainerTuple
- __OBJC_$_PROP_LIST__FEFocusEnvironmentInternal
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPreferenceCache
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPreferenceCacheNode
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPreferenceEnumerationContext.154
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_$_PROP_LIST__FEFocusEnvironmentPrivate
- __OBJC_$_PROP_LIST__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_$_PROP_LIST__FEFocusGroup
- __OBJC_$_PROP_LIST__FEFocusGroupMap
- __OBJC_$_PROP_LIST__FEFocusGuideRegion
- __OBJC_$_PROP_LIST__FEFocusInputDeviceInfo
- __OBJC_$_PROP_LIST__FEFocusItem
- __OBJC_$_PROP_LIST__FEFocusItemContainer
- __OBJC_$_PROP_LIST__FEFocusItemDummy
- __OBJC_$_PROP_LIST__FEFocusItemFrameReporter
- __OBJC_$_PROP_LIST__FEFocusItemInfo
- __OBJC_$_PROP_LIST__FEFocusItemRegion
- __OBJC_$_PROP_LIST__FEFocusItemScrollableContainer
- __OBJC_$_PROP_LIST__FEFocusLinearMovementSequence
- __OBJC_$_PROP_LIST__FEFocusMap
- __OBJC_$_PROP_LIST__FEFocusMapArea
- __OBJC_$_PROP_LIST__FEFocusMapRect
- __OBJC_$_PROP_LIST__FEFocusMapSearchInfo
- __OBJC_$_PROP_LIST__FEFocusMapSnapshotDebugInfo
- __OBJC_$_PROP_LIST__FEFocusMapSnapshotter
- __OBJC_$_PROP_LIST__FEFocusMovementHint
- __OBJC_$_PROP_LIST__FEFocusMovementInfo
- __OBJC_$_PROP_LIST__FEFocusMovementPerformer
- __OBJC_$_PROP_LIST__FEFocusMovementRequest
- __OBJC_$_PROP_LIST__FEFocusPromiseRegion
- __OBJC_$_PROP_LIST__FEFocusRegion
- __OBJC_$_PROP_LIST__FEFocusRegionContainerProxy
- __OBJC_$_PROP_LIST__FEFocusRegionDebugDrawingConfiguration
- __OBJC_$_PROP_LIST__FEFocusRegionMovementInfo
- __OBJC_$_PROP_LIST__FEFocusRegionSearchContext
- __OBJC_$_PROP_LIST__FEFocusRegionSearchContextState
- __OBJC_$_PROP_LIST__FEFocusSearchInfo
- __OBJC_$_PROP_LIST__FEFocusSpeedBumpRegion
- __OBJC_$_PROP_LIST__FEFocusStateObserver
- __OBJC_$_PROP_LIST__FEFocusSystem
- __OBJC_$_PROP_LIST__FEFocusUpdateContext
- __OBJC_$_PROP_LIST__FEFocusUpdateReport
- __OBJC_$_PROP_LIST__FEFocusUpdateRequest
- __OBJC_$_PROP_LIST__FEFocusUpdateRequesting
- __OBJC_$_PROP_LIST__FETreeLock
- __OBJC_$_PROP_LIST__FETreeLockItem
- __OBJC_$_PROP_LIST__FEWeakHelper
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__FEFocusEnvironment
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__FEFocusEnvironmentInternal
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__FEFocusEnvironmentPrivate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__FEFocusItem
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEDebugIssueReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusEnvironment
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusEnvironmentPreferenceEnumerationContextDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusItem
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusItemContainer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusItemScrollableContainer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusMapArea
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusMovementPerformerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusRegionContainer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusRegionSearchContext
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__FEFocusUpdateRequesting
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEDebugIssueReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusEnvironment
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusEnvironmentInternal
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusEnvironmentPreferenceEnumerationContextDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusEnvironmentPrivate
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusItem
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusItemContainer
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusItemScrollableContainer
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusMapArea
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusMovementPerformerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusRegionContainer
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusRegionSearchContext
- __OBJC_$_PROTOCOL_METHOD_TYPES__FEFocusUpdateRequesting
- __OBJC_$_PROTOCOL_REFS__FEDebugIssueReporting
- __OBJC_$_PROTOCOL_REFS__FEFocusDebuggerOutput
- __OBJC_$_PROTOCOL_REFS__FEFocusEnvironment
- __OBJC_$_PROTOCOL_REFS__FEFocusEnvironmentInternal
- __OBJC_$_PROTOCOL_REFS__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_$_PROTOCOL_REFS__FEFocusEnvironmentPreferenceEnumerationContextDelegate
- __OBJC_$_PROTOCOL_REFS__FEFocusEnvironmentPrivate
- __OBJC_$_PROTOCOL_REFS__FEFocusItem
- __OBJC_$_PROTOCOL_REFS__FEFocusItemContainer
- __OBJC_$_PROTOCOL_REFS__FEFocusItemScrollableContainer
- __OBJC_$_PROTOCOL_REFS__FEFocusMapArea
- __OBJC_$_PROTOCOL_REFS__FEFocusMovementPerformerDelegate
- __OBJC_$_PROTOCOL_REFS__FEFocusRegionContainer
- __OBJC_$_PROTOCOL_REFS__FEFocusRegionSearchContext
- __OBJC_$_PROTOCOL_REFS__FEFocusUpdateRequesting
- __OBJC_CLASS_PROTOCOLS_$__FEDebugIssue
- __OBJC_CLASS_PROTOCOLS_$__FEDebugIssueReport
- __OBJC_CLASS_PROTOCOLS_$__FEFocusDebuggerStringOutput
- __OBJC_CLASS_PROTOCOLS_$__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_CLASS_PROTOCOLS_$__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_CLASS_PROTOCOLS_$__FEFocusGroupMap
- __OBJC_CLASS_PROTOCOLS_$__FEFocusInputDeviceInfo
- __OBJC_CLASS_PROTOCOLS_$__FEFocusItemDummy
- __OBJC_CLASS_PROTOCOLS_$__FEFocusItemInfo
- __OBJC_CLASS_PROTOCOLS_$__FEFocusMapRect
- __OBJC_CLASS_PROTOCOLS_$__FEFocusMapSnapshot
- __OBJC_CLASS_PROTOCOLS_$__FEFocusMovementHint
- __OBJC_CLASS_PROTOCOLS_$__FEFocusMovementInfo
- __OBJC_CLASS_PROTOCOLS_$__FEFocusMovementRequest
- __OBJC_CLASS_PROTOCOLS_$__FEFocusRegionContainerProxy
- __OBJC_CLASS_PROTOCOLS_$__FEFocusSystem
- __OBJC_CLASS_PROTOCOLS_$__FEFocusUpdateRequest
- __OBJC_CLASS_RO_$_FocusEngineDummy
- __OBJC_CLASS_RO_$__FEDebugIssue
- __OBJC_CLASS_RO_$__FEDebugIssueReport
- __OBJC_CLASS_RO_$__FEDebugIssueReportFormatter
- __OBJC_CLASS_RO_$__FEDebugLogMessage
- __OBJC_CLASS_RO_$__FEDebugLogNode
- __OBJC_CLASS_RO_$__FEDebugLogNodeTreeStyle
- __OBJC_CLASS_RO_$__FEDebugLogReport
- __OBJC_CLASS_RO_$__FEDebugLogReportFormatter
- __OBJC_CLASS_RO_$__FEDebugLogStack
- __OBJC_CLASS_RO_$__FEDebugLogStatement
- __OBJC_CLASS_RO_$__FEDebugReportComponents
- __OBJC_CLASS_RO_$__FEDebugReportFormatter
- __OBJC_CLASS_RO_$__FEFocusCastingController
- __OBJC_CLASS_RO_$__FEFocusContainerGuideRegion
- __OBJC_CLASS_RO_$__FEFocusDebugger
- __OBJC_CLASS_RO_$__FEFocusDebuggerStringOutput
- __OBJC_CLASS_RO_$__FEFocusEnvironmentContainerTuple
- __OBJC_CLASS_RO_$__FEFocusEnvironmentPreferenceCache
- __OBJC_CLASS_RO_$__FEFocusEnvironmentPreferenceCacheNode
- __OBJC_CLASS_RO_$__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_CLASS_RO_$__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_CLASS_RO_$__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_CLASS_RO_$__FEFocusGroup
- __OBJC_CLASS_RO_$__FEFocusGroupHistory
- __OBJC_CLASS_RO_$__FEFocusGroupMap
- __OBJC_CLASS_RO_$__FEFocusGuideRegion
- __OBJC_CLASS_RO_$__FEFocusInputDeviceInfo
- __OBJC_CLASS_RO_$__FEFocusItemDummy
- __OBJC_CLASS_RO_$__FEFocusItemFrameReporter
- __OBJC_CLASS_RO_$__FEFocusItemInfo
- __OBJC_CLASS_RO_$__FEFocusItemRegion
- __OBJC_CLASS_RO_$__FEFocusLinearMovementCache
- __OBJC_CLASS_RO_$__FEFocusLinearMovementSequence
- __OBJC_CLASS_RO_$__FEFocusMap
- __OBJC_CLASS_RO_$__FEFocusMapRect
- __OBJC_CLASS_RO_$__FEFocusMapSearchInfo
- __OBJC_CLASS_RO_$__FEFocusMapSnapshot
- __OBJC_CLASS_RO_$__FEFocusMapSnapshotDebugInfo
- __OBJC_CLASS_RO_$__FEFocusMapSnapshotter
- __OBJC_CLASS_RO_$__FEFocusMovementHint
- __OBJC_CLASS_RO_$__FEFocusMovementInfo
- __OBJC_CLASS_RO_$__FEFocusMovementPerformer
- __OBJC_CLASS_RO_$__FEFocusMovementRequest
- __OBJC_CLASS_RO_$__FEFocusNullGroup
- __OBJC_CLASS_RO_$__FEFocusPromiseRegion
- __OBJC_CLASS_RO_$__FEFocusRegion
- __OBJC_CLASS_RO_$__FEFocusRegionContainerProxy
- __OBJC_CLASS_RO_$__FEFocusRegionDebugDrawingConfiguration
- __OBJC_CLASS_RO_$__FEFocusRegionDebugQuickLook
- __OBJC_CLASS_RO_$__FEFocusRegionEvaluator
- __OBJC_CLASS_RO_$__FEFocusRegionMovementInfo
- __OBJC_CLASS_RO_$__FEFocusRegionSearchContextState
- __OBJC_CLASS_RO_$__FEFocusSearchInfo
- __OBJC_CLASS_RO_$__FEFocusSpeedBumpRegion
- __OBJC_CLASS_RO_$__FEFocusStateObserver
- __OBJC_CLASS_RO_$__FEFocusSystem
- __OBJC_CLASS_RO_$__FEFocusUpdateContext
- __OBJC_CLASS_RO_$__FEFocusUpdateReport
- __OBJC_CLASS_RO_$__FEFocusUpdateReportFormatter
- __OBJC_CLASS_RO_$__FEFocusUpdateRequest
- __OBJC_CLASS_RO_$__FEFocusUpdateThrottle
- __OBJC_CLASS_RO_$__FETreeLock
- __OBJC_CLASS_RO_$__FETreeLockItem
- __OBJC_CLASS_RO_$__FEWeakHelper
- __OBJC_CLASS_RO_$___FEDebugLogRootNode
- __OBJC_LABEL_PROTOCOL_$__FEDebugIssueReporting
- __OBJC_LABEL_PROTOCOL_$__FEFocusDebuggerOutput
- __OBJC_LABEL_PROTOCOL_$__FEFocusEnvironment
- __OBJC_LABEL_PROTOCOL_$__FEFocusEnvironmentInternal
- __OBJC_LABEL_PROTOCOL_$__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_LABEL_PROTOCOL_$__FEFocusEnvironmentPreferenceEnumerationContextDelegate
- __OBJC_LABEL_PROTOCOL_$__FEFocusEnvironmentPrivate
- __OBJC_LABEL_PROTOCOL_$__FEFocusItem
- __OBJC_LABEL_PROTOCOL_$__FEFocusItemContainer
- __OBJC_LABEL_PROTOCOL_$__FEFocusItemScrollableContainer
- __OBJC_LABEL_PROTOCOL_$__FEFocusMapArea
- __OBJC_LABEL_PROTOCOL_$__FEFocusMovementPerformerDelegate
- __OBJC_LABEL_PROTOCOL_$__FEFocusRegionContainer
- __OBJC_LABEL_PROTOCOL_$__FEFocusRegionSearchContext
- __OBJC_LABEL_PROTOCOL_$__FEFocusUpdateRequesting
- __OBJC_METACLASS_RO_$_FocusEngineDummy
- __OBJC_METACLASS_RO_$__FEDebugIssue
- __OBJC_METACLASS_RO_$__FEDebugIssueReport
- __OBJC_METACLASS_RO_$__FEDebugIssueReportFormatter
- __OBJC_METACLASS_RO_$__FEDebugLogMessage
- __OBJC_METACLASS_RO_$__FEDebugLogNode
- __OBJC_METACLASS_RO_$__FEDebugLogNodeTreeStyle
- __OBJC_METACLASS_RO_$__FEDebugLogReport
- __OBJC_METACLASS_RO_$__FEDebugLogReportFormatter
- __OBJC_METACLASS_RO_$__FEDebugLogStack
- __OBJC_METACLASS_RO_$__FEDebugLogStatement
- __OBJC_METACLASS_RO_$__FEDebugReportComponents
- __OBJC_METACLASS_RO_$__FEDebugReportFormatter
- __OBJC_METACLASS_RO_$__FEFocusCastingController
- __OBJC_METACLASS_RO_$__FEFocusContainerGuideRegion
- __OBJC_METACLASS_RO_$__FEFocusDebugger
- __OBJC_METACLASS_RO_$__FEFocusDebuggerStringOutput
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentContainerTuple
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentPreferenceCache
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentPreferenceCacheNode
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentPreferenceEnumerator
- __OBJC_METACLASS_RO_$__FEFocusEnvironmentScrollableContainerTuple
- __OBJC_METACLASS_RO_$__FEFocusGroup
- __OBJC_METACLASS_RO_$__FEFocusGroupHistory
- __OBJC_METACLASS_RO_$__FEFocusGroupMap
- __OBJC_METACLASS_RO_$__FEFocusGuideRegion
- __OBJC_METACLASS_RO_$__FEFocusInputDeviceInfo
- __OBJC_METACLASS_RO_$__FEFocusItemDummy
- __OBJC_METACLASS_RO_$__FEFocusItemFrameReporter
- __OBJC_METACLASS_RO_$__FEFocusItemInfo
- __OBJC_METACLASS_RO_$__FEFocusItemRegion
- __OBJC_METACLASS_RO_$__FEFocusLinearMovementCache
- __OBJC_METACLASS_RO_$__FEFocusLinearMovementSequence
- __OBJC_METACLASS_RO_$__FEFocusMap
- __OBJC_METACLASS_RO_$__FEFocusMapRect
- __OBJC_METACLASS_RO_$__FEFocusMapSearchInfo
- __OBJC_METACLASS_RO_$__FEFocusMapSnapshot
- __OBJC_METACLASS_RO_$__FEFocusMapSnapshotDebugInfo
- __OBJC_METACLASS_RO_$__FEFocusMapSnapshotter
- __OBJC_METACLASS_RO_$__FEFocusMovementHint
- __OBJC_METACLASS_RO_$__FEFocusMovementInfo
- __OBJC_METACLASS_RO_$__FEFocusMovementPerformer
- __OBJC_METACLASS_RO_$__FEFocusMovementRequest
- __OBJC_METACLASS_RO_$__FEFocusNullGroup
- __OBJC_METACLASS_RO_$__FEFocusPromiseRegion
- __OBJC_METACLASS_RO_$__FEFocusRegion
- __OBJC_METACLASS_RO_$__FEFocusRegionContainerProxy
- __OBJC_METACLASS_RO_$__FEFocusRegionDebugDrawingConfiguration
- __OBJC_METACLASS_RO_$__FEFocusRegionDebugQuickLook
- __OBJC_METACLASS_RO_$__FEFocusRegionEvaluator
- __OBJC_METACLASS_RO_$__FEFocusRegionMovementInfo
- __OBJC_METACLASS_RO_$__FEFocusRegionSearchContextState
- __OBJC_METACLASS_RO_$__FEFocusSearchInfo
- __OBJC_METACLASS_RO_$__FEFocusSpeedBumpRegion
- __OBJC_METACLASS_RO_$__FEFocusStateObserver
- __OBJC_METACLASS_RO_$__FEFocusSystem
- __OBJC_METACLASS_RO_$__FEFocusUpdateContext
- __OBJC_METACLASS_RO_$__FEFocusUpdateReport
- __OBJC_METACLASS_RO_$__FEFocusUpdateReportFormatter
- __OBJC_METACLASS_RO_$__FEFocusUpdateRequest
- __OBJC_METACLASS_RO_$__FEFocusUpdateThrottle
- __OBJC_METACLASS_RO_$__FETreeLock
- __OBJC_METACLASS_RO_$__FETreeLockItem
- __OBJC_METACLASS_RO_$__FEWeakHelper
- __OBJC_METACLASS_RO_$___FEDebugLogRootNode
- __OBJC_PROTOCOL_$__FEDebugIssueReporting
- __OBJC_PROTOCOL_$__FEFocusDebuggerOutput
- __OBJC_PROTOCOL_$__FEFocusEnvironment
- __OBJC_PROTOCOL_$__FEFocusEnvironmentInternal
- __OBJC_PROTOCOL_$__FEFocusEnvironmentPreferenceEnumerationContext
- __OBJC_PROTOCOL_$__FEFocusEnvironmentPreferenceEnumerationContextDelegate
- __OBJC_PROTOCOL_$__FEFocusEnvironmentPrivate
- __OBJC_PROTOCOL_$__FEFocusItem
- __OBJC_PROTOCOL_$__FEFocusItemContainer
- __OBJC_PROTOCOL_$__FEFocusItemScrollableContainer
- __OBJC_PROTOCOL_$__FEFocusMapArea
- __OBJC_PROTOCOL_$__FEFocusMovementPerformerDelegate
- __OBJC_PROTOCOL_$__FEFocusRegionContainer
- __OBJC_PROTOCOL_$__FEFocusRegionSearchContext
- __OBJC_PROTOCOL_$__FEFocusUpdateRequesting
- __OBJC_PROTOCOL_REFERENCE_$__FEFocusEnvironment
- __OBJC_PROTOCOL_REFERENCE_$__FEFocusItem
- __OBJC_PROTOCOL_REFERENCE_$__FEFocusItemScrollableContainer
- __OBJC_PROTOCOL_REFERENCE_$__FEFocusRegionContainer
- ___103-[_FEFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:]_block_invoke
- ___105-[_FEFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]_block_invoke
- ___113-[_FEDebugLogNode __genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:]_block_invoke
- ___19-[_FETreeLock init]_block_invoke
- ___24+[_FEFocusDebugger help]_block_invoke
- ___31-[_FEFocusUpdateThrottle reset]_block_invoke
- ___34-[_FEFocusUpdateContext _validate]_block_invoke
- ___34-[_FEFocusUpdateContext _validate]_block_invoke_2
- ___34-[_FEFocusUpdateThrottle teardown]_block_invoke
- ___35-[_FETreeLock lockEnvironmentTree:]_block_invoke
- ___38-[_FEFocusSystem _requestFocusUpdate:]_block_invoke
- ___40+[_FEDebugLogNodeTreeStyle defaultStyle]_block_invoke
- ___44+[_FEFocusDebugger _ancestryForEnvironment:]_block_invoke
- ___44-[_FEFocusSystem _updateFocusUpdateThrottle]_block_invoke
- ___45-[_FEFocusSystem _focusEnvironmentDidAppear:]_block_invoke
- ___46+[_FEFocusDebugger focusGroupsForEnvironment:]_block_invoke
- ___46+[_FEFocusDebugger focusGroupsForEnvironment:]_block_invoke_2
- ___46-[_FEFocusGroup _validateItemOrderIfNecessary]_block_invoke
- ___47-[_FEFocusSystem _reevaluateLockedEnvironments]_block_invoke
- ___47-[_FEFocusSystem _tickHasSeenFocusedItemTimer:]_block_invoke
- ___48-[_FEFocusUpdateReportFormatter _bodyForReport:]_block_invoke
- ___49-[_FEDebugLogReport fallbackMessagePrefixHandler]_block_invoke
- ___49-[_FEFocusSystem _focusEnvironmentWillDisappear:]_block_invoke
- ___52-[_FEDebugLogReportFormatter _componentsFromReport:]_block_invoke
- ___52-[_FEDebugLogReportFormatter _componentsFromReport:]_block_invoke_2
- ___52-[_FEFocusGroup _validateChildGroupOrderIfNecessary]_block_invoke
- ___54-[_FEDebugIssueReportFormatter _componentsFromReport:]_block_invoke
- ___54-[_FEFocusItemInfo isFocusMovementFlippedHorizontally]_block_invoke
- ___54-[_FEFocusMap _inferredDefaultFocusItemInEnvironment:]_block_invoke
- ___55-[_FEFocusSystem _focusEnvironmentWillBecomeInvisible:]_block_invoke
- ___57-[_FEFocusSystem _buildFocusItemAncestorCacheIfNecessary]_block_invoke
- ___57-[_FEFocusUpdateThrottle scheduleProgrammaticFocusUpdate]_block_invoke
- ___58-[_FEFocusItemFrameReporter _scheduleRepeatingFrameUpdate]_block_invoke
- ___58-[_FETreeLockItem initWithEnvironment:finalUnlockHandler:]_block_invoke
- ___60-[_FEFocusSystem _sendDidUpdateFocusNotificationsInContext:]_block_invoke
- ___61+[_FEFocusDebugger preferredFocusEnvironmentsForEnvironment:]_block_invoke
- ___61-[_FEFocusSystem _sendWillUpdateFocusNotificationsInContext:]_block_invoke
- ___63-[_FEFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke
- ___63-[_FEFocusMovementPerformer _isMovementValidForFocusSequences:]_block_invoke_2
- ___71-[_FEFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]_block_invoke
- ___71-[_FEFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:]_block_invoke_2
- ___73-[_FEDebugLogNode _appendChildDescription:withPrefix:inheritedTreeStyle:]_block_invoke
- ___76-[_FEFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]_block_invoke
- ___76-[_FEFocusMap _linearlySortedFocusItemsForItems:groupFilter:itemStandInMap:]_block_invoke_2
- ___78-[_FEFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]_block_invoke
- ___78-[_FEFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment]_block_invoke
- ___82-[_FEFocusEnvironmentPreferenceCache preferredEnvironmentsForEnvironment:isFinal:]_block_invoke
- ___92-[_FEFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]_block_invoke
- ___98-[_FEFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke
- ___98-[_FEFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:]_block_invoke_2
- ___UIKitCoreLibraryCore_block_invoke
- ____FEFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke
- ____FEFocusEngineCommonEnvironmentScrollableContainerForItems_block_invoke_2
- ____FEFocusEnvironmentInheritedFocusMovementStyle_block_invoke
- ____FEFocusEnvironmentIsAncestorOfEnvironment_block_invoke
- ____FEFocusEnvironmentPreferredFocusMapContainer_block_invoke
- ____FEFocusEnvironmentResolvedRotaryFocusMovementAxis_block_invoke
- ____FEFocusGetSensitivitySetting_block_invoke
- ____FEFocusItemContainerAddChildItemsInContextWithOptions_block_invoke
- ____FEFocusItemIsLegacyTransparentFocusRegionInSearchContext_block_invoke
- ____FEFocusSystemRegister_block_invoke
- ____FEPerformDelayed_block_invoke
- ____FEPreferencesOnce_block_invoke
- ____FEStringFromFocusHeading_block_invoke
- ____FEUserDefaults_block_invoke
- ____UIKitUserDefaults_block_invoke
- ___block_descriptor_32_e35_B32?0"_FEDebugLogMessage"8Q16^B24l
- ___block_descriptor_32_e41_q24?0"_FEFocusGroup"8"_FEFocusGroup"16l
- ___block_descriptor_32_e43_q24?0"<_FEFocusItem>"8"<_FEFocusItem>"16l
- ___block_descriptor_32_e48_16?0"_FEFocusEnvironmentPreferenceCacheNode"8l
- ___block_descriptor_32_e61_v32?0"_FEDebugLogMessage"8"NSString"16"NSMutableString"24l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8
- ___block_descriptor_40_e8_32r_e35_v24?0"<_FEFocusEnvironment>"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e59_B16?0"<_FEFocusEnvironmentPreferenceEnumerationContext>"8lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e30_B32?0"_FEFocusGroup"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e31_v16?0"<_FEFocusEnvironment>"8ls32l8
- ___block_descriptor_40_e8_32s_e33_v36?0"_FEFocusGroup"8Q16B24^B28ls32l8
- ___block_descriptor_40_e8_32s_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e58_"<_FEFocusRegionContainer>"16?0"_FEFocusPromiseRegion"8ls32l8
- ___block_descriptor_40_e8_32s_e60_B32?0"_FEFocusEnvironmentScrollableContainerTuple"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32w_e31_v16?0"<_FEFocusEnvironment>"8lw32l8
- ___block_descriptor_48_e8_32r40r_e35_v24?0"<_FEFocusEnvironment>"8^B16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e37_v32?0"_FEDebugLogStatement"8Q16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e38_v32?0"<_FEFocusEnvironment>"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e24_B16?0"<_FEFocusItem>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e31_16?0"<_FEFocusEnvironment>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e31_v16?0"<_FEFocusEnvironment>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e41_B24?0"<_FEFocusItem>"8"NSDictionary"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e63_v24?0"<_FEFocusEnvironmentPreferenceEnumerationContext>"8^q16ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e63_v24?0"<_FEFocusEnvironmentPreferenceEnumerationContext>"8^q16lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40r_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s_e37_v32?0"_FEDebugLogStatement"8Q16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32s40r_e47_v32?0"_FEFocusLinearMovementSequence"8Q16^B24ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48r56r_e63_v24?0"<_FEFocusEnvironmentPreferenceEnumerationContext>"8^q16lr48l8r56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r_e30_v32?0"_FEDebugIssue"8Q16^B24ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48s56r_e35_v24?0"<_FEFocusEnvironment>"8^B16ls32l8s40l8s48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56r_e47_v32?0"_FEFocusLinearMovementSequence"8Q16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e63_v24?0"<_FEFocusEnvironmentPreferenceEnumerationContext>"8^q16ls32l8r64l8s40l8r72l8s48l8r80l8s56l8
- ___block_descriptor_96_e8_32s40s48s56s64r72r80r88r_e35_v24?0"<_FEFocusEnvironment>"8^B16lr64l8s32l8s40l8r72l8r80l8s48l8s56l8r88l8
- ___block_literal_global.100
- ___block_literal_global.106
- ___block_literal_global.18
- ___block_literal_global.470
- ___const.<block>.paths
- ___getUIApplicationClass_block_invoke
- __dispatch_source_type_timer
- __prefixForItem
- __sl_dlopen
- _audit_stringUIKitCore
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _dispatch_time
- _objc_getClass
- _objc_msgSend$UUID
- _objc_msgSend$__genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:
- _objc_msgSend$__isKindOfUIScrollView
- _objc_msgSend$__isKindOfUIView
- _objc_msgSend$__isKindOfUIViewController
- _objc_msgSend$_allDefaultFocusableRegionsInContainer:intersectingRegion:
- _objc_msgSend$_appendChildDescription:withPrefix:inheritedTreeStyle:
- _objc_msgSend$_axisForHeading:
- _objc_msgSend$_canBecomeFocused
- _objc_msgSend$_cancelRepeatingFrameUpdate
- _objc_msgSend$_castingFrameForFocusedNormalizedFrame:heading:
- _objc_msgSend$_castingPointInNormalizedFrame:forHeading:
- _objc_msgSend$_createFocusMovementIndicator
- _objc_msgSend$_debugDrawingConfigurationWithDebugInfo:
- _objc_msgSend$_debugInfo
- _objc_msgSend$_debugInfoWithFocusMapSearchInfo:
- _objc_msgSend$_drawImage
- _objc_msgSend$_entryPointInNormalizedFrame:forHeading:
- _objc_msgSend$_findAllDefaultFocusableRegionsWithSnapshotter:
- _objc_msgSend$_focusAllowsLeavingWithHeading:
- _objc_msgSend$_focusCastingController
- _objc_msgSend$_focusContentOffset
- _objc_msgSend$_focusContentSize
- _objc_msgSend$_focusCoordinateSpace
- _objc_msgSend$_focusDeferralMode
- _objc_msgSend$_focusEffectsControllerForFocusedItem
- _objc_msgSend$_focusEnvironmentWillDisappear:
- _objc_msgSend$_focusFrame
- _objc_msgSend$_focusGroupIdentifier
- _objc_msgSend$_focusGroupPriority
- _objc_msgSend$_focusGuideBehaviorForMovement:
- _objc_msgSend$_focusItemContainer
- _objc_msgSend$_focusItemsInRect:
- _objc_msgSend$_focusLinearMovementSequence
- _objc_msgSend$_focusMapSnapshotDebugInfoArray
- _objc_msgSend$_focusPreferredMovementStyle
- _objc_msgSend$_focusRotaryMovementAxis
- _objc_msgSend$_focusVisibleSize
- _objc_msgSend$_globalFrameForFocusedItemInSystem:
- _objc_msgSend$_initWithItem:containingView:useFallbackAncestorScroller:
- _objc_msgSend$_isNode
- _objc_msgSend$_isTransparent
- _objc_msgSend$_isTransparentFocusItem
- _objc_msgSend$_isTransparentFocusRegion
- _objc_msgSend$_movementPointInNormalizedFrame:
- _objc_msgSend$_movementWithHeading:isInitial:
- _objc_msgSend$_normalizedCoordinateSpace
- _objc_msgSend$_parentFocusEnvironment
- _objc_msgSend$_performBlockAfterCATransactionCommits:
- _objc_msgSend$_positionFocusMovementIndicators
- _objc_msgSend$_preferredFocusEnvironments
- _objc_msgSend$_regionMapSnapshots
- _objc_msgSend$_regionMapSnapshotsVisualRepresentation
- _objc_msgSend$_reportFocusFrameForCurrentlyFocusedItem
- _objc_msgSend$_reportFocusFrameUpdateForGlobalFrame:
- _objc_msgSend$_requiresFocusedItemToBeInHierarchy
- _objc_msgSend$_scheduleRepeatingFrameUpdate
- _objc_msgSend$_startRememberingEntryPoint
- _objc_msgSend$_stopRememberingEntryPoint
- _objc_msgSend$_stringRepresentation
- _objc_msgSend$_summaryImageForDebugInfoArray:forFocusMovementWithInfo:scaleFactor:
- _objc_msgSend$_topNode
- _objc_msgSend$_updateFocusItemFromNormalizedFrame:toNormalizedFrame:withHeading:
- _objc_msgSend$_updateFocusMovementIndicatorDisplay
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$appendArraySection:withName:skipIfEmpty:
- _objc_msgSend$appendInteger:withName:
- _objc_msgSend$appendString:withName:
- _objc_msgSend$arrayWithObject:
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$checkFocusabilityForItem:
- _objc_msgSend$containerGuideConfigurationForRegion:
- _objc_msgSend$defaultStyle
- _objc_msgSend$descriptionBuilder
- _objc_msgSend$entryPointAxis
- _objc_msgSend$entryPointMemorizationTimeout
- _objc_msgSend$focusCastingIndicator
- _objc_msgSend$focusEntryIndicator
- _objc_msgSend$focusMovementIndicator
- _objc_msgSend$guideConfigurationForRegion:
- _objc_msgSend$image
- _objc_msgSend$indexOfObjectWithOptions:passingTest:
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithFocusBehavior:
- _objc_msgSend$initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:inputType:
- _objc_msgSend$initWithNode:lastNode:intermediate:trailing:
- _objc_msgSend$initWithRegion:baseHue:patternAlpha:dashedStroke:
- _objc_msgSend$initWithSnapshot:focusMapSearchInfo:
- _objc_msgSend$intermediate
- _objc_msgSend$isActive
- _objc_msgSend$isRememberingEntryPoint
- _objc_msgSend$itemConfigurationForRegion:
- _objc_msgSend$lastNode
- _objc_msgSend$legacyIsTransparentFocusRegionSupported
- _objc_msgSend$mainBundle
- _objc_msgSend$modernFocusedItemGetterBehavior
- _objc_msgSend$node
- _objc_msgSend$notifyObserversIfNecessary
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$object
- _objc_msgSend$performSelector:withObject:afterDelay:
- _objc_msgSend$promiseConfigurationForRegion:
- _objc_msgSend$removeFromSuperview
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$screenEntryPoint
- _objc_msgSend$set
- _objc_msgSend$setBounds:
- _objc_msgSend$setCenter:
- _objc_msgSend$setEnabled:
- _objc_msgSend$setEntryPointAxis:
- _objc_msgSend$setFocusCastingIndicator:
- _objc_msgSend$setFocusEntryIndicator:
- _objc_msgSend$setFocusMovementIndicator:
- _objc_msgSend$setHidden:
- _objc_msgSend$setIsRememberingEntryPoint:
- _objc_msgSend$setScreenEntryPoint:
- _objc_msgSend$set_focusFrame:
- _objc_msgSend$set_parentFocusEnvironment:
- _objc_msgSend$sharedApplication
- _objc_msgSend$snapshot
- _objc_msgSend$snapshots
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$styleWithNode:lastNode:intermediate:trailing:
- _objc_msgSend$synchronize
- _objc_msgSend$trailing
- _objc_msgSend$treeStyle
- _objc_msgSend$uppercaseString
- _objc_msgSend$valueWithCGRect:
- _objc_release_x2
CStrings:
+ "!CGRectIsNull(frame)"
+ "%@"
+ "%@, isEnabled: %@"
+ "%@.\nSuppressing subsequent logging of this error."
+ "-[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:]"
+ "-[UIFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:]"
+ "-[UIFocusSystem _validatedAppearingFocusEnvironmentRequest]"
+ "-[UIFocusSystem updateFocusIfNeeded]"
+ "-[_UIFocusEnvironmentPreferenceCache setPreferredEnvironments:forEnvironment:]"
+ "-[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:]_block_invoke"
+ "-[_UIFocusGroupMap _indexItems:]"
+ "-[_UIFocusItemInfo _createFocusedRegion]"
+ "-[_UIFocusMapSnapshot addRegionsInContainer:]"
+ "-[_UIFocusMovementPerformer _bestCandidateForNonLinearFocusMovement:]"
+ "-[_UIFocusMovementPerformer _environmentContainersToCheckForRequest:]"
+ "-[_UIFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:]"
+ "-[_UIFocusUpdateRequest requestByMergingWithRequest:]"
+ "@\"<UICoordinateSpace>\""
+ "@\"<UICoordinateSpace>\"16@0:8"
+ "@\"<UIFocusEnvironment>\""
+ "@\"<UIFocusEnvironment>\"16@0:8"
+ "@\"<UIFocusEnvironment>\"24@0:8@\"UIFocusSystem\"16"
+ "@\"<UIFocusItem>\""
+ "@\"<UIFocusItem>\"16@0:8"
+ "@\"<UIFocusItemContainer>\""
+ "@\"<UIFocusItemContainer>\"16@0:8"
+ "@\"<UIFocusItemContainer>\"24@0:8@\"UIFocusSystem\"16"
+ "@\"<UIFocusItemScrollableContainer>\""
+ "@\"<_UIFocusBehavior>\""
+ "@\"<_UIFocusCasting>\""
+ "@\"<_UIFocusEnvironmentPreferenceEnumerationContextDelegate>\""
+ "@\"<_UIFocusGuideImplDelegate>\""
+ "@\"<_UIFocusGuideRegionDelegate>\""
+ "@\"<_UIFocusMapArea>\"16@0:8"
+ "@\"<_UIFocusMovementPerformerDelegate>\""
+ "@\"<_UIFocusRegionContainer>\""
+ "@\"<_UIFocusRegionContainer>\"16@0:8"
+ "@\"<_UIFocusRegionContainer>\"16@?0@\"_UIFocusPromiseRegion\"8"
+ "@\"<_UIFocusSystemDelegate>\""
+ "@\"<_UIFocusUpdateRequesting>\""
+ "@\"<_UIHostedFocusSystemDelegate>\""
+ "@\"NSArray\"24@0:8@\"UIFocusSystem\"16"
+ "@\"NSArray\"32@0:8@\"_UIFocusGuideRegion\"16@\"_UIFocusMovementRequest\"24"
+ "@\"NSArray\"56@0:8@\"_UIHostedFocusSystem\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "@\"NSString\"24@0:8@\"UIFocusUpdateContext\"16"
+ "@\"UIFocusMovementAction\""
+ "@\"UIFocusSystem\""
+ "@\"UIFocusSystem\"16@0:8"
+ "@\"UIFocusUpdateContext\""
+ "@\"_UIDebugIssueReport\""
+ "@\"_UIDebugLogNode\""
+ "@\"_UIDebugLogReport\""
+ "@\"_UIDebugLogStack\""
+ "@\"_UIDebugLogStack\"16@0:8"
+ "@\"_UIFocusEnvironmentContainerTuple\""
+ "@\"_UIFocusEnvironmentPreferenceCache\""
+ "@\"_UIFocusEnvironmentScrollableContainerTuple\""
+ "@\"_UIFocusGroup\""
+ "@\"_UIFocusGroupHistory\""
+ "@\"_UIFocusGroupMap\""
+ "@\"_UIFocusGuideImpl\""
+ "@\"_UIFocusInputDeviceInfo\""
+ "@\"_UIFocusInputDeviceInfo\"16@0:8"
+ "@\"_UIFocusItemInfo\""
+ "@\"_UIFocusLinearMovementCache\""
+ "@\"_UIFocusMapRect\""
+ "@\"_UIFocusMapSearchInfo\""
+ "@\"_UIFocusMovementInfo\""
+ "@\"_UIFocusMovementInfo\"16@0:8"
+ "@\"_UIFocusMovementPerformer\""
+ "@\"_UIFocusRegion\""
+ "@\"_UIFocusSearchInfo\""
+ "@\"_UIFocusSearchInfo\"16@0:8"
+ "@\"_UIFocusTreeLock\""
+ "@\"_UIFocusUpdateRequest\""
+ "@\"_UIFocusUpdateThrottle\""
+ "@\"_UIHostedFocusSystem\""
+ "@\"_UIHostedFocusSystemDelegateProxy\""
+ "@\"_UIHostedFocusSystemItemContainer\""
+ "@16@?0@\"<UIFocusEnvironment>\"8"
+ "@16@?0@\"_UIFocusEnvironmentPreferenceCacheNode\"8"
+ "@56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "@64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@?56"
+ "@68@0:8@16@24B32{CGRect={CGPoint=dd}{CGSize=dd}}36"
+ "@88@0:8{CGPoint=dd}16{CGRect={CGPoint=dd}{CGSize=dd}}32@?64{CGPoint=dd}72"
+ "@96@0:8{CGPoint=dd}16@32{CGRect={CGPoint=dd}{CGSize=dd}}40{CGPoint=dd}72@?88"
+ "B16@?0@\"<UIFocusItem>\"8"
+ "B16@?0@\"<_UIFocusEnvironmentPreferenceEnumerationContext>\"8"
+ "B16@?0@\"_UIFocusRegion\"8"
+ "B24@0:8@\"UIFocusSystem\"16"
+ "B24@0:8@\"UIFocusUpdateContext\"16"
+ "B24@0:8@\"_UIFocusEnvironmentPreferenceEnumerationContext\"16"
+ "B24@?0@\"<UIFocusItem>\"8@\"NSDictionary\"16"
+ "B32@0:8@\"UIFocusSystem\"16@\"<UIFocusEnvironment>\"24"
+ "B32@0:8@\"UIFocusSystem\"16@\"UIFocusUpdateContext\"24"
+ "B32@0:8@\"UIFocusSystem\"16@\"_UIFocusMovementRequest\"24"
+ "B32@0:8@\"_UIFocusMovementRequest\"16@\"_UIFocusMovementPerformer\"24"
+ "B32@0:8@\"_UIHostedFocusSystem\"16@\"<UIFocusEnvironment>\"24"
+ "B32@?0@\"_UIFocusEnvironmentScrollableContainerTuple\"8Q16^B24"
+ "B32@?0@\"_UIFocusGroup\"8Q16^B24"
+ "B40@0:8@\"UIFocusSystem\"16@\"<UIFocusItemScrollableContainer>\"24^{CGPoint=dd}32"
+ "B40@0:8@16@24^{CGPoint=dd}32"
+ "BOOL _UIFocusEnvironmentIsEligibleForFocusInteraction(__strong id<UIFocusEnvironment> _Nonnull)"
+ "BOOL _UIFocusEnvironmentIsEligibleForFocusOcclusion(__strong id<UIFocusEnvironment> _Nonnull, BOOL * _Nullable)"
+ "BOOL _UIFocusEnvironmentShouldUpdateFocus(__strong id<UIFocusEnvironment> _Nonnull, UIFocusUpdateContext *__strong _Nonnull)"
+ "BOOL _UIFocusItemCanBecomeFocused(__strong id<UIFocusItem> _Nonnull, UIFocusSystem *__strong _Nonnull)"
+ "BOOL _UIFocusItemIsFocusableInFocusSystem(__strong id<UIFocusItem> _Nonnull, UIFocusSystem *__strong _Nonnull)"
+ "BOOL _UIFocusItemIsFocusableInFocusSystemWithSearchInfo(__strong id<UIFocusItem> _Nonnull, UIFocusSystem *__strong _Nonnull, _UIFocusSearchInfo *__strong _Nonnull)"
+ "BOOL _UIFocusItemIsFocused(__strong id<UIFocusItem> _Nonnull)"
+ "BOOL _UIFocusItemIsFocusedOrFocusable(__strong id<UIFocusItem> _Nonnull)"
+ "BOOL _UIFocusItemIsFocusedOrFocusableInFocusSystem(__strong id<UIFocusItem> _Nonnull, UIFocusSystem *__strong _Nonnull)"
+ "BOOL __UIFocusItemIsFocusedOrFocusableInFocusSystem(__strong id<UIFocusItem>, UIFocusSystem *__strong, BOOL, BOOL)"
+ "CGRect _UIFocusShiftAndExpandRectAlongHeadingForNonLinearMovement(CGRect, UIFocusHeading)"
+ "Focus item %@ does not provide a parentFocusEnvironment."
+ "Focus item %@ has a parent focus environment of %@ but this environment does not provide a container for focus items."
+ "FocusEnvironmentUseLegacyIsFocusedOrContainsFocusLogic"
+ "It looks like you are calling a UIFocusDebugger method outside of lldb. That is not allowed."
+ "Method not implemented."
+ "NSArray<id<UIFocusEnvironment>> * _Nonnull _UIFocusEnvironmentEffectivePreferredFocusEnvironments(__strong id<UIFocusEnvironment> _Nonnull, BOOL * _Nullable)"
+ "NSComparisonResult _UIFocusGroupCompare(_UIFocusGroup * _Nonnull __strong, _UIFocusGroup * _Nonnull __strong)"
+ "NSHashTable<_UIHostedFocusSystem *> * _Nullable _UIHostedFocusSystemsForHostEnvironment(__strong id<UIFocusEnvironment> _Nonnull)"
+ "NSString * _Nonnull _UIFocusGroupIdentifierForInstance(id  _Nonnull __strong)"
+ "T@\"<UICoordinateSpace>\",R,N"
+ "T@\"<UICoordinateSpace>\",R,N,V_coordinateSpace"
+ "T@\"<UICoordinateSpace>\",R,N,V_regionCoordinateSpace"
+ "T@\"<UICoordinateSpace>\",R,W,N"
+ "T@\"<UICoordinateSpace>\",R,W,N,V_coordinateSpace"
+ "T@\"<UIFocusEnvironment>\",R,N"
+ "T@\"<UIFocusEnvironment>\",R,N,G_disappearingFocusEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,N,V_environment"
+ "T@\"<UIFocusEnvironment>\",R,N,V_owningEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,N,V_resolvedEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N"
+ "T@\"<UIFocusEnvironment>\",R,W,N,G_commonAncestorEnvironment,V_commonAncestorEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,G_initialDestinationEnvironment,V_initialDestinationEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_deepestPreferredFocusEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_destinationEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_environment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_hostEnvironment"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_parentFocusEnvironment"
+ "T@\"<UIFocusEnvironment>\",W,N,V_owningEnvironment"
+ "T@\"<UIFocusEnvironment>\",W,N,V_parentFocusEnvironment"
+ "T@\"<UIFocusItem>\",?,R,N"
+ "T@\"<UIFocusItem>\",N,V_owningItem"
+ "T@\"<UIFocusItem>\",R,N,V_fulfilledItem"
+ "T@\"<UIFocusItem>\",R,N,V_primaryItem"
+ "T@\"<UIFocusItem>\",R,W,N"
+ "T@\"<UIFocusItem>\",R,W,N,G_previousFocusedItem,V_previousFocusedItem"
+ "T@\"<UIFocusItem>\",R,W,N,V_focusedItem"
+ "T@\"<UIFocusItem>\",R,W,N,V_item"
+ "T@\"<UIFocusItemContainer>\",R,N"
+ "T@\"<UIFocusItemContainer>\",R,N,V_itemContainer"
+ "T@\"<UIFocusItemScrollableContainer>\",R,N,V_scrollableContainer"
+ "T@\"<_UIFocusBehavior>\",&,N,V_behavior"
+ "T@\"<_UIFocusBehavior>\",R,N,V_focusBehavior"
+ "T@\"<_UIFocusCasting>\",&,N,G_focusCasting,S_setFocusCasting:,V_focusCasting"
+ "T@\"<_UIFocusEnvironmentPreferenceEnumerationContextDelegate>\",W,N,V_delegate"
+ "T@\"<_UIFocusGuideImplDelegate>\",R,N,V_delegate"
+ "T@\"<_UIFocusGuideRegionDelegate>\",W,N,V_delegate"
+ "T@\"<_UIFocusMapArea>\",R,N"
+ "T@\"<_UIFocusMovementPerformerDelegate>\",W,N,V_delegate"
+ "T@\"<_UIFocusRegionContainer>\",&,N,V_contentFocusRegionContainer"
+ "T@\"<_UIFocusRegionContainer>\",&,N,V_fallbackRootRegionContainer"
+ "T@\"<_UIFocusRegionContainer>\",?,R,W,N,G_focusMapContainer"
+ "T@\"<_UIFocusRegionContainer>\",R,N,V_regionContainer"
+ "T@\"<_UIFocusRegionContainer>\",R,W,N,V_regionsContainer"
+ "T@\"<_UIFocusRegionContainer>\",R,W,N,V_rootContainer"
+ "T@\"<_UIFocusRegionContainer>\",W,N,V_regionsContainer"
+ "T@\"<_UIFocusSystemDelegate>\",W,N,V_delegate"
+ "T@\"<_UIFocusUpdateRequesting>\",R,N,G_request,V_request"
+ "T@\"<_UIHostedFocusSystemDelegate>\",R,W,N,V_delegate"
+ "T@\"<_UIHostedFocusSystemDelegate>\",W,N"
+ "T@\"NSArray\",?,R,C,N,G_linearFocusMovementSequences"
+ "T@\"NSArray\",C,N,V_preferredFocusEnvironments"
+ "T@\"NSArray\",R,N,V_childItems"
+ "T@\"NSString\",C,N,V_debugIdentifier"
+ "T@\"UIFocusGuide\",R,W,N,G_focusedGuide"
+ "T@\"UIFocusMovementAction\",&,N,V_pendingFocusMovementAction"
+ "T@\"UIFocusSystem\",R,N,V_regionContainerFocusSystem"
+ "T@\"UIFocusSystem\",R,W,N"
+ "T@\"UIFocusSystem\",R,W,N,G_hostFocusSystem"
+ "T@\"UIFocusSystem\",R,W,N,V_focusSystem"
+ "T@\"UIFocusUpdateContext\",&,N,V_context"
+ "T@\"_UIDebugIssueReport\",&,N,G_validationReport,S_setValidationReport:,V_validationReport"
+ "T@\"_UIDebugIssueReport\",R,N,G_subissueReport,V_subissueReport"
+ "T@\"_UIDebugIssueReportFormatter\",R,C,N,G_defaultValidationReportFormatter"
+ "T@\"_UIDebugLogNode\",&,N,V_debugLog"
+ "T@\"_UIDebugLogReport\",&,N,G_preferredFocusReport,S_setPreferredFocusReport:,V_preferredFocusReport"
+ "T@\"_UIDebugLogStack\",&,N,V_debugStack"
+ "T@\"_UIDebugLogStack\",R,N"
+ "T@\"_UIFocusEnvironmentContainerTuple\",&,N,V_environmentContainer"
+ "T@\"_UIFocusEnvironmentPreferenceCache\",R,N,V_deepestPreferredFocusableItemCacheForCurrentUpdate"
+ "T@\"_UIFocusEnvironmentScrollableContainerTuple\",&,N,G_commonEnvironmentScrollableContainer,S_setCommonEnvironmentScrollableContainer:,V_commonEnvironmentScrollableContainer"
+ "T@\"_UIFocusGroup\",R,W,N,V_parentGroup"
+ "T@\"_UIFocusGroupHistory\",R,N,G_focusGroupHistory,V_focusGroupHistory"
+ "T@\"_UIFocusGroupMap\",&,N,V_focusGroupMap"
+ "T@\"_UIFocusGroupMap\",R,N,V_focusGroupMap"
+ "T@\"_UIFocusGuideImpl\",W,N,S_setFocusedGuideImpl:,V_focusedGuideImpl"
+ "T@\"_UIFocusInputDeviceInfo\",&,N,V_inputDeviceInfo"
+ "T@\"_UIFocusInputDeviceInfo\",R,N"
+ "T@\"_UIFocusItemInfo\",&,N,V_focusedItemInfo"
+ "T@\"_UIFocusItemInfo\",R,C,N,G_destinationItemInfo,V_destinationItemInfo"
+ "T@\"_UIFocusItemInfo\",R,C,N,G_sourceItemInfo,V_sourceItemInfo"
+ "T@\"_UIFocusLinearMovementCache\",&,N,G_focusMovementCache,S_setFocusMovementCache:,V_focusMovementCache"
+ "T@\"_UIFocusMapRect\",R,N,G_searchArea,V_searchArea"
+ "T@\"_UIFocusMapRect\",R,N,V_mapArea"
+ "T@\"_UIFocusMapSearchInfo\",&,N,G_focusMapSearchInfo,S_setFocusMapSearchInfo:,V_focusMapSearchInfo"
+ "T@\"_UIFocusMapSearchInfo\",R,N,G_defaultItemSearchContext,V_defaultItemSearchInfo"
+ "T@\"_UIFocusMapSearchInfo\",R,N,G_focusMovementSearchContext,V_focusMovementSearchInfo"
+ "T@\"_UIFocusMovementInfo\",&,N,V_movementInfo"
+ "T@\"_UIFocusMovementInfo\",R,N"
+ "T@\"_UIFocusMovementInfo\",R,N,G_focusMovement,V_focusMovement"
+ "T@\"_UIFocusMovementPerformer\",R,N,V_movementPerformer"
+ "T@\"_UIFocusMovementRequest\",R,N"
+ "T@\"_UIFocusRegion\",&,N,V_focusedRegion"
+ "T@\"_UIFocusRegion\",R,C,N,V_focusedRegion"
+ "T@\"_UIFocusRegion\",R,N,V_focusedRegion"
+ "T@\"_UIFocusSearchInfo\",&,N,V_searchInfo"
+ "T@\"_UIFocusSearchInfo\",R,N"
+ "T@\"_UIFocusSearchInfo\",R,N,V_searchInfo"
+ "T@\"_UIFocusTreeLock\",R,N,V_treeLock"
+ "T@\"_UIFocusUpdateThrottle\",R,N,V_updateThrottle"
+ "T@\"_UIHostedFocusSystem\",W,N,V_focusSystem"
+ "T@\"_UIHostedFocusSystemDelegateProxy\",&,N,V_delegateProxy"
+ "T@\"_UIHostedFocusSystemItemContainer\",R,N,V_itemContainerProxy"
+ "T@?,C,N,V_fallbackItemProvider"
+ "T@?,C,N,V_fulfillmentHandler"
+ "TB,N,GisEnabled"
+ "TB,N,S_setAutomaticallyPreferOwningItem:"
+ "TB,N,S_setDidSetPreferredFocusedEnvironments:"
+ "TB,N,S_setFocusPriorityRequired:"
+ "TB,N,S_setIgnoresSpeedBumpEdges:"
+ "TB,N,S_setIsUnclippable:"
+ "TB,N,S_setIsUnoccludable:"
+ "TB,R,N,G_isInitialMovement"
+ "The newly focused item or one of its parent environments is getting removed from the hierarchy in response of that item becoming focused. This is a client bug that leaves the focus system in an undefined state. Focused item: %@; environment being removed: %@."
+ "This item returns NO from -canBecomeFocused."
+ "Tq,?,R,N,G_preferredFocusMovementStyle"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame"
+ "UIFocusDebugger"
+ "UIFocusDebugger.m"
+ "UIFocusDebuggerOutput"
+ "UIFocusDidUpdateNotification"
+ "UIFocusEnvironment"
+ "UIFocusEnvironment.m"
+ "UIFocusGeometry.m"
+ "UIFocusGeometryKeyedCoding"
+ "UIFocusItem"
+ "UIFocusItem.m"
+ "UIFocusItem: %@ has mismatched parentFocusEnvironment: %@  from focusItemContainer: %@ with owningEnvironment: %@"
+ "UIFocusItem: %@ with parentFocusEnvironment: %@  focusItemContainer: %@ has no coordinate space."
+ "UIFocusItemContainer"
+ "UIFocusItemContainer.m"
+ "UIFocusItemScrollableContainer"
+ "UIFocusMovementAction"
+ "UIFocusMovementDidFailNotification"
+ "UIFocusMovementHint"
+ "UIFocusSystem"
+ "UIFocusSystem *__UIFocusMapRecurseSearchForFocusSystemInEligibleContainer(__strong id<_UIFocusRegionContainer>, NSHashTable<id<UIFocusEnvironment>> *__strong, NSHashTable<id<UIFocusEnvironment>> *__strong, NSArray<_UIFocusRegionSearchContextState *> *__strong)"
+ "UIFocusSystem.m"
+ "UIFocusUpdateAnimationCoordinatorKey"
+ "UIFocusUpdateContext"
+ "UIFocusUpdateContext.m"
+ "UIFocusUpdateContextKey"
+ "Unable to find focus system for request. Environment does not appear to be in a valid focus environment chain."
+ "Warning: encountered a single UIFocusItemContainer: %@ yielded by two mismatched owning UIFocusEnvironments: %@ and %@. UIFocusItemContainer should be 1:1 with its owning environment."
+ "_UIDebugIssue"
+ "_UIDebugIssueReport"
+ "_UIDebugIssueReport.m"
+ "_UIDebugIssueReportFormatter"
+ "_UIDebugIssueReporting"
+ "_UIDebugLogReport"
+ "_UIDebugLogReport.m"
+ "_UIDebugLogReportFormatter"
+ "_UIDebugLogStatement"
+ "_UIDebugReport.m"
+ "_UIDebugReportComponents"
+ "_UIDebugReportFormatter"
+ "_UIFocusContainerGuideFallbackItemsContainer"
+ "_UIFocusContainerGuideFallbackItemsContainer.m"
+ "_UIFocusContainerGuideImpl"
+ "_UIFocusContainerGuideRegion"
+ "_UIFocusDebuggerStringOutput"
+ "_UIFocusEngineGestureDidBeginNotification"
+ "_UIFocusEnvironmentContainerTuple"
+ "_UIFocusEnvironmentInternal"
+ "_UIFocusEnvironmentPlatformSupport"
+ "_UIFocusEnvironmentPreferenceCache"
+ "_UIFocusEnvironmentPreferenceCache.m"
+ "_UIFocusEnvironmentPreferenceCacheNode"
+ "_UIFocusEnvironmentPreferenceEnumerationContext"
+ "_UIFocusEnvironmentPreferenceEnumerationContextDelegate"
+ "_UIFocusEnvironmentPreferenceEnumerator"
+ "_UIFocusEnvironmentPreferenceEnumerator.m"
+ "_UIFocusEnvironmentPrivate"
+ "_UIFocusEnvironmentScrollableContainerTuple"
+ "_UIFocusEnvironmentScrollableContainerTuple * _Nullable _UIFocusNearestAncestorEnvironmentScrollableContainer(__strong id<UIFocusEnvironment> _Nonnull, BOOL)"
+ "_UIFocusGroup"
+ "_UIFocusGroup.m"
+ "_UIFocusGroupHelperFuncs.m"
+ "_UIFocusGroupHistory"
+ "_UIFocusGroupHistory.m"
+ "_UIFocusGroupMap"
+ "_UIFocusGroupMap.m"
+ "_UIFocusGuideImpl"
+ "_UIFocusGuideImpl.m"
+ "_UIFocusGuideRegion"
+ "_UIFocusGuideRegionDelegate"
+ "_UIFocusInputDeviceInfo"
+ "_UIFocusItemDummy"
+ "_UIFocusItemInfo"
+ "_UIFocusItemInfo.m"
+ "_UIFocusItemRegion"
+ "_UIFocusItemRegion got called with a nil focus system. Inferring focus system found %@"
+ "_UIFocusItemRegion.m"
+ "_UIFocusLinearMovementCache"
+ "_UIFocusLinearMovementSequence"
+ "_UIFocusLinearMovementSequence.m"
+ "_UIFocusMap"
+ "_UIFocusMap.m"
+ "_UIFocusMapArea"
+ "_UIFocusMapArea.m"
+ "_UIFocusMapRect"
+ "_UIFocusMapSearchInfo"
+ "_UIFocusMapSnapshot"
+ "_UIFocusMapSnapshot.m"
+ "_UIFocusMapSnapshotter"
+ "_UIFocusMapSnapshotter.m"
+ "_UIFocusMovementInfo"
+ "_UIFocusMovementPerformer"
+ "_UIFocusMovementPerformer.m"
+ "_UIFocusMovementPerformerDelegate"
+ "_UIFocusMovementRequest"
+ "_UIFocusMovementRequest.m"
+ "_UIFocusMovementStyle _UIFocusEnvironmentInheritedFocusMovementStyle(__strong id<UIFocusEnvironment> _Nonnull)"
+ "_UIFocusNullGroup"
+ "_UIFocusPromiseItem"
+ "_UIFocusPromiseItem.m"
+ "_UIFocusPromiseRegion"
+ "_UIFocusRegion"
+ "_UIFocusRegion.m"
+ "_UIFocusRegionContainer"
+ "_UIFocusRegionContainerProxy"
+ "_UIFocusRegionContainerProxy.m"
+ "_UIFocusRegionEvaluator"
+ "_UIFocusRegionEvaluator.m"
+ "_UIFocusRegionMovementInfo"
+ "_UIFocusRegionSearchContext"
+ "_UIFocusRegionSearchContextState"
+ "_UIFocusSearchInfo"
+ "_UIFocusSpeedBumpRegion"
+ "_UIFocusSystemDelegate"
+ "_UIFocusSystemEnabledStateDidChangeNotification"
+ "_UIFocusTreeLock"
+ "_UIFocusTreeLock.m"
+ "_UIFocusTreeLockItem"
+ "_UIFocusUpdateReport"
+ "_UIFocusUpdateReport.m"
+ "_UIFocusUpdateReportFormatter"
+ "_UIFocusUpdateRequest"
+ "_UIFocusUpdateRequest.m"
+ "_UIFocusUpdateRequesting"
+ "_UIFocusUpdateThrottle"
+ "_UIFocusUpdateThrottle.m"
+ "_UIFocusWeakHelper"
+ "_UIHostedFocusSystem"
+ "_UIHostedFocusSystem.m"
+ "_UIHostedFocusSystemDelegate"
+ "_UIHostedFocusSystemDelegateProxy"
+ "_UIHostedFocusSystemItemContainer"
+ "_allRegionsInContainer:intersectingRegion:"
+ "_allowsFocusToLeaveViaHeading:"
+ "_automaticallyPreferOwningItem"
+ "_childItems"
+ "_closestFocusableItemToPoint:inEnvironment:constrainedToRect:distanceMeasuringUnitPoint:itemFilter:"
+ "_closestFocusableItemToPoint:inRect:itemFilter:distanceMeasuringUnitPoint:"
+ "_debugIdentifier"
+ "_delegateProxy"
+ "_didSetPreferredFocusedEnvironments"
+ "_extantFocusItemsInRect:"
+ "_fallbackItemProvider"
+ "_fallbackRootRegionContainer"
+ "_focusCasting"
+ "_focusEnvironmentWillDisappear:remainingInHierarchy:"
+ "_focusGuideBehaviorForFocusMovement:"
+ "_focusItemGuides"
+ "_focusPriorityRequired"
+ "_focusRegionFrameInCoordinateSpace:"
+ "_focusSystem:containsChildOfHostEnvironment:"
+ "_focusSystem:focusItemsInRect:"
+ "_focusedGuideImpl"
+ "_fulfilledItem"
+ "_fulfillmentHandler"
+ "_hostEnvironment"
+ "_initWithHostEnvironment:"
+ "_initWithItem:useFallbackAncestorScroller:"
+ "_itemContainerProxy"
+ "_linearFocusMovementSequences"
+ "_owningItem"
+ "_preferredFocusMovementStyle"
+ "_setAutomaticallyPreferOwningItem:"
+ "_setDidSetPreferredFocusedEnvironments:"
+ "_setFocusCasting:"
+ "_setFocusPriorityRequired:"
+ "_setFocusedGuideImpl:"
+ "_statusForFocusSystem:includeDeferralTarget:"
+ "_uili_isFocusGuide"
+ "`"
+ "appendObject:withName:skipIfNil:"
+ "appendRect:withName:"
+ "bs_CGRectValue"
+ "bs_valueWithCGRect:"
+ "canBecomeFocused"
+ "childEnvironment"
+ "childItems"
+ "childItems != nil"
+ "containsChildOfHostEnvironment:"
+ "contentSize"
+ "convertPoint:toCoordinateSpace:"
+ "debugIdentifier"
+ "delegate != nil"
+ "delegateProxy"
+ "didHintFocusMovement:"
+ "didUpdateFocusFromGuide:"
+ "didUpdateFocusInContext:"
+ "fallbackItemProvider"
+ "fallbackRootRegionContainer"
+ "focusCasting"
+ "focusDidUpdateViaGuide"
+ "focusGroupIdentifier"
+ "focusGroupPriority"
+ "focusGuide:preferredEnvironmentsForHeading:"
+ "focusItemContainer"
+ "focusItemDeferralMode"
+ "focusItemsInRect:"
+ "focusMovementInfo"
+ "focusedFrame"
+ "forwardingTargetForSelector:"
+ "frameForFocusGuide:"
+ "fulfilledItem"
+ "fulfillmentHandler"
+ "fulfillmentHandler != nil"
+ "hostEnvironment"
+ "id<UICoordinateSpace>  _Nonnull _UIParentCoordinateSpaceForFocusItem(__strong id<UIFocusItem> _Nonnull)"
+ "id<UIFocusEnvironment>  _Nonnull _UIFocusEnvironmentRootAncestorEnvironment(__strong id<UIFocusEnvironment> _Nonnull)"
+ "id<UIFocusItem>  _Nonnull _UIFocusGetNextItemFromList(id<UIFocusItem>  _Nullable __strong, NSArray<id<UIFocusItem>> *__strong _Nonnull, UIFocusHeading, BOOL)"
+ "id<_UIFocusRegionContainer>  _Nullable _UIFocusEnvironmentPreferredFocusMapContainer(__strong id<UIFocusEnvironment> _Nonnull)"
+ "info"
+ "init is unavailable on %@"
+ "initWithDelegate:"
+ "initWithFocusMovementInfo:"
+ "initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:"
+ "initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:focusedFrameInSceneCoordinateSpace:"
+ "initWithFocusSystem:delegate:"
+ "initWithHostedFocusSystem:"
+ "initWithInfo:timeout:forResponseOnQueue:withHandler:"
+ "initWithParentEnvironment:childItems:"
+ "initWithParentEnvironment:frame:fullfillmentHandler:"
+ "isTransparentFocusItem"
+ "itemContainerProxy"
+ "linearFocusMovementSequences"
+ "methodSignatureForSelector:"
+ "numberWithBool:"
+ "objectForSetting:"
+ "owningEnvironment.focusItemContainer == itemContainer"
+ "owningEnvironment.focusItemContainer == scrollableContainer"
+ "owningItem"
+ "parentEnvironment != nil"
+ "parentFocusEnvironment"
+ "po UIFocusDebugger.checkFocusability(for: <item reference>)"
+ "po UIFocusDebugger.simulateFocusUpdateRequest(from: <environment reference>)"
+ "po UIFocusDebugger.status()"
+ "po [UIFocusDebugger checkFocusabilityForItem:<item reference>]"
+ "po [UIFocusDebugger simulateFocusUpdateRequestFromEnvironment:<environment reference>]"
+ "po [UIFocusDebugger status]"
+ "preferredFocusMovementStyle"
+ "q24@?0@\"<UIFocusItem>\"8@\"<UIFocusItem>\"16"
+ "q24@?0@\"_UIFocusGroup\"8@\"_UIFocusGroup\"16"
+ "setContentOffset:"
+ "setDebugIdentifier:"
+ "setDelegateProxy:"
+ "setFallbackItemProvider:"
+ "setFallbackRootRegionContainer:"
+ "setFrame:"
+ "setFulfillmentHandler:"
+ "setObject:forSetting:"
+ "setOwningItem:"
+ "setParentFocusEnvironment:"
+ "setPreferredFocusEnvironments:"
+ "shouldUpdateFocusInContext:"
+ "soundIdentifierForFocusUpdateInContext:"
+ "v16@?0@\"<UIFocusEnvironment>\"8"
+ "v24@0:8@\"<_UIFocusRegionContainer>\"16"
+ "v24@0:8@\"<_UIFocusRegionSearchContext>\"16"
+ "v24@0:8@\"UIFocusMovementHint\"16"
+ "v24@0:8@\"UIFocusUpdateContext\"16"
+ "v24@0:8@\"_UIDebugIssue\"16"
+ "v24@0:8@\"_UIFocusRegion\"16"
+ "v24@?0@\"<UIFocusEnvironment>\"8^B16"
+ "v24@?0@\"<_UIFocusEnvironmentPreferenceEnumerationContext>\"8^q16"
+ "v32@0:8@\"UIFocusSystem\"16@\"<UIFocusItem>\"24"
+ "v32@0:8@\"UIFocusSystem\"16@\"UIFocusUpdateContext\"24"
+ "v32@0:8@\"_UIFocusGuideRegion\"16@\"UIFocusUpdateContext\"24"
+ "v32@?0@\"<UIFocusEnvironment>\"8Q16^B24"
+ "v32@?0@\"_UIDebugIssue\"8Q16^B24"
+ "v32@?0@\"_UIDebugLogStatement\"8Q16^B24"
+ "v32@?0@\"_UIFocusLinearMovementSequence\"8Q16^B24"
+ "v36@?0@\"_UIFocusGroup\"8Q16B24^B28"
+ "v40@0:8@\"UIFocusSystem\"16@\"<UIFocusEnvironment>\"24@\"UIFocusUpdateContext\"32"
+ "visibleSize"
+ "void _CommonInit(_UIFocusItemRegion *__strong, id<UIFocusItem>  _Nullable __strong, UIFocusSystem *__strong)"
+ "void _UIHostedFocusSystemRegister(_UIHostedFocusSystem *__strong)"
+ "void _enumeratePreferredFocusEnvironments(_UIFocusEnvironmentPreferenceEnumerator *__strong, _UIFocusEnvironmentPreferenceEnumerationContext *__strong, void (^__strong)(__strong id<_UIFocusEnvironmentPreferenceEnumerationContext>, _UIFocusEnvironmentPreferenceEnumerationResult *), _UIFocusEnvironmentPreferenceEnumerationResult *)"
+ "{?=\"didFulfillPromise\"b1}"
+ "{?=\"isEnabled\"b1\"isUnoccludable\"b1\"isUnclippable\"b1\"focusPriorityRequired\"b1\"ignoresSpeedBumpEdges\"b1\"didSetPreferredFocusedEnvironments\"b1\"automaticallyPreferOwningItem\"b1\"delegatePreferredEnvironmentsForHeading\"b1}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"<UICoordinateSpace>\"16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@\"UIFocusSystem\"16@\"<UICoordinateSpace>\"24"
- "\n%@%@"
- "   "
- "!\x91Q"
- "(%@) %@"
- "(error) %@"
- "(info) %@"
- "(warning) %@"
- "-init is not a useful initializer for this class. Use one of the designated initializers instead."
- "<_FEFocusRegionContainer: %p; focusItemContainer: %@; owningEnvironment: %@>"
- "@\"<_FECoordinateSpace>\""
- "@\"<_FECoordinateSpace>\"16@0:8"
- "@\"<_FEFocusBehavior>\""
- "@\"<_FEFocusEnvironment>\""
- "@\"<_FEFocusEnvironment>\"16@0:8"
- "@\"<_FEFocusEnvironmentPreferenceEnumerationContextDelegate>\""
- "@\"<_FEFocusGuideRegionDelegate>\""
- "@\"<_FEFocusItem>\""
- "@\"<_FEFocusItemContainer>\""
- "@\"<_FEFocusItemContainer>\"16@0:8"
- "@\"<_FEFocusItemScrollableContainer>\""
- "@\"<_FEFocusMapArea>\"16@0:8"
- "@\"<_FEFocusMovementPerformerDelegate>\""
- "@\"<_FEFocusRegionContainer>\""
- "@\"<_FEFocusRegionContainer>\"16@0:8"
- "@\"<_FEFocusRegionContainer>\"16@?0@\"_FEFocusPromiseRegion\"8"
- "@\"<_FEFocusSystemDelegate>\""
- "@\"<_FEFocusUpdateRequesting>\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"UIImage\""
- "@\"UIResponder\"16@0:8"
- "@\"UIView\""
- "@\"_FEDebugIssueReport\""
- "@\"_FEDebugLogNode\""
- "@\"_FEDebugLogNodeTreeStyle\""
- "@\"_FEDebugLogReport\""
- "@\"_FEDebugLogStack\""
- "@\"_FEDebugLogStack\"16@0:8"
- "@\"_FEFocusCastingController\""
- "@\"_FEFocusEnvironmentContainerTuple\""
- "@\"_FEFocusEnvironmentPreferenceCache\""
- "@\"_FEFocusEnvironmentScrollableContainerTuple\""
- "@\"_FEFocusGroup\""
- "@\"_FEFocusGroupHistory\""
- "@\"_FEFocusGroupMap\""
- "@\"_FEFocusGuide\""
- "@\"_FEFocusInputDeviceInfo\""
- "@\"_FEFocusInputDeviceInfo\"16@0:8"
- "@\"_FEFocusItemInfo\""
- "@\"_FEFocusLinearMovementCache\""
- "@\"_FEFocusMapRect\""
- "@\"_FEFocusMapSearchInfo\""
- "@\"_FEFocusMapSnapshot\""
- "@\"_FEFocusMovementAction\""
- "@\"_FEFocusMovementInfo\""
- "@\"_FEFocusMovementInfo\"16@0:8"
- "@\"_FEFocusMovementPerformer\""
- "@\"_FEFocusRegion\""
- "@\"_FEFocusSearchInfo\""
- "@\"_FEFocusSearchInfo\"16@0:8"
- "@\"_FEFocusSystem\""
- "@\"_FEFocusSystem\"16@0:8"
- "@\"_FEFocusUpdateContext\""
- "@\"_FEFocusUpdateRequest\""
- "@\"_FEFocusUpdateThrottle\""
- "@\"_FETreeLock\""
- "@16@?0@\"<_FEFocusEnvironment>\"8"
- "@16@?0@\"_FEFocusEnvironmentPreferenceCacheNode\"8"
- "@28@0:8Q16B24"
- "@32@0:8Q16@24"
- "@40@0:8@16@24B32B36"
- "@40@0:8@16@24d32"
- "@44@0:8@16d24d32B40"
- "@56@0:8Q16{CGVector=dd}24B40B44q48"
- "@88@0:8{CGPoint=dd}16{CGRect={CGPoint=dd}{CGSize=dd}}32@64{CGPoint=dd}72"
- "@rootNode"
- "B16@?0@\"<_FEFocusEnvironmentPreferenceEnumerationContext>\"8"
- "B16@?0@\"<_FEFocusItem>\"8"
- "B24@0:8@\"_FEFocusEnvironmentPreferenceEnumerationContext\"16"
- "B24@0:8@\"_FEFocusUpdateContext\"16"
- "B24@?0@\"<_FEFocusItem>\"8@\"NSDictionary\"16"
- "B32@0:8@\"_FEFocusMovementRequest\"16@\"_FEFocusMovementPerformer\"24"
- "B32@?0@\"_FEDebugLogMessage\"8Q16^B24"
- "B32@?0@\"_FEFocusEnvironmentScrollableContainerTuple\"8Q16^B24"
- "B32@?0@\"_FEFocusGroup\"8Q16^B24"
- "B96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80d88"
- "BOOL _FEFocusEnvironmentIsEligibleForFocusInteraction(__strong id<_FEFocusEnvironment> _Nonnull)"
- "BOOL _FEFocusEnvironmentIsEligibleForFocusOcclusion(__strong id<_FEFocusEnvironment> _Nonnull, BOOL * _Nullable)"
- "BOOL _FEFocusEnvironmentShouldUpdateFocus(__strong id<_FEFocusEnvironment> _Nonnull, _FEFocusUpdateContext *__strong _Nonnull)"
- "BOOL _FEFocusItemCanBecomeFocused(__strong id<_FEFocusItem> _Nonnull, _FEFocusSystem *__strong _Nonnull)"
- "BOOL _FEFocusItemIsFocusableInFocusSystem(__strong id<_FEFocusItem> _Nonnull, _FEFocusSystem *__strong _Nonnull)"
- "BOOL _FEFocusItemIsFocusableInFocusSystemWithSearchInfo(__strong id<_FEFocusItem> _Nonnull, _FEFocusSystem *__strong _Nonnull, _FEFocusSearchInfo *__strong _Nonnull)"
- "BOOL _FEFocusItemIsFocused(__strong id<_FEFocusItem> _Nonnull)"
- "BOOL _FEFocusItemIsFocusedOrFocusable(__strong id<_FEFocusItem> _Nonnull)"
- "BOOL _FEFocusItemIsFocusedOrFocusableInFocusSystem(__strong id<_FEFocusItem> _Nonnull, _FEFocusSystem *__strong _Nonnull)"
- "BOOL __UIFocusItemIsFocusedOrFocusableInFocusSystem(__strong id<_FEFocusItem>, _FEFocusSystem *__strong, BOOL, BOOL)"
- "C"
- "FocusCastingVisualization"
- "FocusEngineDummy"
- "Imbalanced calls to push and pop. Expected node %@ to be popped but got %@."
- "It looks like you are calling a _FEFocusDebugger method outside of lldb. That is not allowed."
- "NOTE: `-[UIView _whyIsThisViewNotFocusable]` is deprecated. Use `+[_FEFocusDebugger checkFocusabilityForItem:]` instead.\nFor more information, try `po [_FEFocusDebugger help]` in LLDB.\n\n%@"
- "NSArray<id<_FEFocusEnvironment>> * _Nonnull _FEFocusEnvironmentEffectivePreferredFocusEnvironments(__strong id<_FEFocusEnvironment> _Nonnull, BOOL * _Nullable)"
- "NSComparisonResult _FEFocusGroupCompare(_FEFocusGroup * _Nonnull __strong, _FEFocusGroup * _Nonnull __strong)"
- "NSString * _Nonnull _FEFocusGroupIdentifierForInstance(id  _Nonnull __strong)"
- "NSString * _Nonnull _prefixForItem(BOOL, BOOL, _FEDebugLogNodeTreeStyle * _Nonnull __strong)"
- "Observer is not of type id<_FEFocusStateObserverToken>."
- "Quick Look is only available for focus updates that represent a user-initiated focus movement."
- "Quick Look is unavailable for this focus update."
- "T@\"<_FECoordinateSpace>\",R,N"
- "T@\"<_FECoordinateSpace>\",R,N,V_coordinateSpace"
- "T@\"<_FECoordinateSpace>\",R,N,V_regionCoordinateSpace"
- "T@\"<_FECoordinateSpace>\",R,W,N"
- "T@\"<_FECoordinateSpace>\",R,W,N,V_coordinateSpace"
- "T@\"<_FEFocusBehavior>\",&,N,V_behavior"
- "T@\"<_FEFocusBehavior>\",R,N,V_focusBehavior"
- "T@\"<_FEFocusEnvironment>\",R,N"
- "T@\"<_FEFocusEnvironment>\",R,N,G_disappearingFocusEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,N,V_environment"
- "T@\"<_FEFocusEnvironment>\",R,N,V_owningEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,N,V_resolvedEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,W,N"
- "T@\"<_FEFocusEnvironment>\",R,W,N,G_commonAncestorEnvironment,V_commonAncestorEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,W,N,G_initialDestinationEnvironment,V_initialDestinationEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,W,N,V_deepestPreferredFocusEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,W,N,V_destinationEnvironment"
- "T@\"<_FEFocusEnvironment>\",R,W,N,V_environment"
- "T@\"<_FEFocusEnvironment>\",W,N,V__parentFocusEnvironment"
- "T@\"<_FEFocusEnvironment>\",W,N,V_owningEnvironment"
- "T@\"<_FEFocusEnvironmentPreferenceEnumerationContextDelegate>\",W,N,V_delegate"
- "T@\"<_FEFocusGuideRegionDelegate>\",W,N,V_delegate"
- "T@\"<_FEFocusItem>\",R,N,V_primaryItem"
- "T@\"<_FEFocusItem>\",R,W,N"
- "T@\"<_FEFocusItem>\",R,W,N,G_previousFocusedItem,V_previousFocusedItem"
- "T@\"<_FEFocusItem>\",R,W,N,V_focusedItem"
- "T@\"<_FEFocusItem>\",R,W,N,V_item"
- "T@\"<_FEFocusItemContainer>\",R,N"
- "T@\"<_FEFocusItemContainer>\",R,N,V_itemContainer"
- "T@\"<_FEFocusItemScrollableContainer>\",R,N,V_scrollableContainer"
- "T@\"<_FEFocusMapArea>\",R,N"
- "T@\"<_FEFocusMovementPerformerDelegate>\",W,N,V_delegate"
- "T@\"<_FEFocusRegionContainer>\",&,N,V_contentFocusRegionContainer"
- "T@\"<_FEFocusRegionContainer>\",?,R,W,N,G_focusMapContainer"
- "T@\"<_FEFocusRegionContainer>\",R,N,V_regionContainer"
- "T@\"<_FEFocusRegionContainer>\",R,W,N,V_regionsContainer"
- "T@\"<_FEFocusRegionContainer>\",R,W,N,V_rootContainer"
- "T@\"<_FEFocusRegionContainer>\",W,N,V_regionsContainer"
- "T@\"<_FEFocusSystemDelegate>\",W,N,V_delegate"
- "T@\"<_FEFocusUpdateRequesting>\",R,N,G_request,V_request"
- "T@\"NSArray\",&,N,G_regionMapSnapshots,S_setRegionMapSnapshots:,V_regionMapSnapshots"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSString\",R,N,V_intermediate"
- "T@\"NSString\",R,N,V_lastNode"
- "T@\"NSString\",R,N,V_node"
- "T@\"NSString\",R,N,V_trailing"
- "T@\"UIImage\",R,N,G_regionMapSnapshotsVisualRepresentation,V_regionMapSnapshotsVisualRepresentation"
- "T@\"UIImage\",R,N,V_image"
- "T@\"UIView\",&,N,V_focusCastingIndicator"
- "T@\"UIView\",&,N,V_focusEntryIndicator"
- "T@\"UIView\",&,N,V_focusMovementIndicator"
- "T@\"_FEDebugIssueReport\",&,N,G_validationReport,S_setValidationReport:,V_validationReport"
- "T@\"_FEDebugIssueReport\",R,N,G_subissueReport,V_subissueReport"
- "T@\"_FEDebugIssueReportFormatter\",R,C,N,G_defaultValidationReportFormatter"
- "T@\"_FEDebugLogNode\",&,N,V_debugLog"
- "T@\"_FEDebugLogNode\",R,N"
- "T@\"_FEDebugLogNodeTreeStyle\",&,N,V_treeStyle"
- "T@\"_FEDebugLogReport\",&,N,G_preferredFocusReport,S_setPreferredFocusReport:,V_preferredFocusReport"
- "T@\"_FEDebugLogStack\",&,N,V_debugStack"
- "T@\"_FEDebugLogStack\",R,N"
- "T@\"_FEFocusCastingController\",&,N,G_focusCastingController,S_setFocusCastingController:,V_focusCastingController"
- "T@\"_FEFocusEnvironmentContainerTuple\",&,N,V_environmentContainer"
- "T@\"_FEFocusEnvironmentPreferenceCache\",R,N,V_deepestPreferredFocusableItemCacheForCurrentUpdate"
- "T@\"_FEFocusEnvironmentScrollableContainerTuple\",&,N,G_commonEnvironmentScrollableContainer,S_setCommonEnvironmentScrollableContainer:,V_commonEnvironmentScrollableContainer"
- "T@\"_FEFocusGroup\",R,W,N,V_parentGroup"
- "T@\"_FEFocusGroupHistory\",R,N,G_focusGroupHistory,V_focusGroupHistory"
- "T@\"_FEFocusGroupMap\",&,N,V_focusGroupMap"
- "T@\"_FEFocusGroupMap\",R,N,V_focusGroupMap"
- "T@\"_FEFocusGuide\",R,W,N,G_focusedGuide,V_focusedGuide"
- "T@\"_FEFocusInputDeviceInfo\",&,N,V_inputDeviceInfo"
- "T@\"_FEFocusInputDeviceInfo\",R,N"
- "T@\"_FEFocusItemInfo\",&,N,V_focusedItemInfo"
- "T@\"_FEFocusItemInfo\",R,C,N,G_destinationItemInfo,V_destinationItemInfo"
- "T@\"_FEFocusItemInfo\",R,C,N,G_sourceItemInfo,V_sourceItemInfo"
- "T@\"_FEFocusLinearMovementCache\",&,N,G_focusMovementCache,S_setFocusMovementCache:,V_focusMovementCache"
- "T@\"_FEFocusMapRect\",R,N,G_searchArea,V_searchArea"
- "T@\"_FEFocusMapRect\",R,N,V_mapArea"
- "T@\"_FEFocusMapSearchInfo\",&,N,G_focusMapSearchInfo,S_setFocusMapSearchInfo:,V_focusMapSearchInfo"
- "T@\"_FEFocusMapSearchInfo\",R,N,G_defaultItemSearchContext,V_defaultItemSearchInfo"
- "T@\"_FEFocusMapSearchInfo\",R,N,G_focusMovementSearchContext,V_focusMovementSearchInfo"
- "T@\"_FEFocusMapSearchInfo\",R,W,N,V_focusMapSearchInfo"
- "T@\"_FEFocusMapSnapshot\",R,N,V_snapshot"
- "T@\"_FEFocusMapSnapshotDebugInfo\",R,N,G_debugInfo"
- "T@\"_FEFocusMovementAction\",&,N,V_pendingFocusMovementAction"
- "T@\"_FEFocusMovementInfo\",&,N,V_movementInfo"
- "T@\"_FEFocusMovementInfo\",R,N"
- "T@\"_FEFocusMovementInfo\",R,N,G_focusMovement,V_focusMovement"
- "T@\"_FEFocusMovementPerformer\",R,N,V_movementPerformer"
- "T@\"_FEFocusMovementRequest\",R,N"
- "T@\"_FEFocusRegion\",&,N,V_focusedRegion"
- "T@\"_FEFocusRegion\",R,C,N,V_focusedRegion"
- "T@\"_FEFocusRegion\",R,N,V_focusedRegion"
- "T@\"_FEFocusSearchInfo\",&,N,V_searchInfo"
- "T@\"_FEFocusSearchInfo\",R,N"
- "T@\"_FEFocusSearchInfo\",R,N,V_searchInfo"
- "T@\"_FEFocusSystem\",R,N,V_regionContainerFocusSystem"
- "T@\"_FEFocusSystem\",R,W,N"
- "T@\"_FEFocusSystem\",R,W,N,G_hostFocusSystem"
- "T@\"_FEFocusSystem\",R,W,N,V_focusSystem"
- "T@\"_FEFocusSystem\",W,N,V_focusSystem"
- "T@\"_FEFocusUpdateContext\",&,N,V_context"
- "T@\"_FEFocusUpdateThrottle\",R,N,V_updateThrottle"
- "T@\"_FETreeLock\",R,N,V_treeLock"
- "T@,R,N,V_associatedObject"
- "T@,R,N,V_color"
- "TB,?,N"
- "TB,N,GisEnabled,V_enabled"
- "TB,N,V_isRememberingEntryPoint"
- "TB,R,N,GisActive"
- "TB,R,N,V_dashedStroke"
- "TQ,N,V_entryPointAxis"
- "T^{CGPattern=},R,N,V_pattern"
- "Td,N,V_entryPointMemorizationTimeout"
- "Td,R,N,V_patternAlpha"
- "This is an abstract class. isActive needs to be implemented by a concrete subclass."
- "This item returns NO from -_canBecomeFocused."
- "T{CGPoint=dd},N,V_screenEntryPoint"
- "T{CGPoint=dd},R,N,V_imageAnchorPoint"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V__focusFrame"
- "UIApplication"
- "UUID"
- "Unable to get normalized coordinate space for focus casting."
- "Unable to pop the last node on the stack. This indicates an imbalance in push and pop calls."
- "Visual description unavailable"
- "Warning: encountered a single _FEFocusItemContainer: %@ yielded by two mismatched owning _FEFocusEnvironments: %@ and %@. _FEFocusItemContainer should be 1:1 with its owning environment."
- "^{CGPattern=}"
- "^{CGPattern=}16@0:8"
- "_FEDebugIssue"
- "_FEDebugIssueReport"
- "_FEDebugIssueReport.m"
- "_FEDebugIssueReportFormatter"
- "_FEDebugIssueReporting"
- "_FEDebugLogMessage"
- "_FEDebugLogNode"
- "_FEDebugLogNodeTreeStyle"
- "_FEDebugLogReport"
- "_FEDebugLogReport.m"
- "_FEDebugLogReportFormatter"
- "_FEDebugLogStack"
- "_FEDebugLogStatement"
- "_FEDebugLogTree.m"
- "_FEDebugReport.m"
- "_FEDebugReportComponents"
- "_FEDebugReportFormatter"
- "_FEFocusCastingController"
- "_FEFocusContainerGuideRegion"
- "_FEFocusDebugger"
- "_FEFocusDebugger.m"
- "_FEFocusDebuggerOutput"
- "_FEFocusDebuggerStringOutput"
- "_FEFocusDebugging"
- "_FEFocusDidUpdateNotification"
- "_FEFocusEngineGestureDidBeginNotification"
- "_FEFocusEnvironment"
- "_FEFocusEnvironment.m"
- "_FEFocusEnvironmentContainerTuple"
- "_FEFocusEnvironmentInternal"
- "_FEFocusEnvironmentPreferenceCache"
- "_FEFocusEnvironmentPreferenceCache.m"
- "_FEFocusEnvironmentPreferenceCacheNode"
- "_FEFocusEnvironmentPreferenceEnumerationContext"
- "_FEFocusEnvironmentPreferenceEnumerationContextDelegate"
- "_FEFocusEnvironmentPreferenceEnumerator"
- "_FEFocusEnvironmentPreferenceEnumerator.m"
- "_FEFocusEnvironmentPrivate"
- "_FEFocusEnvironmentScrollableContainerTuple"
- "_FEFocusEnvironmentScrollableContainerTuple * _Nullable _FEFocusNearestAncestorEnvironmentScrollableContainer(__strong id<_FEFocusEnvironment> _Nonnull, BOOL)"
- "_FEFocusGeometry.m"
- "_FEFocusGroup"
- "_FEFocusGroup.m"
- "_FEFocusGroupHelperFuncs.m"
- "_FEFocusGroupHistory"
- "_FEFocusGroupHistory.m"
- "_FEFocusGroupMap"
- "_FEFocusGroupMap.m"
- "_FEFocusGuideRegion"
- "_FEFocusInputDeviceInfo"
- "_FEFocusItem"
- "_FEFocusItem.m"
- "_FEFocusItem: %@ has mismatched parentFocusEnvironment: %@  from focusItemContainer: %@ with owningEnvironment: %@"
- "_FEFocusItem: %@ with parentFocusEnvironment: %@  focusItemContainer: %@ has no coordinate space."
- "_FEFocusItemContainer"
- "_FEFocusItemContainer.m"
- "_FEFocusItemDummy"
- "_FEFocusItemFrameReporter"
- "_FEFocusItemInfo"
- "_FEFocusItemInfo.m"
- "_FEFocusItemRegion"
- "_FEFocusItemRegion got called with a nil focus system. Inferring focus system found %@"
- "_FEFocusItemRegion.m"
- "_FEFocusItemScrollableContainer"
- "_FEFocusLinearMovementCache"
- "_FEFocusLinearMovementSequence"
- "_FEFocusLinearMovementSequence.m"
- "_FEFocusMap"
- "_FEFocusMap.m"
- "_FEFocusMapArea"
- "_FEFocusMapArea.m"
- "_FEFocusMapRect"
- "_FEFocusMapSearchInfo"
- "_FEFocusMapSnapshot"
- "_FEFocusMapSnapshot.m"
- "_FEFocusMapSnapshotDebugInfo"
- "_FEFocusMapSnapshotDebugInfo.m"
- "_FEFocusMapSnapshotter"
- "_FEFocusMapSnapshotter.m"
- "_FEFocusMovementDidFailNotification"
- "_FEFocusMovementHint"
- "_FEFocusMovementInfo"
- "_FEFocusMovementPerformer"
- "_FEFocusMovementPerformer.m"
- "_FEFocusMovementPerformerDelegate"
- "_FEFocusMovementRequest"
- "_FEFocusMovementRequest.m"
- "_FEFocusMovementStyle _FEFocusEnvironmentInheritedFocusMovementStyle(__strong id<_FEFocusEnvironment> _Nonnull)"
- "_FEFocusNullGroup"
- "_FEFocusPromiseRegion"
- "_FEFocusRegion"
- "_FEFocusRegion.m"
- "_FEFocusRegionContainer"
- "_FEFocusRegionContainerProxy"
- "_FEFocusRegionContainerProxy.m"
- "_FEFocusRegionDebugDrawingConfiguration"
- "_FEFocusRegionDebugQuickLook"
- "_FEFocusRegionEvaluator"
- "_FEFocusRegionEvaluator.m"
- "_FEFocusRegionMovementInfo"
- "_FEFocusRegionSearchContext"
- "_FEFocusRegionSearchContextState"
- "_FEFocusSearchInfo"
- "_FEFocusSensitivitySetting"
- "_FEFocusSensitivityUpdateNotification"
- "_FEFocusSpeedBumpRegion"
- "_FEFocusStateObserver"
- "_FEFocusStateObserver.m"
- "_FEFocusSystem"
- "_FEFocusSystem *__UIFocusMapRecurseSearchForFocusSystemInEligibleContainer(__strong id<_FEFocusRegionContainer>, NSHashTable<id<_FEFocusEnvironment>> *__strong, NSHashTable<id<_FEFocusEnvironment>> *__strong, NSArray<_FEFocusRegionSearchContextState *> *__strong)"
- "_FEFocusSystem.m"
- "_FEFocusSystemEnabledStateDidChangeNotification"
- "_FEFocusUpdateContext"
- "_FEFocusUpdateContext.m"
- "_FEFocusUpdateContextKey"
- "_FEFocusUpdateReport"
- "_FEFocusUpdateReport.m"
- "_FEFocusUpdateReportFormatter"
- "_FEFocusUpdateRequest"
- "_FEFocusUpdateRequest.m"
- "_FEFocusUpdateRequesting"
- "_FEFocusUpdateThrottle"
- "_FEFocusUpdateThrottle.m"
- "_FEGeometry.m"
- "_FEGeometryKeyedCoding"
- "_FETreeLock"
- "_FETreeLock.m"
- "_FETreeLockItem"
- "_FEWeakHelper"
- "__FEDebugLogRootNode"
- "__focusFrame"
- "__genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:"
- "__isKindOfUIScrollView"
- "__isKindOfUIView"
- "__isKindOfUIViewController"
- "__parentFocusEnvironment"
- "_allDefaultFocusableRegionsInContainer:intersectingRegion:"
- "_allFocusableItemsInEnvironment:"
- "_appendChildDescription:withPrefix:inheritedTreeStyle:"
- "_areChildrenFocused"
- "_associatedObject"
- "_axisForHeading:"
- "_canBecomeFocused"
- "_cancelRepeatingFrameUpdate"
- "_castingFrameForFocusedNormalizedFrame:heading:"
- "_castingPointInNormalizedFrame:forHeading:"
- "_childMessages"
- "_closestFocusableItemToPoint:inRect:excludingItems:distanceMeasuringUnitPoint:"
- "_color"
- "_createFocusMovementIndicator"
- "_dashedStroke"
- "_debugDrawingConfigurationWithDebugInfo:"
- "_debugInfo"
- "_debugInfoWithFocusMapSearchInfo:"
- "_destroyFocusMovementIndicator"
- "_drawImage"
- "_entryPointAxis"
- "_entryPointInNormalizedFrame:forHeading:"
- "_entryPointMemorizationTimeout"
- "_findAllDefaultFocusableRegionsWithSnapshotter:"
- "_focusAllowsLeavingWithHeading:"
- "_focusCastingController"
- "_focusCastingIndicator"
- "_focusContentOffset"
- "_focusContentSize"
- "_focusCoordinateSpace"
- "_focusDeferralMode"
- "_focusEffectsControllerForFocusedItem"
- "_focusEntryIndicator"
- "_focusFrame"
- "_focusGroupIdentifier"
- "_focusGroupPriority"
- "_focusGuideBehaviorForMovement:"
- "_focusItemContainer"
- "_focusItemsInRect:"
- "_focusLinearMovementSequence"
- "_focusMapSnapshotDebugInfoArray"
- "_focusMovementIndicator"
- "_focusPreferredMovementStyle"
- "_focusResponderForwardingTarget"
- "_focusRotaryMovementAxis"
- "_focusSystem:isScrollingScrollableContainer:"
- "_focusSystemEnabledStateDidChange:"
- "_focusVisibleSize"
- "_focusedFrameUpdateTimer"
- "_globalFrameForFocusedItemInSystem:"
- "_hasStagedFocusFrameUpdate"
- "_image"
- "_imageAnchorPoint"
- "_initWithItem:containingView:useFallbackAncestorScroller:"
- "_intermediate"
- "_isNode"
- "_isRememberingEntryPoint"
- "_isTransparent"
- "_isTransparentFocusItem"
- "_isTransparentFocusRegion"
- "_lastNode"
- "_legacy_checkFocusabilityForView:"
- "_movementPointInNormalizedFrame:"
- "_movementWithHeading:isInitial:"
- "_node"
- "_normalizedCoordinateSpace"
- "_observers"
- "_pattern"
- "_patternAlpha"
- "_performBlockAfterCATransactionCommits:"
- "_positionFocusMovementIndicators"
- "_publicRegionMapSnapshots"
- "_rect:differsFromRect:lowerThreshold:upperThreshold:"
- "_rectContainingAllFocusRegions"
- "_regionMapSnapshots"
- "_regionMapSnapshotsVisualRepresentation"
- "_reportFocusFrameForCurrentlyFocusedItem"
- "_reportFocusFrameUpdateForGlobalFrame:"
- "_requiresFocusedItemToBeInHierarchy"
- "_scheduleRepeatingFrameUpdate"
- "_screenEntryPoint"
- "_setFocusCastingController:"
- "_setFocusedGuide:"
- "_setRegionMapSnapshots:"
- "_snapshot"
- "_stack"
- "_startRememberingEntryPoint"
- "_statusForFocusSystem:scene:includeSceneLog:includeDeferralTarget:"
- "_stopRememberingEntryPoint"
- "_string"
- "_stringRepresentation"
- "_summaryImageForDebugInfoArray:forFocusMovementWithInfo:scaleFactor:"
- "_topNode"
- "_trailing"
- "_treeStyle"
- "_updateFocusItemFromNormalizedFrame:toNormalizedFrame:withHeading:"
- "_updateFocusMovementIndicatorDisplay"
- "active"
- "addObserver:"
- "addObserver:selector:name:object:"
- "appendArraySection:withName:skipIfEmpty:"
- "appendInteger:withName:"
- "appendString:withName:"
- "arrayWithObject:"
- "associatedObject"
- "block != NULL"
- "bundleIdentifier"
- "color"
- "com.apple.PineBoard"
- "containerGuideConfigurationForRegion:"
- "dashedStroke"
- "debugInfo"
- "debugQuickLookObject"
- "defaultStyle"
- "descriptionBuilder"
- "drawDebugQuickLookImageForRegion:withInfo:inContext:"
- "entryPointAxis"
- "entryPointMemorizationTimeout"
- "focusCastingController"
- "focusCastingIndicator"
- "focusEffectsController:updateMovementDirection:"
- "focusEntryIndicator"
- "focusMovementIndicator"
- "forceUpdateFocusCastingFocusedRect:coordinateSpace:heading:"
- "format"
- "guideConfigurationForRegion:"
- "handler"
- "hasMessages"
- "id<_FEFocusEnvironment>  _Nonnull _FEFocusEnvironmentRootAncestorEnvironment(__strong id<_FEFocusEnvironment> _Nonnull)"
- "id<_FEFocusItem>  _Nonnull _FEFocusGetNextItemFromList(id<_FEFocusItem>  _Nullable __strong, NSArray<id<_FEFocusItem>> *__strong _Nonnull, _FEFocusHeading, BOOL)"
- "id<_FEFocusRegionContainer>  _Nullable _FEFocusEnvironmentPreferredFocusMapContainer(__strong id<_FEFocusEnvironment> _Nonnull)"
- "image"
- "imageAnchorPoint"
- "indexOfObjectWithOptions:passingTest:"
- "initWithCapacity:"
- "initWithHeading:velocity:isInitial:shouldLoadScrollableContainer:groupFilter:"
- "initWithNode:lastNode:intermediate:trailing:"
- "initWithRegion:baseHue:patternAlpha:dashedStroke:"
- "initWithSnapshot:focusMapSearchInfo:"
- "intermediate"
- "isActive"
- "isRememberingEntryPoint"
- "itemConfigurationForRegion:"
- "lastNode"
- "legacyIsTransparentFocusRegionSupported"
- "mainBundle"
- "message != nil && [message isKindOfClass:[_FEDebugLogMessage class]]"
- "messageWithNewline"
- "modernFocusedItemGetterBehavior"
- "node"
- "node != nil && [node isKindOfClass:[_FEDebugLogNode class]]"
- "notifyObserversIfNecessary"
- "numberWithInteger:"
- "observers"
- "owningEnvironment._focusItemContainer == itemContainer"
- "owningEnvironment._focusItemContainer == scrollableContainer"
- "pattern"
- "patternAlpha"
- "performSelector:withObject:afterDelay:"
- "performUpdatesAndNotifyObservers:"
- "performWithPushedNode:block:"
- "po [_FEFocusDebugger checkFocusabilityForItem:<item reference>]"
- "po [_FEFocusDebugger simulateFocusUpdateRequestFromEnvironment:<environment reference>]"
- "po [_FEFocusDebugger status]"
- "po _FEFocusDebugger.checkFocusability(for: <item reference>)"
- "po _FEFocusDebugger.simulateFocusUpdateRequest(from: <environment reference>)"
- "po _FEFocusDebugger.status()"
- "promiseConfigurationForRegion:"
- "q24@?0@\"<_FEFocusItem>\"8@\"<_FEFocusItem>\"16"
- "q24@?0@\"_FEFocusGroup\"8@\"_FEFocusGroup\"16"
- "regionMapSnapshots"
- "regionMapSnapshotsVisualRepresentation"
- "removeFromSuperview"
- "removeObserver:"
- "removeObserver:name:object:"
- "scene: %@"
- "screenEntryPoint"
- "set"
- "setBounds:"
- "setCenter:"
- "setEntryPointAxis:"
- "setEntryPointMemorizationTimeout:"
- "setFocusCastingIndicator:"
- "setFocusEntryIndicator:"
- "setFocusMovementIndicator:"
- "setHidden:"
- "setIsRememberingEntryPoint:"
- "setScreenEntryPoint:"
- "setTreeStyle:"
- "set_areChildrenFocused:"
- "set_focusContentOffset:"
- "set_focusFrame:"
- "set_parentFocusEnvironment:"
- "sharedApplication"
- "softlink:o:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"
- "string != nil"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "styleWithNode:lastNode:intermediate:trailing:"
- "synchronize"
- "trailing"
- "treeStyle"
- "treeStyle != nil"
- "uppercaseString"
- "v16@?0@\"<_FEFocusEnvironment>\"8"
- "v24@0:8@\"<_FEFocusRegionContainer>\"16"
- "v24@0:8@\"<_FEFocusRegionSearchContext>\"16"
- "v24@0:8@\"_FEDebugIssue\"16"
- "v24@0:8@\"_FEFocusRegion\"16"
- "v24@0:8@\"_FEFocusUpdateContext\"16"
- "v24@?0@\"<_FEFocusEnvironment>\"8^B16"
- "v24@?0@\"<_FEFocusEnvironmentPreferenceEnumerationContext>\"8^q16"
- "v32@?0@\"<_FEFocusEnvironment>\"8Q16^B24"
- "v32@?0@\"_FEDebugIssue\"8Q16^B24"
- "v32@?0@\"_FEDebugLogMessage\"8@\"NSString\"16@\"NSMutableString\"24"
- "v32@?0@\"_FEDebugLogStatement\"8Q16^B24"
- "v32@?0@\"_FEFocusLinearMovementSequence\"8Q16^B24"
- "v36@?0@\"_FEFocusGroup\"8Q16B24^B28"
- "v40@0:8@16@24^{CGContext=}32"
- "v40@0:8@16{CGVector=dd}24"
- "v56@0:8@16@24@32:40@?48"
- "v64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48Q56"
- "v88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48Q80"
- "valueWithCGRect:"
- "visualDescription"
- "void _CommonInit(_FEFocusItemRegion *__strong, id<_FEFocusItem>  _Nullable __strong, _FEFocusSystem *__strong)"
- "void _enumeratePreferredFocusEnvironments(_FEFocusEnvironmentPreferenceEnumerator *__strong, _FEFocusEnvironmentPreferenceEnumerationContext *__strong, void (^__strong)(__strong id<_FEFocusEnvironmentPreferenceEnumerationContext>, _FEFocusEnvironmentPreferenceEnumerationResult *), _FEFocusEnvironmentPreferenceEnumerationResult *)"
- "wasActive"
- "{?=\"wasActive\"b1\"supressNotifyObservers\"b1}"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGPoint=dd}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"<_FECoordinateSpace>\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16Q24@32"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48"

```
