## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA_DIRTY.__data`

```diff

-1117.0.0.0.0
-  __TEXT.__text: 0x6b5624
-  __TEXT.__objc_methlist: 0x34c60
+1119.0.0.0.0
+  __TEXT.__text: 0x6bd79c
+  __TEXT.__objc_methlist: 0x34e30
   __TEXT.__const: 0x4bd8
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x41b
-  __TEXT.__oslogstring: 0x8992d
-  __TEXT.__cstring: 0x4a64a
+  __TEXT.__oslogstring: 0x89e8d
+  __TEXT.__cstring: 0x4ae89
   __TEXT.__swift5_capture: 0xdc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x38

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x2ea88
+  __TEXT.__gcc_except_tab: 0x2ef98
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xf1c0
+  __TEXT.__unwind_info: 0xf268
   __TEXT.__eh_frame: 0x6d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x105f0
+  __DATA_CONST.__const: 0x10658
   __DATA_CONST.__objc_classlist: 0x1688
   __DATA_CONST.__objc_catlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b3d8
+  __DATA_CONST.__objc_selrefs: 0x1b4a8
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x1278
+  __DATA_CONST.__objc_superrefs: 0x1280
   __DATA_CONST.__objc_arraydata: 0x2e58
   __DATA_CONST.__got: 0x3510
-  __AUTH_CONST.__const: 0x36d8
-  __AUTH_CONST.__cfstring: 0x2b820
-  __AUTH_CONST.__objc_const: 0x56850
-  __AUTH_CONST.__objc_intobj: 0x4ba8
+  __AUTH_CONST.__const: 0x3738
+  __AUTH_CONST.__cfstring: 0x2c300
+  __AUTH_CONST.__objc_const: 0x56920
+  __AUTH_CONST.__objc_intobj: 0x4bc0
   __AUTH_CONST.__objc_arrayobj: 0xfc0
   __AUTH_CONST.__objc_doubleobj: 0xbe0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x12f0
-  __AUTH.__objc_data: 0x1ad0
-  __DATA.__objc_ivar: 0x28dc
-  __DATA.__data: 0x2dc8
+  __AUTH.__objc_data: 0x1b20
+  __DATA.__objc_ivar: 0x28ec
+  __DATA.__data: 0x2dd0
   __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_ivar: 0x1278
-  __DATA_DIRTY.__objc_data: 0xc7b0
+  __DATA_DIRTY.__objc_ivar: 0x1274
+  __DATA_DIRTY.__objc_data: 0xc760
   __DATA_DIRTY.__data: 0x7d8
-  __DATA_DIRTY.__bss: 0x238
+  __DATA_DIRTY.__bss: 0x258
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21965
-  Symbols:   45721
-  CStrings:  16306
+  Functions: 22020
+  Symbols:   45813
+  CStrings:  16422
 
Symbols:
+ +[RTBluePOIMonitor archivePendingObservations:]
+ +[RTBluePOIMonitor pendingObservationsFromArchivedData:]
+ +[RTBluePOIMonitorPendingObservation supportsSecureCoding]
+ +[RTPersistenceDriver(EntityCountMetrics) _dayCalendar]
+ +[RTPersistenceDriver(EntityCountMetrics) _history:containsDay:forAllEntities:]
+ +[RTPersistenceDriver(EntityCountMetrics) _historyByAppendingCount:forDay:intoHistory:]
+ +[RTPersistenceDriver(EntityCountMetrics) _payloadFromHistory:trackedEntities:todayStartOfDay:]
+ +[RTPersistenceDriver(EntityCountMetrics) _trackedEntities]
+ -[RTBluePOIMonitor _pendingObservationForPOIMuid:]
+ -[RTBluePOIMonitor _persistPendingObservations]
+ -[RTBluePOIMonitor _purgeDepartedPendingObservationsFromLocation:]
+ -[RTBluePOIMonitor _shutdownWithHandler:]
+ -[RTBluePOIMonitor _unconfirmedPendingPOIMuids]
+ -[RTBluePOIMonitor _updatePendingObservationsForEstimate:]
+ -[RTBluePOIMonitor hasSignificantChangeOnPOIEstimate:fromPOIEstimate:]
+ -[RTBluePOIMonitor pendingObservations]
+ -[RTBluePOIMonitor setPendingObservations:]
+ -[RTBluePOIMonitor shouldPostUpdateOnPOIEstimate:fromPOIEstimate:significantChange:]
+ -[RTBluePOIMonitorPendingObservation .cxx_destruct]
+ -[RTBluePOIMonitorPendingObservation confirmed]
+ -[RTBluePOIMonitorPendingObservation encodeWithCoder:]
+ -[RTBluePOIMonitorPendingObservation firstSeen]
+ -[RTBluePOIMonitorPendingObservation initWithCoder:]
+ -[RTBluePOIMonitorPendingObservation initWithPOIMuid:firstSeen:referenceLocation:]
+ -[RTBluePOIMonitorPendingObservation poiMuid]
+ -[RTBluePOIMonitorPendingObservation referenceLocation]
+ -[RTBluePOIMonitorPendingObservation setConfirmed:]
+ -[RTBluePOITileManager categoryIdStringsForMuids:handler:]
+ -[RTBluePOITileStore _fetchBluePOICategoryIdStringsForMuids:handler:]
+ -[RTBluePOITileStore fetchBluePOICategoryIdStringsForMuids:handler:]
+ -[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:limit:handler:]
+ -[RTLearnedLocationManager _fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]
+ -[RTLearnedLocationManager _visitFromLearnedVisit:learnedLOI:finerGranularityInferredMapItem:]
+ -[RTLearnedLocationManager fetchHindsightVisitsWithOptions:handler:]
+ -[RTLearnedLocationManager fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]
+ -[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]
+ -[RTLearnedLocationStore _fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]
+ -[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:]
+ -[RTLearnedLocationStore fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]
+ -[RTLearnedLocationStore fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]
+ -[RTLearnedLocationStore fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:]
+ -[RTPersistenceDriver(EntityCountMetrics) _persistEntityCountHistory:]
+ -[RTPersistenceDriver(EntityCountMetrics) _persistedEntityCountHistory]
+ -[RTPersistenceDriver(EntityCountMetrics) _recordDailyEntityCounts]
+ -[RTPersistenceDriver(EntityCountMetrics) submitDailyEntityCountMetrics]
+ -[RTPersistenceDriver(Metrics) _onDailyMetricsNotification:]
+ -[RTVisitConsolidator _fetchHindsightVisitsWithOptions:handler:]
+ -[RTVisitManager _processVisitsLabeling:error:]
+ -[RTWiFiManager _setup]
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table224
+ GCC_except_table246
+ GCC_except_table252
+ GCC_except_table271
+ GCC_except_table304
+ GCC_except_table345
+ GCC_except_table377
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table86
+ _OBJC_CLASS_$_RTBluePOIMonitorPendingObservation
+ _OBJC_IVAR_$_RTBluePOIMonitorPendingObservation._confirmed
+ _OBJC_IVAR_$_RTBluePOIMonitorPendingObservation._firstSeen
+ _OBJC_IVAR_$_RTBluePOIMonitorPendingObservation._poiMuid
+ _OBJC_IVAR_$_RTBluePOIMonitorPendingObservation._referenceLocation
+ _OBJC_METACLASS_$_RTBluePOIMonitorPendingObservation
+ _RTAnalyticsEventPersistenceEntityCountDaily
+ _RTApplicationManagerExecutableLivTipsd
+ __OBJC_$_CLASS_METHODS_RTBluePOIMonitor
+ __OBJC_$_CLASS_METHODS_RTBluePOIMonitorPendingObservation
+ __OBJC_$_CLASS_METHODS_RTPersistenceDriver(Metrics|EntityCountMetrics)
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOIMonitorPendingObservation
+ __OBJC_$_INSTANCE_METHODS_RTBluePOIMonitorPendingObservation
+ __OBJC_$_INSTANCE_METHODS_RTPersistenceDriver(Metrics|EntityCountMetrics)
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOIMonitorPendingObservation
+ __OBJC_$_PROP_LIST_RTBluePOIMonitorPendingObservation
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOIMonitorPendingObservation
+ __OBJC_CLASS_PROTOCOLS_$_RTPersistenceDriver(Metrics|EntityCountMetrics)
+ __OBJC_CLASS_RO_$_RTBluePOIMonitorPendingObservation
+ __OBJC_METACLASS_RO_$_RTBluePOIMonitorPendingObservation
+ ___106-[RTLearnedLocationStore fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke
+ ___107-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke
+ ___107-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke_2
+ ___23-[RTWiFiManager _setup]_block_invoke
+ ___47-[RTPersistenceDriver _onDataProtectionChange:]_block_invoke
+ ___47-[RTVisitManager _processVisitsLabeling:error:]_block_invoke
+ ___55+[RTPersistenceDriver(EntityCountMetrics) _dayCalendar]_block_invoke
+ ___58-[RTBluePOITileManager categoryIdStringsForMuids:handler:]_block_invoke
+ ___59+[RTPersistenceDriver(EntityCountMetrics) _trackedEntities]_block_invoke
+ ___59-[RTPersistenceDriver(Metrics) onDailyMetricsNotification:]_block_invoke
+ ___64-[RTVisitConsolidator _fetchHindsightVisitsWithOptions:handler:]_block_invoke
+ ___64-[RTVisitConsolidator _fetchHindsightVisitsWithOptions:handler:]_block_invoke_2
+ ___68-[RTBluePOITileStore fetchBluePOICategoryIdStringsForMuids:handler:]_block_invoke
+ ___68-[RTLearnedLocationManager fetchHindsightVisitsWithOptions:handler:]_block_invoke
+ ___69-[RTBluePOITileStore _fetchBluePOICategoryIdStringsForMuids:handler:]_block_invoke
+ ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke_2
+ ___87+[RTPersistenceDriver(EntityCountMetrics) _historyByAppendingCount:forDay:intoHistory:]_block_invoke
+ ___91-[RTLearnedLocationStore fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]_block_invoke
+ ___92-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]_block_invoke
+ ___92-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]_block_invoke_2
+ ___92-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:]_block_invoke_3
+ ___95-[RTLearnedLocationStore fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]_block_invoke
+ ___96-[RTLearnedLocationStore _fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]_block_invoke
+ ___96-[RTLearnedLocationStore _fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]_block_invoke_2
+ ___97-[RTLearnedLocationManager fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:]_block_invoke
+ ___98-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke
+ ___98-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke_2
+ ___98-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:limit:handler:]_block_invoke_3
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e36_v32?0"NSUUID"8"RTMapItemMO"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"RTLearnedLocationOfInterest"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e31_v32?0"NSUUID"8"NSUUID"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48bs_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e29_v24?0"NSArray"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e34_v24?0"NSDictionary"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72bs80w_e5_v8?0lw80l8s72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _objc_msgSend$_dayCalendar
+ _objc_msgSend$_fetchBluePOICategoryIdStringsForMuids:handler:
+ _objc_msgSend$_fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:
+ _objc_msgSend$_fetchHindsightVisitsBetweenStartDate:endDate:ascending:limit:handler:
+ _objc_msgSend$_fetchHindsightVisitsWithOptions:handler:
+ _objc_msgSend$_fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:
+ _objc_msgSend$_fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:
+ _objc_msgSend$_history:containsDay:forAllEntities:
+ _objc_msgSend$_historyByAppendingCount:forDay:intoHistory:
+ _objc_msgSend$_payloadFromHistory:trackedEntities:todayStartOfDay:
+ _objc_msgSend$_pendingObservationForPOIMuid:
+ _objc_msgSend$_persistEntityCountHistory:
+ _objc_msgSend$_persistPendingObservations
+ _objc_msgSend$_persistedEntityCountHistory
+ _objc_msgSend$_processVisitsLabeling:error:
+ _objc_msgSend$_purgeDepartedPendingObservationsFromLocation:
+ _objc_msgSend$_recordDailyEntityCounts
+ _objc_msgSend$_trackedEntities
+ _objc_msgSend$_unconfirmedPendingPOIMuids
+ _objc_msgSend$_updatePendingObservationsForEstimate:
+ _objc_msgSend$_visitFromLearnedVisit:learnedLOI:finerGranularityInferredMapItem:
+ _objc_msgSend$archivePendingObservations:
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$fetchBluePOICategoryIdStringsForMuids:handler:
+ _objc_msgSend$fetchFinerGranularityInferredMapItemsForVisitIdentifiers:handler:
+ _objc_msgSend$fetchHindsightVisitsWithOptions:handler:
+ _objc_msgSend$fetchLocationOfInterestIdentifiersForPlaceMapItemIdentifiers:handler:
+ _objc_msgSend$fetchLocationsOfInterestVisitedBetweenStartDate:endDate:ascending:limit:handler:
+ _objc_msgSend$firstSeen
+ _objc_msgSend$hasSignificantChangeOnPOIEstimate:fromPOIEstimate:
+ _objc_msgSend$initWithPOIMuid:firstSeen:referenceLocation:
+ _objc_msgSend$pendingObservations
+ _objc_msgSend$pendingObservationsFromArchivedData:
+ _objc_msgSend$poiMuid
+ _objc_msgSend$setPendingObservations:
+ _objc_msgSend$shouldPostUpdateOnPOIEstimate:fromPOIEstimate:significantChange:
+ _objc_msgSend$submitDailyEntityCountMetrics
+ _objc_msgSend$timeZoneForSecondsFromGMT:
- -[RTBluePOIMonitor shouldPostUpdateOnPOIEstimate:fromPOIEstimate:]
- -[RTBluePOITileManager categoryIdStringForMuid:handler:]
- -[RTBluePOITileStore _fetchBluePOICategoryIdStringForMuid:handler:]
- -[RTBluePOITileStore fetchBluePOICategoryIdStringForMuid:handler:]
- -[RTHealthKitManager _onNewWorkoutForSMSuggestionsNotification]
- -[RTHealthKitManager listenForNewWorkoutsForSMSuggestionsEnabled]
- -[RTHealthKitManager onNewWorkoutForSMSuggestionsNotification]
- -[RTHealthKitManager setListenForNewWorkoutsForSMSuggestionsEnabled:]
- -[RTHealthKitManager setTheNewWorkoutsForSMSuggestionsQuery:]
- -[RTHealthKitManager theNewWorkoutsForSMSuggestionsQuery]
- -[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]
- -[RTLearnedLocationManager _visitFromLearnedVisit:learnedLOI:handler:]
- -[RTVisitConsolidator _fetchHindsightVisitsWithDateInterval:ascending:handler:]
- GCC_except_table155
- GCC_except_table179
- GCC_except_table181
- GCC_except_table197
- GCC_except_table207
- GCC_except_table221
- GCC_except_table243
- GCC_except_table244
- GCC_except_table268
- GCC_except_table274
- GCC_except_table285
- GCC_except_table298
- GCC_except_table324
- GCC_except_table356
- GCC_except_table434
- GCC_except_table442
- _OBJC_CLASS_$_RTHealthKitManagerNewWorkoutForSMSuggestionsNotification
- _OBJC_METACLASS_$_RTHealthKitManagerNewWorkoutForSMSuggestionsNotification
- _RTApplicationManagerBundleIdLivTips
- __OBJC_$_CLASS_METHODS_RTPersistenceDriver
- __OBJC_$_INSTANCE_METHODS_RTPersistenceDriver(Metrics)
- __OBJC_CLASS_PROTOCOLS_$_RTPersistenceDriver(Metrics)
- __OBJC_CLASS_RO_$_RTHealthKitManagerNewWorkoutForSMSuggestionsNotification
- __OBJC_METACLASS_RO_$_RTHealthKitManagerNewWorkoutForSMSuggestionsNotification
- ___21-[RTWiFiManager init]_block_invoke
- ___56-[RTBluePOITileManager categoryIdStringForMuid:handler:]_block_invoke
- ___62-[RTHealthKitManager onNewWorkoutForSMSuggestionsNotification]_block_invoke
- ___66-[RTBluePOITileStore fetchBluePOICategoryIdStringForMuid:handler:]_block_invoke
- ___67-[RTBluePOITileStore _fetchBluePOICategoryIdStringForMuid:handler:]_block_invoke
- ___70-[RTLearnedLocationManager _visitFromLearnedVisit:learnedLOI:handler:]_block_invoke
- ___70-[RTLearnedLocationManager _visitFromLearnedVisit:learnedLOI:handler:]_block_invoke_2
- ___79-[RTVisitConsolidator _fetchHindsightVisitsWithDateInterval:ascending:handler:]_block_invoke
- ___79-[RTVisitConsolidator _fetchHindsightVisitsWithDateInterval:ascending:handler:]_block_invoke_2
- ___92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke
- ___92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke_2
- ___92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke_3
- ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSString"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48s56s_e29_v24?0"RTVisit"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___block_descriptor_72_e8_32s40s48bs56w_e39_v24?0"RTInferredMapItem"8"NSError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_73_e8_32s40s48bs56w_e29_v24?0"NSArray"8"NSError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72w_e5_v8?0lw72l8s64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_89_e8_32s40s48s56s64bs72w_e5_v8?0lw72l8s64l8s32l8s40l8s48l8s56l8
- _kRTNewWorkoutForSMSuggestionsNotification
- _objc_msgSend$_fetchBluePOICategoryIdStringForMuid:handler:
- _objc_msgSend$_fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:
- _objc_msgSend$_fetchHindsightVisitsWithDateInterval:ascending:handler:
- _objc_msgSend$_onNewWorkoutForSMSuggestionsNotification
- _objc_msgSend$_visitFromLearnedVisit:learnedLOI:handler:
- _objc_msgSend$fetchBluePOICategoryIdStringForMuid:handler:
- _objc_msgSend$listenForNewWorkoutsForSMSuggestionsEnabled
- _objc_msgSend$onNewWorkoutForSMSuggestionsNotification
- _objc_msgSend$setListenForNewWorkoutsForSMSuggestionsEnabled:
- _objc_msgSend$shouldPostUpdateOnPOIEstimate:fromPOIEstimate:
CStrings:
+ "\""
+ "%@, CM labeling complete, batched, %lu, batch_resolved, %lu, individual_fallback, %lu"
+ "%@, CONFIRMED, muid, %lu, age, %.0fs"
+ "%@, DEPARTED, muid with nil location, %lu"
+ "%@, DEPARTED, muid, %lu, distance, %.0fm"
+ "%@, FIRST SEEN, muid, %lu, firstSeen, %@"
+ "%@, WAITING, muid, %lu, age, %.0fs"
+ "%@, batch LOI lookup failed, error, %@"
+ "%@, batch LOI lookup timed out"
+ "%@, batch LOI lookup, requested, %lu, resolved, %lu"
+ "%@, batch fetch POI categories error, %@"
+ "%@, batch fetch POI categories timed out, muids count, %lu, error, %@"
+ "%@, batch fetch POI categories, requested, %lu, resolved, %lu"
+ "%@, batched LOI lookup, requested, %lu, returned, %lu, error, %@"
+ "%@, batched finer-granularity fetch failed, building visits without finer-granularity, error, %@"
+ "%@, batched map item fetch failed, returning empty result, error, %@"
+ "%@, batched visit fetch failed, returning empty result, error, %@"
+ "%@, batched visit fetch, requested, %lu, returned, %lu, error, %@"
+ "%@, didConfirmPOI, %@, pending, %lu"
+ "%@, failed to archive %lu pending observations, %@"
+ "%@, failed to decode pending observations, %@"
+ "%@, identifier fast path hit, skipping bounding-box scan"
+ "%@, individual LOI lookup failed, visit, %{sensitive}@, error, %@"
+ "%@, individual LOI lookup timed out, visit, %{sensitive}@"
+ "%@, individual LOI lookup, visit, %{sensitive}@, LOI, %{sensitive}@"
+ "%@, mapItem has nil identifier, falling back to individual LOI lookup, visit, %{sensitive}@"
+ "%@, muids count, %lu, results count, %lu, error, %@"
+ "%@, primary AOI label, %{sensitive}@, is not from a high confidence source; re-fusing %lu POI candidate(s) to find a POI primary label, visit, %{sensitive}@"
+ "%@, purge departed pending (>%.0fm), muids, %@, %lu -> %lu"
+ "%@, replacing primary AOI label with POI label, %{sensitive}@, visit, %{sensitive}@"
+ "%@, store unavailable for batched finer-granularity fetch, error, %@"
+ "%@,NSNotFound counting %@; skipping"
+ "%@,error counting %@,%@"
+ "%@,failed to decode entity count history,%@"
+ "%@,failed to encode entity count history,%@"
+ "%@,no managed object context available; deferring entity count capture"
+ "%@.%@.accountManager"
+ "%@.%@.altimeter"
+ "%@.%@.assetManager"
+ "%@.%@.authorization"
+ "%@.%@.authorizedLocation"
+ "%@.%@.bluePOIMapItemAndMonitor"
+ "%@.%@.bluePOIStores"
+ "%@.%@.bluePOITileManager"
+ "%@.%@.buildingPolygon"
+ "%@.%@.clientListener"
+ "%@.%@.companionAndLocationContext"
+ "%@.%@.contacts"
+ "%@.%@.dataIntegrity"
+ "%@.%@.dataProtection"
+ "%@.%@.deviceLocationPredictor"
+ "%@.%@.diagnostics"
+ "%@.%@.eventAgentAndTripSegmentProvider"
+ "%@.%@.eventModelProvider"
+ "%@.%@.fingerprint"
+ "%@.%@.fuserAndPortrait"
+ "%@.%@.healthKitAndElevation"
+ "%@.%@.hintAndAppClip"
+ "%@.%@.hintAndVehicleLocation"
+ "%@.%@.inertialData"
+ "%@.%@.initializeContainer"
+ "%@.%@.initiatorService"
+ "%@.%@.intermittentGNSS"
+ "%@.%@.internalListener"
+ "%@.%@.keychain"
+ "%@.%@.learnedLocationEngine"
+ "%@.%@.learnedLocationManager"
+ "%@.%@.learnedLocationStore"
+ "%@.%@.learnedPlaceTypeAndReconcilers"
+ "%@.%@.locationAwareness"
+ "%@.%@.locationManager"
+ "%@.%@.locationStore"
+ "%@.%@.mapServices"
+ "%@.%@.metricManager"
+ "%@.%@.mirroringManager"
+ "%@.%@.motionAndVehicle"
+ "%@.%@.navCameraEvent"
+ "%@.%@.networkOfInterest"
+ "%@.%@.peopleDiscovery"
+ "%@.%@.persistenceCtors"
+ "%@.%@.persistenceDriverStart"
+ "%@.%@.placeInferenceManager"
+ "%@.%@.placeInferenceStores"
+ "%@.%@.poiSamplerAndCuration"
+ "%@.%@.pointOfInterestMonitor"
+ "%@.%@.predictedContext"
+ "%@.%@.purgeManager"
+ "%@.%@.reachability"
+ "%@.%@.receiverAndSMClient"
+ "%@.%@.scenarioTrigger"
+ "%@.%@.signalHandlers"
+ "%@.%@.starkAndBattery"
+ "%@.%@.suggestionsManager"
+ "%@.%@.transitMetricAndBiome"
+ "%@.%@.tripClusterManager"
+ "%@.%@.tripClusterStores"
+ "%@.%@.uptimeMetrics"
+ "%@.%@.visitConsolidator"
+ "%@.%@.visitManager"
+ "%@.%@.walletTxnAndVisitStore"
+ "%@.%@.wifi"
+ "%@.%@.workout"
+ "%@.%@.xpcActivityManager"
+ "%@.%@.xpcEventStreams"
+ "%@.%@.zelkovaLocationManager"
+ "%@.%@.zelkovaSuggestionsHelper"
+ "%@.%@.zelkovaWristAndStores"
+ "%@CountDay%ld"
+ "-[RTPersistenceDriver(Metrics) _onDailyMetricsNotification:]"
+ "06:38:08"
+ "BluePOIMonitorPendingObservations"
+ "CoreRoutine.PersistenceEntityCountDaily"
+ "Jul 11 2026"
+ "RTDefaultsPersistenceEntityCountHistory"
+ "class"
+ "confirmed"
+ "fetched %lu LOIs for visits between start date, %@, end date, %@, limit, %@, error, %@"
+ "fetched %lu hindsight visits, dateInterval, %@, limit, %@, error, %@"
+ "finerGranularityMapItemSource"
+ "firstSeen"
+ "keyPrefix"
+ "learnedLocationOfInterest"
+ "learnedPlace"
+ "learnedVisit"
+ "livtipsd"
+ "place_source_CurrentLocation"
+ "place_source_CurrentPOI"
+ "place_source_LocalBluePOI"
+ "place_source_POIHistorySynced"
+ "place_source_Wallet"
+ "poiMuid"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "v32@?0@\"NSUUID\"8@\"NSUUID\"16^B24"
+ "v32@?0@\"NSUUID\"8@\"RTMapItemMO\"16^B24"
- "%@, %@, No active listeners for Workout Notification For SM Suggestions. Hence skipping the notification"
- "%@, %@, Posting New Workout Notification For SM Suggestions"
- "%@, %@, received workout notification for new workout, %@"
- "%@, LOI lookup failed, visit, %{sensitive}@, error, %@"
- "%@, LOI lookup timed out, visit, %{sensitive}@"
- "%@, fetch POI categories, requested, %lu, resolved, %lu"
- "%@, fetch POI category error, muid, %llu, error, %@"
- "%@, fetch POI category timed out, muid, %llu"
- "%@, muid, %llu, results count, %lu, category string, %@, error, %@"
- "%@, visit, %{sensitive}@, LOI, %{sensitive}@"
- "-[RTPersistenceDriver(Metrics) onDailyMetricsNotification:]"
- "02:54:25"
- "An error, %@, has occurred when fetching the fetchFinerGranularityInferredMapItem for visit, %{sensitive}@"
- "Jun 28 2026"
- "RTHealthKitManagerObservedNewWorkoutForSMSuggestions"
- "com.apple.LivTips"
- "fetched %lu LOIs for visits between start date, %@, end date, %@, error, %@"
- "fetched %lu hindsight visits in date interval, %@, error, %@"
```
