## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6200.2.14.2.5
-  __TEXT.__text: 0x348748
+6200.3.4.0.0
+  __TEXT.__text: 0x34947c
   __TEXT.__auth_stubs: 0x3790
-  __TEXT.__objc_methlist: 0x30324
-  __TEXT.__cstring: 0x35d23
-  __TEXT.__const: 0xac5c2
+  __TEXT.__objc_methlist: 0x3042c
+  __TEXT.__cstring: 0x35e63
+  __TEXT.__const: 0xac772
   __TEXT.__oslogstring: 0xc773
-  __TEXT.__gcc_except_tab: 0x422c
+  __TEXT.__gcc_except_tab: 0x4298
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__constg_swiftt: 0x3064

   __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xfe18
+  __TEXT.__unwind_info: 0xfe98
   __TEXT.__eh_frame: 0x4628
-  __TEXT.__objc_classname: 0x8a0d
-  __TEXT.__objc_methname: 0x5f607
-  __TEXT.__objc_methtype: 0xc05d
-  __TEXT.__objc_stubs: 0x2bfc0
+  __TEXT.__objc_classname: 0x8aba
+  __TEXT.__objc_methname: 0x5f813
+  __TEXT.__objc_methtype: 0xc049
+  __TEXT.__objc_stubs: 0x2c000
   __DATA_CONST.__got: 0x1b68
-  __DATA_CONST.__const: 0xf6c8
-  __DATA_CONST.__objc_classlist: 0x1ae0
+  __DATA_CONST.__const: 0xf6e0
+  __DATA_CONST.__objc_classlist: 0x1ae8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x118b8
+  __DATA_CONST.__objc_selrefs: 0x11908
   __DATA_CONST.__objc_protorefs: 0x618
-  __DATA_CONST.__objc_superrefs: 0x1738
+  __DATA_CONST.__objc_superrefs: 0x1740
   __DATA_CONST.__objc_arraydata: 0x6968
   __AUTH_CONST.__auth_got: 0x1be0
-  __AUTH_CONST.__const: 0xc6a0
-  __AUTH_CONST.__cfstring: 0x32ac0
-  __AUTH_CONST.__objc_const: 0x509a8
+  __AUTH_CONST.__const: 0xc700
+  __AUTH_CONST.__cfstring: 0x32b20
+  __AUTH_CONST.__objc_const: 0x50b08
   __AUTH_CONST.__objc_intobj: 0x4620
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x750
-  __AUTH.__objc_data: 0xecb8
+  __AUTH.__objc_data: 0xed08
   __AUTH.__data: 0x19a8
-  __DATA.__objc_ivar: 0x2e74
+  __DATA.__objc_ivar: 0x2e84
   __DATA.__data: 0xd0c8
   __DATA.__bss: 0x18c40
   __DATA.__common: 0x9c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8F3C8E32-71B6-3BCA-A149-54EF452D0257
-  Functions: 24354
-  Symbols:   61441
-  CStrings:  30242
+  UUID: F7871108-1A8B-3F32-BA95-F70FE1DCE7F8
+  Functions: 24376
+  Symbols:   61508
+  CStrings:  30267
 
