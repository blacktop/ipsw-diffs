## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

 1166.6.7.1.1
-  __TEXT.__text: 0x3cdb9c
+  __TEXT.__text: 0x3d014c
   __TEXT.__auth_stubs: 0x3bf0
-  __TEXT.__objc_methlist: 0x2c224
+  __TEXT.__objc_methlist: 0x2c41c
   __TEXT.__const: 0x4bc8
   __TEXT.__dlopen_cstrs: 0x4b
   __TEXT.__constg_swiftt: 0x1ad8

   __TEXT.__swift5_proto: 0x1e8
   __TEXT.__swift5_types: 0x124
   __TEXT.__swift5_capture: 0xe8c
-  __TEXT.__oslogstring: 0x1d0bc
-  __TEXT.__cstring: 0x33c27
+  __TEXT.__oslogstring: 0x1d1d1
+  __TEXT.__cstring: 0x33df5
   __TEXT.__swift_as_entry: 0x20c
   __TEXT.__swift_as_ret: 0x224
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x5804
+  __TEXT.__gcc_except_tab: 0x58c0
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0xf230
+  __TEXT.__unwind_info: 0xf2f8
   __TEXT.__eh_frame: 0x6a08
-  __TEXT.__objc_classname: 0x7456
-  __TEXT.__objc_methname: 0x5c7cd
-  __TEXT.__objc_methtype: 0x7faf
-  __TEXT.__objc_stubs: 0x3b340
-  __DATA_CONST.__got: 0x3090
-  __DATA_CONST.__const: 0x11070
-  __DATA_CONST.__objc_classlist: 0x1808
+  __TEXT.__objc_classname: 0x74bc
+  __TEXT.__objc_methname: 0x5cdad
+  __TEXT.__objc_methtype: 0x8031
+  __TEXT.__objc_stubs: 0x3b7e0
+  __DATA_CONST.__got: 0x3098
+  __DATA_CONST.__const: 0x110f8
+  __DATA_CONST.__objc_classlist: 0x1810
   __DATA_CONST.__objc_catlist: 0x418
-  __DATA_CONST.__objc_protolist: 0x920
+  __DATA_CONST.__objc_protolist: 0x930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12bf8
+  __DATA_CONST.__objc_selrefs: 0x12d00
   __DATA_CONST.__objc_protorefs: 0x410
-  __DATA_CONST.__objc_superrefs: 0x1308
+  __DATA_CONST.__objc_superrefs: 0x1310
   __DATA_CONST.__objc_arraydata: 0x3b8
   __AUTH_CONST.__auth_got: 0x1e08
-  __AUTH_CONST.__const: 0xe768
-  __AUTH_CONST.__cfstring: 0x26c20
-  __AUTH_CONST.__objc_const: 0x4b338
+  __AUTH_CONST.__const: 0xe7c8
+  __AUTH_CONST.__cfstring: 0x26d80
+  __AUTH_CONST.__objc_const: 0x4b5d8
   __AUTH_CONST.__objc_intobj: 0x22c8
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xa448
+  __AUTH.__objc_data: 0xa498
   __AUTH.__data: 0xd90
-  __DATA.__objc_ivar: 0x15bc
-  __DATA.__data: 0x7290
+  __DATA.__objc_ivar: 0x15e0
+  __DATA.__data: 0x7350
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x3040
   __DATA.__common: 0x150

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel
+  - /System/Library/PrivateFrameworks/HomeKitClips.framework/HomeKitClips
   - /System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents
   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures
   - /System/Library/PrivateFrameworks/HomeServices.framework/HomeServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F7A94A03-634F-3572-AC9D-FE67D2641082
-  Functions: 20495
-  Symbols:   56982
-  CStrings:  28656
+  UUID: 601F7A4D-9234-375F-A094-A7E1F2A7501A
+  Functions: 20543
+  Symbols:   57160
+  CStrings:  28741
 
