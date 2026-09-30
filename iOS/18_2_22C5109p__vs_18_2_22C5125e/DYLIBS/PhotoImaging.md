## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1759cc
-  __TEXT.__auth_stubs: 0x1f20
+720.4.101.0.0
+  __TEXT.__text: 0x1779c8
+  __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xef9c
-  __TEXT.__const: 0x7f2c
-  __TEXT.__cstring: 0x2b7a3
-  __TEXT.__swift5_typeref: 0xcb
+  __TEXT.__objc_methlist: 0xf014
+  __TEXT.__const: 0x7eec
+  __TEXT.__cstring: 0x2bc41
+  __TEXT.__swift5_typeref: 0xb7
   __TEXT.__constg_swiftt: 0x34
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x3d
   __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__swift5_capture: 0x4c
-  __TEXT.__oslogstring: 0x4ff7
+  __TEXT.__oslogstring: 0x4f80
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x43e8
+  __TEXT.__gcc_except_tab: 0x4388
   __TEXT.__dlopen_cstrs: 0x1d8
-  __TEXT.__unwind_info: 0x3a80
-  __TEXT.__eh_frame: 0x288
+  __TEXT.__unwind_info: 0x3ab0
+  __TEXT.__eh_frame: 0x1e0
   __TEXT.__objc_classname: 0x2839
-  __TEXT.__objc_methname: 0x24260
-  __TEXT.__objc_methtype: 0x3bcf
-  __TEXT.__objc_stubs: 0x1b6c0
-  __DATA_CONST.__got: 0x1b48
+  __TEXT.__objc_methname: 0x24396
+  __TEXT.__objc_methtype: 0x3c23
+  __TEXT.__objc_stubs: 0x1b8a0
+  __DATA_CONST.__got: 0x1ba0
   __DATA_CONST.__const: 0x2ac8
   __DATA_CONST.__objc_classlist: 0xaf8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8670
+  __DATA_CONST.__objc_selrefs: 0x86d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4e8
-  __DATA_CONST.__objc_arraydata: 0x7140
-  __AUTH_CONST.__auth_got: 0xfa8
+  __DATA_CONST.__objc_arraydata: 0x7130
+  __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__auth_ptr: 0xb0
-  __AUTH_CONST.__const: 0x3a48
-  __AUTH_CONST.__cfstring: 0x13760
-  __AUTH_CONST.__objc_const: 0x1de00
+  __AUTH_CONST.__const: 0x39c8
+  __AUTH_CONST.__cfstring: 0x13a60
+  __AUTH_CONST.__objc_const: 0x1de78
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_doubleobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270

   __DATA.__data: 0x115c
   __DATA.__bss: 0x7a8
   __DATA_DIRTY.__objc_data: 0x64f0
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6015
-  Symbols:   8023
-  CStrings:  10843
+  Functions: 6047
+  Symbols:   8043
+  CStrings:  10892
 
