## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

 7027.0.72.2.7
-  __TEXT.__text: 0x64dd4
-  __TEXT.__objc_methlist: 0x4f24
-  __TEXT.__const: 0x34a
-  __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__cstring: 0x57d2
-  __TEXT.__oslogstring: 0xc32f
+  __TEXT.__text: 0x67ecc
+  __TEXT.__objc_methlist: 0x5104
+  __TEXT.__const: 0x3ca
+  __TEXT.__gcc_except_tab: 0xb4c
+  __TEXT.__cstring: 0x59e2
+  __TEXT.__oslogstring: 0xca8f
   __TEXT.__ustring: 0x86
   __TEXT.__swift5_typeref: 0x47
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x1748
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1940
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c0
+  __DATA_CONST.__objc_selrefs: 0x3610
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0x538
+  __DATA_CONST.__got: 0xee8
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x4760
-  __AUTH_CONST.__objc_const: 0x9a00
-  __AUTH_CONST.__objc_intobj: 0xdb0
+  __AUTH_CONST.__cfstring: 0x4820
+  __AUTH_CONST.__objc_const: 0x9c10
+  __AUTH_CONST.__objc_intobj: 0xdc8
   __AUTH_CONST.__objc_doubleobj: 0x3d0
-  __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__auth_got: 0x890
+  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x868
-  __DATA.__objc_ivar: 0x634
+  __DATA.__objc_ivar: 0x64c
   __DATA.__data: 0x1d60
-  __DATA_DIRTY.__objc_data: 0x1640
+  __DATA_DIRTY.__objc_data: 0x1690
   __DATA_DIRTY.__data: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2077
-  Symbols:   5498
-  CStrings:  1338
+  Functions: 2153
+  Symbols:   5582
+  CStrings:  1365
 
