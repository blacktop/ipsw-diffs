## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0x86de4
-  __TEXT.__auth_stubs: 0x760
+664.40.15.122.3
+  __TEXT.__text: 0x87130
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x1dbc
   __TEXT.__const: 0x6bec
-  __TEXT.__gcc_except_tab: 0x4ea4
+  __TEXT.__gcc_except_tab: 0x4ea8
   __TEXT.__cstring: 0x8037
   __TEXT.__dlopen_cstrs: 0xf0
   __TEXT.__oslogstring: 0xb083
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x454
   __TEXT.__objc_methname: 0x4bad
   __TEXT.__objc_methtype: 0xc8e4
   __TEXT.__objc_stubs: 0x2c80
   __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH_CONST.__const: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__const: 0x5d8
   __AUTH_CONST.__cfstring: 0x2960
   __AUTH_CONST.__objc_const: 0x49d8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x450
   __DATA.__data: 0x1070
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x78
   __DATA.__common: 0x400
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x15c
-  __DATA_DIRTY.__bss: 0x748
+  __DATA_DIRTY.__bss: 0x758
   __DATA_DIRTY.__common: 0x268
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E074D94D-F872-3CAC-AC25-E0D333217CDA
-  Functions: 1008
-  Symbols:   3565
+  UUID: 4E32BCCC-5202-3A19-8C5B-4B4DE8B678FB
+  Functions: 1038
+  Symbols:   3662
   CStrings:  3067
 
Symbols:
+ +[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:].cold.1
+ +[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:].cold.1
+ +[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:].cold.1
+ +[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.3
+ +[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:].cold.3
+ -[LTMExtractMetadataV1 init].cold.1
+ -[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:].cold.1
+ -[LTMExtractMetadataV2 init].cold.1
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.3
+ __ZN11LTMDriverV19LTMDriver24computeFaceWeightForToneEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput.cold.1
+ __ZN11LTMDriverV29LTMDriver17computeFaceWeightEPK7sBTRectP16sLtmComputeInputPK11sCIspFDRectiPfPKif.cold.1
+ __ZN11LTMDriverV29LTMDriver27computeFaceWeightForToneHFFEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput.cold.1
+ __ZN12LTMComputeV110LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput.cold.1
+ __ZN12LTMComputeV210LTMCompute18generateSpatialLTCEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput.cold.1
+ __ZZ28-[LTMExtractMetadataV1 init]E9onceToken
+ __ZZ28-[LTMExtractMetadataV2 init]E9onceToken
+ __ZZ62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]E9onceToken
+ __ZZ73+[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:]E9onceToken
+ __ZZ90+[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]E9onceToken
+ __ZZ90+[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]E9onceToken
+ __ZZN11LTMDriverV19LTMDriver24computeFaceWeightForToneEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInputE9onceToken
+ __ZZN11LTMDriverV29LTMDriver17computeFaceWeightEPK7sBTRectP16sLtmComputeInputPK11sCIspFDRectiPfPKifE9onceToken
+ __ZZN11LTMDriverV29LTMDriver27computeFaceWeightForToneHFFEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInputE9onceToken
+ __ZZN12LTMComputeV110LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutputE9onceToken
+ __ZZN12LTMComputeV210LTMCompute18generateSpatialLTCEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutputE9onceToken
+ ___107+[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:]_block_invoke
+ ___127-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]_block_invoke
+ ___28-[LTMExtractMetadataV1 init]_block_invoke
+ ___28-[LTMExtractMetadataV2 init]_block_invoke
+ ___62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]_block_invoke.30
+ ___73+[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:]_block_invoke
+ ___83+[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:]_block_invoke
+ ___90+[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]_block_invoke
+ ___90+[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]_block_invoke
+ ____ZN11LTMDriverV19LTMDriver24computeFaceWeightForToneEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput_block_invoke
+ ____ZN11LTMDriverV29LTMDriver17computeFaceWeightEPK7sBTRectP16sLtmComputeInputPK11sCIspFDRectiPfPKif_block_invoke
+ ____ZN11LTMDriverV29LTMDriver27computeFaceWeightForToneHFFEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput_block_invoke
+ ____ZN12LTMComputeV110LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput_block_invoke
+ ____ZN12LTMComputeV210LTMCompute18generateSpatialLTCEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp
+ ___block_descriptor_tmp.1
+ ___block_literal_global.29
+ ___block_literal_global.3
+ ___block_literal_global.33
+ ___block_literal_global.42
+ ___block_literal_global.46
+ ___block_literal_global.66
+ ___block_literal_global.7
+ ___useLowerLocalHistogramThreshold_block_invoke
+ __addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:.onceToken
+ __addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:.onceToken
+ _computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:.onceToken
+ _dispatch_once
+ _useLowerLocalHistogramThreshold.cold.2
+ _useLowerLocalHistogramThreshold.onceToken

```
