## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0x3f100
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x1044
-  __TEXT.__const: 0x4d90
-  __TEXT.__gcc_except_tab: 0x3258
-  __TEXT.__cstring: 0x1e32
+200.4.0.0.0
+  __TEXT.__text: 0x415bc
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x10d4
+  __TEXT.__const: 0x4f70
+  __TEXT.__gcc_except_tab: 0x3514
+  __TEXT.__cstring: 0x1e67
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__oslogstring: 0x2063
-  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__oslogstring: 0x2020
+  __TEXT.__unwind_info: 0x7e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x47f
-  __TEXT.__objc_methname: 0x3a8a
-  __TEXT.__objc_methtype: 0x8adf
-  __TEXT.__objc_stubs: 0x2720
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__objc_methname: 0x3f48
+  __TEXT.__objc_methtype: 0x8ce9
+  __TEXT.__objc_stubs: 0x28c0
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xc50
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x358
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x410
-  __AUTH_CONST.__cfstring: 0x2920
-  __AUTH_CONST.__objc_const: 0x4418
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__cfstring: 0x2a80
+  __AUTH_CONST.__objc_const: 0x45c8
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_ivar: 0x338
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x9e0
-  __DATA.__common: 0x202
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x748
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__common: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 597
-  Symbols:   848
-  CStrings:  1401
+  Functions: 614
+  Symbols:   870
+  CStrings:  1449
 
Symbols:
+ _FigCFDictionaryGetCGRectIfPresent
+ _OBJC_CLASS_$_NSScanner
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomDstRect
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomSrcRect
+ _kFigCaptureStreamMetadata_TotalSensorCropRect
+ _objc_retain_x26
CStrings:
+ "\x0f\t"
+ "D"
+ "D16"
+ "D17"
+ "D27"
+ "D28"
+ "D49"
+ "D63"
+ "D64"
+ "FigCaptureGetModelSpecificName"
+ "NSString *soft_FigCaptureGetModelSpecificName()"
+ "Origin"
+ "SetFile"
+ "T@\"NSDictionary\",&,N,V_regionOfInterestRectInBufferCoords"
+ "T@\"NSDictionary\",&,N,V_secondaryCameraInfo"
+ "T@\"NSDictionary\",&,N,V_secondaryModuleConfig"
+ "T@\"NSDictionary\",&,N,V_validRectInBufferCoords"
+ "T@\"NSDictionary\",&,N,V_validRectInSensorReadoutCoords"
+ "Tf,N,V_inputTextureDownsampleRatio"
+ "T{CGPoint=dd},N,V_deepZoomOrigin"
+ "_"
+ "_adjustConfigToValidRectInBufferCoords:validRectInSensorReadoutCoords:regionOfInterestRectInBufferCoords:"
+ "_deepZoomOrigin"
+ "_regionOfInterestRectInBufferCoords"
+ "_secondaryCameraInfo"
+ "_secondaryModuleConfig"
+ "_validRectInBufferCoords"
+ "_validRectInSensorReadoutCoords"
+ "containsObject:"
+ "deepZoomOrigin"
+ "encodeSetFileIDForModuleConfig:setFileID:"
+ "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:"
+ "hasPrefix:"
+ "i120@0:8@16@24@32@40@48@56^{?=BiiiiSS}64@72^@80@88^@96@104^I112"
+ "i32@0:8@16^I24"
+ "i44@0:8[3I]16I24^{SensorConfigAWBParams={sCSensorCalIdeal=SSSS}{sCSensorCalAbs=SSSS}{sCSensorCalBias=SSSS}{sCSensorCalGain=SSSS}II{sCameraColorConfig=[9s][9s][2s][2I]S[6[9s]][8[3S]][30[2s]]}}28^{sSlaveCameraAWBParam=SSI[3I][3I][3[3i]]BQfffBBf{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}}36"
+ "i64@0:8@16@24@32@40@48@56"
+ "i92@0:8@16@24@32@40@48@56f64f68I72^f76^f84"
+ "initFWPlatformID"
+ "process:clipped:lscGainsTex:validRectInBufferCoords:validRectInSensorReadoutCoords:awbStatsBuffer:awbTileStatsConfig:anstSkinMask:anstSkinMaskData:skyMaskTex:skyMaskData:regionOfInterestRectInBufferCoords:downsizeFactor:"
+ "rangeOfString:"
+ "regionOfInterestRectInBufferCoords"
+ "scanHexInt:"
+ "scannerWithString:"
+ "secondaryCameraInfo"
+ "secondaryModuleConfig"
+ "setDeepZoomOrigin:"
+ "setRegionOfInterestRectInBufferCoords:"
+ "setScanLocation:"
+ "setSecondaryCameraInfo:"
+ "setSecondaryModuleConfig:"
+ "setValidRectInBufferCoords:"
+ "setValidRectInSensorReadoutCoords:"
+ "translateAWBGainsToSecondaryChannelID:secondaryChannelID:secondaryConfig:secondaryAWBParams:"
+ "translateAWBGainsToSecondaryPortType:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:primaryRGain:primaryBGain:secondaryChannelID:secondaryRGain:secondaryBGain:"
+ "v32@0:8{CGPoint=dd}16"
+ "validRectInBufferCoords"
+ "validRectInSensorReadoutCoords"
+ "{CGPoint=\"x\"d\"y\"d}"
+ "{CGPoint=dd}16@0:8"
- "\x0f\x06"
- "+[LTMExtractMetadata extractRectanglesFrom:validBufferRect:ltmGeometry:]"
- "<<<< LTMAlgorithm >>>> %!s(MISSING): Fail to get FigCaptureLocalHistogramsV1"
- "T@\"NSDictionary\",&,N,V_regionOfInterestRect"
- "TI,N,V_inputTextureDownsampleRatio"
- "_adjustConfigToValidBufferRect:regionOfInterestRect:"
- "_regionOfInterestRect"
- "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:"
- "i112@0:8@16@24@32@40@48^{?=BiiiiSS}56@64^@72@80^@88@96^I104"
- "process:clipped:lscGainsTex:validBufferRect:awbStatsBuffer:awbTileStatsConfig:anstSkinMask:anstSkinMaskData:skyMaskTex:skyMaskData:regionOfInterestRect:downsizeFactor:"
- "regionOfInterestRect"
- "setRegionOfInterestRect:"

```
