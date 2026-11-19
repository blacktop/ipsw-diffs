## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1122.0.0.0.0
-  __TEXT.__text: 0x68e67c
-  __TEXT.__objc_methlist: 0x32010
-  __TEXT.__const: 0x45e8
+1123.0.3.0.0
+  __TEXT.__text: 0x6994f4
+  __TEXT.__objc_methlist: 0x32550
+  __TEXT.__const: 0x4678
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x18a
-  __TEXT.__oslogstring: 0x7e1ad
-  __TEXT.__cstring: 0x45a29
+  __TEXT.__constg_swiftt: 0x74
+  __TEXT.__swift5_typeref: 0x190
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__oslogstring: 0x7f1c2
+  __TEXT.__cstring: 0x45d0e
   __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift_as_cont: 0x24
-  __TEXT.__constg_swiftt: 0x48
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27de0
+  __TEXT.__gcc_except_tab: 0x28444
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xde40
+  __TEXT.__unwind_info: 0xdff8
   __TEXT.__eh_frame: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3510
-  __DATA_CONST.__objc_classlist: 0x15f0
+  __DATA_CONST.__const: 0x3560
+  __DATA_CONST.__objc_classlist: 0x1610
   __DATA_CONST.__objc_catlist: 0x3c0
-  __DATA_CONST.__objc_protolist: 0x330
+  __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19688
-  __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x11d0
+  __DATA_CONST.__objc_selrefs: 0x19928
+  __DATA_CONST.__objc_protorefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x11e8
   __DATA_CONST.__objc_arraydata: 0x2ca8
-  __DATA_CONST.__got: 0x2f40
-  __AUTH_CONST.__const: 0xf540
-  __AUTH_CONST.__cfstring: 0x286c0
-  __AUTH_CONST.__objc_const: 0x53ae8
+  __DATA_CONST.__got: 0x2f60
+  __AUTH_CONST.__const: 0xf6e0
+  __AUTH_CONST.__cfstring: 0x28940
+  __AUTH_CONST.__objc_const: 0x542d8
   __AUTH_CONST.__objc_intobj: 0x4860
   __AUTH_CONST.__objc_arrayobj: 0xeb8
   __AUTH_CONST.__objc_doubleobj: 0xbe0

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0xde0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x25e8
+  __AUTH.__objc_data: 0x19a8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x27f8
-  __DATA.__data: 0x2aa0
-  __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_ivar: 0x113c
-  __DATA_DIRTY.__objc_data: 0xb5e0
-  __DATA_DIRTY.__data: 0x5a8
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA.__objc_ivar: 0x2838
+  __DATA.__data: 0x2a98
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_ivar: 0x1170
+  __DATA_DIRTY.__objc_data: 0xc3c0
+  __DATA_DIRTY.__data: 0x648
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20822
-  Symbols:   43210
-  CStrings:  15137
+  Functions: 20980
+  Symbols:   43503
+  CStrings:  15225
 
