## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x27f40
-  __TEXT.__objc_methlist: 0x305c
-  __TEXT.__const: 0x488
-  __TEXT.__oslogstring: 0x18d4
-  __TEXT.__cstring: 0x381a
+7027.1.36.2.7
+  __TEXT.__text: 0x2b4ec
+  __TEXT.__objc_methlist: 0x2ccc
+  __TEXT.__const: 0x724
+  __TEXT.__oslogstring: 0x1934
+  __TEXT.__cstring: 0x380a
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__constg_swiftt: 0x17c
-  __TEXT.__swift5_typeref: 0x18b
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_reflstr: 0x1d1
-  __TEXT.__swift5_fieldmd: 0x104
-  __TEXT.__swift5_proto: 0x20
+  __TEXT.__constg_swiftt: 0x19c
+  __TEXT.__swift5_typeref: 0x1d3
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x201
+  __TEXT.__swift5_fieldmd: 0x120
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x10d0
-  __TEXT.__eh_frame: 0xb0
+  __TEXT.__unwind_info: 0x1170
+  __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd80
-  __DATA_CONST.__objc_classlist: 0x210
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
-  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x1a40
+  __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x678
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x2d80
-  __AUTH_CONST.__objc_const: 0x5ee8
+  __DATA_CONST.__got: 0x680
+  __AUTH_CONST.__const: 0x418
+  __AUTH_CONST.__cfstring: 0x2dc0
+  __AUTH_CONST.__objc_const: 0x6020
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5c0
-  __AUTH.__objc_data: 0xf00
-  __AUTH.__data: 0xf0
+  __AUTH_CONST.__auth_got: 0x6b0
+  __AUTH.__objc_data: 0xf50
+  __AUTH.__data: 0xf8
   __DATA.__objc_ivar: 0x320
-  __DATA.__data: 0x970
-  __DATA.__common: 0x20
+  __DATA.__data: 0xb70
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
+  - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
   - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1324
-  Symbols:   3076
-  CStrings:  517
+  Functions: 1353
+  Symbols:   2939
+  CStrings:  518
 
