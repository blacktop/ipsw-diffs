## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-580.2.0.0.0
-  __TEXT.__text: 0x2f378
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x214c
-  __TEXT.__const: 0x588
-  __TEXT.__gcc_except_tab: 0x1784
-  __TEXT.__oslogstring: 0x423f
-  __TEXT.__cstring: 0x3191
+580.6.21.0.0
+  __TEXT.__text: 0x31a20
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x21dc
+  __TEXT.__const: 0x668
+  __TEXT.__gcc_except_tab: 0x17c4
+  __TEXT.__oslogstring: 0x484c
+  __TEXT.__cstring: 0x33ce
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x900
-  __TEXT.__objc_classname: 0x2ca
-  __TEXT.__objc_methname: 0x7958
-  __TEXT.__objc_methtype: 0x1eb2
-  __TEXT.__objc_stubs: 0x4360
+  __TEXT.__unwind_info: 0x928
+  __TEXT.__objc_classname: 0x2de
+  __TEXT.__objc_methname: 0x7c0d
+  __TEXT.__objc_methtype: 0x20a4
+  __TEXT.__objc_stubs: 0x4520
   __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f0
+  __DATA_CONST.__objc_selrefs: 0x1650
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x5438
+  __AUTH_CONST.__cfstring: 0x1780
+  __AUTH_CONST.__objc_const: 0x5578
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x588
-  __DATA.__data: 0x360
+  __DATA.__objc_ivar: 0x5ac
+  __DATA.__data: 0x380
   __DATA.__common: 0x50
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x7d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 754
-  Symbols:   982
-  CStrings:  2050
+  Functions: 767
+  Symbols:   997
+  CStrings:  2107
 
Symbols:
+ _bzero
+ _malloc_type_calloc
CStrings:
+ "-[DeskCamRenderingSession _updateDeskEdgeDetectionDataInOutputSpace]"
+ "{?=i}16@0:8"
+ "spans"
+ "-[DeskCamRenderingSession autoZoomValue]"
+ "_lineDetectionController.cumRowSum"
+ "_subjectRectangleInFramingSpace"
+ "_subjectRectangleInSensorSpace"
+ "_useFurthestPoint"
+ "24@0:816"
+ "_estimateSubjectRectangleInFramingSpaceFromSubjectRectangleInSensorSpace:"
+ "_filterAutoZoomScalingFactor:"
+ "autoZoomValue"
+ "_lineDetectionController.rowSum"
+ "_lineDetectionController.rowSumTextures[i]"
+ "{?=\"enableTemporalHysteresis\"B\"temporalAlpha\"f\"smallChangeThresh\"f\"largeChangeThresh\"f\"smallChangeObservationDurationInitValue\"i\"largeChangeObservationDurationInitValue\"i\"smallChangeObservationDuration\"i\"largeChangeObservationDuration\"i}"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 2: %!f(MISSING), DominantLineYX [%!f(MISSING), %!f(MISSING)]"
+ "_spanStrengthWeighting"
+ "_updateSubjectRectangleInSensorSpace:withDetections:"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING):  normalizedPointInOutputCropRect 1: (%!f(MISSING), %!f(MISSING))."
+ "getBytes:bytesPerRow:fromRegion:mipmapLevel:"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not allocate lineDetectionController.inputTexture"
+ "_transformMatrixWithOutputCropRectangle:"
+ "72@0:816{?=[3]}24"
+ "_autoZoomSupported"
+ "-[DeskCamRenderingSession _filterDeskEdgeDetectorEndPoints::]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updateDeskEdgeDetectionDataInOutputSpace] Transform matrix is not valid."
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 1: %!f(MISSING), DominantLineYX [%!f(MISSING), %!f(MISSING)]"
+ "deskCam::deskEdgeFinderEdgeSum"
+ "rowSum"
+ "_lineDetectionController.spans"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not allocate lineDetectionController.rowSumTextures[i]"
+ "_autoZoomFilteringController"
+ "_mapNormalizedPointInFramingSpaceToOutputCropRect:withTransformMatrix:"
+ "p03.z != 0.f"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][_filterDeskEdgeDetectorEndPoints]: (%!f(MISSING), %!f(MISSING))"
+ "setTextureType:"
+ "p13.z != 0.f"
+ "{?=\"inputTexture\"@\"<MTLTexture>\"\"lowestPointOfDominantLineInOutputCrop\"\"alpha\"f\"resetCounter\"i\"rowSumTextures\"[7@\"<MTLTexture>\"]\"rowSum\"^\"cumRowSum\"^f\"spans\"^{?}}"
+ "_filterDeskEdgeDetectorEndPoints::"
+ "deskCam::imageWarpingDownscaling"
+ "_multiPassDownscaling"
+ "v32@0:81624"
+ "registerBodyDetections:"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>registerFaceDetections:bodyDetections:handDetections:] Subject rectangle in sensor space: (%!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING))."
+ "v32@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16@24"
+ "TB,R,N,V_autoZoomSupported"
+ "-[DeskCamRenderingSession registerBodyDetections:]"
+ "_deskEdgeDetectorResult"
+ "autoZoomSupported"
+ "_mapPointFromNormalizedSensorSpaceToNormalizedFramingSpace:"
+ "_autoZoomScalingFactor"
+ "Tf,R,N,V_autoZoomValue"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>registerFaceDetections:bodyDetections:handDetections:] Subject rectangle in framing space: (%!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING))."
+ "(uint)rowSumTex.width == nRows"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "\x01\x11\xf0\xf0\xf0\xf0C\x13\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91'"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskCam][_updateDeskEdgeDetectionDataInOutputSpace] rowIndex: %!d(MISSING)"
+ "cumRowSum"
+ "_lineDetectionController.inputTexture"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 3 after Hysteresis: %!f(MISSING)"
+ "_updateDeskEdgeDetectionDataInOutputSpace"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updateDeskEdgeDetectionDataInOutputSpace] Transform matrix inverse is not valid."
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>autoZoomValue]: Auto zoom value %!f(MISSING)."
+ "_autoZoomValue"
+ "_lineDetectionController"
- "\x01\x11\xf0\xf0\xf0\xb3\x13"
- "-1"
- "_zoomFactorApplied"
- "zoomFactorApplied"
- "Tf,R,N,V_zoomFactorApplied"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_subjectRect"
- "subjectRect"
- "_subjectRect"

```
