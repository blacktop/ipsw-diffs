## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1c66fc
-  __TEXT.__auth_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x122d8
-  __TEXT.__const: 0x1e98
-  __TEXT.__gcc_except_tab: 0x7b04
-  __TEXT.__cstring: 0x22592
-  __TEXT.__oslogstring: 0x2f60
+720.4.101.0.0
+  __TEXT.__text: 0x1c5f74
+  __TEXT.__auth_stubs: 0x1bb0
+  __TEXT.__objc_methlist: 0x12280
+  __TEXT.__const: 0x1e58
+  __TEXT.__gcc_except_tab: 0x7b00
+  __TEXT.__cstring: 0x22432
+  __TEXT.__oslogstring: 0x30f7
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0x5520
-  __TEXT.__objc_classname: 0x2dc0
-  __TEXT.__objc_methname: 0x1f254
-  __TEXT.__objc_methtype: 0x543e
+  __TEXT.__unwind_info: 0x5518
+  __TEXT.__objc_classname: 0x2d9a
+  __TEXT.__objc_methname: 0x1f232
+  __TEXT.__objc_methtype: 0x543c
   __TEXT.__objc_stubs: 0x17f60
-  __DATA_CONST.__got: 0x18b8
-  __DATA_CONST.__const: 0x2310
-  __DATA_CONST.__objc_classlist: 0xde0
-  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__got: 0x18a8
+  __DATA_CONST.__const: 0x22e8
+  __DATA_CONST.__objc_classlist: 0xdd8
+  __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7738
+  __DATA_CONST.__objc_selrefs: 0x7740
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x9d8
+  __DATA_CONST.__objc_superrefs: 0x9d0
   __DATA_CONST.__objc_arraydata: 0x948
-  __AUTH_CONST.__auth_got: 0xdf8
-  __AUTH_CONST.__const: 0x2da8
-  __AUTH_CONST.__cfstring: 0x103e0
-  __AUTH_CONST.__objc_const: 0x26378
-  __AUTH_CONST.__objc_intobj: 0x7f8
+  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__const: 0x2dc8
+  __AUTH_CONST.__cfstring: 0x10340
+  __AUTH_CONST.__objc_const: 0x262a8
+  __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0xc0

   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x278
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x8110
+  __DATA_DIRTY.__objc_data: 0x80c0
   __DATA_DIRTY.__bss: 0x188
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7105
-  Symbols:   8974
-  CStrings:  10997
+  Functions: 7101
+  Symbols:   8960
+  CStrings:  10995
 
Symbols:
- _CMPhotoDecompressionContainerCreateImageForIndex
- _NUCMPhotoAuxiliaryImageTypeURN_DeltaMapNew
- _NUCMPhotoAuxiliaryImageTypeURN_LinearThumbnailNew
- _NUCMPhotoAuxiliaryImageTypeURN_OriginalThumbnail
- _NeutrinoCoreVersionNumber
- _NeutrinoCoreVersionString
- _OBJC_CLASS_$_CIRenderTask
- _OBJC_CLASS_$_NUStyleTransferOriginalNode
- _OBJC_METACLASS_$_NUStyleTransferOriginalNode
- _kCMPhotoDecompressionOption_TiledDownsampling
CStrings:
+ "\x012\x12\x11!"
+ " sourceSampleDataTrackIDs: %!@(MISSING)"
+ "+[NURenderNode(Resampling) resampleImage:by:sampleMode:extent:colorSpace:]"
+ "@88@0:8@16{?=qq}24q40{?={?=qq}{?=qq}}48@80"
+ "Failed to color match input image to color space: %!{(MISSING)public}@"
+ "Failed to color match output image to color space: %!{(MISSING)public}@"
+ "Failed to load image properties for rescaling, error: %!@(MISSING)"
+ "NUPixelRectIsEmpty(extent) == NO"
+ "Registered model for key: %!{(MISSING)public}@"
+ "Resampling"
+ "TB,N,V_includeSemanticStyleTracks"
+ "Unregistered model for key: %!{(MISSING)public}@"
+ "[NUVideoCompositor videoMetadataSamplesFromRequest] skipping metadata sample. metadataGroup is nil for trackID %!d(MISSING) (%!{(MISSING)public}@),\n DebugInfo: %!{(MISSING)public}@"
+ "_includeSemanticStyleTracks"
+ "hasCICP"
+ "includeSemanticStyleTracks"
+ "isCompatibleWithVersion:"
+ "metadataTrackContainsSemanticStyleData:"
+ "requiredSourceSampleDataTrackIDs: %!@(MISSING)"
+ "resampleImage:by:sampleMode:extent:colorSpace:"
+ "resamplingColorSpace"
+ "setIncludeSemanticStyleTracks:"
- "\x013\x12\x11!"
- "-[CIRenderTask(NUCoreImageUtilities) nu_waitUntilCompletedAndReturnError:]"
- "-[NUAbstractScaleNode _scaleImage:by:sampleMode:extent:error:]"
- "-[NUStyleTransferOriginalNode initWithInput:settings:]"
- "-[NUStyleTransferOriginalNode initWithSettings:inputs:]"
- "@88@0:8@16{?=qq}24q40{?={?=qq}{?=qq}}48o^@80"
- "Failed to load image properties for rescaling"
- "Failed to read auxiliary image"
- "Failed to read auxiliary image size"
- "FlexRange"
- "NUCoreImageUtilities"
- "NUStyleTransferOriginalNode"
- "NU_STYLES_SHOULD_REVERT"
- "OriginalThumbnail"
- "T@\"NSDictionary\",&,N,V_originalThumbnailDictionary"
- "_originalThumbnailDictionary"
- "_scaleImage:by:sampleMode:extent:error:"
- "nu_waitUntilCompletedAndReturnError:"
- "originalThumbnailDictionary"
- "setOriginalThumbnailDictionary:"
- "setShouldRevertStyledOriginalIfPossible:"
- "shouldRevertStyledOriginalIfPossible"
- "tag:apple.com,2023:photo:aux:deltamap"
- "urn:com:apple:photo:2023:aux:linearthumbnail"
- "urn:com:apple:photo:2023:aux:originalthumbnail"

```
