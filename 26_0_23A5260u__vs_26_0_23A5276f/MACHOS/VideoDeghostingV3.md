## VideoDeghostingV3

> `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/VideoDeghostingV3`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x2e6cc
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x2920
-  __TEXT.__objc_methlist: 0x1bdc
-  __TEXT.__const: 0xec0
-  __TEXT.__objc_methname: 0x6baa
-  __TEXT.__oslogstring: 0x1923
-  __TEXT.__cstring: 0x5354
-  __TEXT.__objc_classname: 0x285
-  __TEXT.__objc_methtype: 0x4818
+655.0.0.122.4
+  __TEXT.__text: 0x2f064
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0x29a0
+  __TEXT.__objc_methlist: 0x1c24
+  __TEXT.__const: 0xec8
+  __TEXT.__objc_methname: 0x6e42
+  __TEXT.__oslogstring: 0x1972
+  __TEXT.__cstring: 0x5508
+  __TEXT.__objc_classname: 0x286
+  __TEXT.__objc_methtype: 0x49e5
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__unwind_info: 0x7a8
-  __DATA_CONST.__auth_got: 0x550
+  __TEXT.__unwind_info: 0x7b8
+  __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2e0
-  __DATA_CONST.__cfstring: 0x1060
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x1180
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x4380
-  __DATA.__objc_selrefs: 0xf68
-  __DATA.__objc_ivar: 0x570
+  __DATA_CONST.__objc_doubleobj: 0x20
+  __DATA.__objc_const: 0x4510
+  __DATA.__objc_selrefs: 0xf98
+  __DATA.__objc_ivar: 0x598
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x2c8
-  __DATA.__common: 0x40
+  __DATA.__common: 0x50
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2910ECAF-53F7-3EC2-AC15-B1E0BC2D4817
-  Functions: 839
-  Symbols:   2054
-  CStrings:  2076
+  UUID: DADF5FAB-B14C-3854-8F87-9763A574EFE0
+  Functions: 836
+  Symbols:   2073
+  CStrings:  2117
 
