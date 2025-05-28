## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x424d8
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x2af8
+4146.4.18.0.0
+  __TEXT.__text: 0x42790
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x2b28
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x54c
-  __TEXT.__cstring: 0x2e24
-  __TEXT.__oslogstring: 0x76d1
-  __TEXT.__unwind_info: 0xf04
-  __TEXT.__objc_classname: 0x157c
-  __TEXT.__objc_methname: 0xbf3a
-  __TEXT.__objc_methtype: 0x2d68
-  __TEXT.__objc_stubs: 0x7760
+  __TEXT.__cstring: 0x2e49
+  __TEXT.__oslogstring: 0x76e8
+  __TEXT.__unwind_info: 0xf08
+  __TEXT.__objc_classname: 0x15e5
+  __TEXT.__objc_methname: 0xc03a
+  __TEXT.__objc_methtype: 0x2db7
+  __TEXT.__objc_stubs: 0x7780
   __DATA_CONST.__got: 0x540
   __DATA_CONST.__const: 0xe20
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x63d0
-  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_const: 0x6520
+  __DATA_CONST.__objc_selrefs: 0x22d8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x628
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x480
-  __AUTH_CONST.__objc_const: 0x1880
-  __AUTH_CONST.__cfstring: 0x2900
+  __AUTH_CONST.__cfstring: 0x2920
+  __AUTH_CONST.__objc_const: 0x18c8
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x620
-  __DATA.__objc_superrefs: 0x1d0
-  __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x1810
+  __DATA.__objc_ivar: 0x418
+  __DATA.__data: 0x1870
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__objc_data: 0xf50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1359
-  Symbols:   5409
-  CStrings:  2700
+  Functions: 1363
+  Symbols:   5433
+  CStrings:  2711
 
