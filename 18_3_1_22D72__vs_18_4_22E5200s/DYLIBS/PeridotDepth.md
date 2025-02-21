## PeridotDepth

> `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`

```diff

-39.0.0.0.0
-  __TEXT.__text: 0x120d20
-  __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x1004
-  __TEXT.__gcc_except_tab: 0x7564
-  __TEXT.__cstring: 0x4d7a
-  __TEXT.__const: 0x18550
-  __TEXT.__oslogstring: 0x1242
-  __TEXT.__unwind_info: 0x1a80
-  __TEXT.__eh_frame: 0x50
+40.0.0.0.0
+  __TEXT.__text: 0x130804
+  __TEXT.__auth_stubs: 0x1840
+  __TEXT.__objc_methlist: 0x110c
+  __TEXT.__const: 0x18600
+  __TEXT.__gcc_except_tab: 0x773c
+  __TEXT.__cstring: 0x5139
+  __TEXT.__oslogstring: 0x12ef
+  __TEXT.__unwind_info: 0x1a28
+  __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x1e1
   __TEXT.__objc_methname: 0x4985
   __TEXT.__objc_methtype: 0x58d1
   __TEXT.__objc_stubs: 0x1f80
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca8
+  __DATA_CONST.__objc_selrefs: 0xd38
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__auth_got: 0xc30
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x2bc0
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x29d0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x3c0
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x274
   __DATA.__data: 0x12770
-  __DATA.__bss: 0x28a824
+  __DATA.__bss: 0x28a8c4
   __DATA.__common: 0x2
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1444
-  Symbols:   2059
-  CStrings:  1816
+  Functions: 1427
+  Symbols:   2087
+  CStrings:  1836
 
Symbols:
+ _CVPixelBufferPoolCreate
+ __ZN16PeridotTelemetry12startSessionE8PDPresetP13_PeridotCalib
+ __ZN16PixelBufferUtils14asVImageBufferEP10__CVBuffer6CGRect
+ __ZN16PixelBufferUtils14asVImageBufferEP10__CVBufferm6CGRect
+ __ZN16PixelBufferUtils21createPixelBufferPoolE6CGSizejm
+ __ZN16PixelBufferUtils23cropAndScalePixelBufferEP10__CVBufferS1_6CGRectS2_b
+ __ZN16PixelBufferUtils26pixelFormatAsFileExtensionEj
+ __ZN16PixelBufferUtils28pixelFormatFromFileExtensionEPKc
+ __ZN7peridot10PeridotDXP18getStrayRisingEdgeEPKNS_20RefHistogramAllSpotsEPA2_KfmPA2_iS8_
+ __ZN7peridot19FullStaticHistogramC1Em
+ __ZN7peridot19FullStaticHistogramC2Em
+ __ZN7peridot20RefHistogramAllSpotsaSERKS0_
+ __os_signpost_emit_unreliably_with_name_impl
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferWidthKey
+ _kVTPixelTransferPropertyKey_DestinationRectangle
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _os_signpost_enabled
+ _vImageConvert_Planar8ToBGRX8888
+ _vImageConvert_Planar8ToBGRXFFFF
+ _vImageConvert_Planar8ToXRGB8888
+ _vImageConvert_Planar8ToXRGBFFFF
+ _vImageConvert_Planar8toPlanar16F
+ _vImageConvert_Planar8toPlanarF
+ _vImageScale_ARGB16F
- __ZN16PeridotTelemetry12startSessionE8PDPreset
- __ZN16PixelBufferUtils14asVImageBufferEP10__CVBuffer
- __ZN16PixelBufferUtils14asVImageBufferEP10__CVBufferm
- __ZN7peridot10PeridotDXP18getStrayRisingEdgeERKNSt3__16vectorINS_20RefHistogramAllSpotsENS1_9allocatorIS3_EEEEPA2_KfmPA2_iSD_
- __ZN7peridot19FullStaticHistogramC1Ef
- __ZN7peridot19FullStaticHistogramC2Ef
- _fmod
- _objc_retain_x26
- _vImageConvert_PlanarFToARGB8888
- _vImageConvert_PlanarFtoARGBFFFF
CStrings:
+ "%s:%d - ERROR - crop origin (%2.2f,%2.2f) size (%2.2f, %2.2f) is outside image bounds (%lu, %lu)"
+ "%s:%d - ERROR - crop origin (%f,%f) size (%f, %f) is outside image bounds"
+ "%s:%d - ERROR - destRect origin (%f,%f) size (%f, %f) is outside image bounds"
+ "%s:%d - ERROR - failed creating pixelBufferPool with error %d"
+ "%s:%d - ERROR - multiplane pixel buffer with nonmatching plane index"
+ "%s:%d - ERROR - multiplane pixel buffers with nonmatching plane index"
+ "BgReplacedDevice"
+ "DXPMacro: wrong _hist_eq size"
+ "DXPMacro: wrong bins num in eqHists"
+ "DXPMacro: wrong histSize"
+ "Error in _baselineRemovalBlock.getBlrParams().priBins size"
+ "No extrinsics info for device %s. Will use 90 degree and a zero baseline"
+ "Wrong configuration (_oneMinus_DTMmod_4LSB size)"
+ "convertColorToGrayscale"
+ "convertGrayscaleAsColor"
+ "createPixelBufferPool"
+ "cropVImageBuffer"
+ "getPulseShapeOptimized: cdf has wrong size"
+ "getPulseShapeOptimized: cdf_newSize has wrong size"
+ "getPulseShapeOptimized: cdf_newSize or tSize has wrong size"
+ "getPulseShapeOptimized: cdf_time has wrong size"
+ "getPulseShapeOptimized: compIdx - wrong Index"
+ "interleave_neon<1> getBinsNum() < CISP_PERIDOT_NUM_HISTOGRAM_BINS"
+ "interleave_neon<1> interlHist.size() < priNum"
+ "interleave_neon<4> getBinsNum() < CISP_PERIDOT_NUM_HISTOGRAM_BINS*4"
+ "interleave_neon<4> interlHist.size() <= priIdx"
+ "ransacComputeHomography: WARNING: abnormal result: (ninliers = 0)"
+ "ransacComputeHomography: WARNING: abnormal result: (x1_norm.GetNumOfPoints() != x2_norm.GetNumOfPoints())"
- "%s:%d - ERROR - invalid crop dimensions"
- "%s:%d - ERROR - muliplane pixel buffer with nonmatching plane index"
- "%s:%d - ERROR - muliplane pixel buffers with nonmatching plane index"
- "*ninliers != 0"
- "No extrinsics info for device %s. Will use zeros"
- "convertGreyscaleAsColor"
- "ransacComputeHomography"
- "x1_norm.GetNumOfPoints() == x2_norm.GetNumOfPoints()"

```
