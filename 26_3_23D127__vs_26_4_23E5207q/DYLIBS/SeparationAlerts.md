## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.12.0.1
-  __TEXT.__text: 0x2f8f4
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x37fc
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x15bc
-  __TEXT.__oslogstring: 0x6de4
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__unwind_info: 0x7f0
-  __TEXT.__objc_classname: 0x5c5
-  __TEXT.__objc_methname: 0x8fc4
-  __TEXT.__objc_methtype: 0x1154
-  __TEXT.__objc_stubs: 0x67e0
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0x100
+107.0.12.0.3
+  __TEXT.__text: 0x36cf8
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x3aa4
+  __TEXT.__const: 0x118
+  __TEXT.__oslogstring: 0x7d16
+  __TEXT.__cstring: 0x1958
+  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__unwind_info: 0xb98
+  __TEXT.__objc_classname: 0x5fd
+  __TEXT.__objc_methname: 0x9d00
+  __TEXT.__objc_methtype: 0x127f
+  __TEXT.__objc_stubs: 0x70a0
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e18
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x21a0
-  __AUTH_CONST.__objc_const: 0x5398
-  __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH.__objc_data: 0x140
+  __DATA_CONST.__objc_selrefs: 0x2070
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x22e0
+  __AUTH_CONST.__objc_const: 0x56e8
+  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x42c
-  __DATA.__data: 0xba0
+  __DATA.__objc_ivar: 0x460
+  __DATA.__data: 0xc00
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 826690AA-9258-33A6-A269-9D2CD4BEE890
-  Functions: 1019
-  Symbols:   3776
-  CStrings:  2502
+  UUID: 83A85D4C-58DB-3969-894B-3AD766CDD422
+  Functions: 1079
+  Symbols:   4003
+  CStrings:  2670
 
