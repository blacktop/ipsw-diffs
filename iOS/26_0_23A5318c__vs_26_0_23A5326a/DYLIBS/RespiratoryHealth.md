## RespiratoryHealth

> `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth`

```diff

-6106.1.2.5.0
-  __TEXT.__text: 0x5894
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x93c
+6106.1.2.9.0
+  __TEXT.__text: 0x62e8
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x954
   __TEXT.__const: 0x72
-  __TEXT.__oslogstring: 0x8c0
-  __TEXT.__cstring: 0x734
+  __TEXT.__oslogstring: 0x902
+  __TEXT.__cstring: 0xae4
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x2c9
-  __TEXT.__objc_methname: 0x1b45
-  __TEXT.__objc_methtype: 0x470
-  __TEXT.__objc_stubs: 0x1120
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x268
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x2cc
+  __TEXT.__objc_methname: 0x1ca1
+  __TEXT.__objc_methtype: 0x4ae
+  __TEXT.__objc_stubs: 0x11e0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x710
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x12f8
+  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x1368
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x300
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C7D533B5-DD0D-315C-B249-67242203FE40
-  Functions: 192
-  Symbols:   819
-  CStrings:  490
+  UUID: E74013C5-06BE-359F-9F2F-EFE1E432A6E3
+  Functions: 198
+  Symbols:   845
+  CStrings:  541
 
Symbols:
+ -[HKRPOxygenSaturationSettings _loadFeatureStatus]
+ -[HKRPOxygenSaturationSettings initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:]
+ -[HKRPOxygenSaturationSettings isCompanionAnalysisEnabled]
+ _HKFeatureAvailabilityContextAnalysis
+ _HKFeatureAvailabilityContextMutualExclusivityEnforcement
+ _HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis
+ _HKHROxygenSaturationShowAllDataLinkUrlPathComponent
+ _HKHROxygenSaturationUnsuccessfulAnalysisEventSampleDetailsLinkUrlPathComponent
+ _HKRPCompanionAnalysisLocalizedString
+ _HKRPOxygenSaturationCompanionAnalysisLocalFeatureAttributes
+ _HKRPOxygenSaturationRecordingCompanionAnalysisFeatureAvailabilityRequirements
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_IVAR_$_HKRPOxygenSaturationSettings._companionAnalysisFeatureStatusManager
+ _OBJC_IVAR_$_HKRPOxygenSaturationSettings._lock
+ _OBJC_IVAR_$_HKRPOxygenSaturationSettings._lock_companionAnalysisFeatureStatus
+ ___NSArray0__struct
+ _objc_msgSend$areAllRequirementsSatisfied
+ _objc_msgSend$featureStatusWithError:
+ _objc_msgSend$initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:
+ _objc_msgSend$isCompanionAnalysisEnabled
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$mutuallyExclusiveFeatureIsOffWithIdentifier:
+ _objc_msgSend$seedIsNotExpiredForFeatureWithIdentifier:
+ _objc_retain_x25
- _objc_msgSend$initWithUserDefaults:userDefaultsSyncProvider:
Functions:
~ -[HKRPOxygenSaturationSettings initWithUserDefaults:userDefaultsSyncProvider:] : 212 -> 8
+ -[HKRPOxygenSaturationSettings initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:]
~ +[HKRPOxygenSaturationSettings standardSettings] : 144 -> 216
+ -[HKRPOxygenSaturationSettings isCompanionAnalysisEnabled]
~ -[HKRPOxygenSaturationSettings .cxx_destruct] : 80 -> 104
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsWithAgeGatingEnabledHeader] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsHeader] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) bloodOxygenRecordingsTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) featureActiveStatusTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) featureActiveStatusDescription] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) featureInactiveStatusTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) featureInactiveStatusDescription] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsFooter] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) learnMoreAboutBloodOxygenURL] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) aboutBloodOxygenFooter] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) aboutBloodOxygenFooterWithLearnMore] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsDetailOptionsTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) backgroundRecordingsDetailOptionsFooter] : 184 -> 248
~ -[HKRPOxygenSaturationSettings(Localization) howToTakeARecordingEducationTitle] : 12 -> 80
~ -[HKRPOxygenSaturationSettings(Localization) recordingInactiveDescription] : 12 -> 80
~ _HKRPOxygenSaturationFeatureAvailabilityRequirements : 824 -> 1276
+ _HKRPOxygenSaturationRecordingCompanionAnalysisFeatureAvailabilityRequirements
+ _HKRPCompanionAnalysisLocalizedString
+ _HKRPOxygenSaturationCompanionAnalysisLocalFeatureAttributes
+ -[HKRPOxygenSaturationSettings _loadFeatureStatus]
CStrings:
+ "1.1"
+ "@\"HKFeatureStatus\""
+ "@\"HKFeatureStatusManager\""
+ "@40@0:8@16@24@32"
+ "COMPANION_ANALYSIS_ABOUT_BLOOD_OXYGEN"
+ "COMPANION_ANALYSIS_BACKGROUND_RECORDING_DESCRIPTION"
+ "COMPANION_ANALYSIS_BACKGROUND_RECORDING_OPTION_FOOTER"
+ "COMPANION_ANALYSIS_BACKGROUND_RECORDING_OPTION_FOOTER_WRIST_DETECT_TURNED_OFF_%@"
+ "COMPANION_ANALYSIS_BACKGROUND_RECORDING_OPTION_TITLE"
+ "COMPANION_ANALYSIS_BLOOD_OXYGEN_RECORDINGS"
+ "COMPANION_ANALYSIS_HOW_TO_MAKE_A_RECORDING"
+ "COMPANION_ANALYSIS_LEARN_MORE_ABOUT_BLOOD_OXYGEN"
+ "COMPANION_ANALYSIS_LEARN_MORE_ABOUT_BLOOD_OXYGEN_LINK_URL"
+ "COMPANION_ANALYSIS_OXYGEN_SATURATION_FEATURE_ACTIVE_DESCRIPTION"
+ "COMPANION_ANALYSIS_OXYGEN_SATURATION_FEATURE_ACTIVE_STATUS"
+ "COMPANION_ANALYSIS_OXYGEN_SATURATION_FEATURE_INACTIVE_DESCRIPTION"
+ "COMPANION_ANALYSIS_OXYGEN_SATURATION_FEATURE_INACTIVE_STATUS"
+ "COMPANION_ANALYSIS_RECORDINGS_DESCRIPTION"
+ "COMPANION_ANALYSIS_RECORDINGS_DESCRIPTION_AGE_GATING_ENABLED"
+ "Localizable-Windbreaker"
+ "OxygenSaturationShowAllData"
+ "OxygenSaturationUnsuccessfulAnalysisEventSampleDetails"
+ "[%{public}@] Failed to load feature status with error: %{public}@"
+ "_companionAnalysisFeatureStatusManager"
+ "_lock_companionAnalysisFeatureStatus"
+ "areAllRequirementsSatisfied"
+ "featureStatusWithError:"
+ "initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:"
+ "isCompanionAnalysisEnabled"
+ "localizedDescription"
+ "mutuallyExclusiveFeatureIsOffWithIdentifier:"
+ "seedIsNotExpiredForFeatureWithIdentifier:"

```
