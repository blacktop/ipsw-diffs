## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x1e46c
-  __TEXT.__objc_methlist: 0x1ff4
+916.51.202.0.0
+  __TEXT.__text: 0x1e9c8
+  __TEXT.__objc_methlist: 0x2004
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x5c0
-  __TEXT.__cstring: 0x5ae4
-  __TEXT.__oslogstring: 0x292c
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__cstring: 0x5c3d
+  __TEXT.__oslogstring: 0x2985
+  __TEXT.__unwind_info: 0x920
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcf8
+  __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16f0
+  __DATA_CONST.__objc_selrefs: 0x16f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x5a8
+  __DATA_CONST.__objc_arraydata: 0x5b8
   __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3520
+  __AUTH_CONST.__cfstring: 0x35c0
   __AUTH_CONST.__objc_const: 0x30d8
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x26c
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 732
-  Symbols:   1536
-  CStrings:  631
+  Functions: 736
+  Symbols:   1542
+  CStrings:  637
 
Symbols:
+ -[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]
+ -[PHMediaFormatConversionRequest _provenanceRenderOutputType]
+ -[PHMediaFormatConversionRequest provenanceRenderSourceURL]
+ -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withUnprocessedSourceRenderURL:processedOriginalDestinationURL:sidecarURL:]
+ GCC_except_table142
+ GCC_except_table157
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table561
+ GCC_except_table569
+ GCC_except_table599
+ GCC_except_table601
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table694
+ GCC_except_table696
+ GCC_except_table709
+ GCC_except_table97
+ GCC_except_table99
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceRenderSourceURL
+ _PAMediaConversionErrorIsProvenanceProcessingError
+ _PAMediaConversionIsProvenanceClientUpgradeRequiredError
+ _PAMediaConversionServiceProvenanceRetryableKey
+ _PAProvenanceCloudAppErrorIsTransient
+ _PFErrorOrUnderlyingErrorMatchesCodesByDomain
+ ___157-[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]_block_invoke
- -[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]
- -[PHMediaFormatConversionRequest provenanceAdjustedRenderSourceURL]
- -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:]
- GCC_except_table139
- GCC_except_table154
- GCC_except_table156
- GCC_except_table158
- GCC_except_table171
- GCC_except_table177
- GCC_except_table424
- GCC_except_table426
- GCC_except_table557
- GCC_except_table565
- GCC_except_table595
- GCC_except_table597
- GCC_except_table685
- GCC_except_table687
- GCC_except_table690
- GCC_except_table692
- GCC_except_table705
- GCC_except_table94
- GCC_except_table96
- _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceAdjustedRenderSourceURL
- ___165-[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]_block_invoke
CStrings:
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppCaptureUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppClientVersionUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceDestinationFormatUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceRevocationCheckClientUpgradeRequired"
+ "PAMediaConversionServiceProvenanceRetryableKey"
+ "Render path extension (%@) is not a known UTType. Falling back to the conversion source's format."
+ "Requesting single-pass Provenance processing with render. Source: %@, destination: %@."
- "Requesting single-pass Provenance processing with adjusted render. Source: %@, destination: %@."
```