Symbols:
+ -[HDHRAFibBurdenRescindedNotificationManager initWithProfile:featureStatusProvider:keyValueDomain:queue:]
+ -[HDHRAFibBurdenRescindedNotificationManager initWithProfile:featureStatusProvider:queueOverride:]
+ -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager _onboardedCountryCodeSupportedStateWithOnboardingCompletion:error:]
+ -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager featureOnboardingRecordWithError:].cold.2
+ -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:deviceSupportedProvider:availabilityRequirementSet:cacheDefaults:isStandalone:]
+ -[HDHRElectrocardiogramRecordingV2UpgradeManager _v1featureSettingsUponBackgroundDelivery]
+ -[HDHRElectrocardiogramV1DeviceSupportedStateProvider isDeviceSupported:]
+ -[HDHRElectrocardiogramV2DeviceSupportedStateProvider isDeviceSupported:]
+ _NSStringFromHKFeatureAvailabilityOnboardedCountrySupportedState
+ _OBJC_CLASS_$_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ _OBJC_CLASS_$_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ _OBJC_IVAR_$_HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager._deviceSupportedProvider
+ _OBJC_METACLASS_$_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ _OBJC_METACLASS_$_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_$_INSTANCE_METHODS_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ __OBJC_$_INSTANCE_METHODS_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_$_PROP_LIST_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ __OBJC_$_PROP_LIST_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDHRElectrocardiogramDeviceSupportedStateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDHRElectrocardiogramDeviceSupportedStateProvider
+ __OBJC_$_PROTOCOL_REFS_HDHRElectrocardiogramDeviceSupportedStateProvider
+ __OBJC_CLASS_PROTOCOLS_$_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ __OBJC_CLASS_PROTOCOLS_$_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_CLASS_RO_$_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ __OBJC_CLASS_RO_$_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_LABEL_PROTOCOL_$_HDHRElectrocardiogramDeviceSupportedStateProvider
+ __OBJC_METACLASS_RO_$_HDHRElectrocardiogramV1DeviceSupportedStateProvider
+ __OBJC_METACLASS_RO_$_HDHRElectrocardiogramV2DeviceSupportedStateProvider
+ __OBJC_PROTOCOL_$_HDHRElectrocardiogramDeviceSupportedStateProvider
+ ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.301
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.265
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.265.cold.1
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.266
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.266.cold.1
+ ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.268
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.270
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.270.cold.1
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.271
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.307
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.307.cold.1
+ ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.298
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.274
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.274.cold.1
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.276
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.276.cold.1
+ ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.247
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.257
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.258
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.349
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.349.cold.1
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.242
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.242.cold.1
+ ___block_literal_global.244
+ ___block_literal_global.269
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.356
+ __unnamed_array_storage.253
+ __unnamed_array_storage.350
+ __unnamed_array_storage.361
+ __unnamed_array_storage.383
+ __unnamed_array_storage.472
+ _objc_msgSend$_onboardedCountryCodeSupportedStateWithOnboardingCompletion:error:
+ _objc_msgSend$initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:deviceSupportedProvider:availabilityRequirementSet:cacheDefaults:isStandalone:
+ _objc_msgSend$initWithProfile:featureStatusProvider:keyValueDomain:queue:
+ _objc_msgSend$isDeviceSupported:
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager _isFeatureSupportedOnDevice:]
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager _onboardingCompletionWithError:].cold.1
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:availabilityRequirementSet:cacheDefaults:isStandalone:]
- -[HDHRElectrocardiogramRecordingV1SettingsProvider featureSettingsUponBackgroundDelivery]
- _OBJC_CLASS_$_HDHRElectrocardiogramRecordingV1SettingsProvider
- _OBJC_METACLASS_$_HDHRElectrocardiogramRecordingV1SettingsProvider
- __OBJC_$_INSTANCE_METHODS_HDHRElectrocardiogramRecordingV1SettingsProvider
- __OBJC_CLASS_PROTOCOLS_$_HDHRElectrocardiogramRecordingV1SettingsProvider
- __OBJC_CLASS_RO_$_HDHRElectrocardiogramRecordingV1SettingsProvider
- __OBJC_METACLASS_RO_$_HDHRElectrocardiogramRecordingV1SettingsProvider
- ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.277
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.241
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.241.cold.1
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.242
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.242.cold.1
- ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.244
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.246
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.246.cold.1
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.247
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.283
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.283.cold.1
- ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.274
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.250
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.250.cold.1
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.252
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.252.cold.1
- ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.223
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.233
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.234
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.325
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.325.cold.1
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.218
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.218.cold.1
- ___block_literal_global.220
- ___block_literal_global.245
- ___block_literal_global.249
- ___block_literal_global.251
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.332
- __unnamed_array_storage.229
- __unnamed_array_storage.326
- __unnamed_array_storage.337
- __unnamed_array_storage.359
- __unnamed_array_storage.448
- _objc_msgSend$ECGV2UpgradeV2
- _objc_msgSend$featureSettingsUponBackgroundDelivery
- _objc_msgSend$initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:availabilityRequirementSet:cacheDefaults:isStandalone:
CStrings:
+ "\x17\x11"
+ "16625FBA-E847-4494-8191-433915DC9F15"
+ "@\"<HDHRElectrocardiogramDeviceSupportedStateProvider>\""
+ "@92@0:8@16@24Q32@40@48@56@64@72@80B88"
+ "B24@0:8@\"NRDevice\"16"
+ "HDHRElectrocardiogramDeviceSupportedStateProvider"
+ "HDHRElectrocardiogramV1DeviceSupportedStateProvider"
+ "HDHRElectrocardiogramV2DeviceSupportedStateProvider"
+ "T@\"NSString\",?,R,C"
+ "[%{public}@] ECG is not onboarded"
+ "[%{public}@] No record of onboarding found, assuming not onboarded"
+ "_deviceSupportedProvider"
+ "_onboardedCountryCodeSupportedStateWithOnboardingCompletion:error:"
+ "initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:deviceSupportedProvider:availabilityRequirementSet:cacheDefaults:isStandalone:"
+ "initWithProfile:featureStatusProvider:keyValueDomain:queue:"
+ "initWithProfile:featureStatusProvider:queueOverride:"
+ "isDeviceSupported:"
- "\x16\x11"
- "@84@0:8@16@24Q32@40@48@56@64@72B80"
- "ECGV2UpgradeV2"
- "HDHRElectrocardiogramRecordingV1SettingsProvider"
- "[%{public}@] Can't read ECG onboarding completion date with error: %{public}@"
- "initWithProfile:featureIdentifier:onboardingVersion:pairedFeatureAttributesProvider:disableAndExpiryProvider:regionAvailabilityProvider:availabilityRequirementSet:cacheDefaults:isStandalone:"

```
