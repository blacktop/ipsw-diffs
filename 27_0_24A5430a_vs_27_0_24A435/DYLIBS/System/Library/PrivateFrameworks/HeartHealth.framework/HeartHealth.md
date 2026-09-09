## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

```diff

 7027.0.72.2.7
-  __TEXT.__text: 0x26e08
-  __TEXT.__objc_methlist: 0x2fec
-  __TEXT.__const: 0x2f8
-  __TEXT.__oslogstring: 0x17d4
-  __TEXT.__cstring: 0x361a
+  __TEXT.__text: 0x291c4
+  __TEXT.__objc_methlist: 0x305c
+  __TEXT.__const: 0x488
+  __TEXT.__oslogstring: 0x18d4
+  __TEXT.__cstring: 0x381a
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__constg_swiftt: 0x90
-  __TEXT.__swift5_typeref: 0x29
+  __TEXT.__constg_swiftt: 0x17c
+  __TEXT.__swift5_typeref: 0x18b
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__swift5_reflstr: 0x57
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__unwind_info: 0xbe0
-  __TEXT.__eh_frame: 0x70
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_reflstr: 0x1d1
+  __TEXT.__swift5_fieldmd: 0x104
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_capture: 0x28
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__eh_frame: 0xb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__const: 0xd80
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1be0
+  __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x5f0
-  __AUTH_CONST.__const: 0x390
-  __AUTH_CONST.__cfstring: 0x2ce0
-  __AUTH_CONST.__objc_const: 0x5e68
+  __DATA_CONST.__got: 0x678
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x2d80
+  __AUTH_CONST.__objc_const: 0x5ee8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH.__objc_data: 0xf00
-  __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0x928
+  __AUTH.__data: 0xf0
+  __DATA.__objc_ivar: 0x320
+  __DATA.__data: 0x970
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1227
-  Symbols:   2979
-  CStrings:  506
+  Functions: 1324
+  Symbols:   3076
+  CStrings:  517
 
Symbols:
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _analysisForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _backgroundDeliveryForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _basePromotionRequirementsForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _baseUsageWithFeatureOnRequirementIncluded:forFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrEducationVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrStatusVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _featureDeviceCapabilityForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _featureFlagEnabledForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _localCountryIsSupportedRequirementForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _notificationSettingsVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _onboardingInitiationForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _onboardingRecordRequirement]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _pregnancyAdjustmentEligibilityForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _promotionForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _remoteCountryIsSupportedRequirementForFeatureIdentifier:isSupportedIfCountryListMissing:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _requirementsByContextForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsUserInteractionEnabledForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsVisibilityWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _sharedFeatureIdentifier]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _usageForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements requirementSetForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsUserInteractionRequirementIdentifiersForFeatureIdentifier:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsVisibilityRequirementIdentifiersWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements usageRequirementIdentifiersForFeatureIdentifier:featureFlagIsEnabled:]
+ +[HKHRHypertensionNotificationsSettings _countryRequirementWithIsOnboardingRecordPresent:]
+ +[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatchedWithV1Evaluation:v2Evaluation:isOnboardingRecordPresent:]
+ -[HKHRHypertensionNotificationsSettings _setupVersionManagersWithIsOnboardingRecordPresent:]
+ -[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatched]
+ -[HKHRHypertensionNotificationsSettings initWithIsOnboardingRecordPresent:]
+ _HKFeatureAvailabilityRequirementIdentifierCurrentCountryIsSupportedOnActiveRemoteDevice
+ _HKFeatureAvailabilityRequirementIdentifierCurrentCountryIsSupportedOnLocalDevice
+ _HKFeatureAvailabilityRequirementIdentifierFeatureFlagIsEnabled
+ _HKFeatureIdentifierHypertensionNotificationsV1
+ _HKFeatureIdentifierHypertensionNotificationsV2
+ _HKHRHypertensionNotificationsV2LocalFeatureAttributes
+ _HKHRHypertensionNotificationsV2SettingsLocstr
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_HKHealthStore
+ _OBJC_CLASS_$_HKHeartRatePreferencesConstants
+ _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._isOnboardingRecordPresent
+ _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._v1StatusManager
+ _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._v2StatusManager
+ __OBJC_$_CLASS_METHODS_HKHRHypertensionNotificationsSettings
+ ___swift_closure_destructor
+ ___swift_closure_destructorTm
+ ___swift_memcpy2_1
+ ___swift_memcpy56_8
+ __swiftEmptySetSingleton
+ _associated conformance 11HeartHealth0A15RatePreferencesVSHAASQ
+ _associated conformance 11HeartHealth0A23RatePreferencesProviderVAA0acD9ProvidingAA0acD8SequenceAaDP_Sci
+ _get_witness_table 11Observation12ObservationsVy11HeartHealth0C15RatePreferencesVs5NeverOGSciHPyHC
+ _objc_allocWithZone
+ _objc_msgSend$_analysisForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_backgroundDeliveryForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_basePromotionRequirementsForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_baseUsageWithFeatureOnRequirementIncluded:forFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_countryRequirementWithIsOnboardingRecordPresent:
+ _objc_msgSend$_dtdrEducationVisibilityForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_dtdrStatusVisibilityForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_featureDeviceCapabilityForFeatureIdentifier:
+ _objc_msgSend$_featureFlagEnabledForFeatureIdentifier:
+ _objc_msgSend$_localCountryIsSupportedRequirementForFeatureIdentifier:
+ _objc_msgSend$_notificationSettingsVisibilityForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_onboardingInitiationForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_onboardingRecordRequirement
+ _objc_msgSend$_pregnancyAdjustmentEligibilityForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_promotionForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_remoteCountryIsSupportedRequirementForFeatureIdentifier:isSupportedIfCountryListMissing:
+ _objc_msgSend$_requirementsByContextForFeatureIdentifier:
+ _objc_msgSend$_settingsVisibilityWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$_setupVersionManagersWithIsOnboardingRecordPresent:
+ _objc_msgSend$_sharedFeatureIdentifier
+ _objc_msgSend$_usageForFeatureIdentifier:featureFlagIsEnabled:
+ _objc_msgSend$areRegionAndWatchSupportedVersionsMismatched
+ _objc_msgSend$areRegionAndWatchSupportedVersionsMismatchedWithV1Evaluation:v2Evaluation:isOnboardingRecordPresent:
+ _objc_msgSend$domain
+ _objc_msgSend$enableGreenLightMeasurementsDuringTheaterModeKey
+ _objc_msgSend$enableGreenLightMeasurementsKey
+ _objc_msgSend$featureFlagIsEnabled:
+ _objc_msgSend$featureStatusWithError:
+ _objc_msgSend$features
+ _objc_msgSend$hermitV2
+ _objc_msgSend$init
+ _objc_msgSend$initWithFeatureIdentifier:healthStore:
+ _objc_msgSend$initWithFeatureIdentifier:healthStore:countryCodeSource:
+ _objc_msgSend$isAppleWatch
+ _objc_msgSend$lastModifiedPreferencesDateKey
+ _objc_msgSend$stringValue
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_getOpaqueTypeConformance2
+ _swift_initStackObject
+ _swift_release_x19
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_retain_x19
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_setDeallocating
+ _symbolic $s11HeartHealth0A24RatePreferencesProvidingP
+ _symbolic 28HeartRatePreferencesSequence_____Qz 11HeartHealth0A24RatePreferencesProvidingP
+ _symbolic 28HeartRatePreferencesSequence______7ElementSciQZ 11HeartHealth0A24RatePreferencesProvidingP
+ _symbolic 28HeartRatePreferencesSequence______7FailureSciQZ 11HeartHealth0A24RatePreferencesProvidingP
+ _symbolic 7ElementSciQz
+ _symbolic 7FailureSciQz
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic So8NSNumberCSg
+ _symbolic _____ 11HeartHealth0A15RatePreferencesV
+ _symbolic _____ 11HeartHealth0A23RatePreferencesProviderV
+ _symbolic _____ s5NeverO
+ _symbolic _____ySbG 15HealthUtilities21ObservableUserDefaultC
+ _symbolic _____yYbc 10Foundation4DateV
+ _symbolic _____y_____SgG 15HealthUtilities21ObservableUserDefaultC 10Foundation4DateV
+ _symbolic _____y__________G 11Observation12ObservationsV 11HeartHealth0C15RatePreferencesV s5NeverO
+ _symbolic x
+ _symbolic ySS_ShySSGtYbc
+ _type_layout_string 11HeartHealth0A15RatePreferencesV
+ _type_layout_string 11HeartHealth0A23RatePreferencesProviderV
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _analysis]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _backgroundDelivery]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _basePromotionRequirements]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _baseUsageWithFeatureOnRequirementIncluded:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrEducationVisibility]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrStatusVisibility]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _hypertensionIdentifier]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _notificationSettingsVisibility]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _onboardingInitiation]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _pregnancyAdjustmentEligibility]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _promotion]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsUserInteractionEnabled]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsVisibilityWithFeatureOnboarded:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _usage]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements onboardingInitiationRequirementIdentifiers]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements promotionRequirementIdentifiers]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements requirementSet]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsUserInteractionRequirementIdentifiers]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsVisibilityRequirementIdentifiersWithFeatureOnboarded:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements usageRequirementIdentifiers]
- _objc_msgSend$_basePromotionRequirements
- _objc_msgSend$_baseUsageWithFeatureOnRequirementIncluded:
- _objc_msgSend$_dtdrEducationVisibility
- _objc_msgSend$_dtdrStatusVisibility
- _objc_msgSend$_hypertensionIdentifier
- _objc_msgSend$_notificationSettingsVisibility
- _objc_msgSend$_settingsUserInteractionEnabled
- _objc_msgSend$_settingsVisibilityWithFeatureOnboarded:
CStrings:
+ "(01)00195951129969"
+ "(01)00195951129976"
+ "+[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatchedWithV1Evaluation:v2Evaluation:isOnboardingRecordPresent:]"
+ "-[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatched]"
+ "2"
+ "HEART_NOTIFICATION_HYPERTENSION_NOTIFICATIONS_FOOTER_REGION_NOT_SUPPORTED_MISMATCH"
+ "HEART_NOTIFICATION_HYPERTENSION_NOTIFICATIONS_FOOTER_REGION_NOT_SUPPORTED_MISMATCH_NANO"
+ "HeartRateSettings-HypertensionNotificationsV2"
+ "[%{public}s] Failed to get v1 feature status: %{public}@"
+ "[%{public}s] Failed to get v2 feature status: %{public}@"
+ "[%{public}s] Supported Region-Watch Mismatch: v1OnlyRegionWithV2Watch: %i, v2OnlyRegionWithV1Watch: %i isOnboardingRecordPresent: %i"
+ "algorithmVersion"
+ "d2f9b521-e715-4a96-94f9-19c209511ee5"
- "(01)00195949001789"
- "(01)00195949001796"
```
