## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-355.2.12.101.0
-  __TEXT.__text: 0x75730
-  __TEXT.__objc_methlist: 0x972c
-  __TEXT.__const: 0x848
-  __TEXT.__cstring: 0x7b16
-  __TEXT.__oslogstring: 0x47a0
-  __TEXT.__gcc_except_tab: 0xc4c
+355.3.7.0.0
+  __TEXT.__text: 0x83a70
+  __TEXT.__objc_methlist: 0xa2c4
+  __TEXT.__const: 0x8a8
+  __TEXT.__cstring: 0x8759
+  __TEXT.__gcc_except_tab: 0xe34
+  __TEXT.__oslogstring: 0x6de3
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x32c0
+  __TEXT.__unwind_info: 0x37c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x22e8
-  __DATA_CONST.__objc_classlist: 0x340
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__const: 0x24b8
+  __DATA_CONST.__objc_classlist: 0x378
+  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5160
+  __DATA_CONST.__objc_selrefs: 0x5788
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x898
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x6000
-  __AUTH_CONST.__objc_const: 0x193b8
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_arraydata: 0x1e0
+  __DATA_CONST.__got: 0x8f0
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0x6840
+  __AUTH_CONST.__objc_const: 0x1ac88
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x90
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH.__objc_data: 0x2030
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH.__objc_data: 0x2260
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x9bc
-  __DATA.__data: 0x16a0
+  __DATA.__objc_ivar: 0xb08
+  __DATA.__data: 0x1760
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3760
-  Symbols:   6098
-  CStrings:  1425
+  Functions: 4111
+  Symbols:   6609
+  CStrings:  1647
 