Symbols:
+ +[RTExtendedTimeToLiveGate isEnabled]
+ +[RTExtendedTimeToLiveGate mFeatureVerdictFromDefaultsManager:]
+ +[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:defaultsManager:]
+ +[RTExtendedTimeToLiveGate sharedGate]
+ -[RTAccount birthYear]
+ -[RTAccount setBirthYear:]
+ -[RTCheckInMetricsProvider .cxx_destruct]
+ -[RTCheckInMetricsProvider _biomeIntervalsForStreamType:interval:]
+ -[RTCheckInMetricsProvider _buildStatesForWindow:homeIntervals:homeKeys:majorityKey:homeFields:lockFields:motionFields:mask:]
+ -[RTCheckInMetricsProvider _chooseWindowStart:longestRun:visits:zone:shift:newestDay:]
+ -[RTCheckInMetricsProvider _collectMetricsWithCompletion:]
+ -[RTCheckInMetricsProvider _coreMotionStationaryIntervalsForWindow:]
+ -[RTCheckInMetricsProvider _deviceHasVisits:inInterval:store:error:]
+ -[RTCheckInMetricsProvider _hasConsentToCollect]
+ -[RTCheckInMetricsProvider _homeIntervalsFromVisits:window:homeKeys:mask:]
+ -[RTCheckInMetricsProvider _homeVisitsForRunWithError:]
+ -[RTCheckInMetricsProvider _homeZoneForVisits:]
+ -[RTCheckInMetricsProvider _isDiagnosticsAndUsageAllowed]
+ -[RTCheckInMetricsProvider _isDueForSubmission]
+ -[RTCheckInMetricsProvider _isEffectivelyIPhoneOnlyInInterval:error:]
+ -[RTCheckInMetricsProvider _isEventActive]
+ -[RTCheckInMetricsProvider _isOptedInToAppleAnalytics]
+ -[RTCheckInMetricsProvider _isSafetyDataSubmissionAllowed]
+ -[RTCheckInMetricsProvider _majorityHomeKeyForVisits:window:]
+ -[RTCheckInMetricsProvider _majorityHomeMovedForVisits:window:]
+ -[RTCheckInMetricsProvider _outcomeForSignals:window:majorityMoved:]
+ -[RTCheckInMetricsProvider _payloadForHomeFields:lockFields:motionFields:startDay:outcome:ageBand:]
+ -[RTCheckInMetricsProvider _recordAttempt]
+ -[RTCheckInMetricsProvider _refreshCachedAccountState]
+ -[RTCheckInMetricsProvider _sendPayloadIfConsented:]
+ -[RTCheckInMetricsProvider _setup]
+ -[RTCheckInMetricsProvider _shouldSkipUnderageForDate:]
+ -[RTCheckInMetricsProvider _shouldStopForDefer]
+ -[RTCheckInMetricsProvider _shutdownWithHandler:]
+ -[RTCheckInMetricsProvider _stationaryIntervalsForWindow:mask:]
+ -[RTCheckInMetricsProvider _submitWindowEndingDay:submitted:deferred:error:]
+ -[RTCheckInMetricsProvider _timeZoneAtLatitude:longitude:]
+ -[RTCheckInMetricsProvider accountManager]
+ -[RTCheckInMetricsProvider biomeManager]
+ -[RTCheckInMetricsProvider cachedAccountIdentifier]
+ -[RTCheckInMetricsProvider cachedAccountLoaded]
+ -[RTCheckInMetricsProvider cachedBirthYear]
+ -[RTCheckInMetricsProvider cachedHomeZonesByLOI]
+ -[RTCheckInMetricsProvider cachedUnderageAccount]
+ -[RTCheckInMetricsProvider defaultsManager]
+ -[RTCheckInMetricsProvider initWithAccountManager:biomeManager:defaultsManager:learnedLocationManager:managedConfiguration:motionActivityManager:xpcActivityManager:]
+ -[RTCheckInMetricsProvider init]
+ -[RTCheckInMetricsProvider learnedLocationManager]
+ -[RTCheckInMetricsProvider managedConfiguration]
+ -[RTCheckInMetricsProvider motionActivityManager]
+ -[RTCheckInMetricsProvider onAccountChangedNotification:]
+ -[RTCheckInMetricsProvider runVisitSpan]
+ -[RTCheckInMetricsProvider setCachedAccountIdentifier:]
+ -[RTCheckInMetricsProvider setCachedAccountLoaded:]
+ -[RTCheckInMetricsProvider setCachedBirthYear:]
+ -[RTCheckInMetricsProvider setCachedHomeZonesByLOI:]
+ -[RTCheckInMetricsProvider setCachedUnderageAccount:]
+ -[RTCheckInMetricsProvider setRunVisitSpan:]
+ -[RTCheckInMetricsProvider setShouldDeferRun:]
+ -[RTCheckInMetricsProvider shouldDeferRun]
+ -[RTCheckInMetricsProvider xpcActivityManager]
+ -[RTExtendedTimeToLiveGate .cxx_destruct]
+ -[RTExtendedTimeToLiveGate defaultsManager]
+ -[RTExtendedTimeToLiveGate featureEnabled]
+ -[RTExtendedTimeToLiveGate initWithFeatureEnabled:trialManager:platform:defaultsManager:featureStatusProvider:]
+ -[RTExtendedTimeToLiveGate internalAndTrialEnabled]
+ -[RTExtendedTimeToLiveGate internalInstall]
+ -[RTExtendedTimeToLiveGate isEnabled]
+ -[RTExtendedTimeToLiveGate isMFeatureEnabled]
+ -[RTExtendedTimeToLiveGate mFeatureEnabled]
+ -[RTExtendedTimeToLiveGate manualOverride]
+ -[RTManagedConfiguration isSafetyDataSubmissionAllowed]
+ -[RTManagedConfiguration_OSX isSafetyDataSubmissionAllowed]
+ -[RTMapItemManager bluePOITileManager]
+ -[RTMapItemManager initWithLearnedLocationStore:mapServiceManager:defaultsManager:bluePOITileManager:]
+ -[RTMapItemManager isBluePOITileAvailableForLocation:]
+ -[RTMapItemManager setBluePOITileManager:]
+ -[RTMapItemManager setTileAvailabilityTimeout:]
+ -[RTMapItemManager tileAvailabilityTimeout]
+ -[RTTrialManager .cxx_destruct]
+ -[RTTrialManager boolValueForFactor:]
+ -[RTTrialManager doubleValueForFactor:]
+ -[RTTrialManager factorProvider]
+ -[RTTrialManager initWithNamespaceName:]
+ -[RTTrialManager initWithNamespaceName:factorProvider:]
+ -[RTTrialManager levelForFactor:]
+ -[RTTrialManager namespaceName]
+ -[RTTrialManager refresh]
+ -[RTTrialManager setFactorProvider:]
+ -[RTTrialManager setNamespaceName:]
+ -[RTTripClusterManager _donationPlaceConfidenceForLocationOfInterest:]
+ -[RTTripClusterManager _nearestLocationOfInterest:toLocation:withinDistance:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalMaxHorizontalAccuracy_m:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalRadius_m:]
+ -[RTTripClusterProcessorOptions setWalkingArrivalRequiredConsecutiveFixes:]
+ -[RTTripClusterProcessorOptions walkingArrivalMaxHorizontalAccuracy_m]
+ -[RTTripClusterProcessorOptions walkingArrivalRadius_m]
+ -[RTTripClusterProcessorOptions walkingArrivalRequiredConsecutiveFixes]
+ -[RTTripClusterWalkAndBikeTripStats .cxx_destruct]
+ -[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForSortedLocations:destinationLatitude:destinationLongitude:segmentStartDate:wallClockDuration:]
+ -[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]
+ -[RTTripClusterWalkAndBikeTripStats initWithTripSegmentManager:options:]
+ -[RTTripClusterWalkAndBikeTripStats options]
+ -[RTTripClusterWalkAndBikeTripStats setOptions:]
+ -[RTTripClusterWalkAndBikeTripStats setTripSegmentManager:]
+ -[RTTripClusterWalkAndBikeTripStats tripSegmentManager]
+ -[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:]
+ OBJC_IVAR_$_RTAccount._birthYear
+ OBJC_IVAR_$_RTCheckInMetricsProvider._cachedAccountLoaded
+ OBJC_IVAR_$_RTCheckInMetricsProvider._cachedUnderageAccount
+ OBJC_IVAR_$_RTCheckInMetricsProvider._shouldDeferRun
+ OBJC_IVAR_$_RTExtendedTimeToLiveGate._defaultsManager
+ OBJC_IVAR_$_RTExtendedTimeToLiveGate._featureEnabled
+ OBJC_IVAR_$_RTExtendedTimeToLiveGate._internalAndTrialEnabled
+ OBJC_IVAR_$_RTExtendedTimeToLiveGate._internalInstall
+ OBJC_IVAR_$_RTExtendedTimeToLiveGate._mFeatureEnabled
+ OBJC_IVAR_$_RTTrialManager._factorProvider
+ OBJC_IVAR_$_RTTrialManager._namespaceName
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalMaxHorizontalAccuracy_m
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRadius_m
+ OBJC_IVAR_$_RTTripClusterProcessorOptions._walkingArrivalRequiredConsecutiveFixes
+ OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._options
+ OBJC_IVAR_$_RTTripClusterWalkAndBikeTripStats._tripSegmentManager
+ _OBJC_CLASS_$_RTActionSuggestionFeatureStatusProvider
+ _OBJC_CLASS_$_RTCheckInMetricsProvider
+ _OBJC_CLASS_$_RTExtendedTimeToLiveGate
+ _OBJC_CLASS_$_RTTrialManager
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_METACLASS_$_RTActionSuggestionFeatureStatusProvider
+ _OBJC_METACLASS_$_RTCheckInMetricsProvider
+ _OBJC_METACLASS_$_RTExtendedTimeToLiveGate
+ _OBJC_METACLASS_$_RTTrialManager
+ _PROTOCOLS_RTActionSuggestionFeatureStatusProvider
+ _RTAnalyticsEventAlwaysOnCheckIn
+ _RTApplicationManagerBundleIdMapsIntents
+ _RTBackgroundTaskIdentifierAlwaysOnCheckInMetrics
+ _RTCheckInAgeBandForBirthYear
+ _RTCheckInAnchorForDayIndex
+ _RTCheckInCanonicalIntervals
+ _RTCheckInClipVisitToInterval
+ _RTCheckInCoverageForIntervals
+ _RTCheckInDayForDayIndex
+ _RTCheckInDayIndexForDate
+ _RTCheckInDeriveQuietFields
+ _RTCheckInEnvelopeForIntervals
+ _RTCheckInGetQuiet
+ _RTCheckInGetState
+ _RTCheckInHomeKeyForVisit
+ _RTCheckInOverlap
+ _RTCheckInQuietCount
+ _RTCheckInSearchSpanForNewestDay
+ _RTCheckInSetQuiet
+ _RTCheckInSetState
+ _RTCheckInStateCount
+ _RTCheckInStationaryIntervalsFromActivities
+ _RTCheckInWindowForDayIndex
+ _RTLearnedLocationExpirationIntervalValue
+ _RTLearnedLocationVisitShortExpirationIntervalValue
+ __34-[RTCheckInMetricsProvider _setup]_block_invoke
+ __74-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]_block_invoke
+ __DATA_RTActionSuggestionFeatureStatusProvider
+ __INSTANCE_METHODS_RTActionSuggestionFeatureStatusProvider
+ __METACLASS_DATA_RTActionSuggestionFeatureStatusProvider
+ __OBJC_$_CLASS_METHODS_RTExtendedTimeToLiveGate
+ __OBJC_$_CLASS_PROP_LIST_RTExtendedTimeToLiveGate
+ __OBJC_$_INSTANCE_METHODS_RTCheckInMetricsProvider
+ __OBJC_$_INSTANCE_METHODS_RTExtendedTimeToLiveGate
+ __OBJC_$_INSTANCE_METHODS_RTTrialManager
+ __OBJC_$_INSTANCE_VARIABLES_RTCheckInMetricsProvider
+ __OBJC_$_INSTANCE_VARIABLES_RTExtendedTimeToLiveGate
+ __OBJC_$_INSTANCE_VARIABLES_RTTrialManager
+ __OBJC_$_PROP_LIST_RTCheckInMetricsProvider
+ __OBJC_$_PROP_LIST_RTExtendedTimeToLiveGate
+ __OBJC_$_PROP_LIST_RTTrialManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RTActionSuggestionFeatureStatusProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RTActionSuggestionFeatureStatusProviding
+ __OBJC_$_PROTOCOL_REFS_RTActionSuggestionFeatureStatusProviding
+ __OBJC_CLASS_RO_$_RTCheckInMetricsProvider
+ __OBJC_CLASS_RO_$_RTExtendedTimeToLiveGate
+ __OBJC_CLASS_RO_$_RTTrialManager
+ __OBJC_LABEL_PROTOCOL_$_RTActionSuggestionFeatureStatusProviding
+ __OBJC_METACLASS_RO_$_RTCheckInMetricsProvider
+ __OBJC_METACLASS_RO_$_RTExtendedTimeToLiveGate
+ __OBJC_METACLASS_RO_$_RTTrialManager
+ __OBJC_PROTOCOL_$_RTActionSuggestionFeatureStatusProviding
+ __PROTOCOLS_RTActionSuggestionFeatureStatusProvider
+ ___34-[RTCheckInMetricsProvider _setup]_block_invoke
+ ___38+[RTExtendedTimeToLiveGate sharedGate]_block_invoke
+ ___52-[RTCheckInMetricsProvider _sendPayloadIfConsented:]_block_invoke
+ ___54-[RTCheckInMetricsProvider _refreshCachedAccountState]_block_invoke
+ ___54-[RTCheckInMetricsProvider _refreshCachedAccountState]_block_invoke_2
+ ___54-[RTMapItemManager isBluePOITileAvailableForLocation:]_block_invoke
+ ___55-[RTCheckInMetricsProvider _homeVisitsForRunWithError:]_block_invoke
+ ___57-[RTCheckInMetricsProvider onAccountChangedNotification:]_block_invoke
+ ___58-[RTCheckInMetricsProvider _timeZoneAtLatitude:longitude:]_block_invoke
+ ___66-[RTCheckInMetricsProvider _biomeIntervalsForStreamType:interval:]_block_invoke
+ ___68-[RTCheckInMetricsProvider _coreMotionStationaryIntervalsForWindow:]_block_invoke
+ ___68-[RTCheckInMetricsProvider _deviceHasVisits:inInterval:store:error:]_block_invoke
+ ___69-[RTCheckInMetricsProvider _isEffectivelyIPhoneOnlyInInterval:error:]_block_invoke
+ ___74-[RTCheckInMetricsProvider _homeIntervalsFromVisits:window:homeKeys:mask:]_block_invoke
+ ___74-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]_block_invoke
+ ___79+[RTExtendedTimeToLiveGate refreshMFeatureVerdictWithProvider:defaultsManager:]_block_invoke
+ ___RTCheckInCanonicalIntervals_block_invoke
+ ___RTCheckInInitFieldNames_block_invoke
+ ___RTCheckInStationaryIntervalsFromActivities_block_invoke
+ ___block_descriptor_32_e29_q24?0"RTVisit"8"RTVisit"16l
+ ___block_descriptor_32_e47_q24?0"RTMotionActivity"8"RTMotionActivity"16l
+ ___block_descriptor_40_e8_32w_e19_v16?0"RTAccount"8l
+ ___block_descriptor_48_e8_32r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_e8_32s40r_e35_v24?0"RTBluePOITile"8"NSError"16l
+ ___block_descriptor_64_e8_32s40r_e5_v8?0l
+ _kRTCheckInBitsPerSlice
+ _kRTCheckInQuietFieldCount
+ _kRTCheckInSliceDuration
+ _kRTCheckInSlicesPerDay
+ _kRTCheckInSlicesPerField
+ _kRTCheckInSlicesPerQuietField
+ _kRTCheckInSlicesPerWindow
+ _kRTCheckInStateFieldCount
+ _kRTCheckInWindowDays
+ _objc_msgSend$_activeWalkingDurationForSortedLocations:destinationLatitude:destinationLongitude:segmentStartDate:wallClockDuration:
+ _objc_msgSend$_activeWalkingDurationForTripSegment:
+ _objc_msgSend$_biomeIntervalsForStreamType:interval:
+ _objc_msgSend$_buildStatesForWindow:homeIntervals:homeKeys:majorityKey:homeFields:lockFields:motionFields:mask:
+ _objc_msgSend$_chooseWindowStart:longestRun:visits:zone:shift:newestDay:
+ _objc_msgSend$_collectMetricsWithCompletion:
+ _objc_msgSend$_deviceHasVisits:inInterval:store:error:
+ _objc_msgSend$_donationPlaceConfidenceForLocationOfInterest:
+ _objc_msgSend$_hasConsentToCollect
+ _objc_msgSend$_homeIntervalsFromVisits:window:homeKeys:mask:
+ _objc_msgSend$_homeVisitsForRunWithError:
+ _objc_msgSend$_homeZoneForVisits:
+ _objc_msgSend$_isDiagnosticsAndUsageAllowed
+ _objc_msgSend$_isDueForSubmission
+ _objc_msgSend$_isEffectivelyIPhoneOnlyInInterval:error:
+ _objc_msgSend$_isEventActive
+ _objc_msgSend$_isOptedInToAppleAnalytics
+ _objc_msgSend$_isSafetyDataSubmissionAllowed
+ _objc_msgSend$_majorityHomeKeyForVisits:window:
+ _objc_msgSend$_majorityHomeMovedForVisits:window:
+ _objc_msgSend$_nearestLocationOfInterest:toLocation:withinDistance:
+ _objc_msgSend$_outcomeForSignals:window:majorityMoved:
+ _objc_msgSend$_payloadForHomeFields:lockFields:motionFields:startDay:outcome:ageBand:
+ _objc_msgSend$_recordAttempt
+ _objc_msgSend$_refreshCachedAccountState
+ _objc_msgSend$_sendPayloadIfConsented:
+ _objc_msgSend$_shouldSkipUnderageForDate:
+ _objc_msgSend$_shouldStopForDefer
+ _objc_msgSend$_stationaryIntervalsForWindow:mask:
+ _objc_msgSend$_submitWindowEndingDay:submitted:deferred:error:
+ _objc_msgSend$_timeZoneAtLatitude:longitude:
+ _objc_msgSend$altDSID
+ _objc_msgSend$birthYear
+ _objc_msgSend$birthYearForAccount:
+ _objc_msgSend$boolValueForFactor:
+ _objc_msgSend$booleanValue
+ _objc_msgSend$cachedAccountLoaded
+ _objc_msgSend$cachedBirthYear
+ _objc_msgSend$cachedHomeZonesByLOI
+ _objc_msgSend$cachedUnderageAccount
+ _objc_msgSend$daylightSavingTimeOffsetForDate:
+ _objc_msgSend$factorProvider
+ _objc_msgSend$fetchFeatureStatusWithCompletion:
+ _objc_msgSend$initWithAccountManager:biomeManager:defaultsManager:learnedLocationManager:managedConfiguration:motionActivityManager:xpcActivityManager:
+ _objc_msgSend$initWithFeatureEnabled:trialManager:platform:defaultsManager:featureStatusProvider:
+ _objc_msgSend$initWithLearnedLocationStore:mapServiceManager:defaultsManager:bluePOITileManager:
+ _objc_msgSend$initWithNamespaceName:
+ _objc_msgSend$initWithNamespaceName:factorProvider:
+ _objc_msgSend$initWithTripSegment:preferredDownsamplingLevel:
+ _objc_msgSend$initWithTripSegmentManager:options:
+ _objc_msgSend$internalAndTrialEnabled
+ _objc_msgSend$isBluePOITileAvailableForLocation:
+ _objc_msgSend$isMFeatureEnabled
+ _objc_msgSend$isSafetyDataSubmissionAllowed
+ _objc_msgSend$levelForFactor:
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$mFeatureEnabled
+ _objc_msgSend$mFeatureVerdictFromDefaultsManager:
+ _objc_msgSend$manualOverride
+ _objc_msgSend$namespaceName
+ _objc_msgSend$refreshMFeatureVerdictWithProvider:defaultsManager:
+ _objc_msgSend$runVisitSpan
+ _objc_msgSend$secondsFromGMTForDate:
+ _objc_msgSend$setBirthYear:
+ _objc_msgSend$setCachedAccountIdentifier:
+ _objc_msgSend$setCachedAccountLoaded:
+ _objc_msgSend$setCachedBirthYear:
+ _objc_msgSend$setCachedUnderageAccount:
+ _objc_msgSend$setRunVisitSpan:
+ _objc_msgSend$setShouldDeferRun:
+ _objc_msgSend$sharedGate
+ _objc_msgSend$shouldDeferRun
+ _objc_msgSend$tileAvailabilityTimeout
+ _objc_msgSend$updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:
+ _objc_msgSend$walkingArrivalMaxHorizontalAccuracy_m
+ _objc_msgSend$walkingArrivalRadius_m
+ _objc_msgSend$walkingArrivalRequiredConsecutiveFixes
+ _symbolic _____ 14libcoreroutine39RTActionSuggestionFeatureStatusProviderC
- -[RTMapItemManager initWithLearnedLocationStore:mapServiceManager:defaultsManager:]
- -[RTTripClusterWalkAndBikeTripStats init]
- -[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:]
- _objc_msgSend$initWithLearnedLocationStore:mapServiceManager:defaultsManager:
- _objc_msgSend$updateWalkAndBikeStats:isTripSegmentBeforeDriving:
CStrings:
+ "%.5f:%.5f"
+ "%@, %lu non-iPhone devices, all dormant over the interval, treating as iPhone-only"
+ "%@, %lu non-iPhone devices, past the bound, excluding"
+ "%@, account has a device other than an iPhone, or the device fetch failed, skipping, error, %@"
+ "%@, account not eligible, skipping"
+ "%@, account state not loaded, skipping"
+ "%@, chosen window has no home time, so the search and the clip disagree"
+ "%@, collecting expired records, cutoff, %@, ownedByThisDevice, %{public}@, entities, %lu"
+ "%@, consent withdrawn during the run, not submitting"
+ "%@, defer requested, abandoning the run"
+ "%@, device fetch returned no list and no error, excluding"
+ "%@, device visit probe returned no result and no error, excluding"
+ "%@, event not active, skipping"
+ "%@, fetched %lu home visits for the search span, %@"
+ "%@, iCloud account %@, birth year %@, underage, %{sensitive}d"
+ "%@, long cutoff, %@, shortRetentionDelta, %.0f, profile short cutoff, %@"
+ "%@, longest run of days at home was %lu, need %lu consecutive"
+ "%@, no consent to collect, skipping"
+ "%@, no home visits in the search span"
+ "%@, no learned location store, cannot check for other devices"
+ "%@, no single home timezone"
+ "%@, no timezone for a home location, not submitting"
+ "%@, nothing submitted, transient failure, %d, error, %@"
+ "%@, optInApple, %@, isDna, %@, improveSafety, %@"
+ "%@, query window startDate (%@) is before retention boundary (%@), capping to retention boundary"
+ "%@, refreshing mapItem, muid, %lu, isAOI, %d"
+ "%@, registered background task, %@"
+ "%@, run deferred, nothing submitted"
+ "%@, skipping AOI mapItem, not sourced from BluePOI, muid, %lu"
+ "%@, skipping mapItem, no BluePOI tile in store, muid, %lu"
+ "%@, startDay, %lld, window, %{sensitive}@, outcome, %lu, longest run, %lu, majority home slices, %lu, other home slices, %lu, away slices, %lu, lock not known, %lu, motion not known, %lu, signals, %lu"
+ "%@, timed out waiting for tile availability, refreshing anyway, error, %@"
+ "%@, timezone lookup timed out, error, %@"
+ "%@, window bands as underage though the run gate passed, not submitting"
+ "%@, within back-off, skipping, last submission, %@, last attempt, %@"
+ "%@,Error computing distance to destination,%@"
+ "%@,_activeWalkingDurationForSortedLocations,arrival not confirmed,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForSortedLocations,implausible active duration,%.1f,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForSortedLocations,leg never left arrival radius,maxDistance,%.1f,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForTripSegment,tripID,%@,no location data,fetchError,%@,semaError,%@,falling back to wall-clock duration,%.1f"
+ "%@,_activeWalkingDurationForTripSegment,tripID,%@,tripDistance,%.1f,wallClockDuration,%.1f,activeWalkingDuration,%.1f"
+ "%@.%@.checkInMetrics"
+ "%@:%@, found location of interest for location %@ with name '%@', place confidence, %.3f, derived from %lu visits"
+ "%@:%@, location of interest, %@, has no visits, donating place confidence, %.3f"
+ "%@:%@, location of interest, %@, has out of range place confidence, %.3f, clamping"
+ "%{public}@, %{public}@, featureEnabled, %{public}@, internalInstall, %{public}@, internalAndTrial, %{public}@, mFeature, %{public}@"
+ "%{public}@, %{public}@, namespace, %{public}@, factor, %{public}@, level, %{public}@"
+ "%{public}@, mFeature indeterminate, holding previous verdict, error, %{public}@"
+ "%{public}@, mFeature verdict persisted for next launch, %{public}@"
+ "-[RTTripClusterWalkAndBikeTripStats _activeWalkingDurationForTripSegment:]"
+ "-[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:isTerminalTripSegment:]"
+ "20:25:43"
+ "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@,maxCleanUpOperationsCountPerRun,%ld,maxRouteRehydrationsCountPerRun,%ld,maxDeletionAttemptsForClusterData,%ld,rehydrateRouteLocationsFromWaypoints,%@,cleanUpClusterWithDuplicateWaypoints,%@,cleanUpOrphanedLocalStoreEntries,%@,walkingArrivalRadius_m,%.2f,walkingArrivalMaxHorizontalAccuracy_m,%.2f,walkingArrivalRequiredConsecutiveFixes,%ld>"
+ "CoreRoutine.AlwaysOnCheckInV2"
+ "ExtendedRetentionInternalEnabled"
+ "Invalid parameter not satisfying: factorName"
+ "Invalid parameter not satisfying: factorProvider"
+ "Invalid parameter not satisfying: homeFields"
+ "Invalid parameter not satisfying: interval"
+ "Invalid parameter not satisfying: ioMask"
+ "Invalid parameter not satisfying: lockFields"
+ "Invalid parameter not satisfying: motionFields"
+ "Invalid parameter not satisfying: namespaceName"
+ "Invalid parameter not satisfying: outDeferred"
+ "Invalid parameter not satisfying: outStartDay"
+ "Invalid parameter not satisfying: outSubmitted"
+ "Invalid parameter not satisfying: self.runVisitSpan"
+ "MOMENTS_TRIAL"
+ "Oct  3 2026"
+ "RTDefaultsCheckInLastAttemptDate"
+ "RTDefaultsCheckInLastSubmissionDate"
+ "RTDefaultsExtendedTimeToLiveEnabled"
+ "RTDefaultsExtendedTimeToLiveMFeatureEnabled"
+ "absent"
+ "ageBand"
+ "check-in metrics asked to defer, stopping at the next checkpoint"
+ "check-in metrics defer signal failed, error, %@"
+ "check-in metrics task did not launch, error, %@"
+ "check-in metrics, CoreMotion fetch failed, error, %@"
+ "check-in metrics, CoreMotion fetch timed out, error, %@"
+ "check-in metrics, biome stream, %@, error, %@"
+ "com.apple.Maps.MapsIntents"
+ "com.apple.routined.%@.%@"
+ "com.apple.routined.alwaysOnCheckIn.metrics"
+ "finished lookup for primary icloud account, %@, underage, %{sensitive}d, birth year, %{public}@, error, %{public}@"
+ "homeState%lu"
+ "lockState%lu"
+ "motionState%lu"
+ "outcome"
+ "present"
+ "q24@?0@\"RTMotionActivity\"8@\"RTMotionActivity\"16"
+ "q24@?0@\"RTVisit\"8@\"RTVisit\"16"
+ "quietState%lu"
+ "startDayIndex"
+ "\x92"
- "%@, query window startDate (%@) is before 8-week retention boundary (%@), capping to retention boundary"
- "%@:%@, found location of interest for location %@ with name '%@'"
- "-[RTTripClusterWalkAndBikeTripStats updateWalkAndBikeStats:isTripSegmentBeforeDriving:]"
- "21:24:12"
- "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@,maxCleanUpOperationsCountPerRun,%ld,maxRouteRehydrationsCountPerRun,%ld,maxDeletionAttemptsForClusterData,%ld,rehydrateRouteLocationsFromWaypoints,%@,cleanUpClusterWithDuplicateWaypoints,%@,cleanUpOrphanedLocalStoreEntries,%@>"
- "Aug  8 2026"
- "finished lookup for primary icloud account %@, underage, %d, error, %@"
```
