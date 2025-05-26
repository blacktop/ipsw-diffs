## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-1.69.0.0.0
-  __TEXT.__text: 0x15a69c
-  __TEXT.__auth_stubs: 0x2db0
+1.107.0.0.0
+  __TEXT.__text: 0x15b394
+  __TEXT.__auth_stubs: 0x2dc0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x20da7
+  __TEXT.__cstring: 0x20f5b
   __TEXT.__const: 0x1f218
-  __TEXT.__gcc_except_tab: 0x4b08
-  __TEXT.__oslogstring: 0x141f5
-  __TEXT.__unwind_info: 0x3710
+  __TEXT.__gcc_except_tab: 0x4b40
+  __TEXT.__oslogstring: 0x14451
+  __TEXT.__unwind_info: 0x3724
   __TEXT.__eh_frame: 0x320
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x1821
+  __TEXT.__objc_methname: 0x188b
   __TEXT.__objc_methtype: 0xf00
-  __TEXT.__objc_stubs: 0x1b60
-  __DATA_CONST.__got: 0x2ce8
-  __DATA_CONST.__const: 0xe6d0
+  __TEXT.__objc_stubs: 0x1ba0
+  __DATA_CONST.__got: 0x2cf0
+  __DATA_CONST.__const: 0xe710
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa08
-  __DATA_CONST.__objc_selrefs: 0x708
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__const: 0x1c20
-  __AUTH_CONST.__cfstring: 0x88a0
+  __AUTH_CONST.__cfstring: 0x88e0
   __AUTH_CONST.__auth_ptr: 0x88
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x16d0
+  __AUTH_CONST.__auth_got: 0x16d8
   __AUTH.__const_weak: 0x100
   __AUTH.__objc_data: 0xf0
   __AUTH.__got_weak: 0x18
   __DATA.__got_weak: 0xe8
-  __DATA.__objc_classrefs: 0x160
+  __DATA.__objc_classrefs: 0x168
   __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x10b2e0

   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
-  - /System/Library/PrivateFrameworks/AppleCV3DHA.framework/AppleCV3DHA
   - /System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA
   - /System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4141
-  Symbols:   9896
-  CStrings:  6087
+  Functions: 4150
+  Symbols:   9918
+  CStrings:  6118
 
Symbols:
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table67
+ GCC_except_table72
+ GCC_except_table82
+ _OBJC_CLASS_$_ADFigCameraCalibrationSource
+ __Z24reportPeridotCoexRetriesjj
+ __ZN12MetalObjects13createTextureEPU15__autoreleasingPU21objcproto10MTLTexture11objc_objectPfii.cold.1
+ __ZN14CalibrateRgbIr15PrepareXyzWorldERN8MathLibs10_CamParamsIfEER6MatrixIfERK4_ROIS6_P10PixelCoordPj.cold.3
+ __ZN14CalibrateRgbIr22PrepareGridCalculationER6MatrixIfES2_jj.cold.1
+ __ZN6H16ISP12H16ISPDevice24ISP_GetFWErrorStatisticsEP23H16ISPFWErrorStatistics
+ __ZN6H16ISP20H16ISPServicesRemote16RegisterDeviceIDEPKc
+ __ZN6H16ISP20H16ISPServicesRemote7RunRgbjEP10__CVBufferPK14__CFDictionaryS5_PK9__CFArrayS5_S5_23kFigJasperRgbBufferTypebjjtjbjjjj20kFigIsfStepDetection
+ __ZN6H16ISP30TimeOfFlightAutoFocusAssistant20getPreviewMasterTypeEv
+ __ZN6H16ISP35H16ISPTimeOfFlightColorSynchronizer37TimeOfFlightColorSynchronizerInternal14logColorBufferEbP10__CVBufferP12NSDictionary
+ __ZNK6H16ISP12H16ISPDevice13getSensorTypeEj
+ ____Z24reportPeridotCoexRetriesjj_block_invoke
+ ___block_descriptor_44_e30_"NSObject<OS_xpc_object>"8?0l
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_tmp.2110
+ ___block_descriptor_tmp.2136
+ ___block_descriptor_tmp.2248
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.27
+ ___block_literal_global.29
+ _kFigCaptureStreamMetadata_AdaptiveLensShadingStrength
+ _objc_msgSend$getFrameTransformsFromMetadataDictionary:sensorCropRect:rawSensorSize:postReadCropRect:
+ _objc_msgSend$setInternalState:
+ _objc_retain_x3
- GCC_except_table54
- GCC_except_table68
- GCC_except_table76
- __ZN6H16ISP20H16ISPServicesRemote7RunRgbjEP10__CVBufferPK14__CFDictionaryPK9__CFArrayS5_S5_23kFigJasperRgbBufferTypebjjtjbjjjj20kFigIsfStepDetectiond
- __ZN6H16ISP30TimeOfFlightAutoFocusAssistant15isImageRelevantEv
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.2102
- ___block_descriptor_tmp.2128
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.2240
- ___block_descriptor_tmp.25
- ___block_literal_global.27
CStrings:
+ "%s: Failed to convert CFString to C string"
+ "%s: Failed to register device ID '%s' with remote assistant err=0x%08x"
+ "ConnectWithRemoteAssistant"
+ "Got Wide buffer from %s scaler. Zoom factor: %f. Sensor crop: (%.1f, %.1f, %.1f, %.1f), readout size: (%.1f, %.1f), ISP crop: (%.1f, %.1f, %.1f, %.1f), image size: (%zu, %zu). Preview master: %s"
+ "H16ISPFrameReceiver::%s - InitiateShutdown error: 0x%08X\n"
+ "H16ISPServicesRemoteDeviceID"
+ "H16ISPServicesRemoteRGBJMetadataKey"
+ "Link Training"
+ "Lock PLL"
+ "PrepareGridCalculation"
+ "PrepareGridCalculation failed."
+ "RGB-IR: %s: rdar://112006283 Aborting texture creation rows: %d, cols: %d, buffer: %p"
+ "RGB-IR: %s: rdar://112006283 Error creating textures => Abortig Rgb-Ir run"
+ "RGB-IR: %s: rdar://112006283 numOfGoodPts is %d < 256 => Abortig Rgb-Ir run"
+ "RetryCounter"
+ "Source"
+ "Spmi0ErrorCount"
+ "Spmi1ErrorCount"
+ "SuperWide"
+ "Tele"
+ "Temperature"
+ "VSpad"
+ "Wide"
+ "com.apple.isp.PeridotCoexRetry"
+ "createTexture"
+ "getFrameTransformsFromMetadataDictionary:sensorCropRect:rawSensorSize:postReadCropRect:"
+ "primary"
+ "secondary"
+ "setInternalState:"

```