Symbols:
+ -[CMIVideoDeghostingV3 isHWAccelerated]
+ -[CMIVideoDeghostingV3 statistics]
+ -[GGMMetalToolBox _compileShaders].cold.44
+ -[GGMMetalToolBox _compileShaders].cold.45
+ -[GGMMetalToolBox encodeCollectClusterOpticalCenterEstStats:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeUpdateEstOpticalCenterOffset:meta:]
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:]
+ -[VideoDeghostingDetectionV3 getFutureRoisFutureOpticalCenter:futureLightSourceMaskTotalArea:currFrameMetaContainer:futureFrameMetaBuf:]
+ -[VideoDeghostingDetectionV3 getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:lightSourceMaskTotalArea:]
+ -[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:]
+ GCC_except_table30
+ OBJC_IVAR_$_CMIVideoDeghostingV3._accumulatedStatistics
+ OBJC_IVAR_$_CMIVideoDeghostingV3._detectionNotGatedFrameCount
+ OBJC_IVAR_$_CMIVideoDeghostingV3._imageDimensions
+ OBJC_IVAR_$_CMIVideoDeghostingV3._repairedFrameCount
+ OBJC_IVAR_$_GGMMetalToolBox._collectOpticalCenterEstStats
+ OBJC_IVAR_$_GGMMetalToolBox._updateEstOpticalCenterOffset
+ OBJC_IVAR_$_VideoDeghostingDetectionV3._estOpticalCenterOffset
+ OBJC_IVAR_$_VideoDeghostingDetectionV3._futureIspBaseOpticalCenter
+ OBJC_IVAR_$_VideoDeghostingDetectionV3._opticalCenterEstConf
+ OBJC_IVAR_$_VideoDeghostingDetectionV3._prevOpticalCenterEstConf
+ _FigNote_AllowInternalDefaultLogs
+ ___210-[VideoDeghostingDetectionV3 getProbMapsTarget:rawProbMap:probMap:rawRefinedProbMap:refinedProbMap:refinedReflLsMap:reflLsMap4TrackingRef:probMapRepairRef0:probMapRepairRef1:metaBuf:metaBufArray:commandBuffer:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
+ _kCMIVideoDeghostingDetectionResult_IsDetectionGated
+ _kVGGMDetectionResult_AverageGhostArea
+ _kVGGMDetectionResult_AverageGhostCount
+ _kVGGMDetectionResult_OpticalCenterEstConfidence
+ _kVGGMDetectionResult_OpticalCenterOffsetMag
+ _kVGGMDetectionResult_OpticalCenterOffsetX
+ _kVGGMDetectionResult_OpticalCenterOffsetY
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$encodeCollectClusterOpticalCenterEstStats:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeUpdateEstOpticalCenterOffset:meta:
+ _objc_msgSend$getFutureRoisFutureOpticalCenter:futureLightSourceMaskTotalArea:currFrameMetaContainer:futureFrameMetaBuf:
+ _objc_msgSend$getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:lightSourceMaskTotalArea:
+ _objc_msgSend$maxTotalThreadsPerThreadgroup
+ _objc_msgSend$prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:
+ _objc_msgSend$updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:
- -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:frameDim:]
- -[VideoDeghostingDetectionV3 getFutureRoisFutureOpticalCenter:currFrameMetaContainer:futureFrameMetaBuf:]
- -[VideoDeghostingDetectionV3 getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:]
- -[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:doLite:]
- -[VideoMitigation mitigate:info:futureFrames:inputTexture:].cold.2
- -[VideoMitigation mitigate:info:futureFrames:inputTexture:].cold.3
- -[VideoMitigation mitigate:info:futureFrames:inputTexture:].cold.4
- -[VideoMitigation mitigate:info:futureFrames:inputTexture:].cold.5
- GCC_except_table29
- _objc_msgSend$getFutureRoisFutureOpticalCenter:currFrameMetaContainer:futureFrameMetaBuf:
- _objc_msgSend$getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:
- _objc_msgSend$prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:doLite:
- _objc_msgSend$updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:frameDim:
- fetchOneFrameFromSampleBuffer.cold.1
- fetchOneFrameFromSampleBuffer.cold.2
- fetchOneFrameFromSampleBuffer.cold.3
- fetchOneFrameFromSampleBuffer.cold.4
- fetchOneFrameFromSampleBuffer.cold.5
- fetchOneFrameFromSampleBuffer.cold.6
CStrings:
+ "-[CMIVideoDeghostingV3 statistics]"
+ "-[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:]"
+ "-[VideoDeghostingDetectionV3 getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:lightSourceMaskTotalArea:]"
+ "-[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:]"
+ "<<<< CMIVideoDeghostingV3 >>>> %s: Statistics: opticalCenterMag = %f, opticalCenterOffsetX = %f, opticalCenterOffsetY = %f, opticalCenterEstConfidence = %f, averageGhostCount = %f, averageGhostArea = %f"
+ "@24@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}16"
+ "@48@0:8^{__CVBuffer=}1624^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}32B40f44"
+ "AverageGhostArea"
+ "AverageGhostCount"
+ "IsDetectionGated"
+ "OpticalCenterEstConfidence "
+ "OpticalCenterOffsetMag"
+ "OpticalCenterOffsetX"
+ "OpticalCenterOffsetY"
+ "TB,R,N"
+ "T^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f},V_metaContainer"
+ "T{CMIVideoDeghostingStatistics=dddddd},R,N"
+ "VideoDeghostingV3::collectOpticalCenterEstStats"
+ "VideoDeghostingV3::updateEstOpticalCenterOffset"
+ "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}"
+ "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}16@0:8"
+ "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}68@0:8@16@24B323644f5256f64"
+ "_accumulatedStatistics"
+ "_collectOpticalCenterEstStats"
+ "_collectOpticalCenterEstStats is NULL"
+ "_detectionNotGatedFrameCount"
+ "_estOpticalCenterOffset"
+ "_futureIspBaseOpticalCenter"
+ "_opticalCenterEstConf"
+ "_prevOpticalCenterEstConf"
+ "_repairedFrameCount"
+ "_updateEstOpticalCenterOffset"
+ "_updateEstOpticalCenterOffset is NULL"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "encodeCollectClusterOpticalCenterEstStats:clusterMetaBuf:metaBuf:"
+ "encodeUpdateEstOpticalCenterOffset:meta:"
+ "f32@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}16i24i28"
+ "f88@0:8{?=ffffffff}16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}48^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}56^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}64^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}72B80f84"
+ "getFutureRoisFutureOpticalCenter:futureLightSourceMaskTotalArea:currFrameMetaContainer:futureFrameMetaBuf:"
+ "getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:lightSourceMaskTotalArea:"
+ "isHWAccelerated"
+ "maxTotalThreadsPerThreadgroup"
+ "prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:"
+ "statistics"
+ "updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:"
+ "v24@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}16"
+ "v32@0:8^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}24"
+ "v44@0:816f24^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}28@36"
+ "v44@0:8q16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fBfff[32I][32I][32I]f}24f32f36B40"
+ "v84@0:8{?=^{__CVBuffer}@@@@^{__CVBuffer}}16^64^f72B80"
+ "{CMIVideoDeghostingStatistics=\"averageGhostArea\"d\"averageGhostCount\"d\"opticalCenterOffsetMag\"d\"opticalCenterOffsetX\"d\"opticalCenterOffsetY\"d\"opticalCenterEstConfidence\"d}"
+ "{CMIVideoDeghostingStatistics=dddddd}16@0:8"
- "-[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:frameDim:]"
- "-[RepairWeightsProcessor temporalFilterMetaContainerAtIndex_PA_L:ofQueue:ofQueue_HW:lookaheadBufferLen:]"
- "-[VideoDeghostingDetectionV3 getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:]"
- "-[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:doLite:]"
- "<<<< VEVideoDeghostingV3 >>>> %s: Frm#: %d, ID: %d, (x,y): (%5.2f, %5.2f), (w, h): (%5.2f, %5.2f), SPA: %.2f, S SPA R: %.2f"
- "@24@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}16"
- "@44@0:8^{__CVBuffer=}1624^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}32B40"
- "T^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB},V_metaContainer"
- "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}"
- "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}16@0:8"
- "^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}52@0:8@16@24B323644"
- "f32@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}16i24i28"
- "f88@0:8{?=ffffffff}16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}48^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}56^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}64^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}72B80f84"
- "getFutureRoisFutureOpticalCenter:currFrameMetaContainer:futureFrameMetaBuf:"
- "getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:"
- "prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:doLite:"
- "updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:frameDim:"
- "v24@0:8^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}16"
- "v32@0:8^{?=[2s][2[32{?=ffffffff}]][2[32f]][32f][32f]^{__CVBuffer}B}16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}24"
- "v40@0:816^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}24@32"
- "v44@0:8q16^{?=sssffffII[32{?=ffffffff}]B[32i][32s]fff[32][32f][32f][32f][32i][32f]B[32i][32i][32I][32][32][32][32I][32I][32I][32f][32I][32I][32I][32i][32i][32i][32I][32I][32i][32i][32f][32I][32I][32f][32f][32I][32I][32f][32f][32f][32f][32f][32f][32f][32f][32f][32f][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32I][32f][32f][32I]f{?=[3]}{?=[3]}ffff{?=[3]}BB{?=[3]}fB}24f32f36B40"
- "v76@0:8{?=^{__CVBuffer}@@@@^{__CVBuffer}}16^64B72"

```
