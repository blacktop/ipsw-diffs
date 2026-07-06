## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-  __TEXT.__text: 0x8a658
+  __TEXT.__text: 0x8a6fc
   __TEXT.__objc_methlist: 0x1f44
   __TEXT.__const: 0x6ab4
-  __TEXT.__gcc_except_tab: 0x5064
-  __TEXT.__cstring: 0x9434
+  __TEXT.__gcc_except_tab: 0x5090
+  __TEXT.__cstring: 0x9471
   __TEXT.__dlopen_cstrs: 0xf0
-  __TEXT.__oslogstring: 0xb949
+  __TEXT.__oslogstring: 0xb990
   __TEXT.__unwind_info: 0xc50
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x360
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x4b0
   __AUTH_CONST.__const: 0x4b8
   __AUTH_CONST.__cfstring: 0x2fa0
   __AUTH_CONST.__objc_const: 0x4c60

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x538
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x488
   __DATA.__data: 0xcb8
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x4a8
   __DATA_DIRTY.__bss: 0x7a8
   __DATA_DIRTY.__common: 0x1648

   - /usr/lib/libobjc.A.dylib
   Functions: 1361
   Symbols:   4434
-  CStrings:  2267
+  CStrings:  2270
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Functions:
~ -[HazeEstimation estimateHaze:] : 1420 -> 1440
~ -[AWBAlgorithm configWithModuleConfig:metadata:cameraInfo:awbParams:] : 6588 -> 7036
~ __ZN12LTMComputeV110LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput : 4612 -> 4604
~ __ZN12LTMComputeV210LTMCompute11interpolateEPKfS2_iS2_Pfi : 220 -> 216
~ __ZN12LTMComputeV110LTMCompute19computeRGBToneCurveEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_15sLtmFrameParamsEP17sLtmComputeOutput : 1388 -> 1384
~ __ZN12LTMComputeV110LTMCompute12makeScaleGTCEPfPKfff : 444 -> 440
~ __ZN12LTMComputeV110LTMCompute16computeLocalLumaEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsE : 552 -> 548
~ __ZN12LTMComputeV210LTMCompute11interpolateEPKfS2_iS2_Pfif : 220 -> 228
~ __ZN12LTMComputeV110LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE : 1864 -> 1860
~ __ZN12LTMComputeV110LTMCompute19calculateSceneFlareEPKfiPiffPfS4_S4_ : 1136 -> 1144
~ __ZN12LTMComputeV110LTMCompute38calculateGlobalLUTandModifySceneModelsEmPK16sLtmComputeInputPK15sLtmComputeMetaPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsEP17sLtmComputeOutput : 3320 -> 3268
~ __ZN7CAWBAFE8SetStatsEPK16_FE_3A_Stats_H15PK15_TILE_Stat_ElemPK16_AEAWB_Stat_ElemPKvS2_ : 336 -> 328
~ __ZN7CAWBAFE13TrimHistogramEPjt : 1632 -> 1600
~ __ZN7CAWBAFE19calculateRGBFromCCTEjPt : 676 -> 660
~ __ZN7CAWBAFE24SetFlashProjectionConfigEPK47sCIspCmdAppleChAWBFlashProjectionConfigSetEntry : 3936 -> 3828
~ __ZN28CDualLEDsWhitePointProjector9ParamInitEff13eFlashLEDTypePK22sPerModuleLEDCalibDataPK35sDualLEDsWhitePointProjectionConfig : 520 -> 472
~ __ZN12LTMComputeV210LTMCompute16computeLocalLumaEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsE : 572 -> 568
~ __ZN12LTMComputeV210LTMCompute30calculateHighlightSceneModelV2EPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPKNS_15sLtmFrameParamsEPfSA_SA_ : 2660 -> 2648
~ __ZN12LTMComputeV210LTMCompute38calculateGlobalLUTandModifySceneModelsEmPK16sLtmComputeInputPK15sLtmComputeMetaPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsEP17sLtmComputeOutput : 4220 -> 4208
~ __ZN12LTMComputeV210LTMCompute12allocateToneEPfS1_PKfPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPKNS_15sLtmFrameParamsES3_S3_S3_S3_S3_fffbbb : 3944 -> 3936
~ __ZN12LTMComputeV210LTMCompute12makeScaleGTCEPfPKfff : 444 -> 440
~ __ZN12LTMComputeV210LTMCompute19computeRGBToneCurveEPK24sLtmComputeInput_SOFTISPPKNS_16sLtmTuningParamsEPKNS_15sLtmFrameParamsEP17sLtmComputeOutput : 1424 -> 1436
~ __ZN12LTMComputeV210LTMCompute18generateSpatialLTCEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput : 10308 -> 10324
~ +[LTMExtractMetadataV1 extractCCMFromMetadata:toDriverInput:] : 904 -> 896
~ +[LTMExtractMetadataV2 extractCCMFromMetadata:toDriverInput:] : 904 -> 896
CStrings:
+ "<<<< AWBAlgorithm >>>> %s: Configuring SoftISP AWB, SetFile origin: %@"
+ "AWB requires a moduleConfig to configure."
+ "moduleConfig.count"

```
