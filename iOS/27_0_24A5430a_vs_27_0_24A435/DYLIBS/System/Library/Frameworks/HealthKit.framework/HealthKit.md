## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

 7027.0.72.2.7
-  __TEXT.__text: 0x3f82ac
-  __TEXT.__objc_methlist: 0x317c4
-  __TEXT.__cstring: 0x37d12
-  __TEXT.__const: 0x16218c
+  __TEXT.__text: 0x3f8d30
+  __TEXT.__objc_methlist: 0x318fc
+  __TEXT.__cstring: 0x380c2
+  __TEXT.__const: 0x16219c
   __TEXT.__oslogstring: 0xd8f3
-  __TEXT.__gcc_except_tab: 0x3f80
+  __TEXT.__gcc_except_tab: 0x3ff0
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__ustring: 0x1d8
   __TEXT.__constg_swiftt: 0x569c
   __TEXT.__swift5_typeref: 0x5275
   __TEXT.__swift5_builtin: 0x53c
-  __TEXT.__swift5_reflstr: 0x36bb
-  __TEXT.__swift5_fieldmd: 0x5320
+  __TEXT.__swift5_reflstr: 0x37cb
+  __TEXT.__swift5_fieldmd: 0x5338
   __TEXT.__swift5_assocty: 0x1578
   __TEXT.__swift5_proto: 0x1954
   __TEXT.__swift5_types: 0x738

   __TEXT.__swift_as_cont: 0x354
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x13458
+  __TEXT.__unwind_info: 0x134a8
   __TEXT.__eh_frame: 0x7b00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10478
-  __DATA_CONST.__objc_classlist: 0x1bd0
+  __DATA_CONST.__const: 0x104a8
+  __DATA_CONST.__objc_classlist: 0x1be0
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x848
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12070
+  __DATA_CONST.__objc_selrefs: 0x120e0
   __DATA_CONST.__objc_protorefs: 0x640
-  __DATA_CONST.__objc_superrefs: 0x17a8
-  __DATA_CONST.__objc_arraydata: 0x69e0
-  __DATA_CONST.__got: 0x1e08
-  __AUTH_CONST.__const: 0x13de9
-  __AUTH_CONST.__cfstring: 0x338a0
-  __AUTH_CONST.__objc_const: 0x53528
+  __DATA_CONST.__objc_superrefs: 0x17b0
+  __DATA_CONST.__objc_arraydata: 0x6a00
+  __DATA_CONST.__got: 0x1e10
+  __AUTH_CONST.__const: 0x13e69
+  __AUTH_CONST.__cfstring: 0x33ae0
+  __AUTH_CONST.__objc_const: 0x53780
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x46b0
-  __AUTH_CONST.__objc_arrayobj: 0x768
+  __AUTH_CONST.__objc_intobj: 0x46c8
+  __AUTH_CONST.__objc_arrayobj: 0x780
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__auth_got: 0x2028
-  __AUTH.__objc_data: 0xf2c8
+  __AUTH.__objc_data: 0xf368
   __AUTH.__data: 0x34e8
-  __DATA.__objc_ivar: 0x2f88
+  __DATA.__objc_ivar: 0x2f9c
   __DATA.__data: 0xfdb0
   __DATA.__common: 0xa00
   __DATA_DIRTY.__objc_data: 0x2738

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 29661
-  Symbols:   41731
-  CStrings:  9196
+  Functions: 29686
+  Symbols:   41789
+  CStrings:  9230
 
