## PhotosUIEdit

> `/System/Library/PrivateFrameworks/PhotosUIEdit.framework/Versions/A/PhotosUIEdit`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x55d3c
-  __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_methlist: 0x2944
+751.0.104.0.0
+  __TEXT.__text: 0x568a0
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0x2cb4
+  __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__const: 0xf70
   __TEXT.__swift5_typeref: 0x5eca
   __TEXT.__swift5_reflstr: 0x5c2

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x210
-  __TEXT.__cstring: 0x3585
+  __TEXT.__cstring: 0x33f7
   __TEXT.__oslogstring: 0x3d9e
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x64
   __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x2c
   __TEXT.__gcc_except_tab: 0x6c4
-  __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__unwind_info: 0x11b8
-  __TEXT.__eh_frame: 0x4a0
+  __TEXT.__eh_frame: 0x4c0
   __TEXT.__objc_classname: 0x63e
-  __TEXT.__objc_methname: 0xac7a
-  __TEXT.__objc_methtype: 0x1206
-  __TEXT.__objc_stubs: 0x93a0
-  __DATA_CONST.__got: 0xbd0
-  __DATA_CONST.__const: 0x610
+  __TEXT.__objc_methname: 0xaff0
+  __TEXT.__objc_methtype: 0x1232
+  __TEXT.__objc_stubs: 0x95a0
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29a8
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_selrefs: 0x2ac8
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0xde8
+  __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x2648
-  __AUTH_CONST.__cfstring: 0x2be0
-  __AUTH_CONST.__objc_const: 0x62a8
+  __AUTH_CONST.__cfstring: 0x2dc0
+  __AUTH_CONST.__objc_const: 0x5ec8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x1470
   __AUTH.__data: 0x3c8
-  __DATA.__objc_ivar: 0x358
-  __DATA.__data: 0xd78
+  __DATA.__objc_ivar: 0x370
+  __DATA.__data: 0xd28
   __DATA.__bss: 0xb30
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosUIFoundation.framework/Versions/A/PhotosUIFoundation
+  - /System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/Versions/A/SensitiveContentAnalysisML
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 801941BB-AD71-38DF-BBFA-73B4878308EB
-  Functions: 1801
-  Symbols:   4138
-  CStrings:  3076
+  UUID: F9AECE8E-2913-338F-82FB-73EF69C11561
+  Functions: 1838
+  Symbols:   4206
+  CStrings:  3120
 
