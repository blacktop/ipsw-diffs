## CCPortrait

> `/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait`

```diff

-665.80.10.0.0
-  __TEXT.__text: 0x3d360
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x2b7c
-  __TEXT.__const: 0x2c8
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__cstring: 0x71ec
+665.100.6.0.0
+  __TEXT.__text: 0x3fc5c
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x2b8c
+  __TEXT.__const: 0x2b8
+  __TEXT.__gcc_except_tab: 0x828
+  __TEXT.__cstring: 0x77d8
   __TEXT.__oslogstring: 0x1ca2
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__unwind_info: 0xa98
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methname: 0x7cf4
+  __TEXT.__objc_methname: 0x7d0c
   __TEXT.__objc_methtype: 0x33f8
   __TEXT.__objc_stubs: 0x4a40
   __DATA_CONST.__got: 0x3b8

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d38
+  __DATA_CONST.__objc_selrefs: 0x1d40
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0x52c0
-  __AUTH_CONST.__objc_const: 0x4da0
+  __AUTH_CONST.__objc_const: 0x4db8
   __AUTH_CONST.__objc_intobj: 0xb88
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3912FA39-6C49-3A6D-B159-345B6F1933E2
-  Functions: 1266
-  Symbols:   365
-  CStrings:  3514
+  UUID: FAFAD3A7-8788-3255-BEE1-FD8A3FD1C622
+  Functions: 1301
+  Symbols:   361
+  CStrings:  3554
 
Symbols:
+ _FigSignalErrorAt3
- _FigSignalErrorAtGM
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x5
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "(2 == [_fgSegmentArray count]) is NULL"
+ "(2 == [_segmentArray count]) is NULL"
+ "-[ApplyBlurmap applyForegroundUsingConfig:image:inputBlurMap:inputAlpha:inputGainMap:inputImage:inputLuma:inputChroma:inputIntermediate:inputHalfRes1:inputHalfRes2:inputHalfResRG:outputLuma:outputChroma:scale:coreImageRender:version:context:captureFolderMiscPath:]"
+ "-[ApplyBlurmap initWithMetalQueue:]"
+ "-[ApplyBlurmap loadShaders]"
+ "/Library/Caches/com.apple.xbs/36C787BD-51D4-404A-A076-0F05B7B0FA6C/TemporaryDirectory.qH7drh/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/ApplyBlurmap.m"
+ "/Library/Caches/com.apple.xbs/36C787BD-51D4-404A-A076-0F05B7B0FA6C/TemporaryDirectory.qH7drh/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/EspressoWrapper.m"
+ "/Library/Caches/com.apple.xbs/36C787BD-51D4-404A-A076-0F05B7B0FA6C/TemporaryDirectory.qH7drh/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/MakeBlurMap.m"
+ "[_fgSegmentArray[0] isKindOfClass:[NSData class]] && [_fgSegmentArray[1] isKindOfClass:[NSData class]] is NULL"
+ "[_segmentArray[0] isKindOfClass:[NSData class]] && [_segmentArray[1] isKindOfClass:[NSData class]] is NULL"
+ "_addNoiseOnly is NULL"
+ "_antialiasRGBAX is NULL"
+ "_antialiasRGBAY is NULL"
+ "_antialiasX is NULL"
+ "_antialiasY is NULL"
+ "_blendRaytraced is NULL"
+ "_extractNegativeBlurValues is NULL"
+ "_extractPositiveBlurValues is NULL"
+ "_fgSegmentArray is NULL"
+ "_gainmapMultiply is NULL"
+ "_highlightRecovery is NULL"
+ "_library is NULL"
+ "_localContrast is NULL"
+ "_morphology is NULL"
+ "_prefilterX is NULL"
+ "_prefilterY is NULL"
+ "_preprocess is NULL"
+ "_preprocessScaled is NULL"
+ "_segmentArray is NULL"
+ "_sparseNoAlpha is NULL"
+ "_sparseNoAlphaRayFg is NULL"
+ "_sparseWithAlpha is NULL"
+ "_yuv1 is NULL"
+ "_yuv2 is NULL"
+ "bundle is NULL"
+ "config_params is NULL"
+ "image is NULL"
+ "image1As_sRGB is NULL"
+ "image2As_sRGB is NULL"
+ "imageRayFg is NULL"
+ "self is NULL"
+ "supportsPlacementSparse"
- "%s signalled err=%d at <>:%d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/ApplyBlurmap.m"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/EspressoWrapper.m"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/CCPortrait/MakeBlurMap.m"

```
