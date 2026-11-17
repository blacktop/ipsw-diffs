## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1123.0.6.0.0
-  __TEXT.__text: 0x6c3370
-  __TEXT.__objc_methlist: 0x35670
+1123.0.9.0.0
+  __TEXT.__text: 0x6c6d4c
+  __TEXT.__objc_methlist: 0x35798
   __TEXT.__const: 0x4d08
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x477

   __TEXT.__constg_swiftt: 0x12c
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x8b936
-  __TEXT.__cstring: 0x4b6f0
+  __TEXT.__oslogstring: 0x8bad7
+  __TEXT.__cstring: 0x4b840
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_reflstr: 0x14
-  __TEXT.__gcc_except_tab: 0x2f974
+  __TEXT.__gcc_except_tab: 0x2fbc4
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x11d68
+  __TEXT.__unwind_info: 0x11e00
   __TEXT.__eh_frame: 0x7d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10810
-  __DATA_CONST.__objc_classlist: 0x16d0
+  __DATA_CONST.__const: 0x108a8
+  __DATA_CONST.__objc_classlist: 0x16e0
   __DATA_CONST.__objc_catlist: 0x3f8
   __DATA_CONST.__objc_protolist: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8e0
+  __DATA_CONST.__objc_selrefs: 0x1b990
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA_CONST.__objc_superrefs: 0x12b0
+  __DATA_CONST.__objc_superrefs: 0x12c0
   __DATA_CONST.__objc_arraydata: 0x2dd8
-  __DATA_CONST.__got: 0x3598
-  __AUTH_CONST.__const: 0x3918
-  __AUTH_CONST.__cfstring: 0x2c7a0
-  __AUTH_CONST.__objc_const: 0x576f8
+  __DATA_CONST.__got: 0x35a8
+  __AUTH_CONST.__const: 0x3998
+  __AUTH_CONST.__cfstring: 0x2c8a0
+  __AUTH_CONST.__objc_const: 0x578f8
   __AUTH_CONST.__objc_intobj: 0x4c38
   __AUTH_CONST.__objc_arrayobj: 0xfc0
   __AUTH_CONST.__objc_doubleobj: 0xbe0
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1320
-  __AUTH.__objc_data: 0x1bd0
+  __AUTH_CONST.__auth_got: 0x1328
+  __AUTH.__objc_data: 0x1c70
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x2950
+  __DATA.__objc_ivar: 0x2960
   __DATA.__data: 0x2e48
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_ivar: 0x12b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22285
-  Symbols:   34322
-  CStrings:  16577
+  Functions: 22317
+  Symbols:   34379
+  CStrings:  16596
 
