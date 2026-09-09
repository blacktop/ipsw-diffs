## HDRProcessing

> `/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing`

```diff

 1.517.51.0.0
-  __TEXT.__text: 0xa8500
+  __TEXT.__text: 0xa856c
   __TEXT.__objc_methlist: 0x2548
   __TEXT.__const: 0x4c18
-  __TEXT.__gcc_except_tab: 0x25ac
+  __TEXT.__gcc_except_tab: 0x25a0
   __TEXT.__oslogstring: 0xf446
   __TEXT.__cstring: 0x85fa
-  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__unwind_info: 0x15e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
Functions:
~ -[HDRProcessor initProcessingEngine:config:] : 1560 -> 1572
~ __ZN9HDRConfig15ReadConfigEntryE11HDRConfigID : 1460 -> 1468
~ __ZN16EDRMetaData_RBSP16rpu_data_mappingEjj : 1976 -> 2020
~ __ZN16EDRMetaData_RBSP22rpu_data_mapping_paramEjjjj : 2420 -> 2436
~ __ZN16EDRMetaData_RBSP13copy_rpu_dataEP12RPU_MetaData : 2804 -> 2796
~ -[DolbyVisionDM4 applyL9:] : 596 -> 592
~ __ZL14packHCUInPlaceP13NSMutableDataPK29hcuApiHdrConfigurationUnitsV3 : 424 -> 428
~ -[MSRHDRProcessing populateMSRColorConfigStageB01_01:Enabled:Prefix:DMConfig:DMData:tcControl:hdrControl:MSRHDRContext:] : 1504 -> 1500
~ -[MSRHDRProcessing populateMSRColorConfigStageB01_02:Enabled:Prefix:DMConfig:DMData:tcControl:hdrControl:MSRHDRContext:] : 3120 -> 3108
~ -[MSRHDRProcessing updatePolynomialTables:TableSize:] : 112 -> 116
~ -[HDRBackwardDisplayManagement createMetadataTexture] : 520 -> 512
~ -[HDRBackwardDisplayManagement encodeToCommandBuffer:video:videoSrcRegion:videoDstRegion:ui:uiSrcRegion:uiDstRegion:backgroundColor:output:frameProperties:] : 6524 -> 6480
~ -[MSRHDRProcessingT2 updatePolynomialTablesForComponent:Component:TableSize:] : 112 -> 116
~ __ZN16EDRMetaData_RBSP12rpu_data_nlqEjj : 1368 -> 1340
~ __ZN16EDRMetaData_RBSP29rpu_data_el_chroma_resamplingEjj : 280 -> 276
~ __ZN16EDRMetaData_RBSP40rpu_data_chroma_resampling_filter_2D_expEjjj : 572 -> 592
~ __ZN16EDRMetaData_RBSP45rpu_data_chroma_resampling_filter_2D_exp_coefEjjjj : 272 -> 288
~ __ZN16EDRMetaData_RBSP45rpu_data_chroma_resampling_filter_1D_exp_coefEjjjj : 236 -> 244
~ __ZN16EDRMetaData_RBSP38rpu_data_spatial_resampling_filter_expEjjj : 284 -> 276
~ -[DolbyVisionComposer embeddedSetupEncoderForCommandBuffer:DMData:dmConfig:isInput422:hasThreeOutputPlane:isSdrOnDolbyOrHDR10:isHDR10OnHDR10TV:isDolbyOnHDR10TV:isHDR10OnDolby:isHDR10OnPad:isHLGOnPad:isDoviOnPad:isDoviOnLLDovi:isHDR10OnLLDovi:isHLGOnHDR10TV:isHLGOnDolbyTV:isHLGOnLLDovi:isPtvMode:orientation:isDolby84:dovi50toHDR10TVMode:isDM4:isGpuTmRefMode:] : 7128 -> 7136
~ -[DolbyVisionComposer embeddedSetupEncoderForGpuMatchMsrCommandBuffer:DMData:dmConfig:isInput422:orientation:isDolby84:dovi50toHDR10TVMode:isDM4:dpcParam:tcControl:hdrControl:isHDR10Content:isHLGContent:isDOVIContent:] : 3156 -> 3160
~ -[DolbyVisionDM4 DmProcess:Height:bufI:bufU:bufV:] : 296 -> 308
~ _SMPTE_ST_2094_50_DbgPrintMetadataItems : 584 -> 580
~ _SMPTE_ST_2094_50_EncodeSyntaxElementsToBinaryData : 912 -> 908
~ _applyAmveB2DAdaptationS_C : 136 -> 140
~ -[HistBasedToneMapping computeFrameAvgFromHistData] : 72 -> 76
~ -[HistBasedToneMapping computeFrameStdFromHistData] : 84 -> 88
~ -[MSRHDRProcessingByCapabilities updatePolynomialTablesForComponent:Component:TableSize:] : 124 -> 128
~ -[HDRMetadataManager multiviewAddDoViHDMIMetadata:width:height:priority:] : 2220 -> 2212
~ -[HDRMetadataManager multiviewGenerateDoViHDMIMetadata:] : 5392 -> 5432
~ _hdrpMetadataReconstruction : 5744 -> 5788
~ -[DolbyVisionMR metadataReconstruction:dmData:maxDisplayBrightnessNits:targetMaxNits:targetMinNits:displayPrimaries:baseMax:baseMin:videoFullRangeFlag:colourPrimaries:matrixCoeffs:numFrames:] : 6600 -> 6616
~ _Dm4Tc : 3876 -> 3844
```
