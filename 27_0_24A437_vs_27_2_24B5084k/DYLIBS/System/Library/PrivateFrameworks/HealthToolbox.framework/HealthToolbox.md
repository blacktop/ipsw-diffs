## HealthToolbox

> `/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x60688
-  __TEXT.__objc_methlist: 0x6f18
-  __TEXT.__cstring: 0x7881
+7027.1.36.2.7
+  __TEXT.__text: 0x62500
+  __TEXT.__objc_methlist: 0x6fe8
+  __TEXT.__cstring: 0x7a21
   __TEXT.__const: 0x1a6
-  __TEXT.__oslogstring: 0x18c2
-  __TEXT.__gcc_except_tab: 0xc00
+  __TEXT.__oslogstring: 0x1cf2
+  __TEXT.__gcc_except_tab: 0xc34
   __TEXT.__dlopen_cstrs: 0x4b
   __TEXT.__ustring: 0x38
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xc
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1f88
+  __TEXT.__unwind_info: 0x1ff8
   __TEXT.__eh_frame: 0xb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1938
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__const: 0x1948
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4830
+  __DATA_CONST.__objc_selrefs: 0x4868
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0xc70
+  __DATA_CONST.__got: 0xc68
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5440
-  __AUTH_CONST.__objc_const: 0xb050
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0xb2b8
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH.__objc_data: 0x2300
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH.__objc_data: 0x23a0
   __AUTH.__data: 0x130
-  __DATA.__objc_ivar: 0x68c
-  __DATA.__data: 0xff0
+  __DATA.__objc_ivar: 0x6ac
+  __DATA.__data: 0x1050
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/PDFKit.framework/PDFKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
-  - /System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI
   - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
+  - /System/Library/PrivateFrameworks/HealthFoundationUI.framework/HealthFoundationUI
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2350
-  Symbols:   6415
-  CStrings:  1069
+  Functions: 2380
+  Symbols:   6454
+  CStrings:  1095
 
Symbols:
+ -[WDBilateralQuantityListDataProvider initWithDisplayType:profile:]
+ -[WDBilateralQuantityListDataProvider sampleTypes]
+ -[WDBilateralQuantityListDataProvider textForObject:]
+ -[WDBilateralQuantityListDataProvider titleForSection:]
+ -[WDBuddyFlowUserInfoViewController buddyFlowUserInfoDidUpdateValue:]
+ -[WDDisplayTypeDataSourcesTableViewController _createHeaderView]
+ -[WDExportManager exportError]
+ -[WDExportManager setExportError:]
+ -[WDHealthReportListDataProvider sampleTypes]
+ -[WDHealthReportListDataProvider textForObject:]
+ -[WDOverheadSquatListDataProvider sampleTypes]
+ -[WDOverheadSquatListDataProvider textForObject:]
+ -[WDProfileTableViewCell _setupDescriptionConstraints]
+ -[WDProfileTableViewCell _syncDisplayValueText]
+ -[WDProfileTableViewCell _updateDescriptionLayout]
+ -[WDProfileTableViewCell descriptionText]
+ -[WDProfileTableViewCell setDescriptionText:]
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table63
+ GCC_except_table70
+ GCC_except_table85
+ GCC_except_table96
+ _OBJC_CLASS_$_HKBilateralQuantityType
+ _OBJC_CLASS_$_WDBilateralQuantityListDataProvider
+ _OBJC_CLASS_$_WDHealthReportListDataProvider
+ _OBJC_CLASS_$_WDOverheadSquatListDataProvider
+ _OBJC_IVAR_$_WDExportManager._exportError
+ _OBJC_IVAR_$_WDProfileTableViewCell._accessibilitySizeDescriptionConstraints
+ _OBJC_IVAR_$_WDProfileTableViewCell._activeDescriptionConstraints
+ _OBJC_IVAR_$_WDProfileTableViewCell._descriptionLabel
+ _OBJC_IVAR_$_WDProfileTableViewCell._descriptionText
+ _OBJC_IVAR_$_WDProfileTableViewCell._displayNameCenterYConstraint
+ _OBJC_IVAR_$_WDProfileTableViewCell._displayValueCenterYConstraint
+ _OBJC_IVAR_$_WDProfileTableViewCell._normalSizeDescriptionConstraints
+ _OBJC_METACLASS_$_WDBilateralQuantityListDataProvider
+ _OBJC_METACLASS_$_WDHealthReportListDataProvider
+ _OBJC_METACLASS_$_WDOverheadSquatListDataProvider
+ __OBJC_$_INSTANCE_METHODS_WDBilateralQuantityListDataProvider
+ __OBJC_$_INSTANCE_METHODS_WDHealthReportListDataProvider
+ __OBJC_$_INSTANCE_METHODS_WDOverheadSquatListDataProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WDBuddyFlowUserInfoDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WDBuddyFlowUserInfoDelegate
+ __OBJC_$_PROTOCOL_REFS_WDBuddyFlowUserInfoDelegate
+ __OBJC_CLASS_RO_$_WDBilateralQuantityListDataProvider
+ __OBJC_CLASS_RO_$_WDHealthReportListDataProvider
+ __OBJC_CLASS_RO_$_WDOverheadSquatListDataProvider
+ __OBJC_LABEL_PROTOCOL_$_WDBuddyFlowUserInfoDelegate
+ __OBJC_METACLASS_RO_$_WDBilateralQuantityListDataProvider
+ __OBJC_METACLASS_RO_$_WDHealthReportListDataProvider
+ __OBJC_METACLASS_RO_$_WDOverheadSquatListDataProvider
+ __OBJC_PROTOCOL_$_WDBuddyFlowUserInfoDelegate
+ ___61-[WDBuddyFlowUserInfoViewController _saveDataWithCompletion:]_block_invoke_3
+ ___block_descriptor_56_e8_32s40s48s_e56_v36?0"HKWorkoutRouteQuery"8"NSArray"16B24"NSError"28ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e47_v32?0"HKSampleQuery"8"NSArray"16"NSError"24lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_HealthToolbox
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_HealthToolbox
+ _objc_msgSend$_createHeaderView
+ _objc_msgSend$_setupDescriptionConstraints
+ _objc_msgSend$_syncDisplayValueText
+ _objc_msgSend$_updateContinueButtonState
+ _objc_msgSend$_updateDescriptionLayout
+ _objc_msgSend$buddyFlowUserInfoDidUpdateValue:
+ _objc_msgSend$compensations
+ _objc_msgSend$error
+ _objc_msgSend$exportError
+ _objc_msgSend$hk_error:format:
+ _objc_msgSend$leftQuantity
+ _objc_msgSend$omakase
+ _objc_msgSend$rightQuantity
+ _objc_msgSend$setExportError:
+ _objc_msgSend$setLayoutMarginsWithTableView:
- +[HBXFitnessManager divingFitnessNonGradientTextColor]
- +[HBXFitnessManager fitnessIconFor:]
- +[HBXFitnessManager fitnessNonGradientTextColor]
- GCC_except_table35
- GCC_except_table41
- GCC_except_table62
- GCC_except_table69
- GCC_except_table83
- GCC_except_table95
- _FIUIStaticWorkoutIconImage
- _OBJC_CLASS_$_ARUIMetricColors
- _OBJC_CLASS_$_FIUIWorkoutActivityType
- _OBJC_CLASS_$_HBXFitnessManager
- _OBJC_METACLASS_$_HBXFitnessManager
- _OUTLINED_FUNCTION_5
- __OBJC_$_CLASS_METHODS_HBXFitnessManager
- __OBJC_CLASS_RO_$_HBXFitnessManager
- __OBJC_METACLASS_RO_$_HBXFitnessManager
- ___36-[WDExportManager _writeWorkoutType]_block_invoke_2
- ___38-[WDExportManager _writeAudiogramType]_block_invoke_2
- ___38-[WDExportManager _writeCategoryType:]_block_invoke_2
- ___40-[WDExportManager _writeDataForVisionRx]_block_invoke_2
- ___41-[WDExportManager _writeCorrelationType:]_block_invoke_2
- ___41-[WDExportManager _writeHRVAndTachograms]_block_invoke_2
- ___41-[WDExportManager _writePrescriptionType]_block_invoke_2
- ___42-[WDExportManager _writeActivitySummaries]_block_invoke_2
- ___58-[WDExportManager _writeWorkoutRouteForWorkout:semaphore:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e56_v36?0"HKWorkoutRouteQuery"8"NSArray"16B24"NSError"28ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e47_v32?0"HKSampleQuery"8"NSArray"16"NSError"24lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
- _objc_msgSend$activityTypeWithWorkout:
- _objc_msgSend$diveColors
- _objc_msgSend$imageWithRenderingMode:
- _objc_msgSend$isPinnedInBrowse
- _objc_msgSend$keyColors
- _objc_msgSend$nonGradientTextColor
CStrings:
+ "Attempt to create a bilateral quantity list provider with a non-bilateral quantity data group"
+ "BILATERAL_LEFT_FORMAT_%@"
+ "BILATERAL_NO_DATA"
+ "BILATERAL_RIGHT_FORMAT_%@"
+ "Error appending workout route locations to GPX: %{public}@"
+ "Failed to close archive for export data: %{public}@"
+ "Failed to fetch attachments for vision prescription: %{public}@"
+ "Failed to fetch data for vision prescription attachment %{public}@: %{public}@"
+ "Failed to generate archive for export data: %{public}@"
+ "Failed to write vision prescription attachment data to file: %{public}@"
+ "HealthRecords.healthplugin"
+ "HealthUI-Localizable-Mulberry"
+ "PRESENCE_NOT_PRESENT"
+ "PRESENCE_PRESENT"
+ "Query for activity summaries failed during export attempt: %{public}@"
+ "Query for audiogram samples failed during export attempt: %{public}@"
+ "Query for category type %{public}@ failed during export attempt: %{public}@"
+ "Query for correlation type %{public}@ failed during export attempt: %{public}@"
+ "Query for heart rate variability samples failed during export attempt: %{public}@"
+ "Query for vision prescription samples failed during export attempt: %{public}@"
+ "Query for workout effort score samples failed during export attempt: %{public}@"
+ "Query for workout route samples failed during export attempt: %{public}@"
+ "Query for workout samples failed during export attempt: %{public}@"
+ "Unable to write health record document to file."
+ "Unable to write health record document to file: %{public}@"
+ "Unable to write vision prescription attachment data to file."
```
