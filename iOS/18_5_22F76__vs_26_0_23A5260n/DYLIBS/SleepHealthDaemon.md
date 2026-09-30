## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0xabc0
+6074.1.2.4.0
+  __TEXT.__text: 0xaf48
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0xa94
+  __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x62a
-  __TEXT.__oslogstring: 0x17fe
+  __TEXT.__cstring: 0x64a
+  __TEXT.__oslogstring: 0x1831
   __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x34d
-  __TEXT.__objc_methname: 0x30a4
-  __TEXT.__objc_methtype: 0x95f
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_classname: 0x36e
+  __TEXT.__objc_methname: 0x31d4
+  __TEXT.__objc_methtype: 0xa28
   __TEXT.__objc_stubs: 0x2220
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xaf8
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x1420
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1520
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xb0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x660
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BreathingAlgorithms.framework/BreathingAlgorithms
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3662E3E-FA91-3619-B6AC-EA5D0ECA76AF
-  Functions: 156
-  Symbols:   1021
-  CStrings:  699
+  UUID: 5392344C-CB3E-3881-A729-215F548FF37C
+  Functions: 159
+  Symbols:   1039
+  CStrings:  722
 
Symbols:
+ +[HDSHReplaceSleepSamplesOperation supportsSecureCoding]
+ -[HDSHBreathingDisturbanceAnalyzer _createEnumeratorWithAnalysisInterval:profile:includeTimeZones:]
+ -[HDSHBreathingDisturbanceAnalyzer fetchSamplesWithAnalysisInterval:profile:includeTimeZones:error:]
+ -[HDSHReplaceSleepSamplesOperation .cxx_destruct]
+ -[HDSHReplaceSleepSamplesOperation encodeWithCoder:]
+ -[HDSHReplaceSleepSamplesOperation initWithCoder:]
+ -[HDSHReplaceSleepSamplesOperation initWithSleepSamplesToInsert:source:replacementInterval:accessibilityAssertion:]
+ -[HDSHReplaceSleepSamplesOperation performWithProfile:transaction:error:]
+ -[HDSHReplaceSleepSamplesOperation transactionContext]
+ -[HDSHSleepApneaControlServer remote_getBreathingDisturbanceSamplesInDateInterval:includeTimeZones:completion:]
+ _HDDataEntityEncodingOptionIncludeAutomaticTimeZone
+ _OBJC_CLASS_$_HDJournalableOperation
+ _OBJC_CLASS_$_HDSHReplaceSleepSamplesOperation
+ _OBJC_CLASS_$_HKSource
+ _OBJC_METACLASS_$_HDJournalableOperation
+ _OBJC_METACLASS_$_HDSHReplaceSleepSamplesOperation
+ __OBJC_$_CLASS_METHODS_HDSHReplaceSleepSamplesOperation
+ __OBJC_$_INSTANCE_METHODS_HDSHReplaceSleepSamplesOperation
+ __OBJC_$_INSTANCE_VARIABLES_HDSHReplaceSleepSamplesOperation
+ __OBJC_CLASS_RO_$_HDSHReplaceSleepSamplesOperation
+ __OBJC_METACLASS_RO_$_HDSHReplaceSleepSamplesOperation
+ ___100-[HDSHBreathingDisturbanceAnalyzer fetchSamplesWithAnalysisInterval:profile:includeTimeZones:error:]_block_invoke
+ ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.348
+ ___64-[HDSHReplaceSleepSamplesOperation _performNanoSyncWithProfile:]_block_invoke
+ ___65-[HDSHReplaceSleepSamplesOperation _performCloudSyncWithProfile:]_block_invoke
+ ___73-[HDSHReplaceSleepSamplesOperation performWithProfile:transaction:error:]_block_invoke
+ ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.308
+ ___block_literal_global.304
+ ___kCFBooleanTrue
+ _objc_msgSend$_createEnumeratorWithAnalysisInterval:profile:includeTimeZones:
+ _objc_msgSend$addEncodingOptionsFromDictionary:
+ _objc_msgSend$contextForWritingProtectedData
+ _objc_msgSend$contextWithAccessibilityAssertion:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$fetchSamplesWithAnalysisInterval:profile:includeTimeZones:error:
+ _objc_msgSend$hd_sourceForClient:bundleIdentifier:
+ _objc_msgSend$initWithSleepSamplesToInsert:source:replacementInterval:accessibilityAssertion:
+ _objc_msgSend$onCommit:orRollback:
+ _objc_msgSend$performOrJournalWithProfile:error:
+ _objc_msgSend$sourceEntityForClientSource:createOrUpdateIfNecessary:error:
- -[HDSHBreathingDisturbanceAnalyzer _createEnumeratorWithAnalysisInterval:profile:]
- -[HDSHBreathingDisturbanceAnalyzer fetchSamplesWithAnalysisInterval:profile:error:]
- -[HDSHPluginServer _deleteSleepSamplesWithClientSourceInDateInterval:error:]
- -[HDSHPluginServer _insertSleepSamplesWithClientSource:replacingSamplesInDateInterval:error:]
- -[HDSHPluginServer _performCloudSync]
- -[HDSHPluginServer _performNanoSyncWithAccessibilityAssertion:]
- -[HDSHSleepApneaControlServer remote_getBreathingDisturbanceSamplesInDateInterval:completion:]
- ___104-[HDSHPluginServer _saveSleepTrackingSamplesAfterFirstUnlock:replacingSamplesInDateInterval:completion:]_block_invoke
- ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.345
- ___37-[HDSHPluginServer _performCloudSync]_block_invoke
- ___63-[HDSHPluginServer _performNanoSyncWithAccessibilityAssertion:]_block_invoke
- ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.305
- ___83-[HDSHBreathingDisturbanceAnalyzer fetchSamplesWithAnalysisInterval:profile:error:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e9_B16?0^8ls32l8s40l8s48l8
- ___block_literal_global.301
- _objc_msgSend$_createEnumeratorWithAnalysisInterval:profile:
- _objc_msgSend$_deleteSleepSamplesWithClientSourceInDateInterval:error:
- _objc_msgSend$_insertSleepSamplesWithClientSource:replacingSamplesInDateInterval:error:
- _objc_msgSend$_performCloudSync
- _objc_msgSend$_performNanoSyncWithAccessibilityAssertion:
- _objc_msgSend$addAccessibilityAssertion:
- _objc_msgSend$featureFlagIsEnabled:
- _objc_msgSend$features
- _objc_msgSend$fetchSamplesWithAnalysisInterval:profile:error:
- _objc_msgSend$nebula
- _objc_msgSend$performWithTransactionContext:error:block:
- _objc_msgSend$sourceForClient:error:
- _objc_msgSend$updateCriteria
CStrings:
+ "@\"HKSource\""
+ "@\"NSArray\""
+ "@\"NSDateInterval\""
+ "@36@0:8@16@24B32"
+ "@44@0:8@16@24B32^@36"
+ "HDSHReplaceSleepSamplesOperation"
+ "[%{public}@] Deleting sleep samples source: %@, dateInterval: %@"
+ "[%{public}@] Failed to retrieve source entity for deletion: %@"
+ "[%{public}@] Failed to retrieve source entity for insertion: %@"
+ "[%{public}@] Inserting sleep samples for source: %@"
+ "_createEnumeratorWithAnalysisInterval:profile:includeTimeZones:"
+ "_replacementInterval"
+ "_sleepSamples"
+ "_source"
+ "addEncodingOptionsFromDictionary:"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "contextForWritingProtectedData"
+ "contextWithAccessibilityAssertion:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "fetchSamplesWithAnalysisInterval:profile:includeTimeZones:error:"
+ "hd_sourceForClient:bundleIdentifier:"
+ "initWithCoder:"
+ "initWithSleepSamplesToInsert:source:replacementInterval:accessibilityAssertion:"
+ "invalidateAndWait"
+ "onCommit:orRollback:"
+ "performOrJournalWithProfile:error:"
+ "performWithProfile:transaction:error:"
+ "remote_getBreathingDisturbanceSamplesInDateInterval:includeTimeZones:completion:"
+ "replacement_interval"
+ "sleep_samples"
+ "sourceEntityForClientSource:createOrUpdateIfNecessary:error:"
+ "supportsSecureCoding"
+ "transactionContext"
+ "v36@0:8@\"NSDateInterval\"16B24@?<v@?@\"NSArray\">28"
+ "v36@0:8@16B24@?28"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "@40@0:8@16@24^@32"
- "B16@?0^@8"
- "[%{public}@] Deleting for client: %@, source: %@, dateInterval: %@"
- "[%{public}@] adding accessibility assertion to transaction context"
- "[%{public}@] failed to save samples with error: %{public}@"
- "_createEnumeratorWithAnalysisInterval:profile:"
- "_deleteSleepSamplesWithClientSourceInDateInterval:error:"
- "_insertSleepSamplesWithClientSource:replacingSamplesInDateInterval:error:"
- "_performCloudSync"
- "_performNanoSyncWithAccessibilityAssertion:"
- "addAccessibilityAssertion:"
- "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
- "featureFlagIsEnabled:"
- "features"
- "fetchSamplesWithAnalysisInterval:profile:error:"
- "nebula"
- "performWithTransactionContext:error:block:"
- "remote_getBreathingDisturbanceSamplesInDateInterval:completion:"
- "sourceForClient:error:"
- "updateCriteria"
- "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\">24"

```