Symbols:
+ +[PBUIPosterWallpaperRemoteViewController supportsLandscapeWallpaperContentsForDisplayConfiguration:]
+ +[_PBUIPendingSceneOperation activateOperationWithBlock:completion:]
+ +[_PBUIPendingSceneOperation updateOperationWithBlock:completion:]
+ -[FBScene(PaperBoard) _pb_enqueueOperation:]
+ -[FBScene(PaperBoard) _pb_pendingOperations]
+ -[FBScene(PaperBoard) _pb_reallyActivate:withCompletion:]
+ -[FBScene(PaperBoard) _pb_reallyUpdate:withCompletion:]
+ -[FBScene(PaperBoard) pb_coalescingScheduler]
+ -[FBScene(PaperBoard) pb_flushCoalescedUpdatesIfNeeded]
+ -[FBScene(PaperBoard) pb_setCoalescingScheduler:]
+ -[FBScene(PaperBoard) pb_updateImmediately:]
+ -[PBUICachedSnapshotEffectProvider _effectiveSnapshotImage]
+ -[PBUICachedSnapshotEffectProvider setFallbackImage:key:]
+ -[PBUICoalescingUpdateScheduler .cxx_destruct]
+ -[PBUICoalescingUpdateScheduler _flushIfPending]
+ -[PBUICoalescingUpdateScheduler _invokeFlushHandler]
+ -[PBUICoalescingUpdateScheduler _removeRunLoopObserver]
+ -[PBUICoalescingUpdateScheduler _scheduleRunLoopFlushIfNeeded]
+ -[PBUICoalescingUpdateScheduler beginCoalescingWindowForReason:]
+ -[PBUICoalescingUpdateScheduler coalescesEveryRunLoopTurn]
+ -[PBUICoalescingUpdateScheduler dealloc]
+ -[PBUICoalescingUpdateScheduler flushNow]
+ -[PBUICoalescingUpdateScheduler initWithIdentifier:flushHandler:]
+ -[PBUICoalescingUpdateScheduler invalidate]
+ -[PBUICoalescingUpdateScheduler isFlushing]
+ -[PBUICoalescingUpdateScheduler noteUpdatePendingRequiringImmediateFlush:]
+ -[PBUICoalescingUpdateScheduler noteUpdatePending]
+ -[PBUICoalescingUpdateScheduler setCoalescesEveryRunLoopTurn:]
+ -[PBUIEffectTrackingReplicaView lastLoggedShowSnapshot]
+ -[PBUIEffectTrackingReplicaView setLastLoggedShowSnapshot:]
+ -[PBUIFakeBlurView _performRotateToInterfaceOrientation:]
+ -[PBUIFrozenFloatingLayerPortalSource .cxx_destruct]
+ -[PBUIFrozenFloatingLayerPortalSource _tearDown]
+ -[PBUIFrozenFloatingLayerPortalSource acquireSourceUsageAssertionForView:]
+ -[PBUIFrozenFloatingLayerPortalSource cacheIdentifier]
+ -[PBUIFrozenFloatingLayerPortalSource currentReplicas]
+ -[PBUIFrozenFloatingLayerPortalSource dealloc]
+ -[PBUIFrozenFloatingLayerPortalSource descriptionBuilderWithMultilinePrefix:]
+ -[PBUIFrozenFloatingLayerPortalSource descriptionWithMultilinePrefix:]
+ -[PBUIFrozenFloatingLayerPortalSource description]
+ -[PBUIFrozenFloatingLayerPortalSource effectsAreBakedIn]
+ -[PBUIFrozenFloatingLayerPortalSource initWithFloatingView:inContainerView:screen:legibilitySettings:forReason:]
+ -[PBUIFrozenFloatingLayerPortalSource invalidate]
+ -[PBUIFrozenFloatingLayerPortalSource legibilitySettings]
+ -[PBUIFrozenFloatingLayerPortalSource reason]
+ -[PBUIFrozenFloatingLayerPortalSource screen]
+ -[PBUIFrozenFloatingLayerPortalSource succinctDescriptionBuilder]
+ -[PBUIFrozenFloatingLayerPortalSource succinctDescription]
+ -[PBUIFrozenFloatingLayerPortalSource targetView]
+ -[PBUIPortalReplicaView _reloadPortalSourceView]
+ -[PBUIPortalReplicaView _setPortalSourceView:]
+ -[PBUIPortalReplicaView _sourceViewDidMoveToWindow:]
+ -[PBUIPortalReplicaView _sourceViewIsOnDifferentScreenThan:]
+ -[PBUIPortalReplicaView allowsCrossDisplayPortalling]
+ -[PBUIPortalReplicaView pendingSourceReacquisitionAnimationSettings]
+ -[PBUIPortalReplicaView setPendingSourceReacquisitionAnimationSettings:]
+ -[PBUIPosterFloatingLayerReplica allowsCrossDisplayPortalling]
+ -[PBUIPosterFloatingView currentFloatingReplicas]
+ -[PBUIPosterHUDController _generateColumnContentForVariant:snapshot:snapshotDate:legibilityEnvironment:legibilityDate:readiness:]
+ -[PBUIPosterHUDController noteUpdatedScene:]
+ -[PBUIPosterHUDController updateVariant:snapshotReadiness:]
+ -[PBUIPosterHomeViewController _snapshotViewShouldBeHidden]
+ -[PBUIPosterHomeViewController _updateEffectViewSnapshotPresentation]
+ -[PBUIPosterHomeViewController activeSnapshotHoldReasons]
+ -[PBUIPosterHomeViewController fallbackImageKeyPresentationComponent]
+ -[PBUIPosterHomeViewController isCurrentlyShowingSnapshot]
+ -[PBUIPosterHomeViewController noteDidRotateToInterfaceOrientation:]
+ -[PBUIPosterHomeViewController noteHingeDidBecomeActive]
+ -[PBUIPosterHomeViewController noteHingeDidBecomeStable]
+ -[PBUIPosterHomeViewController requestSnapshotForHingeStableWithReason:]
+ -[PBUIPosterHomeViewController requestSnapshotForSignificantEventWithReason:]
+ -[PBUIPosterHomeViewController shouldSkipSnapshotForExistingFallbackWithReason:]
+ -[PBUIPosterHomeViewController snapshotAvailability]
+ -[PBUIPosterLockViewController _armSnapshotBackstopIfNeeded]
+ -[PBUIPosterLockViewController _fireSnapshotBackstop]
+ -[PBUIPosterLockViewController _frozenFloatingLayerSourceForScreen:]
+ -[PBUIPosterLockViewController _installSnapshotBackstopTimerForReason:]
+ -[PBUIPosterLockViewController _lockShouldSkipRedundantSnapshot]
+ -[PBUIPosterLockViewController _prepareFloatingLayerFadeForDisplayConfiguration:]
+ -[PBUIPosterLockViewController _reloadSourceForFloatingLayerReplicasOnScreen:]
+ -[PBUIPosterLockViewController _reloadSourceForFloatingLayerReplicasWithoutAnimation:]
+ -[PBUIPosterLockViewController _removeAllFrozenFloatingLayerSources]
+ -[PBUIPosterLockViewController _removeFrozenFloatingLayerSource:withAnimationFactory:]
+ -[PBUIPosterLockViewController _resetSnapshotBackstop]
+ -[PBUIPosterLockViewController _setPendingFloatingLayerFadeInSettings:]
+ -[PBUIPosterLockViewController _setupCachesIfNeeded]
+ -[PBUIPosterLockViewController _tearDownSnapshotBackstop]
+ -[PBUIPosterLockViewController dealloc]
+ -[PBUIPosterLockViewController didCompleteSuccessfulSnapshot:fallbackImageKey:fallbackStoreGeneration:]
+ -[PBUIPosterLockViewController displayConfigurationDidUpdate:]
+ -[PBUIPosterLockViewController displayConfigurationWillUpdate:]
+ -[PBUIPosterLockViewController freezeWallpaperFloatingLayerInContainerView:forReason:]
+ -[PBUIPosterLockViewController noteDidRotateToInterfaceOrientation:]
+ -[PBUIPosterLockViewController noteWillRotateToInterfaceOrientation:]
+ -[PBUIPosterLockViewController permitsForcedSnapshot]
+ -[PBUIPosterLockViewController requestSnapshotForHingeStableWithReason:]
+ -[PBUIPosterLockViewController requestSnapshotForSignificantEventWithReason:]
+ -[PBUIPosterSnapshotReadiness .cxx_destruct]
+ -[PBUIPosterSnapshotReadiness descriptionBuilderWithMultilinePrefix:]
+ -[PBUIPosterSnapshotReadiness descriptionWithMultilinePrefix:]
+ -[PBUIPosterSnapshotReadiness description]
+ -[PBUIPosterSnapshotReadiness isHingeActive]
+ -[PBUIPosterSnapshotReadiness isRotating]
+ -[PBUIPosterSnapshotReadiness isShowingSnapshot]
+ -[PBUIPosterSnapshotReadiness isSnapshotting]
+ -[PBUIPosterSnapshotReadiness needsSnapshot]
+ -[PBUIPosterSnapshotReadiness reasonsToNotSnapshot]
+ -[PBUIPosterSnapshotReadiness scheduled]
+ -[PBUIPosterSnapshotReadiness secondsUntilDeadline]
+ -[PBUIPosterSnapshotReadiness setIsHingeActive:]
+ -[PBUIPosterSnapshotReadiness setIsRotating:]
+ -[PBUIPosterSnapshotReadiness setIsShowingSnapshot:]
+ -[PBUIPosterSnapshotReadiness setIsSnapshotting:]
+ -[PBUIPosterSnapshotReadiness setNeedsSnapshot:]
+ -[PBUIPosterSnapshotReadiness setReasonsToNotSnapshot:]
+ -[PBUIPosterSnapshotReadiness setScheduled:]
+ -[PBUIPosterSnapshotReadiness setSecondsUntilDeadline:]
+ -[PBUIPosterSnapshotReadiness setSnapshotHoldReasons:]
+ -[PBUIPosterSnapshotReadiness setVariant:]
+ -[PBUIPosterSnapshotReadiness snapshotHoldReasons]
+ -[PBUIPosterSnapshotReadiness succinctDescriptionBuilder]
+ -[PBUIPosterSnapshotReadiness succinctDescription]
+ -[PBUIPosterSnapshotReadiness variant]
+ -[PBUIPosterVariantViewController _beginSignificantEventTransition]
+ -[PBUIPosterVariantViewController _countShufflePostersForPath:]
+ -[PBUIPosterVariantViewController _endSignificantEventTransition]
+ -[PBUIPosterVariantViewController _fallbackCacheManagerForInstanceURL:]
+ -[PBUIPosterVariantViewController _fallbackImageKey]
+ -[PBUIPosterVariantViewController _fireSnapshotWhenQuiescedForReason:]
+ -[PBUIPosterVariantViewController _invalidateFallbackSnapshotsForReason:]
+ -[PBUIPosterVariantViewController _isFallbackSnapshotSupportedForProvider:]
+ -[PBUIPosterVariantViewController _isFallbackSnapshotSupported]
+ -[PBUIPosterVariantViewController _mainQueue_scheduleSnapshotIfNeeded:]
+ -[PBUIPosterVariantViewController _markSnapshottingFinished]
+ -[PBUIPosterVariantViewController _populateFallbackSnapshotIfNeeded:key:storeGeneration:]
+ -[PBUIPosterVariantViewController _pruneFallbackSnapshotsOutsideSeedWindowOfKey:]
+ -[PBUIPosterVariantViewController _shouldConsultFallbackSkipForReason:]
+ -[PBUIPosterVariantViewController _snapshotReadiness]
+ -[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]
+ -[PBUIPosterVariantViewController _snapshotViewShouldBeHidden]
+ -[PBUIPosterVariantViewController _updateFallbackSubstitution]
+ -[PBUIPosterVariantViewController _updateSnapshotReadinessHUD]
+ -[PBUIPosterVariantViewController _updateSnapshotViewVisibility]
+ -[PBUIPosterVariantViewController activeSnapshotHoldReasons]
+ -[PBUIPosterVariantViewController addSnapshotSuppressionReason:]
+ -[PBUIPosterVariantViewController deleteCurrentSnapshot]
+ -[PBUIPosterVariantViewController didCompleteSuccessfulSnapshot:fallbackImageKey:fallbackStoreGeneration:]
+ -[PBUIPosterVariantViewController enqueueSnapshotForReason:]
+ -[PBUIPosterVariantViewController fallbackImageKeyPresentationComponent]
+ -[PBUIPosterVariantViewController hasFallbackSnapshot]
+ -[PBUIPosterVariantViewController hasValidSnapshotForCurrentGeometry]
+ -[PBUIPosterVariantViewController invalidateInFlightSnapshot]
+ -[PBUIPosterVariantViewController isCurrentlyShowingSnapshot]
+ -[PBUIPosterVariantViewController isRotating]
+ -[PBUIPosterVariantViewController isSnapshotSuppressed]
+ -[PBUIPosterVariantViewController noteHingeDidBecomeActive]
+ -[PBUIPosterVariantViewController noteHingeDidBecomeStable]
+ -[PBUIPosterVariantViewController permitsForcedSnapshot]
+ -[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:generation:completion:]
+ -[PBUIPosterVariantViewController removeSnapshotSuppressionReason:]
+ -[PBUIPosterVariantViewController requestSnapshotForHingeStableWithReason:]
+ -[PBUIPosterVariantViewController requestSnapshotForSignificantEventWithReason:]
+ -[PBUIPosterVariantViewController resolveSnapshotNeedWithoutCapturingForReason:]
+ -[PBUIPosterVariantViewController shouldSkipSnapshotForExistingFallbackWithReason:]
+ -[PBUIPosterVariantViewController snapshotAvailability]
+ -[PBUIPosterViewController _applyLifecycleToSettings:forScene:]
+ -[PBUIPosterViewController _endHingeMotionWindowForReason:]
+ -[PBUIPosterViewController _ensureHingeProgressProvider]
+ -[PBUIPosterViewController _fireHingeSettleWhenQuiesced]
+ -[PBUIPosterViewController _flushCoalescedSceneUpdates]
+ -[PBUIPosterViewController _handleSnapshotGatingHingeUpdate:]
+ -[PBUIPosterViewController _installSnapshotGatingHingeInteractionIfNeeded]
+ -[PBUIPosterViewController _lifecycleForScene:settings:]
+ -[PBUIPosterViewController _lifecycleWouldChangeForScene:]
+ -[PBUIPosterViewController _noteHingeMotion]
+ -[PBUIPosterViewController _queueCoalescedUpdateForReasons:updater:completion:]
+ -[PBUIPosterViewController _reArmSnapshotsForVariantsThatBecameEligible]
+ -[PBUIPosterViewController _reallyUpdatePosterScenesForReasons:updater:completion:]
+ -[PBUIPosterViewController _removeSnapshotGatingHingeInteraction]
+ -[PBUIPosterViewController _seedHingeMotionStateForRebuiltVariant:]
+ -[PBUIPosterViewController _snapshotEligibleForVariant:]
+ -[PBUIPosterViewController _updateVisibility]
+ -[PBUIPosterViewController _verdictForScene:sceneVariant:]
+ -[PBUIPosterViewController beginCoalescingSceneUpdatesForReason:]
+ -[PBUIPosterViewController freezeWallpaperFloatingLayerInContainerView:forReason:]
+ -[PBUIPosterViewController hasRequestedHingeStateEvents]
+ -[PBUIPosterViewController inExtendedRenderSession]
+ -[PBUIPosterViewController posterComponent:reasonToNotSnapshotForVariant:]
+ -[PBUIPosterViewController setInExtendedRenderSession:]
+ -[PBUIPosterViewController startSendingHingeProgressEvents]
+ -[PBUIPosterViewController stopSendingHingeProgressEvents]
+ -[PBUIPosterViewController viewDidDisappear:]
+ -[PBUIPosterViewController viewIsAppearing:]
+ -[PBUIPosterViewController viewWillAppear:]
+ -[PBUIPosterWallpaperRemoteViewController beginCoalescingSceneUpdatesForReason:]
+ -[PBUIPosterWallpaperRemoteViewController freezeWallpaperFloatingLayerInContainerView:forReason:]
+ -[PBUIPosterWallpaperRemoteViewController noteFencedUpdatesShouldBeSuppressed:]
+ -[PBUIPosterWallpaperRemoteViewController posterHasRequestedHingeStateEvents]
+ -[PBUIPosterWallpaperRemoteViewController startSendingHingeProgressEvents]
+ -[PBUIPosterWallpaperRemoteViewController stopSendingHingeProgressEvents]
+ -[PBUIPosterWallpaperViewController beginCoalescingSceneUpdatesForReason:]
+ -[PBUIPosterWallpaperViewController freezeWallpaperFloatingLayerInContainerView:forReason:]
+ -[PBUIPosterWallpaperViewController posterHasRequestedHingeStateEvents]
+ -[PBUIPosterWallpaperViewController startSendingHingeProgressEvents]
+ -[PBUIPosterWallpaperViewController stopSendingHingeProgressEvents]
+ -[PBUIPosterWallpaperViewController viewIsAppearing:]
+ -[PBUIReplicaSourceObserverBox hasObservers]
+ -[PBUISharedFenceBox .cxx_destruct]
+ -[PBUISharedFenceBox applyToContext:]
+ -[PBUISharedFenceBox dealloc]
+ -[PBUISharedFenceBox initWithWindowScene:animationDuration:]
+ -[PBUISharedFenceBox invalidate]
+ -[PBUISnapshotCancellationToken .cxx_destruct]
+ -[PBUISnapshotCancellationToken cancel]
+ -[PBUISnapshotCancellationToken currentGeneration]
+ -[PBUISnapshotCancellationToken init]
+ -[PBUIWallpaperPrototypeSettings floatingLayerDisplayTransferFadeInDuration]
+ -[PBUIWallpaperPrototypeSettings setFloatingLayerDisplayTransferFadeInDuration:]
+ -[PBUIWindowChangeInteraction .cxx_destruct]
+ -[PBUIWindowChangeInteraction _didMoveFromWindow:toWindow:]
+ -[PBUIWindowChangeInteraction didMoveToView:]
+ -[PBUIWindowChangeInteraction initWithWindowDidChangeHandler:]
+ -[PBUIWindowChangeInteraction view]
+ -[PBUIWindowChangeInteraction willMoveToView:]
+ -[UIWindowScene(PBUIFencedUpdates) pbui_setShouldSuppressFencedUpdates:]
+ -[UIWindowScene(PBUIFencedUpdates) pbui_shouldSuppressFencedUpdates]
+ -[UIWindowScene(PBUIHostInformedOrientation) pbui_hostInformedOrientation]
+ -[UIWindowScene(PBUIHostInformedOrientation) pbui_setHostInformedOrientation:]
+ -[_PBUIPendingSceneOperation .cxx_destruct]
+ -[_PBUIPendingSceneOperation block]
+ -[_PBUIPendingSceneOperation completion]
+ -[_PBUIPendingSceneOperation isActivate]
+ -[_PBUIPendingSceneOperation setBlock:]
+ -[_PBUIPendingSceneOperation setCompletion:]
+ -[_PBUIPendingSceneOperation setIsActivate:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table16
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table168
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table64
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table93
+ _BSFloatApproximatelyEqualToFloat
+ _CFRunLoopAddObserver
+ _CFRunLoopGetMain
+ _CFRunLoopObserverCreateWithHandler
+ _CFRunLoopRemoveObserver
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_BSBuildVersion
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_PBUICoalescingUpdateScheduler
+ _OBJC_CLASS_$_PBUIFrozenFloatingLayerPortalSource
+ _OBJC_CLASS_$_PBUIPosterSnapshotReadiness
+ _OBJC_CLASS_$_PBUISharedFenceBox
+ _OBJC_CLASS_$_PBUISnapshotCancellationToken
+ _OBJC_CLASS_$_PBUIWindowChangeInteraction
+ _OBJC_CLASS_$_UIHingeInteraction
+ _OBJC_CLASS_$__PBUIPendingSceneOperation
+ _OBJC_IVAR_$_PBUICachedSnapshotEffectProvider._fallbackImage
+ _OBJC_IVAR_$_PBUICachedSnapshotEffectProvider._fallbackImageKey
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._coalescesEveryRunLoopTurn
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._flushDepth
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._flushHandler
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._flushPending
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._hasFlushedImmediatelyThisTurn
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._identifier
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._isFlushing
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._runLoopObserver
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._turnBoundaryObserver
+ _OBJC_IVAR_$_PBUICoalescingUpdateScheduler._windowAssertion
+ _OBJC_IVAR_$_PBUIEffectTrackingReplicaView._lastLoggedShowSnapshot
+ _OBJC_IVAR_$_PBUIFakeBlurView._lastRequestedInterfaceOrientation
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._currentUsers
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._frozenView
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._invalidated
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._legibilitySettings
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._reason
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._screen
+ _OBJC_IVAR_$_PBUIFrozenFloatingLayerPortalSource._wrapperView
+ _OBJC_IVAR_$_PBUIPortalReplicaView._pendingSourceReacquisitionAnimationSettings
+ _OBJC_IVAR_$_PBUIPortalReplicaView._sourceWindowChangeInteraction
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeSnapshotReadiness
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockSnapshotReadiness
+ _OBJC_IVAR_$_PBUIPosterLockViewController._frozenFloatingLayerSources
+ _OBJC_IVAR_$_PBUIPosterLockViewController._lastKnownDisplayConfiguration
+ _OBJC_IVAR_$_PBUIPosterLockViewController._snapshotBackstopTimer
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._isHingeActive
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._isRotating
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._isShowingSnapshot
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._isSnapshotting
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._needsSnapshot
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._reasonsToNotSnapshot
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._scheduled
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._secondsUntilDeadline
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._snapshotHoldReasons
+ _OBJC_IVAR_$_PBUIPosterSnapshotReadiness._variant
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._displayedSignificantEvent
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._fallbackCache
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._fallbackCacheManager
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._fallbackImageKeys
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._fallbackStoreGeneration
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._hasObservedSignificantEvent
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._isHingeActive
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._numberOfShufflePosters
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._rotationGeneration
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._significantEventSuppressionGeneration
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._significantEventSuppressionInstalled
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotCancellationToken
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotDeadline
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotRequestedDuringCapture
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._snapshotSuppressionReasons
+ _OBJC_IVAR_$_PBUIPosterViewController._coalescingScheduler
+ _OBJC_IVAR_$_PBUIPosterViewController._hasLastHinge
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeActiveAssertion
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeAngleIsLive
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeInMotion
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeMotionSignpostID
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeMotionStartTime
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeProgressController
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeReferenceAngle
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeSettleDeadline
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeUpdatesAcceptedSinceMotionStart
+ _OBJC_IVAR_$_PBUIPosterViewController._hingeUpdatesDeliveredSinceMotionStart
+ _OBJC_IVAR_$_PBUIPosterViewController._homeSnapshotEligible
+ _OBJC_IVAR_$_PBUIPosterViewController._inExtendedRenderSession
+ _OBJC_IVAR_$_PBUIPosterViewController._lastHingeStatus
+ _OBJC_IVAR_$_PBUIPosterViewController._lockSnapshotEligible
+ _OBJC_IVAR_$_PBUIPosterViewController._pendingCoalescedCompletions
+ _OBJC_IVAR_$_PBUIPosterViewController._pendingCoalescedReasons
+ _OBJC_IVAR_$_PBUIPosterViewController._pendingCoalescedUpdaters
+ _OBJC_IVAR_$_PBUIPosterViewController._snapshotGatingHingeInteraction
+ _OBJC_IVAR_$_PBUIPosterViewController._wallpaperIsIdle
+ _OBJC_IVAR_$_PBUIPosterViewController._wallpaperObscured
+ _OBJC_IVAR_$_PBUISharedFenceBox._animationDuration
+ _OBJC_IVAR_$_PBUISharedFenceBox._fenceHandle
+ _OBJC_IVAR_$_PBUISharedFenceBox._windowScene
+ _OBJC_IVAR_$_PBUISnapshotCancellationToken._generationLock
+ _OBJC_IVAR_$_PBUIWallpaperPrototypeSettings._floatingLayerDisplayTransferFadeInDuration
+ _OBJC_IVAR_$_PBUIWindowChangeInteraction._view
+ _OBJC_IVAR_$_PBUIWindowChangeInteraction._windowDidChangeHandler
+ _OBJC_IVAR_$__PBUIPendingSceneOperation._block
+ _OBJC_IVAR_$__PBUIPendingSceneOperation._completion
+ _OBJC_IVAR_$__PBUIPendingSceneOperation._isActivate
+ _OBJC_METACLASS_$_PBUICoalescingUpdateScheduler
+ _OBJC_METACLASS_$_PBUIFrozenFloatingLayerPortalSource
+ _OBJC_METACLASS_$_PBUIPosterSnapshotReadiness
+ _OBJC_METACLASS_$_PBUISharedFenceBox
+ _OBJC_METACLASS_$_PBUISnapshotCancellationToken
+ _OBJC_METACLASS_$_PBUIWindowChangeInteraction
+ _OBJC_METACLASS_$__PBUIPendingSceneOperation
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _PBUIDebugCheckerboardColorWithColors
+ _PBUIDebugFallbackReasonMarker
+ _PBUIDebugFallbackSnapshotCheckerboardColor
+ _PBUIDebugFallbackSnapshotCheckerboardColor.color
+ _PBUIDebugFallbackSnapshotCheckerboardColor.onceToken
+ _PBUIFallbackSnapshotCacheEpochPrefix
+ _PBUIFallbackSnapshotCacheEpochPrefix.epochPrefix
+ _PBUIFallbackSnapshotCacheEpochPrefix.onceToken
+ _PBUIFallbackSnapshotSeedInKey
+ _PBUIFallbackSnapshotSupportedProviderBundleIdentifiers.onceToken
+ _PBUIFallbackSnapshotSupportedProviderBundleIdentifiers.supportedProviderBundleIdentifiers
+ _PBUIHomeEffectViewFallbackReason.fallbackReason
+ _PBUIHomeEffectViewFallbackReason.onceToken
+ _PBUILogSignpost
+ _PBUILogSignpost.__logObj
+ _PBUILogSignpost.onceToken
+ _PBUILogStatus
+ _PBUILogStatus.__logObj
+ _PBUILogStatus.onceToken
+ _PBUIPosterSnapshotSuppressionReasonSignificantEvent
+ _PBUISnapshotCancelledError
+ _PBUISnapshotCancelledError.cancelledError
+ _PBUISnapshotCancelledError.onceToken
+ _PBUISupportsDynamicRotation
+ __OBJC_$_CATEGORY_UIWindowScene_$_PBUIFencedUpdates
+ __OBJC_$_CLASS_METHODS__PBUIPendingSceneOperation
+ __OBJC_$_INSTANCE_METHODS_PBUICoalescingUpdateScheduler
+ __OBJC_$_INSTANCE_METHODS_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_$_INSTANCE_METHODS_PBUIPosterSnapshotReadiness
+ __OBJC_$_INSTANCE_METHODS_PBUISharedFenceBox
+ __OBJC_$_INSTANCE_METHODS_PBUISnapshotCancellationToken
+ __OBJC_$_INSTANCE_METHODS_PBUIWindowChangeInteraction
+ __OBJC_$_INSTANCE_METHODS_UIWindowScene(PBUIFencedUpdates|PBUIHostInformedOrientation)
+ __OBJC_$_INSTANCE_METHODS__PBUIPendingSceneOperation
+ __OBJC_$_INSTANCE_VARIABLES_PBUICoalescingUpdateScheduler
+ __OBJC_$_INSTANCE_VARIABLES_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_$_INSTANCE_VARIABLES_PBUIPosterSnapshotReadiness
+ __OBJC_$_INSTANCE_VARIABLES_PBUISharedFenceBox
+ __OBJC_$_INSTANCE_VARIABLES_PBUISnapshotCancellationToken
+ __OBJC_$_INSTANCE_VARIABLES_PBUIWindowChangeInteraction
+ __OBJC_$_INSTANCE_VARIABLES__PBUIPendingSceneOperation
+ __OBJC_$_PROP_LIST_FBScene_$_PaperBoard
+ __OBJC_$_PROP_LIST_PBUICoalescingUpdateScheduler
+ __OBJC_$_PROP_LIST_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_$_PROP_LIST_PBUIPosterSnapshotReadiness
+ __OBJC_$_PROP_LIST_PBUIWindowChangeInteraction
+ __OBJC_$_PROP_LIST_UIInteraction
+ __OBJC_$_PROP_LIST_UIInteraction_Private
+ __OBJC_$_PROP_LIST__PBUIPendingSceneOperation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PBUIPosterComponentDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIInteraction_Private
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIInteraction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIInteraction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIInteraction_Private
+ __OBJC_$_PROTOCOL_REFS_UIInteraction
+ __OBJC_$_PROTOCOL_REFS_UIInteraction_Private
+ __OBJC_CLASS_PROTOCOLS_$_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_CLASS_PROTOCOLS_$_PBUIPosterSnapshotReadiness
+ __OBJC_CLASS_PROTOCOLS_$_PBUIWindowChangeInteraction
+ __OBJC_CLASS_RO_$_PBUICoalescingUpdateScheduler
+ __OBJC_CLASS_RO_$_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_CLASS_RO_$_PBUIPosterSnapshotReadiness
+ __OBJC_CLASS_RO_$_PBUISharedFenceBox
+ __OBJC_CLASS_RO_$_PBUISnapshotCancellationToken
+ __OBJC_CLASS_RO_$_PBUIWindowChangeInteraction
+ __OBJC_CLASS_RO_$__PBUIPendingSceneOperation
+ __OBJC_LABEL_PROTOCOL_$_UIInteraction
+ __OBJC_LABEL_PROTOCOL_$_UIInteraction_Private
+ __OBJC_METACLASS_RO_$_PBUICoalescingUpdateScheduler
+ __OBJC_METACLASS_RO_$_PBUIFrozenFloatingLayerPortalSource
+ __OBJC_METACLASS_RO_$_PBUIPosterSnapshotReadiness
+ __OBJC_METACLASS_RO_$_PBUISharedFenceBox
+ __OBJC_METACLASS_RO_$_PBUISnapshotCancellationToken
+ __OBJC_METACLASS_RO_$_PBUIWindowChangeInteraction
+ __OBJC_METACLASS_RO_$__PBUIPendingSceneOperation
+ __OBJC_PROTOCOL_$_UIInteraction
+ __OBJC_PROTOCOL_$_UIInteraction_Private
+ ___113-[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]_block_invoke
+ ___113-[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]_block_invoke_2
+ ___113-[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]_block_invoke_3
+ ___113-[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]_block_invoke_4
+ ___113-[PBUIPosterVariantViewController _snapshotScene:generation:fallbackImageKey:fallbackStoreGeneration:completion:]_block_invoke_5
+ ___122-[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:generation:completion:]_block_invoke
+ ___122-[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:generation:completion:]_block_invoke_2
+ ___39-[PBUISnapshotCancellationToken cancel]_block_invoke
+ ___46-[PBUIPortalReplicaView _setPortalSourceView:]_block_invoke
+ ___46-[PBUIPortalReplicaView _setPortalSourceView:]_block_invoke_2
+ ___51-[PBUISnapshotReplicaView _updateImageViewRotation]_block_invoke
+ ___52-[PBUIPortalReplicaView _sourceViewDidMoveToWindow:]_block_invoke
+ ___55-[FBScene(PaperBoard) _pb_reallyUpdate:withCompletion:]_block_invoke
+ ___55-[FBScene(PaperBoard) _pb_reallyUpdate:withCompletion:]_block_invoke_2
+ ___55-[FBScene(PaperBoard) pb_flushCoalescedUpdatesIfNeeded]_block_invoke
+ ___55-[FBScene(PaperBoard) pb_flushCoalescedUpdatesIfNeeded]_block_invoke_2
+ ___55-[PBUIPosterViewController _flushCoalescedSceneUpdates]_block_invoke
+ ___55-[PBUIPosterViewController _flushCoalescedSceneUpdates]_block_invoke_2
+ ___55-[PBUIPosterViewController setSalientContentRectangle:]_block_invoke
+ ___56-[PBUIPosterViewController _fireHingeSettleWhenQuiesced]_block_invoke
+ ___60-[PBUIPosterVariantViewController enqueueSnapshotForReason:]_block_invoke
+ ___62-[PBUICoalescingUpdateScheduler _scheduleRunLoopFlushIfNeeded]_block_invoke
+ ___65-[PBUICoalescingUpdateScheduler initWithIdentifier:flushHandler:]_block_invoke
+ ___67-[PBUIPosterVariantViewController _beginSignificantEventTransition]_block_invoke
+ ___69-[PBUIPosterSnapshotReadiness descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___70-[PBUIPosterVariantViewController _fireSnapshotWhenQuiescedForReason:]_block_invoke
+ ___71-[PBUIPosterLockViewController _installSnapshotBackstopTimerForReason:]_block_invoke
+ ___72-[PBUIPosterVariantViewController noteWillRotateToInterfaceOrientation:]_block_invoke
+ ___74-[PBUIPosterViewController _installSnapshotGatingHingeInteractionIfNeeded]_block_invoke
+ ___79-[PBUIPosterWallpaperRemoteViewController noteFencedUpdatesShouldBeSuppressed:]_block_invoke
+ ___83-[PBUIPosterViewController _reallyUpdatePosterScenesForReasons:updater:completion:]_block_invoke
+ ___83-[PBUIPosterViewController _reallyUpdatePosterScenesForReasons:updater:completion:]_block_invoke_2
+ ___86-[PBUIPosterLockViewController freezeWallpaperFloatingLayerInContainerView:forReason:]_block_invoke
+ ___86-[PBUIPosterWallpaperViewController posterComponent:didUpdateInExtendedRenderSession:]_block_invoke
+ ___PBUIDebugFallbackSnapshotCheckerboardColor_block_invoke
+ ___PBUIFallbackSnapshotCacheEpochPrefix_block_invoke
+ ___PBUIFallbackSnapshotSupportedProviderBundleIdentifiers_block_invoke
+ ___PBUIHomeEffectViewFallbackReason_block_invoke
+ ___PBUILogSignpost_block_invoke
+ ___PBUILogStatus_block_invoke
+ ___PBUISnapshotCancelledError_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s96l8s80l8s88l8
+ ___block_descriptor_139_e8_32s40s48s56s64bs_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24ls32l8
+ ___block_descriptor_40_e8_32w_e18_v16?0"UIWindow"8lw32l8
+ ___block_descriptor_40_e8_32w_e33_v24?0^{__CFRunLoopObserver=}8Q16lw32l8
+ ___block_descriptor_40_e8_32w_e57_v24?0"UIHingeInteraction"8"UIHingeInteractionUpdate"16lw32l8
+ ___block_descriptor_48_e8_32s40w_e36_v16?0"<BSCompoundAssertionState>"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e52_v24?0"BSSimpleAssertion"8"BSUIAnimationFactory"16lw40l8s32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32s40s48w_e18_"UIImage"16?0^Q8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
+ ___block_descriptor_56_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_64_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
+ ___block_descriptor_72_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s_e40_v16?0"PBUISnapshotPreconditionResult"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40bs48w_e130_v56?0"PUIPosterSnapshotBundle"8"PUIPosterSnapshotDestination"16"UIImage"24"PUIColorStatistics"32"NSDictionary"40"NSError"48lw48l8s40l8s32l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___getPFContextSupportsDynamicRotationSymbolLoc_block_invoke
+ ___getPFCurrentDeviceClassSymbolLoc_block_invoke
+ ___getPFOSUnfairLockClass_block_invoke
+ ___getPFPathProviderClass_block_invoke
+ ___getPRDisplayTypeFromFBSDisplayConfigurationSymbolLoc_block_invoke
+ ___getPRUISHingeProgressControllerClass_block_invoke
+ ___getPRUISHingeProgressProviderClass_block_invoke
+ ___getPUIWindowSceneHostInformedOrientationSymbolLoc_block_invoke
+ ___getPUIWindowSceneSetHostInformedOrientationSymbolLoc_block_invoke
+ ___getPUIWindowSceneSetShouldSuppressFencedUpdatesSymbolLoc_block_invoke
+ ___getPUIWindowSceneShouldSuppressFencedUpdatesSymbolLoc_block_invoke
+ _getPFContextSupportsDynamicRotationSymbolLoc
+ _getPFContextSupportsDynamicRotationSymbolLoc.ptr
+ _getPFCurrentDeviceClassSymbolLoc
+ _getPFCurrentDeviceClassSymbolLoc.ptr
+ _getPFOSUnfairLockClass
+ _getPFOSUnfairLockClass.softClass
+ _getPFPathProviderClass
+ _getPFPathProviderClass.softClass
+ _getPRDisplayTypeFromFBSDisplayConfigurationSymbolLoc
+ _getPRDisplayTypeFromFBSDisplayConfigurationSymbolLoc.ptr
+ _getPRUISHingeProgressControllerClass
+ _getPRUISHingeProgressControllerClass.softClass
+ _getPRUISHingeProgressProviderClass
+ _getPRUISHingeProgressProviderClass.softClass
+ _getPUIWindowSceneHostInformedOrientationSymbolLoc
+ _getPUIWindowSceneHostInformedOrientationSymbolLoc.ptr
+ _getPUIWindowSceneSetHostInformedOrientationSymbolLoc
+ _getPUIWindowSceneSetHostInformedOrientationSymbolLoc.ptr
+ _getPUIWindowSceneSetShouldSuppressFencedUpdatesSymbolLoc
+ _getPUIWindowSceneSetShouldSuppressFencedUpdatesSymbolLoc.ptr
+ _getPUIWindowSceneShouldSuppressFencedUpdatesSymbolLoc
+ _getPUIWindowSceneShouldSuppressFencedUpdatesSymbolLoc.ptr
+ _kCFRunLoopCommonModes
+ _kPBSceneCoalescingSchedulerAssociationKey
+ _kPBScenePendingOperationsAssociationKey
+ _objc_getAssociatedObject
+ _objc_setAssociatedObject
+ _soft_PFContextSupportsDynamicRotation
+ _soft_PFCurrentDeviceClass
+ _soft_PRDisplayTypeFromFBSDisplayConfiguration
+ _soft_PUIWindowSceneHostInformedOrientation
+ _soft_PUIWindowSceneSetHostInformedOrientation
+ _soft_PUIWindowSceneSetShouldSuppressFencedUpdates
+ _soft_PUIWindowSceneShouldSuppressFencedUpdates
- -[PBUIPosterHUDController _generateColumnContentForVariant:snapshot:snapshotDate:legibilityEnvironment:legibilityDate:]
- -[PBUIPosterVariantViewController _snapshotScene:completion:]
- -[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:completion:]
- -[PBUIPosterViewController startSendingDisplayStateProgressEvents]
- -[PBUIPosterViewController stopSendingDisplayStateProgressEvents]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table110
- GCC_except_table113
- GCC_except_table115
- GCC_except_table116
- GCC_except_table122
- GCC_except_table124
- GCC_except_table127
- GCC_except_table131
- GCC_except_table134
- GCC_except_table140
- GCC_except_table142
- GCC_except_table144
- GCC_except_table148
- GCC_except_table151
- GCC_except_table167
- GCC_except_table169
- GCC_except_table173
- GCC_except_table36
- GCC_except_table38
- GCC_except_table41
- GCC_except_table43
- GCC_except_table66
- GCC_except_table80
- GCC_except_table84
- GCC_except_table89
- GCC_except_table92
- GCC_except_table95
- _OBJC_IVAR_$_PBUIPosterViewController._displayStateProgressController
- _OBJC_IVAR_$_PBUIPosterWallpaperViewController._extendedRenderSessionKeepActiveReason
- ___111-[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:completion:]_block_invoke
- ___111-[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:completion:]_block_invoke_2
- ___47-[PBUIPosterViewController setWallpaperIsIdle:]_block_invoke
- ___48-[FBScene(PaperBoard) pb_update:withCompletion:]_block_invoke
- ___48-[FBScene(PaperBoard) pb_update:withCompletion:]_block_invoke_2
- ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke_3
- ___49-[PBUIPosterViewController setWallpaperObscured:]_block_invoke
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_2
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_3
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_4
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_5
- ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke
- ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke_2
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
- ___block_descriptor_141_e8_32s40s48bs_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24ls32l8s40l8s48l8
- ___block_descriptor_33_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
- ___block_descriptor_48_e8_32s40w_e18_"UIImage"16?0^Q8lw40l8s32l8
- ___block_descriptor_48_e8_32s_e40_v16?0"PBUISnapshotPreconditionResult"8ls32l8
- ___block_descriptor_56_e8_32bs40w_e130_v56?0"PUIPosterSnapshotBundle"8"PUIPosterSnapshotDestination"16"UIImage"24"PUIColorStatistics"32"NSDictionary"40"NSError"48lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s64l8s56l8
- ___getPRUISDisplayStateProgressControllerClass_block_invoke
- ___getPUIDynamicRotationIsActiveSymbolLoc_block_invoke
- _getPRUISDisplayStateProgressControllerClass
- _getPRUISDisplayStateProgressControllerClass.softClass
- _getPUIDynamicRotationIsActiveSymbolLoc
- _getPUIDynamicRotationIsActiveSymbolLoc.ptr
- _soft_PUIDynamicRotationIsActive
CStrings:
+ "\n"
+ " (fence suppressed by host)"
+ " (inactive scene)"
+ " (no transition context)"
+ " (no window scene)"
+ " (not requested)"
+ " (not visible)"
+ " (nothing changed)"
+ " (obscured)"
+ "%.0fx%.0f"
+ "%@"
+ "%@ %@"
+ "%@-%@"
+ "%@-%@-%@-di%ld-io%ld"
+ "(fallback)"
+ "(nil)"
+ "(unnamed)"
+ "-%@"
+ "-se"
+ "-se%lu-mc%lu"
+ "-st%ld"
+ "2"
+ "<%{public}@:%p> _updatePosterScenesForReasons: updating displayConfig for scene %{public}@"
+ "<%{public}@:%p> invalidate: flushing any pending coalesced updates before scene teardown"
+ "<%{public}@:%p> viewDidMoveToWindow: displayConfigMismatch=%{BOOL}u (scene=%{public}@ view=%{public}@)"
+ "<%{public}@:%p> viewDidMoveToWindow: general"
+ "A visibility input moved but no scene lifecycle value changed; skipping the scene update."
+ "Applying fence %{public}@ (windowScene=%{public}@)"
+ "A\xf0\xf0Q"
+ "BOOL soft_PFContextSupportsDynamicRotation(__strong PFPosterRole, __strong PFDisplayType, PFDeviceClass)"
+ "BOOL soft_PUIWindowSceneShouldSuppressFencedUpdates(UIWindowScene *__strong)"
+ "CLEAR_ALL notification"
+ "CachedSnapshot-Fallback-%@-%@"
+ "Class getPFOSUnfairLockClass(void)_block_invoke"
+ "Class getPFPathProviderClass(void)_block_invoke"
+ "Class getPRUISHingeProgressControllerClass(void)_block_invoke"
+ "Class getPRUISHingeProgressProviderClass(void)_block_invoke"
+ "Coalesced scene update still pending (%@)"
+ "Configuration re-pushed with identical content for %{public}@ (%{public}s); no content fence"
+ "Could not compare configuration content for %{public}@ (%{public}s); treating as changed"
+ "Could not obtain a model object cache for the incoming poster path; treating content as changed."
+ "Could not read the home screen configuration for the incoming poster path: %{public}@. Treating content as changed."
+ "DisplayChange"
+ "Enabling %@ as a cross-display portal because source view is on a different screen."
+ "FallbackSnapshots"
+ "Fenced update requested but suppressed (windowScene=%{public}@)"
+ "Floating Layer Fade In (0 = off)"
+ "Flooring UIInterfaceOrientationUnknown to Portrait to avoid AlwaysAll scene-update fault (rdar://178665054)"
+ "Flushing coalesced scene update for reasons: %{public}@ (%lu queued updaters, %lu queued completions)"
+ "Fold Display Transfer"
+ "FrozenFloatingLayerReplicas"
+ "Hi; bestWallpaperSizeForParallaxFactor: is an old API, please move to bestWallpaperSizeForParallaxFactor:isPortrait: - this class is really not supported by modern infrastructure (Posters vs WooP)"
+ "HingeMotion"
+ "Home screen configuration changed behind identical poster content for %{public}@ (%{public}s)"
+ "In extended render session was updated: %{BOOL}u"
+ "LIVE portal"
+ "PBUIPortalReplicaView: Fading in floating layer over %.3fs to alpha %.2f (%{public}@)"
+ "PBUIPosterDisplaySwitchInTransaction"
+ "PBUIPosterSnapshotHoldReasonDisplayConfigurationTransition"
+ "PBUIPosterSnapshotHoldReasonHinge"
+ "PBUIPosterSnapshotHoldReasonRotation"
+ "PBUIPosterViewController scene updates"
+ "PBUISnapshotCancellation"
+ "PFContextSupportsDynamicRotation"
+ "PFCurrentDeviceClass"
+ "PFDeviceClass soft_PFCurrentDeviceClass(void)"
+ "PFOSUnfairLock"
+ "PFPathProvider"
+ "PRDisplayType soft_PRDisplayTypeFromFBSDisplayConfiguration(FBSDisplayConfiguration * _Nullable __strong)"
+ "PRDisplayTypeFromFBSDisplayConfiguration"
+ "PRUISHingeProgressController"
+ "PRUISHingeProgressProvider"
+ "PUIWindowSceneHostInformedOrientation"
+ "PUIWindowSceneSetHostInformedOrientation"
+ "PUIWindowSceneSetShouldSuppressFencedUpdates"
+ "PUIWindowSceneShouldSuppressFencedUpdates"
+ "Poster hinge is in motion"
+ "Poster scene state site=posterVC scene=%{public}s variant=%{public}@ visible=%{BOOL}u onScreen=%{BOOL}u displayConfig=%{public}@->%{public}@ txDisplaySwitch=%{public}@ interfaceOrientation=%ld->%ld deviceOrientation=%ld->%ld activityMode=%{public}@->%{public}@ jetsamMode=%ld->%ld obscured=%{BOOL}u->%{BOOL}u idle=%{BOOL}u->%{BOOL}u"
+ "Poster scenes FENCED update for reasons: %{public}@ site=posterVC scene=%{public}s variant=%{public}@ hinge=%{BOOL}u"
+ "Poster scenes FENCED update for reasons: HomeRotation site=homeVC scene=home interfaceOrientation=%ld deviceOrientation=%ld contextNil=%{BOOL}u"
+ "Poster scenes fence JOINED site=variantVC variant=%{public}@ handle=%{public}@"
+ "Poster scenes un-fenced update for reasons: %{public}@%{public}s site=posterVC scene=%{public}s variant=%{public}@ hinge=%{BOOL}u sceneObscured=%{BOOL}u activelyRequired=%{BOOL}u"
+ "PosterContentChange"
+ "Queuing coalesced update for reasons: %{public}@ (had updater: %{BOOL}d, had completion: %{BOOL}d) -- %lu updaters queued so far"
+ "Replacing lock poster scene %{public}@ -- flushing any pending coalesced updates first"
+ "SNAPSHOT"
+ "SignificantEvent"
+ "Signpost"
+ "Snapshot cancelled before it was persisted"
+ "Status"
+ "Tearing down home poster scene %{public}@ -- flushing any pending coalesced updates first"
+ "UIInterfaceOrientation soft_PUIWindowSceneHostInformedOrientation(UIWindowScene *__strong)"
+ "Updating activity mode for scene %@/%{public}@ to %{public}@"
+ "UserInterfaceStyleUpdate"
+ "V%ld-OS%@"
+ "Variant %@ is not the active variant (%@)"
+ "VisibilityUpdate"
+ "Wallpaper idle was updated: %{BOOL}u"
+ "Wallpaper is not on screen (variant %@, onScreen %@, obscured %@)"
+ "Wallpaper obscured was updated: %{BOOL}u"
+ "[%{public}@] Coalescing window closed; flushing now"
+ "[%{public}@] Coalescing window open; noted update pending, deferring flush"
+ "[%{public}@] DISCARDING snapshot AFTER WRITE (fallback not seeded): captureGeneration=%lu currentGeneration=%lu"
+ "[%{public}@] DISCARDING snapshot BEFORE WRITE: captureGeneration=%lu currentGeneration=%lu"
+ "[%{public}@] Flushing %lu coalesced pb_activate:/pb_update: calls (anyActivate=%{BOOL}d, %lu had blocks, %lu had completions)"
+ "[%{public}@] Immediate flush requested -- honoring (first this run loop turn)"
+ "[%{public}@] Immediate flush requested but NOT honored -- already flushed immediately once this run loop turn; queuing normally instead."
+ "[%{public}@] Immediate flush requested while already flushing -- queuing normally instead."
+ "[%{public}@] No coalescing window open; flushing immediately"
+ "[%{public}@] Queuing coalesced %{public}s call -- %lu operations queued so far"
+ "[%{public}@] Run loop turn ending; flushing now"
+ "[%{public}@] Scheduling flush for end of this run loop turn"
+ "[%{public}@] Snapshot already scheduled; extended quiesce deadline for reason: %{public}@"
+ "[%{public}@] _rotateToPathProvider: instanceURLChanged=%d, hardwareIdentifierChanged=%d"
+ "[%{public}@] _setupCachesIfNeeded: fallbackCacheIdentifier CHANGED: old=%{public}@ new=%{public}@ fallbackStoreGenerationBefore=%lu provider=%{public}@ isServerPosterPath=%{BOOL}d"
+ "[%{public}@] _setupCachesIfNeeded: fallbackStoreGenerationAfter=%lu"
+ "[%{public}@] downgrading forced snapshot to a schedule (variant does not permit force) reason: %{public}@"
+ "[%{public}@] fallback cache checked out: %{public}@ provider=%{public}@ (shufflePosters=%{public}@ knownKeys=%lu)"
+ "[%{public}@] fallback seed: displayed=%lu pending=%lu src=%{public}s posters=%lu"
+ "[%{public}@] fallback snapshot MISSING for key %{public}@; dropping"
+ "[%{public}@] fallback snapshot POPULATED for key %{public}@ wroteSize=%@ mappedBackSize=%@"
+ "[%{public}@] fallback snapshot write FAILED for key %{public}@ (wrote size %@)"
+ "[%{public}@] fallback snapshots INVALIDATED (%{public}@); dropping %lu key(s)"
+ "[%{public}@] fallback substitution: snapshotBit=%{BOOL}d fallbackBit=%{BOOL}d mapped=%{BOOL}d mappedOrientation=%ld rawMappedSize=%@ finalSize=%@ currentKey=%{public}@"
+ "[%{public}@] hasValidSnapshotForCurrentGeometry=NO hardwareIdentifier=%{public}@ current(device=%ld,interface=%ld) snapshot(device=%ld,interface=%ld)"
+ "[%{public}@] in-flight snapshot INVALIDATED"
+ "[%{public}@] not populating fallback while suppressed: %{public}@"
+ "[%{public}@] not populating fallback: capture produced no image for key %{public}@"
+ "[%{public}@] not populating fallback: fallbackImageKey is already tracked: %{public}@"
+ "[%{public}@] not populating fallback: fallbackImageKey was nil"
+ "[%{public}@] not populating fallback: snapshot geometry no longer matches key %{public}@"
+ "[%{public}@] not populating fallback: store was invalidated since capture kicked off for key %{public}@"
+ "[%{public}@] pb_activate: requiresImmediateFlush=%{BOOL}u"
+ "[%{public}@] pb_update: requiresImmediateFlush=%{BOOL}u"
+ "[%{public}@] pruning fallback outside the seed window: %{public}@"
+ "[%{public}@] re-driving snapshot: a request arrived during the previous capture"
+ "[%{public}@] rotation window never closed; clearing after 5s"
+ "[%{public}@] seeding hinge-active state into a variant rebuilt mid-fold"
+ "[%{public}@] significant event OBSERVED %lu -> %lu"
+ "[%{public}@] significant event never acknowledged; lifting after 5s"
+ "[%{public}@] snapshot SUPPRESSED (+%{public}@) reasons=%{public}@ cancelledInFlight=%{BOOL}d"
+ "[%{public}@] snapshot capture DECLINED (variant is serving a stored image) for reason: %{public}@"
+ "[%{public}@] snapshot capture KICKED OFF (force=%{BOOL}d) for reason: %{public}@"
+ "[%{public}@] snapshot debounce fired (quiesced) for reason: %{public}@"
+ "[%{public}@] snapshot suppression LIFTED (-%{public}@) reasons=%{public}@ wantOutstanding=%{BOOL}d"
+ "[%{public}@] snapshot-cadence: ENQUEUE reason: %{public}@"
+ "[%{public}@] snapshot-cadence: NOT rescheduling, not the active variant (reason: %{public}@)"
+ "[%{public}@] snapshot-cadence: RESOLVED WITHOUT CAPTURE reason: %{public}@"
+ "[%{public}@] snapshot-cadence: SCHEDULE reason: %{public}@"
+ "[%{public}@] snapshotView visibility: self=%p hidden=%{BOOL}d snapshotViewNil=%{BOOL}d sceneViewHidden=%{BOOL}d contentContainerHidden=%{BOOL}d"
+ "[%{public}@] unable to create fallback snapshot directory: %{public}@"
+ "[effect: %{public}@] now showing %{public}s (showsSnapshot=%{BOOL}d snapshotReady=%{BOOL}d)"
+ "[floatingLayer] cancelled any pending floating layer fade in"
+ "[floatingLayer] the next source change will fade the floating layer in over %.2f seconds"
+ "[frozenFloatingLayer] cannot freeze the floating layer for %{public}@ because the container view is not in a window"
+ "[frozenFloatingLayer] cannot freeze the floating layer for %{public}@ because the poster layers are not set up yet"
+ "[frozenFloatingLayer] froze the floating layer %{public}@"
+ "[frozenFloatingLayer] not freezing the floating layer for %{public}@ because this poster has none on this screen"
+ "[frozenFloatingLayer] removing the frozen floating layer %{public}@, moving %lu replica(s) back to the live floating layer"
+ "[home] configureEffectViewForMode: setShowsSnapshot=%{BOOL}d blurred=%{BOOL}d effectStyle=%{public}@ mode=%ld snapshotSourceValid=%{BOOL}d needsSnapshot=%{BOOL}d isSnapshotting=%{BOOL}d servingFallback=%{BOOL}d"
+ "[home] noteHingeDidBecomeActive: added 'hinge', holdReasons=%@, canShowSnapshot=%{BOOL}d"
+ "[home] noteHingeDidBecomeStable: removed 'hinge', holdReasons=%@"
+ "[home] skipping snapshot; already storing a fallback for the current geometry (reason: %{public}@)"
+ "[lock] hinge stable: skipping snapshot; nothing wanted and already have a valid snapshot for current geometry (reason: %{public}@)"
+ "[lock] snapshot backstop FIRED; requesting snapshot"
+ "[lock] snapshot backstop armed: fires in %.0fs (%{public}@; %{public}s)"
+ "[lock] snapshot backstop fired; nothing wanted and already have a valid snapshot for current geometry, skipping"
+ "[snapshot] _updateImageViewRotation: self=%p reason=%{public}@ orientation=%ld radians=%f windowScene=%@"
+ "_updatePosterScenesForReasons: reasons=%{public}@ requiresImmediateFlush=%{BOOL}u"
+ "accepted=%lu delivered=%lu reason=%{public}s"
+ "com.apple.EmojiPoster.EmojiPosterExtension"
+ "com.apple.GradientPoster.GradientPosterExtension"
+ "components invalidated"
+ "conditionsNecessitateTokenCancel"
+ "currentReplicas"
+ "floatingLayerDisplayTransferFadeInDuration"
+ "frozenFloatingLayer"
+ "frozenFloatingLayerWrapper"
+ "frozenView"
+ "generation"
+ "have snapshot"
+ "hinge MOTION STARTED: snapshotting deferred on both variants; poster pinned running"
+ "hinge SETTLED after %.2fs of motion (%lu accepted / %lu delivered updates); snapshotting re-enabled (%{public}@)"
+ "hinge became stable"
+ "hinge is active"
+ "hinge update: BASELINE status=%ld angle=%.4fdeg (not motion)"
+ "hinge update: CHANGED status %ld->%ld angle %.4f->%.4fdeg (delta %.4fdeg)"
+ "hinge update: DETACHED (no hinge in this hierarchy); keeping last known state"
+ "hinge update: UNKNOWN status; keeping last known state"
+ "hinge update: WITHIN TOLERANCE status=%ld angle=%.4fdeg (ref %.4fdeg, delta %.4fdeg, ignored)"
+ "home screen configuration unreadable"
+ "initial"
+ "installed snapshot-gating hinge interaction"
+ "isHingeActive"
+ "isRotating"
+ "isShowingSnapshot"
+ "isSnapshotting"
+ "liveHoldReasons"
+ "lock rotation complete"
+ "lock snapshot backstop"
+ "model object cache unavailable"
+ "n/a"
+ "needsSnapshot"
+ "nil instanceURL"
+ "nil path"
+ "no file resource identifier"
+ "no valid snapshot"
+ "observed"
+ "pb_activate:"
+ "pb_update:"
+ "pm%ld"
+ "quiesced"
+ "re-capture: request arrived during previous capture"
+ "reasonsToNotSnapshot"
+ "reset after successful capture"
+ "salient rect %{public}@: fenced update pending; coalescing"
+ "salient rect %{public}@: pushing immediately"
+ "same version and storage"
+ "same version and storage, home screen configuration differs"
+ "scene recreated"
+ "screen"
+ "secondsUntilDeadline"
+ "setActiveVariant:%{public}@ (was %{public}@)"
+ "significant event"
+ "snapshot readiness %{public}@"
+ "snapshot suppressed for reasons: %@"
+ "snapshot suppression lifted: "
+ "storage differs"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v16@?0@\"UIWindow\"8"
+ "v24@?0@\"UIHingeInteraction\"8@\"UIHingeInteractionUpdate\"16"
+ "v24@?0^{__CFRunLoopObserver=}8Q16"
+ "version differs"
+ "visibility inputs: activelyRequired=%{BOOL}u needsRuntime=%{BOOL}u activeStyle=%{public}@ (hidden=%{BOOL}u) lockStyle=%{public}@ homeStyle=%{public}@ activeVariant=%{public}@ homeScene=%{BOOL}u obscured=%{BOOL}u idle=%{BOOL}u"
+ "void soft_PUIWindowSceneSetHostInformedOrientation(UIWindowScene *__strong, UIInterfaceOrientation)"
+ "void soft_PUIWindowSceneSetShouldSuppressFencedUpdates(UIWindowScene *__strong, BOOL)"
+ "wallpaper became eligible to snapshot"
+ "wallpaper: scene effectiveGeometry.interfaceOrientation (%ld) disagrees with rotation target (%ld) on %{public}@; using rotation target. rdar://181263043"
+ "willRotateToInterfaceOrientation: %ld -> %ld (dynamicRotation=%{BOOL}u, deviceOrientationToUse=%ld)"
+ "wrapperView"
+ "\xa5"
+ "\xf0\xe1"
+ "\xf0\xf0\xf0q"
- "\v"
- "A\xf0q"
- "BOOL soft_PUIDynamicRotationIsActive(void)"
- "Class getPRUISDisplayStateProgressControllerClass(void)_block_invoke"
- "Enabling %@ as a cross-display portal because moving between windows on different screens."
- "PRUISDisplayStateProgressController"
- "PUIDynamicRotationIsActive"
- "Poster scenes FENCED update for reasons: %{public}@"
- "Poster scenes un-fenced update for reasons: %{public}@"
- "Q"
- "Updating activity mode for scene %@ to %{public}@"
- "[%{public}@] Snapshot already %@, not scheduling for reason: %{public}@"
- "[%{public}@] WIPE cache (pathProvider rotate): old=%{public}@ new=%{public}@"
- "[home] configureEffectViewForMode: setShowsSnapshot=%{BOOL}d snapshotSourceValid=%{BOOL}d needsSnapshot=%{BOOL}d isSnapshotting=%{BOOL}d"
- "[snapshot] _updateImageViewRotation: orientation=%ld radians=%f windowScene=%@"
- "displayConfigurationTransition"
- "in extended render session"
- "in progress"
- "\x95"
- "\xf0\xf0a"
- "\xf0\xf1"
```
