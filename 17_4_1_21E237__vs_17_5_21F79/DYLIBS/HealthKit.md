## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-4146.4.18.0.0
+4146.5.13.0.0
   __TEXT.__text: 0x26b5d0
   __TEXT.__auth_stubs: 0x24d0
   __TEXT.__objc_methlist: 0x27a74
-  __TEXT.__cstring: 0x2bb89
+  __TEXT.__cstring: 0x2bbf9
   __TEXT.__const: 0x4030
   __TEXT.__oslogstring: 0xb079
   __TEXT.__gcc_except_tab: 0x3628

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0xc770
   __TEXT.__eh_frame: 0x1300
-  __TEXT.__objc_classname: 0x7780
-  __TEXT.__objc_methname: 0x54b7e
+  __TEXT.__objc_classname: 0x777e
+  __TEXT.__objc_methname: 0x54b78
   __TEXT.__objc_methtype: 0xb1d6
   __TEXT.__objc_stubs: 0x272c0
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0xd9e0
+  __DATA_CONST.__const: 0xd9f0
   __DATA_CONST.__objc_classlist: 0x17a8
   __DATA_CONST.__objc_catlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x720

   __DATA_CONST.__objc_classrefs: 0x1658
   __DATA_CONST.__objc_superrefs: 0x1560
   __DATA_CONST.__objc_arraydata: 0x66c8
-  __AUTH_CONST.__cfstring: 0x2d680
+  __AUTH_CONST.__cfstring: 0x2d6c0
   __AUTH_CONST.__objc_const: 0x17760
   __AUTH_CONST.__const: 0x5e88
   __AUTH_CONST.__objc_intobj: 0x42f0

   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__auth_got: 0x1280
-  __AUTH.__objc_data: 0xcc78
+  __AUTH.__objc_data: 0xcc28
   __AUTH.__data: 0xd20
   __DATA.__got_weak: 0x8
   __DATA.__objc_ivar: 0x29e8
   __DATA.__data: 0x9bd0
   __DATA.__bss: 0x53e0
   __DATA.__common: 0x940
-  __DATA_DIRTY.__objc_data: 0x2030
+  __DATA_DIRTY.__objc_data: 0x2080
   __DATA_DIRTY.__bss: 0xad8
   __DATA_DIRTY.__common: 0xe8
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6B4B0FB5-85F8-3FDF-B77F-9473F9958EA6
+  UUID: 94D9F2DB-6E38-3206-A392-2F0857896DA9
   Functions: 18427
-  Symbols:   52784
-  CStrings:  26914
+  Symbols:   52786
+  CStrings:  26918
 
Symbols:
+ +[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled requirementIdentifier]
+ +[HKFeatureAvailabilityRequirements bloodOxygenRecordingsAreEnabled]
+ -[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled defaultValueWhenKeyIsMissing]
+ -[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled init]
+ -[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled isSatisfiedForBoolValue:]
+ -[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled requirementDescription]
+ -[HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled whichUserDefaultsDataSourceInDataSource:]
+ _HKFeatureAvailabilityRequirementIdentifierBloodOxygenRecordingsAreEnabled
+ _HKRespiratoryKeyBackgroundRecordingsEnabled
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
+ _OBJC_METACLASS_$_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
+ __HKPrivateMetadataKeyVisionReaderStrengthRangeHigh
+ __HKPrivateMetadataKeyVisionReaderStrengthRangeLow
+ __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
+ __OBJC_$_INSTANCE_METHODS_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
+ __OBJC_CLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
+ __OBJC_METACLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled
- +[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled requirementIdentifier]
- +[HKFeatureAvailabilityRequirements bloodOxygenMeasurementsAreEnabled]
- -[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled defaultValueWhenKeyIsMissing]
- -[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled init]
- -[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled isSatisfiedForBoolValue:]
- -[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled requirementDescription]
- -[HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled whichUserDefaultsDataSourceInDataSource:]
- _HKFeatureAvailabilityRequirementIdentifierBloodOxygenMeasurementsAreEnabled
- _HKRespiratoryKeyBackgroundMeasurementsEnabled
- _OBJC_CLASS_$_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
- _OBJC_METACLASS_$_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
- __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
- __OBJC_$_INSTANCE_METHODS_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
- __OBJC_CLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
- __OBJC_METACLASS_RO_$_HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled
CStrings:
+ "Blood Oxygen Recordings must be enabled"
+ "BloodOxygenRecordingsAreEnabled"
+ "HKFeatureAvailabilityRequirementBloodOxygenRecordingsAreEnabled"
+ "_HKPrivateMetadataKeyVisionReaderStrengthRangeHigh"
+ "_HKPrivateMetadataKeyVisionReaderStrengthRangeLow"
+ "bloodOxygenRecordingsAreEnabled"
- "Blood Oxygen Measurements must be enabled"
- "BloodOxygenMeasurementsAreEnabled"
- "HKFeatureAvailabilityRequirementBloodOxygenMeasurementsAreEnabled"
- "bloodOxygenMeasurementsAreEnabled"

```