Symbols:
+ +[HDFeatureAvailabilityManager(HypertensionNotifications) hdhr_HypertensionNotificationsV1AvailabilityManagerWithProfile:]
+ +[HDFeatureAvailabilityManager(HypertensionNotifications) hdhr_HypertensionNotificationsV2AvailabilityManagerWithProfile:]
+ +[HKCountrySet(HypertensionNotificationsV2) localAvailabilityForHypertensionNotificationsV2]
+ -[HDHRCarouselUITriggerObserver _mostRecentHypertensionEventSample]
+ -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:algorithmVersion:databaseTransactionContext:error:]
+ -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleWithDateInterval:algorithmVersion:error:]
+ -[HDHRHypertensionNotificationDeliveryEvent initWithProfile:type:algorithmVersion:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaAlgorithmVersionAnalyticsWithDataSource:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager .cxx_destruct]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager _featureSupportedStateForOnboardedV1CountryCodeSupportedState:onboardedV2CountryCodeSupportedState:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager _watchSupportedFeatureIdentifier]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityExtensionDidUpdateRegionAvailability:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityExtensionOnboardingCompletionDataDidBecomeAvailable:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdateOnboardingCompletion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdateSettings:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityRequirementsWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureIdentifier]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager featureOnboardingRecordWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager getFeatureOnboardingRecordWithCompletion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager initWithProfile:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:pairedDeviceCapabilityProvider:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager observers]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager onboardingEligibilityForCountryCode:error:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager pairedDeviceCapabilityProvider]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager pairedFeatureAttributesWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager regionAvailabilityWithError:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager registerObserver:queue:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager resetOnboardingWithCompletion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager saveOnboardingCompletion:settings:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager setFeatureSettingData:forKey:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager setFeatureSettingString:forKey:completion:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager unregisterObserver:]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager v1FeatureAvailabilityManager]
+ -[HDHRHypertensionNotificationsFeatureAvailabilityManager v2FeatureAvailabilityManager]
+ _HDHRAnalyticsPropertyNameAlgorithmVersion
+ _HDHRHypertensionNotificationsAnalysisResultAlgorithmVersionOverride
+ _HKFeatureAvailabilityRequirementIdentifierFeatureFlagIsEnabled
+ _HKFeatureIdentifierHypertensionNotificationsV1
+ _HKFeatureIdentifierHypertensionNotificationsV2
+ _HKHRHypertensionNotificationsV2LocalFeatureAttributes
+ _HKSampleSortIdentifierEndDate
+ _NSStringFromHKFeatureIdentifier
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHRHypertensionNotificationDeliveryEvent._algorithmVersion
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsFeatureAvailabilityManager._observers
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsFeatureAvailabilityManager._pairedDeviceCapabilityProvider
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsFeatureAvailabilityManager._v1FeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsFeatureAvailabilityManager._v2FeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsV1BackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsV2BackgroundFeatureDeliveryManager
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_$_CLASS_METHODS_HDFeatureAvailabilityManager(BPJ|CardioFitness|HypertensionNotifications|HDHRIrregularRhythmNotificationsV2FeatureAvailabilityManager)
+ __OBJC_$_CLASS_METHODS_HKCountrySet(BloodPressureJournal|ElectrocardiogramV2Recording|HypertensionNotifications|HypertensionNotificationsV2|IrregularRhythmNotificationsV2)
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsFeatureAvailabilityManager
+ ___105-[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdateSettings:]_block_invoke
+ ___115-[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityExtensionDidUpdateRegionAvailability:]_block_invoke
+ ___117-[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdateOnboardingCompletion:]_block_invoke
+ ___130-[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityExtensionOnboardingCompletionDataDidBecomeAvailable:]_block_invoke
+ ___157-[HDHRHypertensionNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke
+ ___163-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:algorithmVersion:databaseTransactionContext:error:]_block_invoke
+ ___163-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:algorithmVersion:databaseTransactionContext:error:]_block_invoke_2
+ ___67-[HDHRCarouselUITriggerObserver _mostRecentHypertensionEventSample]_block_invoke
+ ___78-[HDHRHypertensionNotificationsFeatureAvailabilityManager unregisterObserver:]_block_invoke
+ ___82-[HDHRHypertensionNotificationsFeatureAvailabilityManager registerObserver:queue:]_block_invoke
+ ___89-[HDHRHypertensionNotificationsFeatureAvailabilityManager resetOnboardingWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e9_B16?0^8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e20_v20?0B8"NSError"12lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls64l8s32l8s40l8s48l8s56l8
+ _objc_msgSend$_ihaAlgorithmVersionAnalyticsWithDataSource:
+ _objc_msgSend$_mostRecentHypertensionEventSample
+ _objc_msgSend$_watchSupportedFeatureIdentifier
+ _objc_msgSend$hdhr_HypertensionNotificationsV1AvailabilityManagerWithProfile:
+ _objc_msgSend$hdhr_HypertensionNotificationsV2AvailabilityManagerWithProfile:
+ _objc_msgSend$initWithFeatureIdentifier:currentOnboardingVersion:
+ _objc_msgSend$initWithProfile:type:algorithmVersion:
+ _objc_msgSend$initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:pairedDeviceCapabilityProvider:
+ _objc_msgSend$localAvailabilityForHypertensionNotificationsV2
+ _objc_msgSend$requirementSetForFeatureIdentifier:
+ _objc_msgSend$setFeatureSettingData:forKey:completion:
+ _objc_msgSend$setFeatureSettingString:forKey:completion:
- -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]
- -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleWithDateInterval:error:]
- -[HDHRHypertensionNotificationDeliveryEvent initWithProfile:type:]
- _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsBackgroundFeatureDeliveryManager
- __OBJC_$_CLASS_METHODS_HDFeatureAvailabilityManager(BPJ|CardioFitness|HDHRIrregularRhythmNotificationsV2FeatureAvailabilityManager)
- __OBJC_$_CLASS_METHODS_HKCountrySet(BloodPressureJournal|ElectrocardiogramV2Recording|HypertensionNotifications|IrregularRhythmNotificationsV2)
- ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke
- ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e9_B16?0^8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
- _objc_msgSend$initWithProfile:type:
CStrings:
+ "!!! [HDHRHypertensionMeasurementAnalyzer] Overriding analyzer result, algorithm version: %@"
+ "%{public}s Failed to determine V2 device capability support with error: %{public}@"
+ "%{public}s Returning requirement set for %{public}@"
+ "-[HDHRHypertensionNotificationsFeatureAvailabilityManager _watchSupportedFeatureIdentifier]"
+ "-[HDHRHypertensionNotificationsFeatureAvailabilityManager featureAvailabilityRequirementsWithError:]"
+ "AnalysisResultAlgorithmVersionOverride"
+ "HKCountrySet+HypertensionNotificationsV2.m"
+ "Saving HKOnboardingCompletion directly is not supported for %@ (combined feature identifier)"
+ "Unable to determine paired feature attributes for Hypertension Notifications without onboarding completion"
+ "[%{public}@] Analysis result override was set without an algorithm version override"
+ "[%{public}@] Error checking onboarded country code supported state for Hypertension Notifications 1.0, returning supported state for 2.0: %{public}@"
+ "[%{public}@] Error checking onboarded country code supported state for Hypertension Notifications 2.0, returning supported state for 1.0: %{public}@"
+ "[%{public}@] Error getting region availability for Hypertension Notifications 1.0, returning availability for 2.0: %{public}@"
+ "[%{public}@] Error getting region availability for Hypertension Notifications 2.0, returning availability for 1.0: %{public}@"
+ "[%{public}@] Failed to complete onboarding using the 1.0 extension: %{public}@"
+ "[%{public}@] Failed to complete onboarding using the 2.0 extension: %{public}@"
+ "[%{public}@] Failed to query most recent hypertension event sample: %@"
+ "[%{public}@] Failed to reset onboarding for %{public}@ using the 1.0 extension: %{public}@"
+ "[%{public}@] Failed to reset onboarding for %{public}@ using the 2.0 extension: %{public}@"
+ "[%{public}@] Failed to retrieve lowest onboarding version completed with the 1.0 extension: %{public}@"
+ "[%{public}@] Failed to retrieve lowest onboarding version completed with the 2.0 extension: %{public}@"
+ "[%{public}@] Failed to retrieve onboarding record with the 1.0 extension: %{public}@"
+ "[%{public}@] Failed to retrieve onboarding record with the 2.0 extension: %{public}@"
+ "[%{public}@] No intersection of unavailability reasons for %{public}@ and %{public}@: %{public}@ (v1) | %{public}@ (v2)"
+ "[%{public}@] Unable to determine paired feature attributes for Hypertension Notifications without onboarding completion"
+ "algorithmVersion"
+ "d2f9b521-e715-4a96-94f9-19c209511ee5"
+ "\xf0\xf1"
- "\xf0\xe1"
```
