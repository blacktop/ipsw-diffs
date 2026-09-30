## Visage

> `/System/Library/PrivateFrameworks/Visage.framework/Visage`

```diff

-279.0.11.0.0
-  __TEXT.__text: 0x9c534
-  __TEXT.__objc_methlist: 0x4584
-  __TEXT.__const: 0x34d0
-  __TEXT.__gcc_except_tab: 0xf3d0
-  __TEXT.__cstring: 0x5548
-  __TEXT.__oslogstring: 0x5dff
-  __TEXT.__unwind_info: 0x3790
+279.0.13.0.0
+  __TEXT.__text: 0x9d8cc
+  __TEXT.__objc_methlist: 0x461c
+  __TEXT.__const: 0x34e0
+  __TEXT.__gcc_except_tab: 0xf450
+  __TEXT.__cstring: 0x565c
+  __TEXT.__oslogstring: 0x6451
+  __TEXT.__unwind_info: 0x37e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x2740
+  __DATA_CONST.__objc_selrefs: 0x27b0
   __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0xf8
+  __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x7b8
   __AUTH_CONST.__const: 0x8e8
-  __AUTH_CONST.__cfstring: 0x4700
-  __AUTH_CONST.__objc_const: 0xa1b0
+  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__objc_const: 0xa2e8
   __AUTH_CONST.__weak_auth_got: 0x100
   __AUTH_CONST.__objc_floatobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1f40
-  __DATA.__objc_ivar: 0x73c
+  __DATA.__objc_ivar: 0x758
   __DATA.__data: 0x520
   __DATA.__common: 0x8
-  __DATA.__bss: 0x280
+  __DATA.__bss: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3070
-  Symbols:   6106
-  CStrings:  1393
+  Functions: 3090
+  Symbols:   6144
+  CStrings:  1437
 
Symbols:
+ +[VGHRTFAssetManager getAssetForEnrollmentMode:error:]
+ -[VGHRTFEarPCACaptureProcessor initWithDebugDataPath:withModelsRootPath:useDepth:rectifyColor:]
+ -[VGHRTFFaceCaptureProcessor initWithDebugDataPath:useDepth:rectifyColor:]
+ -[VGHRTFSession initWithConfig:applyDefaults:error:]
+ -[VGHRTFSession setupWithConfig:applyDefaults:error:]
+ -[VGHRTFSessionConfig enrollmentMode]
+ -[VGHRTFSessionConfig modelSource]
+ -[VGHRTFSessionConfig rectifyRGBOnlyColor]
+ -[VGHRTFSessionConfig resolveModelSource]
+ -[VGHRTFSessionConfig setEnrollmentMode:]
+ -[VGHRTFSessionConfig setModelSource:]
+ -[VGHRTFSessionConfig setRectifyRGBOnlyColor:]
+ -[VGHRTFSessionConfig setUseFrameworkResourcePath:]
+ -[VGHRTFSessionConfig setUseLocalModels:]
+ -[VGHRTFSessionConfig shouldRectifyColor]
+ -[VGHRTFSessionConfig useFrameworkResourcePath]
+ -[VGHRTFSessionConfig useLocalModels]
+ GCC_except_table162
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table192
+ OBJC_IVAR_$_VGMLHRTFEncoderModel._useDepth
+ _OBJC_IVAR_$_VGHRTFEarPCACaptureProcessor._rectifyColor
+ _OBJC_IVAR_$_VGHRTFFaceCaptureProcessor._rectifyColor
+ _OBJC_IVAR_$_VGHRTFSessionConfig._enrollmentMode
+ _OBJC_IVAR_$_VGHRTFSessionConfig._modelSource
+ _OBJC_IVAR_$_VGHRTFSessionConfig._rectifyRGBOnlyColor
+ _OBJC_IVAR_$_VGHRTFSessionConfig._useFrameworkResourcePath
+ _OBJC_IVAR_$_VGHRTFSessionConfig._useLocalModels
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_INSTANCE_VARIABLES_VGMLHRTFEncoderModel
+ __ZL28VGLogHRTFEnrollmentModeUtilsv
+ __ZN2vg4hrtf12EncoderModel6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EEb
+ __ZN2vg4hrtf12HRTFPrepDataD1Ev
+ __ZN2vg4hrtf12_GLOBAL__N_116kModeDescriptorsE
+ __ZN2vg4hrtf13HRTFModelImplC1ERKNS0_18HRTFModelImplInputEb
+ __ZN2vg4hrtf13HRTFModelImplC2ERKNS0_18HRTFModelImplInputEb
+ __ZN2vg4hrtf15getAssetForModeE20VGHRTFEnrollmentModeRNS_6shared15NSErrorCWrapperE
+ __ZN2vg4hrtf16EncoderModelImpl4initERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EEb
+ __ZN2vg4hrtf18modelSetDescriptorE20VGHRTFEnrollmentMode
+ __ZN2vg4hrtf20EncoderModelEspresso6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EEb
+ __ZN2vg4hrtf21preprocessCaptureDataERKNSt3__16vectorINS0_12FrameROIDataENS1_9allocatorIS3_EEEEmmb
+ __ZN2vg4hrtf22checkAttributesForModeE20VGHRTFEnrollmentModeP12NSDictionary
+ __ZN2vg4hrtf24EncoderModelEspressoImpl4initERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EEb
+ __ZN2vg4hrtf24preprocessEarCaptureDataERKNSt3__16vectorINS0_12EarFrameDataENS1_9allocatorIS3_EEEEmmbb
+ __ZN2vg4hrtf25preprocessFaceCaptureDataERKNSt3__16vectorINS0_13FaceFrameDataENS1_9allocatorIS3_EEEEmmb
+ __ZN2vg4hrtf30enrollmentModeApplyingDefaultsE20VGHRTFEnrollmentMode
+ __ZN2vg4hrtf9HRTFModel6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEb
+ __ZN2vg4hrtf9HRTFModelC1ERKNS0_18HRTFModelImplInputEb
+ __ZN2vg4hrtf9HRTFModelC2ERKNS0_18HRTFModelImplInputEb
+ __ZNSt3__123__optional_storage_baseIN2vg4hrtf13RectifiedDataELb0EE13__assign_fromB9fqe220106INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__18optionalIN2vg4hrtf13RectifiedDataEEaSB9fqe220106IS3_Li0EEERS4_OT_
+ __ZZL28VGLogHRTFEnrollmentModeUtilsvE6handle
+ __ZZL28VGLogHRTFEnrollmentModeUtilsvE9onceToken
+ __ZZN2vg4hrtf30enrollmentModeApplyingDefaultsE20VGHRTFEnrollmentModeE8defaults
+ __ZZN2vg4hrtf30enrollmentModeApplyingDefaultsE20VGHRTFEnrollmentModeE9onceToken
+ ____ZL28VGLogHRTFEnrollmentModeUtilsv_block_invoke
+ ____ZN2vg4hrtf15getAssetForModeE20VGHRTFEnrollmentModeRNS_6shared15NSErrorCWrapperE_block_invoke
+ ____ZN2vg4hrtf30enrollmentModeApplyingDefaultsE20VGHRTFEnrollmentMode_block_invoke
+ ____ZN2vg4hrtf6detailL12filterAssetsEP7NSArrayIP7MAAssetERKNS0_18ModelSetDescriptorE_block_invoke
+ ____ZN2vg4hrtf6detailL19filterAssetsForModeEP7NSArrayIP7MAAssetERKNS0_18ModelSetDescriptorE_block_invoke
+ ____ZN2vg4hrtf6detailL23filterAssetsWithVersionEP7NSArrayIP7MAAssetERKNS0_18ModelSetDescriptorEll_block_invoke
+ ____ZN2vg4hrtf6detailL23filterAssetsWithVersionEP7NSArrayIP7MAAssetERKNS0_18ModelSetDescriptorEll_block_invoke_2
+ ____ZN2vg4hrtf6detailL32sortByContentThenMasteredVersionEP7NSArrayIP7MAAssetE_block_invoke
+ ___block_descriptor_40_e34_B24?0"MAAsset"8"NSDictionary"16l
+ ___block_descriptor_56_e5_v8?0l
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$getAssetForEnrollmentMode:error:
+ _objc_msgSend$initWithDebugDataPath:useDepth:rectifyColor:
+ _objc_msgSend$initWithDebugDataPath:withModelsRootPath:useDepth:rectifyColor:
+ _objc_msgSend$modelSource
+ _objc_msgSend$rectifyRGBOnlyColor
+ _objc_msgSend$resolveModelSource
+ _objc_msgSend$setupWithConfig:applyDefaults:error:
+ _objc_msgSend$shouldRectifyColor
+ _objc_msgSend$useFrameworkResourcePath
+ _objc_msgSend$useLocalModels
- -[VGHRTFEarPCACaptureProcessor initWithDebugDataPath:withModelsRootPath:useDepth:]
- -[VGHRTFFaceCaptureProcessor initWithDebugDataPath:useDepth:]
- -[VGHRTFSessionConfig setUseDepth:]
- -[VGHRTFSessionConfig useDepth]
- GCC_except_table116
- GCC_except_table145
- GCC_except_table161
- GCC_except_table169
- GCC_except_table171
- GCC_except_table191
- _OBJC_IVAR_$_VGHRTFSessionConfig._useDepth
- __ZN2vg4hrtf12EncoderModel6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EE
- __ZN2vg4hrtf13HRTFModelImplC1ERKNS0_18HRTFModelImplInputE
- __ZN2vg4hrtf13HRTFModelImplC2ERKNS0_18HRTFModelImplInputE
- __ZN2vg4hrtf16EncoderModelImpl4initERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EE
- __ZN2vg4hrtf17getAssetWithErrorERNS_6shared15NSErrorCWrapperE
- __ZN2vg4hrtf20EncoderModelEspresso6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EE
- __ZN2vg4hrtf21preprocessCaptureDataERKNSt3__16vectorINS0_12FrameROIDataENS1_9allocatorIS3_EEEEmm
- __ZN2vg4hrtf22writeSelectedRGBFramesENSt3__14spanIU8__strongKP9IOSurfaceLm18446744073709551615EEENS1_17basic_string_viewIcNS1_11char_traitsIcEEEESA_
- __ZN2vg4hrtf24EncoderModelEspressoImpl4initERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEERKNS2_8optionalIS8_EE
- __ZN2vg4hrtf24preprocessEarCaptureDataERKNSt3__16vectorINS0_12EarFrameDataENS1_9allocatorIS3_EEEEmmb
- __ZN2vg4hrtf25preprocessFaceCaptureDataERKNSt3__16vectorINS0_13FaceFrameDataENS1_9allocatorIS3_EEEEmm
- __ZN2vg4hrtf9HRTFModel6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
- __ZN2vg4hrtf9HRTFModelC1ERKNS0_18HRTFModelImplInputE
- __ZN2vg4hrtf9HRTFModelC2ERKNS0_18HRTFModelImplInputE
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_2
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_3
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_4
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_5
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_6
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_7
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_8
- ___50-[VGMLHRTFEncoderModel inferCaptureData:toOutput:]_block_invoke_9
- ____ZN2vg4hrtf17getAssetWithErrorERNS_6shared15NSErrorCWrapperE_block_invoke
- ____ZN2vg4hrtf6detailL12filterAssetsEP7NSArrayIP7MAAssetE_block_invoke
- ____ZN2vg4hrtf6detailL22filterAssetsWithLatestEP7NSArrayIP7MAAssetEl_block_invoke
- ____ZN2vg4hrtf6detailL23filterAssetsWithVersionEP7NSArrayIP7MAAssetEll_block_invoke
- ___block_descriptor_32_e34_B24?0"MAAsset"8"NSDictionary"16l
- _objc_msgSend$initWithDebugDataPath:useDepth:
- _objc_msgSend$initWithDebugDataPath:withModelsRootPath:useDepth:
CStrings:
+ " Failed to compile HRTF DTF model at: %s "
+ " Failed to compile HRTF DTFBias model at: %s "
+ " Failed to compile HRTF decoder model at: %s "
+ " Failed to compile HRTF delay model at: %s "
+ " Failed to compile HRTF encoder model at: %s "
+ " Failed to create BGRA color surface for encoder input. "
+ " Failed to initialize HRTF DTF model at %s: %s "
+ " Failed to initialize HRTF DTF model at %s: unknown error "
+ " Failed to initialize HRTF DTFBias model at %s: %s "
+ " Failed to initialize HRTF DTFBias model at %s: unknown error "
+ " Failed to initialize HRTF decoder model at %s: %s "
+ " Failed to initialize HRTF decoder model at %s: unknown error "
+ " Failed to initialize HRTF delay model at %s: %s "
+ " Failed to initialize HRTF delay model at %s: unknown error "
+ " Failed to initialize HRTF encoder model at %s: %s "
+ " Failed to initialize HRTF encoder model at %s: unknown error "
+ " HRTF DTF model missing expected port: %s (model=%s) "
+ " HRTF DTFBias model missing expected port: %s (model=%s) "
+ " HRTF decoder model missing expected port: %s (model=%s) "
+ " HRTF delay model missing expected port: %s (model=%s) "
+ " HRTF encoder model missing expected port: %s (model=%s) "
+ " HRTF session requested: enrollmentMode=%@, useLocalModels=%@, rectifyRGBOnlyColor=%@ (applyDefaults=%@). "
+ " HRTF session resolved: enrollmentMode=%@, modelSource=%@. "
+ " HRTF: applying NSUserDefault debugDataRootPathHRTF "
+ " HRTF: applying NSUserDefault useFrameworkResourcePath (framework-local models) "
+ " HRTF: applying NSUserDefault writeDebugDataHRTF "
+ " HRTFModelImpl::predict useDepth=%s "
+ "%lu asset(s) at version %zu.%zu, but none for enrollment mode %@ (different model set)"
+ "%s E5RT create threw; will fall back to Espresso."
+ "%s E5RT predict threw; falling back to Espresso."
+ "%s Espresso predict threw."
+ "Applying NSUserDefault %@=%@ (overrides requested mode)."
+ "DepthLocal"
+ "DepthMobileAsset"
+ "Enrollment mode %ld is out of range; using RGBDepth."
+ "GetAssetForMode"
+ "HRTFData"
+ "HRTFEnrollmentModeUtils"
+ "HRTFRGBOnlyData"
+ "HRTFRGBOnlyModels"
+ "Invalid hrtfMACompatContentVersion; expected CompatibilityVersion.ContentVersion (e.g. 1.3)"
+ "Minimum 3 ear frames per side required."
+ "No %@ asset at version %zu.%zu"
+ "No %@ asset found (compatibility version %zu)"
+ "RGBDepth enrollment requires captureData.depthBuffer and .depthCalibrationData (both non-nil)."
+ "RGBOnlyLocal"
+ "RGBOnlyMobileAsset"
+ "Resolving HRTF asset for enrollment mode %@."
+ "Selected %@ asset {%@, %@} version %zu.%zu.%zu (compatibility.content.mastered)"
+ "Selecting %@ asset at version %zu.%zu ..."
+ "Selecting latest %@ asset (compatibility version %zu) ..."
+ "Unknown"
+ "Unknown HRTF model source."
+ "Unrecognized NSUserDefault %@=%@; ignoring it."
+ "Using %@ asset version %zu.%zu from hrtfMACompatContentVersion"
+ "VisageHRTFRGBOnlyModel"
+ "hrtfEnrollmentMode"
+ "rgbDepth"
+ "rgbOnly"
+ "useFrameworkResourcePath"
- " Failed to compile DTFBiasModel: %s "
- " HRTF post-processing skipped: useDepth=NO (frame selection only). "
- " Unable to write selected frame %.*s_%zu. "
- "/selected_"
- "Filtering assets with version: %zu.%zu (compatibility.content) ..."
- "Filtering assets with version: %zu.latest (compatibility.content) ..."
- "GetAssetWithError"
- "Overriding default CompatibilityVersion (version: %zu) with asset version: %zu.%zu (compatibility.content)"
- "Selected asset {%@, %@} version: %zu.%zu.%zu (compatibility.content.mastered)"
- "Unable to find any compatible assets for asset type %@ with compatibility version %zu"
- "Unable to find any compatible assets for asset type %@ with version: %zu.%zu (compatibility.content)"
- "Wrong format provided for the asset version (expected: CompatibilityVersion.ContentVersion; example: 1.3)"
- "_"
- "_useVNFiltersEnrollment"
- "left_ear"
- "useLocalHRTFModels"
```