Symbols:
+ +[PEAdjustmentAperture _error:asset:description:]
+ +[PEAdjustmentDepth _error:asset:description:]
+ +[PEAutoEnhanceActionHelper applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:enabled:completion:]
+ -[PEAdjustmentAutoEnhance enabled]
+ -[PEAdjustmentAutoEnhance initWithEnabled:]
+ -[PEAdjustmentAutoEnhance setEnabled:]
+ -[PEAdjustmentPresetManager autoEnhanceAssets:enabled:async:progress:completion:]
+ -[PEAutoEnhanceAction enabled]
+ -[PEAutoEnhanceAction setEnabled:]
+ -[PEEditSessionEventBuilder cumulativePixelsOfConsecutiveInpaints]
+ -[PEEditSessionEventBuilder highestEncounteredThermalStateInCleanup]
+ -[PEEditSessionEventBuilder numberOfConsecutiveInpaints]
+ -[PEEditSessionEventBuilder setCumulativePixelsOfConsecutiveInpaints:]
+ -[PEEditSessionEventBuilder setHighestEncounteredThermalStateInCleanup:]
+ -[PEEditSessionEventBuilder setNumberOfConsecutiveInpaints:]
+ -[PEEditSessionEventBuilder setTimeSpentInEachTab:]
+ -[PEEditSessionEventBuilder timeSpentInEachTab]
+ GCC_except_table1071
+ GCC_except_table599
+ GCC_except_table741
+ GCC_except_table753
+ GCC_except_table765
+ GCC_except_table817
+ GCC_except_table824
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table846
+ GCC_except_table858
+ GCC_except_table966
+ OBJC_IVAR_$_PEAdjustmentAutoEnhance._enabled
+ OBJC_IVAR_$_PEAutoEnhanceAction._enabled
+ OBJC_IVAR_$_PEEditSessionEventBuilder._cumulativePixelsOfConsecutiveInpaints
+ OBJC_IVAR_$_PEEditSessionEventBuilder._highestEncounteredThermalStateInCleanup
+ OBJC_IVAR_$_PEEditSessionEventBuilder._numberOfConsecutiveInpaints
+ OBJC_IVAR_$_PEEditSessionEventBuilder._timeSpentInEachTab
+ _OBJC_CLASS_$_PICleanupAvailability
+ _OBJC_CLASS_$_PIGlobalSettings
+ _OBJC_CLASS_$_PIModelCatalog
+ _OBJC_CLASS_$_SCMLHandler
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _PEAdjustmentApertureMediaTypeErrorKey
+ _PEAdjustmentDepthMediaTypeErrorKey
+ _PEAdjustmentFilterMediaTypeErrorKey
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.308
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.310
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.314
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.319
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.323
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.327
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.331
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.334
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke_2.312
+ __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke_2.329
+ __120-[PEAdjustmentDepth applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.44
+ __121-[PEAdjustmentFilter applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.12
+ __123-[PEAdjustmentAperture applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.44
+ __126-[PEAdjustmentAutoEnhance applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.6
+ __167-[PECleanupSegmentAnalyzer analyzeStrokeMaskIntersections:inpaintMaskContext:compositionController:geometry:imageToScreenSpaceScale:userSettings:faceRects:completion:]_block_invoke.72
+ __52+[PEAdjustmentPreset sanitizeCompositionController:]_block_invoke.238
+ __53-[PEPlaybackRateAction applyToLoadResult:completion:]_block_invoke.509
+ __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.343
+ __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.348
+ __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.351
+ __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.353
+ __82-[PESmartPasteablePreset _loadResourcesForSourceAssetWithPhotoLibrary:completion:]_block_invoke.399
+ __83-[PESmartPasteablePreset applyToCompositionController:asset:editSource:completion:]_block_invoke.390
+ __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke.79
+ __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke.89
+ __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke_2.83
+ __Block_byref_object_copy_.2144
+ __Block_byref_object_copy_.2337
+ __Block_byref_object_copy_.2451
+ __Block_byref_object_copy_.2912
+ __Block_byref_object_dispose_.2145
+ __Block_byref_object_dispose_.2338
+ __Block_byref_object_dispose_.2452
+ __Block_byref_object_dispose_.2913
+ __OBJC_$_INSTANCE_VARIABLES_PEAdjustmentAutoEnhance
+ __OBJC_$_INSTANCE_VARIABLES_PEAutoEnhanceAction
+ __OBJC_$_PROP_LIST_PEAutoEnhanceAction
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v16?0"NUResponse"8l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ __block_literal_global.1250
+ __block_literal_global.1563
+ __block_literal_global.1792
+ __block_literal_global.2358
+ __block_literal_global.2459
+ __block_literal_global.2764
+ __block_literal_global.2908
+ __block_literal_global.319
+ __block_literal_global.433
+ __block_literal_global.535
+ __block_literal_global.655
+ __block_literal_global.737
+ __block_literal_global.82
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_PhotosUIEdit
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_PhotosUIEdit
+ _objc_msgSend$_error:asset:description:
+ _objc_msgSend$applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:enabled:completion:
+ _objc_msgSend$cleanupVersion
+ _objc_msgSend$cumulativePixelsOfConsecutiveInpaints
+ _objc_msgSend$currentModelVersion
+ _objc_msgSend$disableAutoEnhanceOnCompositionController:
+ _objc_msgSend$highestEncounteredThermalStateInCleanup
+ _objc_msgSend$inpaintModelVersion
+ _objc_msgSend$inpaintPixellationIntersectionAreaToFaceAreaThreshold
+ _objc_msgSend$inpaintPixellationIntersectionAreaToMaskAreaThreshold
+ _objc_msgSend$maskIsMostlyWithinFace:imageSize:imageOrientation:intAreaOverMaskAreaThreshold:intAreaOverFaceAreaThreshold:detectedFaces:
+ _objc_msgSend$numberOfConsecutiveInpaints
+ _objc_msgSend$options
+ _objc_msgSend$refinementModelVersion
+ _objc_msgSend$segmentationModelVersion
+ _objc_msgSend$shared
+ _objc_msgSend$status
+ _objc_msgSend$timeSpentInEachTab
+ _objc_msgSend$unsignedIntValue
- +[PEAdjustmentAperture _error:description:]
- +[PEAdjustmentDepth _error:description:]
- +[PEAutoEnhanceActionHelper applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:completion:]
- -[PEAdjustmentPresetManager autoEnhanceAssets:async:progress:completion:]
- GCC_except_table1057
- GCC_except_table597
- GCC_except_table735
- GCC_except_table747
- GCC_except_table759
- GCC_except_table811
- GCC_except_table818
- GCC_except_table821
- GCC_except_table825
- GCC_except_table840
- GCC_except_table852
- GCC_except_table960
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.194
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.196
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.200
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.205
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.209
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.213
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.217
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke.220
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke_2.198
- __100-[PEPasteablePreset applyToCompositionController:asset:editSource:invalidAdjustmentKeys:completion:]_block_invoke_2.215
- __120-[PEAdjustmentDepth applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.41
- __121-[PEAdjustmentFilter applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.7
- __123-[PEAdjustmentAperture applyToCompositionController:valuesCalculator:asset:livePortraitBehaviorDelegate:completionHandler:]_block_invoke.41
- __167-[PECleanupSegmentAnalyzer analyzeStrokeMaskIntersections:inpaintMaskContext:compositionController:geometry:imageToScreenSpaceScale:userSettings:faceRects:completion:]_block_invoke.71
- __52+[PEAdjustmentPreset sanitizeCompositionController:]_block_invoke.124
- __53-[PEPlaybackRateAction applyToLoadResult:completion:]_block_invoke.390
- __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.229
- __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.234
- __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.237
- __64-[PEPasteablePreset _runAutoCalculatorForCompositionController:]_block_invoke.239
- __82-[PESmartPasteablePreset _loadResourcesForSourceAssetWithPhotoLibrary:completion:]_block_invoke.285
- __83-[PESmartPasteablePreset applyToCompositionController:asset:editSource:completion:]_block_invoke.276
- __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke.78
- __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke.88
- __96-[PECleanupSegmentAnalyzer _strokeAppearsToBeClosedShape:imageToScreenSpaceScale:lassoDistance:]_block_invoke_2.82
- __Block_byref_object_copy_.2160
- __Block_byref_object_copy_.2356
- __Block_byref_object_copy_.2469
- __Block_byref_object_copy_.2907
- __Block_byref_object_dispose_.2161
- __Block_byref_object_dispose_.2357
- __Block_byref_object_dispose_.2470
- __Block_byref_object_dispose_.2908
- ___block_descriptor_56_e8_32s40s48bs_e20_v16?0"NUResponse"8l
- __block_literal_global.1282
- __block_literal_global.1587
- __block_literal_global.1807
- __block_literal_global.2377
- __block_literal_global.2478
- __block_literal_global.2747
- __block_literal_global.2903
- __block_literal_global.320
- __block_literal_global.434
- __block_literal_global.587
- __block_literal_global.704
- __block_literal_global.786
- __block_literal_global.81
- _objc_msgSend$applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:completion:
- _objc_msgSend$deviceSupportsObjectRemoval
- _objc_msgSend$maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:
- _swift_bridgeObjectRelease_n
CStrings:
+ "\nC: %@"
+ "\nIN: %@"
+ "\nRE: %@"
+ "\nSA: %@"
+ "\nSE: %@"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/AutoCalculator/PEAutoAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/PELivePortraitBehaviorController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/PEResourceLoader.m"
+ "@40@0:8q16@24@32"
+ "PEAdjustmentApertureMediaTypeErrorKey"
+ "PEAdjustmentDepthMediaTypeErrorKey"
+ "PEAdjustmentFilterMediaTypeErrorKey"
+ "T@\"NSDictionary\",&,N,V_timeSpentInEachTab"
+ "Tq,N,V_cumulativePixelsOfConsecutiveInpaints"
+ "Tq,N,V_highestEncounteredThermalStateInCleanup"
+ "Tq,N,V_numberOfConsecutiveInpaints"
+ "_cumulativePixelsOfConsecutiveInpaints"
+ "_error:asset:description:"
+ "_highestEncounteredThermalStateInCleanup"
+ "_numberOfConsecutiveInpaints"
+ "_timeSpentInEachTab"
+ "applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:enabled:completion:"
+ "autoEnhanceAssets:enabled:async:progress:completion:"
+ "cleanupVersion"
+ "cleanup_consecutive_inpaints"
+ "cleanup_cumulative_consecutive_inpaint_kpixels"
+ "cleanup_highest_thermal_state"
+ "cumulativePixelsOfConsecutiveInpaints"
+ "currentModelVersion"
+ "highestEncounteredThermalStateInCleanup"
+ "init()"
+ "inpaintModelVersion"
+ "inpaintPixellationIntersectionAreaToFaceAreaThreshold"
+ "inpaintPixellationIntersectionAreaToMaskAreaThreshold"
+ "inpaint_redacted_count"
+ "inpaint_retouch_brush_face_count"
+ "inpaint_retouch_brush_general_count"
+ "inpaint_retouch_clone_count"
+ "maskIsMostlyWithinFace:imageSize:imageOrientation:intAreaOverMaskAreaThreshold:intAreaOverFaceAreaThreshold:detectedFaces:"
+ "numberOfConsecutiveInpaints"
+ "options"
+ "refinementModelVersion"
+ "segmentationModelVersion"
+ "setCumulativePixelsOfConsecutiveInpaints:"
+ "setHighestEncounteredThermalStateInCleanup:"
+ "setNumberOfConsecutiveInpaints:"
+ "setTimeSpentInEachTab:"
+ "shared"
+ "status"
+ "timeSpentInEachTab"
+ "time_in_tool_%d"
+ "unsignedIntValue"
+ "v44@0:8@16B24B28B32@?36"
+ "v48@0:8@16B24B28@32@?40"
- "%ld"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/AutoCalculator/PEAutoAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/PELivePortraitBehaviorController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_UI/Projects/PhotosUIEdit/PhotosUIEdit/PEResourceLoader.m"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "applyAutoEnhance:replacesAffectedAdjustments:useCompositionIntensity:completion:"
- "autoEnhanceAssets:async:progress:completion:"
- "deviceSupportsObjectRemoval"
- "invalid Collection: less than 'count' elements in collection"
- "maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:"
- "v40@0:8@16B24B28@?32"

```
