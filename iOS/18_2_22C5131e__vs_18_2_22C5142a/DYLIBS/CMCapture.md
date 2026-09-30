## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-587.60.14.122.2
-  __TEXT.__text: 0x503468
-  __TEXT.__auth_stubs: 0x4dc0
-  __TEXT.__objc_methlist: 0x2a60c
+587.62.18.0.0
+  __TEXT.__text: 0x503f24
+  __TEXT.__auth_stubs: 0x4db0
+  __TEXT.__objc_methlist: 0x2a5ac
   __TEXT.__const: 0x1504f8
-  __TEXT.__cstring: 0x71e72
-  __TEXT.__oslogstring: 0x24c46
+  __TEXT.__cstring: 0x71fb0
+  __TEXT.__oslogstring: 0x24e00
   __TEXT.__gcc_except_tab: 0x28c0
   __TEXT.__dlopen_cstrs: 0x686
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xbed8
-  __TEXT.__objc_classname: 0x7581
-  __TEXT.__objc_methname: 0x91969
-  __TEXT.__objc_methtype: 0x139b8
-  __TEXT.__objc_stubs: 0x3f5e0
-  __DATA_CONST.__got: 0x5ef0
-  __DATA_CONST.__const: 0x9780
-  __DATA_CONST.__objc_classlist: 0x18b8
+  __TEXT.__unwind_info: 0xbed0
+  __TEXT.__objc_classname: 0x7562
+  __TEXT.__objc_methname: 0x91946
+  __TEXT.__objc_methtype: 0x139af
+  __TEXT.__objc_stubs: 0x3f4e0
+  __DATA_CONST.__got: 0x5f00
+  __DATA_CONST.__const: 0x97a0
+  __DATA_CONST.__objc_classlist: 0x18a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12108
+  __DATA_CONST.__objc_selrefs: 0x120c0
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x1730
-  __DATA_CONST.__objc_arraydata: 0x35d0
-  __AUTH_CONST.__auth_got: 0x26f0
+  __DATA_CONST.__objc_superrefs: 0x1720
+  __DATA_CONST.__objc_arraydata: 0x3568
+  __AUTH_CONST.__auth_got: 0x26e8
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3a70
-  __AUTH_CONST.__cfstring: 0x37820
-  __AUTH_CONST.__objc_const: 0x86468
+  __AUTH_CONST.__const: 0x3a90
+  __AUTH_CONST.__cfstring: 0x37880
+  __AUTH_CONST.__objc_const: 0x86308
   __AUTH_CONST.__objc_intobj: 0x4e18
-  __AUTH_CONST.__objc_arrayobj: 0x2580
-  __AUTH_CONST.__objc_doubleobj: 0xa80
-  __AUTH_CONST.__objc_floatobj: 0x230
+  __AUTH_CONST.__objc_arrayobj: 0x2568
+  __AUTH_CONST.__objc_doubleobj: 0x9c0
+  __AUTH_CONST.__objc_floatobj: 0x220
   __AUTH_CONST.__objc_dictobj: 0x1798
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x9408
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x9404
   __DATA.__data: 0x48f0
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x5e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 20581
-  Symbols:   26239
-  CStrings:  36376
+  Functions: 20580
+  Symbols:   26241
+  CStrings:  36372
 
Symbols:
+ _OBJC_CLASS_$_BWMovingWindowStats
+ _OBJC_CLASS_$_BWStats
+ _OBJC_METACLASS_$_BWMovingWindowStats
+ _OBJC_METACLASS_$_BWStats
- _bsearch
CStrings:
+ ", median: %lf%@"
+ "-[BWFigCaptureSession graph:didStartSourceNode:error:]"
+ "/System/Library/PrivateFrameworks/VisualIntelligence.framework/assets_581/ObjectDetectionModel.bundle"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Can't cancel deferred graph setup because a recording has been started"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Releasing visISPProcessingSession %p after starting wide source node"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Saved visISPProcessingSession %p"
+ "<<<< FigCaptureSourceServer >>>> %s: client already holds this source - don't vend this again for prewarming. Will vend new list of sources"
+ "@28@0:8B16q20"
+ "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@ %@"
+ "Preview Output Splitter"
+ "T@\"BWFigCaptureISPProcessingSession\",R,N,V_ispProcessingSession"
+ "T@\"BWStats\",C,N,V_videoFrameDurationStats"
+ "Td,R,N,V_max"
+ "Td,R,N,V_min"
+ "Tq,N,V_nextDataPointIndex"
+ "[graph connectOutput:previewOutputsBySourceDeviceType[sourceDeviceType] toInput:previewSplitterNode.input pipelineStage:((void *)0)]"
+ "_dataPoints"
+ "_medianCalculationEnabled"
+ "_nextDataPointIndex"
+ "_nextPreviewOutputIndexBySourceDeviceType"
+ "_numDataPoints"
+ "_previewOutputsArrayBySourceDeviceType"
+ "captureSourceServer_handleCopySourcesMessage"
+ "com.apple.PassbookUIService"
+ "description=CameraCapture-587.62.18"
+ "findPreviewOutput"
+ "graph:didStartSourceNode:error:"
+ "haveStartedRecordingDuringDeferredSetup"
+ "initWithMedianCalculationEnabled:maxNumberOfSamplesForMedianCalculation:"
+ "nextDataPointIndex"
+ "nmsBoxIdices"
+ "nmsBoxes"
+ "nmsNumBoxes"
+ "nmsScores"
+ "nonVDOPreviewDerivedConnectionConfigurations.count"
+ "removeDataPoint:"
+ "setNextDataPointIndex:"
+ "tag_scores"
+ "v36@0:8@\"BWGraph\"16@\"BWSourceNode\"24i32"
- "%@, median: %lf%@ over %lu samples"
- "-[BWHistogramStats addDataPointP:]"
- "0 <= foundIndex && foundIndex < _binsCount"
- "@\"BWHistogramStats\""
- "@\"BWMedianStats\""
- "B24@0:8d16"
- "BWHistogramStats"
- "BWMedianStats"
- "Histogram bins are invalid"
- "Index out of range"
- "Invalid median max number of samples"
- "Invalid quantile count"
- "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@"
- "T@\"BWMedianStats\",C,N,V_videoFrameDurationStats"
- "T@\"NSDictionary\",&,N,V_luxHistogram"
- "Td,R,N,V_estimatedMedian"
- "Tf,N,V_medianLuxValue"
- "_areas"
- "_bins"
- "_binsCount"
- "_counts"
- "_estimatedMedian"
- "_luxHistogram"
- "_medianLuxValue"
- "_previewOutputsBySourceDeviceType"
- "addDataPointP:"
- "alsLuxBin%@"
- "description=CameraCapture-587.60.14.122.2"
- "detectorModelDescriptions"
- "estimatedMedian"
- "getEstimatedQuantiles:n:"
- "histogramAsDictionary"
- "initWithBins:"
- "initWithMaxNumberOfSamplesForMedianCalculation:"
- "inputImageSize"
- "luxHistogram"
- "medianLuxValue"
- "modelOutputs"
- "modelURL"
- "setLuxHistogram:"
- "setMedianLuxValue:"
- "v28@0:8^d16i24"

```
