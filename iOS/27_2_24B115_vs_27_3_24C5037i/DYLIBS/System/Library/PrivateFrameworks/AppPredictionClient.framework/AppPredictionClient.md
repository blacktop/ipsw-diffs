## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-678.0.1.0.0
-  __TEXT.__text: 0x188f0c
-  __TEXT.__objc_methlist: 0x190bc
-  __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x1c96f
-  __TEXT.__oslogstring: 0x180dc
-  __TEXT.__gcc_except_tab: 0x20ac
+678.2.1.0.3
+  __TEXT.__text: 0x18cb54
+  __TEXT.__objc_methlist: 0x1930c
+  __TEXT.__const: 0x720
+  __TEXT.__cstring: 0x1d041
+  __TEXT.__oslogstring: 0x186d9
+  __TEXT.__gcc_except_tab: 0x2114
   __TEXT.__dlopen_cstrs: 0x491
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x8670
+  __TEXT.__unwind_info: 0x8758
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6490
-  __DATA_CONST.__objc_classlist: 0xe40
+  __DATA_CONST.__const: 0x6618
+  __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa200
+  __DATA_CONST.__objc_selrefs: 0xa340
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0xc48
-  __DATA_CONST.__objc_arraydata: 0xb48
-  __DATA_CONST.__got: 0x1730
-  __AUTH_CONST.__const: 0x2ba0
-  __AUTH_CONST.__cfstring: 0x15680
-  __AUTH_CONST.__objc_const: 0x462b0
-  __AUTH_CONST.__objc_intobj: 0xa68
-  __AUTH_CONST.__objc_arrayobj: 0x708
+  __DATA_CONST.__objc_superrefs: 0xc50
+  __DATA_CONST.__objc_arraydata: 0xb58
+  __DATA_CONST.__got: 0x1740
+  __AUTH_CONST.__const: 0x2be0
+  __AUTH_CONST.__cfstring: 0x15940
+  __AUTH_CONST.__objc_const: 0x46b48
+  __AUTH_CONST.__objc_intobj: 0xa80
+  __AUTH_CONST.__objc_arrayobj: 0x720
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH.__objc_data: 0x4740
-  __DATA.__objc_ivar: 0x1cb8
-  __DATA.__data: 0x1cf0
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH.__objc_data: 0x4790
+  __DATA.__objc_ivar: 0x1d38
+  __DATA.__data: 0x1d50
   __DATA_DIRTY.__objc_data: 0x4740
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x278

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10980
-  Symbols:   16896
-  CStrings:  4876
+  Functions: 11050
+  Symbols:   17008
+  CStrings:  4945
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager _pendingWidgetIdentifiersForPersonalities:clientIdentity:]
+ +[ATXDefaultHomeScreenItemManager _personalitiesOfPairedDeviceWidgets:replacedByLocalCopiesAmongDescriptors:]
+ +[ATXDefaultHomeScreenItemManager _snapshotOfSmartStackRequest:]
+ +[ATXDefaultHomeScreenItemManager _widgetPersonalitiesFilteredOutOfDescriptors:keptDescriptors:personaIdentifier:]
+ +[ATXDefaultHomeScreenItemProducerUtilities _widgetKeyResolvingGatedWidgetPlaceholder:]
+ -[ATXDefaultHomeScreenItemManager _fetchWidgetSmartStackWithRequest:findingPendingWidgets:completionHandler:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackResponseWithRequest:findingPendingWidgets:error:]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:findingPendingWidgets:error:]
+ -[ATXDefaultHomeScreenItemManager observeWidgetSmartStackWithRequest:timeout:updateHandler:]
+ -[ATXDefaultHomeScreenItemOnboardingStacks initWithOnboardingStacks:sortedThirdPartyWidgets:pendingWidgetPersonalities:]
+ -[ATXDefaultHomeScreenItemOnboardingStacks pendingWidgetPersonalities]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _isWaitingForDescriptorOfPersonality:size:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _pendingWidgetPersonalitiesForTvOSOnboardingStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _standInForWidgetWithPersonality:appBundleId:supportedFamilies:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _tvOSOnboardingStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setShouldFindPendingWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setWidgetIdentifiersDeniedForClient:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setWidgetPersonalitiesFilteredOutForClient:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer shouldFindPendingWidgets]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer widgetIdentifiersDeniedForClient]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer widgetPersonalitiesFilteredOutForClient]
+ -[ATXDefaultHomeScreenItemProducer setShouldFindPendingWidgets:]
+ -[ATXDefaultHomeScreenItemProducer setWidgetIdentifiersDeniedForClient:]
+ -[ATXDefaultHomeScreenItemProducer setWidgetPersonalitiesFilteredOutForClient:]
+ -[ATXDefaultHomeScreenItemProducer shouldFindPendingWidgets]
+ -[ATXDefaultHomeScreenItemProducer widgetIdentifiersDeniedForClient]
+ -[ATXDefaultHomeScreenItemProducer widgetPersonalitiesFilteredOutForClient]
+ -[ATXWidgetSmartStackObservation .cxx_destruct]
+ -[ATXWidgetSmartStackObservation _queue_deadlineDidPass]
+ -[ATXWidgetSmartStackObservation _queue_finishWithOutcome:]
+ -[ATXWidgetSmartStackObservation _queue_firstBuildDeadlineDidPass]
+ -[ATXWidgetSmartStackObservation _queue_generate]
+ -[ATXWidgetSmartStackObservation _queue_handleResponse:error:]
+ -[ATXWidgetSmartStackObservation _queue_scheduleRebuild]
+ -[ATXWidgetSmartStackObservation _queue_sendFinalResult]
+ -[ATXWidgetSmartStackObservation _queue_sendResponse:error:isFinal:]
+ -[ATXWidgetSmartStackObservation _queue_startDeadlineTimer]
+ -[ATXWidgetSmartStackObservation cancelWithReason:]
+ -[ATXWidgetSmartStackObservation cancel]
+ -[ATXWidgetSmartStackObservation cancellationReason]
+ -[ATXWidgetSmartStackObservation descriptorsDidChange]
+ -[ATXWidgetSmartStackObservation initWithTimeout:generator:updateHandler:]
+ -[ATXWidgetSmartStackObservation startObservingDescriptorCacheFromProvider:]
+ -[ATXWidgetSmartStackObservation startObservingDescriptorCacheFromProvider:rebuildNotificationName:]
+ -[ATXWidgetSmartStackObservation widgetDescriptorCacheDidUpdateHomeScreenDescriptors:]
+ -[ATXWidgetSmartStackResponse initWithStacks:pendingWidgetIdentifiers:isFinal:]
+ -[ATXWidgetSmartStackResponse isFinal]
+ -[ATXWidgetSmartStackResponse pendingWidgetIdentifiers]
+ GCC_except_table21
+ GCC_except_table34
+ GCC_except_table42
+ GCC_except_table45
+ _ATXPairedDeviceWidgetRankingImportedDarwinNotificationName
+ _OBJC_CLASS_$_ATXWidgetSmartStackObservation
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacks._pendingWidgetPersonalities
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._shouldFindPendingWidgets
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._widgetIdentifiersDeniedForClient
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._widgetPersonalitiesFilteredOutForClient
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._shouldFindPendingWidgets
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._widgetIdentifiersDeniedForClient
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._widgetPersonalitiesFilteredOutForClient
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._buildQueue
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._cancellationReason
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._deadlinePassed
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._deadlineTimer
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._descriptorCache
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._generator
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._hasBuildResult
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._hasStarted
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._isFinished
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._isGenerating
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._isRebuildScheduled
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._lastSentResponse
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._latestError
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._latestResponse
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._needsGeneration
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._queue
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._rebuildNotificationToken
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._retainedSelf
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._signpostID
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._startUptime
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._timeout
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._updateCount
+ _OBJC_IVAR_$_ATXWidgetSmartStackObservation._updateHandler
+ _OBJC_IVAR_$_ATXWidgetSmartStackResponse._isFinal
+ _OBJC_IVAR_$_ATXWidgetSmartStackResponse._pendingWidgetIdentifiers
+ _OBJC_METACLASS_$_ATXWidgetSmartStackObservation
+ __OBJC_$_INSTANCE_METHODS_ATXWidgetSmartStackObservation
+ __OBJC_$_INSTANCE_VARIABLES_ATXWidgetSmartStackObservation
+ __OBJC_$_PROP_LIST_ATXWidgetSmartStackObservation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ATXWidgetDescriptorCacheObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ATXWidgetDescriptorCacheObserver
+ __OBJC_$_PROTOCOL_REFS_ATXWidgetDescriptorCacheObserver
+ __OBJC_CLASS_PROTOCOLS_$_ATXWidgetSmartStackObservation
+ __OBJC_CLASS_RO_$_ATXWidgetSmartStackObservation
+ __OBJC_LABEL_PROTOCOL_$_ATXWidgetDescriptorCacheObserver
+ __OBJC_METACLASS_RO_$_ATXWidgetSmartStackObservation
+ __OBJC_PROTOCOL_$_ATXWidgetDescriptorCacheObserver
+ ___100-[ATXWidgetSmartStackObservation startObservingDescriptorCacheFromProvider:rebuildNotificationName:]_block_invoke
+ ___109-[ATXDefaultHomeScreenItemManager _fetchWidgetSmartStackWithRequest:findingPendingWidgets:completionHandler:]_block_invoke
+ ___189-[ATXDefaultHomeScreenItemOnboardingStacksProducer _pendingWidgetPersonalitiesForTvOSOnboardingStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___49-[ATXWidgetSmartStackObservation _queue_generate]_block_invoke
+ ___49-[ATXWidgetSmartStackObservation _queue_generate]_block_invoke_2
+ ___49-[ATXWidgetSmartStackObservation _queue_generate]_block_invoke_3
+ ___51-[ATXWidgetSmartStackObservation cancelWithReason:]_block_invoke
+ ___54-[ATXWidgetSmartStackObservation descriptorsDidChange]_block_invoke
+ ___56-[ATXWidgetSmartStackObservation _queue_scheduleRebuild]_block_invoke
+ ___59-[ATXWidgetSmartStackObservation _queue_startDeadlineTimer]_block_invoke
+ ___92+[ATXDefaultHomeScreenItemManager _pendingWidgetIdentifiersForPersonalities:clientIdentity:]_block_invoke
+ ___92-[ATXDefaultHomeScreenItemManager observeWidgetSmartStackWithRequest:timeout:updateHandler:]_block_invoke
+ ___block_descriptor_40_e8_32w_e49_v24?0"ATXWidgetSmartStackResponse"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_58_e8_32s40s48r_e54_v16?0?<v?"ATXWidgetSmartStackResponse""NSError">8lr48l8s32l8s40l8
+ __os_feature_enabled_impl
- -[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:error:]
- -[ATXDefaultHomeScreenItemManager _generateSmartStacksWithRequest:error:]
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke
CStrings:
+ "%s: %p already building, so building again after"
+ "%s: %p couldn't build the first stacks, and nothing will build them again: %{public}@"
+ "%s: %p couldn't build the first stacks, so waiting for descriptors to change: %{public}@"
+ "%s: %p couldn't register for %{public}@ (status %u), so it won't build again when it's posted"
+ "%s: %p finished (%{public}s, cancellation reason: %{public}s) after %.1fs and %lu updates, still waiting on %{public}@"
+ "%s: %p keeping the last stacks after a rebuild failed: %{public}@"
+ "%s: %p observing for Client: %@, variant: %lu, timeout: %.1fs"
+ "%s: %p rebuilt stacks are unchanged, still waiting on %lu widgets"
+ "%s: %p sending update %lu with %lu stacks, final: %{BOOL}d, still waiting on %lu widgets, error: %{public}@"
+ "%s: %p started, waiting up to %.1fs after the first stacks for missing widgets"
+ "%s: %p stopped waiting for missing widgets after %.1fs"
+ "%s: %p the first build didn't finish within %.1fs, so giving up"
+ "%s: Client has no persona, so it isn't waiting on %{public}@"
+ "%s: Couldn't copy the smart stack request, so the observation uses the caller's: %{public}@"
+ "%s: building the tvOS onboarding stacks again with stand-ins for %lu missing widgets"
+ "%s: local copies take the place of %lu of the paired device's widgets: %{public}@"
+ "%s: tvOS onboarding stacks are waiting on descriptors for %{public}@"
+ "+[ATXDefaultHomeScreenItemManager _pendingWidgetIdentifiersForPersonalities:clientIdentity:]"
+ "+[ATXDefaultHomeScreenItemManager _snapshotOfSmartStackRequest:]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackResponseWithRequest:findingPendingWidgets:error:]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:findingPendingWidgets:error:]"
+ "-[ATXDefaultHomeScreenItemManager observeWidgetSmartStackWithRequest:timeout:updateHandler:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _pendingWidgetPersonalitiesForTvOSOnboardingStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXWidgetSmartStackObservation _queue_deadlineDidPass]"
+ "-[ATXWidgetSmartStackObservation _queue_finishWithOutcome:]"
+ "-[ATXWidgetSmartStackObservation _queue_firstBuildDeadlineDidPass]"
+ "-[ATXWidgetSmartStackObservation _queue_generate]"
+ "-[ATXWidgetSmartStackObservation _queue_handleResponse:error:]"
+ "-[ATXWidgetSmartStackObservation _queue_sendResponse:error:isFinal:]"
+ "-[ATXWidgetSmartStackObservation startObservingDescriptorCacheFromProvider:rebuildNotificationName:]_block_invoke"
+ "-[ATXWidgetSmartStackObservation startObservingDescriptorCacheFromProvider:rebuildNotificationName:]_block_invoke_2"
+ "ATXStandInWidgetDevice"
+ "ATXWidgetSmartStackObservation"
+ "ATXWidgetSmartStackObservation.build"
+ "ClassicAnalog"
+ "ClassicCalendar"
+ "ClassicDigital"
+ "Failed to rebuild smart stacks"
+ "HomeCamera"
+ "HomeModular"
+ "Memories"
+ "Modular"
+ "PhotoFrame"
+ "PriorityFeedbackNegative"
+ "PriorityFeedbackPositive"
+ "PriorityFeedbackReportConcern"
+ "ResponsiveArt"
+ "Rushmore"
+ "SharedPhotoFrame"
+ "Snoopy"
+ "StandByInfraGallery"
+ "Timed out building the first smart stacks"
+ "cancelled"
+ "com.apple.duetexpertd.pairedDeviceWidgetRankingImported"
+ "failed"
+ "final:%{BOOL}d stacks:%lu pending:%lu"
+ "isFinal"
+ "no_longer_needed"
+ "none"
+ "nothing"
+ "outcome:%{public}s cancellation:%{public}s updates:%lu pending:%lu"
+ "pendingWidgetIdentifiers"
+ "smartStackObservation"
+ "smartStackObservationRebuild"
+ "smartStackObservationUpdate"
+ "stack_removed"
+ "stacks:%lu pending:%lu"
+ "timedOut"
+ "unspecified"
+ "user_edited_stack"
+ "v16@?0@?<v@?@\"ATXWidgetSmartStackResponse\"@\"NSError\">8"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStackWithDescriptorCacheFromRequest:error:]"
- "-[ATXDefaultHomeScreenItemManager _generateSmartStacksWithRequest:error:]"
```
