## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-710.17.103.0.0
-  __TEXT.__text: 0x1721f8
-  __TEXT.__auth_stubs: 0x1dd0
+710.22.200.0.0
+  __TEXT.__text: 0x173fdc
+  __TEXT.__auth_stubs: 0x1df0
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xedbc
+  __TEXT.__objc_methlist: 0xee8c
   __TEXT.__const: 0x7f1c
-  __TEXT.__cstring: 0x2b0b3
+  __TEXT.__cstring: 0x2b185
   __TEXT.__swift5_typeref: 0xbd
   __TEXT.__constg_swiftt: 0x34
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_capture: 0x4c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x43bc
-  __TEXT.__oslogstring: 0x4e83
+  __TEXT.__gcc_except_tab: 0x43f4
+  __TEXT.__oslogstring: 0x4f46
   __TEXT.__dlopen_cstrs: 0x1d8
-  __TEXT.__unwind_info: 0x39f0
+  __TEXT.__unwind_info: 0x3a18
   __TEXT.__eh_frame: 0x288
   __TEXT.__objc_classname: 0x2834
-  __TEXT.__objc_methname: 0x23be8
-  __TEXT.__objc_methtype: 0x3c30
-  __TEXT.__objc_stubs: 0x1b400
-  __DATA_CONST.__got: 0x1b38
-  __DATA_CONST.__const: 0x2948
+  __TEXT.__objc_methname: 0x23ed6
+  __TEXT.__objc_methtype: 0x3c08
+  __TEXT.__objc_stubs: 0x1b540
+  __DATA_CONST.__got: 0x1b40
+  __DATA_CONST.__const: 0x2a58
   __DATA_CONST.__objc_classlist: 0xaf8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8558
+  __DATA_CONST.__objc_selrefs: 0x85e0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x4e0
-  __DATA_CONST.__objc_arraydata: 0x71a0
-  __AUTH_CONST.__auth_got: 0xf00
+  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_arraydata: 0x7120
+  __AUTH_CONST.__auth_got: 0xf10
   __AUTH_CONST.__auth_ptr: 0xa8
-  __AUTH_CONST.__const: 0x3a08
-  __AUTH_CONST.__cfstring: 0x13540
-  __AUTH_CONST.__objc_const: 0x1db80
+  __AUTH_CONST.__const: 0x39c8
+  __AUTH_CONST.__cfstring: 0x134c0
+  __AUTH_CONST.__objc_const: 0x1dbf8
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_doubleobj: 0x910
-  __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__objc_dictobj: 0x4420
+  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_dictobj: 0x43f8
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH.__objc_data: 0x8e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x10e8
+  __DATA.__objc_ivar: 0x10ec
   __DATA.__data: 0x1154
   __DATA.__bss: 0x760
   __DATA_DIRTY.__objc_data: 0x64f0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5948
-  Symbols:   7960
-  CStrings:  10735
+  Functions: 5973
+  Symbols:   7985
+  CStrings:  10763
 
