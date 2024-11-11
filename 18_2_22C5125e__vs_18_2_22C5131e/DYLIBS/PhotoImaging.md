## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-720.4.101.0.0
-  __TEXT.__text: 0x1779c8
+720.10.101.0.0
+  __TEXT.__text: 0x176a28
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xf014
-  __TEXT.__const: 0x7eec
-  __TEXT.__cstring: 0x2bc41
+  __TEXT.__objc_methlist: 0xefe4
+  __TEXT.__const: 0x7f1c
+  __TEXT.__cstring: 0x2bb17
   __TEXT.__swift5_typeref: 0xb7
   __TEXT.__constg_swiftt: 0x34
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x3d
   __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__oslogstring: 0x4f80
+  __TEXT.__oslogstring: 0x4ed2
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x4388
+  __TEXT.__gcc_except_tab: 0x42b4
   __TEXT.__dlopen_cstrs: 0x1d8
   __TEXT.__unwind_info: 0x3ab0
   __TEXT.__eh_frame: 0x1e0
-  __TEXT.__objc_classname: 0x2839
-  __TEXT.__objc_methname: 0x24396
-  __TEXT.__objc_methtype: 0x3c23
-  __TEXT.__objc_stubs: 0x1b8a0
+  __TEXT.__objc_classname: 0x2808
+  __TEXT.__objc_methname: 0x245ca
+  __TEXT.__objc_methtype: 0x3c1c
+  __TEXT.__objc_stubs: 0x1bb80
   __DATA_CONST.__got: 0x1ba0
-  __DATA_CONST.__const: 0x2ac8
-  __DATA_CONST.__objc_classlist: 0xaf8
+  __DATA_CONST.__const: 0x2c00
+  __DATA_CONST.__objc_classlist: 0xae8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x86d0
+  __DATA_CONST.__objc_selrefs: 0x8788
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x7130
   __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__auth_ptr: 0xb0
-  __AUTH_CONST.__const: 0x39c8
-  __AUTH_CONST.__cfstring: 0x13a60
-  __AUTH_CONST.__objc_const: 0x1de78
+  __AUTH_CONST.__const: 0x39e8
+  __AUTH_CONST.__cfstring: 0x13aa0
+  __AUTH_CONST.__objc_const: 0x1dd20
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_doubleobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270

   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH.__objc_data: 0x8e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1118
+  __DATA.__objc_ivar: 0x110c
   __DATA.__data: 0x115c
-  __DATA.__bss: 0x7a8
-  __DATA_DIRTY.__objc_data: 0x64f0
+  __DATA.__bss: 0x7a0
+  __DATA_DIRTY.__objc_data: 0x6450
   __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6047
-  Symbols:   8043
-  CStrings:  10892
+  Functions: 6052
+  Symbols:   8052
+  CStrings:  10912
 
