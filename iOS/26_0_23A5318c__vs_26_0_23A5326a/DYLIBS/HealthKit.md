## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6106.1.2.5.0
-  __TEXT.__text: 0x3327b4
+6106.1.2.9.0
+  __TEXT.__text: 0x3330c4
   __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__objc_methlist: 0x2f8f4
-  __TEXT.__cstring: 0x34c03
+  __TEXT.__objc_methlist: 0x2f98c
+  __TEXT.__cstring: 0x34d73
   __TEXT.__const: 0xabfa2
   __TEXT.__oslogstring: 0xc263
-  __TEXT.__gcc_except_tab: 0x4064
+  __TEXT.__gcc_except_tab: 0x4070
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x5da
   __TEXT.__constg_swiftt: 0x2fa4

   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf8b0
+  __TEXT.__unwind_info: 0xf8d8
   __TEXT.__eh_frame: 0x3fe8
-  __TEXT.__objc_classname: 0x8971
-  __TEXT.__objc_methname: 0x5d60f
-  __TEXT.__objc_methtype: 0xbf29
-  __TEXT.__objc_stubs: 0x2b240
-  __DATA_CONST.__got: 0x1b08
-  __DATA_CONST.__const: 0xf460
-  __DATA_CONST.__objc_classlist: 0x1aa8
+  __TEXT.__objc_classname: 0x89b5
+  __TEXT.__objc_methname: 0x5d7b3
+  __TEXT.__objc_methtype: 0xbf51
+  __TEXT.__objc_stubs: 0x2b2a0
+  __DATA_CONST.__got: 0x1b10
+  __DATA_CONST.__const: 0xf4a0
+  __DATA_CONST.__objc_classlist: 0x1ab8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11340
+  __DATA_CONST.__objc_selrefs: 0x11360
   __DATA_CONST.__objc_protorefs: 0x608
-  __DATA_CONST.__objc_superrefs: 0x1728
-  __DATA_CONST.__objc_arraydata: 0x68e8
+  __DATA_CONST.__objc_superrefs: 0x1730
+  __DATA_CONST.__objc_arraydata: 0x6910
   __AUTH_CONST.__auth_got: 0x1b80
   __AUTH_CONST.__const: 0xbff8
-  __AUTH_CONST.__cfstring: 0x32080
-  __AUTH_CONST.__objc_const: 0x4fc50
-  __AUTH_CONST.__objc_intobj: 0x4590
+  __AUTH_CONST.__cfstring: 0x321a0
+  __AUTH_CONST.__objc_const: 0x4fe08
+  __AUTH_CONST.__objc_intobj: 0x45c0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
-  __AUTH_CONST.__objc_arrayobj: 0x6d8
-  __AUTH.__objc_data: 0xea50
+  __AUTH_CONST.__objc_arrayobj: 0x6f0
+  __AUTH.__objc_data: 0xeaf0
   __AUTH.__data: 0x1938
-  __DATA.__objc_ivar: 0x2dcc
+  __DATA.__objc_ivar: 0x2dd0
   __DATA.__data: 0xce58
-  __DATA.__bss: 0x182a0
+  __DATA.__bss: 0x182b0
   __DATA.__common: 0x9a0
   __DATA_DIRTY.__objc_data: 0x2480
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7F0CD6A3-FA24-3D9D-8C1E-333C4267A721
-  Functions: 23891
-  Symbols:   60650
-  CStrings:  29742
+  UUID: DAAC16C5-3C18-3E04-A611-43560D795EE8
+  Functions: 23905
+  Symbols:   60700
+  CStrings:  29770
 