Symbols:
+ _NUAuxiliaryImageTypeToString
+ _OBJC_CLASS_$_NUVersion
+ _PIDepthInfoMajorVersionKey
+ _PIDepthInfoMinorVersionKey
+ _PIInpaintMasksAdjustmentKey
+ _PIPortraitTapToFocusEnabledKey
+ _PISemanticStyleCurrentMetadataVersion
+ _PISemanticStyleCurrentRenderingVersion
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_bridgeErrorToNSError
+ _swift_dynamicCastUnknownClassUnconditional
+ _swift_errorRetain
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_retain
- _PhotoImagingVersionNumber
- _PhotoImagingVersionString
- __Block_copy
- __Block_release
- _swift_deallocObject
- _swift_task_create
CStrings:
+ "+[PICompositionSidecarData _loadContentsDictionaryFromData:error:]"
+ "+[PICompositionSidecarData loadFromDictionary:error:]"
+ "+[PIInpaintCacheNode inpaintNodeWithInput:operations:masks:error:]"
+ "+[PIObjectRemoval maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:]"
+ "-[PICompositionSidecarData serialize:]"
+ "-[PIInpaintSourceNode _applyInpaintOperation:toImage:operationIndex:context:error:]"
+ "-[PIInpaintSourceNode initWithInputImage:inpaintOperations:maskNodes:sourceOrientation:isHDR:cacheKey:]"
+ "-[PISemanticStyleAdjustmentController hasDefaultStyleParameters]"
+ "-[PISemanticStyleAutoCalculator _resultFromImageProperties:error:]"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PISemanticStyleAdjustmentController.m"
+ "<%!@(MISSING):%!p(MISSING) \n\taperture:%!f(MISSING) \n\tminimumAperture:%!@(MISSING) \n\tmaximumAperture:%!@(MISSING) \n\tfocusRect:%!@(MISSING) \n\tportraitStrength:%!f(MISSING) \n\tSDOFRenderingVersion:%!l(MISSING)u \n\tportraitMajorVersion:%!l(MISSING)u \n\tportraitMinorVersion:%!l(MISSING)u \n\tdepthInfoMajorVersion:%!d(MISSING) \n\tdepthInfoMinorVersion:%!d(MISSING)>"
+ "@60@0:8@16@24@32q40B48@52"
+ "Asset is not stylable"
+ "B56@0:8@16@24Q32@40o^@48"
+ "B56@0:8@16{?=qq}24q40@48"
+ "Could not load cleanup model bundle URL"
+ "Could not load metadata version info: %!@(MISSING)"
+ "Failed to dump composition sidecar data, error: %!@(MISSING)"
+ "Failed to dump composition, error: %!@(MISSING)"
+ "Failed to export brush stroke history data"
+ "Invalid MakerNote Style dictionary"
+ "Invalid brush stroke history data"
+ "Invalid mask data"
+ "Invalid source extent for operation"
+ "Invalid source extent for operation %!{(MISSING)public}@"
+ "Missing brush stroke history data"
+ "Missing contents manifest"
+ "Missing contents manifest data"
+ "Missing mask"
+ "Missing mask %!@(MISSING)"
+ "Missing version info in "
+ "PISemanticStyleAutoCalculator - not supported: %!{(MISSING)public}@"
+ "PhotosComposition.plist"
+ "PhotosCompositionSidecar.aar"
+ "Styles not supported on current platform"
+ "Successfully dumped composition sidecar data to %!@(MISSING)"
+ "Successfully dumped composition to %!@(MISSING)"
+ "T@\"NSString\",N,R"
+ "Unexpected error when loading cleanup model bundle URL %!@(MISSING)"
+ "Unexpected metadata content type"
+ "Unexpected version info type"
+ "Unknown model name"
+ "Unsupported style metadata version"
+ "Unsupported style rendering version"
+ "_applyInpaintOperation:toImage:operationIndex:context:error:"
+ "_cleanupModelBundleURLString"
+ "_loadContentsDictionaryFromData:error:"
+ "_metadataVersionInfo"
+ "_resultFromImageProperties:error:"
+ "addImageSpaceInpaintingStroke:exclusionMask:closeAndFillStroke:needsPixellation:recordStroke:completion:"
+ "addObjectRemovalUsingImageSpaceStroke:exclusionMask:completion:"
+ "applyInpaintOperations:toImage:error:"
+ "blendWithRedMaskFilter"
+ "cleanupVersion"
+ "couldn't get inpainted image"
+ "dataDictionary != nil"
+ "default values should contain 3 values (tone / color / "
+ "depthInfoMajorVersion"
+ "depthInfoMinorVersion"
+ "dumpComposition"
+ "dumpComposition:toURL:error:"
+ "fileURLWithPath:isDirectory:"
+ "foregroundbackgroundsegmenter"
+ "hasDefaultStyleParameters"
+ "http://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia"
+ "inflatedFaceRect:imageOrientation:"
+ "initWithInputImage:inpaintOperations:maskNodes:sourceOrientation:isHDR:cacheKey:"
+ "initWithMajor:minor:"
+ "initializeAdjustment"
+ "inpaintModelVersion"
+ "inpaintNodeWithInput:operations:masks:error:"
+ "inpaintVersion"
+ "isCompatibleWithVersion:"
+ "isStylableFromImageProperties:error:"
+ "isTapToFocusEnabled:"
+ "loadFromDictionary:error:"
+ "maskByDilatingMask:fullExtent:"
+ "maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:"
+ "modelVersionInfo"
+ "refinementModelVersion"
+ "refinementVersion"
+ "resampleImage:by:sampleMode:extent:colorSpace:"
+ "resamplingColorSpace"
+ "resolveWithInputImage:inpaintOperations:cacheKey:"
+ "segmentationModelVersion"
+ "segmentationVersion"
+ "serialize:"
+ "setInpaintMasks:"
+ "strokeIsEntirelyWithinFace:imageSize:imageOrientation:detectedFaces:"
+ "tapToFocusEnabled"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
- "\nPixellation COUNT: %!l(MISSING)u"
- "+[PIInpaintCacheNode inpaintNodeWithInput:operations:masks:detectedFaces:error:]"
- "+[PIObjectRemoval maskIsMostlyWithinFace:imageSize:detectedFaces:]"
- "-[PIInpaintCompositeNode _colorSpaceForRescaling:]"
- "-[PIInpaintCompositeNode _evaluateImage:]"
- "-[PIInpaintSourceNode applyInpaintOperations:toImage:]"
- "-[PIInpaintSourceNode initWithInputImage:inpaintOperations:maskNodes:detectedFaces:sourceOrientation:isHDR:cacheKey:]"
- "-[PISemanticStyleAutoCalculator _resultFromImageProperties:]"
- "<%!@(MISSING):%!p(MISSING) \n\taperture:%!f(MISSING) \n\tminimumAperture:%!@(MISSING) \n\tmaximumAperture:%!@(MISSING) \n\tfocusRect:%!@(MISSING) \n\tportraitStrength:%!f(MISSING) \n\tSDOFRenderingVersion:%!l(MISSING)u \n\tportraitMajorVersion:%!l(MISSING)u \n\tportraitMinorVersion:%!l(MISSING)u>"
- "@40@0:8@16q24d32"
- "@68@0:8@16@24@32@40q48B56@60"
- "B48@0:8@16{?=qq}24@40"
- "Failed to export brush history to data blob"
- "Failed to load image properties for inpaint rescaling"
- "Invalid MakerNote SmartStyle dictionary: %!{(MISSING)public}@, ignored"
- "PISemanticStyleAutoCalculator Styles not supported on the current platform"
- "Pixellation[%!l(MISSING)u] NO"
- "Pixellation[%!l(MISSING)u] YES"
- "Pixellation[%!l(MISSING)u] intersectionArea / faceArea of %!f(MISSING) below threshold of %!f(MISSING)"
- "Pixellation[%!l(MISSING)u] intersectionArea / faceArea of %!f(MISSING) exceeds threshold of %!f(MISSING)"
- "Pixellation[%!l(MISSING)u] intersectionBBoxArea / maskBBoxArea of %!f(MISSING) below threshold of %!f(MISSING)"
- "Pixellation[%!l(MISSING)u] stroke intersection mask density of %!f(MISSING) changes intersectionAreaOverFaceArea to %!f(MISSING)"
- "_colorSpaceForRescaling:"
- "_detectedFacesFromFaceResult:"
- "_resultFromImageProperties:"
- "addImageSpaceInpaintingStroke:closeAndFillStroke:needsPixellation:recordStroke:completion:"
- "addObjectRemovalUsingImageSpaceStroke:completion:"
- "adjustmentContainsDeclutter"
- "applyInpaintOperations:toImage:"
- "downloadCleanupModelBundleWithCompletionHandler:"
- "foregroundbackgroundsegmenter.mlmodelc"
- "https://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia"
- "imageBySettingAlphaOneInExtent:"
- "inflatedFaceRects:captureOrientation:multiplier:"
- "initWithInputImage:inpaintOperations:maskNodes:detectedFaces:sourceOrientation:isHDR:cacheKey:"
- "inpaintNodeWithInput:operations:masks:detectedFaces:error:"
- "inpainting.mlmodelc"
- "isRGB"
- "isStylableFromImageProperties:"
- "maskByDilatingMask:amount:"
- "maskIsMostlyWithinFace:imageSize:detectedFaces:"
- "nu_waitUntilCompletedAndReturnError:"
- "refinement.mlmodelc"
- "resampleInSourceColorSpace"
- "resolveWithInputImage:inpaintOperations:detectedFaces:cacheKey:"
- "strokeIsEntirelyWithinFace:imageSize:detectedFaces:"
- "v24@0:8@?<v@?@\"NSError\">16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}52@?0{CGRect={CGPoint=dd}{CGSize=dd}}8Q40B48"

```