Symbols:
+ +[RTBiomeManager _isOnOffStreamType:]
+ +[RTBiomeManager batteryLevelStream]
+ +[RTCheckInMetricsProvider _indexesOfIntervals:]
+ +[RTPersistenceMirroringManager exportMirroringIsAvailableForLastImportDate:referenceDate:]
+ -[RTBiomeBatteryLevel .cxx_destruct]
+ -[RTBiomeBatteryLevel date]
+ -[RTBiomeBatteryLevel initWithDate:percentage:]
+ -[RTBiomeBatteryLevel init]
+ -[RTBiomeBatteryLevel percentage]
+ -[RTBiomeManager _onStateForEvent:streamType:]
+ -[RTBiomeManager enumerateBatteryLevelsWithinDateInterval:handler:]
+ -[RTBiomeManager enumerateStateChangesWithinDateInterval:streamType:handler:]
+ -[RTBiomeManager setSynchronousReadTimeout:]
+ -[RTBiomeManager synchronousReadTimeout]
+ -[RTBiomeStateChange .cxx_destruct]
+ -[RTBiomeStateChange date]
+ -[RTBiomeStateChange initWithDate:on:]
+ -[RTBiomeStateChange init]
+ -[RTBiomeStateChange on]
+ -[RTCheckInMetricsProvider _batteryLevelsForWindow:]
+ -[RTCheckInMetricsProvider _bootSessionOutagesForWindow:]
+ -[RTCheckInMetricsProvider _buildStatesForWindow:homeIntervals:homeKeys:majorityKey:homeFields:lockFields:motionFields:powerFields:mask:]
+ -[RTCheckInMetricsProvider _homeDaysInWindowStartingDay:visits:zone:shift:]
+ -[RTCheckInMetricsProvider _lockedIntervalsForWindow:known:]
+ -[RTCheckInMetricsProvider _onIntervalsForStreamType:window:known:]
+ -[RTCheckInMetricsProvider _outagesForWindow:plugged:poweredOff:died:]
+ -[RTCheckInMetricsProvider _payloadsForHomeFields:lockFields:motionFields:powerFields:startDay:outcome:ageBand:rowId:]
+ -[RTCheckInMetricsProvider _pluggedIntervalsForWindow:known:]
+ -[RTCheckInMetricsProvider _sendPayloadsIfConsented:]
+ -[RTCheckInMetricsProvider _submitWindowForToday:submitted:deferred:error:]
+ -[RTCheckInMetricsProvider fetchTimeout]
+ -[RTCheckInMetricsProvider initWithAccountManager:biomeManager:defaultsManager:learnedLocationManager:managedConfiguration:xpcActivityManager:]
+ -[RTCheckInMetricsProvider setFetchTimeout:]
+ -[RTPersistenceMirroringManager _captureBugForDeletionEnforcementError:]
+ -[RTPersistenceMirroringManager initWithAccountManager:defaultsManager:mirroringPolicies:persistenceCloudDeletionEnforcer:persistenceManager:platform:reachabilityManager:timerManager:xpcActivityManager:]
+ GCC_except_table64
+ _OBJC_CLASS_$_RTBiomeBatteryLevel
+ _OBJC_CLASS_$_RTBiomeStateChange
+ _OBJC_IVAR_$_RTBiomeBatteryLevel._date
+ _OBJC_IVAR_$_RTBiomeBatteryLevel._percentage
+ _OBJC_IVAR_$_RTBiomeStateChange._date
+ _OBJC_IVAR_$_RTBiomeStateChange._on
+ _OBJC_METACLASS_$_RTBiomeBatteryLevel
+ _OBJC_METACLASS_$_RTBiomeStateChange
+ _RTCheckInClassifyOutages
+ _RTCheckInNewestClosedDay
+ _RTCheckInOnIntervalsFromChanges
+ _RTCheckInOutagesFromBootChanges
+ _RTCheckInQuietStateForSlice
+ _RTCheckInSpanListCovered
+ _RTCheckInSpanListMake
+ _RTCheckInSubtractIntervals
+ __OBJC_$_CLASS_METHODS_RTCheckInMetricsProvider
+ __OBJC_$_INSTANCE_METHODS_RTBiomeBatteryLevel
+ __OBJC_$_INSTANCE_METHODS_RTBiomeStateChange
+ __OBJC_$_INSTANCE_VARIABLES_RTBiomeBatteryLevel
+ __OBJC_$_INSTANCE_VARIABLES_RTBiomeStateChange
+ __OBJC_$_PROP_LIST_RTBiomeBatteryLevel
+ __OBJC_$_PROP_LIST_RTBiomeStateChange
+ __OBJC_CLASS_RO_$_RTBiomeBatteryLevel
+ __OBJC_CLASS_RO_$_RTBiomeStateChange
+ __OBJC_METACLASS_RO_$_RTBiomeBatteryLevel
+ __OBJC_METACLASS_RO_$_RTBiomeStateChange
+ ___137-[RTCheckInMetricsProvider _buildStatesForWindow:homeIntervals:homeKeys:majorityKey:homeFields:lockFields:motionFields:powerFields:mask:]_block_invoke
+ ___52-[RTCheckInMetricsProvider _batteryLevelsForWindow:]_block_invoke
+ ___53-[RTCheckInMetricsProvider _sendPayloadsIfConsented:]_block_invoke
+ ___57-[RTCheckInMetricsProvider _bootSessionOutagesForWindow:]_block_invoke
+ ___67-[RTBiomeManager enumerateBatteryLevelsWithinDateInterval:handler:]_block_invoke
+ ___67-[RTBiomeManager enumerateBatteryLevelsWithinDateInterval:handler:]_block_invoke_2
+ ___67-[RTCheckInMetricsProvider _onIntervalsForStreamType:window:known:]_block_invoke
+ ___72-[RTPersistenceMirroringManager _captureBugForDeletionEnforcementError:]_block_invoke
+ ___77-[RTBiomeManager enumerateStateChangesWithinDateInterval:streamType:handler:]_block_invoke
+ ___77-[RTBiomeManager enumerateStateChangesWithinDateInterval:streamType:handler:]_block_invoke_2
+ ___RTCheckInClassifyOutages_block_invoke
+ ___RTCheckInClassifyOutages_block_invoke_2
+ ___RTCheckInOnIntervalsFromChanges_block_invoke
+ ___RTCheckInOutagesFromBootChanges_block_invoke
+ ___block_descriptor_32_e51_q24?0"RTBiomeStateChange"8"RTBiomeStateChange"16l
+ ___block_descriptor_32_e53_q24?0"RTBiomeBatteryLevel"8"RTBiomeBatteryLevel"16l
+ ___block_descriptor_40_e8_32s_e22_v16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_56_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e22_v16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r_e19_v16?0"IMSPIChat"8ls32l8s40l8r56l8s48l8
+ _arc4random_buf
+ _kRTCheckInPartCount
+ _kRTCheckInSlicesPerPart
+ _kRTCheckInWindowFieldCount
- -[RTCheckInMetricsProvider _buildStatesForWindow:homeIntervals:homeKeys:majorityKey:homeFields:lockFields:motionFields:mask:]
- -[RTCheckInMetricsProvider _chooseWindowStart:longestRun:visits:zone:shift:newestDay:]
- -[RTCheckInMetricsProvider _coreMotionStationaryIntervalsForWindow:]
- -[RTCheckInMetricsProvider _payloadForHomeFields:lockFields:motionFields:startDay:outcome:ageBand:]
- -[RTCheckInMetricsProvider _sendPayloadIfConsented:]
- -[RTCheckInMetricsProvider _submitWindowEndingDay:submitted:deferred:error:]
- -[RTCheckInMetricsProvider initWithAccountManager:biomeManager:defaultsManager:learnedLocationManager:managedConfiguration:motionActivityManager:xpcActivityManager:]
- -[RTCheckInMetricsProvider motionActivityManager]
- -[RTPersistenceMirroringManager exportMirroringIsAvailableWithExpirationEnforcer:expirationDate:context:error:]
- -[RTPersistenceMirroringManager initWithAccountManager:defaultsManager:mirroringPolicies:persistenceCloudDeletionEnforcer:persistenceExpirationEnforcer:persistenceManager:platform:reachabilityManager:timerManager:xpcActivityManager:]
- -[RTPersistenceMirroringManager onExpiredRecordsRemoved:]
- -[RTPersistenceMirroringManager persistenceExpirationEnforcer]
- -[RTPersistenceMirroringManager setPersistenceExpirationEnforcer:]
- _RTCheckInCoverageForIntervals
- _RTCheckInDeriveQuietFields
- _RTCheckInEnvelopeForIntervals
- _RTCheckInGetQuiet
- _RTCheckInOverlap
- _RTCheckInQuietCount
- _RTCheckInSetQuiet
- _RTCheckInStationaryIntervalsFromActivities
- _RTPersistenceExpirationEnforcerDidRemoveExpiredRecordsNotificationName
- ___52-[RTCheckInMetricsProvider _sendPayloadIfConsented:]_block_invoke
- ___57-[RTPersistenceMirroringManager onExpiredRecordsRemoved:]_block_invoke
- ___68-[RTCheckInMetricsProvider _coreMotionStationaryIntervalsForWindow:]_block_invoke
- ___RTCheckInStationaryIntervalsFromActivities_block_invoke
- ___block_descriptor_32_e47_q24?0"RTMotionActivity"8"RTMotionActivity"16l
- ___block_descriptor_48_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
- _kRTCheckInQuietFieldCount
- _kRTCheckInSlicesPerQuietField
CStrings:
+ "%@, %@, chat guid, %{sensitive}@, handles count, %lu, isGroup, %@"
+ "%@, %@, final output date interval, %{sensitive}@"
+ "%@, %@, levels, %lu"
+ "%@, %@, output date interval, %{sensitive}@"
+ "%@, %@, streamType, %@, changes, %lu"
+ "%@, %@, streamType, %@, date interval, %{sensitive}@"
+ "%@, %@, streamType, %@, date interval, %{sensitive}@, outputDateIntervals count, %lu"
+ "%@, %lu days at home in the window, need %lu"
+ "%@, diagnostics not available, cannot capture bug for deletion enforcement failure"
+ "%@, event no longer collected, not submitting"
+ "%@, exporting available, %{public}@, last import, %@"
+ "%@, ignoring last import value of unexpected type, %{public}@"
+ "%@, startDay, %lld, window, %{sensitive}@, outcome, %lu, home days, %lu, majority home slices, %lu, other home slices, %lu, away slices, %lu, lock not known, %lu, motion not known, %lu, power not known, %lu, plugged slices, %lu, battery died slices, %lu, signals, %lu"
+ "%@, window has home days but no home time, so the count and the clip disagree"
+ "(no error)"
+ "-[RTBiomeManager _compareEvent1:event2:streamType:]"
+ "-[RTBiomeManager _extractDateIntervalFromBiomeEvent1:event2:streamType:]"
+ "A Biome read failed."
+ "CorePersonalization"
+ "CorePersonalizationDaemon"
+ "CoreRoutine.AlwaysOnCheckInV3"
+ "DeletionEnforcementFailedAfterImport: %@ %ld"
+ "Device Boot Session"
+ "Failed to capture bug for deletion enforcement failure: %@"
+ "Invalid parameter not satisfying: outDied"
+ "Invalid parameter not satisfying: outPoweredOff"
+ "Invalid parameter not satisfying: powerFields"
+ "No battery level stream."
+ "RTDefaultsCheckInLastSubmissionDateV3"
+ "Read boot session as state changes."
+ "Stream type has no on/off state."
+ "Unhandled stream type, %lu (in %s:%d)"
+ "check-in metrics, %@ changes, %lu, longest hold, %.1f h"
+ "check-in metrics, %@ changes, error, %@"
+ "check-in metrics, battery levels, error, %@"
+ "check-in metrics, boot session, error, %@"
+ "check-in metrics, outages, %lu, powered off, %lu, battery died, %lu"
+ "part"
+ "powerState%lu"
+ "q24@?0@\"RTBiomeBatteryLevel\"8@\"RTBiomeBatteryLevel\"16"
+ "q24@?0@\"RTBiomeStateChange\"8@\"RTBiomeStateChange\"16"
+ "rowId"
- "%@, %@, final output date interval, %@"
- "%@, %@, output date interval, %@"
- "%@, %@, streamType, %@, date interval, %@"
- "%@, %@, streamType, %@, date interval, %@, outputDateIntervals count, %lu"
- "%@, chosen window has no home time, so the search and the clip disagree"
- "%@, exporting available, %{public}@"
- "%@, failed to check for expired records, suspending export, error, %@"
- "%@, longest run of days at home was %lu, need %lu consecutive"
- "%@, startDay, %lld, window, %{sensitive}@, outcome, %lu, longest run, %lu, majority home slices, %lu, other home slices, %lu, away slices, %lu, lock not known, %lu, motion not known, %lu, signals, %lu"
- "%@, thin Biome motion for window, %@, biome coverage, %.0f s, CoreMotion coverage, %.0f s"
- "%@, window older than CoreMotion retention, skipping motion fetch"
- "CoreRoutine.AlwaysOnCheckInV2"
- "GenerativeLearning"
- "GenerativeLearningPlatform"
- "Invalid parameter not satisfying: outStartDay"
- "Invalid parameter not satisfying: persistenceExpirationEnforcer"
- "RTPersistenceExpirationEnforcerDidRemoveExpiredRecordsNotificationName"
- "Suspending export mirroring due to expired records."
- "check-in metrics, CoreMotion fetch failed, error, %@"
- "check-in metrics, CoreMotion fetch timed out, error, %@"
- "expirationEnforcer"
- "q24@?0@\"RTMotionActivity\"8@\"RTMotionActivity\"16"
- "quietState%lu"
```