Symbols:
+ +[HKObjectType unprocessedBloodOxygenDataType]
+ +[HKUnprocessedBloodOxygenDataSample _isConcreteObjectClass]
+ +[HKUnprocessedBloodOxygenDataSample supportsSecureCoding]
+ +[HKUnprocessedBloodOxygenDataSample unprocessedBloodOxygenDataSampleWithPayload:startDate:endDate:device:metadata:]
+ -[HKFeatureAvailabilityRequirementSatisfactionOverrideEligibility isRequirementOverridable:featureIdentifier:importExclusionDeviceDataSource:behavior:]
+ -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:]
+ -[HKImportExclusionDeviceDataSource isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:]
+ -[HKImportExclusionDeviceDataSource isImportAllowedForActiveWatchWithBehavior:featureIdentifier:].cold.3
+ -[HKUnprocessedBloodOxygenDataSample .cxx_destruct]
+ -[HKUnprocessedBloodOxygenDataSample _setPayload:]
+ -[HKUnprocessedBloodOxygenDataSample encodeWithCoder:]
+ -[HKUnprocessedBloodOxygenDataSample initWithCoder:]
+ -[HKUnprocessedBloodOxygenDataSample payload]
+ _HKCategoryTypeIdentifierUnsuccessfulBloodOxygenSaturationAnalysisEvent
+ _HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis
+ _OBJC_CLASS_$_HKUnprocessedBloodOxygenDataSample
+ _OBJC_CLASS_$_HKUnprocessedBloodOxygenDataType
+ _OBJC_IVAR_$_HKUnprocessedBloodOxygenDataSample._payload
+ _OBJC_METACLASS_$_HKUnprocessedBloodOxygenDataSample
+ _OBJC_METACLASS_$_HKUnprocessedBloodOxygenDataType
+ __HKDataTypeIdentifierUnprocessedBloodOxygenData
+ __OBJC_$_CLASS_METHODS_HKUnprocessedBloodOxygenDataSample
+ __OBJC_$_INSTANCE_METHODS_HKUnprocessedBloodOxygenDataSample
+ __OBJC_$_INSTANCE_VARIABLES_HKUnprocessedBloodOxygenDataSample
+ __OBJC_$_PROP_LIST_HKUnprocessedBloodOxygenDataSample
+ __OBJC_CLASS_PROTOCOLS_$_HKUnprocessedBloodOxygenDataSample
+ __OBJC_CLASS_RO_$_HKUnprocessedBloodOxygenDataSample
+ __OBJC_CLASS_RO_$_HKUnprocessedBloodOxygenDataType
+ __OBJC_METACLASS_RO_$_HKUnprocessedBloodOxygenDataSample
+ __OBJC_METACLASS_RO_$_HKUnprocessedBloodOxygenDataType
+ ___116+[HKUnprocessedBloodOxygenDataSample unprocessedBloodOxygenDataSampleWithPayload:startDate:endDate:device:metadata:]_block_invoke
+ ___block_descriptor_40_e8_32s_e44_v16?0"HKUnprocessedBloodOxygenDataSample"8ls32l8
+ _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:
+ _objc_msgSend$isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:
+ _objc_msgSend$isRequirementOverridable:featureIdentifier:importExclusionDeviceDataSource:behavior:
+ _objc_msgSend$unprocessedBloodOxygenDataType
- -[HKFeatureAvailabilityRequirementSatisfactionOverrideEligibility isRequirementOverridable:featureIdentifier:dataSource:]
- _objc_msgSend$isRequirementOverridable:featureIdentifier:dataSource:
CStrings:
+ "@44@0:8@16B24@28@36"
+ "B48@0:8@16@24@32@40"
+ "Blood Oxygen Companion Analysis"
+ "HKCategoryTypeIdentifierUnsuccessfulBloodOxygenSaturationAnalysisEvent"
+ "HKDataTypeIdentifierUnprocessedBloodOxygenData"
+ "HKUnprocessedBloodOxygenDataSample"
+ "HKUnprocessedBloodOxygenDataType"
+ "LW"
+ "Oxygen Saturation Phone-Only"
+ "OxygenSaturationRecordingCompanionAnalysis"
+ "PayloadDataKey"
+ "T@\"NSData\",R,C,N,V_payload"
+ "blood_oxygen_companion_analysis"
+ "isHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisImportAllowedForActiveWatchWithDeviceType:prodFused:serialNumber:regionCode:"
+ "isHKFeatureIdentifierOxygenSaturationRecordingImportAllowedForActiveWatchWithDeviceType:serialNumber:regionCode:"
+ "isRequirementOverridable:featureIdentifier:importExclusionDeviceDataSource:behavior:"
+ "unprocessedBloodOxygenDataSampleWithPayload:startDate:endDate:device:metadata:"
+ "unprocessedBloodOxygenDataType"
+ "v16@?0@\"HKUnprocessedBloodOxygenDataSample\"8"
- "Reserved14"
- "isRequirementOverridable:featureIdentifier:dataSource:"

```
