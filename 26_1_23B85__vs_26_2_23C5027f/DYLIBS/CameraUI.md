## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4097.40.19.0.0
-  __TEXT.__text: 0x3eab00
-  __TEXT.__auth_stubs: 0x6850
-  __TEXT.__objc_methlist: 0x2fa10
-  __TEXT.__const: 0x21d24
-  __TEXT.__gcc_except_tab: 0x335c
-  __TEXT.__cstring: 0x1f437
-  __TEXT.__oslogstring: 0x16554
-  __TEXT.__dlopen_cstrs: 0x407
+4097.60.4.0.1
+  __TEXT.__text: 0x3e9e5c
+  __TEXT.__auth_stubs: 0x6880
+  __TEXT.__objc_methlist: 0x2fa30
+  __TEXT.__const: 0x21f24
+  __TEXT.__gcc_except_tab: 0x31ec
+  __TEXT.__cstring: 0x1f3a7
+  __TEXT.__oslogstring: 0x16584
+  __TEXT.__dlopen_cstrs: 0x3b9
   __TEXT.__ustring: 0x8
-  __TEXT.__constg_swiftt: 0x59e4
-  __TEXT.__swift5_typeref: 0x25d86
-  __TEXT.__swift5_reflstr: 0x5d5a
-  __TEXT.__swift5_fieldmd: 0x4f00
+  __TEXT.__constg_swiftt: 0x5a38
+  __TEXT.__swift5_typeref: 0x25df6
+  __TEXT.__swift5_reflstr: 0x5dda
+  __TEXT.__swift5_fieldmd: 0x4f90
   __TEXT.__swift5_builtin: 0x3fc
   __TEXT.__swift5_assocty: 0x15a0
-  __TEXT.__swift5_proto: 0xa24
-  __TEXT.__swift5_types: 0x530
+  __TEXT.__swift5_proto: 0xa3c
+  __TEXT.__swift5_types: 0x53c
   __TEXT.__swift5_capture: 0x2820
   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xeb60
-  __TEXT.__eh_frame: 0x2b98
+  __TEXT.__unwind_info: 0xeb70
+  __TEXT.__eh_frame: 0x2bc8
   __TEXT.__objc_classname: 0x5671
-  __TEXT.__objc_methname: 0x9e77a
+  __TEXT.__objc_methname: 0x9e7e9
   __TEXT.__objc_methtype: 0x10883
-  __TEXT.__objc_stubs: 0x5a8c0
-  __DATA_CONST.__got: 0x4418
-  __DATA_CONST.__const: 0x7e40
+  __TEXT.__objc_stubs: 0x5a8e0
+  __DATA_CONST.__got: 0x4428
+  __DATA_CONST.__const: 0x7e08
   __DATA_CONST.__objc_classlist: 0x1220
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x7b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19ee0
+  __DATA_CONST.__objc_selrefs: 0x19ee8
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1048
-  __AUTH_CONST.__auth_got: 0x3438
-  __AUTH_CONST.__const: 0xdbf8
-  __AUTH_CONST.__cfstring: 0x16520
-  __AUTH_CONST.__objc_const: 0x50508
+  __AUTH_CONST.__auth_got: 0x3450
+  __AUTH_CONST.__const: 0xdd90
+  __AUTH_CONST.__cfstring: 0x167e0
+  __AUTH_CONST.__objc_const: 0x50538
   __AUTH_CONST.__objc_intobj: 0x1860
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x5b40
-  __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0x3c50
-  __DATA.__data: 0xb158
+  __AUTH.__data: 0xef8
+  __DATA.__objc_ivar: 0x3c54
+  __DATA.__data: 0xb180
+  __DATA.__bss: 0x10ed0
   __DATA.__common: 0x170
-  __DATA.__bss: 0x10c70
   __DATA_DIRTY.__objc_data: 0x7710
-  __DATA_DIRTY.__data: 0x3428
+  __DATA_DIRTY.__data: 0x3438
   __DATA_DIRTY.__bss: 0x3fc0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 71233417-9FA8-31DE-AEA7-6CC29528EAE2
