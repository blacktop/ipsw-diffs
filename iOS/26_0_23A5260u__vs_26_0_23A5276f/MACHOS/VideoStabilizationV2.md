## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x57ddc
+655.0.0.122.4
+  __TEXT.__text: 0x5831c
   __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x2ea0
-  __TEXT.__objc_methlist: 0x195c
-  __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x510f
-  __TEXT.__objc_methtype: 0x14ef
+  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_methlist: 0x190c
+  __TEXT.__objc_classname: 0x1d4
+  __TEXT.__objc_methname: 0x50a5
+  __TEXT.__objc_methtype: 0x14ae
   __TEXT.__const: 0x6a0
-  __TEXT.__oslogstring: 0xd176
-  __TEXT.__cstring: 0x901f
-  __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__oslogstring: 0xd15c
+  __TEXT.__cstring: 0x8fef
+  __TEXT.__gcc_except_tab: 0x3cc
+  __TEXT.__unwind_info: 0x7a0
   __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x760
+  __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__cfstring: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x828
   __DATA_CONST.__objc_arraydata: 0x2718
   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x3f68
-  __DATA.__objc_selrefs: 0xeb0
-  __DATA.__objc_ivar: 0x450
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x3de8
+  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_ivar: 0x438
+  __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__common: 0x60
   __DATA.__bss: 0x24

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9E084D9-E8C9-35A4-865B-C9861FADCA48
-  Functions: 1204
-  Symbols:   2549
-  CStrings:  2746
+  UUID: C5C42549-164F-38A6-8797-7176FEC88DF3
+  Functions: 1193
+  Symbols:   2534
+  CStrings:  2734
 
Symbols:
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ __runVideoDeghostingRepairOnSingleFrame
+ _kFigCaptureVideoDeghostingSampleBufferAttachmentKey_VideoDeghostingStatistics
+ _kFigCaptureVideoDeghostingStatisticsKey_AverageGhostArea
+ _kFigCaptureVideoDeghostingStatisticsKey_AverageGhostCount
+ _kFigCaptureVideoDeghostingStatisticsKey_Enabled
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterEstConfidence
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetMag
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetX
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetY
+ _kFigCaptureVideoDeghostingStatisticsKey_Version
+ _objc_msgSend$isHWAccelerated
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$statistics
+ _objc_retain_x25
+ _runVideoDeghostingRepairOnSingleFrame.cold.1
- -[GVSIIRCascadedFilterProcessor filteredValue]
- -[GVSIIRCascadedFilterProcessor frameRate]
- -[GVSIIRCascadedFilterProcessor initWithConfig:]
- -[GVSIIRCascadedFilterProcessor initWithConfig:].cold.1
- -[GVSIIRCascadedFilterProcessor initWithConfig:].cold.2
- -[GVSIIRCascadedFilterProcessor reset]
- -[GVSIIRCascadedFilterProcessor setFrameRate:]
- -[GVSIIRCascadedFilterProcessor updateValue:frameDuration:]
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._delay
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._filteredValue
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._frameRate
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._isFilterInitialized
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._lowPassBuffers
- OBJC_IVAR_$_GVSIIRCascadedFilterProcessor._order
- _OBJC_CLASS_$_GVSIIRCascadedFilterProcessor
- _OBJC_METACLASS_$_GVSIIRCascadedFilterProcessor
- _OUTLINED_FUNCTION_80
- __Block_object_dispose
- __OBJC_$_INSTANCE_METHODS_GVSIIRCascadedFilterProcessor
- __OBJC_$_INSTANCE_VARIABLES_GVSIIRCascadedFilterProcessor
- __OBJC_$_PROP_LIST_GVSIIRCascadedFilterProcessor
- __OBJC_CLASS_RO_$_GVSIIRCascadedFilterProcessor
- __OBJC_METACLASS_RO_$_GVSIIRCascadedFilterProcessor
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_40_e8_32r_e8_v12?0i8lr32l8
CStrings:
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Forcing transformFits NO due to quaternion negation at centerFrameOffset %d"
+ "<<<< GyroVideoStabilizationV2 >>>> %s: VideoDeghostingStatistics: %@"
+ "<<<< VISISPMeshGeneratorV2 >>>> %s: ISP Mesh is too big for current ISP hardware, current size needed = %d, max size = %d for output size = (%d,%d)"
+ "_attachVideoDeghostingAnalytics"
+ "isHWAccelerated"
+ "numberWithDouble:"
+ "repairFrameLookahead >= 0"
+ "statistics"
- "-[GVSIIRCascadedFilterProcessor initWithConfig:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Bundle/Common/Computation/GVSFilteringUtilities.m %s: 'delay' should be > 0"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Bundle/Common/Computation/GVSFilteringUtilities.m %s: 'order' should be an integer number between [1, %d]"
- "@24@0:8{?=If}16"
- "GVSIIRCascadedFilterProcessor"
- "Tf,N,V_frameRate"
- "T{?=},R,N,V_filteredValue"
- "[5{?=\"vector\"}]"
- "_delay"
- "_frameRate"
- "_lowPassBuffers"
- "_order"
- "config.delay > 0"
- "config.order > 0 && config.order <= (5)"
- "frameRate"
- "initWithConfig:"
- "setFrameRate:"
- "updateValue:frameDuration:"
- "{?=\"vector\"}"
- "{?=}36@0:8{?=}16f32"

```
