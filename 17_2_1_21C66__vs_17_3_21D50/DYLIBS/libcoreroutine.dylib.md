## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-895.0.11.0.2
-  __TEXT.__text: 0x44f560
-  __TEXT.__auth_stubs: 0x1830
-  __TEXT.__objc_methlist: 0x223f0
-  __TEXT.__const: 0x1ab0
-  __TEXT.__gcc_except_tab: 0x16770
-  __TEXT.__oslogstring: 0x505fb
-  __TEXT.__cstring: 0x3347b
+896.0.1.0.1
+  __TEXT.__text: 0x4530e8
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_methlist: 0x22558
+  __TEXT.__const: 0x1ab8
+  __TEXT.__gcc_except_tab: 0x16b84
+  __TEXT.__oslogstring: 0x50f3c
+  __TEXT.__cstring: 0x33656
   __TEXT.__ustring: 0x16
   __TEXT.__dlopen_cstrs: 0x254
-  __TEXT.__unwind_info: 0xa69c
-  __TEXT.__objc_classname: 0x4452
-  __TEXT.__objc_methname: 0x6a089
-  __TEXT.__objc_methtype: 0xa3cd
-  __TEXT.__objc_stubs: 0x3fd00
-  __DATA_CONST.__got: 0xa50
-  __DATA_CONST.__const: 0xb690
-  __DATA_CONST.__objc_classlist: 0x1078
+  __TEXT.__unwind_info: 0xa6f8
+  __TEXT.__objc_classname: 0x4463
+  __TEXT.__objc_methname: 0x6a66f
+  __TEXT.__objc_methtype: 0xa3e3
+  __TEXT.__objc_stubs: 0x3fe20
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0xb6e0
+  __DATA_CONST.__objc_classlist: 0x1080
   __DATA_CONST.__objc_catlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x33268
-  __DATA_CONST.__objc_selrefs: 0x12570
-  __DATA_CONST.__objc_arraydata: 0x19c0
-  __AUTH_CONST.__const: 0x2600
-  __AUTH_CONST.__cfstring: 0x1f060
-  __AUTH_CONST.__objc_const: 0xda08
-  __AUTH_CONST.__objc_intobj: 0x2b98
+  __DATA_CONST.__objc_const: 0x334a0
+  __DATA_CONST.__objc_selrefs: 0x12648
+  __DATA_CONST.__objc_arraydata: 0x19c8
+  __AUTH_CONST.__const: 0x2620
+  __AUTH_CONST.__cfstring: 0x1f0c0
+  __AUTH_CONST.__objc_const: 0xda50
+  __AUTH_CONST.__objc_intobj: 0x2bb0
   __AUTH_CONST.__objc_doubleobj: 0x900
-  __AUTH_CONST.__objc_arrayobj: 0xba0
+  __AUTH_CONST.__objc_arrayobj: 0xbb8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xc28
-  __AUTH.__objc_data: 0x2080
+  __AUTH_CONST.__auth_got: 0xc38
+  __AUTH.__objc_data: 0x20d0
   __DATA.__objc_protorefs: 0x108
-  __DATA.__objc_classrefs: 0x1c58
-  __DATA.__objc_superrefs: 0xe28
-  __DATA.__objc_ivar: 0x1c1c
-  __DATA.__data: 0x2460
+  __DATA.__objc_classrefs: 0x1c60
+  __DATA.__objc_superrefs: 0xe30
+  __DATA.__objc_ivar: 0x1c38
+  __DATA.__data: 0x2468
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_ivar: 0xc04
+  __DATA_DIRTY.__objc_ivar: 0xc10
   __DATA_DIRTY.__objc_data: 0x8430
   __DATA_DIRTY.__data: 0x498
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A933A4A7-09E9-3980-B0B8-5F0895E111C8
-  Functions: 14939
-  Symbols:   48925
-  CStrings:  30089
+  UUID: 0B04E158-6B46-378B-9FAF-1CE62751EA39
+  Functions: 14974
+  Symbols:   49034
+  CStrings:  30170
 