-  Functions: 25951
-  Symbols:   60186
-  CStrings:  31464
+  UUID: B164142E-41CE-3FBB-81CA-F5745899B3E1
+  Functions: 25955
+  Symbols:   60089
+  CStrings:  31490
 
Symbols:
+ -[CAMAnalyticsPreferencesEvent _lockScreenSwipeForCameraEnabled]
+ -[CAMCaptureCapabilities maximumRecordedDurationSeconds]
+ _OBJC_IVAR_$_CAMCaptureCapabilities._maximumRecordedDurationSeconds
+ _UIInterfaceOrientationIsLandscape
+ ___swift_memcpy49_8
+ ___swift_project_boxed_opaque_existential_2
+ _associated conformance 8CameraUI13CaptureErrorsO10Foundation13CustomNSErrorAAs5Error
+ _associated conformance 8CameraUI14AppIntentErrorV0E4KindOSHAASQ
+ _associated conformance 8CameraUI14AppIntentErrorV10Foundation13CustomNSErrorAAs0E0
+ _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.77
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI012StartCaptureC0VGAA0dE0HPyHC.79
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI015OpenCaptureModeC0VGAA0dE0HPyHC.76
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI06Changef6DeviceC0VGAA0dE0HPyHC.78
+ _objc_msgSend$_lockScreenSwipeForCameraEnabled
+ _objc_msgSend$maximumRecordedDurationSeconds
+ _swift_willThrowTypedImpl
+ _symbolic _____ 7SwiftUI5AngleV
+ _symbolic _____ 8CameraUI14AppIntentErrorV
+ _symbolic _____ 8CameraUI14AppIntentErrorV0E4KindO
+ _symbolic _____ 8CameraUI18ControlOrientationV
+ _symbolic ___________p 10Foundation40CustomLocalizedStringResourceConvertibleP AA0B7NSErrorP
+ _symbolic _____y_____ySaySi6offset_Say_____G7elementtGSi_____y__________y_____GGSgSgGG 7SwiftUI6HStackV AA7ForEachV 06CameraB013ChromeElementO AA15ModifiedContentV AF0G6TopBarV15ExpandableGroup33_BBF3D7885B060A508D38D6C2DC0D27C8LLV AA21_TraitWritingModifierV AA010TransitionY3KeyV
+ _type_layout_string 8CameraUI14AppIntentErrorV
+ _type_layout_string 8CameraUI18ControlOrientationV
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.1
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.10
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.11
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.2
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.3
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.4
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.5
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.6
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.7
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.8
- -[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.9
- -[CAMBurstImageFaceAnalysisContext setupFaceDetector].cold.1
- -[CAMBurstImageFaceAnalysisContext setupFaceDetector].cold.2
- GCC_except_table45
- GCC_except_table46
- GCC_except_table47
- _FaceCoreLibrary
- _FaceCoreLibraryCore
- _FaceCoreLibraryCore.frameworkLibrary
- __Block_object_assign
- ___FaceCoreLibraryCore_block_invoke
- ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
- ___getFCRDetectionParamDetectionRegionSymbolLoc_block_invoke
- ___getFCRDetectionParamInitialAngleSymbolLoc_block_invoke
- ___getFCRExtractionParamEnhancedEyesAndMouthLocalizationSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractBlinkSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractFaceprintSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractLandmarkPointsSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractSmileSymbolLoc_block_invoke
- ___getFCRExtractionParamInitialAngleSymbolLoc_block_invoke
- ___getFCRFaceExpressionLeftEyeClosedScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionLeftEyeClosedSymbolLoc_block_invoke
- ___getFCRFaceExpressionRightEyeClosedScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionRightEyeClosedSymbolLoc_block_invoke
- ___getFCRFaceExpressionSmileScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionSmileSymbolLoc_block_invoke
- ___getFCRFastFaceDetectionParametersSymbolLoc_block_invoke
- ___getFCRSetupParamNumberOfAnglesSymbolLoc_block_invoke
- ___getFaceCoreDetectorClass_block_invoke
- ___getFaceCoreDetectorClass_block_invoke.cold.1
- ___getFaceCoreFaceClass_block_invoke
- ___getFaceCoreFaceClass_block_invoke.cold.1
- ___getFaceCoreImageClass_block_invoke
- ___getFaceCoreImageClass_block_invoke.cold.1
- _audit_stringFaceCore
- _getFCRDetectionParamDetectionRegionSymbolLoc.ptr
- _getFCRDetectionParamInitialAngleSymbolLoc.ptr
- _getFCRExtractionParamEnhancedEyesAndMouthLocalizationSymbolLoc.ptr
- _getFCRExtractionParamExtractBlinkSymbolLoc.ptr
- _getFCRExtractionParamExtractFaceprintSymbolLoc.ptr
- _getFCRExtractionParamExtractLandmarkPointsSymbolLoc.ptr
- _getFCRExtractionParamExtractSmileSymbolLoc.ptr
- _getFCRExtractionParamInitialAngleSymbolLoc.ptr
- _getFCRFaceExpressionLeftEyeClosed
- _getFCRFaceExpressionLeftEyeClosed.cold.1
- _getFCRFaceExpressionLeftEyeClosedScoreSymbolLoc.ptr
- _getFCRFaceExpressionLeftEyeClosedSymbolLoc.ptr
- _getFCRFaceExpressionRightEyeClosed
- _getFCRFaceExpressionRightEyeClosed.cold.1
- _getFCRFaceExpressionRightEyeClosedScoreSymbolLoc.ptr
- _getFCRFaceExpressionRightEyeClosedSymbolLoc.ptr
- _getFCRFaceExpressionSmile
- _getFCRFaceExpressionSmile.cold.1
- _getFCRFaceExpressionSmileScoreSymbolLoc.ptr
- _getFCRFaceExpressionSmileSymbolLoc.ptr
- _getFCRFastFaceDetectionParametersSymbolLoc.ptr
- _getFCRSetupParamNumberOfAnglesSymbolLoc.ptr
- _getFaceCoreDetectorClass.softClass
- _getFaceCoreFaceClass.softClass
- _getFaceCoreImageClass.softClass
- _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.72
- _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI012StartCaptureC0VGAA0dE0HPyHC.74
- _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI015OpenCaptureModeC0VGAA0dE0HPyHC.71
- _get_witness_table 10AppIntents22IntentParameterSummaryVy8CameraUI06Changef6DeviceC0VGAA0dE0HPyHC.73
- _objc_msgSend$isRunningInStoreDemoMode
CStrings:
+ "CAMDebugMaximumRecordedDurationSeconds"
+ "Custom max video duration set to: %{public}f"
+ "FCRDetectBlink"
+ "FCRDetectSmile"
+ "FCRDetectionRegion"
+ "FCRDetectorType"
+ "FCRDetectorTypeFastFaceDetection"
+ "FCRExtractFaceprint"
+ "FCRExtractLandmarkPoints"
+ "LockScreenSwipeGestureEnabled"
+ "SBLockScreenCameraSwipeEnabled"
+ "Tq,R,N,V_maximumRecordedDurationSeconds"
+ "_lockScreenSwipeForCameraEnabled"
+ "_maximumRecordedDurationSeconds"
+ "eye_and_mouth"
+ "initial_angle"
+ "maximumRecordedDurationSeconds"
+ "nb_angles"
- "CameraUI/UIKit+CameraUI.swift"
- "FCRDetectionParamDetectionRegion"
- "FCRDetectionParamInitialAngle"
- "FCRExtractionParamEnhancedEyesAndMouthLocalization"
- "FCRExtractionParamExtractBlink"
- "FCRExtractionParamExtractFaceprint"
- "FCRExtractionParamExtractLandmarkPoints"
- "FCRExtractionParamExtractSmile"
- "FCRExtractionParamInitialAngle"
- "FCRFastFaceDetectionParameters"
- "FCRSetupParamNumberOfAngles"
- "Unknown UIInterfaceOrientation "
- "isRunningInStoreDemoMode"
- "softlink:o:path:/System/Library/Frameworks/Vision.framework/libfaceCore.dylib"

```