Symbols:
+ OBJC_IVAR_$_PIInpaintCacheNode._cacheKey
+ OBJC_IVAR_$_PIInpaintCacheNode._inpaintQueue
+ OBJC_IVAR_$_PIInpaintCacheNode._inputImage
+ OBJC_IVAR_$_PIInpaintCacheNode._inputRegion
+ OBJC_IVAR_$_PIInpaintCacheNode._operations
+ OBJC_IVAR_$_PIInpaintCacheNode._outputImage
+ OBJC_IVAR_$_PIInpaintCacheNode._outputRegion
+ OBJC_IVAR_$_PIInpaintCacheNode._sourceIsHDR
+ OBJC_IVAR_$_PIInpaintCacheNode._sourceOrientation
+ _OBJC_CLASS_$_NUImageLayout
+ _OBJC_CLASS_$_NUMemoryProviderCacheNode
+ _OBJC_CLASS_$_NURenderer
- OBJC_IVAR_$_PIInpaintSourceNode._cacheKey
- OBJC_IVAR_$_PIInpaintSourceNode._operations
- OBJC_IVAR_$_PIInpaintSourceNode._renderedImage
- OBJC_IVAR_$_PIInpaintSourceNode._retouchImage
- _OBJC_CLASS_$_PIInpaintSourceNode
- _OBJC_CLASS_$_PIInpaintSubsampleSourceNode
- _OBJC_METACLASS_$_PIInpaintSourceNode
- _OBJC_METACLASS_$_PIInpaintSubsampleSourceNode
CStrings:
+ "\x16!\x13\x1a"
+ "+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:renderer:error:]"
+ "-[PIInpaintCacheNode _applyInpaintOperation:toImage:operationIndex:renderer:error:]"
+ "-[PIInpaintCacheNode _newMaskImageFromIdentifiers:useSourceImage:error:]"
+ "-[PIInpaintCacheNode _renderWithBackgroundImage:error:]"
+ "-[PIInpaintCacheNode newExclusionMaskImageForOperation:inputImage:error:]"
+ "-[PIInpaintSubsampleCacheNode compositeNode]"
+ "-[PIInpaintSubsampleCacheNode inpaintNode]"
+ "@40@0:8{?=qq}16@32"
+ "A2RGB10"
+ "B24@?0d8d16"
+ "Failed to read buffer"
+ "Failed to render inpaint background"
+ "Failed to render inpaint operations:@"
+ "Failed to render: %!{(MISSING)public}@"
+ "No input image!"
+ "PI_SENSITIVITY_V2_THRESHOLDS"
+ "T@\"NSCache\",R"
+ "T@\"NSDictionary\",C,N,V_inputExtendedStatistics"
+ "Unexpected input node: %!@(MISSING)"
+ "_applyInpaintOperation:toImage:operationIndex:renderer:error:"
+ "_computeBaseIdentifier"
+ "_inpaintQueue"
+ "_inputExtendedStatistics"
+ "_renderBackgroundImage:intoMutableBuffer:renderer:error:"
+ "_renderWithBackgroundImage:error:"
+ "_sourceIsHDR"
+ "_sourceOrientation"
+ "applyInpaintOperations:toImage:renderer:error:"
+ "bufferImageWithLayout:format:colorSpace:"
+ "bufferStoragePool"
+ "compositeNode"
+ "currentSensitivityExceedsThresholdsV1:initialSensitivity:"
+ "currentSensitivityExceedsThresholdsV2:initialSensitivity:"
+ "extendedStats"
+ "hasCICP"
+ "i16@?0d8"
+ "includesRect:"
+ "initWithCIContext:priority:"
+ "inpaintInputNode"
+ "inpaintNode"
+ "inputExtendedStatistics"
+ "intermediateCache"
+ "isExtended"
+ "ivs.nsfw_explicit"
+ "newImageOfSize:colorSpace:"
+ "newStorageWithMinimumSize:format:"
+ "renderImage:intoMutableBuffer:destinationBounds:renderer:error:"
+ "sensitivityCheckVersion2Thresholds"
+ "setInputExtendedStatistics:"
+ "setInputStatisticsByStatsKey:"
+ "setSensitivityCheckVersion2Thresholds:"
+ "shouldCacheIntermediates"
+ "tiledLayoutForImageSize:tileSize:"
+ "tryLoad:"
+ "wantsDependentJob"
+ "xstats"
- "\x16!\x12\x1b"
- "%!@(MISSING)-newRequest s:%!l(MISSING)d"
- "%!@(MISSING)-setup s:%!l(MISSING)d"
- "+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:context:error:]"
- "-[PIInpaintCacheNode _resolveSourceWithResponse:]"
- "-[PIInpaintCacheNode _setupRenderRequest:error:]"
- "-[PIInpaintCacheNode newRenderRequestWithOriginalRequest:error:]"
- "-[PIInpaintSourceNode _applyInpaintOperation:toImage:operationIndex:context:error:]"
- "-[PIInpaintSourceNode _newMaskImageFromIdentifiers:useSourceImage:error:]"
- "-[PIInpaintSourceNode initWithImage:identifier:orientation:]"
- "-[PIInpaintSourceNode initWithImage:settings:orientation:]"
- "-[PIInpaintSourceNode initWithInputImage:inpaintOperations:maskNodes:sourceOrientation:isHDR:cacheKey:]"
- "-[PIInpaintSourceNode newExclusionMaskImageForOperation:inputImage:error:]"
- "-[PIInpaintSubsampleCacheNode _updateInputRegion:outputRegion:forOperation:geometry:error:]"
- "@60@0:8@16@24@32q40B48@52"
- "Error retrieving image properties for source orientation: %!@(MISSING)"
- "Failed to generate inpaint render request"
- "Failed to load inpaint geometry, error: %!{(MISSING)public}@"
- "Inpaint intermediate #%!d(MISSING) cache hit [partial] (operation #%!d(MISSING) out of %!d(MISSING)), invalid region: %!@(MISSING)"
- "Missing input inpaint region"
- "PIInpaintRendering-renderImageIntoMutableBuffer"
- "PIInpaintSourceNode"
- "PIInpaintSubsampleSourceNode"
- "T@\"NSDictionary\",R,C,N,V_maskNodes"
- "T@\"NSNumber\",C,N,V_personMasksValidHint"
- "_applyInpaintOperation:toImage:operationIndex:context:error:"
- "_baseOperationIndex"
- "_maskNodes"
- "_personMasksValidHint"
- "applyInpaintOperations:toImage:error:"
- "initWithInputImage:inpaintOperations:maskNodes:sourceOrientation:isHDR:cacheKey:"
- "maskNodes"
- "personMasksValidHint"
- "renderImage:intoMutableBuffer:destinationBounds:context:error:"
- "resolveWithInputImage:inpaintOperations:cacheKey:"
- "setPersonMasksValidHint:"
- "sourceOrientation"

```