Symbols:
+ +[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch requirementIdentifier]
+ +[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch supportsSecureCoding]
+ +[HKFeatureAvailabilityRequirements bloodOxygenCompanionAnalysisIsSupportedOnActiveWatchWithCapabilitySupportedOnLocalDevice:]
+ +[HKImportExclusionDeviceDataSource(HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisAllowedDeviceSerialNumbers) isDeviceSerialNumberOnAllowedListForHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch capabilitySupportedOnLocalDevice]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch encodeWithCoder:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch hash]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch initWithCapabilitySupportedOnLocalDevice:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch initWithCoder:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch isEqual:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch isSatisfiedWithDataSource:error:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch registerObserver:forDataSource:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch requiredEntitlements]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch requirementDescription]
+ -[HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch unregisterObserver:fromDataSource:]
+ -[HKImportExclusionDeviceDataSource isDeviceSerialNumberOnImportAllowList:featureIdentifier:]
+ -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithSerialNumber:]
+ -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:]
+ -[_HKFeatureFlags setSleepScoreVersion2:]
+ -[_HKFeatureFlags setSleepScoreVersion3:]
+ -[_HKFeatureFlags setVitalsCompanionBloodOxygenAnalysis:]
+ -[_HKFeatureFlags sleepScoreVersion2]
+ -[_HKFeatureFlags sleepScoreVersion3]
+ -[_HKFeatureFlags vitalsCompanionBloodOxygenAnalysis]
+ GCC_except_table159
+ _HKFeatureAvailabilityRequirementIdentifierBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ _OBJC_IVAR_$_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch._capabilitySupportedOnLocalDevice
+ _OBJC_IVAR_$__HKFeatureFlags._sleepScoreVersion2
+ _OBJC_IVAR_$__HKFeatureFlags._sleepScoreVersion3
+ _OBJC_IVAR_$__HKFeatureFlags._vitalsCompanionBloodOxygenAnalysis
+ _OBJC_METACLASS_$_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_$_CLASS_METHODS_HKImportExclusionDeviceDataSource(HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceTypes|HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceSerialNumbers|HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisAllowedDeviceSerialNumbers|HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceSerialNumbersTIB)
+ __OBJC_$_INSTANCE_METHODS_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_$_INSTANCE_VARIABLES_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_$_PROP_LIST_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_CLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __OBJC_METACLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch
+ __ZN64hk_HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisL30allowed_encoded_serial_numbersE
+ __ZN64hk_HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisL33additional_allowed_serial_numbersE
+ ___37-[_HKFeatureFlags sleepScoreVersion2]_block_invoke
+ ___37-[_HKFeatureFlags sleepScoreVersion3]_block_invoke
+ ___53-[_HKFeatureFlags vitalsCompanionBloodOxygenAnalysis]_block_invoke
+ ___block_literal_global.172
+ ___block_literal_global.178
+ _objc_msgSend$initWithCapabilitySupportedOnLocalDevice:
+ _objc_msgSend$isDeviceSerialNumberOnAllowedListForHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis:
+ _objc_msgSend$isDeviceSerialNumberOnImportAllowList:featureIdentifier:
+ _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithSerialNumber:
+ _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:
- -[HKImportExclusionDeviceDataSource isDeviceSerialNumberOnPreImportExclusionList:featureIdentifier:]
- -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:]
- -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:]
- -[HKImportExclusionDeviceDataSource isImportAllowedForActiveWatchWithBehavior:featureIdentifier:].cold.3
- GCC_except_table129
- GCC_except_table132
- GCC_except_table135
- __OBJC_$_CLASS_METHODS_HKImportExclusionDeviceDataSource(HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceTypes|HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceSerialNumbers|HKFeatureIdentifierOxygenSaturationRecordingAllowedDeviceSerialNumbersTIB)
- _objc_msgSend$isDeviceSerialNumberOnPreImportExclusionList:featureIdentifier:
- _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:
- _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:
CStrings:
+ "Blood Oxygen Companion Analysis must be supported on active watch"
+ "Blood Oxygen Companion Analysis must be supported on watch"
+ "BloodOxygenCompanionAnalysisIsSupportedOnActiveWatch"
+ "Could not determine active watch fuse"
+ "HKFeatureAvailabilityRequirementBloodOxygenCompanionAnalysisIsSupportedOnActiveWatch"
+ "HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisAllowedDeviceSerialNumbers"
+ "TB,R,N,V_capabilitySupportedOnLocalDevice"
+ "_capabilitySupportedOnLocalDevice"
+ "_sleepScoreVersion2"
+ "_sleepScoreVersion3"
+ "_vitalsCompanionBloodOxygenAnalysis"
+ "bloodOxygenCompanionAnalysisIsSupportedOnActiveWatchWithCapabilitySupportedOnLocalDevice:"
+ "capabilitySupportedOnLocalDevice"
+ "initWithCapabilitySupportedOnLocalDevice:"
+ "isDeviceSerialNumberOnAllowedListForHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis:"
+ "isDeviceSerialNumberOnImportAllowList:featureIdentifier:"
+ "isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithSerialNumber:"
+ "isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:"
+ "setSleepScoreVersion2:"
+ "setSleepScoreVersion3:"
+ "setVitalsCompanionBloodOxygenAnalysis:"
+ "sleepScoreVersion2"
+ "sleepScoreVersion3"
+ "vitalsCompanionBloodOxygenAnalysis"
- "@44@0:8@16B24@28@36"
- "LM"
- "LW"
- "isDeviceSerialNumberOnPreImportExclusionList:featureIdentifier:"
- "isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:"
- "isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:"

```