Symbols:
+ _CGRectIntersectsRect
+ _CMTimeMakeWithSeconds
- _NSSelectorFromString
CStrings:
+ "PISegmentationLoader.m"
+ "_instancesForOperation:"
+ "inflatedFaceRects:captureOrientation:multiplier:"
+ "allowCachedLayoutConfigurationMismatch"
+ "_loadFirstResourceOnly"
+ "preferFullResolutionResource"
+ "TB,N,V_preferFullResolutionResource"
+ "B24@?0Q8^B16"
+ "isRGB"
+ "-[PISensitiveContentAnalysisRequest submit:]"
+ "setAllowCachedLayoutConfigurationMismatch:"
+ "subjectMaskDigestForComposition:subjectMaskBuffer:"
+ "densityForMask:context:"
+ "TB,N,V_loadFirstResourceOnly"
+ "Pixellation[%!l(MISSING)u] intersectionBBoxArea / maskBBoxArea of %!f(MISSING) exceeds threshold of %!f(MISSING)"
+ "Item already has full resolution resource loaded."
+ "emptyImage"
+ "addImageSpaceInpaintingStroke:closeAndFillStroke:needsPixellation:recordStroke:completion:"
+ "@40@0:8@16q24d32"
+ "Failed to load image properties for inpaint rescaling"
+ "Pixellation[%!l(MISSING)u] stroke intersection mask density of %!f(MISSING) changes intersectionAreaOverFaceArea to %!f(MISSING)"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}52@?0{CGRect={CGPoint=dd}{CGSize=dd}}8Q40B48"
+ "maskIdentifier != nil"
+ "setInput:"
+ "TB,N,V_allowCachedLayoutConfigurationMismatch"
+ "maskByRemovingMask:fromMask:"
+ "_foregroundOperationsFromComposition:subjectMaskBuffer:"
+ "@56@0:8@16@24@32{?=qq}40"
+ "_createSubjectMaskFromBuffer:digest:ciContext:fullImageSize:"
+ "Pixellation[%!l(MISSING)u] intersectionBBoxArea / maskBBoxArea of %!f(MISSING) below threshold of %!f(MISSING)"
+ "Pixellation[%!l(MISSING)u] faceBBoxArea        : %!f(MISSING)"
+ "@\"CIImage\"24@?0@\"NSString\"8^@16"
+ "-[PIInpaintCombinedMaskNode maskImageForIdentifier:error:]"
+ "Failed to apply exclusion mask"
+ "@128@0:8@16@24@32@40{?={?=qq}{?=qq}}48@80@88d96{?=qiIq}104"
+ "_sanitizeQueue"
+ "initWithSegmentationResult:composition:subjectMaskBuffer:detectedFaces:fullImageExtent:assetIdentifier:requestID:initialSensitivityScore:livePhotoKeyFrameTime:"
+ "initFileURLWithPath:isDirectory:"
+ "CGRectIsEmpty(strokeMask.extent) == NO"
+ "_loadFirstPreferredResource:completion:"
+ "Pixellation[%!l(MISSING)u] maskBBoxArea        : %!f(MISSING)"
+ "loadFirstResourceOnly"
+ "B48@0:8@16{?=qq}24@40"
+ "maskByAddingMask:toMask:"
+ "Sanitize queue not initialized"
+ "Inpaint sub=%!l(MISSING)d"
+ "_colorSpaceForRescaling:"
+ "indexesPassingTest:"
+ "strokeIsEntirelyWithinFace:imageSize:detectedFaces:"
+ "isLassoedSelection"
+ "@\"CIImage\"32@?0@\"CIImage\"8@\"PIInpaintOperation\"16^@24"
+ "\x113!\"5"
+ "_preferFullResolutionResource"
+ "subject-"
+ "resampleInSourceColorSpace"
+ "sanitizeQueue"
+ "Failed to generate mask"
+ "maskImageForIdentifier:error:"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_sanitizeQueue"
+ "setSanitizeQueue:"
+ "semanticStyleInterpolationHalfWindowTime"
+ "NUPixelSizeIsEmpty(imageSize) == NO"
+ "_loadFinalResource:completion:"
+ "_allowCachedLayoutConfigurationMismatch"
+ "setPreferFullResolutionResource:"
+ "+[PIObjectRemoval maskIsMostlyWithinFace:imageSize:detectedFaces:]"
+ "isScribbledSelection"
+ "Pixellation[%!l(MISSING)u] intersectionBBoxArea: %!f(MISSING)"
+ "setLoadFirstResourceOnly:"
+ "-[PIInpaintCompositeNode _colorSpaceForRescaling:]"
+ "Expected a valid version value from settings but got %!@(MISSING), skipping"
- "hasExclusionMasks"
- "_foregroundOperationsFromComposition:"
- "Pixellation[%!l(MISSING)u] maskArea        : %!f(MISSING)"
- "@48@0:8@16@24{?=qq}32"
- "linearThumb"
- "addImageSpaceInpaintingStroke:closeAndFillStroke:needsPixellation:recordStroke:"
- "-[PIInpaintAdjustmentController takeNewOperationsFromComposition:redactNewOperations:]"
- "Failed to convert exclusion mask to image"
- "Failed to convert mask to image"
- "maskIdentifiers.count > 0"
- "objectAtPoint"
- "showSubjectMatte"
- "_proxyOnly"
- "inflatedFaceRects:captureOrientation:geometry:"
- "\x113\x11\"5"
- "initWithScale:sampleMode:input:"
- "newMaskImageForIdentifiers:targetSize:error:"
- "@48@0:8@16{CGSize=dd}24o^@40"
- "initWithSegmentationResult:subjectMask:detectedFaces:fullImageExtent:assetIdentifier:requestID:initialSensitivityScore:livePhotoKeyFrameTime:ciContext:"
- "proxyOnly"
- "initWithDurationBefore:durationAfter:"
- "@128@0:8@16@24@32{?={?=qq}{?=qq}}40@72@80d88{?=qiIq}96@120"
- "_instancesForOperation:maskContext:"
- "updateMaskContext:forComposition:requestID:"
- "debugModeKey"
- "showSkyMatte"
- "Pixellation[%!l(MISSING)u] faceArea        : %!f(MISSING)"
- "subject"
- "originalThumb"
- "Pixellation[%!l(MISSING)u] intersectionArea: %!f(MISSING)"
- "Pixellation[%!l(MISSING)u] intersectionArea / maskArea of %!f(MISSING) exceeds threshold of %!f(MISSING)"
- "setProxyOnly:"
- "-[PIInpaintCombinedMaskNode newMaskImageForIdentifiers:targetSize:error:]"
- "showSkinMatte"
- "Expected incoming to be superset of current"
- "_createSubjectMaskFromBuffer:ciContext:fullImageSize:"
- "TB,N,V_proxyOnly"
- "Pixellation[%!l(MISSING)u] intersectionArea / maskArea of %!f(MISSING) below threshold of %!f(MISSING)"
- "semanticStyleTemporalWindowSize"
- "Auxiliary image properties not found"
- "B72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{?=qq}48@64"

```