Symbols:
+ +[HKFeatureAvailabilityRequirementEntitlement userDefaultsHeartRatePreferencesDomainReadAccessEntitlement]
+ +[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled requirementIdentifier]
+ +[HKFeatureAvailabilityRequirements greenLightMeasurementsAreEnabled]
+ +[HKHeartRatePreferencesConstants domain]
+ +[HKHeartRatePreferencesConstants enableGreenLightMeasurementsDuringTheaterModeKey]
+ +[HKHeartRatePreferencesConstants enableGreenLightMeasurementsKey]
+ +[HKHeartRatePreferencesConstants lastModifiedPreferencesDateKey]
+ +[HKUserDefaultsDataSource heartRatePreferencesDataSource]
+ -[HKFeatureAvailabilityRequirementEvaluationDataSource heartRatePreferencesDataSource]
+ -[HKFeatureAvailabilityRequirementEvaluationDataSource initWithHealthDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:heartRatePreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:authorizationRecordDataSource:]
+ -[HKFeatureAvailabilityRequirementEvaluationDataSource initWithHealthDataSource:featureAvailabilityProvidingDataSource:featureStatusProvidingDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:heartRatePreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:healthDataRequirementDataSource:importExclusionDeviceDataSource:authorizationRecordDataSource:]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled defaultBoolValueWhenKeyIsMissing]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled init]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled isSatisfiedForBoolValue:]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled requiredEntitlements]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled requirementDescription]
+ -[HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled whichUserDefaultsDataSourceInDataSource:]
+ -[_HKFeatureFlags allDayHRV]
+ -[_HKFeatureFlags allDayHeartRate]
+ -[_HKFeatureFlags hermitV2]
+ -[_HKFeatureFlags liveHeartRateComplications]
+ -[_HKFeatureFlags setAllDayHRV:]
+ -[_HKFeatureFlags setAllDayHeartRate:]
+ -[_HKFeatureFlags setHermitV2:]
+ -[_HKFeatureFlags setLiveHeartRateComplications:]
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table188
+ _HKFeatureAvailabilityContextReadiness
+ _HKFeatureAvailabilityRequirementIdentifierGreenLightMeasurementsAreEnabled
+ _HKFeatureIdentifierHypertensionNotificationsV1
+ _HKFeatureIdentifierHypertensionNotificationsV2
+ _HKLocalDeviceHardwareSupportsContinuousHeartRate
+ _HKQuantityTypeIdentifierHeartRateVariabilityRMSSD
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ _OBJC_CLASS_$_HKHeartRatePreferencesConstants
+ _OBJC_IVAR_$_HKFeatureAvailabilityRequirementEvaluationDataSource._heartRatePreferencesDataSource
+ _OBJC_IVAR_$__HKFeatureFlags._allDayHRV
+ _OBJC_IVAR_$__HKFeatureFlags._allDayHeartRate
+ _OBJC_IVAR_$__HKFeatureFlags._hermitV2
+ _OBJC_IVAR_$__HKFeatureFlags._liveHeartRateComplications
+ _OBJC_METACLASS_$_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ _OBJC_METACLASS_$_HKHeartRatePreferencesConstants
+ __HKWorkoutPowerModeTypeUsesBufferedSensorBehavior
+ __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ __OBJC_$_CLASS_METHODS_HKHeartRatePreferencesConstants
+ __OBJC_$_CLASS_PROP_LIST_HKHeartRatePreferencesConstants
+ __OBJC_$_INSTANCE_METHODS_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ __OBJC_CLASS_RO_$_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ __OBJC_CLASS_RO_$_HKHeartRatePreferencesConstants
+ __OBJC_METACLASS_RO_$_HKFeatureAvailabilityRequirementGreenLightMeasurementsAreEnabled
+ __OBJC_METACLASS_RO_$_HKHeartRatePreferencesConstants
+ ___27-[_HKFeatureFlags hermitV2]_block_invoke
+ ___28-[_HKFeatureFlags allDayHRV]_block_invoke
+ ___34-[_HKFeatureFlags allDayHeartRate]_block_invoke
+ ___45-[_HKFeatureFlags liveHeartRateComplications]_block_invoke
+ _kHKInternalSettingsKeyFakeLiveHeartRates
+ _objc_msgSend$allDayHRV
+ _objc_msgSend$enableGreenLightMeasurementsKey
+ _objc_msgSend$heartRatePreferencesDataSource
+ _objc_msgSend$initWithHealthDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:heartRatePreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:authorizationRecordDataSource:
+ _objc_msgSend$initWithHealthDataSource:featureAvailabilityProvidingDataSource:featureStatusProvidingDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:heartRatePreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:healthDataRequirementDataSource:importExclusionDeviceDataSource:authorizationRecordDataSource:
+ _objc_msgSend$userDefaultsHeartRatePreferencesDomainReadAccessEntitlement
- -[HKFeatureAvailabilityRequirementEvaluationDataSource initWithHealthDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:authorizationRecordDataSource:]
- -[HKFeatureAvailabilityRequirementEvaluationDataSource initWithHealthDataSource:featureAvailabilityProvidingDataSource:featureStatusProvidingDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:healthDataRequirementDataSource:importExclusionDeviceDataSource:authorizationRecordDataSource:]
- GCC_except_table96
- _objc_msgSend$initWithHealthDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:authorizationRecordDataSource:
- _objc_msgSend$initWithHealthDataSource:featureAvailabilityProvidingDataSource:featureStatusProvidingDataSource:bluetoothDeviceDataSource:privacyPreferencesDataSource:respiratoryPreferencesDataSource:ageGatingDataSource:userNotificationSettingsDataSource:wristDetectionSettingDataSource:devicePairingAndSwitchingNotificationDataSource:darwinNotificationDataSource:watchLowPowerModeDataSource:currentCountryCodeProvider:requirementSatisfactionOverridesDataSource:currentDateDataSource:OSEligibilityDataSource:watchAppInstallationDataSource:onboardingRecordFallbackProvider:userNotificationsDataSource:healthDataRequirementDataSource:importExclusionDeviceDataSource:authorizationRecordDataSource:
CStrings:
+ "AllDayHRV"
+ "AllDayHeartRate"
+ "DaytimeMetricsInHealth"
+ "DaytimeMetricsIncludeFutureData"
+ "Device1,8240"
+ "Device1,8242"
+ "Device1,8245"
+ "Device1,8246"
+ "Device1,8247"
+ "Device1,8248"
+ "DeviceSupportsContinuousHeartRate"
+ "DeviceSupportsContinuousHeartRateOverride"
+ "EnableGreenLightMeasurements"
+ "EnableGreenLightMeasurementsDuringTheaterMode"
+ "FakeLiveHeartRates"
+ "Green Light Measurements must be enabled in Heart Rate preferences"
+ "GreenLightMeasurementsAreEnabled"
+ "HEART_RATE_VARIABILITY_RMSSD"
+ "HEART_RATE_VARIABILITY_SDNN"
+ "HKQuantityTypeIdentifierHeartRateVariabilityRMSSD"
+ "Hypertension Notifications 1.0"
+ "Hypertension Notifications 2.0"
+ "HypertensionNotificationsV1"
+ "HypertensionNotificationsV2"
+ "LastModifiedPreferencesDate"
+ "Localizable-AllDayHRV"
+ "Readiness"
+ "VitalsEnhancementsAlternatingExperienceVersion"
+ "VitalsEnhancementsExerciseCessation"
+ "VitalsEnhancementsUseSDNN"
+ "com.apple.HeartRate.preferences"
+ "heartRateStreamingChart"
+ "hermit1"
+ "hermit2"
+ "hermitV2"
+ "liveHeartRateComplications"
- "HEART_RATE_VARIABILITY"
- "\xf0!"
```