Symbols:
+ +[SAFamiliarityManager dateIntervalForLookback:]
+ -[SAFamiliarityManager .cxx_destruct]
+ -[SAFamiliarityManager familiarityIndexRequester]
+ -[SAFamiliarityManager finalizeAssessmentWithRecentScore:historicalScore:]
+ -[SAFamiliarityManager handleFamiliarityIndexEvent:]
+ -[SAFamiliarityManager handleLocationOfInterestEvent:]
+ -[SAFamiliarityManager handleVisitEvent:]
+ -[SAFamiliarityManager hasPendingLongLookback]
+ -[SAFamiliarityManager hasPendingShortLookback]
+ -[SAFamiliarityManager ingestTAEvent:]
+ -[SAFamiliarityManager initWithFamiliarityIndexRequester:]
+ -[SAFamiliarityManager lastVisitHistoricalFamiliarity]
+ -[SAFamiliarityManager lastVisitHistoricalScore]
+ -[SAFamiliarityManager lastVisitRecentFamiliarity]
+ -[SAFamiliarityManager lastVisitRecentScore]
+ -[SAFamiliarityManager pendingHistoricalScore]
+ -[SAFamiliarityManager pendingRecentScore]
+ -[SAFamiliarityManager pendingRequestLocation]
+ -[SAFamiliarityManager requestFamiliarityIndexForLocation:]
+ -[SAFamiliarityManager setFamiliarityIndexRequester:]
+ -[SAFamiliarityManager setHasPendingLongLookback:]
+ -[SAFamiliarityManager setHasPendingShortLookback:]
+ -[SAFamiliarityManager setLastVisitHistoricalScore:]
+ -[SAFamiliarityManager setLastVisitRecentScore:]
+ -[SAFamiliarityManager setPendingHistoricalScore:]
+ -[SAFamiliarityManager setPendingRecentScore:]
+ -[SAFamiliarityManager setPendingRequestLocation:]
+ -[SAMonitoringSessionManager btHintCountDuringTravelForDeviceUUID:]
+ -[SAMonitoringSessionManager calculateDistanceToHome:]
+ -[SAMonitoringSessionManager currentTAPredictedContexts]
+ -[SAMonitoringSessionManager deviceUUIDtoBTHintCountDuringTravel]
+ -[SAMonitoringSessionManager familiarityManager]
+ -[SAMonitoringSessionManager findMatchingPredictedContextForLocation:withRadiusMeters:]
+ -[SAMonitoringSessionManager getSecondsUntilReturnToPredictedContext:]
+ -[SAMonitoringSessionManager handleNewTAPredictedContext:]
+ -[SAMonitoringSessionManager initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:familiarityManager:]
+ -[SAMonitoringSessionManager lastKnownHomeLOI]
+ -[SAMonitoringSessionManager secondsToActualReturnFromAlertLocation:toReunionLocation:withTimeToReunion:]
+ -[SAMonitoringSessionManager setCurrentTAPredictedContexts:]
+ -[SAMonitoringSessionManager setDeviceUUIDtoBTHintCountDuringTravel:]
+ -[SAMonitoringSessionManager setFamiliarityManager:]
+ -[SAMonitoringSessionManager setLastKnownHomeLOI:]
+ -[SAMonitoringSessionManager trackBTHintUsageDuringTravelingSessions:]
+ -[SAService familiarityManager]
+ -[SAService requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:]
+ -[SAService setFamiliarityManager:]
+ -[SAServiceManager _fetchAndIngestHomeLocation]
+ -[SAServiceManager _ingestPredictedContexts:]
+ -[SAServiceManager _startMonitoringAndIngestingPredictedContexts]
+ -[SAServiceManager _stopMonitoringPredictedContexts]
+ -[SAServiceManager separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:]
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_RTFamiliarityIndexOptions
+ _OBJC_CLASS_$_RTLocation
+ _OBJC_CLASS_$_RTPredictedContextLocation
+ _OBJC_CLASS_$_RTPredictedContextOptions
+ _OBJC_CLASS_$_SAFamiliarityManager
+ _OBJC_CLASS_$_TAFamiliarityIndexEvent
+ _OBJC_CLASS_$_TAPredictedContext
+ _OBJC_IVAR_$_SAFamiliarityManager._familiarityIndexRequester
+ _OBJC_IVAR_$_SAFamiliarityManager._hasPendingLongLookback
+ _OBJC_IVAR_$_SAFamiliarityManager._hasPendingShortLookback
+ _OBJC_IVAR_$_SAFamiliarityManager._lastVisitHistoricalScore
+ _OBJC_IVAR_$_SAFamiliarityManager._lastVisitRecentScore
+ _OBJC_IVAR_$_SAFamiliarityManager._pendingHistoricalScore
+ _OBJC_IVAR_$_SAFamiliarityManager._pendingRecentScore
+ _OBJC_IVAR_$_SAFamiliarityManager._pendingRequestLocation
+ _OBJC_IVAR_$_SAMonitoringSessionManager._currentTAPredictedContexts
+ _OBJC_IVAR_$_SAMonitoringSessionManager._deviceUUIDtoBTHintCountDuringTravel
+ _OBJC_IVAR_$_SAMonitoringSessionManager._familiarityManager
+ _OBJC_IVAR_$_SAMonitoringSessionManager._lastKnownHomeLOI
+ _OBJC_IVAR_$_SAService._familiarityManager
+ _OBJC_METACLASS_$_SAFamiliarityManager
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _TALocationOfInterestTypeToString
+ __OBJC_$_CLASS_METHODS_SAFamiliarityManager
+ __OBJC_$_INSTANCE_METHODS_SAFamiliarityManager
+ __OBJC_$_INSTANCE_VARIABLES_SAFamiliarityManager
+ __OBJC_$_PROP_LIST_SAFamiliarityManager
+ __OBJC_$_PROP_LIST_SATravelTypeClassifierServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAFamiliarityIndexRequestProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAFamiliarityIndexRequestProtocol
+ __OBJC_CLASS_RO_$_SAFamiliarityManager
+ __OBJC_LABEL_PROTOCOL_$_SAFamiliarityIndexRequestProtocol
+ __OBJC_METACLASS_RO_$_SAFamiliarityManager
+ __OBJC_PROTOCOL_$_SAFamiliarityIndexRequestProtocol
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__117__floyd_sift_downB9foe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE8pop_backB9foe210106Ev
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB9foe210106ERU8__strongKS2_
+ __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___118-[SAServiceManager separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:]_block_invoke
+ ___118-[SAServiceManager separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:]_block_invoke_2
+ ___44-[SAServiceManager _fetchAndIngestLastVisit]_block_invoke.58
+ ___44-[SAServiceManager _fetchAndIngestLastVisit]_block_invoke_2.59
+ ___47-[SAServiceManager _fetchAndIngestHomeLocation]_block_invoke
+ ___47-[SAServiceManager _fetchAndIngestHomeLocation]_block_invoke_2
+ ___52-[SAServiceManager _stopMonitoringPredictedContexts]_block_invoke
+ ___65-[SAServiceManager _startMonitoringAndIngestingPredictedContexts]_block_invoke
+ ___65-[SAServiceManager _startMonitoringAndIngestingPredictedContexts]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40s_e46_v24?0"RTPredictedContextResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_fetchAndIngestHomeLocation
+ _objc_msgSend$_ingestPredictedContexts:
+ _objc_msgSend$_startMonitoringAndIngestingPredictedContexts
+ _objc_msgSend$_stopMonitoringPredictedContexts
+ _objc_msgSend$calculateDistanceToHome:
+ _objc_msgSend$contextProbability
+ _objc_msgSend$currentTAPredictedContexts
+ _objc_msgSend$dateInterval
+ _objc_msgSend$dateIntervalForLookback:
+ _objc_msgSend$deviceUUIDtoBTHintCountDuringTravel
+ _objc_msgSend$distantFuture
+ _objc_msgSend$endDate
+ _objc_msgSend$error
+ _objc_msgSend$familiarityIndex
+ _objc_msgSend$familiarityIndexRequester
+ _objc_msgSend$familiarityManager
+ _objc_msgSend$familiarityScore
+ _objc_msgSend$fetchFamiliarityIndexResultsWithOptions:handler:
+ _objc_msgSend$fetchLocationsOfInterestOfType:withHandler:
+ _objc_msgSend$filterContextTypeMask
+ _objc_msgSend$finalizeAssessmentWithRecentScore:historicalScore:
+ _objc_msgSend$findMatchingPredictedContextForLocation:withRadiusMeters:
+ _objc_msgSend$getSecondsUntilReturnToPredictedContext:
+ _objc_msgSend$handleFamiliarityIndexEvent:
+ _objc_msgSend$handleLocationOfInterestEvent:
+ _objc_msgSend$handleNewTAPredictedContext:
+ _objc_msgSend$handleVisitEvent:
+ _objc_msgSend$hasPendingLongLookback
+ _objc_msgSend$hasPendingShortLookback
+ _objc_msgSend$initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:
+ _objc_msgSend$initWithFamiliarityIndex:dateInterval:lookbackInterval:referenceLocation:date:error:
+ _objc_msgSend$initWithFamiliarityIndexRequester:
+ _objc_msgSend$initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:
+ _objc_msgSend$initWithLatitude:longitude:creationDate:startDate:endDate:contextProbability:
+ _objc_msgSend$initWithLatitude:longitude:horizontalUncertainty:date:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:purpose:date:
+ _objc_msgSend$initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:familiarityManager:
+ _objc_msgSend$lastKnownHomeLOI
+ _objc_msgSend$lastVisitHistoricalFamiliarity
+ _objc_msgSend$lastVisitHistoricalScore
+ _objc_msgSend$lastVisitRecentFamiliarity
+ _objc_msgSend$lastVisitRecentScore
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$locationOfInterest
+ _objc_msgSend$lookbackInterval
+ _objc_msgSend$lookbackIntervalInWeeks
+ _objc_msgSend$nextStepPredictedContextsWithFilterMask:
+ _objc_msgSend$pendingHistoricalScore
+ _objc_msgSend$pendingRecentScore
+ _objc_msgSend$pendingRequestLocation
+ _objc_msgSend$probability
+ _objc_msgSend$purpose
+ _objc_msgSend$referenceLocation
+ _objc_msgSend$requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:
+ _objc_msgSend$requestFamiliarityIndexForLocation:
+ _objc_msgSend$secondsToActualReturnFromAlertLocation:toReunionLocation:withTimeToReunion:
+ _objc_msgSend$separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:
+ _objc_msgSend$setHasPendingLongLookback:
+ _objc_msgSend$setHasPendingShortLookback:
+ _objc_msgSend$setLastKnownHomeLOI:
+ _objc_msgSend$setLastVisitHistoricalScore:
+ _objc_msgSend$setLastVisitRecentScore:
+ _objc_msgSend$setPendingHistoricalScore:
+ _objc_msgSend$setPendingRecentScore:
+ _objc_msgSend$setPendingRequestLocation:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$startDate
+ _objc_msgSend$startMonitoringPredictedContextWithOptions:completionHandler:
+ _objc_msgSend$stopMonitoringPredictedContextWithHandler:
+ _objc_msgSend$trackBTHintUsageDuringTravelingSessions:
- -[SAMonitoringSessionManager initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:]
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE9push_backB8ne200100ERU8__strongKS2_
- __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___44-[SAServiceManager _fetchAndIngestLastVisit]_block_invoke.44
- ___44-[SAServiceManager _fetchAndIngestLastVisit]_block_invoke_2.45
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHp0ugDkj1Qy_PTM2oUMvx5IuOS6V2oeO8Ose38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHp0ugDkj1Qy_PTM2oUMvx5IuOS6V2oeO8Ose38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "@\"<SAFamiliarityIndexRequestProtocol>\""
+ "@\"SAFamiliarityManager\""
+ "@\"TALocationOfInterest\""
+ "@24@0:8d16"
+ "@28@0:8@16i24"
+ "@96@0:8@16@24@32@40@48@56@64@72@80@88"
+ "SAFamiliarityIndexRequestProtocol"
+ "SAFamiliarityManager"
+ "T@\"<SAFamiliarityIndexRequestProtocol>\",&,N,V_familiarityIndexRequester"
+ "T@\"CLLocation\",&,N,V_pendingRequestLocation"
+ "T@\"NSMutableArray\",&,N,V_currentTAPredictedContexts"
+ "T@\"NSMutableDictionary\",&,N,V_deviceUUIDtoBTHintCountDuringTravel"
+ "T@\"SAFamiliarityManager\",&,N,V_familiarityManager"
+ "T@\"TALocationOfInterest\",&,N,V_lastKnownHomeLOI"
+ "TB,N,V_hasPendingLongLookback"
+ "TB,N,V_hasPendingShortLookback"
+ "TQ,N"
+ "Td,N,V_lastVisitHistoricalScore"
+ "Td,N,V_lastVisitRecentScore"
+ "Td,N,V_pendingHistoricalScore"
+ "Td,N,V_pendingRecentScore"
+ "Vehicular - Motorcycle"
+ "_currentTAPredictedContexts"
+ "_deviceUUIDtoBTHintCountDuringTravel"
+ "_familiarityIndexRequester"
+ "_familiarityManager"
+ "_fetchAndIngestHomeLocation"
+ "_hasPendingLongLookback"
+ "_hasPendingShortLookback"
+ "_ingestPredictedContexts:"
+ "_lastKnownHomeLOI"
+ "_lastVisitHistoricalScore"
+ "_lastVisitRecentScore"
+ "_pendingHistoricalScore"
+ "_pendingRecentScore"
+ "_pendingRequestLocation"
+ "_startMonitoringAndIngestingPredictedContexts"
+ "_stopMonitoringPredictedContexts"
+ "actualLocationReturnTime"
+ "alertDistanceToHome"
+ "btHintCountDuringTravel"
+ "btHintCountDuringTravelForDeviceUUID:"
+ "calculateDistanceToHome:"
+ "contextProbability"
+ "currentTAPredictedContexts"
+ "d40@0:8@16@24d32"
+ "dateInterval"
+ "dateInterval.startDate.date"
+ "dateIntervalForLookback:"
+ "deviceUUIDtoBTHintCountDuringTravel"
+ "distanceToHome"
+ "distantFuture"
+ "endDate"
+ "error"
+ "familiarityIndex"
+ "familiarityIndexRequester"
+ "familiarityManager"
+ "familiarityScore"
+ "fetchFamiliarityIndexResultsWithOptions:handler:"
+ "fetchLocationsOfInterestOfType:withHandler:"
+ "filterContextTypeMask"
+ "finalizeAssessmentWithRecentScore:historicalScore:"
+ "findMatchingPredictedContextForLocation:withRadiusMeters:"
+ "getSecondsUntilReturnToPredictedContext:"
+ "handleFamiliarityIndexEvent:"
+ "handleLocationOfInterestEvent:"
+ "handleNewTAPredictedContext:"
+ "handleVisitEvent:"
+ "hasPendingLongLookback"
+ "hasPendingShortLookback"
+ "historicalFamiliarity"
+ "initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:"
+ "initWithFamiliarityIndex:dateInterval:lookbackInterval:referenceLocation:date:error:"
+ "initWithFamiliarityIndexRequester:"
+ "initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
+ "initWithLatitude:longitude:creationDate:startDate:endDate:contextProbability:"
+ "initWithLatitude:longitude:horizontalUncertainty:date:"
+ "initWithStartDate:endDate:"
+ "initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:purpose:date:"
+ "initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:familiarityManager:"
+ "lastKnownHomeLOI"
+ "lastVisitHistoricalFamiliarity"
+ "lastVisitHistoricalScore"
+ "lastVisitRecentFamiliarity"
+ "lastVisitRecentScore"
+ "localizedDescription"
+ "locationOfInterest"
+ "lookbackInterval"
+ "lookbackIntervalInWeeks"
+ "nextStepPredictedContextsWithFilterMask:"
+ "pendingHistoricalScore"
+ "pendingRecentScore"
+ "pendingRequestLocation"
+ "predictedLocationReturnTime"
+ "probability"
+ "purpose"
+ "recentFamiliarity"
+ "referenceLocation"
+ "requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:"
+ "requestFamiliarityIndexForLocation:"
+ "secondsToActualReturnFromAlertLocation:toReunionLocation:withTimeToReunion:"
+ "separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:"
+ "setCurrentTAPredictedContexts:"
+ "setDeviceUUIDtoBTHintCountDuringTravel:"
+ "setFamiliarityIndexRequester:"
+ "setFamiliarityManager:"
+ "setHasPendingLongLookback:"
+ "setHasPendingShortLookback:"
+ "setLastKnownHomeLOI:"
+ "setLastVisitHistoricalScore:"
+ "setLastVisitRecentScore:"
+ "setPendingHistoricalScore:"
+ "setPendingRecentScore:"
+ "setPendingRequestLocation:"
+ "sortDescriptorWithKey:ascending:"
+ "startDate"
+ "startMonitoringPredictedContextWithOptions:completionHandler:"
+ "stopMonitoringPredictedContextWithHandler:"
+ "trackBTHintUsageDuringTravelingSessions:"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"RTPredictedContextResult\"8@\"NSError\"16"
+ "v32@0:8d16d24"
+ "v48@0:8@\"NSDateInterval\"16d24@\"CLLocation\"32d40"
+ "v48@0:8@16d24@32d40"
+ "v56@0:8@\"SAService\"16@\"NSDateInterval\"24d32@\"CLLocation\"40d48"
+ "v56@0:8@16@24d32@40d48"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager LOI entry\", \"type\":\"%{private}s\", \"loi\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager familiarity index request failed\", \"dateIntervalStart\":\"%{private}@\", \"dateIntervalEnd\":\"%{private}@\", \"lookback_weeks\":%{private}ld, \"referenceLocation\":\"%{sensitive}@\", \"error\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager historical familiarity score\", \"dateIntervalStart\":\"%{private}@\", \"dateIntervalEnd\":\"%{private}@\", \"lookback\":%{private}ld, \"referenceLocation\":\"%{sensitive}@\", \"score\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager last visit familiarity\", \"score\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager not visit entry, skipping\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager received familiarity index event for different location\", \"distance\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager received familiarity index event with no pending request\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager recent familiarity score\", \"dateIntervalStart\":\"%{private}@\", \"dateIntervalEnd\":\"%{private}@\", \"lookback\":%{private}ld, \"referenceLocation\":\"%{sensitive}@\", \"score\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager result\", \"recentScore\":\"%{private}f\", \"historicalScore\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager skipping duplicate request for same location\", \"distance\":\"%{private}f\", \"hasPendingShort\":%{private}hhd, \"hasPendingLong\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager unrecognized lookback interval\", \"dateIntervalStart\":\"%{private}@\", \"dateIntervalEnd\":\"%{private}@\", \"lookback\":%{private}ld, \"referenceLocation\":\"%{sensitive}@\", \"score\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAFamiliarityManager visit entry\", \"visit\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager LOI for caching, not setting as current visit\", \"purpose\":%{private}ld, \"type\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager distance to home\", \"distanceMeters\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleNewTAPredictedContext processed events\", \"added\":%{private}lu, \"removed\":%{private}lu, \"total\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager incremented BT hint count during travel\", \"uuid\":\"%{private}@\", \"count\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager no home location available for distance calculation\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager reset BT hint count for new traveling session\", \"uuid\":\"%{private}@\", \"initialCount\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager updated last known home location\", \"lastKnownHomeLOI\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAScenarioClassifier LOI for caching, not creating unsafe location\", \"device\":\"%{private}@\", \"purpose\":%{private}ld, \"type\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#SAServiceManager error fetching home location\", \"error\":\"%{public}@\"}"
+ "{\"msg%{public}.0s\":\"#SAServiceManager fetching home location\"}"
+ "{\"msg%{public}.0s\":\"#SAServiceManager no home location available\"}"
+ "{\"msg%{public}.0s\":\"#SAServiceManager received home location\", \"loi\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:PLC error starting monitoring predicted contexts\", \"error\":\"%{public}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:PLC error stopping monitoring predicted contexts\", \"error\":\"%{public}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:PLC ingesting predicted contexts\", \"contextCount\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#manager:PLC not ingesting TAEvent as SA service is down\"}"
+ "{\"msg%{public}.0s\":\"#manager:PLC successfully stopped monitoring predicted contexts\"}"
+ "{\"msg%{public}.0s\":\"#sa Service requestFamiliarityIndexForLocation\", \"dateIntervalStart\":\"%{private}@\", \"dateIntervalEnd\":\"%{private}@\", \"weeks\":%{private}ld, \"location\":\"%{sensitive}@\", \"distance\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#sa ServiceMgr #familiarity nil location provided\"}"
- "\t"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "initWithWithYouDetector:fenceRequestServicer:fenceManager:travelTypeClassifier:clock:deviceRecord:analytics:persistenceManager:audioAccessoryManager:"

```
