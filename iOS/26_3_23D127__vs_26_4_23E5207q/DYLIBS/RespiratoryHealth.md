## RespiratoryHealth

> `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x62dc
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x954
+6200.5.77.2.6
+  __TEXT.__text: 0x4ad0
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x7fc
   __TEXT.__const: 0x72
-  __TEXT.__oslogstring: 0x902
-  __TEXT.__cstring: 0xb14
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x2cc
-  __TEXT.__objc_methname: 0x1cfb
-  __TEXT.__objc_methtype: 0x4ae
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x278
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__cstring: 0xa94
+  __TEXT.__oslogstring: 0x40b
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__objc_classname: 0x24c
+  __TEXT.__objc_methname: 0x1b68
+  __TEXT.__objc_methtype: 0x424
+  __TEXT.__objc_stubs: 0xe60
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x1368
+  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__objc_const: 0x1110
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x60
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x300
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E9E39275-5881-34D4-B5C1-73381B66B5D7
-  Functions: 198
-  Symbols:   845
-  CStrings:  544
+  UUID: DE815802-5038-31E4-A85A-0FB2B63F6C9A
+  Functions: 161
+  Symbols:   722
+  CStrings:  490
 
Symbols:
+ -[HKRPOxygenSaturationOnboardingManager _notifyStatusDidChange]
+ -[HKRPOxygenSaturationOnboardingManager _updateWithFeatureStatus:]
+ -[HKRPOxygenSaturationOnboardingManager addObserver:queue:]
+ -[HKRPOxygenSaturationOnboardingManager deliverFeatureWithCompletion:]
+ -[HKRPOxygenSaturationOnboardingManager deviceIsSupported]
+ -[HKRPOxygenSaturationOnboardingManager featureStatusProviding:didUpdateFeatureStatus:]
+ -[HKRPOxygenSaturationOnboardingManager initWithFeatureStatusProvider:regulatoryDomainEstimate:]
+ -[HKRPOxygenSaturationOnboardingManager initWithFeatureStatusProvider:regulatoryDomainEstimate:].cold.1
+ -[HKRPOxygenSaturationOnboardingManager regionIsSupported]
+ -[HKRPOxygenSaturationOnboardingManager removeObserver:]
+ -[HKRPOxygenSaturationOnboardingManager settingsInteractionEnabled]
+ -[HKRPOxygenSaturationOnboardingManager shouldDeliverFeature]
+ _HKFeatureAvailabilityContextSettingsUserInteractionEnabled
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _HKFeatureAvailabilityRequirementIdentifierActiveWatchIsNotUnderInternalDevelopmentImportExclusion
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnActiveRemoteDevice
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _HKFeatureAvailabilityRequirementIdentifierNotAgeGatedForUserDefaultsKey
+ _OBJC_CLASS_$_NSDate
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._ageIsAppropriate
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._bloodOxygenRemoteDisabled
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._deviceIsSupported
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._featureAvailabilityProvider
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._featureIsOnboarded
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._featureStatusProvider
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._observers
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._regionIsSupported
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._regulatoryDomainEstimate
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._settingsInteractionEnabled
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._settingsShouldAppear
+ _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._shouldDeliverFeature
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureStatusProvidingObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureStatusProvidingObserver
+ __OBJC_$_PROTOCOL_REFS_HKFeatureStatusProvidingObserver
+ __OBJC_CLASS_PROTOCOLS_$_HKRPOxygenSaturationOnboardingManager
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureStatusProvidingObserver
+ __OBJC_PROTOCOL_$_HKFeatureStatusProvidingObserver
+ ___63-[HKRPOxygenSaturationOnboardingManager _notifyStatusDidChange]_block_invoke
+ ___block_descriptor_40_e8_32s_e57_v16?0"<HKRPOxygenSaturationOnboardingManagerObserver>"8ls32l8
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_notifyStatusDidChange
+ _objc_msgSend$_updateWithFeatureStatus:
+ _objc_msgSend$currentEstimate
+ _objc_msgSend$featureAvailabilityProviding
+ _objc_msgSend$initWithFeatureAvailabilityProviding:healthDataSource:currentCountryCode:
+ _objc_msgSend$initWithFeatureStatusProvider:regulatoryDomainEstimate:
+ _objc_msgSend$isOnboardingRecordPresent
+ _objc_msgSend$isRequirementSatisfiedWithIdentifier:
+ _objc_msgSend$oxygenSaturationFeatureStatusDidChange:
+ _objc_opt_new
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- -[HKRPOxygenSaturationOnboardingManager _currentDeviceHasCapability]
- -[HKRPOxygenSaturationOnboardingManager _currentDeviceHasCapability].cold.1
- -[HKRPOxygenSaturationOnboardingManager _isAlternateDevice]
- -[HKRPOxygenSaturationOnboardingManager bloodOxygenFeatureEnabled]
- -[HKRPOxygenSaturationOnboardingManager bloodOxygenRemoteDisabled].cold.1
- -[HKRPOxygenSaturationOnboardingManager bloodOxygenRemoteDisabled].cold.2
- -[HKRPOxygenSaturationOnboardingManager cacheCompletedOnboardingStateIfNeeded]
- -[HKRPOxygenSaturationOnboardingManager cacheCompletedOnboardingStateIfNeeded].cold.1
- -[HKRPOxygenSaturationOnboardingManager dataSource]
- -[HKRPOxygenSaturationOnboardingManager initWithDataSource:]
- -[HKRPOxygenSaturationOnboardingManager initWithDevice:]
- -[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]
- -[HKRPOxygenSaturationOnboardingManager onboardingComplete]
- -[HKRPOxygenSaturationOnboardingManager onboardingComplete].cold.1
- -[HKRPOxygenSaturationOnboardingManager onboardingDuringPairingShouldAppear]
- -[HKRPOxygenSaturationOnboardingManager onboardingShouldAppear]
- -[HKRPOxygenSaturationOnboardingManager pairedDeviceIsAppropriate]
- -[HKRPOxygenSaturationOnboardingManager shouldAdvertise]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource .cxx_destruct]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource _lazyPropertyWithLockedBlock:]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource countryCodeFromCurrentLocale]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource device]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource featureAvailabilityProvider]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource init]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource isAgeGated]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource isBloodOxygenSaturationEnabled]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource mobileCountryCodeManager]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource oxygenSaturationSettings]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource shouldAdvertise]
- -[_HKRPOxygenSaturationOnboardingManagerDataSource skipHardwareCheck]
- -[_HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource .cxx_destruct]
- -[_HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource device]
- -[_HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource initWithDevice:]
- -[_HKRPWatchAppInstallabilityDataSource isBloodOxygenSaturationEnabled]
- GCC_except_table14
- GCC_except_table15
- GCC_except_table46
- _HKErrorDomain
- _HKLogRespiratoryCategory
- _HKRPShouldSkipOnboardingCompletedCheck
- _HKRPShouldSkipRegionCheck
- _NSStringFromHKFeatureAvailabilityOnboardedCountrySupportedState
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$__HKRPOxygenSaturationOnboardingManagerDataSource
- _OBJC_CLASS_$__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- _OBJC_IVAR_$_HKRPOxygenSaturationOnboardingManager._dataSource
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._featureAvailabilityProvider
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._lock
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._mobileCountryCodeManager
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._oxygenSaturationAvailability
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerDataSource._oxygenSaturationSettings
- _OBJC_IVAR_$__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource._device
- _OBJC_METACLASS_$__HKRPOxygenSaturationOnboardingManagerDataSource
- _OBJC_METACLASS_$__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- __OBJC_$_INSTANCE_METHODS__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_INSTANCE_METHODS__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- __OBJC_$_INSTANCE_VARIABLES__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_INSTANCE_VARIABLES__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- __OBJC_$_PROP_LIST_HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_PROP_LIST__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_$_PROTOCOL_REFS_HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_CLASS_PROTOCOLS_$__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_CLASS_RO_$__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_CLASS_RO_$__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- __OBJC_LABEL_PROTOCOL_$_HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_METACLASS_RO_$__HKRPOxygenSaturationOnboardingManagerDataSource
- __OBJC_METACLASS_RO_$__HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource
- __OBJC_PROTOCOL_$_HKRPOxygenSaturationOnboardingManagerDataSource
- __Unwind_Resume
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.303
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.309
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.320
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.cold.1
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.cold.2
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke_2
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke_3
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke_3.cold.1
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke_3.cold.2
- ___76-[_HKRPOxygenSaturationOnboardingManagerDataSource mobileCountryCodeManager]_block_invoke
- ___76-[_HKRPOxygenSaturationOnboardingManagerDataSource oxygenSaturationSettings]_block_invoke
- ___79-[_HKRPOxygenSaturationOnboardingManagerDataSource featureAvailabilityProvider]_block_invoke
- ___block_descriptor_40_e8_32s_e5_8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_57_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___block_descriptor_64_e8_32s40bs48w_e20_v20?0B8"NSError"12lu56l8s32l8w48l8s40l8
- ___block_descriptor_64_e8_32s40bs48w_e44_v24?0"<HKCurrentCountryCode>"8"NSError"16lu56l8s40l8s32l8w48l8
- ___objc_personality_v0
- _kHKAgeGatingDomain
- _kHKAgeGatingKeyEnableOxygenSaturationRecording
- _objc_claimAutoreleasedReturnValue
- _objc_copyWeak
- _objc_initWeak
- _objc_msgSend$_currentDeviceHasCapability
- _objc_msgSend$_isAlternateDevice
- _objc_msgSend$_lazyPropertyWithLockedBlock:
- _objc_msgSend$activateDefaultValuesIfNeeded
- _objc_msgSend$activeDeviceSelectorBlock
- _objc_msgSend$ageIsAppropriate
- _objc_msgSend$bloodOxygenFeatureEnabled
- _objc_msgSend$bloodOxygenRemoteDisabled
- _objc_msgSend$cacheCompletedOnboardingStateIfNeeded
- _objc_msgSend$canCompleteOnboardingForCountryCode:error:
- _objc_msgSend$code
- _objc_msgSend$countryCodeFromCurrentLocale
- _objc_msgSend$device
- _objc_msgSend$domain
- _objc_msgSend$featureAvailabilityProvider
- _objc_msgSend$fetchMobileCountryCodeFromCellularWithCompletion:
- _objc_msgSend$firstObject
- _objc_msgSend$getDevicesMatching:
- _objc_msgSend$hk_error:description:underlyingError:
- _objc_msgSend$ineligibilityReasons
- _objc_msgSend$integerValue
- _objc_msgSend$isAgeGated
- _objc_msgSend$isBloodOxygenSaturationEnabled
- _objc_msgSend$isCountryAllowed:
- _objc_msgSend$isCurrentOnboardingVersionCompletedWithError:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isFeatureCapabilitySupportedOnActivePairedDeviceWithError:
- _objc_msgSend$mobileCountryCodeManager
- _objc_msgSend$onboardedCountryCodeSupportedStateWithError:
- _objc_msgSend$onboardingComplete
- _objc_msgSend$onboardingEligibilityForCountryCode:error:
- _objc_msgSend$onboardingShouldAppear
- _objc_msgSend$oxygenSaturationSettings
- _objc_msgSend$pairedDeviceIsAppropriate
- _objc_msgSend$settingsShouldAppear
- _objc_msgSend$sharedInstance
- _objc_msgSend$shouldAdvertise
- _objc_msgSend$standardSettings
- _objc_release_x9
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "@\"<HKFeatureAvailabilityProviding>\""
+ "@\"<HKFeatureStatusProviding>\""
+ "@\"HKRegulatoryDomainEstimate\""
+ "B"
+ "BD3A4341-332F-481C-B7DE-7E80973B07BF"
+ "HKFeatureStatusProvidingObserver"
+ "HKRPOxygenSaturationOnboardingManagerObserver"
+ "TB,R,N,V_ageIsAppropriate"
+ "TB,R,N,V_bloodOxygenRemoteDisabled"
+ "TB,R,N,V_deviceIsSupported"
+ "TB,R,N,V_regionIsSupported"
+ "TB,R,N,V_settingsInteractionEnabled"
+ "TB,R,N,V_settingsShouldAppear"
+ "TB,R,N,V_shouldDeliverFeature"
+ "[%{public}@] could not get feature status with error: %{public}@"
+ "_ageIsAppropriate"
+ "_bloodOxygenRemoteDisabled"
+ "_deviceIsSupported"
+ "_featureIsOnboarded"
+ "_featureStatusProvider"
+ "_notifyStatusDidChange"
+ "_regionIsSupported"
+ "_regulatoryDomainEstimate"
+ "_settingsInteractionEnabled"
+ "_settingsShouldAppear"
+ "_shouldDeliverFeature"
+ "_updateWithFeatureStatus:"
+ "currentEstimate"
+ "deliverFeatureWithCompletion:"
+ "featureAvailabilityProviding"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "initWithFeatureAvailabilityProviding:healthDataSource:currentCountryCode:"
+ "initWithFeatureStatusProvider:regulatoryDomainEstimate:"
+ "isOnboardingRecordPresent"
+ "isRequirementSatisfiedWithIdentifier:"
+ "oxygenSaturationFeatureStatusDidChange:"
+ "regionIsSupported"
+ "settingsInteractionEnabled"
+ "shouldDeliverFeature"
+ "v16@?0@\"<HKRPOxygenSaturationOnboardingManagerObserver>\"8"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
- "1P`"
- "@\"<HKFeatureAvailabilityProviding>\"16@0:8"
- "@\"<HKRPOxygenSaturationOnboardingManagerDataSource>\""
- "@\"<HKRegulatoryDomainProvider>\""
- "@\"<HKRegulatoryDomainProvider>\"16@0:8"
- "@\"HKFeatureAvailabilityStore\""
- "@\"HKRPOxygenSaturationSettings\""
- "@\"HKRPOxygenSaturationSettings\"16@0:8"
- "@\"NRDevice\"16@0:8"
- "@24@0:8@?16"
- "@8@?0"
- "BD3A4341-7090-4622-9694-2AC0F536C478"
- "Feature unavailable for country code %@ (error)"
- "HKRPBloodOxygenSaturationEnabled"
- "HKRPOxygenSaturationOnboardingManagerDataSource"
- "HKRPSkipOnboardingCompletedCheck"
- "HKRPSkipRegionCheck"
- "T@\"<HKFeatureAvailabilityProviding>\",R,N"
- "T@\"<HKRPOxygenSaturationOnboardingManagerDataSource>\",R,N,V_dataSource"
- "T@\"<HKRegulatoryDomainProvider>\",R,N"
- "T@\"HKRPOxygenSaturationSettings\",R,N"
- "T@\"NRDevice\",R,N"
- "T@\"NSString\",R,N"
- "TB,R,N,GisAgeGated"
- "TB,R,N,GisBloodOxygenSaturationEnabled"
- "[%{public}@] -> 0 (Not allowed when feature is disabled)"
- "[%{public}@] Age is appropriate for oxygen saturation: %{public}@"
- "[%{public}@] Alternate device check: active device is nil"
- "[%{public}@] Alternate device check: alternate device flag: %d"
- "[%{public}@] Attempting to onboard feature, checking country code..."
- "[%{public}@] Caching the fact that onboarding has completed"
- "[%{public}@] Cannot onboard with country code %{public}@, it is not supported"
- "[%{public}@] Device check failed: %{public}@"
- "[%{public}@] Device check override is in place"
- "[%{public}@] Device check result: %{public}@"
- "[%{public}@] Feature is enabled: %d"
- "[%{public}@] On board check failed: %{public}@"
- "[%{public}@] Onboarding completed state: %{public}@"
- "[%{public}@] Remote disabled check failed eligibility check with error: %{public}@"
- "[%{public}@] Remote disabled check failed with error: %{public}@"
- "[%{public}@] Setting current onboarding version completed for %{public}@..."
- "[%{public}@] Should advertise onboarding of feature: %{public}@"
- "[%{public}@] The user has previously onboarded this feature, ignoring feature availability store error"
- "[%{public}@] Unable to cache the fact that onboarding has completed: %{public}@"
- "[%{public}@] Unable to onboard feature: %{public}@"
- "[%{public}@] Unable to set current onboarding version completed for %{public}@: %{public}@"
- "_HKRPOxygenSaturationOnboardingManagerDataSource"
- "_HKRPOxygenSaturationOnboardingManagerStaticDeviceDataSource"
- "_currentDeviceHasCapability"
- "_isAlternateDevice"
- "_lazyPropertyWithLockedBlock:"
- "_mobileCountryCodeManager"
- "_oxygenSaturationAvailability"
- "_oxygenSaturationSettings"
- "activeDeviceSelectorBlock"
- "ageGated"
- "bloodOxygenFeatureEnabled"
- "bloodOxygenSaturationEnabled"
- "cacheCompletedOnboardingStateIfNeeded"
- "canCompleteOnboardingForCountryCode:error:"
- "code"
- "country code not found"
- "countryCodeFromCurrentLocale"
- "dataSource"
- "device"
- "domain"
- "featureAvailabilityProvider"
- "fetchMobileCountryCodeFromCellularWithCompletion:"
- "firstObject"
- "getDevicesMatching:"
- "hk_error:description:underlyingError:"
- "ineligibilityReasons"
- "integerValue"
- "isAgeGated"
- "isBloodOxygenSaturationEnabled"
- "isCurrentOnboardingVersionCompletedWithError:"
- "isEqualToString:"
- "isFeatureCapabilitySupportedOnActivePairedDeviceWithError:"
- "mobileCountryCodeManager"
- "onboardWithCompletion:"
- "onboardedCountryCodeSupportedStateWithError:"
- "onboardingComplete"
- "onboardingDuringPairingShouldAppear"
- "onboardingEligibilityForCountryCode:error:"
- "onboardingShouldAppear"
- "oxygenSaturationSettings"
- "pairedDeviceIsAppropriate"
- "sharedInstance"
- "shouldAdvertise"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"<HKCurrentCountryCode>\"8@\"NSError\"16"

```