Symbols:
+ +[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatchedWithIsOnboardingRecordPresent:]
+ -[HKHRAFibBurdenNotificationSettingsFactory initWithRequirementsEvaluationByContext:isOnboardingRecordPresent:]
+ -[HKHRCardioFitnessNotificationSettingsFactory _bridgeNotificationsFooterForEvaluation:]
+ -[HKHRCardioFitnessNotificationSettingsFactory _bridgeOnboardingFooterForEvaluation:]
+ -[HKHRCardioFitnessNotificationSettingsFactory _watchFooterForEvaluation:]
+ -[HKHRCardioFitnessNotificationSettingsFactory initWithRequirementsEvaluationByContext:]
+ -[HKHRHypertensionNotificationsSettings _isWatchSettingsVisible]
+ -[HKHRHypertensionNotificationsSettings _notificationsEnabled]
+ -[HKHRHypertensionNotificationsSettings _onboardingAcknowledged]
+ -[HKHRHypertensionNotificationsSettings initWithRequirementsEvaluationByContext:featureSettings:isOnboardingRecordPresent:]
+ GCC_except_table19
+ _HKNRDEVICECAPABILITY_CONTINUOUS_HEART_RATE
+ _HKNRDEVICECAPABILITY_ECG2_UPGRADE_BACKGROUND_DELIVERY
+ _HKNRDEVICECAPABILITY_HERMIT_HW
+ _OBJC_CLASS_$_HKHRHypertensionNotificationsAnalyticsUtilities
+ _OBJC_IVAR_$_HKHRAFibBurdenNotificationSettingsFactory._isOnboardingRecordPresent
+ _OBJC_IVAR_$_HKHRAFibBurdenNotificationSettingsFactory._requirementsEvaluationByContext
+ _OBJC_IVAR_$_HKHRCardioFitnessNotificationSettingsFactory._requirementsEvaluationByContext
+ _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._featureSettings
+ _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._requirementsEvaluationByContext
+ _OBJC_METACLASS_$_HKHRHypertensionNotificationsAnalyticsUtilities
+ __CATEGORY_HKFeatureAvailabilityRequirementSet_$_HeartHealth
+ __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementSet(HeartHealth|HeartHealth1|HeartHealth2|HeartHealth3|HeartHealth4)
+ __OBJC_$_CLASS_PROP_LIST_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROP_LIST_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_REFS_HKFeatureAvailabilityRequirement
+ __OBJC_CLASS_RO_$_HKHRHypertensionNotificationsAnalyticsUtilities
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityRequirement
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_METACLASS_RO_$_HKHRHypertensionNotificationsAnalyticsUtilities
+ __OBJC_PROTOCOL_$_HKFeatureAvailabilityRequirement
+ __OBJC_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ ___82-[HKHeartbeatSeriesFeatureStatusManager registerObserver:queue:activationHandler:]_block_invoke_5
+ _associated conformance So28HKFeatureAvailabilityContextaSHSCSQ
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_bridgeNotificationsFooterForEvaluation:
+ _objc_msgSend$_bridgeOnboardingFooterForEvaluation:
+ _objc_msgSend$_isWatchSettingsVisible
+ _objc_msgSend$_notificationsEnabled
+ _objc_msgSend$_onboardingAcknowledged
+ _objc_msgSend$_watchFooterForEvaluation:
+ _objc_msgSend$areRegionAndWatchSupportedVersionsMismatchedWithIsOnboardingRecordPresent:
+ _objc_msgSend$hkhr_aFibBurdenRequirementSet
+ _objc_msgSend$hkhr_cardioFitnessRequirementSet
+ _objc_msgSend$hkhr_electrocardiogramRecordingRequirementSet
+ _objc_msgSend$hkhr_electrocardiogramRecordingV2RequirementSet
+ _objc_msgSend$hkhr_hypertensionNotificationsRequirementSetForFeatureWithIdentifier:
+ _objc_msgSend$hkhr_irregularRhythmNotificationsRequirementSetForFeatureWithIdentifier:
+ _objc_msgSend$initWithRequirementsEvaluationByContext:
+ _objc_msgSend$initWithRequirementsEvaluationByContext:featureSettings:isOnboardingRecordPresent:
+ _objc_msgSend$initWithRequirementsEvaluationByContext:isOnboardingRecordPresent:
+ _objc_retain_x9
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCastMetatype
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_getObjCClassFromMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic So8NSStringC
+ _symbolic _____ So28HKFeatureAvailabilityContexta
+ _type_layout_string So28HKFeatureAvailabilityContexta
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _analysis]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _featureIdentifier]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _highlightGeneration]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _lifeFactorPlatterGeneration]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _mutualExclusivityEnforcement]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _onboardingInitiation]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _pdfGeneration]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _promotion]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _requirementIdentifiersForRequirements:]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _tipsAppVisibility]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements _usage]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements analysisRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements highlightGenerationRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements lifeFactorPlatterGenerationRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements onboardingInitiationRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements pdfRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements promotionRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements tipsAppVisibilityRequirementIdentifiers]
- +[HKHRAFibBurdenFeatureAvailabilityRequirements usageRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _advertiseableFeature]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _backgroundDelivery]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _bridgeNotificationsEnablement]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _bridgeNotificationsFooter]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _bridgeOnboardingEnablement]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _bridgeOnboardingVisibility]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _bridgeSettingsVisibility]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _classification]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _featureIdentifier]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _healthChecklistSettingsFooter]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _nanoSettingsEnablement]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _nanoSettingsVisibility]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _notInPregnancyMode]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _notOnboardedHealthChecklist]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _notificationGeneration]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _onboardedHealthChecklist]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _onboardingInitiation]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _postPregnancyAdjustmentEligibility]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _pregnancyAdjustmentEligibility]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _promotion]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _requirementIdentifiersForRequirements:]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements _usage]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements backgroundDelivery]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements bridgeNotificationsEnablementRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements bridgeNotificationsFooterRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements bridgeOnboardingEnablementRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements bridgeOnboardingVisibilityRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements bridgeSettingsVisibilityRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements classificationGeneration]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements healthChecklistSettingsFooter]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements nanoSettingsEnablementRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements nanoSettingsVisibilityRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements notInPregnancyModeRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements notificationGeneration]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements onboardingInitiationRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements promotionRequirementIdentifiers]
- +[HKHRCardioFitnessFeatureAvailabilityRequirements usageRequirementIdentifiers]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _onboardingInitiationRequirementsForFeatureIdentifier:]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _onboardingPromotionRequirementsForFeatureIdentifier:]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _settingsUserInteractionEnabledForFeatureIdentifier:]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _settingsVisibilityRequirementsForFeatureIdentifier:]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _upgradeInitiation]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _upgradePromotion]
- +[HKHRElectrocardiogramRecordingFeatureAvailabilityRequirements _usageRequirementsForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _analysisForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _backgroundDeliveryForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _basePromotionRequirementsForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _baseUsageWithFeatureOnRequirementIncluded:forFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrEducationVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _dtdrStatusVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _featureDeviceCapabilityForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _featureFlagEnabledForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _localCountryIsSupportedRequirementForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _notificationSettingsVisibilityForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _onboardingInitiationForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _onboardingRecordRequirement]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _pregnancyAdjustmentEligibilityForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _promotionForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _remoteCountryIsSupportedRequirementForFeatureIdentifier:isSupportedIfCountryListMissing:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _requirementIdentifiersForRequirements:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _requirementsByContextForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsUserInteractionEnabledForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _settingsVisibilityWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _sharedFeatureIdentifier]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements _usageForFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsUserInteractionRequirementIdentifiersForFeatureIdentifier:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements settingsVisibilityRequirementIdentifiersWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:]
- +[HKHRHypertensionNotificationsFeatureAvailabilityRequirements usageRequirementIdentifiersForFeatureIdentifier:featureFlagIsEnabled:]
- -[HKHRAFibBurdenNotificationSettingsFactory _isOnboarded]
- -[HKHRAFibBurdenNotificationSettingsFactory featureStatus]
- -[HKHRAFibBurdenNotificationSettingsFactory setFeatureStatus:]
- -[HKHRCardioFitnessNotificationSettingsFactory _bridgeNotificationsFooterForEvaluation::]
- -[HKHRCardioFitnessNotificationSettingsFactory _bridgeOnboardingFooterForEvaluation::]
- -[HKHRCardioFitnessNotificationSettingsFactory _watchFooterForEvaluation::]
- -[HKHRCardioFitnessNotificationSettingsFactory featureStatus]
- -[HKHRCardioFitnessNotificationSettingsFactory setFeatureStatus:]
- -[HKHRHypertensionNotificationsSettings _isWatchSettingsVisibleWithFeatureStatus:]
- -[HKHRHypertensionNotificationsSettings _notificationsEnabledWithFeatureStatus:]
- -[HKHRHypertensionNotificationsSettings _onboardingAcknowledgedWithFeatureStatus:]
- -[HKHRHypertensionNotificationsSettings _setupVersionManagersWithIsOnboardingRecordPresent:]
- -[HKHRHypertensionNotificationsSettings _showOnboardingWithFeatureStatus:]
- -[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatched]
- -[HKHRHypertensionNotificationsSettings initWithIsOnboardingRecordPresent:]
- GCC_except_table18
- GCC_except_table7
- _HKFeatureAvailabilityRequirementIdentifierOnboardingNotAcknowledged
- _HKFeatureAvailabilityRequirementIdentifierOnboardingRecordIsPresent
- _OBJC_IVAR_$_HKHRAFibBurdenNotificationSettingsFactory._featureStatus
- _OBJC_IVAR_$_HKHRCardioFitnessNotificationSettingsFactory._featureStatus
- _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._featureStatus
- _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._v1StatusManager
- _OBJC_IVAR_$_HKHRHypertensionNotificationsSettings._v2StatusManager
- __OBJC_$_PROP_LIST_HKHRAFibBurdenNotificationSettingsFactory
- __OBJC_$_PROP_LIST_HKHRCardioFitnessNotificationSettingsFactory
- __TipsAppVisibilityRequirementsForFeatureIdentifier
- __UsageRequirementsForFeatureIdentifier
- __UsageRequirementsPendingOnboardingForFeatureIdentifier
- ___55+[HKHRAFibBurdenFeatureAvailabilityRequirements _usage]_block_invoke
- ___58+[HKHRAFibBurdenFeatureAvailabilityRequirements _analysis]_block_invoke
- ___69+[HKHRAFibBurdenFeatureAvailabilityRequirements _highlightGeneration]_block_invoke
- ___73+[HKHRCardioFitnessFeatureAvailabilityRequirements _advertiseableFeature]_block_invoke
- ___78+[HKHRAFibBurdenFeatureAvailabilityRequirements _mutualExclusivityEnforcement]_block_invoke
- ___88+[HKHRAFibBurdenFeatureAvailabilityRequirements _requirementIdentifiersForRequirements:]_block_invoke
- ___91+[HKHRCardioFitnessFeatureAvailabilityRequirements _requirementIdentifiersForRequirements:]_block_invoke
- ____MutualExclusivityEnforcementRequirementsForFeatureIdentifier_block_invoke
- ___block_descriptor_32_e44_B16?0"<HKFeatureAvailabilityRequirement>"8l
- ___block_descriptor_32_e54_"NSString"16?0"<HKFeatureAvailabilityRequirement>"8l
- _kHKAgeGatingKeyEnableCardioFitness
- _kHKAgeGatingKeyEnableHeart
- _objc_msgSend$_advertiseableFeature
- _objc_msgSend$_analysis
- _objc_msgSend$_analysisForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_backgroundDelivery
- _objc_msgSend$_backgroundDeliveryForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_basePromotionRequirementsForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_baseUsageWithFeatureOnRequirementIncluded:forFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_bridgeNotificationsEnablement
- _objc_msgSend$_bridgeNotificationsFooter
- _objc_msgSend$_bridgeNotificationsFooterForEvaluation::
- _objc_msgSend$_bridgeOnboardingEnablement
- _objc_msgSend$_bridgeOnboardingFooterForEvaluation::
- _objc_msgSend$_bridgeOnboardingVisibility
- _objc_msgSend$_bridgeSettingsVisibility
- _objc_msgSend$_classification
- _objc_msgSend$_dtdrEducationVisibilityForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_dtdrStatusVisibilityForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_featureDeviceCapabilityForFeatureIdentifier:
- _objc_msgSend$_featureFlagEnabledForFeatureIdentifier:
- _objc_msgSend$_featureIdentifier
- _objc_msgSend$_healthChecklistSettingsFooter
- _objc_msgSend$_highlightGeneration
- _objc_msgSend$_isOnboarded
- _objc_msgSend$_isWatchSettingsVisibleWithFeatureStatus:
- _objc_msgSend$_lifeFactorPlatterGeneration
- _objc_msgSend$_localCountryIsSupportedRequirementForFeatureIdentifier:
- _objc_msgSend$_mutualExclusivityEnforcement
- _objc_msgSend$_nanoSettingsEnablement
- _objc_msgSend$_nanoSettingsVisibility
- _objc_msgSend$_notInPregnancyMode
- _objc_msgSend$_notOnboardedHealthChecklist
- _objc_msgSend$_notificationGeneration
- _objc_msgSend$_notificationSettingsVisibilityForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_notificationsEnabledWithFeatureStatus:
- _objc_msgSend$_onboardedHealthChecklist
- _objc_msgSend$_onboardingAcknowledgedWithFeatureStatus:
- _objc_msgSend$_onboardingInitiation
- _objc_msgSend$_onboardingInitiationForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_onboardingInitiationRequirementsForFeatureIdentifier:
- _objc_msgSend$_onboardingPromotionRequirementsForFeatureIdentifier:
- _objc_msgSend$_onboardingRecordRequirement
- _objc_msgSend$_pdfGeneration
- _objc_msgSend$_postPregnancyAdjustmentEligibility
- _objc_msgSend$_pregnancyAdjustmentEligibility
- _objc_msgSend$_pregnancyAdjustmentEligibilityForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_promotion
- _objc_msgSend$_promotionForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_remoteCountryIsSupportedRequirementForFeatureIdentifier:isSupportedIfCountryListMissing:
- _objc_msgSend$_requirementIdentifiersForRequirements:
- _objc_msgSend$_requirementsByContextForFeatureIdentifier:
- _objc_msgSend$_settingsUserInteractionEnabledForFeatureIdentifier:
- _objc_msgSend$_settingsVisibilityRequirementsForFeatureIdentifier:
- _objc_msgSend$_settingsVisibilityWithFeatureOnboarded:forFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_setupVersionManagersWithIsOnboardingRecordPresent:
- _objc_msgSend$_sharedFeatureIdentifier
- _objc_msgSend$_showOnboardingWithFeatureStatus:
- _objc_msgSend$_tipsAppVisibility
- _objc_msgSend$_upgradeInitiation
- _objc_msgSend$_upgradePromotion
- _objc_msgSend$_usage
- _objc_msgSend$_usageForFeatureIdentifier:featureFlagIsEnabled:
- _objc_msgSend$_usageRequirementsForFeatureIdentifier:
- _objc_msgSend$_watchFooterForEvaluation::
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$areRegionAndWatchSupportedVersionsMismatched
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_msgSend$arrayWithArray:
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$featureStatus
- _objc_msgSend$hk_filter:
- _objc_msgSend$hk_map:
- _objc_msgSend$hk_removeObjectsPassingTest:
- _objc_msgSend$initWithFeatureIdentifier:healthStore:countryCodeSource:
- _objc_msgSend$mutableCopy
- _objc_msgSend$onboardingState
- _objc_msgSend$removeObject:
- _objc_msgSend$setFeatureStatus:
CStrings:
+ "+[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatchedWithIsOnboardingRecordPresent:]"
+ "-[HKHRHypertensionNotificationsSettings _isWatchSettingsVisible]"
+ "2.0"
+ "Heartbeat series feature status is only available on watchOS"
+ "Requirements evaluations should never be nil."
+ "[%{public}@:%p] Heartbeat series feature status is unavailable off-watch; refusing to register %@"
- "-[HKHRHypertensionNotificationsSettings _isWatchSettingsVisibleWithFeatureStatus:]"
- "-[HKHRHypertensionNotificationsSettings areRegionAndWatchSupportedVersionsMismatched]"
- "@\"NSString\"16@?0@\"<HKFeatureAvailabilityRequirement>\"8"
- "B16@?0@\"<HKFeatureAvailabilityRequirement>\"8"
- "Feature status should never be nil."
```