Symbols:
+ +[HFCameraUtilities overrideIncrementalCameraMetadataFetchLimit]
+ +[HFCameraUtilities overrideInitialCameraMetadataFetchLimit]
+ +[HFCameraUtilities shouldDisableFetchAdditionalCameraEvents]
+ +[HFCameraUtilities shouldDisableRecurringCameraEventFetchTimer]
+ -[HFCameraPlaybackEngine _beginRecurringEventFetch]
+ -[HFCameraPlaybackEngine _endRecurringEventFetch]
+ -[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]
+ -[HFCameraPlaybackEngine _fetchNewerEventsWithLimit:shouldOrderAscending:reason:]
+ -[HFCameraPlaybackEngine eventPrefetcher]
+ -[HFCameraPlaybackEngine existingEvents]
+ -[HFCameraPlaybackEngine fetchNewerEventsInAscendingOrder:]
+ -[HFCameraPlaybackEngine fetchNewerEventsWithLimit:]
+ -[HFCameraPlaybackEngine fetchOlderEventsWithLimit:]
+ -[HFCameraPlaybackEngine incrementalFetchLimit]
+ -[HFCameraPlaybackEngine initialFetchLimit]
+ -[HFCameraPlaybackEngine recurringEventFetchTimer]
+ -[HFCameraPlaybackEngine setEventPrefetcher:]
+ -[HFCameraPlaybackEngine setIncrementalFetchLimit:]
+ -[HFCameraPlaybackEngine setInitialFetchLimit:]
+ -[HFCameraPlaybackEngine setRecurringEventFetchTimer:]
+ -[HFCameraPlaybackEngineEventPrefetcher .cxx_destruct]
+ -[HFCameraPlaybackEngineEventPrefetcher boundarySize]
+ -[HFCameraPlaybackEngineEventPrefetcher cancelAllFetches]
+ -[HFCameraPlaybackEngineEventPrefetcher delegate]
+ -[HFCameraPlaybackEngineEventPrefetcher eventFetchLimit]
+ -[HFCameraPlaybackEngineEventPrefetcher fetchMoreEventsIfNeededWithCurrentEvent:]
+ -[HFCameraPlaybackEngineEventPrefetcher fetchNewerEventsIfNeededForCurrentEvent:]
+ -[HFCameraPlaybackEngineEventPrefetcher fetchOlderEventsIfNeededForCurrentEvent:]
+ -[HFCameraPlaybackEngineEventPrefetcher fetchOperationQueue]
+ -[HFCameraPlaybackEngineEventPrefetcher initWithDelegate:]
+ -[HFCameraPlaybackEngineEventPrefetcher initWithDelegate:boundarySize:eventFetchLimit:]
+ -[HFCameraPlaybackEngineEventPrefetcher init]
+ -[HFCameraPlaybackEngineEventPrefetcher setDelegate:]
+ -[HFCameraTimelapseClipManager newestTimelapseClip]
+ -[HFCameraTimelapseClipManager oldestTimelapseClip]
+ GCC_except_table119
+ GCC_except_table123
+ _HFDisableFetchAdditionalCameraEventsKey
+ _HFDisableRecurringCameraEventFetchTimerKey
+ _HFOverrideIncrementalCameraMetadataFetchLimitKey
+ _HFOverrideInitialCameraMetadataFetchLimitKey
+ _HFPreferencesCameraClipsDebugUIKey
+ _HFPreferencesCameraDebugKey
+ _HFPreferencesCameraVisibilityDebugKey
+ _OBJC_CLASS_$_HFCameraPlaybackEngineEventPrefetcher
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._eventPrefetcher
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._incrementalFetchLimit
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._initialFetchLimit
+ _OBJC_IVAR_$_HFCameraPlaybackEngine._recurringEventFetchTimer
+ _OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._boundarySize
+ _OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._delegate
+ _OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._eventFetchLimit
+ _OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._fetchOperationQueue
+ _OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._visitedEventIDs
+ _OBJC_METACLASS_$_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_$_INSTANCE_METHODS_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_$_INSTANCE_VARIABLES_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_$_PROP_LIST_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HFCameraPlaybackEngineEventPrefetcherDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HFCameraPlaybackEngineEventPrefetcherDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_HFCameraPlaybackEngineEventPrefetcherDelegate
+ __OBJC_$_PROTOCOL_REFS_HMFTimerDelegate
+ __OBJC_CLASS_RO_$_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_LABEL_PROTOCOL_$_HFCameraPlaybackEngineEventPrefetcherDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMFTimerDelegate
+ __OBJC_METACLASS_RO_$_HFCameraPlaybackEngineEventPrefetcher
+ __OBJC_PROTOCOL_$_HFCameraPlaybackEngineEventPrefetcherDelegate
+ __OBJC_PROTOCOL_$_HMFTimerDelegate
+ ___43-[HFCameraPlaybackEngine fetchCameraEvents]_block_invoke.85
+ ___43-[HFCameraPlaybackEngine fetchCameraEvents]_block_invoke_2.87
+ ___44-[HFCameraPlaybackEngine fetchClipWithUUID:]_block_invoke_6
+ ___44-[HFCameraPlaybackEngine fetchClipWithUUID:]_block_invoke_7
+ ___45-[HFHomeKitDispatcher updateHomeSensingState]_block_invoke.660
+ ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke.123
+ ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke_2
+ ___55-[HFCameraPlaybackEngine startPlaybackAtDate:withClip:]_block_invoke
+ ___55-[HFCameraPlaybackEngine startPlaybackAtDate:withClip:]_block_invoke_2
+ ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.631
+ ___57-[HFCameraPlaybackEngineEventPrefetcher cancelAllFetches]_block_invoke
+ ___61-[HFHomeKitDispatcher _createAudioAnalysisSubscriberForHome:]_block_invoke.669
+ ___63-[HFCameraPlaybackEngine fetchClipForSignificantEventWithUUID:]_block_invoke.94
+ ___63-[HFCameraPlaybackEngine fetchClipForSignificantEventWithUUID:]_block_invoke_2.95
+ ___65-[HFCameraPlaybackEngine updatePlaybackPositionToDate:usingClip:]_block_invoke_2
+ ___73-[HFCameraTimelapseClipManager _fetchClipsFromStartDate:toEndDate:limit:]_block_invoke.12
+ ___74-[HFCameraPlaybackEngine _recordingEventManager:didUpdateRecordingEvents:]_block_invoke.161
+ ___81-[HFCameraPlaybackEngineEventPrefetcher fetchNewerEventsIfNeededForCurrentEvent:]_block_invoke
+ ___81-[HFCameraPlaybackEngineEventPrefetcher fetchOlderEventsIfNeededForCurrentEvent:]_block_invoke
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_2
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_3
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_4
+ ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.138
+ ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.139
+ ___block_descriptor_40_e8_32bs_e16_v16?0"NSNull"8ls32l8
+ ___block_descriptor_65_e8_32s40s48w_e25_v16?0?<v?"NSError">8lw48l8s32l8s40l8
+ ___block_literal_global.119
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.640
+ ___block_literal_global.653
+ ___block_literal_global.668
+ _objc_msgSend$_beginRecurringEventFetch
+ _objc_msgSend$_endRecurringEventFetch
+ _objc_msgSend$_fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:
+ _objc_msgSend$_fetchNewerEventsWithLimit:shouldOrderAscending:reason:
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$boundarySize
+ _objc_msgSend$cancelAllFetches
+ _objc_msgSend$containsClip:
+ _objc_msgSend$eventFetchLimit
+ _objc_msgSend$eventPrefetcher
+ _objc_msgSend$existingEvents
+ _objc_msgSend$fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:
+ _objc_msgSend$fetchMoreEventsIfNeededWithCurrentEvent:
+ _objc_msgSend$fetchNewerEventsIfNeededForCurrentEvent:
+ _objc_msgSend$fetchNewerEventsWithLimit:
+ _objc_msgSend$fetchOlderEventsIfNeededForCurrentEvent:
+ _objc_msgSend$fetchOlderEventsWithLimit:
+ _objc_msgSend$fetchOperationQueue
+ _objc_msgSend$hf_fetchTimelapseClipsWithDateInterval:padding:shouldOrderAscending:
+ _objc_msgSend$incrementalFetchLimit
+ _objc_msgSend$initWithDelegate:boundarySize:eventFetchLimit:
+ _objc_msgSend$initialFetchLimit
+ _objc_msgSend$logFetchEventsToJSONWithDateInterval:limit:ascending:reason:playheadPosition:completionHandler:
+ _objc_msgSend$newestTimelapseClip
+ _objc_msgSend$notificationUUID
+ _objc_msgSend$oldestTimelapseClip
+ _objc_msgSend$overrideIncrementalCameraMetadataFetchLimit
+ _objc_msgSend$overrideInitialCameraMetadataFetchLimit
+ _objc_msgSend$recurringEventFetchTimer
+ _objc_msgSend$removeExistingFilesWithCompletionHandler:
+ _objc_msgSend$setDebugLogger:
+ _objc_msgSend$setDiagnosticsAttachmentRequestListener:
+ _objc_msgSend$setEventPrefetcher:
+ _objc_msgSend$setRecurringEventFetchTimer:
+ _objc_msgSend$shouldDisableFetchAdditionalCameraEvents
+ _objc_msgSend$shouldDisableRecurringCameraEventFetchTimer
+ _objc_msgSend$suspend
- GCC_except_table105
- GCC_except_table39
- ___43-[HFCameraPlaybackEngine fetchCameraEvents]_block_invoke.82
- ___43-[HFCameraPlaybackEngine fetchCameraEvents]_block_invoke_2.84
- ___45-[HFHomeKitDispatcher updateHomeSensingState]_block_invoke.657
- ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke.108
- ___55-[HFHomeKitDispatcher _setupLocationSensingCoordinator]_block_invoke.628
- ___61-[HFHomeKitDispatcher _createAudioAnalysisSubscriberForHome:]_block_invoke.667
- ___63-[HFCameraPlaybackEngine fetchClipForSignificantEventWithUUID:]_block_invoke.90
- ___63-[HFCameraPlaybackEngine fetchClipForSignificantEventWithUUID:]_block_invoke_2.91
- ___73-[HFCameraTimelapseClipManager _fetchClipsFromStartDate:toEndDate:limit:]_block_invoke.9
- ___74-[HFCameraPlaybackEngine _recordingEventManager:didUpdateRecordingEvents:]_block_invoke.139
- ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.122
- ___91-[HFCameraPlaybackEngine _updatePlaybackStateNotifyingObservers:rebuildClipPlayerIfNeeded:]_block_invoke.123
- ___block_literal_global.305
- ___block_literal_global.327
- ___block_literal_global.637
- ___block_literal_global.650
- ___block_literal_global.666
CStrings:
+ "-[HFCameraPlaybackEngineEventPrefetcher init]"
+ "@\"<HFCameraPlaybackEngineEventPrefetcherDelegate>\""
+ "@\"HFCameraPlaybackEngineEventPrefetcher\""
+ "Batch recording event throttling timer paused because the handler did not receive any events."
+ "Events produced by `HMCameraRecordingEventManager` should always be sent to its observers."
+ "HFCameraPlaybackEngineEventPrefetcher"
+ "HFCameraPlaybackEngineEventPrefetcher.m"
+ "HFCameraPlaybackEngineEventPrefetcherDelegate"
+ "HFDisableFetchAdditionalCameraEvents"
+ "HFDisableRecurringCameraEventFetchTimer"
+ "HFOverrideIncrementalCameraMetadataFetchLimit"
+ "HFOverrideInitialCameraMetadataFetchLimit"
+ "HMFTimerDelegate"
+ "T@\"<HFCameraPlaybackEngineEventPrefetcherDelegate>\",W,N,V_delegate"
+ "T@\"HFCameraPlaybackEngineEventPrefetcher\",&,N,V_eventPrefetcher"
+ "T@\"HMFTimer\",&,N,V_recurringEventFetchTimer"
+ "T@\"NSOperationQueue\",R,N,V_fetchOperationQueue"
+ "TQ,N,V_incrementalFetchLimit"
+ "TQ,N,V_initialFetchLimit"
+ "TQ,R,N,V_boundarySize"
+ "TQ,R,N,V_eventFetchLimit"
+ "[INCREMENTAL FETCH] prefetching newer events"
+ "[INCREMENTAL FETCH] prefetching older events with limit: %lu"
+ "[INCREMENTAL FETCH] recurringEventFetchTimer fired..."
+ "_beginRecurringEventFetch"
+ "_boundarySize"
+ "_endRecurringEventFetch"
+ "_eventFetchLimit"
+ "_eventPrefetcher"
+ "_fetchEvents error: %@"
+ "_fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:"
+ "_fetchNewerEventsWithLimit:shouldOrderAscending:reason:"
+ "_fetchOperationQueue"
+ "_incrementalFetchLimit"
+ "_initialFetchLimit"
+ "_recurringEventFetchTimer"
+ "_visitedEventIDs"
+ "addOperationWithBlock:"
+ "boundarySize"
+ "cameraClipsShowDebugUI"
+ "cameraDebug"
+ "cameraVisibility"
+ "cancelAllFetches"
+ "eventFetchLimit"
+ "eventPrefetcher"
+ "existingEvents"
+ "fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:"
+ "fetchMoreEventsIfNeededWithCurrentEvent:"
+ "fetchNewerEventsIfNeededForCurrentEvent:"
+ "fetchNewerEventsInAscendingOrder:"
+ "fetchNewerEventsWithLimit:"
+ "fetchOlderEventsIfNeededForCurrentEvent:"
+ "fetchOlderEventsWithLimit:"
+ "fetchOperationQueue"
+ "hkc_incremental_fetch"
+ "incrementalFetchLimit"
+ "initWithDelegate:boundarySize:eventFetchLimit:"
+ "initialFetchLimit"
+ "newestTimelapseClip"
+ "oldestTimelapseClip"
+ "overrideIncrementalCameraMetadataFetchLimit"
+ "overrideInitialCameraMetadataFetchLimit"
+ "recurringEventFetchTimer"
+ "setEventPrefetcher:"
+ "setIncrementalFetchLimit:"
+ "setInitialFetchLimit:"
+ "setRecurringEventFetchTimer:"
+ "shouldDisableFetchAdditionalCameraEvents"
+ "shouldDisableRecurringCameraEventFetchTimer"
+ "suspend"
+ "userTappedLiveButton"
+ "v24@0:8@\"HMFTimer\"16"
+ "v36@0:8Q16B24@28"

```
