## Home

> `/System/iOSSupport/System/Library/PrivateFrameworks/Home.framework/Versions/A/Home`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1166.7.1.0.0
-  __TEXT.__text: 0x3af170
+1166.7.2.0.0
+  __TEXT.__text: 0x3b1720
   __TEXT.__auth_stubs: 0x3a10
-  __TEXT.__objc_methlist: 0x2b404
+  __TEXT.__objc_methlist: 0x2b5fc
   __TEXT.__const: 0x4878
   __TEXT.__constg_swiftt: 0x198c
   __TEXT.__swift5_typeref: 0x2420

   __TEXT.__swift5_proto: 0x1dc
   __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_capture: 0xe38
-  __TEXT.__oslogstring: 0x1b2eb
-  __TEXT.__cstring: 0x3324e
+  __TEXT.__oslogstring: 0x1b400
+  __TEXT.__cstring: 0x3341c
   __TEXT.__swift_as_entry: 0x1e8
   __TEXT.__swift_as_ret: 0x1f0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x539c
+  __TEXT.__gcc_except_tab: 0x5458
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0xeb40
+  __TEXT.__unwind_info: 0xec00
   __TEXT.__eh_frame: 0x6360
-  __TEXT.__objc_classname: 0x7123
-  __TEXT.__objc_methname: 0x59c8d
-  __TEXT.__objc_methtype: 0x7acb
-  __TEXT.__objc_stubs: 0x39760
-  __DATA_CONST.__got: 0x2ef8
-  __DATA_CONST.__const: 0x10ba8
-  __DATA_CONST.__objc_classlist: 0x17b0
+  __TEXT.__objc_classname: 0x7189
+  __TEXT.__objc_methname: 0x5a24d
+  __TEXT.__objc_methtype: 0x7b4d
+  __TEXT.__objc_stubs: 0x39c00
+  __DATA_CONST.__got: 0x2f00
+  __DATA_CONST.__const: 0x10c30
+  __DATA_CONST.__objc_classlist: 0x17b8
   __DATA_CONST.__objc_catlist: 0x418
-  __DATA_CONST.__objc_protolist: 0x8b0
+  __DATA_CONST.__objc_protolist: 0x8c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x123c0
+  __DATA_CONST.__objc_selrefs: 0x124c8
   __DATA_CONST.__objc_protorefs: 0x3c8
-  __DATA_CONST.__objc_superrefs: 0x12d0
+  __DATA_CONST.__objc_superrefs: 0x12d8
   __DATA_CONST.__objc_arraydata: 0x368
   __AUTH_CONST.__auth_got: 0x1d18
-  __AUTH_CONST.__const: 0xe3b8
-  __AUTH_CONST.__cfstring: 0x26620
-  __AUTH_CONST.__objc_const: 0x49ed8
+  __AUTH_CONST.__const: 0xe418
+  __AUTH_CONST.__cfstring: 0x26780
+  __AUTH_CONST.__objc_const: 0x4a178
   __AUTH_CONST.__objc_intobj: 0x2190
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xa098
+  __AUTH.__objc_data: 0xa0e8
   __AUTH.__data: 0xb00
-  __DATA.__objc_ivar: 0x1508
-  __DATA.__data: 0x6c20
+  __DATA.__objc_ivar: 0x152c
+  __DATA.__data: 0x6ce0
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x2ec0
   __DATA.__common: 0x128

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation
+  - /System/Library/PrivateFrameworks/HomeKitClips.framework/Versions/A/HomeKitClips
   - /System/Library/PrivateFrameworks/HomeKitEvents.framework/Versions/A/HomeKitEvents
   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/Versions/A/HomeKitFeatures
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19989
-  Symbols:   36860
-  CStrings:  22577
+  Functions: 20037
+  Symbols:   36980
+  CStrings:  22650
 
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
+ OBJC_IVAR_$_HFCameraPlaybackEngine._eventPrefetcher
+ OBJC_IVAR_$_HFCameraPlaybackEngine._incrementalFetchLimit
+ OBJC_IVAR_$_HFCameraPlaybackEngine._initialFetchLimit
+ OBJC_IVAR_$_HFCameraPlaybackEngine._recurringEventFetchTimer
+ OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._boundarySize
+ OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._delegate
+ OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._eventFetchLimit
+ OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._fetchOperationQueue
+ OBJC_IVAR_$_HFCameraPlaybackEngineEventPrefetcher._visitedEventIDs
+ _HFDisableFetchAdditionalCameraEventsKey
+ _HFDisableRecurringCameraEventFetchTimerKey
+ _HFOverrideIncrementalCameraMetadataFetchLimitKey
+ _HFOverrideInitialCameraMetadataFetchLimitKey
+ _HFPreferencesCameraClipsDebugUIKey
+ _HFPreferencesCameraDebugKey
+ _HFPreferencesCameraVisibilityDebugKey
+ _OBJC_CLASS_$_HFCameraPlaybackEngineEventPrefetcher
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
+ ___44-[HFCameraPlaybackEngine fetchClipWithUUID:]_block_invoke_6
+ ___44-[HFCameraPlaybackEngine fetchClipWithUUID:]_block_invoke_7
+ ___46-[HFCameraPlaybackEngine updateConfiguration:]_block_invoke_2
+ ___55-[HFCameraPlaybackEngine startPlaybackAtDate:withClip:]_block_invoke
+ ___55-[HFCameraPlaybackEngine startPlaybackAtDate:withClip:]_block_invoke_2
+ ___57-[HFCameraPlaybackEngineEventPrefetcher cancelAllFetches]_block_invoke
+ ___65-[HFCameraPlaybackEngine updatePlaybackPositionToDate:usingClip:]_block_invoke_2
+ ___81-[HFCameraPlaybackEngineEventPrefetcher fetchNewerEventsIfNeededForCurrentEvent:]_block_invoke
+ ___81-[HFCameraPlaybackEngineEventPrefetcher fetchOlderEventsIfNeededForCurrentEvent:]_block_invoke
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_2
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_3
+ ___89-[HFCameraPlaybackEngine _fetchEventsWithDateInterval:limit:shouldOrderAscending:reason:]_block_invoke_4
+ ___block_descriptor_40_e8_32bs_e16_v16?0"NSNull"8ls32l8
+ ___block_descriptor_65_e8_32s40s48w_e25_v16?0?<v?"NSError">8lw48l8s32l8s40l8
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
CStrings:
+ "-[HFCameraPlaybackEngineEventPrefetcher init]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LyLACr/Sources/Home/HomeFramework/Utilities/HFAccessoryListUtilities.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LyLACr/Sources/Home/HomeFramework/Utilities/ReorderableItemList.swift"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MZMzaD/Sources/Home/HomeFramework/Utilities/HFAccessoryListUtilities.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MZMzaD/Sources/Home/HomeFramework/Utilities/ReorderableItemList.swift"
```
