## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-325.4.1.0.0
-  __TEXT.__text: 0x15a960
-  __TEXT.__auth_stubs: 0x1c90
+334.5.4.0.0
+  __TEXT.__text: 0x1597d0
+  __TEXT.__auth_stubs: 0x1c80
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x9290
-  __TEXT.__const: 0x480d
-  __TEXT.__cstring: 0xd1b2
-  __TEXT.__gcc_except_tab: 0xc414
-  __TEXT.__oslogstring: 0x74bb
+  __TEXT.__objc_methlist: 0x9a74
+  __TEXT.__const: 0x485d
+  __TEXT.__cstring: 0xd1e3
+  __TEXT.__gcc_except_tab: 0xc628
+  __TEXT.__oslogstring: 0x758c
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__unwind_info: 0x4df0
-  __TEXT.__eh_frame: 0x19c
-  __TEXT.__objc_classname: 0x1839
-  __TEXT.__objc_methname: 0x15cac
-  __TEXT.__objc_methtype: 0x471a
-  __TEXT.__objc_stubs: 0xe540
-  __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__const: 0x3800
+  __TEXT.__unwind_info: 0x4e38
+  __TEXT.__eh_frame: 0x1e4
+  __TEXT.__objc_classname: 0x183a
+  __TEXT.__objc_methname: 0x15dc3
+  __TEXT.__objc_methtype: 0x4793
+  __TEXT.__objc_stubs: 0xe560
+  __DATA_CONST.__got: 0xbc0
+  __DATA_CONST.__const: 0x3810
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4370
+  __DATA_CONST.__objc_selrefs: 0x4480
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x5a8
   __DATA_CONST.__objc_arraydata: 0x618
-  __AUTH_CONST.__auth_got: 0xe60
+  __AUTH_CONST.__auth_got: 0xe58
   __AUTH_CONST.__auth_ptr: 0x70
   __AUTH_CONST.__const: 0x45c0
-  __AUTH_CONST.__cfstring: 0x86c0
-  __AUTH_CONST.__objc_const: 0x15678
+  __AUTH_CONST.__cfstring: 0x8700
+  __AUTH_CONST.__objc_const: 0x14b40
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH.__objc_data: 0x4088
+  __AUTH.__objc_data: 0x3f98
   __AUTH.__data: 0x350
   __DATA.__objc_ivar: 0xc1c
   __DATA.__data: 0xcd4
-  __DATA.__bss: 0x490
-  __DATA_DIRTY.__objc_data: 0x258
-  __DATA_DIRTY.__bss: 0x290
+  __DATA.__bss: 0x438
+  __DATA_DIRTY.__objc_data: 0x348
+  __DATA_DIRTY.__bss: 0x2e8
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5157
-  Symbols:   6394
-  CStrings:  6835
+  Functions: 5197
+  Symbols:   6500
+  CStrings:  6850
 
Symbols:
+ _CVPixelFormatDescriptionGetDescriptionWithPixelFormatType
+ _HMIPeakPowerPressureLevelDidChangeNotification
+ _HMIThermalLevelDidChangeNotification
+ _VTDecompressionSessionCreateWithOptions
+ _kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey
+ _kCVPixelFormatCompressionType
+ _kVTDecompressionSessionOption_LoggingIdentifier
- _CMTimeAbsoluteValue
- _VTDecompressionSessionCreate
- _fmod
CStrings:
+ "\x11\x13"
+ "%{public}@Creating pixel buffer with IOSurface because the pixel format is compressed."
+ "%{public}@Override set for preference: %@ value: %@"
+ "%{public}@VTCompressionSessionEncodeFrameWithOutputHandler failed: %d"
+ "@\"HMIVideoFrameIntervalSampler\""
+ "B20@0:8I16"
+ "HMIPeakPowerPressureLevelDidChangeNotification"
+ "HMIThermalLevelDidChangeNotification"
+ "HomeAI"
+ "Sample buffer has an invalid presentation time stamp: %@"
+ "T@\"HMISystemResourceUsage\",R"
+ "T@\"HMIVideoFrameIntervalSampler\",R,V_frameThumbnailSampler"
+ "T@\"HMIVideoFrameIntervalSampler\",R,V_frameTimelapseSampler"
+ "T{?=qiIq},R,V_preferredOutputSegmentInterval"
+ "T{?=qiIq},V_lastFlushedFramePresentationTimeStamp"
+ "^{__CVBuffer=}72@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24q56^@64"
+ "_lastFlushedFramePresentationTimeStamp"
+ "_lastSampledIntervalIndex"
+ "cropPixelBuffer:crop:options:error:"
+ "isPixelFormatCompressed:"
+ "lastFlushedFramePresentationTimeStamp"
+ "maxNumberOfAnalyzers"
+ "maximumAnalysisFPSDidChangeTo:"
+ "maximumNumberOfAnalyzersDidChangeTo:"
+ "setLastFlushedFramePresentationTimeStamp:"
- "Sample buffer has an invalid PTS."
- "T@\"HMIVideoFrameSampler\",R,V_frameThumbnailSampler"
- "T@\"HMIVideoFrameSampler\",R,V_frameTimelapseSampler"
- "T{?=qiIq},V_currentFragmentStartTime"
- "T{?=qiIq},V_preferredOutputSegmentInterval"
- "VTCompressionSessionEncodeFrameWithOutputHandler failed, err: %d"
- "_currentFragmentStartTime"
- "_lastIndex"
- "currentFragmentStartTime"
- "setCurrentFragmentStartTime:"

```