Symbols:
+ -[NSArray(RTExtensions) shuffle]
+ -[RTAuthorizedLocation description]
+ -[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]
+ -[RTAuthorizedLocationManager isUnlockedSinceBoot]
+ -[RTAuthorizedLocationManager retroRegistrationAttemptCount]
+ -[RTAuthorizedLocationManager setIsUnlockedSinceBoot:]
+ -[RTAuthorizedLocationManager setRetroRegistrationAttemptCount:]
+ -[RTAuthorizedLocationManager trustedTimeCache]
+ -[RTAuthorizedLocationQueryMetrics description]
+ -[RTTrustedTimeCache cachedReferenceTimeCfatSeconds]
+ -[RTTrustedTimeCache cachedReferenceTimeMachContSeconds]
+ -[RTTrustedTimeCache cachedTrustedTimeCfatSeconds]
+ -[RTTrustedTimeCache cachedTrustedTimeMachContSeconds]
+ -[RTTrustedTimeCache getApproximateTrustedDateNowWithUnsecureFallback]
+ -[RTTrustedTimeCache getApproximateTrustedDateNow]
+ -[RTTrustedTimeCache init]
+ -[RTTrustedTimeCache machContinuousTimeSeconds]
+ -[RTTrustedTimeCache maxBoundReferenceTimeCfatSeconds]
+ -[RTTrustedTimeCache minBoundReferenceTimeCfatSeconds]
+ -[RTTrustedTimeCache setBoundsForReferenceTimeWithMinimumDate:maximumDate:]
+ -[RTTrustedTimeCache setCachedReferenceTimeCfatSeconds:]
+ -[RTTrustedTimeCache setCachedReferenceTimeMachContSeconds:]
+ -[RTTrustedTimeCache setCachedTrustedTimeCfatSeconds:]
+ -[RTTrustedTimeCache setCachedTrustedTimeMachContSeconds:]
+ -[RTTrustedTimeCache setMaxBoundReferenceTimeCfatSeconds:]
+ -[RTTrustedTimeCache setMinBoundReferenceTimeCfatSeconds:]
+ -[SMSessionMetricManager _gatherSessionDestinationStats:]
+ -[SMSessionMetricManager getLocationsForInterval:nearBoundingLocation:]
+ -[SMSessionMetricManager getRTLocationOfInterestForCLLocation:]
+ -[SMSessionMetricManager initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:]
+ -[SMSessionMetricManager locationManager]
+ -[SMSessionMetricManager setLocationManager:]
+ GCC_except_table71
+ GCC_except_table84
+ _OBJC_CLASS_$_RTTrustedTimeCache
+ _OBJC_IVAR_$_RTTrustedTimeCache._cachedReferenceTimeCfatSeconds
+ _OBJC_IVAR_$_RTTrustedTimeCache._cachedReferenceTimeMachContSeconds
+ _OBJC_IVAR_$_RTTrustedTimeCache._cachedTrustedTimeCfatSeconds
+ _OBJC_IVAR_$_RTTrustedTimeCache._cachedTrustedTimeMachContSeconds
+ _OBJC_IVAR_$_RTTrustedTimeCache._maxBoundReferenceTimeCfatSeconds
+ _OBJC_IVAR_$_RTTrustedTimeCache._minBoundReferenceTimeCfatSeconds
+ _OBJC_IVAR_$_SMSessionMetricManager._locationManager
+ _OBJC_METACLASS_$_RTTrustedTimeCache
+ _RTAnalyticsEventSafetyMonitorInitiatorExitAndArrivalMetrics
+ _SMSessionBimonthlyCount
+ _SMSessionDestinationWasReached
+ _SMSessionTimeToExitOriginLoi
+ _SMSessionTimeToMove250Meters
+ _SMSessionTrueDurationRelativeToETA
+ __OBJC_$_INSTANCE_METHODS_RTTrustedTimeCache
+ __OBJC_$_INSTANCE_VARIABLES_RTTrustedTimeCache
+ __OBJC_$_PROP_LIST_RTTrustedTimeCache
+ __OBJC_CLASS_RO_$_RTTrustedTimeCache
+ __OBJC_METACLASS_RO_$_RTTrustedTimeCache
+ ___126-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:]_block_invoke.209
+ ___47-[RTTrustedTimeCache machContinuousTimeSeconds]_block_invoke
+ ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.285
+ ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.180
+ ___54-[SMSessionMetricManager _onDailyMetricsNotification:]_block_invoke_4
+ ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke
+ ___62-[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]_block_invoke.218
+ ___63-[SMSessionMetricManager getRTLocationOfInterestForCLLocation:]_block_invoke
+ ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.198
+ ___70-[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]_block_invoke
+ ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.192
+ ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.193
+ ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.195
+ ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.196
+ ___71-[SMSessionMetricManager getLocationsForInterval:nearBoundingLocation:]_block_invoke
+ ___block_descriptor_48_e8_32s_e20_v24?0Q8"NSError"16ls32l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e20_v24?0Q8"NSError"16lr56l8r64l8s32l8s40l8s48l8
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_msgSend$_fetchCurrentLocationSinceDate:handler:
+ _objc_msgSend$_gatherSessionDestinationStats:
+ _objc_msgSend$getApproximateTrustedDateNow
+ _objc_msgSend$getApproximateTrustedDateNowWithUnsecureFallback
+ _objc_msgSend$getLocationsForInterval:nearBoundingLocation:
+ _objc_msgSend$getRTLocationOfInterestForCLLocation:
+ _objc_msgSend$initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:
+ _objc_msgSend$machContinuousTimeSeconds
+ _objc_msgSend$setBoundsForReferenceTimeWithMinimumDate:maximumDate:
+ _objc_msgSend$trustedTimestamp
- -[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]
- -[SMSessionMetricManager initWithDefaultsManager:learnedLocationManager:sessionStore:]
- GCC_except_table61
- GCC_except_table82
- ___126-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:]_block_invoke.198
- ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.275
- ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.172
- ___62-[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]_block_invoke.208
- ___64-[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]_block_invoke
- ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.186
- ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke_2
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.182
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.184
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.185
- _objc_msgSend$initWithDefaultsManager:learnedLocationManager:sessionStore:
CStrings:
+ "%@, downgrading leeched location integrity because trusted-time is unavailable."
+ "%@, downgrading leeched location integrity because user-time to trusted-time offset is too large: %@, %@."
+ "%@, vertex idx, %lu, coordinate, %@"
+ "%@:%@ distance, %{public}.1f, duration, %{public}.1f, accuracy, %{public}.1f, position uncertainty rate, %{public}.2f, distance threshold, %{public}.1f, location batch is consistent."
+ "%@:%@ distance, %{public}.1f, duration, %{public}.1f, accuracy, %{public}.1f, position uncertainty rate, %{public}.2f, distance threshold, %{public}.1f, location batch is not consistent."
+ "%@:%@ distance, %{public}.3f, matched, %{public}d, threshold %{public}.3f, type, %{public}d, unc, %{public}.1f, age, %{public}.1f"
+ "%@:%@ exceeded max retry, disabling futher retroactive registration of visits."
+ "%@:%@ fetched current location: %@"
+ "%@:%@ fetched location: %@"
+ "%@:%@ fetched visit %@."
+ "%@:%@ invoked with two or more locations, start location, %@, end location, %@."
+ "%@:%@ passed 11 (%{private}d)"
+ "%@:%@ rejection 11 (%{private}d)"
+ "%@:%@ rejection 5 (%@)."
+ "%@:%@, Authorized Locations: total visit dwell, %{private}.0f, number of unique days visited, %{private}ld, Authorized Location, %@."
+ "%@:%@, WARNING, attempting to retroactively register all stored visits. This will be run one time after software upgrade."
+ "%@:%@, appending LOI, total visit dwell, %{private}.0f, threshold, %{private}.0f, number of unique days visited, %{private}ld, threshold, %{private}ld, LOI %@."
+ "%@:%@, applying check between startTime %@ and endTime %@."
+ "%@:%@, currentVisit.entry has no value setting endTime to trustedNow: %@."
+ "%@:%@, detected vehicular motion of %{private}f seconds (threshold %{private}f seconds) in visit."
+ "%@:%@, failed to fetch trusted time now. Not regenerating authorized location list."
+ "%@:%@, failed to register any visits, will try again, not setting default RTDefaultsAuthorizedLocationIsFirstRunSinceSwUpdate to NO."
+ "%@:%@, fetched %{private}ld historical locations of interest between %@ and %@."
+ "%@:%@, fetched %{private}ld locations for date interval %@."
+ "%@:%@, fetched %{private}ld motion activities for date interval %@."
+ "%@:%@, fetched %{private}ld visit logs for interval: %@."
+ "%@:%@, most recent location is older than %{private}.0f seconds, %@."
+ "%@:%@, motion activity, %{private}d, cumulative interval %.3f s, position uncertainty rate, %.3f."
+ "%@:%@, no motion activity, defaulting to %{private}f mps."
+ "%@:%@, no visits to register for registrationDate: %@"
+ "%@:%@, processing %{private}lu visits for LOI %@."
+ "%@:%@, processing motion activity on date interval %@."
+ "%@:%@, processing visit %@."
+ "%@:%@, rejection 8 (%{private}ld)."
+ "%@:%@, rejection reason 1 (%{public}.1f)."
+ "%@:%@, rejection reason 1 (unavailable)."
+ "%@:%@, setting bound from date %@"
+ "%@:%@, setting endTime to currentVisit.entry: %@."
+ "%@:%@, skipping LOI, total visit dwell, %{private}.0f, threshold, %{private}.0f, number of unique days visited, %{private}ld, threshold, %{private}ld, LOI %@."
+ "%@:%@, starting visit curation, processing %{private}lu LOIs"
+ "%@:%@, successfully registered %{public}d visits via XPC Activity."
+ "%@:%@, trustedNow is before user-time currentVisit.entry, overriding endTime with trustedNow: %@."
+ "%@:%@, using default position uncertainty rate, %{private}f mps."
+ "%@:%@, using weighted average position uncertainty rate from motion activity, %{private}f mps."
+ "%@:%@, zero authorized locations created during current curation, retaining previously generated list of length %{public}lu, creation, %@, age, %{public}.1f."
+ "%@:%@: time since last authorized location curation %{private}.0f seconds, greater than threshold %{private}.0f seconds. Clearing authorized location list."
+ "%@:%@: time since last authorized location curation %{private}.0f seconds, less than threshold %{private}.0f seconds. Not regenerating authorized location list."
+ "%@:%@:_authorizedLocationArr Sorted Authorized Locations: total visit dwell, %{private}.0f, number of unique days visited, %{private}ld, Authorized Location, %@."
+ "*"
+ "-[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]"
+ "20:13:30"
+ "@\"RTTrustedTimeCache\""
+ "Jan  5 2024"
+ "RTAuthorizedLocation, loi, %@, dwellTime_s, %f, numberOfDaysVisited, %ld."
+ "RTAuthorizedLocationManager,%@:%@, %@"
+ "RTTrustedTimeCache"
+ "Reference time %{public}.1f violated bounds %{public}.1f,%{public}.1f"
+ "Reference time fetched with age %{public}.3f and offset %{public}.3f"
+ "Reference time fetched with offset %{public}.3f,unc,%{public}.3f,rel,%{public}d"
+ "Reference time unavailable"
+ "SafetyMonitor.initiator.exitAndArrivalMetrics"
+ "Set reference time bounds to %{public}.1f,%{public}.1f, age, %{public}.1f,%{public}.1f"
+ "T@\"RTTrustedTimeCache\",R,N,V_trustedTimeCache"
+ "TB,V_isUnlockedSinceBoot"
+ "TQ,V_retroRegistrationAttemptCount"
+ "Td,N,V_cachedReferenceTimeCfatSeconds"
+ "Td,N,V_cachedReferenceTimeMachContSeconds"
+ "Td,N,V_cachedTrustedTimeCfatSeconds"
+ "Td,N,V_cachedTrustedTimeMachContSeconds"
+ "Td,N,V_maxBoundReferenceTimeCfatSeconds"
+ "Td,N,V_minBoundReferenceTimeCfatSeconds"
+ "Trusted interval fetched with age %{public}.3f and offset %{public}.3f"
+ "Trusted interval fetched with offset %{public}.3f,unc,%{public}.3f"
+ "Trusted interval unavailable"
+ "_cachedReferenceTimeCfatSeconds"
+ "_cachedReferenceTimeMachContSeconds"
+ "_cachedTrustedTimeCfatSeconds"
+ "_cachedTrustedTimeMachContSeconds"
+ "_fetchCurrentLocationSinceDate:handler:"
+ "_gatherSessionDestinationStats:"
+ "_isUnlockedSinceBoot"
+ "_maxBoundReferenceTimeCfatSeconds"
+ "_minBoundReferenceTimeCfatSeconds"
+ "_retroRegistrationAttemptCount"
+ "_trustedTimeCache"
+ "cachedReferenceTimeCfatSeconds"
+ "cachedReferenceTimeMachContSeconds"
+ "cachedTrustedTimeCfatSeconds"
+ "cachedTrustedTimeMachContSeconds"
+ "daemonResponseLatencyMs, %f, loiFamiliarityRank, %d, maxCumulativeDwellTimeForNotFamiliarLoiHours, %f, maxUniqueVisitDaysForNotFamiliarLois, %d, normalizedDistanceToCentroid, %f, numFamiliarLois, %d, rejectionReasonCode, %d, responseValue, %d, technologyAvailability, %d, roundedUserTimeOffsetHours, %f, visitDwellMinutes, %f."
+ "getApproximateTrustedDateNow"
+ "getApproximateTrustedDateNowWithUnsecureFallback"
+ "getLocationsForInterval:nearBoundingLocation:"
+ "getRTLocationOfInterestForCLLocation:"
+ "initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:"
+ "isUnlockedSinceBoot"
+ "machContinuousTimeSeconds"
+ "maxBoundReferenceTimeCfatSeconds"
+ "minBoundReferenceTimeCfatSeconds"
+ "retroRegistrationAttemptCount"
+ "sessionStartTimeOfDay"
+ "setBoundsForReferenceTimeWithMinimumDate:maximumDate:"
+ "setCachedReferenceTimeCfatSeconds:"
+ "setCachedReferenceTimeMachContSeconds:"
+ "setCachedTrustedTimeCfatSeconds:"
+ "setCachedTrustedTimeMachContSeconds:"
+ "setIsUnlockedSinceBoot:"
+ "setMaxBoundReferenceTimeCfatSeconds:"
+ "setMinBoundReferenceTimeCfatSeconds:"
+ "setRetroRegistrationAttemptCount:"
+ "shuffle"
+ "trustedTimeCache"
+ "trustedTimestamp"
- "\x1d"
- "%@, downgrading leeched location integrity because user-time to trusted-time offset is too large: %@."
- "%@, vertex idx, %lu, latitude, %f, longitude, %f"
- "%@:%@ distance %{private}.3f m is greater than threshold %{private}.3f, is not considered at authorized location."
- "%@:%@ distance %{private}.3f m is less than threshold %{private}.3f, is considered at authorized location."
- "%@:%@ distance, %.1f, duration, %.1f, accuracy, %.1f, position uncertainty rate, %.2f, distance threshold, %.1f, location batch is consistent."
- "%@:%@ distance, %.1f, duration, %.1f, accuracy, %.1f, position uncertainty rate, %.2f, distance threshold, %.1f, location batch is not consistent."
- "%@:%@ fetched current location: %{private}@"
- "%@:%@ fetched location: %{private}@"
- "%@:%@ passed 11 (%d)"
- "%@:%@ rejection 11 (%d)"
- "%@:%@ rejection 5 (%{private}@)."
- "%@:%@, WARNING, retroactively registering all stored visits. This will be run one time on first launch after software upgrade."
- "%@:%@, appending LOI, total visit dwell, %.0f, threshold, %.0f, number of unique days visited, %ld, threshold, %ld, LOI %@."
- "%@:%@, detected vehicular motion of %f seconds (threshold %f seconds) in visit."
- "%@:%@, failed to fetch trusted time now, not updating visit logs."
- "%@:%@, fetched %ld historical locations of interest between %@ and %@."
- "%@:%@, fetched %ld locations for date interval %@."
- "%@:%@, fetched %ld motion activities for date interval %@."
- "%@:%@, fetched %ld visit logs for interval: %@."
- "%@:%@, most recent location is older than %.0f seconds, %@."
- "%@:%@, no motion activity, defaulting to %f mps."
- "%@:%@, rejection 8 (%ld)."
- "%@:%@, rejection reason 1 (%.1f)."
- "%@:%@, skipping LOI, total visit dwell, %.0f, threshold, %.0f, number of unique days visited, %ld, threshold, %ld, LOI %@."
- "%@:%@, starting visit curation."
- "%@:%@, successfully registered visits via XPC Activity."
- "%@:%@, weighted average position uncertainty rate, %f mps."
- "%@:%@: time since last run %.0f seconds, less than threshold %.0f seconds. Not regenerating authorized location list."
- "%@:%@:_authorizedLocationArr Sorted Authorized Locations: total visit dwell, %.0f, number of unique days visited, %ld, Authorized Location, %@."
- ")"
- "-[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]"
- "20:55:40"
- "Nov 28 2023"
- "initWithDefaultsManager:learnedLocationManager:sessionStore:"

```
